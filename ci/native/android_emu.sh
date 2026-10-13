#!/usr/bin/env bash
# Run inside reactivecircus/android-emulator-runner, after ci/native/android_build.sh: install the debug APK in the emulator,
# open it, run the page's self-test inside the WebView with the shipped pocket recognizer, then press Begin with the
# emulator's camera, and (unless BIG=0) fetch the larger model. APK= names another APK to install. Screenshots, logcat and what the page reports about itself go into out/android/.
set -uo pipefail
ROOT="$PWD"; OUT="$ROOT/out/android"; mkdir -p "$OUT/shots"
exec > >(tee -a "$OUT/emu-log.txt") 2>&1
step() { echo; echo "=== $(date -u +%T) $*"; }
PKG=org.seenback.shell
APK="${APK:-native/android-shell/app/build/outputs/apk/debug/app-debug.apk}"
RECQ="&rec=models/pocket&recphotos=test/rec/photos/heron.png,test/rec/photos/portrait.jpg,test/rec/photos/wall.png,test/rec/photos/garden.jpg"
shot() { adb exec-out screencap -p > "$OUT/shots/$1.png" 2>/dev/null; echo "screenshot $1"; }
state() { adb shell run-as $PKG cat files/state.json 2>/dev/null; }

step "emulator"
adb devices
for p in ro.build.version.release ro.build.version.sdk ro.product.model ro.product.cpu.abi; do echo "$p=$(adb shell getprop $p | tr -d '\r')"; done
adb shell dumpsys package com.google.android.webview 2>/dev/null | grep -m2 -E "versionName" | sed 's/^ */webview (com.google.android.webview) /'
adb shell dumpsys webviewupdate 2>/dev/null | grep -m3 -E "Current WebView package|version" | sed 's/^ *//'
adb shell cat /proc/meminfo | head -2

step "install"
adb install -r -g "$APK" 2>&1 | tail -2
adb shell pm grant $PKG android.permission.CAMERA 2>&1; adb shell dumpsys package $PKG | grep -m1 "android.permission.CAMERA" | sed 's/^ *//'
adb logcat -c
adb logcat -v time > "$OUT/logcat-all.txt" 2>&1 &
LOGPID=$!

step "1. open the app as a person would"
adb shell am start -W -n $PKG/.MainActivity 2>&1 | grep -E "Status|TotalTime|Error"
sleep 15; shot 1-open
state > "$OUT/state-open.json"; head -c 600 "$OUT/state-open.json"; echo

step "2. the page's self-test inside the WebView, with the shipped pocket recognizer (models/pocket) on four photos"
adb shell am force-stop $PKG; sleep 1
adb shell "am start -W -n $PKG/.MainActivity --es q 'selftest=1&nosw=1$RECQ'" 2>&1 | grep -E "Status|TotalTime|Error"
t0=$(date +%s); n=0; fin=0
while [ $(( $(date +%s) - t0 )) -lt 480 ]; do
  sleep 5; n=$((n+1)); el=$(( $(date +%s) - t0 ))
  case $n in 2|4|8|14|24|40|60|80) shot "2-selftest-$(printf %03d $el)s";; esac
  state > "$OUT/selftest-state.json"
  if grep -q '"done":true' "$OUT/selftest-state.json"; then echo "self-test done after about $el s"; fin=1; sleep 2; shot 2-selftest-final; break; fi
done
[ $fin = 1 ] || echo "self-test did not report done within 480 s"
state > "$OUT/selftest-state.json"
python3 -I - "$OUT/selftest-state.json" <<'PY'
import json, sys
try:
    d = json.load(open(sys.argv[1]))
except Exception as e:
    print("state unreadable:", e); sys.exit(0)
T = d.get("st") or {}
E = T.get("env") or {}
print("secure context:", d.get("secure"), "| crossOriginIsolated:", d.get("coi"))
print("user agent:", d.get("ua"))
print("self-test done:", T.get("done"), "ok:", T.get("ok"), "checks:", T.get("checks"), "phase:", T.get("phase"))
print("fails:", json.dumps(T.get("fails"))[:1500])
print("webgl2:", E.get("webgl2"), "float:", E.get("floatOK"), "renderer:", E.get("unmaskedRenderer") or E.get("renderer"), "engineError:", E.get("engineError"))
for k in ("rec", "recognizer", "recog"):
    if k in T: print(k + ":", json.dumps(T[k])[:2500])
