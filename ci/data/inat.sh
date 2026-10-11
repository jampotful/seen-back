#!/usr/bin/env bash
# Write regions/us-fl-alachua/inat.json (tools/species/build_inat.py), check it, publish it into pub/data-alachua beside
# the species list, and return it with the log. Run by the traindatas3 workflow when ci/data/job.txt says "inat".
set -uo pipefail
mkdir -p out work stage/regions/us-fl-alachua
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
step "inat.json" python3 tools/species/build_inat.py --out stage/regions/us-fl-alachua/inat.json --cache work \
  --report out/inat-REPORT.md || exit 1
cp stage/regions/us-fl-alachua/inat.json out/inat.json
step "check" python3 - <<'PY' || exit 1
import json
d = json.load(open("stage/regions/us-fl-alachua/inat.json", encoding="utf-8"))
sp = {str(s["key"]): s for s in json.load(open("data/regions/us-fl-alachua/species.json", encoding="utf-8"))["species"]}
bad = [k for k, v in d.items() if k not in sp or not isinstance(v.get("inat_id"), int) or not v.get("sci")]
print("entries %d of %d keys; malformed or unknown keys: %d; names differing from GBIF's: %d" % (
    len(d), len(sp), len(bad), sum(1 for k, v in d.items() if k in sp and v["sci"] != sp[k]["sci"])))
raise SystemExit(1 if bad or len(d) < 1000 else 0)
PY
step "publish" bash ci/data/merge_pub.sh pub/data-alachua stage "inat.json, iNaturalist's names for the species list" \
  regions/us-fl-alachua/inat.json || exit 1
