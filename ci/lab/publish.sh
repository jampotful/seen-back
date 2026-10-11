#!/usr/bin/env bash
# Merge one model's job outputs with what its pub/lab-<model> branch already holds, and publish the branch.
# Usage: bash ci/lab/publish.sh <model>   (parts/ holds one directory per job artifact; data_in/ the manifest)
set -uo pipefail
model="$1"; mkdir -p ret pubdir
L=ret/log.txt
say() { echo "[$(date -u +%T)] $*" | tee -a "$L"; }
run() { say "+ $*"; "$@" >> "$L" 2>&1; local rc=$?; say "exit $rc"; return $rc; }
for d in parts/*/; do [ -f "$d/_ci/log.txt" ] && { echo "==== job log $d"; cat "$d/_ci/log.txt"; } >> "$L"; done
if git ls-remote --exit-code origin "refs/heads/pub/lab-$model" >/dev/null 2>&1; then
  git fetch -q --depth 1 origin "pub/lab-$model" && git --work-tree=pubdir checkout FETCH_HEAD -- . && git reset -q
  say "merging into existing pub/lab-$model ($(git rev-parse --short FETCH_HEAD))"
fi
ls -d parts/*/ >> "$L" 2>&1 || { say "no job outputs to publish"; exit 1; }
run python3 -u tools/lab/lab.py merge --model "$model" --manifest data_in/manifest.csv --out pubdir parts/*/ || exit 1
rm -rf pubdir/_ci
run bash ci/put_branch.sh "pub/lab-$model" pubdir "lab: $model" || exit 1
cp pubdir/card.json ret/ 2>/dev/null; cp pubdir/onnx/parity.json ret/ 2>/dev/null
(cd pubdir && find . -type f -not -path './.git/*' -printf '%s %p\n' | sort -k2) > ret/files.txt
say "published pub/lab-$model"
