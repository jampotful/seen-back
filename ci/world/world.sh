#!/usr/bin/env bash
# World photos for the 33 groups (docs/COVERAGE.md), from iNaturalist's open-data files with no API, published to
# pub/data-world. Called by .github/workflows/world.yml; see tools/world/README.md.
#
# taxa.csv.gz is downloaded whole. observations.csv.gz (13.4 GB) and photos.csv.gz (20.7 GB) are each streamed once
# through the decompressor and mawk and never written to disk. The observation pass keeps, for each species, at most
# three research-grade observations a continent dated through 2024, three dated 2025 or later, and two casual ones
# (60, 60 and 20 in the ten groups with fewest species, 20, 20 and 6 in the next seven), plus a thin even sample of research-grade observations from 2025 on, and counts every research-grade and casual
# observation by group, continent and period. tools/world/select.py ranks from those; the photo pass fetches the
# photos of the ranked observations; select.py keeps those the licence rule allows. S3_BASE replaces the bucket's
# address and NE_URL Natural Earth's, for a local test.
set -uo pipefail
mkdir -p out work stage/world
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
NE="${NE_URL:-https://raw.githubusercontent.com/nvkelso/natural-earth-vector/v5.1.2/geojson/ne_50m_admin_0_countries.geojson}"
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

# The observation pass. Files in order: the taxon map, the continent grid, then the observations on standard input.
OBS='
BEGIN { FS = "\t"; OFS = "\t"
  # the even sample keeps an observation when the first three hex digits of its id fall under the continent limit
  lim["NA"] = "003"; lim["EU"] = "003"; lim["AS"] = "010"; lim["OC"] = "010"; lim["AF"] = "020"; lim["SA"] = "020"; lim["AN"] = "fff~"
  # groups with few species keep more observations of each, so that their sets can still fill (run 1 of the job)
  n1 = split("cat dog alligator rabbit tick flyingfox deer whale cephalopod primate", g1, " ")
  for (i = 1; i <= n1; i++) cap[g1[i]] = 60
  n2 = split("hawk salamander slime shark bat mammal wader", g2, " ")
  for (i = 1; i <= n2; i++) cap[g2[i]] = 20 }
FNR == 1 { file++ }
file == 1 { tm[$1] = $2 "\t" $3 "\t" $4; next }
file == 2 { gr[$1] = $2; next }
FNR == 1 {
  for (i = 1; i <= NF; i++) col[$i] = i
  q = col["quality_grade"]; la = col["latitude"]; lo = col["longitude"]; t = col["taxon_id"]; d = col["observed_on"]
  u = col["observation_uuid"]; ob = col["observer_id"]
  if (!q || !la || !lo || !t || !d || !u || !ob) { print "unexpected header: " $0 > "/dev/stderr"; exit 3 }
  next
}
{
  g = $q
  if (g != "research" && g != "casual") next
  tx = $t
  if (!(tx in tm)) { nomap[g]++; next }
  split(tm[tx], m, "\t"); grp = m[1]
  if (grp == "person") { skipped[grp]++; next }
  y = $la; x = $lo
  if (y == "" || x == "") { noplace[g]++; next }
  r = int((y + 90) * 2); c = int((x + 180) * 2)
  if (r < 0) r = 0; if (r > 359) r = 359; if (c < 0) c = 0; if (c > 719) c = 719
  k0 = gr[r * 720 + c]
  if (g == "casual") {
    cnt[grp "\t" k0 "\tC"]++
    key = m[2] SUBSEP k0
    if (nc[key] < ((grp in cap) ? cap[grp] / 3 : 2)) { nc[key]++; print "C", grp, k0, "C", m[3], m[2], tx, $u, $ob, $d > CAS }
    next
  }
  dd = $d
  if (dd == "") { nodate++; next }
  per = (dd <= "2024-12-31") ? "F" : "E"
  cnt[grp "\t" k0 "\t" per]++
  key = m[2] SUBSEP k0 SUBSEP per
  if (n[key] < ((grp in cap) ? cap[grp] : 3)) { n[key]++; print "R", grp, k0, per, m[3], m[2], tx, $u, $ob, dd > CAND }
  if (per == "E" && substr(tolower($u), 1, 3) < lim[k0]) print "R", grp, k0, per, m[3], m[2], tx, $u, $ob, dd > EVEN
}
END {
  for (k in cnt) print k, cnt[k] > CNT
  for (k in nomap) print "no taxon in the map, " k ": " nomap[k] > "/dev/stderr"
  for (k in skipped) print "left out as " k ": " skipped[k] > "/dev/stderr"
  for (k in noplace) print "no place, " k ": " noplace[k] > "/dev/stderr"
  print "research grade with no date: " nodate + 0 > "/dev/stderr"
}'

obs_pass() {
  local try s unz
  unz="$(cat work/unz.txt)"
  for try in 1 2 3; do
    rm -f work/cand.tsv work/casual.tsv work/even.tsv work/counts.tsv
    "${CURL[@]}" "$B/observations.csv.gz" | $unz | "$AWK" -v CAND=work/cand.tsv -v CAS=work/casual.tsv -v EVEN=work/even.tsv \
      -v CNT=work/counts.tsv "$OBS" work/taxmap.tsv work/grid.tsv -
    s=("${PIPESTATUS[@]}")
    echo "try $try: curl ${s[0]}, decompress ${s[1]}, pass ${s[2]}; $(date -u +%T)"
    if [ "${s[0]}${s[1]}${s[2]}" = "000" ]; then wc -l work/cand.tsv work/casual.tsv work/even.tsv work/counts.tsv; return 0; fi
    sleep 15
  done
  return 1
}

