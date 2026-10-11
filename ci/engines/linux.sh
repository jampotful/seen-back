#!/usr/bin/env bash
# The engines job on Linux: the self-test in Chromium, Firefox and WebKit (Playwright), at a phone and a desktop
# size; in Chromium also the existing checks, installability and the service worker; in Firefox the live camera
# flow with its fake camera. Everything it does goes into out/log.txt.
set -uo pipefail
ROOT="$PWD"; OUT="$ROOT/out"; mkdir -p "$OUT/shots" "$OUT/reports"
exec > >(tee -a "$OUT/log.txt") 2>&1
step() { echo; echo "=== $(date -u +%T) $*"; }
PORT=8781; PW=/tmp/pw; PWV=1.56.0

step "machine"
uname -a; nproc; free -m | head -2; node --version; python3 --version; (lsb_release -ds 2>/dev/null || true)

step "build"
python3 -I build.py && node --check dist/app.js && echo "build ok"

step "playwright $PWV and its browsers"
mkdir -p "$PW" && (cd "$PW" && npm init -y >/dev/null && npm install --no-audit --no-fund "playwright@$PWV" 2>&1 | tail -2)
export NODE_PATH="$PW/node_modules"
node "$PW/node_modules/playwright/cli.js" install --with-deps chromium firefox webkit 2>&1 | grep -v -E "^\s*\|?[■ ]*\|? *[0-9]+%" | tail -25

step "ffmpeg and Pillow"
command -v ffmpeg >/dev/null || (sudo apt-get update -qq && sudo apt-get install -y -qq ffmpeg >/dev/null 2>&1)
ffmpeg -hide_banner -version | head -1
python3 -m venv /tmp/venv && /tmp/venv/bin/pip install -q pillow && echo "pillow ok"

step "serve the repository on 127.0.0.1:$PORT"
python3 -I ci/engines/serve.py "$PORT" "$ROOT" "$OUT/reports" > "$OUT/serve-log.txt" 2>&1 &
sleep 1; curl -s -o /dev/null -w "index.html -> %{http_code}\n" "http://127.0.0.1:$PORT/index.html"

step "self-test: chromium, firefox, webkit x phone, desktop"
PORT=$PORT OUT="$OUT/shots" BROWSERS=chromium,firefox,webkit VIEWPORTS=phone,desktop LABEL=linux LIMIT_MS=240000 node test/engines/run.js

step "existing checks in Chromium (test/check4.js, unchanged)"
sh tools/make_test_media.sh
for m in lex record viewer edge sweep; do
  t0=$(date +%s)
  PORT=$PORT timeout 400 node test/check4.js "$m" > "$OUT/check4-$m.json" 2> "$OUT/check4-$m.err.txt"
  echo "check4 $m: exit $? in $(( $(date +%s) - t0 )) s"
  tail -c 600 "$OUT/check4-$m.err.txt"
done
mkdir -p "$OUT/check4-shots"; cp test/shots4/S-*.png test/shots4/R7-*.png test/shots4/V1-*.png "$OUT/check4-shots/" 2>/dev/null || true

step "summary"
python3 -I ci/engines/summarize.py "$OUT" linux
step "shrink pictures"
/tmp/venv/bin/python -I ci/engines/shrink.py "$OUT"
du -sh "$OUT"
