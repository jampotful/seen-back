#!/usr/bin/env bash
# Where every species is recorded, and where the world test photos were taken (docs/tracks/worlddb.md, steps 2 to 4).
# Called by .github/workflows/worlddb.yml for run/worlddb/grid-*. From iNaturalist's open-data snapshot, with no API:
#   pass 1 over observations.csv.gz: every research-grade record dated through 2024 with a place, as its quarter-degree
#          cell and taxon; and the observations of the world test photos (lab/world-species on pub/data-world)
#   pass 2: every research-grade record of the test photos' observers, and up to 300 research-grade records from 2025 on
#          in each one-degree cell that holds a test photo (other people's creatures, for photos whose observer has met
#          too few)
# then tools/world/grid.py counts each species a cell, rasterizes Natural Earth's countries (public domain), finds the
# time zone of each test photo and each creature met in timezone-boundary-builder's polygons (ODbL; measurement only:
# nothing of it ships), and publishes the lot to pub/world-place.
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
NE="${NE_URL:-https://raw.githubusercontent.com/nvkelso/natural-earth-vector/v5.1.2/geojson/ne_50m_admin_0_countries.geojson}"
TZ_REL="${TZ_REL:-2026b}"
AWK="$(command -v mawk || command -v awk)"
CURL=(curl -sS -L --fail --connect-timeout 30 --speed-limit 20000 --speed-time 300)
get() { "${CURL[@]}" --retry 8 --retry-delay 5 --retry-all-errors -C - -o "work/$1" "$B/$1"; }
pick_unz() {
  command -v igzip >/dev/null || timeout 150 sudo apt-get install -y -qq --no-install-recommends isal >/dev/null 2>&1 || true
  command -v mawk >/dev/null || timeout 150 sudo apt-get install -y -qq --no-install-recommends mawk >/dev/null 2>&1 || true
  local want got
  want="$(gzip -dc < work/taxa.csv.gz | md5sum)"
  echo "gzip -dc" > work/unz.txt
  if command -v igzip >/dev/null; then got="$(igzip -dc < work/taxa.csv.gz | md5sum)"; [ "$got" = "$want" ] && echo "igzip -dc" > work/unz.txt; fi
  echo "decompressor: $(cat work/unz.txt)"
}
P1='
BEGIN { FS = "\t"; OFS = "\t" }
FNR == 1 { file++ }
file == 1 { t[$1] = 1; next }
FNR == 1 {
  for (i = 1; i <= NF; i++) col[$i] = i
  q = col["quality_grade"]; la = col["latitude"]; lo = col["longitude"]; tx = col["taxon_id"]; d = col["observed_on"]; u = col["observation_uuid"]; ob = col["observer_id"]
  if (!q || !la || !lo || !tx || !d || !u || !ob) { print "unexpected header: " $0 > "/dev/stderr"; exit 3 }
  next
}
{
  if ($u in t) print $u, $ob, $la, $lo, $d, $tx, $q > TEST
  if ($q != "research") next
  dd = $d; if (dd == "" || dd > "2024-12-31") next
  y = $la; x = $lo; if (y == "" || x == "" || $tx == "") next
  r = int((y + 90) * 4); c = int((x + 180) * 4)
  if (r < 0) r = 0; if (r > 719) r = 719; if (c < 0) c = 0; if (c > 1439) c = 1439
  print r * 1440 + c, $tx > REC
}'
P2='
BEGIN { FS = "\t"; OFS = "\t" }
FNR == 1 { file++ }
file == 1 { w[$1] = 1; next }
file == 2 { tc[$1] = 1; next }
FNR == 1 {
  for (i = 1; i <= NF; i++) col[$i] = i
  q = col["quality_grade"]; la = col["latitude"]; lo = col["longitude"]; tx = col["taxon_id"]; d = col["observed_on"]; u = col["observation_uuid"]; ob = col["observer_id"]
  next
}
{
  if ($q != "research") next
  y = $la; x = $lo; if (y == "" || x == "" || $tx == "") next
  if ($ob in w) print $u, $ob, y, x, $d, $tx > OBS
  if ($d >= "2025-01-01") {
    k = int(y + 90) * 360 + int(x + 180)
    if ((k in tc) && n[k] < 300) { n[k]++; print $u, $ob, y, x, $d, $tx > NEAR }
  }
}'
pass() {               # pass <program> <awk -v assignments...> -- <files before the stream...>
  local prog="$1"; shift
  local vars=() files=() try s unz
  while [ "$1" != "--" ]; do vars+=(-v "$1"); shift; done; shift
  files=("$@")
  unz="$(cat work/unz.txt)"
  for try in 1 2 3; do
    "${CURL[@]}" "$B/observations.csv.gz" | $unz | "$AWK" "${vars[@]}" "$prog" "${files[@]}" -
    s=("${PIPESTATUS[@]}")
    echo "try $try: curl ${s[0]}, decompress ${s[1]}, pass ${s[2]}; $(date -u +%T)"
    [ "${s[0]}${s[1]}${s[2]}" = "000" ] && return 0
    sleep 15
  done
  return 1
}
step "machine" bash -c 'getconf _NPROCESSORS_ONLN; df -h . | tail -1; free -m | head -2'
step "install" python3 -m pip install --quiet numpy pandas shapely || exit 1
step "world test photos" bash -c 'git fetch -q --depth 1 origin pub/data-world && git show FETCH_HEAD:lab/world-species/manifest.csv > work/test_manifest.csv && git rev-parse FETCH_HEAD > work/data_world_sha.txt && wc -l work/test_manifest.csv' || exit 1
python3 -I -c "
import csv
with open('work/test_uuids.txt', 'w') as f:
    for r in csv.DictReader(open('work/test_manifest.csv', encoding='utf-8')):
        f.write(r['obs_url'].rstrip('/').split('/')[-1].lower() + '\n')
