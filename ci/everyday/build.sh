#!/usr/bin/env bash
# The full database extended with the species people photograph at home, measured (tools/species/everyday_build.py), on a
# build machine. Called by .github/workflows/everyday.yml for run/everyday/build-* and again-*. Reads the world slot from
# before these species (the commit kept by pin/naturalist-world-9ae0806), pub/world-place and the world test photos'
# vectors on pub/lab-bioclip2-l14, and the photos' vectors from the embed job or, with PHOTO_VECTORS, from an earlier
# build's results on ci. With PUBLISH=1 the changed files go to PUB_BRANCH (default pub/naturalist-everyday;
# ci/put_branch.sh).
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
step "the world slot before the species people keep (pin/naturalist-world-9ae0806)" fetch pin/naturalist-world-9ae0806 work/slot rows.i8.part00 rows.i8.part01 rows.i8.part02 rows.i8.part03 scale.f32 table.json place.bin zones.json || exit 1
step "check the slot" python3 -I - <<'PY' || exit 1
# git names a commit by its content, so the commit is the check of every file in it; the files the manifest still serves
# from that commit (the first parts of the rows and the zones) must also match the manifest byte for byte.
import hashlib, json, os, subprocess
WORLD = "9ae08068166814ef9522c15a225a1b5e1e1f2df3"
got = subprocess.check_output(["git", "rev-parse", "FETCH_HEAD"]).decode().strip()
print("commit", got, "ok" if got == WORLD else "DIFFERS")
assert got == WORLD
m = json.load(open("models/naturalist/manifest.json"))
fs = [(p["url"], p["bytes"], p["sha256"]) for p in m["species"]["parts"]] + [(m["place"]["zones"]["url"], m["place"]["zones"]["bytes"], m["place"]["zones"]["sha256"])]
for u, n, h in fs:
    if "/%s/" % WORLD not in u:
        continue
    p = os.path.join("work/slot", os.path.basename(u))
    same = os.path.getsize(p) == n and hashlib.sha256(open(p, "rb").read()).hexdigest() == h
    print(os.path.basename(u), os.path.getsize(p), "ok" if same else "DIFFERS")
    assert same
PY
step "place data (pub/world-place)" fetch pub/world-place work/place test.tsv met.tsv || exit 1
step "vectors (pub/lab-bioclip2-l14)" bash -c 'git fetch -q --depth 1 origin pub/lab-bioclip2-l14 && git rev-parse FETCH_HEAD && for f in images/world-species.f16.npy images/world-species.ids.json; do git show "FETCH_HEAD:$f" > "work/vec/$(basename "$f")" || exit 1; done; ls -la work/vec' || exit 1
cat vecs/*/log.txt >> "$LOG" 2>/dev/null
pvec=vecs
if [ -n "${PHOTO_VECTORS:-}" ]; then
  # the photos' BioCLIP 2 vectors of an earlier build of the same photos.csv, from the ci branch, checked by SHA-256
  pvec=work/pvec
  step "the photos' vectors ($PHOTO_VECTORS on ci)" bash -c 'mkdir -p work/pvec && for f in photos.f16.npy photos.ids.json; do curl -sSfL --retry 4 -o "work/pvec/$f" "https://raw.githubusercontent.com/jampotful/seen-back/ci/$PHOTO_VECTORS/$f" || exit 1; done; sha256sum work/pvec/*' || exit 1
  step "check the photos' vectors" bash -c 'echo "636e8d44769cbc781b4dbbf1a3ab4880e8122a73767828beaf141c0129601579  work/pvec/photos.f16.npy
50dc95578023e2930cac8f62764fbb4845885a0fc2ddb126c5361100e0853814  work/pvec/photos.ids.json" | sha256sum -c' || exit 1
fi
stage=()
if [ "${PUBLISH:-0}" = 1 ]; then stage=(--stage work/stage); fi
step "build and measure" python3 -I tools/species/everyday_build.py --species data/everyday/species.csv --photos data/everyday/photos.csv \
  --photos-dir work/photos --photo-vectors "$pvec" --slot work/slot --place work/place --vectors work/vec/world-species --out out "${stage[@]}" || exit 1
if [ "${PUBLISH:-0}" = 1 ]; then
  cp work/stage/parts.json out/stage-parts.json
  cat > work/stage/README.md <<MD
# The full database's changed files for the species people photograph at home
Made by .github/workflows/everyday.yml (tools/species/everyday_build.py) from the slot kept by pin/naturalist-world-9ae0806:
the last part of the rows with the new rows at its end, the scale, the table with its "home" list, and the place file with
the new rows (no records). parts.json gives every length and SHA-256. The other parts of the rows are unchanged.
MD
  step "publish" bash ci/put_branch.sh "${PUB_BRANCH:-pub/naturalist-everyday}" work/stage "the full database for the species people photograph at home" || exit 1
fi
