#!/usr/bin/env bash
# The publishing job's last step, run only after ci/native/android_pub_emu.sh has passed its gate: put apk/seen-back-debug.apk
# on the branch pub/app-android with a README.md and a built.json (ci/put_branch.sh replaces the branch's whole content),
# then fetch the file back from raw.githubusercontent.com at the new commit and compare its checksum.
# Everything goes into out/android/pub-log.txt. Needs only files on main: native/, ci/native/, ci/put_branch.sh.
set -uo pipefail
ROOT="$PWD"; OUT="$ROOT/out/android"; mkdir -p "$OUT"
exec > >(tee -a "$OUT/pub-log.txt") 2>&1
step() { echo; echo "=== $(date -u +%T) $*"; }
BRANCH=pub/app-android
F=apk/seen-back-debug.apk
[ -f "$F" ] || { echo "no $F"; exit 1; }
python3 -I -c "import json,sys; sys.exit(0 if json.load(open(sys.argv[1])).get('pass') is True else 1)" "$OUT/gate.json" \
  || { echo "the gate did not pass; nothing is published"; exit 1; }

step "the directory to publish"
P="$ROOT/pubdir"; rm -rf "$P"; mkdir -p "$P"
cp "$F" "$P/seen-back-debug.apk"
python3 -I ci/native/android_pub_files.py "$P" "$OUT/gate.json" src/cam.a.js || exit 1
ls -l "$P"; cat "$P/built.json"
cp "$P/built.json" "$P/README.md" "$OUT/"

step "publish $BRANCH"
bash ci/put_branch.sh "$BRANCH" "$P" "Seen Back debug APK" || exit 1
C=$(git ls-remote "$(git remote get-url origin)" "refs/heads/$BRANCH" | cut -c1-40)
echo "$BRANCH is at $C"
echo "branch_commit=$C" > "$OUT/pub-branch.txt"

step "fetch the file back from raw.githubusercontent.com at that commit"
want=$(python3 -I -c "import json,sys; print(json.load(open(sys.argv[1]))['sha256'])" "$P/built.json")
for i in 1 2 3 4 5 6; do
  rm -f /tmp/back.apk
  curl -sSfL -o /tmp/back.apk "https://raw.githubusercontent.com/jampotful/seen-back/$C/seen-back-debug.apk" && break
  sleep 10
done
got=$(sha256sum /tmp/back.apk 2>/dev/null | cut -c1-64)
echo "by commit: $(stat -c %s /tmp/back.apk 2>/dev/null) bytes, sha256 $got"
curl -sSI "https://raw.githubusercontent.com/jampotful/seen-back/$BRANCH/seen-back-debug.apk" | grep -i -E "^(HTTP|content-type|content-length)" | tr -d '\r'
if [ "$got" = "$want" ]; then echo "raw copy matches built.json"; echo "raw_check=match" >> "$OUT/pub-branch.txt"; else echo "raw copy does not match (or could not be read)"; echo "raw_check=mismatch" >> "$OUT/pub-branch.txt"; fi
exit 0