photos_pass() {
  local try s unz
  unz="$(cat work/unz.txt)"
  for try in 1 2 3; do
    "${CURL[@]}" "$B/photos.csv.gz" | $unz | "$AWK" -F'\t' '
      NR == FNR { w[$1] = 1; next }
      FNR == 1 { for (i = 1; i <= NF; i++) if ($i == "observation_uuid") c = i; if (!c) { print "unexpected header: " $0 > "/dev/stderr"; exit 3 } print; next }
      ($c in w)' work/uuids.txt - > work/photos.tsv
    s=("${PIPESTATUS[@]}")
    echo "try $try: curl ${s[0]}, decompress ${s[1]}, filter ${s[2]}; rows kept $(($(wc -l < work/photos.tsv) - 1)); $(date -u +%T)"
    if [ "${s[0]}${s[1]}${s[2]}" = "000" ]; then head -2 work/photos.tsv; return 0; fi
    sleep 15
  done
  return 1
}

address_check() {      # twenty of the chosen photo addresses answer
  local bad=0 n=0 url
  for url in $(tail -n +2 stage/world/fit.csv | awk -F, 'NR % 150 == 1 { print $13 }' | head -20); do
    n=$((n + 1))
    if ! curl -sSfI --retry 3 -o /dev/null "$url"; then bad=$((bad + 1)); echo "no answer: $url"; fi
  done
  echo "photo addresses checked: $n, without an answer: $bad"
  for url in $(tail -n +2 stage/world/fit.csv | awk -F, 'NR % 900 == 1 { print $12 }' | head -3); do   # an observation's address by its id
    echo "observation address $url: $(curl -sS -o /dev/null -L -w '%{http_code} after %{num_redirects} redirects' "$url" 2>&1)"
  done
  [ "$bad" -eq 0 ]
}

step "machine" machine
step "download taxa" get taxa.csv.gz || exit 1
step "decompressor" pick_unz
AWK="$(command -v mawk || command -v awk)"
SNAP=$(curl -sI "$B/observations.csv.gz" | tr -d '\r' | awk -F': ' 'tolower($1)=="last-modified"{print $2}')
step "sizes" bash -c 'for f in observations.csv.gz photos.csv.gz taxa.csv.gz; do printf "%s " "$f"; curl -sI "'"$B"'/$f" | tr -d "\r" | grep -i -E "^(content-length|last-modified):" | tr "\n" " "; echo; done'
step "group rules" python3 -I tools/world/test_groups.py || exit 1
step "group of every taxon" python3 -I tools/world/groups.py --taxa work/taxa.csv.gz --out work/taxmap.tsv --summary out/groups-taxa.tsv || exit 1
step "Natural Earth countries" "${CURL[@]}" --retry 5 -o work/ne.geojson "$NE" || exit 1
step "continent grid" python3 -I tools/world/continents.py --geojson work/ne.geojson --out work/grid.tsv --map out/continents-map.txt || exit 1
step "observations (streamed)" obs_pass || exit 1
sort -t$'\t' -k1,1 -k2,2 -k3,3 work/counts.tsv > out/counts.tsv
step "rank" python3 -I tools/world/select.py pick --cand work/cand.tsv --casual work/casual.tsv --even work/even.tsv \
  --out work/ranked.tsv --uuids work/uuids.txt || exit 1
step "photos of the ranked observations (streamed)" photos_pass || exit 1
step "manifests" python3 -I tools/world/select.py finish --ranked work/ranked.tsv --photos work/photos.tsv --taxa work/taxa.csv.gz \
  --counts out/counts.tsv --out stage/world --snapshot "$SNAP" || exit 1
cp stage/world/SUMMARY.md out/
cp work/grid.tsv stage/world/continents-0.5deg.tsv
cp out/counts.tsv stage/world/records-by-group.tsv
cat > stage/world/README.md <<EOF
# World photos

Lists of iNaturalist photos for fitting, tuning and testing the base app's group head on the 33 groups of
docs/COVERAGE.md, and for the full database's world test. Made by tools/world/select.py through ci/world/world.sh
from iNaturalist's open-data snapshot of ${SNAP:-an unrecorded date}. Each row gives the observation's address,
the photo's address and the photo's licence; the photographer is named on the observation's page.

- fit.csv, tune.csv, test.csv, casual.csv, species.csv: the sets (SUMMARY.md says what each holds).
- records-by-group.tsv: research-grade (F through 2024, E from 2025) and casual (C) observations by group and continent.
- lab/world-fit, lab/world-eval, lab/world-species: the same rows as manifests for tools/lab (an id and a split added).
- continents-0.5deg.tsv: the continent of each half-degree cell, from Natural Earth's countries at 1:50 million
  (public domain, https://www.naturalearthdata.com), as tools/world/continents.py makes it.
EOF
if [ -n "${S3_BASE:-}" ]; then echo "local test: not checking photo addresses and not publishing" | tee -a "$LOG"; exit 0; fi
step "photo address check" address_check || exit 1
step "publish" bash ci/put_branch.sh pub/data-world stage/world "world photos for the 33 groups" || exit 1
exit 0
