#!/usr/bin/env bash
# ci/engines/patches/sw-5xx-kept.patch, proven: two copies of the built page (as it is, and with the patch), served by
# test/engines/coi_serve.js on 8795 and 8796; test/engines/sw5xx.js keeps everything on a first visit, then has the server answer 502
# to everything and opens the page again. ENGINES="chromium firefox webkit" bash ci/engines/sw5xx.sh   (results in out/sw5xx/)
set -uo pipefail
ROOT="$PWD"; OUT="${OUT:-$ROOT/out}"; R="$OUT/sw5xx"; T=/tmp/sw5xx; mkdir -p "$R"; rm -rf "$T"; mkdir -p "$T/old"
echo; echo "=== $(date -u +%T) the service worker and a 5xx: as built, and with ci/engines/patches/sw-5xx-kept.patch"
tar -C "$ROOT" --exclude=./.git --exclude=./out --exclude=./ci-rec -cf - . | tar -C "$T/old" -xf -
(cd "$T/old" && python3 -I build.py >/dev/null && echo "old: built")
cp -R "$T/old" "$T/new"; (cd "$T/new" && patch -p1 --forward < "$ROOT/ci/engines/patches/sw-5xx-kept.patch" && python3 -I build.py >/dev/null && grep -c "res.status >= 500" sw.js | sed 's/^/new: sw.js 5xx lines: /')
node "$ROOT/test/engines/coi_serve.js" "$R" 8795="$T/old" 8796="$T/new" > "$R/serve-log.txt" 2>&1 & S=$!; sleep 1
for E in ${ENGINES:-chromium}; do BROWSERS=$E OUT="$R" OLD=8795 NEW=8796 timeout 600 node "$ROOT/test/engines/sw5xx.js"; echo "sw5xx.js $E: exit $?"; done
kill $S 2>/dev/null
