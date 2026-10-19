#!/usr/bin/env bash
# The pocket job of .github/workflows/nonlife.yml: tools/world/nonlife.py on the real photos, with ROOT laid out as
# ci/world/head.sh lays it out (pub/lab-tinyclip-39m-16, pub/data-alachua, pub/data-world).
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
fetch() { git fetch -q --depth 1 origin "$1" && git archive FETCH_HEAD "${@:3}" | tar -x -C "$2"; }
label="${GITHUB_REF_NAME#run/nonlife/}"
[ -f "ci/nonlife/runs/$label.env" ] && . "ci/nonlife/runs/$label.env"
read -r -a extra <<< "${NONLIFE_ARGS:-}"
step "vectors of today's encoder" fetch pub/lab-tinyclip-39m-16 root/lab/tinyclip-39m-16 images card.json _files.json || exit 1
step "files kept in parts" python3 -I ci/lab/bigfiles.py join root/lab || exit 1
step "county data" fetch pub/data-alachua root/data || exit 1
step "world photos" fetch pub/data-world root/world || exit 1
step "the real photos" bash -c 'wc -l work/real/manifest.csv; ls work/real | head'
step "the rule search on the tuning photos, then the test photos once" python3 -I tools/world/nonlife.py root --made work/real --out out/nonlife \
  --probe --asked-mark "${ASKED_MARK:-0.05}" --made-review tools/world/nonlife-real-review.csv "${extra[@]}" || exit 1
cp out/nonlife/report.json out/report.json
exit 0
