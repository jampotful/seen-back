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
  ff-pwopt) PREFS='{"javascript.options.wasm_optimizingjit":true,"javascript.options.wasm_baselinejit":true}'; CASES="pocket:all:5" ;;
  ff-plain*) CASES="pocket:all:5 big:all:2" ;;
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
# ff-plain: the machine's own Firefox (or Mozilla's latest release), started by hand with no automation attached, on a fresh profile;
# ff-plainpw: Playwright's Firefox started the same way. The page posts its figures to ci/engines/serve.py, case after case.
case "$V" in ff-plain*)
  if [ "$V" = ff-plainpw ]; then FX=$(ls -d "$HOME"/.cache/ms-playwright/firefox-*/firefox/firefox | head -1)
  else FX=$(command -v firefox || true); if [ -z "$FX" ] || ! "$FX" --version > /dev/null 2>&1; then
      curl -s -L -o /tmp/fx.tar.xz 'https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64&lang=en-US' && mkdir -p /tmp/fx && tar -xf /tmp/fx.tar.xz -C /tmp/fx && FX=/tmp/fx/firefox/firefox; fi
  fi
  echo "firefox: $FX, $("$FX" --version 2>&1 | head -1)"
  pkill -f 'python3 -I - 8790' 2>/dev/null; sleep 1
  python3 -I ci/engines/serve.py 8790 "$ROOT" "$OUT/reports" > "$OUT/serve.txt" 2>&1 & sleep 2
  k=0
  for c in $CASES; do
    k=$((k + 1)); IFS=: read -r model opt reps _ <<< "$c"; P=$(mktemp -d /tmp/fxp-XXXX)
    printf '%s\n' 'user_pref("browser.shell.checkDefaultBrowser", false);' 'user_pref("browser.startup.homepage_override.mstone", "ignore");' 'user_pref("datareporting.policy.dataSubmissionEnabled", false);' \
      'user_pref("toolkit.telemetry.reportingpolicy.firstRun", false);' 'user_pref("browser.aboutwelcome.enabled", false);' 'user_pref("app.update.disabledForTesting", true);' > "$P/user.js"
    name="case$k"; url="http://127.0.0.1:8790/test/engines/ffbench.html?model=$model&opt=$opt&reps=$reps&report=$name"
    "$FX" --headless --no-remote --profile "$P" "$url" > "$OUT/fx-$name.txt" 2>&1 & FP=$!
    lim=$([ "$model" = big ] && echo 1200 || echo 300); t=0
    while [ $t -lt $lim ]; do sleep 3; t=$((t + 3)); python3 -I -c "import json,sys; sys.exit(0 if json.load(open(sys.argv[1])).get('done') else 1)" "$OUT/reports/$name.json" 2>/dev/null && break; done
    kill $FP 2>/dev/null; sleep 2; pkill -f "$P" 2>/dev/null
    python3 -I -c "
import json,sys
j=json.load(open(sys.argv[1])); r=j.get('result') or {}; t=r.get('t') or {}
print(sys.argv[2], sys.argv[3], '| fetch', t.get('fetch'), 'ms | session', t.get('session'), 'ms | runs', t.get('runs'), 'ms | head', r.get('head'), 'sum', r.get('sum'), '| error', j.get('error') or '', '| done', j.get('done'), '| features', json.dumps(j.get('features')))" "$OUT/reports/$name.json" "$V" "$c" 2>&1 || echo "$V $c: no report after $t s"
  done
  (top -b -n 1 | head -12) 2>/dev/null; exit 0 ;;
esac
( export BROWSER=$B LABEL=$V OUT="$OUT" SITE=http://127.0.0.1:8790/ CASES="$CASES" PREFS="$PREFS" HEADED=$HEADED; timeout 2400 node test/engines/ffbench.js ); echo "ffbench.js: exit $?"
(top -b -n 1 | head -15) 2>/dev/null
