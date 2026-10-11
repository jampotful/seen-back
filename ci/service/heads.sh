#!/usr/bin/env bash
# Build the service's head for Alachua County from the laboratory's branch and the species list, and check it.
# Usage: bash ci/service/heads.sh <out dir>
# Leaves the laboratory's files under lab/ (label rows, card, the evaluation set's image vectors for the parity check)
# and the head under service/heads/us-fl-alachua/. iNaturalist's names are used when pub/data-alachua has them.
set -euo pipefail
out="${1:-out}"; mkdir -p "$out" lab
git fetch -q --depth 1 origin pub/lab-bioclip2-l14
for f in card.json text/species_sci.f16.npy text/species_sci.labels.json images/alachua-2025.f16.npy images/alachua-2025.ids.json; do
  mkdir -p "lab/$(dirname "$f")"; git show "FETCH_HEAD:$f" > "lab/$f"
done
inat=()
if git fetch -q --depth 1 origin pub/data-alachua && git cat-file -e FETCH_HEAD:regions/us-fl-alachua/inat.json 2>/dev/null; then
  git show FETCH_HEAD:regions/us-fl-alachua/inat.json > lab/inat.json; inat=(--inat lab/inat.json)
  echo "iNaturalist names: found on pub/data-alachua" | tee -a "$out/log.txt"
else
  echo "iNaturalist names: not on pub/data-alachua yet; English names from the species list" | tee -a "$out/log.txt"
fi
python3 ci/service/build_heads.py --rows lab/text/species_sci.f16.npy --labels lab/text/species_sci.labels.json \
  --species data/regions/us-fl-alachua/species.json --card lab/card.json "${inat[@]}" --out service/heads/us-fl-alachua | tee -a "$out/log.txt"
python3 ci/service/check_head.py --head service/heads/us-fl-alachua --images lab/images/alachua-2025.f16.npy \
  --ids lab/images/alachua-2025.ids.json --manifest data/eval/alachua-2025/manifest.csv | tee -a "$out/log.txt"
cp service/heads/us-fl-alachua/manifest.json "$out/heads-manifest.json"
