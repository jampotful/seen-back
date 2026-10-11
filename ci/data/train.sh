#!/usr/bin/env bash
# Build the training manifest and iNaturalist's names on a build machine, publish them beside the species list and
# the evaluation manifest, and gather what comes back. Called by .github/workflows/traindata.yml.
set -uo pipefail
mkdir -p out
LOG=out/log.txt
: > "$LOG"
step() {
  local name="$1"; shift
  echo "=== $(date -u +%FT%TZ) $name" | tee -a "$LOG"
  "$@" 2>&1 | tee -a "$LOG"
  local rc=${PIPESTATUS[0]}
  echo "=== $(date -u +%FT%TZ) $name: exit $rc" | tee -a "$LOG"
  return "$rc"
}
step "install requests" python3 -m pip install --quiet requests || exit 1
step "training manifest" python3 tools/species/build_train.py --out data/train/alachua-pre2025 --cache work/cache --cap "${CAP:-60}"
rc=$?
cp data/train/alachua-pre2025/SUMMARY.md out/train-SUMMARY.md 2>/dev/null || true
if [ -f data/train/alachua-pre2025/manifest.csv ]; then
  step "rows" bash -c 'wc -l data/train/alachua-pre2025/manifest.csv; head -3 data/train/alachua-pre2025/manifest.csv; ls -la data/regions/us-fl-alachua/'
  awk -F, 'NR==1 || (NR-2)%4000==0' data/train/alachua-pre2025/manifest.csv > work/photo-check.csv
  step "photo address check" python3 tools/species/fetch_photos.py work/photo-check.csv work/photo-check --shard 0/1
fi
if [ "$rc" -eq 0 ]; then
  step "publish" bash ci/put_branch.sh pub/data-alachua data "species list, evaluation manifest, training manifest, iNaturalist names" || exit 1
fi
exit "$rc"
