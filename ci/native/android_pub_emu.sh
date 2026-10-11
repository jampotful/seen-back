#!/usr/bin/env bash
# The publishing job's emulator step, inside reactivecircus/android-emulator-runner, after ci/native/android_pub_build.sh.
#  1. apk/check.apk (the bundle with check files): the opening screen, the page's self-test with the pocket recognizer on four
#     photos, and Begin with the emulator's camera (ci/native/android_emu.sh with BIG=0).
#  2. apk/seen-back-debug.apk (the file to publish), installed fresh in place of the first: the opening screen as a person
#     opens it, then Begin with the emulator's camera.
# The gate passes only when the self-test reports done with no failed check, and the published APK shows the opening screen
# ("intro") at a secure origin and reaches the finder with the camera as its source. The verdict goes to out/android/gate.json,
# and the exit status follows it, so the publishing step runs only after a pass.
set -uo pipefail
ROOT="$PWD"; OUT="$ROOT/out/android"; mkdir -p "$OUT/shots"
PKG=org.seenback.shell

APK=apk/check.apk BIG=0 bash ci/native/android_emu.sh

exec > >(tee -a "$OUT/pub-emu-log.txt") 2>&1
step() { echo; echo "=== $(date -u +%T) $*"; }
shot() { adb exec-out screencap -p > "$OUT/shots/$1.png" 2>/dev/null; echo "screenshot $1"; }
state() { adb shell run-as $PKG cat files/state.json 2>/dev/null; }

step "5. the published APK, installed fresh, opened as a person would"
adb uninstall $PKG 2>&1 | tail -1
adb install -g apk/seen-back-debug.apk 2>&1 | tail -2
adb shell am start -W -n $PKG/.MainActivity 2>&1 | grep -E "Status|TotalTime|Error"
sleep 15; shot 5-pub-open
state > "$OUT/pub-state-open.json"; head -c 600 "$OUT/pub-state-open.json"; echo

step "6. the published APK: Begin, with the emulator's camera"
adb shell am force-stop $PKG; sleep 1
adb shell "am start -W -n $PKG/.MainActivity --es js 'document.getElementById(\"btnBegin\").click()'" 2>&1 | grep -E "Status|TotalTime|Error"
sleep 25; shot 6-pub-begin
state > "$OUT/pub-state-begin.json"; head -c 600 "$OUT/pub-state-begin.json"; echo
adb shell am force-stop $PKG

step "the gate"
python3 -I - "$OUT" <<'PY'
import json, os, sys
out = sys.argv[1]
def load(n):
    try:
        return json.load(open(os.path.join(out, n)))
    except Exception as e:
        return {"unreadable": str(e)}
st = (load("selftest-state.json").get("st") or {})
op, be = load("pub-state-open.json"), load("pub-state-begin.json")
g = {
    "selftest": {"done": st.get("done"), "ok": st.get("ok"), "checks": st.get("checks"), "fails": (st.get("fails") or [])[:20],
                 "ms_total": (st.get("ms") or {}).get("total"), "build": st.get("build")},
    "published_open": {k: op.get(k) for k in ("sb", "screen", "src", "href", "secure", "ua")},
    "published_begin": {k: be.get(k) for k in ("sb", "screen", "src", "secure")},
}
g["pass"] = bool(st.get("done") is True and st.get("ok") is True and (st.get("checks") or 0) > 0
                 and op.get("sb") is True and op.get("secure") is True and op.get("screen") == "intro"
                 and be.get("screen") == "finder" and be.get("src") == "cam")
json.dump(g, open(os.path.join(out, "gate.json"), "w"), indent=1)
print(json.dumps(g, indent=1))
sys.exit(0 if g["pass"] else 1)
PY
