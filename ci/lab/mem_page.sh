#!/usr/bin/env bash
# The page's own worker in headless Chromium (tools/lab/mem_page.mjs), after ci/lab/mem.sh has put the shipped file in
# model/ and the pixels in pix/. Writes ret/routes/page.json and page.f32.
set -uo pipefail
L=ret/log.txt
say() { echo "[$(date -u +%T)] $*" | tee -a "$L"; }
PW=/tmp/pw; PWV=1.56.0
mkdir -p "$PW" && (cd "$PW" && npm init -y >/dev/null && npm install --no-audit --no-fund "playwright@$PWV" 2>&1 | tail -1) >> "$L" 2>&1
node "$PW/node_modules/playwright/cli.js" install --with-deps chromium 2>&1 | grep -v -E "[0-9]+%" | tail -4 >> "$L"
node test/rec/serve.js 8790 > serve.log 2>&1 & spid=$!
sleep 2
say "page run: the shipped file through vendor/rec-worker.js"
timeout 1200 node tools/lab/mem_page.mjs "$PW" 8790 /model/vision.int8.onnx 24 ret/routes/page.json ret/routes/page.f32 >> "$L" 2>&1 || say "page run failed"
kill "$spid" 2>/dev/null
say "page run done"
