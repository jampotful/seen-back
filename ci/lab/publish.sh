#!/usr/bin/env bash
# Merge one model's job outputs with what its pub/lab-<model> branch already holds, and publish the branch.
# Usage: bash ci/lab/publish.sh <model>   (parts/ holds one directory per job artifact; data_in/ the manifest)
set -uo pipefail
model="$1"; mkdir -p ret pubdir
L=ret/log.txt
say() { echo "[$(date -u +%T)] $*" | tee -a "$L"; }
run() { say "+ $*"; "$@" >> "$L" 2>&1; local rc=$?; say "exit $rc"; return $rc; }
for d in parts/*/; do [ -f "$d/_ci/log.txt" ] && { echo "==== job log $d"; cat "$d/_ci/log.txt"; } >> "$L"; done
# Optionally wait until an earlier run has published this model, so that two publishes never race (PUBLISH_AFTER_RUN=n).
if [ -n "${PUBLISH_AFTER_RUN:-}" ]; then
  t0=$(date +%s)
  while :; do
    rn=0
    if git fetch -q --depth 1 origin "pub/lab-$model" 2>/dev/null; then
      rn=$(git show FETCH_HEAD:_made.txt 2>/dev/null | sed -n 's/^run_number=//p'); rn=${rn:-0}
    fi
    if [ "$rn" -ge "$PUBLISH_AFTER_RUN" ]; then say "pub/lab-$model was published by run $rn; going ahead"; break; fi
    if [ $(( $(date +%s) - t0 )) -ge 3000 ]; then say "gave up waiting for run $PUBLISH_AFTER_RUN to publish pub/lab-$model (branch at run $rn)"; break; fi
    sleep 30
  done
fi
if git ls-remote --exit-code origin "refs/heads/pub/lab-$model" >/dev/null 2>&1; then
  git fetch -q --depth 1 origin "pub/lab-$model" && git --work-tree=pubdir checkout FETCH_HEAD -- . && git reset -q
  say "merging into existing pub/lab-$model ($(git rev-parse --short FETCH_HEAD))"
fi
ls -d parts/*/ >> "$L" 2>&1 || { say "no job outputs to publish"; exit 1; }
run python3 -u tools/lab/lab.py merge --model "$model" --manifest data_in/manifest.csv --run "${GITHUB_RUN_NUMBER:-0}" --out pubdir parts/*/ || exit 1
rm -rf pubdir/_ci
run bash ci/put_branch.sh "pub/lab-$model" pubdir "lab: $model" || exit 1
cp pubdir/card.json ret/ 2>/dev/null; cp pubdir/onnx/parity.json ret/ 2>/dev/null
(cd pubdir && find . -type f -not -path './.git/*' -printf '%s %p\n' | sort -k2) > ret/files.txt
say "published pub/lab-$model"
