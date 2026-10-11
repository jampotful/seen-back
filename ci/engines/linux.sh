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
case "$PART" in chromium) BROWSERS="chromium" ;; *) BROWSERS="firefox webkit" ;; esac

step "machine"; uname -a; nproc; free -m | head -2; node --version; python3 --version
step "build"; python3 -I build.py && node --check dist/app.js && echo "build ok"
step "playwright $PWV: $BROWSERS"
mkdir -p "$PW" && (cd "$PW" && npm init -y >/dev/null && npm install --no-audit --no-fund "playwright@$PWV" 2>&1 | tail -1)
export NODE_PATH="$PW/node_modules"
node "$PW/node_modules/playwright/cli.js" install --with-deps $BROWSERS 2>&1 | grep -v -E "[0-9]+%" | tail -6
if [ "$PART" != chromium ]; then sudo apt-get install -y -qq xvfb libegl1 libegl-mesa0 libgl1-mesa-dri libgles2 >/dev/null 2>&1; echo "mesa and xvfb: exit $?"; fi
python3 -m venv /tmp/venv && /tmp/venv/bin/pip install -q pillow
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
  step "self-test with the recognizer phase: $B (picture limited to 540 on this software renderer)"
  if [ "$B" = firefox ]; then
    LIBGL_ALWAYS_SOFTWARE=1 HEADED=1 TAG=-xvfb PORT=8781 OUT="$OUT/shots" BROWSERS=firefox VIEWPORTS=phone,desktop LABEL=linux-xvfb LIMIT_MS=480000 EXTRA="&side=540$RECQ" \
      xvfb-run -a -s "-screen 0 1400x1000x24" node test/engines/run.js
  else
    PORT=8781 OUT="$OUT/shots" BROWSERS=$B VIEWPORTS=phone,desktop LABEL=linux LIMIT_MS=480000 EXTRA="&side=540$RECQ" node test/engines/run.js
  fi
done

step "summary"; python3 -I ci/engines/summarize.py "$OUT" "linux-$PART"
step "shrink pictures"; /tmp/venv/bin/python -I ci/engines/shrink.py "$OUT"; du -sh "$OUT"
