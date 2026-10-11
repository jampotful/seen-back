#!/usr/bin/env bash
# The threads experiment, on a build machine: what cross-origin isolation through the service worker would buy and break.
#   ENGINES="chromium firefox webkit" (Playwright), "safari" (safaridriver on :4444) and/or "sim" (UDID=<booted simulator>)
#   bash ci/engines/threads.sh   (from the repository root; results in out/threads/)
# Three copies of the built page, each served on its own port (so each is its own origin with its own service worker), all with
# ci/engines/patches/threads-rec.patch (the worker takes ?threads=N when the page is isolated):
#   8791 no isolation; 8792 + ci/engines/patches/coi-sw.patch (the service worker adds COOP same-origin and COEP require-corp to
#   everything it answers); 8793 the same with COEP credentialless; 8794 the other origin, a stand-in for raw.githubusercontent.com.
# The server adds test/engines/coi_probe.js to the page; the probe posts its report; threads.js and the simulator loop wait for it.
set -uo pipefail
ROOT="$PWD"; OUT="${OUT:-$ROOT/out}"; R="$OUT/threads"; T="${COI_TMP:-/tmp/coi}"; mkdir -p "$R"
step() { echo; echo "=== $(date -u +%T) $*"; }
ENGINES="${ENGINES:-chromium}"; P0="${COI_P0:-8791}"; P1=$((P0+1)); P2=$((P0+2)); P3=$((P0+3))
export MODES="none:$P0,require-corp:$P1,credentialless:$P2" XORIGIN="http://127.0.0.1:$P3"
step "threads experiment: three copies of the page, patched"
rm -rf "$T"; mkdir -p "$T/base"
tar -C "$ROOT" --exclude=./.git --exclude=./out --exclude=./ci-rec -cf - . | tar -C "$T/base" -xf -
(cd "$T/base" && patch -p1 --forward < "$ROOT/ci/engines/patches/threads-rec.patch" && python3 -I build.py >/dev/null && echo "base: threads patch applied and built") || echo "base: FAILED"
cp -R "$T/base" "$T/rc"
(cd "$T/rc" && patch -p1 --forward < "$ROOT/ci/engines/patches/coi-sw.patch" && python3 -I build.py >/dev/null && grep -c "Cross-Origin-Embedder-Policy" sw.js | sed 's/^/rc: sw.js isolation lines: /') || echo "rc: FAILED"
cp -R "$T/rc" "$T/cl"; sed -i.bak "s/const COEP = 'require-corp';/const COEP = 'credentialless';/" "$T/cl/sw.js" && rm -f "$T/cl/sw.js.bak"; grep -o "const COEP = '[a-z-]*'" "$T/cl/sw.js" "$T/rc/sw.js"
grep -c "threads: +((" "$T/base/index.html" | sed 's/^/base index.html carries the threads switch: /'
step "headers of the other origins a large model or a typeface would come from"
for u in https://raw.githubusercontent.com/jampotful/seen-back/main/manifest.webmanifest https://fonts.googleapis.com/css2?family=Instrument+Serif; do
  echo "--- $u"; curl -s -o /dev/null -D - "$u" | grep -i -E "^HTTP|access-control|cross-origin|timing-allow|content-type" ; done
node "$ROOT/test/engines/coi_serve.js" "$R" $P0="$T/base" $P1="$T/rc" $P2="$T/cl" $P3="$T/base:cors" > "$R/serve-log.txt" 2>&1 &
SERVER=$!; sleep 1
for p in $P0 $P1 $P2 $P3; do curl --noproxy "*" -s -o /dev/null -w "$p -> %{http_code}\n" "http://127.0.0.1:$p/index.html"; done
for E in $ENGINES; do
  case "$E" in
    sim)
      step "threads experiment: Safari on the iPhone simulator ${UDID:-none}"
      [ -z "${UDID:-}" ] && { echo "no simulator"; continue; }
      PH=test/rec/photos/heron.png,test/rec/photos/portrait.jpg,test/rec/photos/wall.png,test/rec/photos/garden.jpg
      for mp in none:$P0 require-corp:$P1 credentialless:$P2; do
        m=${mp%%:*}; p=${mp##*:}; W=coi; [ "$m" = none ] && W=; TH="1 2 4"; [ "$m" = none ] && TH="1 4"
        for th in $TH; do
          n="sim-$m-t$th"; rm -f "$R/$n.json"
          xcrun simctl openurl "$UDID" "http://127.0.0.1:$p/index.html?probe=1&name=$n&threads=$th&want=$W&photos=$PH&rounds=${ROUNDS:-3}&x=$XORIGIN&cam=0" 2>&1
          t0=$(date +%s)
          while [ $(( $(date +%s) - t0 )) -lt "${SIM_WAIT:-240}" ]; do sleep 3; if [ -f "$R/$n.json" ] && grep -q '"done":true' "$R/$n.json"; then break; fi; done
          echo "$n: $(( $(date +%s) - t0 )) s, $( [ -f "$R/$n.json" ] && head -c 300 "$R/$n.json" | tr '\n' ' ')"
          xcrun simctl io "$UDID" screenshot "$R/$n.png" >/dev/null 2>&1
        done
      done ;;
    *)
      step "threads experiment: $E"
      BROWSERS="$E" REPORTS="$R" timeout 1500 node "$ROOT/test/engines/threads.js"; echo "threads.js $E: exit $?" ;;
  esac
done
kill "$SERVER" 2>/dev/null
step "threads experiment: summary"
python3 -I - "$R" <<'PY'
import json, glob, os, sys
R = sys.argv[1]; S = {}
def brief(r):
    runs = sorted(x['ms']['run'] for x in r.get('photos') or [] if x.get('round', 0) > 0 and x.get('ms') and x['ms'].get('run'))
    a = r.get('about') or {}
    return {'coi': r.get('coi'), 'controlled': r.get('controlled'), 'reloads': r.get('reloads'), 'ready': r.get('ready'), 'readyMs': r.get('readyMs'), 'threads': a.get('threads'), 'loadMs': a.get('loadMs'),
            'start': a.get('start'), 'medianRunMs': runs[len(runs) // 2] if runs else None, 'minRunMs': runs[0] if runs else None, 'n': len(runs),
            'kinds': [x['name'] + ':' + str(x.get('kind')) for x in r.get('photos') or [] if x.get('round') == 0], 'breaks': r.get('breaks'), 'error': r.get('error'), 'done': r.get('done')}
for f in sorted(glob.glob(os.path.join(R, '*-t[0-9]*.json'))):
    try: S[os.path.basename(f)[:-5]] = brief(json.load(open(f)))
    except Exception as e: S[os.path.basename(f)[:-5]] = {'unreadable': str(e)}
json.dump(S, open(os.path.join(R, 'threads-summary.json'), 'w'), indent=1)
for k, v in S.items():
    print(f"{k:34s} coi={v.get('coi')!s:5s} threads={v.get('threads')!s:4s} ready={str(v.get('ready'))[:40]:40s} readyMs={v.get('readyMs')!s:6s} median run ms={v.get('medianRunMs')!s:7s} min={v.get('minRunMs')!s:7s} n={v.get('n')}")
    print(f"{'':34s} breaks={json.dumps(v.get('breaks'))[:400]} error={v.get('error')}")
PY
