#!/usr/bin/env bash
# Rerun the whole evaluation on a build machine from the published branches, compare it with the files committed in
# this commit, and publish the exported heads. Called by .github/workflows/eval.yml.
set -uo pipefail
mkdir -p out work
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
ROOT=work/root
step "install" python3 -m pip install --quiet numpy scikit-learn || exit 1
mkdir -p out/committed && cp docs/eval/*.json out/committed/ 2>/dev/null; cp docs/EVAL.md out/committed/EVAL.md 2>/dev/null
step "fetch" python3 -I tools/eval/fetch.py "$ROOT" || exit 1
step "checks" python3 -I tools/eval/checks.py "$ROOT"
step "study 1" python3 -I tools/eval/study1.py "$ROOT" || exit 1
TRAINS="sentences val"
[ -f "$ROOT/lab/tinyclip-39m-16/images/alachua-pre2025.f16.npy" ] && TRAINS="$TRAINS alachua-pre2025"
for t in $TRAINS; do
  step "study 2: $t" env SKIP_FETCH=1 SKIP_STUDY1=1 bash tools/eval/run.sh "$ROOT" "$t"
done
step "report" python3 -I tools/eval/report.py
mkdir -p out/rerun && cp docs/eval/*.json out/rerun/ && cp docs/EVAL.md out/rerun/EVAL.md
step "compare with the committed files" python3 -I tools/eval/compare.py out/committed out/rerun
python3 -I tools/eval/compare.py out/committed out/rerun > out/compare.txt 2>&1
rm -rf out/committed
for t in $TRAINS; do
  [ "$t" = "val" ] && continue        # stand-in heads are for proving the machinery and are not published
  for d in "$ROOT/slots/$t"/*/; do
    [ -f "$d/manifest.json" ] || continue
    step "publish heads $t $(basename "$d")" bash ci/put_branch.sh "pub/heads-$t-$(basename "$d")" "$d" "heads: $t, $(basename "$d")"
  done
done
exit 0
