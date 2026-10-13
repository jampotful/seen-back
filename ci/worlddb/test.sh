#!/usr/bin/env bash
# The world test of the full database (tools/world/worldtest.py), and its place files (tools/world/prior.py), on a build
# machine. Called by .github/workflows/worlddb.yml for run/worlddb/test-*. Reads pub/naturalist-world (the rows),
# pub/world-place (tools/world/grid.py) and the world test photos' vectors on pub/lab-bioclip2-l14. With PUBLISH_GRID set
# (a grid size in degrees), that grid's place.bin and zones.json are added to pub/naturalist-world.
set -uo pipefail
mkdir -p out work/rows work/place work/vec
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
fetch() { git fetch -q --depth 1 origin "$1" && git rev-parse FETCH_HEAD && git archive FETCH_HEAD "${@:3}" | tar -x -C "$2"; }
GRIDS="${GRIDS:-1,2}"
step "machine" bash -c 'getconf _NPROCESSORS_ONLN; free -m | head -2'
step "install" python3 -m pip install --quiet numpy || exit 1
step "rows (pub/naturalist-world)" fetch pub/naturalist-world work/rows parts.json scale.f32 table.json rows.i8.part00 rows.i8.part01 rows.i8.part02 rows.i8.part03 || exit 1
step "place data (pub/world-place)" fetch pub/world-place work/place || exit 1
step "vectors (pub/lab-bioclip2-l14)" bash -c 'git fetch -q --depth 1 origin pub/lab-bioclip2-l14 && git rev-parse FETCH_HEAD && for f in images/world-species.f16.npy images/world-species.ids.json; do git show "FETCH_HEAD:$f" > "work/vec/$(basename "$f")" || exit 1; done; ls -la work/vec' || exit 1
step "checks of the encounter rule" python3 -I tools/world/test_place.py --tzdb work/place/tzdb || exit 1
N=$(python3 -c "import json; print(json.load(open('work/rows/parts.json'))['count'])")
ships=""
for g in ${GRIDS//,/ }; do
  step "place files at $g degrees" python3 -I tools/world/prior.py --place work/place --tzdb work/place/tzdb --rows "$N" --res "$g" --out "ship$g" || exit 1
  ships="${ships:+$ships,}ship$g"
  ls -la "ship$g" | tee -a "$LOG"
done
step "world test" python3 -I tools/world/worldtest.py --rows work/rows --vectors work/vec/world-species --place work/place --ship "$ships" --out out/test || exit 1
cp out/test/WORLDTEST.md out/test/worldtest.json out/
if [ -n "${PUBLISH_GRID:-}" ]; then
  mkdir -p pubplace && cp "ship$PUBLISH_GRID/place.bin" "ship$PUBLISH_GRID/zones.json" pubplace/
  python3 - "$PUBLISH_GRID" <<'PY' >> "$LOG"
import hashlib, json, os, sys
d = "pubplace"
man = {f: {"bytes": os.path.getsize(os.path.join(d, f)), "sha256": hashlib.sha256(open(os.path.join(d, f), "rb").read()).hexdigest()} for f in ("place.bin", "zones.json")}
man["res"] = float(sys.argv[1])
json.dump(man, open(os.path.join(d, "place.json"), "w"), indent=1)
print(json.dumps(man))
PY
  step "publish the place files" bash ci/data/merge_pub.sh pub/naturalist-world pubplace "place files at $PUBLISH_GRID degrees" place.bin zones.json place.json || exit 1
fi
exit 0
