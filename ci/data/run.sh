#!/usr/bin/env bash
# Build the species list and the evaluation manifest on a build machine, publish them, and gather what comes back.
# Called by .github/workflows/data.yml. Every step's output goes into out/log.txt, which is returned on the ci branch.
set -uo pipefail
mkdir -p out out/diag
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
counts() {
  python3 - <<'PY' > out/counts.txt 2>&1
import csv, json, os
from collections import Counter
p = "data/regions/us-fl-alachua/species.json"
if os.path.exists(p):
    d = json.load(open(p, encoding="utf-8"))
    sp = d["species"]
    print("species.json: %d species, %d records, retrieved %s, through %s" % (
        len(sp), sum(s["n"] for s in sp), d["source"]["retrieved"], d["source"]["records_through"]))
q = "data/eval/alachua-2025/manifest.csv"
if os.path.exists(q):
    rows = list(csv.DictReader(open(q, encoding="utf-8")))
    print("manifest.csv: %d rows, columns %s" % (len(rows), list(rows[0].keys()) if rows else []))
    print("  splits %s" % dict(Counter(r["split"] for r in rows)))
    print("  dates %s .. %s" % (min(r["date"] for r in rows), max(r["date"] for r in rows)))
PY
  cat out/counts.txt | tee -a "$LOG"
}

step "machine" bash -c 'python3 --version; uname -a; getconf _NPROCESSORS_ONLN; date -u'
step "install requests" python3 -m pip install --quiet requests || exit 1
step "unit tests" python3 -m unittest discover -s tools/species -v || exit 1

step "species list" python3 tools/species/build_species.py --out data/regions/us-fl-alachua --cache work/cache --diag out/diag
rc_species=$?
cp data/regions/us-fl-alachua/SUMMARY.md out/species-SUMMARY.md 2>/dev/null || true
if [ "$rc_species" -eq 0 ] && [ "${PUBLISH:-1}" = "1" ]; then
  step "publish species list" bash ci/put_branch.sh pub/data-alachua data "species list"
fi
[ -f data/regions/us-fl-alachua/species.json ] || { counts; exit 1; }

step "evaluation manifest" python3 tools/species/build_eval.py --out data/eval/alachua-2025 --end 2026-09-29 \
  --species data/regions/us-fl-alachua/species.json --cache work/cache --diag out/diag
rc_eval=$?
cp data/eval/alachua-2025/SUMMARY.md out/eval-SUMMARY.md 2>/dev/null || true
counts

if [ -f data/eval/alachua-2025/manifest.csv ]; then
  # A few rows spread over the whole period: are the medium-size addresses served?
  awk -F, 'NR==1 || (NR-2)%200==0' data/eval/alachua-2025/manifest.csv > work/photo-check.csv
  step "photo address check" python3 tools/species/fetch_photos.py work/photo-check.csv work/photo-check --shard 0/1
  step "photo files" bash -c 'ls work/photo-check | head -5; file work/photo-check/*.jpg 2>/dev/null | head -3 || true; du -sh work/photo-check'
  head -3 data/eval/alachua-2025/manifest.csv > out/manifest-head.csv
fi

if [ "$rc_species" -eq 0 ] && [ "$rc_eval" -eq 0 ] && [ "${PUBLISH:-1}" = "1" ]; then
  step "publish species list and manifest" bash ci/put_branch.sh pub/data-alachua data "species list and evaluation manifest" || exit 1
fi
[ "$rc_species" -eq 0 ] && [ "$rc_eval" -eq 0 ]
