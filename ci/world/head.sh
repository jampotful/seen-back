#!/usr/bin/env bash
# Fit the group head on the world photos and score it (tools/world/head.py). Called by .github/workflows/worldhead.yml.
# Lays out ROOT as tools/eval/fetch.py does, from three branches only: pub/lab-tinyclip-39m-16 (images/),
# pub/data-alachua (ROOT/data) and pub/data-world (ROOT/world). The candidate slot goes to pub/heads-world-<label>;
# the report comes back on ci.
set -uo pipefail
mkdir -p out root/lab/tinyclip-39m-16 root/data root/world
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
step "machine" bash -c 'getconf _NPROCESSORS_ONLN; free -m | head -2; python3 -c "import sklearn, numpy; print(sklearn.__version__, numpy.__version__)"'
step "vectors" fetch pub/lab-tinyclip-39m-16 root/lab/tinyclip-39m-16 images card.json _files.json || exit 1
step "county data" fetch pub/data-alachua root/data || exit 1
step "world photos" fetch pub/data-world root/world || exit 1
step "what is there" bash -c 'ls -la root/lab/tinyclip-39m-16/images | grep -E "world|alachua|coco"; wc -l root/world/lab/*/manifest.csv'
step "fit, tune and test" python3 -I tools/world/head.py root --slot models/pocket --out out/head --with-alachua "${WITH_ALACHUA:-both}" --powers "${POWERS:-0,0.5,1}" --groups "${HEAD_GROUPS:-fold}" || exit 1
cp out/head/REPORT.md out/head/report.json out/
label="${GITHUB_REF_NAME#run/worldhead/}"
step "publish the candidate" bash ci/put_branch.sh "pub/heads-world-$label" out/head/slot "group head fitted on the world photos" || exit 1
exit 0
