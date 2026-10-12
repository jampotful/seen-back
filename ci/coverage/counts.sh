#!/usr/bin/env bash
# Counts for docs/COVERAGE.md from iNaturalist's open-data files, with no API. Called by .github/workflows/coverage.yml.
#
# taxa.csv.gz is downloaded whole. observations.csv.gz (13.4 GB in the 27 September 2026 snapshot) is streamed once
# through the decompressor and mawk and never written to disk. Written to work/counts/, one taxon a line:
#   world_rg_all, world_rg_2024   research-grade observations of each taxon, all time and dated through 2024-12-31
#   world_casual                  casual observations (captive or cultivated, or missing evidence), all time
#   alachua_*                     inside the box the Alachua County list was built from (all time, through 2024)
#   usa48_*                       inside a box round the lower 48 states
#   gnv25, gnv100_*, gnv400_*, gnv1600_*   within 25, 100, 400 and 1600 km of Gainesville (29.65 N, 82.32 W), haversine
# and work/counts/totals.tsv (rows by quality grade). S3_BASE replaces the bucket's address for a local test.
set -uo pipefail
mkdir -p out work/counts
LOG=out/log-counts.txt
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
AWK="$(command -v mawk || command -v awk)"
CURL=(curl -sS --fail --connect-timeout 30 --speed-limit 20000 --speed-time 300)

machine() { getconf _NPROCESSORS_ONLN; df -h . 2>/dev/null; free -m | head -2; date -u; echo "awk: $AWK"; }
get() { "${CURL[@]}" --retry 8 --retry-delay 5 --retry-all-errors -C - -o "work/$1" "$B/$1"; }

pick_unz() {           # the fastest decompressor that gives exactly gzip's output on taxa.csv.gz
  if [ -z "${S3_BASE:-}" ]; then
    command -v igzip >/dev/null || timeout 150 sudo apt-get install -y -qq --no-install-recommends isal >/dev/null 2>&1 || true
    command -v pigz >/dev/null || timeout 150 sudo apt-get install -y -qq --no-install-recommends pigz >/dev/null 2>&1 || true
    command -v mawk >/dev/null || timeout 150 sudo apt-get install -y -qq --no-install-recommends mawk >/dev/null 2>&1 || true
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

# One pass over every observation. Arrays are printed at the end, one file each.
AGG='
BEGIN { FS = "\t"; OFS = "\t"; D = 3.14159265358979 / 180; la0 = 29.65; lo0 = -82.32; c0 = cos(la0 * D) }
NR == 1 {
  for (i = 1; i <= NF; i++) col[$i] = i
  q = col["quality_grade"]; la = col["latitude"]; lo = col["longitude"]; t = col["taxon_id"]; d = col["observed_on"]
  if (!q || !la || !lo || !t || !d) { print "unexpected header: " $0 > "/dev/stderr"; exit 3 }
  next
}
{
  g = $q; tot[g]++
  tx = $t
  if (tx == "") { notaxon[g]++; next }
  if (g == "casual") { cas[tx]++; next }
  if (g != "research") next
  old = ($d != "" && $d <= "2024-12-31")
  wa[tx]++; if (old) wo[tx]++
  y = $la; x = $lo
  if (y == "" || x == "") next
  y += 0; x += 0
  if (y >= 29.42 && y <= 29.95 && x >= -82.66 && x <= -82.05) { aa[tx]++; if (old) ao[tx]++ }
  if (y >= 24.3 && y <= 49.5 && x >= -125.0 && x <= -66.8) { ua[tx]++; if (old) uo[tx]++ }
  if (y > 14.5 && y < 44.9 && x > -99.0 && x < -65.6) {
    p2 = y * D; dp = (y - la0) * D; dl = (x - lo0) * D
    s1 = sin(dp / 2); s2 = sin(dl / 2)
    h = s1 * s1 + c0 * cos(p2) * s2 * s2
    km = 2 * 6371.0088 * atan2(sqrt(h), sqrt(1 - h))
    if (km <= 1600) {
      k1a[tx]++; if (old) k1o[tx]++
      if (km <= 400) {
        k4a[tx]++; if (old) k4o[tx]++
        if (km <= 100) {
          k0a[tx]++; if (old) k0o[tx]++
          if (km <= 25) k25[tx]++
        }
      }
    }
  }
}
END {
  for (k in tot) print k, tot[k] > (O "/totals.tsv")
  for (k in notaxon) print "no taxon " k, notaxon[k] > (O "/totals.tsv")
  for (k in wa) print k, wa[k] > (O "/world_rg_all.tsv")
  for (k in wo) print k, wo[k] > (O "/world_rg_2024.tsv")
  for (k in cas) print k, cas[k] > (O "/world_casual.tsv")
  for (k in aa) print k, aa[k] > (O "/alachua_all.tsv")
  for (k in ao) print k, ao[k] > (O "/alachua_2024.tsv")
  for (k in ua) print k, ua[k] > (O "/usa48_all.tsv")
  for (k in uo) print k, uo[k] > (O "/usa48_2024.tsv")
  for (k in k25) print k, k25[k] > (O "/gnv25_all.tsv")
  for (k in k0a) print k, k0a[k] > (O "/gnv100_all.tsv")
  for (k in k0o) print k, k0o[k] > (O "/gnv100_2024.tsv")
  for (k in k4a) print k, k4a[k] > (O "/gnv400_all.tsv")
  for (k in k4o) print k, k4o[k] > (O "/gnv400_2024.tsv")
  for (k in k1a) print k, k1a[k] > (O "/gnv1600_all.tsv")
  for (k in k1o) print k, k1o[k] > (O "/gnv1600_2024.tsv")
}'

agg_pass() {           # download, decompress and count in one pipe, with retries
  local try s unz
  unz="$(cat work/unz.txt)"
  for try in 1 2 3; do
    rm -f work/counts/*.tsv
    "${CURL[@]}" "$B/observations.csv.gz" | $unz | "$AWK" -v O=work/counts "$AGG"
    s=("${PIPESTATUS[@]}")
    echo "try $try: curl ${s[0]}, decompress ${s[1]}, count ${s[2]}; $(date -u +%T)"
    if [ "${s[0]}${s[1]}${s[2]}" = "000" ]; then wc -l work/counts/*.tsv; cat work/counts/totals.tsv; return 0; fi
    sleep 15
  done
  return 1
}

step "machine" machine
step "download taxa" get taxa.csv.gz || exit 1
step "decompressor" pick_unz
AWK="$(command -v mawk || command -v awk)"
SNAP=$(curl -sI "$B/observations.csv.gz" | tr -d '\r' | awk -F': ' 'tolower($1)=="last-modified"{print $2}')
echo "$SNAP" > work/counts/snapshot.txt
step "sizes" bash -c 'for f in observations.csv.gz taxa.csv.gz; do printf "%s " "$f"; curl -sI "'"$B"'/$f" | tr -d "\r" | grep -i -E "^(content-length|last-modified):" | tr "\n" " "; echo; done'
step "header" bash -c "curl -sS -r 0-2000 '$B/observations.csv.gz' | gzip -dc 2>/dev/null | head -3"
step "count every observation (streamed)" agg_pass || exit 1
cp work/taxa.csv.gz work/counts/
exit 0
