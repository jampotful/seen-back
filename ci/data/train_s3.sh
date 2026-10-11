#!/usr/bin/env bash
# Build the training manifest from iNaturalist's open-data files (no API), publish it beside the species list, and
# gather what comes back. Called by .github/workflows/traindatas3.yml. See tools/species/build_train_s3.py.
#
# observations.csv.gz (13.4 GB) and photos.csv.gz (20.7 GB) in the 27 September 2026 snapshot are together larger than
# a build machine's free disk, so neither is written to disk: each is streamed from the bucket through the decompressor
# and a filter, and only the region's rows are kept. A pass whose stream breaks is run again from the start (3 tries).
# S3_BASE replaces the bucket's address (for a local test with small made-up files).
set -uo pipefail
mkdir -p out work stage
LOG=out/log.txt
: > "$LOG"
export LC_ALL=C
step() {
  local name="$1"; shift
  echo "=== $(date -u +%FT%TZ) $name" | tee -a "$LOG"
  "$@" 2>&1 | tee -a "$LOG"
  local rc=${PIPESTATUS[0]}
  echo "=== $(date -u +%FT%TZ) $name: exit $rc" | tee -a "$LOG"
  return "$rc"
}
B="${S3_BASE:-https://inaturalist-open-data.s3.amazonaws.com}"
LAT0=29.42; LAT1=29.95; LON0=-82.66; LON1=-82.05
TAB=$'\t'
AWK="$(command -v mawk || command -v awk)"
CURL=(curl -sS --fail --connect-timeout 30 --speed-limit 20000 --speed-time 300)

machine() { getconf _NPROCESSORS_ONLN; df -h . /mnt 2>/dev/null; free -m | head -2; date -u; echo "awk: $AWK"; }

get() { "${CURL[@]}" --retry 8 --retry-delay 5 --retry-all-errors -C - -o "work/$1" "$B/$1"; }

pick_unz() {           # the fastest decompressor that gives exactly gzip's output on taxa.csv.gz
  if [ -z "${S3_BASE:-}" ]; then
    command -v igzip >/dev/null || timeout 150 sudo apt-get install -y -qq --no-install-recommends isal >/dev/null 2>&1 || true
    command -v pigz >/dev/null || timeout 150 sudo apt-get install -y -qq --no-install-recommends pigz >/dev/null 2>&1 || true
  fi
  local want got z
  want="$(gzip -dc < work/taxa.csv.gz | md5sum)"
  echo "gzip -dc" > work/unz.txt
  for z in "igzip -dc" "pigz -dc"; do
    command -v "${z%% *}" >/dev/null || { echo "${z%% *}: not available"; continue; }
    got="$($z < work/taxa.csv.gz | md5sum)"
    if [ "$got" = "$want" ]; then echo "$z" > work/unz.txt; break; fi
    echo "$z gives other output than gzip -dc; not used"
  done
  echo "decompressor: $(cat work/unz.txt)"
}

obs_filter() {         # header, then only lines with a longitude beginning -82. (a fast superset), then the exact test
  { IFS= read -r h; printf '%s\n' "$h"; grep -F -e "${TAB}-82." || [ $? -eq 1 ]; } |
  "$AWK" -F'\t' -v a="$LAT0" -v b="$LAT1" -v c="$LON0" -v d="$LON1" '
    NR==1 { for (i = 1; i <= NF; i++) col[$i] = i; q = col["quality_grade"]; la = col["latitude"]; lo = col["longitude"];
            if (!q || !la || !lo || !col["observation_uuid"] || !col["taxon_id"] || !col["observed_on"]) { print "unexpected header: " $0 > "/dev/stderr"; exit 3 }
            print; next }
    $q == "research" && $la != "" && $lo != "" && $la + 0 >= a && $la + 0 <= b && $lo + 0 >= c && $lo + 0 <= d'
}

photos_filter() {      # the photos of the observations in work/uuids.txt
  "$AWK" -F'\t' '
    NR == FNR { u[$1] = 1; next }
    FNR == 1 { for (i = 1; i <= NF; i++) if ($i == "observation_uuid") c = i; if (!c) { print "unexpected header: " $0 > "/dev/stderr"; exit 3 } print; next }
    ($c in u)' work/uuids.txt -
}