print("keys:", sorted(T.keys()))
PY

step "3. Begin, with the emulator's camera (the shell grants the page's camera request)"
adb shell am force-stop $PKG; sleep 1
adb shell "am start -W -n $PKG/.MainActivity --es js 'document.getElementById(\"btnBegin\").click()'" 2>&1 | grep -E "Status|TotalTime|Error"
sleep 25; shot 3-begin
state > "$OUT/state-begin.json"; head -c 600 "$OUT/state-begin.json"; echo

if [ "${BIG:-1}" = 1 ]; then
step "4. the larger model (models/naturalist: 310 MB from raw.githubusercontent.com) through the page's own recognizer object, then four photos"
adb shell am force-stop $PKG; sleep 1
( while :; do echo "$(date -u +%T) $(adb shell ps -A -o PID,RSS,NAME 2>/dev/null | grep -E 'seenback|sandboxed|webview' | tr -s ' ' | tr '\n' ';') $(adb shell grep MemAvailable /proc/meminfo | tr -s ' ')"; sleep 4; done ) > "$OUT/big-memory.txt" 2>&1 &
MEMPID=$!
adb shell "am start -W -n $PKG/.MainActivity --es probe native-probe/big.js" 2>&1 | grep -E "Status|TotalTime|Error"
t0=$(date +%s); n=0; fin=0
while [ $(( $(date +%s) - t0 )) -lt 900 ]; do
  sleep 6; n=$((n+1)); el=$(( $(date +%s) - t0 ))
  case $n in 3|10|20|40|70|100) shot "4-big-$(printf %03d $el)s";; esac
  state > "$OUT/big-state.json"
  if python3 -I -c "import json,sys; d=json.load(open(sys.argv[1])); sys.exit(0 if (d.get('big') or {}).get('done') else 1)" "$OUT/big-state.json" 2>/dev/null; then echo "probe done after about $el s"; fin=1; shot 4-big-final; break; fi
  [ $((n % 10)) = 0 ] && python3 -I -c "import json,sys; d=json.load(open(sys.argv[1])); b=d.get('big') or {}; print($el, 's:', b.get('line'), b.get('has'), b.get('steps'))" "$OUT/big-state.json" 2>/dev/null
done
[ $fin = 1 ] || { echo "the probe did not finish within 900 s"; shot 4-big-stopped; }
kill $MEMPID 2>/dev/null
state > "$OUT/big-state.json"
python3 -I - "$OUT/big-state.json" "$OUT/big-memory.txt" <<'PY'
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
low = None
for line in open(sys.argv[2]):
    for pid, rss, name in re.findall(r"(\d+) (\d+) ([\w.:]+);", line):
        peak[name] = max(peak.get(name, 0), int(rss))
    m = re.search(r"MemAvailable: (\d+)", line)
    if m:
        low = int(m.group(1)) if low is None else min(low, int(m.group(1)))
for name, kb in sorted(peak.items()):
    print("peak resident memory: %s %d MB" % (name, kb // 1024))
print("lowest MemAvailable in the emulator: %s MB" % (low // 1024 if low else "?"))
PY

else echo; echo "step 4 (the larger model) left out: BIG=0"; fi

step "logcat lines from the shell and the page"
kill $LOGPID 2>/dev/null; sleep 1
grep -E "SeenBack|chromium|cr_|WebView|FATAL|AndroidRuntime" "$OUT/logcat-all.txt" | grep -v "SeenBack *: state " > "$OUT/logcat-seenback.txt"
wc -l "$OUT/logcat-all.txt" "$OUT/logcat-seenback.txt"
grep -c "SeenBackConsole" "$OUT/logcat-seenback.txt" | sed 's/^/console lines: /'
grep -E "SeenBack|AndroidRuntime" "$OUT/logcat-seenback.txt" | grep -v "SeenBack *: state " | head -80
gzip -f "$OUT/logcat-all.txt"
exit 0
