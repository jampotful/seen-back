#!/usr/bin/env bash
# Put the species list and evaluation manifest in data_in/: from pub/data-alachua when it exists (or when asked),
# otherwise a stand-in made from GBIF by tools/lab/standin.py. Usage: bash ci/lab/data.sh <auto|pub/data-alachua|standin>
set -uo pipefail
want="${1:-auto}"; manpath="${2:-}"; waitmin="${3:-0}"; waitfile="${4:-}"
# Optionally wait (up to waitmin minutes) for the manifest to appear on pub/data-alachua, and for a file on another
# branch (waitfile: JSON ["<branch>", "<path>"]), e.g. an earlier run's published vectors.
t0=$(date +%s)
if [ -n "$manpath" ] && [ "${waitmin:-0}" -gt 0 ]; then
  until git fetch -q --depth 1 origin pub/data-alachua 2>/dev/null && git cat-file -e "FETCH_HEAD:$manpath" 2>/dev/null; do
    [ $(( $(date +%s) - t0 )) -ge $(( waitmin * 60 )) ] && { echo "waited $waitmin minutes; $manpath never appeared"; exit 1; }
    echo "[$(date -u +%T)] waiting for $manpath on pub/data-alachua"; sleep 60
  done
fi
if [ -n "$waitfile" ] && [ "$waitfile" != '""' ]; then
  wb=$(python3 -c "import json,sys;print(json.loads(sys.argv[1])[0])" "$waitfile"); wf=$(python3 -c "import json,sys;print(json.loads(sys.argv[1])[1])" "$waitfile")
  until git fetch -q --depth 1 origin "$wb" 2>/dev/null && git cat-file -e "FETCH_HEAD:$wf" 2>/dev/null; do
    [ $(( $(date +%s) - t0 )) -ge $(( ${waitmin:-0} * 60 + 60 )) ] && { echo "waited; $wb:$wf never appeared"; exit 1; }
    echo "[$(date -u +%T)] waiting for $wf on $wb"; sleep 60
  done
  echo "found $wf on $wb"
fi
mkdir -p data_in
src=standin
if [ "$want" != standin ] && git ls-remote --exit-code origin refs/heads/pub/data-alachua >/dev/null 2>&1; then src=pub/data-alachua; fi
if [ "$want" = pub/data-alachua ] && [ "$src" != pub/data-alachua ]; then echo "pub/data-alachua was asked for and does not exist"; exit 1; fi
if [ "$src" = pub/data-alachua ]; then
  git fetch -q --depth 1 origin pub/data-alachua
  sha=$(git rev-parse FETCH_HEAD)
  git show FETCH_HEAD:regions/us-fl-alachua/species.json > data_in/species.json
  git show FETCH_HEAD:_made.txt > data_in/data_made.txt 2>/dev/null || true
  [ -n "$(git ls-tree --name-only FETCH_HEAD tools/species/fetch_photos.py)" ] && git show FETCH_HEAD:tools/species/fetch_photos.py > data_in/fetch_photos_species.py || true
  if [ -n "$manpath" ]; then man="$manpath"; git cat-file -e "FETCH_HEAD:$man" 2>/dev/null || { echo "$man is not on pub/data-alachua"; exit 1; }
  else man=$(git ls-tree -r --name-only FETCH_HEAD | grep -E '^eval/[^/]+/manifest\.csv$' | head -1); fi
  if [ -n "$man" ]; then
    git show "FETCH_HEAD:$man" > data_in/manifest.csv
    ename=$(basename "$(dirname "$man")")
    echo "source=pub/data-alachua@$sha manifest=$man"
  else
    echo "pub/data-alachua@$sha has no eval/*/manifest.csv yet; species from the branch, photos from the stand-in"
    python3 tools/lab/standin.py standin_out
    cp standin_out/eval/standin/manifest.csv data_in/manifest.csv
    ename=standin
    src="pub/data-alachua (species) + stand-in (manifest)"
  fi
else
  python3 tools/lab/standin.py standin_out
  cp standin_out/regions/us-fl-alachua/species.json data_in/species.json
  cp standin_out/eval/standin/manifest.csv data_in/manifest.csv
  ename=standin
  echo "source=stand-in (tools/lab/standin.py)"
fi
echo "$ename" > data_in/evalname.txt
{ echo "data_source=$src"; echo "data_made=$(tr '\n' ' ' < data_in/data_made.txt 2>/dev/null)"; echo "evalname=$ename"; echo "manifest_rows=$(($(wc -l < data_in/manifest.csv) - 1))"; echo "species=$(python3 -c "import json;print(len(json.load(open('data_in/species.json'))['species']))")"; } | tee data_in/source.txt
