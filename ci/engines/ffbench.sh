#!/usr/bin/env bash
# The recognizer's runtime alone in Firefox (run/engines/ffx-*, docs/ENGINES.md, the Firefox section): test/engines/ffbench.js on
# test/engines/ffbench.html, served from this commit. V names the variant; each variant is one job of its own on a fresh machine.
set -uo pipefail
ROOT="$PWD"; OUT="$ROOT/out"; mkdir -p "$OUT"
exec > >(tee -a "$OUT/log.txt") 2>&1
step() { echo; echo "=== $(date -u +%T) $*"; }
PW=/tmp/pw; PWV=1.56.0; V="${V:-ff-default}"
step "machine ($V)"; uname -a; free -m; nproc; grep -m1 'model name' /proc/cpuinfo; grep -m1 flags /proc/cpuinfo | tr ' ' '\n' | grep -E '^(avx|avx2|avx512f|avx512_vnni|avx_vnni|fma|sse4_1|sse4_2|ssse3)$' | tr '\n' ' '; echo
step "playwright $PWV"
mkdir -p "$PW" && (cd "$PW" && npm init -y >/dev/null && npm install --no-audit --no-fund "playwright@$PWV" 2>&1 | tail -1)
export NODE_PATH="$PW/node_modules"
B=firefox; case "$V" in chromium*) B=chromium ;; esac
for t in 1 2; do timeout 300 node "$PW/node_modules/playwright/cli.js" install --with-deps $B > "$OUT/install-$B.txt" 2>&1 && break; done
HEADED=0; PREFS='{}'; COI=0; BIG="big:all:2"
case "$V" in
  ff-default|chromium) CASES="pocket:all:5 $BIG" ;;
  ff-headed) HEADED=1; CASES="pocket:all:5 $BIG" ;;
  ff-ion) PREFS='{"javascript.options.wasm_baselinejit":false}'; CASES="pocket:all:5 $BIG" ;;
  ff-base) PREFS='{"javascript.options.wasm_optimizingjit":false}'; CASES="pocket:all:3" ;;
  ff-lazy) PREFS='{"javascript.options.wasm_lazy_tiering":false}'; CASES="pocket:all:5 $BIG" ;;
  ff-opt) CASES="pocket:disabled:4 pocket:basic:4 pocket:extended:4 big:basic:2" ;;
  ff-wb) CASES="pocket:all:5:wb big:all:2:wb" ;;
  ff-coi) COI=1; CASES="pocket:all:5:t4 big:all:2:t4" ;;
  *) CASES="pocket:all:3" ;;
esac
if [ "$HEADED" = 1 ]; then sudo apt-get install -y -q xvfb > /dev/null 2>&1; Xvfb :99 -screen 0 1280x1024x24 > /dev/null 2>&1 & export DISPLAY=:99; sleep 1; fi
python3 -I - 8790 "$ROOT" "$COI" > "$OUT/serve.txt" 2>&1 <<'PY' &
import http.server, sys
port, root, coi = int(sys.argv[1]), sys.argv[2], sys.argv[3] == '1'
class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k): super().__init__(*a, directory=root, **k)
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        if coi:
            self.send_header('Cross-Origin-Opener-Policy', 'same-origin'); self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        super().end_headers()
    def log_message(self, *a): pass
http.server.ThreadingHTTPServer(('127.0.0.1', port), H).serve_forever()
PY
sleep 2
step "variant $V: $B, headed $HEADED, prefs $PREFS, cases $CASES"
( export BROWSER=$B LABEL=$V OUT="$OUT" SITE=http://127.0.0.1:8790/ CASES="$CASES" PREFS="$PREFS" HEADED=$HEADED; timeout 2400 node test/engines/ffbench.js ); echo "ffbench.js: exit $?"
(top -b -n 1 | head -15) 2>/dev/null
