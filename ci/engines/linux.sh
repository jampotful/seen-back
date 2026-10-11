#!/usr/bin/env bash
# The engines job on Linux, one part per job (PART=chromium or PART=firefox-webkit):
#  1. test/rec/check_rec.js, every check, against the stand-in model, and its parity check against a real slot (ci/engines/rec_setup.sh)
#  2. the page's self-test (?selftest=1) with the recognizer phase on that slot, at a phone and a desktop size
# Firefox runs headed on a virtual display (Xvfb, Mesa llvmpipe), as headless Firefox has no WebGL here. Everything goes into out/log.txt.
set -uo pipefail
ROOT="$PWD"; OUT="$ROOT/out"; mkdir -p "$OUT/shots" "$OUT/reports" "$OUT/rec"
exec > >(tee -a "$OUT/log.txt") 2>&1
step() { echo; echo "=== $(date -u +%T) $*"; }
PART="${PART:-chromium}"; PW=/tmp/pw; PWV=1.56.0
case "${GITHUB_REF_NAME:-}" in run/engines/linux-probe*) PROBE_ONLY=1 ;; *) PROBE_ONLY=0 ;; esac   # only rec_probe.js in WebKit, with and without phone emulation
case "${GITHUB_REF_NAME:-}" in run/engines/linux-thr*) THR_ONLY=1 ;; *) THR_ONLY=0 ;; esac   # only the threads experiment (ci/engines/threads.sh)
case "${GITHUB_REF_NAME:-}" in run/engines/linux-b7*) NO_ST=1 ;; *) NO_ST=0 ;; esac   # the build's checks (check_rec.js, parity, probes, threads) without the self-test, for time
if [ "$PROBE_ONLY" = 1 ] && [ "$PART" = chromium ]; then echo "probe-only run: nothing for the chromium part"; exit 0; fi
case "$PART" in chromium) BROWSERS="chromium" ;; *) BROWSERS="firefox webkit" ;; esac

step "machine"; uname -a; nproc; free -m | head -2; node --version; python3 --version; lscpu | grep -E "Model name|Flags" | sed -E "s/(Flags:).*/\1 $(grep -o -w -E "avx2|avx512f|avx512_vnni|avx_vnni|avx512bw" /proc/cpuinfo | sort -u | tr "\n" " ")/"
step "build, with ci/engines/patches/build-selftest-on-demand.patch where build.py does not carry it yet (the self-test becomes selftest.js, fetched only for ?selftest=1)"
if [ "${SELFTEST_INLINE:-0}" != 1 ] && git apply --check ci/engines/patches/build-selftest-on-demand.patch 2>/dev/null; then git apply ci/engines/patches/build-selftest-on-demand.patch && echo "build.py patched"; fi
python3 -I build.py && node --check dist/app.js && { [ ! -f selftest.js ] || node --check selftest.js; } && echo "build ok"; ls -l index.html selftest.js 2>&1 | awk '{print $5, $NF}'
step "playwright $PWV: $BROWSERS"
mkdir -p "$PW" && (cd "$PW" && npm init -y >/dev/null && npm install --no-audit --no-fund "playwright@$PWV" 2>&1 | tail -1)
export NODE_PATH="$PW/node_modules"
node "$PW/node_modules/playwright/cli.js" install --with-deps $BROWSERS 2>&1 | grep -v -E "[0-9]+%" | tail -6
if [ "$PART" != chromium ]; then sudo apt-get install -y -qq xvfb libegl1 libegl-mesa0 libgl1-mesa-dri libgles2 >/dev/null 2>&1; echo "mesa and xvfb: exit $?"; fi
python3 -m venv /tmp/venv && /tmp/venv/bin/pip install -q pillow
if [ "$THR_ONLY" = 1 ]; then ENGINES="$BROWSERS" OUT="$OUT" bash ci/engines/threads.sh; exit 0; fi
case "${GITHUB_REF_NAME:-}" in run/engines/linux-sw5*) ENGINES="$BROWSERS" OUT="$OUT" bash ci/engines/sw5xx.sh; exit 0 ;; esac   # only ci/engines/patches/sw-5xx-kept.patch, proven
if [ "$PROBE_ONLY" = 1 ]; then
  PORT=8782 node test/rec/serve.js 8782 > "$OUT/rec-serve-log.txt" 2>&1 &
  sleep 1; curl -s -o /dev/null -w "8782 -> %{http_code}\n" http://127.0.0.1:8782/index.html
  for PH1 in 1 2; do
    step "rec_probe.js in WebKit, PHONE=$PH1"
    PHONE=$PH1 BROWSER=webkit PORT=8782 timeout 400 node test/engines/rec_probe.js > "$OUT/rec/probe-webkit-phone$PH1.json" 2>&1; echo "probe: exit $?"; python3 -I -c "
