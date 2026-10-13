#!/usr/bin/env bash
# The iOS shell on a macOS build machine: compile native/ios-shell/main.swift for the iPhone simulator with swiftc (no Xcode
# project, no signing identity: an ad hoc signature, which the simulator accepts), copy the built page into the app, install it in
# an iPhone simulator, open it, run the page's self-test with the pocket recognizer inside the app, and then the same app pointed at
# the page served from this machine (http://127.0.0.1:8781) for comparison. Inside the app the page comes from the shell's own
# server at http://127.0.0.1:41730/ (main.swift, class Loopback). A label starting with ios-big runs the larger-model probe instead
# of the comparison; one starting with ios-loop runs the larger-model probe inside the app twice (the second launch must find the
# model kept) and then presses Begin. Everything goes into out/ios/.
set -uo pipefail
ROOT="$PWD"; OUT="$ROOT/out/ios"; mkdir -p "$OUT/shots" "$ROOT/out/reports"
exec > >(tee -a "$OUT/log.txt") 2>&1
step() { echo; echo "=== $(date -u +%T) $*"; }
limit() { local s=$1; shift; "$@" & local p=$!; ( sleep "$s"; kill "$p" 2>/dev/null ) & local w=$!; wait "$p"; local rc=$?; kill "$w" 2>/dev/null; return $rc; }
BID=org.seenback.shell
RECQ="&rec=models/pocket&recphotos=test/rec/photos/heron.png,test/rec/photos/portrait.jpg,test/rec/photos/wall.png,test/rec/photos/garden.jpg"

step "machine"
sw_vers; uname -m; sysctl -n hw.memsize; xcodebuild -version | tr '\n' ' '; echo; echo "simulator SDK $(xcrun --sdk iphonesimulator --show-sdk-version)"

step "boot an iPhone simulator now, it takes a while"
UDID=$(xcrun simctl list devices available -j | python3 -I -c "
import json, sys
d = json.load(sys.stdin)['devices']
c = sorted((rt, x['udid'], x['name']) for rt, xs in d.items() for x in xs if x['name'] == 'iPhone 17' and x.get('isAvailable', True))
if not c: c = sorted((rt, x['udid'], x['name']) for rt, xs in d.items() for x in xs if x['name'].startswith('iPhone') and x.get('isAvailable', True))
print(c[-1][1] + ' ' + c[-1][0] + ' ' + c[-1][2] if c else '')")
echo "simulator: ${UDID:-none found}"; UDID="${UDID%% *}"
[ -n "$UDID" ] && xcrun simctl boot "$UDID" 2>&1

step "build the page"
python3 -I build.py && node --check dist/app.js && echo "build ok"

step "compile the shell with swiftc for the simulator"
APP="$ROOT/build-ios/SeenBack.app"; rm -rf "$ROOT/build-ios"; mkdir -p "$APP"
ARCH=$(uname -m); SDK=$(xcrun --sdk iphonesimulator --show-sdk-path)
xcrun --sdk iphonesimulator swiftc -swift-version 5 -module-name SeenBack -O -target "$ARCH-apple-ios16.0-simulator" -sdk "$SDK" \
  -o "$APP/SeenBack" native/ios-shell/main.swift 2>&1 | grep -v -E "^\s*$" | head -60
[ -f "$APP/SeenBack" ] || { echo "swiftc made no binary"; exit 1; }
cp native/ios-shell/Info.plist "$APP/Info.plist"
cp icons/icon-180.png "$APP/AppIcon60x60@3x.png"
bash ci/native/bundle.sh "$APP/www"
codesign --force --sign - --timestamp=none "$APP" 2>&1; echo "codesign (ad hoc): exit $?"
echo "app: $(du -sk "$APP" | cut -f1) kB"; (cd "$ROOT/build-ios" && mkdir -p Payload && cp -R SeenBack.app Payload/ && zip -qr -9 shell.zip Payload && echo "zipped like an .ipa: $(stat -f %z shell.zip) bytes"; rm -rf Payload)

state() { local d; d=$(xcrun simctl get_app_container "$UDID" $BID data 2>/dev/null) && cat "$d/Documents/state.json" 2>/dev/null; }
applog() { local d; d=$(xcrun simctl get_app_container "$UDID" $BID data 2>/dev/null) && cat "$d/Documents/log.txt" 2>/dev/null; }
shot() { xcrun simctl io "$UDID" screenshot "$OUT/shots/$1.png" >/dev/null 2>&1; echo "screenshot $1"; }
summary() {
python3 -I - "$1" <<'PY'
import json, sys
try:
    d = json.load(open(sys.argv[1]))
except Exception as e:
    print("state unreadable:", e); sys.exit(0)
T = d.get("st") or {}
E = T.get("env") or {}
print("address:", d.get("href"), "| secure context:", d.get("secure"), "| crossOriginIsolated:", d.get("coi"))
print("user agent:", d.get("ua"))
print("self-test done:", T.get("done"), "ok:", T.get("ok"), "checks:", T.get("checks"), "phase:", T.get("phase"))
print("fails:", json.dumps(T.get("fails"))[:1500])
print("webgl2:", E.get("webgl2"), "float:", E.get("floatOK"), "renderer:", E.get("unmaskedRenderer") or E.get("renderer"), "engineError:", E.get("engineError"))
for k in ("rec", "recognizer", "recog"):
    if k in T: print(k + ":", json.dumps(T[k])[:2500])
print("keys:", sorted(T.keys()))
PY
}
selftest() {   # $1 label, then the launch arguments
  local label=$1; shift
  xcrun simctl terminate "$UDID" $BID >/dev/null 2>&1; sleep 1
  xcrun simctl launch "$UDID" $BID "$@" 2>&1
  local t0=$(date +%s) n=0 fin=0 el
  while [ $(( $(date +%s) - t0 )) -lt 420 ]; do
    sleep 5; n=$((n+1)); el=$(( $(date +%s) - t0 ))
    case $n in 2|4|8|14|24|40|60) shot "$label-$(printf %03d $el)s";; esac
    state > "$OUT/$label-state.json"
    if grep -q '"done":true' "$OUT/$label-state.json"; then echo "self-test done after about $el s"; fin=1; sleep 2; shot "$label-final"; break; fi
  done
  [ $fin = 1 ] || echo "self-test did not report done within 420 s"
  state > "$OUT/$label-state.json"; summary "$OUT/$label-state.json"
}

