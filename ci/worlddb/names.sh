#!/usr/bin/env bash
# GBIF's names and iNaturalist's English names for every species of the world list (tools/world/names.py).
# Called by .github/workflows/worlddb.yml. The world list is the coverage study's (runs/coverage/2-lists on ci);
# iNaturalist's taxonomy comes from its open-data bucket and its taxonomy archive, GBIF's from its backbone archive.
set -uo pipefail
mkdir -p out work names
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
B="${S3_BASE:-https://inaturalist-open-data.s3.amazonaws.com}"
GBIF="${GBIF_BACKBONE:-https://hosted-datasets.gbif.org/datasets/backbone/current/backbone.zip}"
INAT="${INAT_DWCA:-https://www.inaturalist.org/taxa/inaturalist-taxonomy.dwca.zip}"
CURL=(curl -sS -L --fail --connect-timeout 30 --retry 6 --retry-delay 10 --retry-all-errors)
step "machine" bash -c 'getconf _NPROCESSORS_ONLN; df -h . | tail -1; free -m | head -2'
step "the world list (coverage run 2)" bash -c 'git fetch -q --depth 1 origin ci && git show FETCH_HEAD:runs/coverage/2-lists/world.tsv.gz > work/world.tsv.gz && git show FETCH_HEAD:runs/coverage/2-lists/_meta.txt && zcat work/world.tsv.gz | wc -l' || exit 1
step "iNaturalist taxa" "${CURL[@]}" -o work/taxa.csv.gz "$B/taxa.csv.gz" || exit 1
step "GBIF backbone" bash -c "curl -sSI -L '$GBIF' | tr -d '\r' | grep -i -E '^(HTTP|content-length|last-modified)'; ${CURL[*]} -o work/backbone.zip '$GBIF' && ls -la work/backbone.zip && unzip -l work/backbone.zip" || exit 1
core=$(unzip -Z1 work/backbone.zip | grep -i -E '(^|/)taxon\.(tsv|txt)$' | head -1)
step "backbone core file ($core)" bash -c "unzip -p work/backbone.zip '$core' > work/Taxon.tsv && wc -l work/Taxon.tsv && head -2 work/Taxon.tsv" || exit 1
unzip -p work/backbone.zip eml.xml > out/gbif-backbone-eml.xml 2>/dev/null || true
rm -f work/backbone.zip
vern=""
if step "iNaturalist taxonomy archive" bash -c "${CURL[*]} -o work/inat.zip '$INAT' && ls -la work/inat.zip && unzip -l work/inat.zip | head -80"; then
  f=$(unzip -Z1 work/inat.zip | grep -i -E 'vernacularnames-english\.csv$' | head -1)
  if [ -n "$f" ]; then unzip -p work/inat.zip "$f" > work/vern-en.csv && vern=work/vern-en.csv && head -3 "$vern" | tee -a "$LOG"; fi
  unzip -p work/inat.zip eml.xml > out/inat-taxonomy-eml.xml 2>/dev/null || true
  rm -f work/inat.zip
fi
step "group of every taxon" python3 -I tools/world/groups.py --taxa work/taxa.csv.gz --out work/taxmap.tsv || exit 1
step "names" python3 -I tools/world/names.py --world work/world.tsv.gz --taxa work/taxa.csv.gz --backbone work/Taxon.tsv \
  ${vern:+--vernacular "$vern"} --county models/naturalist/species.json --out names || exit 1
cp names/summary.json out/
head -301 names/rows.tsv > out/rows-head.tsv
gzip -c names/rows.tsv > out/rows.tsv.gz
gzip -c names/inat_rows.tsv > out/inat_rows.tsv.gz
exit 0