import json,sys
d=json.load(open(sys.argv[1])); print('phone', d.get('phone'), '| offline', json.dumps(d.get('offline'))[:300]); print('keptBad', json.dumps(d.get('keptBad'))[:600]); print('error', d.get('error'))" "$OUT/rec/probe-webkit-phone$PH1.json"
  done
  exit 0
fi
case "${GITHUB_REF_NAME:-}" in run/engines/linux-svc*)    # only check_rec.js service, with ci/engines/patches/check_rec-quiet-cors.patch (each engine's own words for a refused CORS request)
  git apply ci/engines/patches/check_rec-quiet-cors.patch && echo "patch applied"
  PORT=8782 node test/rec/serve.js 8782 > "$OUT/rec-serve-log.txt" 2>&1 & sleep 1
  for B in $BROWSERS; do
    step "check_rec.js service, patched: $B"
    if [ "$B" = firefox ]; then NODE_PATH="$ROOT/ci/engines/pwshim:$PW/node_modules" PW_REAL="$PW/node_modules/playwright" PW_HEADED=1 LIBGL_ALWAYS_SOFTWARE=1 BROWSER=$B PORT=8782 \
      timeout 900 xvfb-run -a -s "-screen 0 1400x1000x24" node test/rec/check_rec.js service > "$OUT/rec/svc-$B.json" 2> "$OUT/rec/svc-$B.err.txt"
    else BROWSER=$B PORT=8782 timeout 900 node test/rec/check_rec.js service > "$OUT/rec/svc-$B.json" 2> "$OUT/rec/svc-$B.err.txt"; fi
    echo "check_rec service $B: exit $?"; tail -1 "$OUT/rec/svc-$B.json"; tail -c 300 "$OUT/rec/svc-$B.err.txt"
  done
  git checkout -q test/rec/check_rec.js; exit 0 ;;
esac
step "a real slot and its photos"; bash ci/engines/rec_setup.sh
PH=$(ls ci-rec/photos | sed 's#^#ci-rec/photos/#' | paste -sd, -)
RECQ="&rec=ci-rec/slot&recphotos=$PH&recexpect=ci-rec/slot/expect.json"
step "servers: the self-test's on 8781, the recognizer checks' own on 8782"
python3 -I ci/engines/serve.py 8781 "$ROOT" "$OUT/reports" > "$OUT/serve-log.txt" 2>&1 &
PORT=8782 node test/rec/serve.js 8782 > "$OUT/rec-serve-log.txt" 2>&1 &
sleep 1; curl -s -o /dev/null -w "8781 -> %{http_code}\n" http://127.0.0.1:8781/index.html; curl -s -o /dev/null -w "8782 -> %{http_code}\n" http://127.0.0.1:8782/index.html