step "install and open the app"
[ -n "$UDID" ] && limit 300 xcrun simctl bootstatus "$UDID" -b 2>&1 | tail -2
xcrun simctl install "$UDID" "$APP" 2>&1; echo "install: exit $?"
xcrun simctl launch "$UDID" $BID 2>&1; sleep 15; shot 1-open
state > "$OUT/open-state.json"; head -c 700 "$OUT/open-state.json"; echo
applog | grep -E "loopback|open " | head -6
for u in index.html "models/pocket/manifest.json" "nothing-here.txt"; do
  curl -s -o /dev/null -w "the app's server, from the Mac: $u -> %{http_code}, %{size_download} bytes, %{content_type}\n" "http://127.0.0.1:41730/$u"
done
curl -s -o /dev/null -r 0-99 -w "the app's server, a byte range of test/assets/motion.mp4 -> %{http_code}, %{size_download} bytes\n" "http://127.0.0.1:41730/test/assets/motion.mp4"

step "2. the page's self-test inside the app (served by the app itself), with the shipped pocket recognizer on four photos"
selftest 2-selftest -q "selftest=1&nosw=1$RECQ"

case "${GITHUB_REF_NAME:-}" in run/native/ios-big*|run/native/big*) BIG=1 ;; run/native/ios-loop*) BIG=2 ;; *) BIG=0 ;; esac
if [ $BIG = 0 ]; then
step "3. the same app pointed at the page served from this Mac (http://127.0.0.1:8781), for comparison"
python3 -I ci/engines/serve.py 8781 "$ROOT" "$ROOT/out/reports" > "$OUT/serve-log.txt" 2>&1 &
sleep 1; curl -s -o /dev/null -w "8781 -> %{http_code}\n" http://127.0.0.1:8781/index.html
selftest 3-served -url "http://127.0.0.1:8781/index.html?selftest=1&nosw=1&report=/report/ios-served$RECQ"
else
step "4. the larger model (models/naturalist: 310 MB from raw.githubusercontent.com) through the page's own recognizer inside the app, then four photos"
bigprobe() {   # $1 label, then the launch arguments
local label=$1; shift
( while :; do echo "$(date -u +%T) $(ps -axo pid=,rss=,command= | grep -E 'WebKit.WebContent|SeenBack' | grep -v grep | awk '{ n = ($0 ~ /WebContent/) ? "WebContent" : "SeenBack"; printf "%s %s %s;", $1, $2, n }')"; sleep 4; done ) > "$OUT/$label-memory.txt" 2>&1 &
MEMPID=$!
xcrun simctl terminate "$UDID" $BID >/dev/null 2>&1; sleep 1
xcrun simctl launch "$UDID" $BID "$@" 2>&1
local t0=$(date +%s) n=0 fin=0 el
while [ $(( $(date +%s) - t0 )) -lt 900 ]; do
  sleep 6; n=$((n+1)); el=$(( $(date +%s) - t0 ))
  case $n in 3|10|20|40|70|100) shot "$label-$(printf %03d $el)s";; esac
  state > "$OUT/$label-state.json"
  if python3 -I -c "import json,sys; d=json.load(open(sys.argv[1])); sys.exit(0 if (d.get('big') or {}).get('done') else 1)" "$OUT/$label-state.json" 2>/dev/null; then echo "probe done after about $el s"; fin=1; shot $label-final; break; fi
  [ $((n % 10)) = 0 ] && python3 -I -c "import json,sys; d=json.load(open(sys.argv[1])); b=d.get('big') or {}; print($el, 's:', b.get('line'), b.get('has'), b.get('steps'))" "$OUT/$label-state.json" 2>/dev/null
