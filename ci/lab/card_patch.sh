#!/usr/bin/env bash
# Merge a patch into card.json on model branches and republish them (nothing else on the branch changes).
# Usage: bash ci/lab/card_patch.sh '<json: {"<model id>": {patch}, ...}>'
set -uo pipefail
mkdir -p ret
L=ret/log.txt
say() { echo "[$(date -u +%T)] $*" | tee -a "$L"; }
fail=0
for m in $(python3 -c "import json,sys;print(' '.join(json.loads(sys.argv[1])))" "$1"); do
  d="cp_$m"; mkdir -p "$d"
  git fetch -q --depth 1 origin "pub/lab-$m" || { say "no pub/lab-$m"; fail=1; continue; }
  git archive FETCH_HEAD | tar -x -C "$d"
  say "pub/lab-$m at $(git rev-parse --short FETCH_HEAD) (run $(git show FETCH_HEAD:_made.txt 2>/dev/null | sed -n 's/^run_number=//p'))"
  python3 - "$d" "$m" "$1" <<'PY' >> "$L" 2>&1 || { fail=1; continue; }
import json, sys
sys.path.insert(0, "tools/lab")
import lab
d, m, patch = sys.argv[1], sys.argv[2], json.loads(sys.argv[3])[sys.argv[2]]
for rel, info in (patch.get("broken") or {}).items():
    want = info.get("sha256")
    got = lab.sha256("%s/%s" % (d, rel))
    assert not want or got == want, "%s: sha256 %s, expected %s" % (rel, got, want)
lab.update_card(d, patch)
print("card patched:", m, json.dumps(patch)[:300])
PY
  python3 -u tools/lab/lab.py provenance --out "$d" >> "$L" 2>&1
  if bash ci/put_branch.sh "pub/lab-$m" "$d" "lab: $m card patched" >> "$L" 2>&1; then say "republished pub/lab-$m"; else say "PUBLISH FAILED pub/lab-$m"; fail=1; fi
  cp "$d/card.json" "ret/$m.card.json"
done
exit $fail
