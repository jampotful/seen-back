#!/usr/bin/env bash
# The engines job on macOS: test/rec/check_rec.js in Playwright's WebKit (every check on the stand-in, parity on a real slot), then the
# page's self-test with the recognizer phase in Playwright's WebKit, in real Safari through safaridriver, and in Safari on an iPhone
# simulator, which posts its report to the server here. Everything goes into out/log.txt.
set -uo pipefail
ROOT="$PWD"; OUT="$ROOT/out"; mkdir -p "$OUT/shots" "$OUT/reports" "$OUT/sim" "$OUT/rec"
exec > >(tee -a "$OUT/log.txt") 2>&1
step() { echo; echo "=== $(date -u +%T) $*"; }
limit() { local s=$1; shift; "$@" & local p=$!; ( sleep "$s"; kill "$p" 2>/dev/null ) & local w=$!; wait "$p"; local rc=$?; kill "$w" 2>/dev/null; return $rc; }
PW=/tmp/pw; PWV=1.56.0

step "machine"
sw_vers; sysctl -n machdep.cpu.brand_string hw.ncpu hw.memsize; xcodebuild -version | tr '\n' ' '; echo
defaults read /Applications/Safari.app/Contents/Info.plist CFBundleShortVersionString 2>/dev/null | sed 's/^/Safari /'; node --version; python3 --version
step "build, with ci/engines/patches/build-selftest-on-demand.patch where build.py does not carry it yet (the self-test becomes selftest.js, fetched only for ?selftest=1)"
if [ "${SELFTEST_INLINE:-0}" != 1 ] && git apply --check ci/engines/patches/build-selftest-on-demand.patch 2>/dev/null; then git apply ci/engines/patches/build-selftest-on-demand.patch && echo "build.py patched"; fi
python3 -I build.py && node --check dist/app.js && { [ ! -f selftest.js ] || node --check selftest.js; } && echo "build ok"; ls -l index.html selftest.js 2>&1 | awk '{print $5, $NF}'

