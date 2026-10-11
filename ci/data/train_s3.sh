#!/usr/bin/env bash
# Build the training manifest from iNaturalist's open-data files (no API), publish it beside the species list, and
# gather what comes back. Called by .github/workflows/traindatas3.yml. See tools/species/build_train_s3.py.
set -uo pipefail
mkdir -p out work stage
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
B=https://inaturalist-open-data.s3.amazonaws.com
LAT0=29.42; LAT1=29.95; LON0=-82.66; LON1=-82.05
get() { curl -sS --fail --retry 8 --retry-delay 5 --retry-all-errors -C - -o "work/$1" "$B/$1"; }
step "machine" bash -c 'getconf _NPROCESSORS_ONLN; df -h . | tail -1; date -u'
step "download taxa" get taxa.csv.gz || exit 1
( get observations.csv.gz; echo "observations download: exit $?" ) > work/dl-obs.log 2>&1 &
( get photos.csv.gz; echo "photos download: exit $?" ) > work/dl-photos.log 2>&1 &
wait
step "downloads" bash -c 'cat work/dl-obs.log work/dl-photos.log; ls -la work/*.gz; curl -sI '"$B"'/observations.csv.gz | grep -i last-modified'
grep -q "observations download: exit 0" work/dl-obs.log && grep -q "photos download: exit 0" work/dl-photos.log || exit 1
SNAP=$(curl -sI "$B/observations.csv.gz" | tr -d '\r' | awk -F': ' 'tolower($1)=="last-modified"{print $2}')

step "observations in the box" bash -c '
  gzip -dc work/observations.csv.gz | awk -F"\t" -v a='"$LAT0"' -v b='"$LAT1"' -v c='"$LON0"' -v d='"$LON1"' '"'"'
    NR==1 { for (i = 1; i <= NF; i++) col[$i] = i; q = col["quality_grade"]; la = col["latitude"]; lo = col["longitude"];
            if (!q || !la || !lo || !col["observation_uuid"] || !col["taxon_id"] || !col["observed_on"]) { print "unexpected header: " $0 > "/dev/stderr"; exit 3 }
            print; next }
    $q == "research" && $la != "" && $lo != "" && $la + 0 >= a && $la + 0 <= b && $lo + 0 >= c && $lo + 0 <= d
  '"'"' > work/obs.tsv; echo "rows: $(($(wc -l < work/obs.tsv) - 1))"; head -2 work/obs.tsv' || exit 1
rm -f work/observations.csv.gz
awk -F"\t" 'NR==1 { for (i = 1; i <= NF; i++) if ($i == "observation_uuid") c = i; next } { print $c }' work/obs.tsv > work/uuids.txt
step "photos of those observations" bash -c '
  gzip -dc work/photos.csv.gz | awk -F"\t" '"'"'
    NR == FNR { u[$1] = 1; next }
    FNR == 1 { for (i = 1; i <= NF; i++) if ($i == "observation_uuid") c = i; if (!c) { print "unexpected header: " $0 > "/dev/stderr"; exit 3 } print; next }
    ($c in u)
  '"'"' work/uuids.txt - > work/photos.tsv; echo "rows: $(($(wc -l < work/photos.tsv) - 1))"; head -2 work/photos.tsv' || exit 1
rm -f work/photos.csv.gz

step "training manifest" python3 tools/species/build_train_s3.py --obs work/obs.tsv --photos work/photos.tsv --taxa work/taxa.csv.gz \
  --out stage/train/alachua-pre2025 --cap "${CAP:-60}" --snapshot "$SNAP"
rc=$?
cp stage/train/alachua-pre2025/SUMMARY.md out/train-SUMMARY.md 2>/dev/null || true
[ -f stage/train/alachua-pre2025/manifest.csv ] || exit 1
step "rows" bash -c 'wc -l stage/train/alachua-pre2025/manifest.csv; head -3 stage/train/alachua-pre2025/manifest.csv'
step "check" python3 tools/species/check_train.py stage/train/alachua-pre2025/manifest.csv || true
awk -F, 'NR==1 || (NR-2)%3000==0' stage/train/alachua-pre2025/manifest.csv > work/photo-check.csv
step "photo address check" python3 tools/species/fetch_photos.py work/photo-check.csv work/photo-check --shard 0/1
if [ "$rc" -eq 0 ]; then
  name=alachua-pre2025
  if git ls-remote --exit-code origin refs/heads/pub/data-alachua >/dev/null 2>&1 && git fetch -q --depth 1 origin refs/heads/pub/data-alachua \
     && git cat-file -e FETCH_HEAD:train/alachua-pre2025/manifest.csv 2>/dev/null; then
    name=alachua-pre2025-s3      # the other route got there first; keep both, under different names
    mv stage/train/alachua-pre2025 "stage/train/$name"
  fi
  echo "publishing as train/$name" | tee -a "$LOG"
  step "publish" bash ci/data/merge_pub.sh pub/data-alachua stage "training manifest from iNaturalist's open-data files" "train/$name" || exit 1
fi
exit "$rc"