for B in $BROWSERS; do
  step "check_rec.js, every check, stand-in model: $B"
  t0=$(date +%s)
  if [ "$B" = firefox ]; then
    NODE_PATH="$ROOT/ci/engines/pwshim:$PW/node_modules" PW_REAL="$PW/node_modules/playwright" PW_HEADED=1 LIBGL_ALWAYS_SOFTWARE=1 BROWSER=$B PORT=8782 \
      timeout 1500 xvfb-run -a -s "-screen 0 1400x1000x24" node test/rec/check_rec.js > "$OUT/rec/check_rec-$B.json" 2> "$OUT/rec/check_rec-$B.err.txt"
  else
    BROWSER=$B PORT=8782 timeout 1500 node test/rec/check_rec.js > "$OUT/rec/check_rec-$B.json" 2> "$OUT/rec/check_rec-$B.err.txt"
  fi
  echo "check_rec $B: exit $? in $(( $(date +%s) - t0 )) s"; tail -1 "$OUT/rec/check_rec-$B.json"; tail -c 400 "$OUT/rec/check_rec-$B.err.txt"
  mkdir -p "$OUT/rec/shots-$B"; cp test/rec/shots/*.png "$OUT/rec/shots-$B/" 2>/dev/null; rm -rf test/rec/shots
  step "check_rec.js parity, real slot (tinyclip-8m-16): $B"
  t0=$(date +%s)
  if [ "$B" = firefox ]; then
    NODE_PATH="$ROOT/ci/engines/pwshim:$PW/node_modules" PW_REAL="$PW/node_modules/playwright" PW_HEADED=1 LIBGL_ALWAYS_SOFTWARE=1 BROWSER=$B PORT=8782 SLOT=ci-rec/slot PHOTOS="$ROOT/ci-rec/photos" \
      timeout 900 xvfb-run -a -s "-screen 0 1400x1000x24" node test/rec/check_rec.js parity > "$OUT/rec/parity-real-$B.json" 2> "$OUT/rec/parity-real-$B.err.txt"
  else
    BROWSER=$B PORT=8782 SLOT=ci-rec/slot PHOTOS="$ROOT/ci-rec/photos" timeout 900 node test/rec/check_rec.js parity > "$OUT/rec/parity-real-$B.json" 2> "$OUT/rec/parity-real-$B.err.txt"
  fi
  echo "parity (real) $B: exit $? in $(( $(date +%s) - t0 )) s"; tail -1 "$OUT/rec/parity-real-$B.json"; tail -c 400 "$OUT/rec/parity-real-$B.err.txt"
  if git apply --check ci/engines/patches/check_rec-int8-cosine.patch 2>/dev/null; then
    step "check_rec.js parity, real slot, with ci/engines/patches/check_rec-int8-cosine.patch applied: $B"
    git apply ci/engines/patches/check_rec-int8-cosine.patch && echo "patch applied"
    if [ "$B" = firefox ]; then
      NODE_PATH="$ROOT/ci/engines/pwshim:$PW/node_modules" PW_REAL="$PW/node_modules/playwright" PW_HEADED=1 LIBGL_ALWAYS_SOFTWARE=1 BROWSER=$B PORT=8782 SLOT=ci-rec/slot PHOTOS="$ROOT/ci-rec/photos" \
        timeout 900 xvfb-run -a -s "-screen 0 1400x1000x24" node test/rec/check_rec.js parity > "$OUT/rec/parity-real-patched-$B.json" 2> "$OUT/rec/parity-real-patched-$B.err.txt"
    else
      BROWSER=$B PORT=8782 SLOT=ci-rec/slot PHOTOS="$ROOT/ci-rec/photos" timeout 900 node test/rec/check_rec.js parity > "$OUT/rec/parity-real-patched-$B.json" 2> "$OUT/rec/parity-real-patched-$B.err.txt"
    fi
    echo "parity (real, patched) $B: exit $?"; tail -1 "$OUT/rec/parity-real-patched-$B.json"; git checkout -q test/rec/check_rec.js
  else echo "(ci/engines/patches/check_rec-int8-cosine.patch is already in test/rec/check_rec.js on this commit)"; fi
  if [ "$B" = webkit ]; then
    step "rec_probe.js: the offline second visit without Playwright's offline switch, and a kept model that is not a model: $B"
    BROWSER=$B PORT=8782 timeout 400 node test/engines/rec_probe.js > "$OUT/rec/probe-$B.json" 2>&1; echo "probe: exit $?"; head -c 3000 "$OUT/rec/probe-$B.json"
    step "offline_repeat.js: the offline case again and again, with and without phone emulation, and what Cache Storage holds when it fails: $B"
    BROWSER=$B PORT=8782 TRIALS=6 VARIANTS=desk,phone timeout 900 node test/engines/offline_repeat.js > "$OUT/rec/offline-repeat-$B.json" 2> "$OUT/rec/offline-repeat-$B.err.txt"; echo "offline_repeat: exit $?"
    python3 -I -c "
import json,sys
d=json.load(open(sys.argv[1])); print('failed', d.get('failed'), 'of', len(d.get('trials', [])))
for t in d.get('trials', []): print(t['variant'], t['trial'], json.dumps(t.get('offline'))[:160], '| after', json.dumps(t.get('after'))[:260], '| asked', t.get('asked'), '| errors', json.dumps(t.get('errors'))[:200])" "$OUT/rec/offline-repeat-$B.json"
  fi
  if [ "$NO_ST" = 1 ]; then echo "(no self-test on ${GITHUB_REF_NAME})"; continue; fi
  step "self-test with the recognizer phase: $B (picture limited to 540 on this software renderer)"
  if [ "$B" = firefox ]; then
    LIBGL_ALWAYS_SOFTWARE=1 HEADED=1 TAG=-xvfb PORT=8781 OUT="$OUT/shots" BROWSERS=firefox VIEWPORTS=phone,desktop LABEL=linux-xvfb LIMIT_MS=480000 EXTRA="&side=540$RECQ" \
      xvfb-run -a -s "-screen 0 1400x1000x24" node test/engines/run.js
  else
    PORT=8781 OUT="$OUT/shots" BROWSERS=$B VIEWPORTS=phone,desktop LABEL=linux LIMIT_MS=480000 EXTRA="&side=540$RECQ" node test/engines/run.js
  fi
done

ENGINES="$BROWSERS" OUT="$OUT" bash ci/engines/threads.sh
step "summary"; python3 -I ci/engines/summarize.py "$OUT" "linux-$PART"
step "shrink pictures"; /tmp/venv/bin/python -I ci/engines/shrink.py "$OUT"; du -sh "$OUT"
