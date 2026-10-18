#!/usr/bin/env bash
# The photos job of .github/workflows/nonlife.yml: search, fetch, split, encode with the pocket encoder, publish.
set -uo pipefail
mkdir -p out work/real
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
step "install" python3 -m pip install --quiet requests numpy pillow onnxruntime || exit 1
step "search Wikimedia Commons" python3 -I tools/world/nonlife_real.py manifest work/real --per "${PER:-105}" || exit 1
cp work/real/manifest.csv work/real/summary.json out/
step "fetch the photos" python3 -I tools/species/fetch_photos.py work/real/manifest.csv work/real/photos --workers 6 || exit 1
cp work/real/photos/_failures.tsv out/ 2>/dev/null || true
step "the pocket encoder's vectors" python3 -I tools/world/nonlife_real.py pocket work/real || exit 1
cp work/real/pocket-missing.json out/ 2>/dev/null || true
step "sizes" bash -c 'ls work/real/photos | wc -l; du -sh work/real/photos'
cat > work/real/README.md <<MD
# Real photographs with nothing alive in them
Made by .github/workflows/nonlife.yml (tools/world/nonlife_real.py) from Wikimedia Commons. manifest.csv gives every photo's
family, set (tune or test, by a hash of the id, fixed before anything was measured), the query that found it, its Commons page
(source), the address of the 500-pixel copy fetched, its licence (CC0, CC BY or public domain), the licence's address and the
author as Commons gives it. photos/<id>.jpg are those copies. nonlife-made.f16.npy and nonlife-made.ids.json are the pocket
encoder's unit vectors (tools/world/nonlife.py --made reads them beside manifest.csv).
MD
step "publish pub/nonlife-real" bash ci/put_branch.sh pub/nonlife-real work/real "real photographs with nothing alive in them" || exit 1
exit 0
