#!/usr/bin/env bash
# The big job of .github/workflows/nonlife.yml: BioCLIP 2's vectors of the photos and the larger model's answers on the full
# database as the page downloads it (every file that models/naturalist/manifest.json names, checked by SHA-256).
set -uo pipefail
mkdir -p out work/slot
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
step "the full database's files" python3 -I - <<'PY' || exit 1
import hashlib, json, os, urllib.request
m = json.load(open("models/naturalist/manifest.json"))
fs = [(p["url"], p["sha256"]) for p in m["species"]["parts"]] + [(m["species"]["scale"]["url"], m["species"]["scale"]["sha256"]),
     (m["species"]["table"]["url"], m["species"]["table"]["sha256"]), (m["place"]["url"], m["place"]["sha256"]),
     (m["place"]["zones"]["url"], m["place"]["zones"]["sha256"])]
for u, h in fs:
    p = os.path.join("work/slot", os.path.basename(u))
    for k in range(4):
        try:
            urllib.request.urlretrieve(u, p)
            if hashlib.sha256(open(p, "rb").read()).hexdigest() == h:
                break
        except Exception as e:
            print("retry", u, e)
    ok = hashlib.sha256(open(p, "rb").read()).hexdigest() == h
    print(os.path.basename(u), os.path.getsize(p), "ok" if ok else "DIFFERS")
    assert ok
PY
step "BioCLIP 2's vectors" python3 -I tools/world/nonlife_real.py bigvec work/real || exit 1
step "the larger model's answers" python3 -I tools/world/nonlife_real.py big work/real --slot work/slot --review tools/world/nonlife-real-review.csv || exit 1
cp work/real/big.json work/real/big-photos.jsonl work/real/big.ids.json out/
cp work/real/big.f16.npy out/ 2>/dev/null || true
exit 0
