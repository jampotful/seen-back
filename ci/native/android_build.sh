#!/usr/bin/env bash
# The Android shell's build on a Linux build machine: the page, the bundle under assets/www, a debug APK (Gradle makes the debug
# keystore in ~/.android on this machine; it is never committed or returned). Everything goes into out/android/build-log.txt.
set -uo pipefail
ROOT="$PWD"; OUT="$ROOT/out/android"; mkdir -p "$OUT"
exec > >(tee -a "$OUT/build-log.txt") 2>&1
step() { echo; echo "=== $(date -u +%T) $*"; }
step "machine"
uname -srm; nproc; free -m | head -2; java -version 2>&1 | head -1; gradle --version 2>/dev/null | grep -E "^Gradle"
echo "ANDROID_HOME=${ANDROID_HOME:-}"; ls "${ANDROID_HOME:-/nonexistent}/platforms" 2>&1 | tr '\n' ' '; echo; ls "${ANDROID_HOME:-/nonexistent}/build-tools" 2>&1 | tr '\n' ' '; echo
step "build the page"
python3 -I build.py && node --check dist/app.js && echo "build ok"
step "bundle the page into the APK's assets"
A=native/android-shell/app/src/main
bash ci/native/bundle.sh "$A/assets/www"
mkdir -p "$A/res/mipmap-xxxhdpi" && cp icons/icon-192.png "$A/res/mipmap-xxxhdpi/ic_launcher.png"
step "gradle assembleDebug"
t0=$(date +%s)
(cd native/android-shell && gradle --no-daemon --console=plain assembleDebug 2>&1 | grep -v -E "^(> Task|Download)" | tail -80)
APK=native/android-shell/app/build/outputs/apk/debug/app-debug.apk
echo "assembleDebug took $(( $(date +%s) - t0 )) s"
if [ -f "$APK" ]; then
  echo "APK: $(stat -c %s "$APK") bytes"; sha256sum "$APK" | cut -c1-64
  unzip -l "$APK" | tail -1
  unzip -l "$APK" | sort -k1 -n -r | head -8
  "$ANDROID_HOME"/build-tools/$(ls "$ANDROID_HOME/build-tools" | sort -V | tail -1)/aapt2 dump badging "$APK" 2>/dev/null | grep -E "^(package|sdkVersion|targetSdkVersion|uses-permission|application-label)" | head -8
  echo "apk_bytes=$(stat -c %s "$APK")" > "$OUT/apk.txt"
  exit 0
fi
echo "no APK was made"; exit 1