stream_pass() {        # stream_pass <object> <filter> <output>: download, decompress and filter in one pipe, with retries
  local obj="$1" filt="$2" outf="$3" try s unz
  unz="$(cat work/unz.txt)"
  for try in 1 2 3; do
    "${CURL[@]}" "$B/$obj" | $unz | "$filt" > "$outf"
    s=("${PIPESTATUS[@]}")
    echo "try $try: curl ${s[0]}, decompress ${s[1]}, filter ${s[2]}; rows kept $(($(wc -l < "$outf") - 1)); $(date -u +%T)"
    if [ "${s[0]}${s[1]}${s[2]}" = "000" ]; then head -2 "$outf"; return 0; fi
    sleep 15
  done
  return 1
}

step "machine" machine
step "download taxa" get taxa.csv.gz || exit 1
step "decompressor" pick_unz
SNAP=$(curl -sI "$B/observations.csv.gz" | tr -d '\r' | awk -F': ' 'tolower($1)=="last-modified"{print $2}')
step "sizes" bash -c 'for f in observations.csv.gz photos.csv.gz; do printf "%s " "$f"; curl -sI "'"$B"'/$f" | tr -d "\r" | grep -i -E "^(content-length|last-modified):" | tr "\n" " "; echo; done'

step "observations in the box (streamed)" stream_pass observations.csv.gz obs_filter work/obs.tsv || exit 1
awk -F"\t" 'NR==1 { for (i = 1; i <= NF; i++) if ($i == "observation_uuid") c = i; next } { print $c }' work/obs.tsv > work/uuids.txt
[ -s work/uuids.txt ] || { echo "no observations in the box" | tee -a "$LOG"; exit 1; }
step "photos of those observations (streamed)" stream_pass photos.csv.gz photos_filter work/photos.tsv || exit 1

step "training manifest" python3 tools/species/build_train_s3.py --obs work/obs.tsv --photos work/photos.tsv --taxa work/taxa.csv.gz \
  --out stage/train/alachua-pre2025 --cap "${CAP:-60}" --snapshot "$SNAP"
rc=$?
cp stage/train/alachua-pre2025/SUMMARY.md out/train-SUMMARY.md 2>/dev/null || true
[ -f stage/train/alachua-pre2025/manifest.csv ] || exit 1
step "rows" bash -c 'wc -l stage/train/alachua-pre2025/manifest.csv; head -3 stage/train/alachua-pre2025/manifest.csv; sha256sum stage/train/alachua-pre2025/manifest.csv'
[ -f tools/species/check_train_s3.py ] && step "check" python3 tools/species/check_train_s3.py stage/train/alachua-pre2025/manifest.csv
gzip -c work/obs.tsv > out/obs-in-box.tsv.gz 2>/dev/null; [ "$(stat -c %s out/obs-in-box.tsv.gz 2>/dev/null || echo 0)" -lt 12000000 ] || rm -f out/obs-in-box.tsv.gz
awk -F, 'NR==1 || (NR-2)%3000==0' stage/train/alachua-pre2025/manifest.csv > work/photo-check.csv
[ -z "${S3_BASE:-}" ] && step "photo address check" python3 tools/species/fetch_photos.py work/photo-check.csv work/photo-check --shard 0/1
if [ "$rc" -eq 0 ]; then
  name=alachua-pre2025
  if [ -n "${S3_BASE:-}" ]; then
    echo "local test: not publishing" | tee -a "$LOG"; exit 0
  fi
  if git ls-remote --exit-code origin refs/heads/pub/data-alachua >/dev/null 2>&1 && git fetch -q --depth 1 origin refs/heads/pub/data-alachua \
     && git cat-file -e FETCH_HEAD:train/alachua-pre2025/manifest.csv 2>/dev/null; then
    if [ "$(git show FETCH_HEAD:train/alachua-pre2025/manifest.csv | sha256sum)" = "$(sha256sum < stage/train/alachua-pre2025/manifest.csv)" ]; then
      echo "train/alachua-pre2025/manifest.csv is already published with exactly these rows; not publishing again" | tee -a "$LOG"
      exit 0
    fi
    name=alachua-pre2025-s3      # the other route got there first; keep both, under different names
    mv stage/train/alachua-pre2025 "stage/train/$name"
  fi
  echo "publishing as train/$name" | tee -a "$LOG"
  step "publish" bash ci/data/merge_pub.sh pub/data-alachua stage "training manifest from iNaturalist's open-data files" "train/$name" || exit 1
fi
exit "$rc"
