#!/usr/bin/env bash
# The publishing job's build (a push to run/native/pub<anything>), on a Linux build machine. It makes two debug APKs from one
# build of the page, with the same debug key (Gradle makes it in ~/.android on this machine; it is never committed or returned):
#   apk/check.apk             the bundle with the check files (TEST=1), which the emulator runs the self-test on
#   apk/seen-back-debug.apk   the bundle without them (TEST=0), which is published
# It then compares the two APKs entry by entry (CRC-32 from `unzip -lv`): they may differ only in the check files
# (assets/www/test/, assets/www/native-probe/) and in the signature files under META-INF/. Everything goes into
# out/android/pub-build-log.txt; the comparison also into out/android/pub-compare.txt.
set -uo pipefail
ROOT="$PWD"; OUT="$ROOT/out/android"; mkdir -p "$OUT" "$ROOT/apk"
A=native/android-shell/app/src/main
APK=native/android-shell/app/build/outputs/apk/debug/app-debug.apk
step() { echo; echo "=== $(date -u +%T) $*"; }

# 1. the page, the bundle with the check files, and the first APK (android_build.sh writes out/android/build-log.txt)
bash ci/native/android_build.sh || { echo "android_build.sh failed" | tee -a "$OUT/pub-build-log.txt"; exit 1; }
cp "$APK" apk/check.apk

exec > >(tee -a "$OUT/pub-build-log.txt") 2>&1
step "the bundle without check files (TEST=0), and the APK to publish"
TEST=0 bash ci/native/bundle.sh "$A/assets/www"
for d in test native-probe; do [ -e "$A/assets/www/$d" ] && { echo "check files are still in the bundle: $d"; exit 1; }; done
t0=$(date +%s)
(cd native/android-shell && gradle --no-daemon --console=plain clean assembleDebug 2>&1 | grep -v -E "^(> Task|Download)" | tail -40)
echo "assembleDebug took $(( $(date +%s) - t0 )) s"
[ -f "$APK" ] || { echo "no APK was made"; exit 1; }
cp "$APK" apk/seen-back-debug.apk
for f in apk/check.apk apk/seen-back-debug.apk; do echo "$f: $(stat -c %s "$f") bytes, sha256 $(sha256sum "$f" | cut -c1-64)"; done

step "compare the two APKs entry by entry"
python3 -I - apk/check.apk apk/seen-back-debug.apk "$OUT/pub-compare.txt" <<'PY'
import sys, zipfile
a, b, out = sys.argv[1:4]
def entries(p):
    with zipfile.ZipFile(p) as z:
        return {i.filename: (i.CRC, i.file_size) for i in z.infolist()}
A, B = entries(a), entries(b)
check = lambda n: n.startswith("assets/www/test/") or n.startswith("assets/www/native-probe/")
sig = lambda n: n.startswith("META-INF/")
lines, bad = [], []
only_a = sorted(set(A) - set(B)); only_b = sorted(set(B) - set(A))
diff = sorted(n for n in set(A) & set(B) if A[n] != B[n])
for n in only_a:
    lines.append("only in the check APK: %s (%d bytes)" % (n, A[n][1]))
    if not (check(n) or sig(n)): bad.append(n)
for n in B:
    if check(n): lines.append("check file in the published APK: %s" % n); bad.append(n)
for n in only_b:
    lines.append("only in the published APK: %s" % n)
    if not sig(n): bad.append(n)
for n in diff:
    lines.append("differs: %s" % n)
    if not sig(n): bad.append(n)
same = len(set(A) & set(B)) - len(diff)
lines.append("entries: %d in the check APK, %d in the published APK, %d identical (same CRC-32 and size)" % (len(A), len(B), same))
lines.append("verdict: %s" % ("the APKs differ only in check files and signature files" if not bad else "UNEXPECTED differences: " + ", ".join(bad[:20])))
open(out, "w").write("\n".join(lines) + "\n")
print("\n".join(lines[-2:]))
sys.exit(1 if bad else 0)
PY