done
[ $fin = 1 ] || { echo "the probe did not finish within 900 s"; shot $label-stopped; }
kill $MEMPID 2>/dev/null
state > "$OUT/$label-state.json"
python3 -I - "$OUT/$label-state.json" "$OUT/$label-memory.txt" <<'PY'
import json, re, sys
try:
    d = json.load(open(sys.argv[1]))
except Exception as e:
    print("state unreadable:", e); d = {}
b = d.get("big") or {}
for k in ("started", "steps", "before", "after", "gotMs", "has", "size", "readyMs", "error", "ms", "done", "line"):
    print(k + ":", json.dumps(b.get(k)))
print("about:", json.dumps(b.get("about"))[:900])
for p in b.get("photos") or []:
    print("photo:", json.dumps(p)[:700])
peak = {}
for line in open(sys.argv[2]):
    for pid, rss, name in re.findall(r"(\d+) (\d+) ([\w.:-]+);", line):
        peak[pid + " " + name] = max(peak.get(pid + " " + name, 0), int(rss))
for name, kb in sorted(peak.items()):
    print("peak resident memory on the Mac: %s %d MB" % (name, kb // 1024))
PY
}
bigprobe 4-big -probe native-probe/big.js
if [ $BIG = 2 ]; then
step "4b. the larger model once more, after the app is closed and opened again: the parts must come from what the page kept"
bigprobe 4b-big-again -probe native-probe/big.js
step "6. Begin inside the app: the page asks for the camera (the simulator has none)"
xcrun simctl terminate "$UDID" $BID >/dev/null 2>&1; sleep 1
xcrun simctl launch "$UDID" $BID -js 'document.getElementById("btnBegin").click()' 2>&1
sleep 25; shot 6-begin
state > "$OUT/6-begin-state.json"; head -c 900 "$OUT/6-begin-state.json"; echo
applog | grep -E "camera|loopback|open " | tail -12
else
step "5. the larger model again, with the same app pointed at the page served from this Mac (http://127.0.0.1:8781), where Cache Storage takes http addresses"
python3 -I ci/engines/serve.py 8781 "$ROOT" "$ROOT/out/reports" > "$OUT/serve-log.txt" 2>&1 &
sleep 1; curl -s -o /dev/null -w "8781 -> %{http_code}\n" http://127.0.0.1:8781/index.html
bigprobe 5-big-served -url "http://127.0.0.1:8781/index.html" -probe ci/native/probe-big.js
fi
fi

step "the app's own log (console errors and warnings, loads it could not serve)"
applog > "$OUT/app-log.txt"; wc -l "$OUT/app-log.txt"; grep -v "^[0-9.]* console warn" "$OUT/app-log.txt" | head -60
xcrun simctl shutdown "$UDID" 2>&1 || true
exit 0