" || exit 1
step "taxa" get taxa.csv.gz || exit 1
step "decompressor" pick_unz
AWK="$(command -v mawk || command -v awk)"
SNAP=$(curl -sI "$B/observations.csv.gz" | tr -d '\r' | awk -F': ' 'tolower($1)=="last-modified"{print $2}')
echo "$SNAP" > work/snapshot.txt
step "group and species of every taxon" python3 -I tools/world/groups.py --taxa work/taxa.csv.gz --out work/taxmap.tsv || exit 1
step "pass 1: records through 2024, and the test photos (streamed)" pass "$P1" TEST=work/test_obs.tsv REC=work/rec.tsv -- work/test_uuids.txt || exit 1
step "what pass 1 kept" bash -c 'wc -l work/test_obs.tsv work/rec.tsv; ls -la work'
step "names of the rows (the rows run's names job)" bash -c '
  for i in $(seq 1 60); do
    git fetch -q --depth 1 origin ci
    run=$(git show FETCH_HEAD:INDEX.txt | grep -E " runs/worlddb/[0-9]+-names success " | tail -1 | cut -d" " -f2)
    [ -n "$run" ] && break
    echo "[$(date -u +%T)] waiting for a names job to return"; sleep 60
  done
  [ -n "$run" ] || { echo "no names job has returned"; exit 1; }
  echo "$run" > work/names_run.txt
  git show "FETCH_HEAD:$run/inat_rows.tsv.gz" | gunzip > work/inat_rows.tsv && git show "FETCH_HEAD:$run/rows.tsv.gz" | gunzip > work/rows.tsv && wc -l work/inat_rows.tsv work/rows.tsv && echo "from $run"' || exit 1
cut -f2 work/test_obs.tsv | sort -u > work/observers.txt
python3 -I -c "
for line in open('work/test_obs.tsv'):
    p = line.rstrip('\n').split('\t')
    if p[2] and p[3]:
        print(int(float(p[2]) + 90) * 360 + int(float(p[3]) + 180))
" | sort -u > work/test_cells.txt
step "pass 2: the observers' records, and other people's near the test photos (streamed)" pass "$P2" OBS=work/obs.tsv NEAR=work/near.tsv -- work/observers.txt work/test_cells.txt || exit 1
step "what pass 2 kept" bash -c 'wc -l work/observers.txt work/test_cells.txt work/obs.tsv work/near.tsv'
step "Natural Earth countries" "${CURL[@]}" --retry 5 -o work/ne.geojson "$NE" || exit 1
step "time-zone polygons" bash -c '
  tag=$(curl -sS https://api.github.com/repos/evansiroky/timezone-boundary-builder/releases/latest | python3 -c "import json,sys; print(json.load(sys.stdin)[\"tag_name\"])")
  echo "timezone-boundary-builder release: $tag"; echo "$tag" > work/tzb_tag.txt
  curl -sS -L --fail --retry 5 -o work/tz.zip "https://github.com/evansiroky/timezone-boundary-builder/releases/download/$tag/timezones.geojson.zip" && unzip -o -q work/tz.zip -d work/tz && ls -la work/tz' || exit 1
step "tz database ($TZ_REL)" bash -c "mkdir -p work/tzdb && for f in zone1970.tab zone.tab backward iso3166.tab; do ${CURL[*]} -o work/tzdb/\$f https://raw.githubusercontent.com/eggert/tz/$TZ_REL/\$f || exit 1; done; ls -la work/tzdb" || exit 1
step "cells, places and zones" python3 -I tools/world/grid.py --rec work/rec.tsv --taxmap work/taxmap.tsv --inat-rows work/inat_rows.tsv \
  --test-manifest work/test_manifest.csv --test-obs work/test_obs.tsv --obs work/obs.tsv --near work/near.tsv \
  --countries work/ne.geojson --tz "$(ls work/tz/*.json work/tz/*/*.json 2>/dev/null | head -1)" --out stage || exit 1
cp -R work/tzdb stage/tzdb
{ echo "snapshot=$SNAP"; echo "names_run=$(cat work/names_run.txt)"; echo "data_world=$(cat work/data_world_sha.txt)"; echo "timezone_boundary_builder=$(cat work/tzb_tag.txt)"; echo "tzdb=$TZ_REL"; } > stage/SOURCES.txt
cp stage/SOURCES.txt stage/summary.json out/ 2>/dev/null
ls -la stage | tee -a "$LOG"
step "publish" bash ci/put_branch.sh pub/world-place stage "where species are recorded, and the world test photos' places" || exit 1
exit 0
