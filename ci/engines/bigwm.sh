#!/usr/bin/env bash
# The larger model's memory, page against page (run/engines/bigwm*, docs/ENGINES.md, 18 October 2026): each page named in
# ci/engines/wm-variants.txt is built and served on this machine, each on a port of its own (so its own origin, and nothing one kept is found
# by the next), and the larger model is put through test/engines/big.js once on each, with no census of the caches (NOCACHES=1). A variant
# named main is the page of origin/main; one named at-<commit> is the page of that commit, fetched from the branches listed in
# ci/engines/wm-branches.txt; any other name is this commit's page, opened with ?wm=<name> for a trial page that reads it.
# PART=linux: Playwright's WebKit; PART=mac-ws: Playwright's WebKit, then Safari. Memory: ci/engines/memwatch.py (ps, once a second) and
# ci/engines/memwatch2.py (each process's footprint and its own peak, four times a second, with breakdowns); ci/engines/bigwmsum.py writes the tables.
set -uo pipefail
ROOT="$PWD"; OUT="$ROOT/out"; mkdir -p "$OUT"
exec > >(tee -a "$OUT/log.txt") 2>&1
step() { echo; echo "=== $(date -u +%T) $*"; }
limit() { local s=$1; shift; "$@" & local p=$!; ( sleep "$s"; kill "$p" 2>/dev/null ) & local w=$!; wait "$p"; local rc=$?; kill "$w" 2>/dev/null; return $rc; }
PW=/tmp/pw; PWV=1.56.0; PART="${PART:-linux}"
VARS=$(grep -v '^#' ci/engines/wm-variants.txt | tr '\n' ' ')
step "machine ($PART), variants: $VARS"; uname -a; (command -v free >/dev/null && free -m) || (sysctl -n hw.memsize hw.ncpu; sw_vers); node --version
step "build and serve"
python3 -I build.py | tail -1
for v in $VARS; do case "$v" in
  main) git fetch -q --depth 1 origin main && git worktree add -q /tmp/v-main FETCH_HEAD && (cd /tmp/v-main && python3 -I build.py | tail -1 && git log --oneline -1) ;;
  at-*) for b in $(cat ci/engines/wm-branches.txt 2>/dev/null); do git fetch -q --depth 5 origin "$b" 2>/dev/null; done
        git worktree add -q "/tmp/v-$v" "${v#at-}" && (cd "/tmp/v-$v" && python3 -I build.py | tail -1 && git log --oneline -1) ;;
esac; done
k=0; for v in $VARS; do dir="$ROOT"; case "$v" in main|at-*) dir="/tmp/v-$v" ;; esac; python3 -I ci/engines/serve.py $((8781 + k)) "$dir" "$OUT/reports-$v" > "$OUT/serve-$v.txt" 2>&1 & k=$((k + 1)); done
sleep 2
step "photos"; python3 -I ci/engines/big_photos.py /tmp/bigphotos
step "playwright $PWV"
mkdir -p "$PW" && (cd "$PW" && npm init -y >/dev/null && npm install --no-audit --no-fund "playwright@$PWV" 2>&1 | tail -1)
export NODE_PATH="$PW/node_modules"
if [ "$PART" = linux ]; then for t in 1 2; do timeout 300 node "$PW/node_modules/playwright/cli.js" install --with-deps webkit > "$OUT/install-webkit.txt" 2>&1 && break; done
else node "$PW/node_modules/playwright/cli.js" install webkit 2>&1 | grep -v -E "[0-9]+%" | tail -2; sudo safaridriver --enable 2>&1; safaridriver -p 4444 > "$OUT/safaridriver-log.txt" 2>&1 & sleep 2; fi
python3 -I ci/engines/memwatch.py "$OUT/mem.jsonl" & MW=$!
python3 -I ci/engines/memwatch2.py "$OUT" & MW2=$!
k=0
for v in $VARS; do
  port=$((8781 + k)); k=$((k + 1))
  for B in webkit $([ "$PART" = mac-ws ] && echo safari); do
    step "variant $v in $B (port $port)"; mkdir -p "$OUT/$v"
    ( export BROWSER=$B OUT="$OUT/$v" PHOTOS=/tmp/bigphotos/photos.json SITE="http://127.0.0.1:$port/?wm=$v" HOME_CHECKS=0 NOCACHES=1; limit 900 node test/engines/big.js ); echo "big.js $v $B: exit $?"
    if [ "$B" = safari ]; then pkill -x Safari 2>/dev/null; sleep 3; fi
    sleep 5
  done
done
kill $MW $MW2 2>/dev/null
step "summary"; python3 -I ci/engines/bigwmsum.py "$OUT" | tee "$OUT/wm-summary.txt"
for v in $VARS; do cp "$OUT/mem.jsonl" "$OUT/$v/" 2>/dev/null; python3 -I ci/engines/bigsum.py "$OUT/$v" > "$OUT/$v/big-summary.txt" 2>&1; rm -f "$OUT/$v/mem.jsonl"; done
gzip -9 -k "$OUT/mem2.jsonl" 2>/dev/null; du -sh "$OUT"; ls -la "$OUT"