step "iPhone simulator: boot it now, it takes a while"
UDID=$(xcrun simctl list devices available -j | python3 -I -c "
import json, sys
d = json.load(sys.stdin)['devices']
c = sorted((rt, x['udid']) for rt, xs in d.items() for x in xs if x['name'] == 'iPhone 17' and x.get('isAvailable', True))
print(c[-1][1] if c else '')")
echo "iPhone 17: ${UDID:-none found}"; [ -n "$UDID" ] && xcrun simctl boot "$UDID" 2>&1

step "a real slot and its photos"; bash ci/engines/rec_setup.sh
PH=$(ls ci-rec/photos | sed 's#^#ci-rec/photos/#' | paste -sd, -)
RECQ="&rec=ci-rec/slot&recphotos=$PH&recexpect=ci-rec/slot/expect.json"

step "servers: the self-test's on 8781, the recognizer checks' own on 8782"
python3 -I ci/engines/serve.py 8781 "$ROOT" "$OUT/reports" > "$OUT/serve-log.txt" 2>&1 &
PORT=8782 node test/rec/serve.js 8782 > "$OUT/rec-serve-log.txt" 2>&1 &
sleep 1; curl -s -o /dev/null -w "8781 -> %{http_code}\n" http://127.0.0.1:8781/index.html; curl -s -o /dev/null -w "8782 -> %{http_code}\n" http://127.0.0.1:8782/index.html

step "playwright $PWV and WebKit"
mkdir -p "$PW" && (cd "$PW" && npm init -y >/dev/null && npm install --no-audit --no-fund "playwright@$PWV" 2>&1 | tail -1)
export NODE_PATH="$PW/node_modules"
node "$PW/node_modules/playwright/cli.js" install webkit 2>&1 | grep -v -E "[0-9]+%" | tail -3

step "check_rec.js, every check, stand-in model: webkit (macOS)"
t0=$(date +%s); BROWSER=webkit PORT=8782 limit 1500 node test/rec/check_rec.js > "$OUT/rec/check_rec-webkit.json" 2> "$OUT/rec/check_rec-webkit.err.txt"
echo "check_rec webkit: exit $? in $(( $(date +%s) - t0 )) s"; tail -1 "$OUT/rec/check_rec-webkit.json"; tail -c 400 "$OUT/rec/check_rec-webkit.err.txt"
mkdir -p "$OUT/rec/shots-webkit"; cp test/rec/shots/*.png "$OUT/rec/shots-webkit/" 2>/dev/null; rm -rf test/rec/shots
step "begin_probe.js: what Begin does in macOS WebKit, with and without check_rec.js's phone emulation"
BROWSER=webkit PORT=8782 OUT="$OUT/rec" limit 120 node test/engines/begin_probe.js > "$OUT/rec/begin-probe-webkit.json" 2>&1; echo "begin probe: exit $?"; head -c 4000 "$OUT/rec/begin-probe-webkit.json"
# (run engines/12 ran check_rec.js a second time with locator.tap() made a click: every case still stopped at the same place, so that run is dropped)
step "check_rec.js parity, real slot: webkit (macOS)"
t0=$(date +%s); NODE_PATH="$ROOT/ci/engines/pwshim:$PW/node_modules" PW_REAL="$PW/node_modules/playwright" PW_TAP_AS_CLICK=1 BROWSER=webkit PORT=8782 SLOT=ci-rec/slot PHOTOS="$ROOT/ci-rec/photos" limit 900 node test/rec/check_rec.js parity > "$OUT/rec/parity-real-webkit.json" 2> "$OUT/rec/parity-real-webkit.err.txt"
echo "parity (real) webkit: exit $? in $(( $(date +%s) - t0 )) s"; tail -1 "$OUT/rec/parity-real-webkit.json"; tail -c 400 "$OUT/rec/parity-real-webkit.err.txt"
if git apply --check ci/engines/patches/check_rec-int8-cosine.patch 2>/dev/null; then
  step "check_rec.js parity, real slot, with ci/engines/patches/check_rec-int8-cosine.patch applied: webkit (macOS)"
  git apply ci/engines/patches/check_rec-int8-cosine.patch && echo "patch applied"
  NODE_PATH="$ROOT/ci/engines/pwshim:$PW/node_modules" PW_REAL="$PW/node_modules/playwright" PW_TAP_AS_CLICK=1 BROWSER=webkit PORT=8782 SLOT=ci-rec/slot PHOTOS="$ROOT/ci-rec/photos" limit 900 node test/rec/check_rec.js parity > "$OUT/rec/parity-real-patched-webkit.json" 2> "$OUT/rec/parity-real-patched-webkit.err.txt"
  echo "parity (real, patched) webkit: exit $?"; tail -1 "$OUT/rec/parity-real-patched-webkit.json"; git checkout -q test/rec/check_rec.js
else echo "(ci/engines/patches/check_rec-int8-cosine.patch is already in test/rec/check_rec.js on this commit)"; fi

step "rec_probe.js: the offline second visit without Playwright's offline switch, and a kept model that is not a model: webkit (macOS)"
BROWSER=webkit PORT=8782 limit 400 node test/engines/rec_probe.js > "$OUT/rec/probe-webkit.json" 2>&1; echo "probe: exit $?"; head -c 3000 "$OUT/rec/probe-webkit.json"
step "self-test with the recognizer phase: Playwright WebKit (macOS) x phone, desktop"
PORT=8781 OUT="$OUT/shots" BROWSERS=webkit VIEWPORTS=phone,desktop LABEL=macos LIMIT_MS=300000 EXTRA="$RECQ" node test/engines/run.js

step "self-test with the recognizer phase: real Safari through safaridriver"
sudo safaridriver --enable 2>&1; echo "safaridriver --enable: exit $?"
safaridriver -p 4444 > "$OUT/safaridriver-log.txt" 2>&1 &
sleep 2
PORT=8781 OUT="$OUT/shots" EXTRA="$RECQ" limit 420 node test/engines/safari.js; echo "safari.js: exit $?"

step "iPhone simulator: Safari opens the self-test with the recognizer phase and posts its report"
if [ -n "$UDID" ]; then
  limit 240 xcrun simctl bootstatus "$UDID" -b 2>&1 | tail -2
  xcrun simctl openurl "$UDID" "http://127.0.0.1:8781/index.html?nosw=1" 2>&1; sleep 10
  xcrun simctl io "$UDID" screenshot "$OUT/sim/iphone-0-open.png" >/dev/null 2>&1
  xcrun simctl openurl "$UDID" "http://127.0.0.1:8781/index.html?selftest=1&nosw=1&report=/report/iphone$RECQ" 2>&1; echo "openurl: exit $?"
  t0=$(date +%s); n=0
  while [ $(( $(date +%s) - t0 )) -lt 300 ]; do
    sleep 3; n=$((n+1)); el=$(( $(date +%s) - t0 ))
    if [ $n -le 14 ] || [ $((n % 10)) -eq 0 ]; then xcrun simctl io "$UDID" screenshot "$OUT/sim/iphone-$(printf %03d $el)s.png" >/dev/null 2>&1; fi
    if [ -f "$OUT/reports/iphone.json" ] && grep -q '"done":true' "$OUT/reports/iphone.json"; then echo "report arrived after $el s"; sleep 2; xcrun simctl io "$UDID" screenshot "$OUT/sim/iphone-final.png" >/dev/null 2>&1; break; fi
  done
  ls "$OUT/reports" | tr '\n' ' '; echo
  xcrun simctl shutdown "$UDID" 2>&1 || true
fi

step "summary"; python3 -I ci/engines/summarize.py "$OUT" macos
step "shrink pictures"; python3 -m venv /tmp/venv && /tmp/venv/bin/pip install -q pillow && /tmp/venv/bin/python -I ci/engines/shrink.py "$OUT"; du -sh "$OUT"
