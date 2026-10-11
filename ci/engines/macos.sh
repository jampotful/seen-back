#!/usr/bin/env bash
# The engines job on macOS: the self-test in Playwright's WebKit (the macOS build), then in real Safari through
# safaridriver, then in Safari on an iPhone simulator, which posts its report to the server here.
# Everything it does goes into out/log.txt.
set -uo pipefail
ROOT="$PWD"; OUT="$ROOT/out"; mkdir -p "$OUT/shots" "$OUT/reports" "$OUT/sim"
exec > >(tee -a "$OUT/log.txt") 2>&1
step() { echo; echo "=== $(date -u +%T) $*"; }
# run a command with a time limit (macOS has no `timeout`)
limit() { local s=$1; shift; "$@" & local p=$!; ( sleep "$s"; kill "$p" 2>/dev/null ) & local w=$!; wait "$p"; local rc=$?; kill "$w" 2>/dev/null; return $rc; }
PORT=8781; PW=/tmp/pw; PWV=1.56.0

step "machine"
sw_vers; uname -a; sysctl -n machdep.cpu.brand_string hw.ncpu hw.memsize; xcodebuild -version | tr '\n' ' '; echo
system_profiler SPDisplaysDataType 2>/dev/null | head -30
defaults read /Applications/Safari.app/Contents/Info.plist CFBundleShortVersionString 2>/dev/null | sed 's/^/Safari /'
node --version; python3 --version

step "build"
python3 -I build.py && node --check dist/app.js && echo "build ok"

step "serve the repository on 127.0.0.1:$PORT"
python3 -I ci/engines/serve.py "$PORT" "$ROOT" "$OUT/reports" > "$OUT/serve-log.txt" 2>&1 &
sleep 1; curl -s -o /dev/null -w "index.html -> %{http_code}\n" "http://127.0.0.1:$PORT/index.html"

step "iPhone simulator: boot it now, it takes a while"
xcrun simctl list runtimes | grep -i ios
UDID=$(xcrun simctl list devices available -j | python3 -I -c "
import json, sys
d = json.load(sys.stdin)['devices']
c = sorted((rt, x['udid']) for rt, xs in d.items() for x in xs if x['name'] == 'iPhone 17' and x.get('isAvailable', True))
print(c[-1][1] if c else '')")
echo "iPhone 17: ${UDID:-none found}"
if [ -n "$UDID" ]; then xcrun simctl boot "$UDID" 2>&1; fi

step "playwright $PWV and WebKit"
mkdir -p "$PW" && (cd "$PW" && npm init -y >/dev/null && npm install --no-audit --no-fund "playwright@$PWV" 2>&1 | tail -2)
export NODE_PATH="$PW/node_modules"
node "$PW/node_modules/playwright/cli.js" install webkit 2>&1 | grep -v -E "[0-9]+%" | tail -8

step "self-test: Playwright WebKit (macOS build) x phone, desktop"
PORT=$PORT OUT="$OUT/shots" BROWSERS=webkit VIEWPORTS=phone,desktop LABEL=macos LIMIT_MS=240000 node test/engines/run.js

step "self-test: real Safari through safaridriver"
sudo safaridriver --enable 2>&1; echo "safaridriver --enable: exit $?"
safaridriver -p 4444 > "$OUT/safaridriver-log.txt" 2>&1 &
sleep 2
PORT=$PORT OUT="$OUT/shots" limit 400 node test/engines/safari.js; echo "safari.js: exit $?"

step "iPhone simulator: Safari opens the self-test and posts its report"
if [ -n "$UDID" ]; then
  limit 240 xcrun simctl bootstatus "$UDID" -b 2>&1 | tail -3
  xcrun simctl list devices | grep "$UDID"
  # first the opening screen, as a person sees it (is the WebGL picture on the screen?)
  xcrun simctl openurl "$UDID" "http://127.0.0.1:$PORT/index.html?nosw=1" 2>&1; echo "openurl (opening screen): exit $?"
  sleep 10; xcrun simctl io "$UDID" screenshot "$OUT/sim/iphone-0-open.png" >/dev/null 2>&1
  sleep 4; xcrun simctl io "$UDID" screenshot "$OUT/sim/iphone-0-open-b.png" >/dev/null 2>&1
  xcrun simctl openurl "$UDID" "http://127.0.0.1:$PORT/index.html?selftest=1&nosw=1&report=/report/iphone" 2>&1; echo "openurl: exit $?"
  t0=$(date +%s); n=0
  while [ $(( $(date +%s) - t0 )) -lt 300 ]; do
    sleep 2; n=$((n+1)); el=$(( $(date +%s) - t0 ))
    if [ $n -le 20 ] || [ $((n % 15)) -eq 0 ]; then xcrun simctl io "$UDID" screenshot "$OUT/sim/iphone-$(printf %03d $el)s.png" >/dev/null 2>&1; fi
    if [ -f "$OUT/reports/iphone.json" ] && grep -q '"done":true' "$OUT/reports/iphone.json"; then echo "report arrived after $el s"; sleep 3; xcrun simctl io "$UDID" screenshot "$OUT/sim/iphone-final.png" >/dev/null 2>&1; break; fi
  done
  ls -la "$OUT/reports" "$OUT/sim"
  xcrun simctl spawn "$UDID" log show --last 6m --style compact --predicate 'process == "MobileSafari" OR process CONTAINS "WebContent"' 2>/dev/null | grep -i -E "error|webgl|gpu|crash" | tail -40 > "$OUT/sim/safari-log-tail.txt" || true
  xcrun simctl shutdown "$UDID" 2>&1 || true
fi

step "summary"
python3 -I ci/engines/summarize.py "$OUT" macos
step "shrink pictures"
python3 -m venv /tmp/venv && /tmp/venv/bin/pip install -q pillow && /tmp/venv/bin/python -I ci/engines/shrink.py "$OUT"
du -sh "$OUT"
