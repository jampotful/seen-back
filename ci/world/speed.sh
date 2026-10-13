#!/usr/bin/env bash
# Image encoders timed in headless Chromium through the page's own runtime, one thread and four (tools/world/speed.mjs).
# Called by .github/workflows/worldspeed.yml. Fetches the laboratory's int8 file of each model in MODELS
# (pub/lab-<model>:onnx/vision.int8-per-channel.onnx, the file the pocket slot ships for TinyCLIP 39M/16) and
# Playwright's Chromium, then times every file with every thread count in THREADS.
set -uo pipefail
mkdir -p out models
LOG=out/log.txt
: > "$LOG"
step() {
  local name="$1"; shift
  echo "=== $(date -u +%FT%TZ) $name" | tee -a "$LOG"
  "$@" 2>&1 | tee -a "$LOG"
  local rc=${PIPESTATUS[0]}
  echo "=== $(date -u +%FT%TZ) $name: exit $rc" | tee -a "$LOG"
  return "$rc"
}
MODELS="${MODELS:-tinyclip-39m-16,bioclip-b16}"; PW=/tmp/pw; PWV=1.56.0
step "machine" bash -c 'nproc; free -m | head -2; node --version; lscpu | grep -E "Model name"'
for m in ${MODELS//,/ }; do
  step "int8 file of $m" bash -c "git fetch -q --depth 1 origin pub/lab-$m && git show FETCH_HEAD:onnx/vision.int8-per-channel.onnx > models/$m.onnx && git show FETCH_HEAD:card.json > out/card-$m.json" || exit 1
done
step "the files" bash -c 'ls -l models; sha256sum models/*.onnx; grep -h -o "\"ship_sha256\": \"[0-9a-f]*\"" out/card-*.json'
step "playwright $PWV" bash -c "mkdir -p $PW && cd $PW && npm init -y >/dev/null && npm install --no-audit --no-fund playwright@$PWV 2>&1 | tail -1 && node node_modules/playwright/cli.js install --with-deps chromium 2>&1 | grep -v -E '[0-9]+%' | tail -3" || exit 1
step "time" node tools/world/speed.mjs "$PW" models out/speed.json "${PHOTOS:-30}" "${THREADS:-1,4}" "${ROUNDS:-3}" || exit 1
exit 0
