#!/usr/bin/env bash
# The full database extended with the species people photograph at home, measured (tools/species/everyday_build.py), on a
# build machine. Called by .github/workflows/everyday.yml for run/everyday/build-*. Reads the shipped world slot from the
# commit models/naturalist/manifest.json names (kept by pin/naturalist-world-9ae0806), pub/world-place and the world test
# photos' vectors on pub/lab-bioclip2-l14, and downloads the photos of data/everyday/photos.csv (tools/lab/fetch_photos.py).
# With PUBLISH=1 the changed files go to pub/naturalist-everyday (ci/put_branch.sh).
set -uo pipefail
mkdir -p out work/slot work/place work/vec work/photos
LOG=out/log.txt
step() {
  local name="$1"; shift
  echo "=== $(date -u +%FT%TZ) $name" | tee -a "$LOG"
  "$@" 2>&1 | tee -a "$LOG"
  local rc=${PIPESTATUS[0]}
  echo "=== $(date -u +%FT%TZ) $name: exit $rc" | tee -a "$LOG"
  return "$rc"
}
fetch() { git fetch -q --depth 1 origin "$1" && git rev-parse FETCH_HEAD && git archive FETCH_HEAD "${@:3}" | tar -x -C "$2"; }
step "machine" bash -c 'getconf _NPROCESSORS_ONLN; free -m | head -2; df -h . | tail -1'
step "the shipped slot (pin/naturalist-world-9ae0806)" fetch pin/naturalist-world-9ae0806 work/slot rows.i8.part00 rows.i8.part01 rows.i8.part02 rows.i8.part03 scale.f32 table.json place.bin zones.json || exit 1
step "check the slot against the manifest" python3 -I - <<'PY' || exit 1
import hashlib, json, os
m = json.load(open("models/naturalist/manifest.json"))
fs = [(p["url"], p["bytes"], p["sha256"]) for p in m["species"]["parts"]]
fs += [(m["species"]["scale"]["url"], m["species"]["scale"]["bytes"], m["species"]["scale"]["sha256"]),
       (m["species"]["table"]["url"], m["species"]["table"]["bytes"], m["species"]["table"]["sha256"]),
       (m["place"]["url"], m["place"]["bytes"], m["place"]["sha256"]), (m["place"]["zones"]["url"], m["place"]["zones"]["bytes"], m["place"]["zones"]["sha256"])]
for u, n, h in fs:
    p = os.path.join("work/slot", os.path.basename(u))
    got = hashlib.sha256(open(p, "rb").read()).hexdigest()
    print(os.path.basename(u), os.path.getsize(p), "ok" if (os.path.getsize(p) == n and got == h) else "DIFFERS")
    assert os.path.getsize(p) == n and got == h
PY
step "place data (pub/world-place)" fetch pub/world-place work/place test.tsv met.tsv || exit 1
step "vectors (pub/lab-bioclip2-l14)" bash -c 'git fetch -q --depth 1 origin pub/lab-bioclip2-l14 && git rev-parse FETCH_HEAD && for f in images/world-species.f16.npy images/world-species.ids.json; do git show "FETCH_HEAD:$f" > "work/vec/$(basename "$f")" || exit 1; done; ls -la work/vec' || exit 1
step "photos" python3 -I tools/lab/fetch_photos.py data/everyday/photos.csv work/photos --threads 16 || exit 1
stage=()
if [ "${PUBLISH:-0}" = 1 ]; then stage=(--stage work/stage); fi
step "build and measure" python3 -I tools/species/everyday_build.py --species data/everyday/species.csv --photos data/everyday/photos.csv \
  --photos-dir work/photos --slot work/slot --place work/place --vectors work/vec/world-species --out out "${stage[@]}" || exit 1
if [ "${PUBLISH:-0}" = 1 ]; then
  cp work/stage/parts.json out/stage-parts.json
  cat > work/stage/README.md <<MD
# The full database's changed files for the species people photograph at home
Made by .github/workflows/everyday.yml (tools/species/everyday_build.py) from the slot kept by pin/naturalist-world-9ae0806:
the last part of the rows with the new rows at its end, the scale, the table with its "home" list, and the place file with
the new rows (no records). parts.json gives every length and SHA-256. The other parts of the rows are unchanged.
MD
  step "publish" bash ci/put_branch.sh pub/naturalist-everyday work/stage "the full database for the species people photograph at home" || exit 1
fi
