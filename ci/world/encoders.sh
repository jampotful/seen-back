#!/usr/bin/env bash
# Encoders compared on the world photos (tools/world/encoders.py). Called by .github/workflows/worldenc.yml.
# Fetches pub/data-world to ROOT/world and, for each model in MODELS, the world vectors and card of pub/lab-<model>.
set -uo pipefail
mkdir -p out root/world
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
fetch() {
  git fetch -q --depth 1 origin "$1" && git archive FETCH_HEAD "${@:3}" | tar -x -C "$2"
}
MODELS="${MODELS:-tinyclip-39m-16,bioclip-b16,bioclip25-mobile-fastvit}"
step "world photos" fetch pub/data-world root/world || exit 1
for m in ${MODELS//,/ }; do
  mkdir -p "root/lab/$m"
  step "vectors of $m" fetch "pub/lab-$m" "root/lab/$m" card.json images/world-fit.f16.npy images/world-fit.ids.json images/world-eval.f16.npy images/world-eval.ids.json
done
step "compare" python3 -I tools/world/encoders.py root --models "$MODELS" --out out/enc || exit 1
cp out/enc/ENCODERS.md out/enc/encoders.json out/
exit 0
