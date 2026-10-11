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

# A branch named run/eval/armed* waits until the training vectors are published, then runs. armed-all also waits for BioCLIP 2's.
has_file() {   # has_file <branch> <path>: does the published branch hold the path? (trees only, no file is downloaded)
  git fetch -q --depth 1 --filter=blob:none origin "refs/heads/$1" 2>/dev/null || return 1
  git ls-tree -r --name-only FETCH_HEAD | grep -qx "$2"
}
# A branch named run/eval/coco* waits (up to ninety minutes) until both pocket models' vectors of the extra set
# (people, pets, livestock, rooms) are published, then reruns everything, so that the sentence slots it publishes
# are tuned with them.
WAIT_EXTRA=""
# A branch named run/eval/licence* reruns only the heads fitted under the licence rule (tools/eval/licences.py) for
# TinyCLIP 39M/16, the pocket v3 decision, the last check of the assembled files and the pets check, and compares them
# with the committed files. It publishes nothing: the slot's manifest and the checksums of its files come back in out/pocket-v3.
if [[ "${GITHUB_REF_NAME:-}" == run/eval/licence* ]]; then
  step "install" python3 -m pip install --quiet numpy scikit-learn || exit 1
  mkdir -p out/committed && cp docs/eval/*.json out/committed/ 2>/dev/null; cp docs/EVAL.md out/committed/EVAL.md 2>/dev/null
  step "fetch" python3 -I tools/eval/fetch.py "$ROOT" || exit 1
  # the sandbox's run had no BioCLIP 2 vectors of the training photos; leave any that appeared since out, so that the same heads are tried
  if ls "$ROOT"/lab/bioclip2-l14/images/alachua-pre2025* >/dev/null 2>&1; then
    echo "=== BioCLIP 2's vectors of the training photos are published now; they are left out of this rerun to match the sandbox's run" | tee -a "$LOG"
    rm -f "$ROOT"/lab/bioclip2-l14/images/alachua-pre2025*
  fi
  step "checks" python3 -I tools/eval/checks.py "$ROOT"
  for rule in nc by; do
    step "study 2: alachua-pre2025, licence rule $rule" python3 -I tools/eval/study2.py "$ROOT" --train alachua-pre2025 --models tinyclip-39m-16 --licence "$rule" --save "$ROOT/heads/alachua-pre2025-$rule"
    step "export: $rule" python3 -I tools/eval/export_heads.py "$ROOT" --head "$ROOT/heads/alachua-pre2025-$rule/tinyclip-39m-16.npz" --out "$ROOT/slots/alachua-pre2025-$rule/tinyclip-39m-16"
  done
  step "scored: nc, name_at at 92 in 100" python3 -I tools/eval/shipped.py "$ROOT" "$ROOT/slots/alachua-pre2025-nc/tinyclip-39m-16" --name alachua-pre2025-nc-tinyclip-39m-16 --name-bar 0.92
  step "scored: nc, name_at at 90 in 100" python3 -I tools/eval/shipped.py "$ROOT" "$ROOT/slots/alachua-pre2025-nc/tinyclip-39m-16" --name alachua-pre2025-nc-tinyclip-39m-16-at90 --no-write
  step "scored: by" python3 -I tools/eval/shipped.py "$ROOT" "$ROOT/slots/alachua-pre2025-by/tinyclip-39m-16" --name alachua-pre2025-by-tinyclip-39m-16
  step "pocket v3 decision" python3 -I tools/eval/decide_v3.py --candidate alachua-pre2025-nc-tinyclip-39m-16
  step "pocket v3 files" python3 -I tools/eval/pocket_v3.py "$ROOT/slots/alachua-pre2025-nc/tinyclip-39m-16" --shipped docs/eval/shipped-alachua-pre2025-nc-tinyclip-39m-16.json --decision docs/eval/decision-pocket-v3.json --ready "$ROOT/pocket-v3" --publish "$ROOT/pub-pocket-v3"
  step "last check" python3 -I tools/eval/shipped.py "$ROOT" "$ROOT/pocket-v3" --name pocket-v3 --name-bar 0.92 --no-write
  step "pets and livestock" python3 -I tools/eval/pets.py "$ROOT" "$ROOT/pocket-v3" --name pocket-v3
  step "report" python3 -I tools/eval/report.py
  mkdir -p out/rerun && cp docs/eval/*.json docs/eval/*.md out/rerun/ && cp docs/EVAL.md out/rerun/EVAL.md
  step "compare with the committed files" python3 -I tools/eval/compare.py out/committed out/rerun
  python3 -I tools/eval/compare.py out/committed out/rerun > out/compare.txt 2>&1
  rm -rf out/committed
  mkdir -p out/pocket-v3 && cp "$ROOT/pocket-v3/manifest.json" out/pocket-v3/ && (cd "$ROOT/pocket-v3" && sha256sum -- * > "$GITHUB_WORKSPACE/out/pocket-v3/sha256.txt")
  cp "$ROOT/FETCHED.json" out/FETCHED.json 2>/dev/null
  exit 0
fi
case "${GITHUB_REF_NAME:-}" in
  run/eval/armed-all*) WAIT="pub/lab-tinyclip-39m-16 pub/lab-tinyclip-8m-16 pub/lab-bioclip2-l14" ;;
  run/eval/armed*) WAIT="pub/lab-tinyclip-39m-16 pub/lab-tinyclip-8m-16" ;;
  run/eval/coco*) WAIT=""; WAIT_EXTRA="pub/lab-tinyclip-39m-16 pub/lab-tinyclip-8m-16" ;;
  *) WAIT="" ;;
esac
if [ -n "$WAIT_EXTRA" ]; then
  echo "=== $(date -u +%FT%TZ) waiting for images/coco-kinds.f16.npy on: $WAIT_EXTRA" | tee -a "$LOG"
  deadline=$(( $(date +%s) + ${EXTRA_WAIT_SECONDS:-5400} ))
  while :; do
    missing=""
    for b in $WAIT_EXTRA; do has_file "$b" images/coco-kinds.f16.npy || missing="$missing $b"; done
    [ -z "$missing" ] && break
    if [ "$(date +%s)" -ge "$deadline" ]; then
      echo "=== $(date -u +%FT%TZ) going on without the extra set's vectors on:$missing" | tee -a "$LOG"
      echo "The extra set's vectors never arrived on:$missing" > out/extra-never-arrived.txt
      break
    fi
    sleep 60
  done
  echo "=== $(date -u +%FT%TZ) done waiting for the extra set" | tee -a "$LOG"
fi
if [ -n "$WAIT" ]; then
  echo "=== $(date -u +%FT%TZ) waiting for images/alachua-pre2025.f16.npy on: $WAIT" | tee -a "$LOG"
  deadline=$(( $(date +%s) + ${WAIT_SECONDS:-18000} ))
  while :; do
    missing=""
    for b in $WAIT; do has_file "$b" images/alachua-pre2025.f16.npy || missing="$missing $b"; done
    has_file pub/data-alachua train/alachua-pre2025/manifest.csv || missing="$missing pub/data-alachua(manifest)"
    [ -z "$missing" ] && break
    if [ "$(date +%s)" -ge "$deadline" ]; then
      echo "=== $(date -u +%FT%TZ) gave up waiting; still missing:$missing" | tee -a "$LOG"
      echo "The training vectors never arrived; missing:$missing" > out/never-arrived.txt
      exit 0
    fi
    sleep 60
  done
  echo "=== $(date -u +%FT%TZ) the training vectors are published" | tee -a "$LOG"
  # The kind decision is tuned with photos of people, pets, livestock and rooms (extra/coco-kinds). Give their vectors a
  # bounded time to appear, then go on with whatever is published: the studies say which they had.
  deadline=$(( $(date +%s) + ${EXTRA_WAIT_SECONDS:-2400} ))
  while :; do
    missing=""
    for b in $WAIT; do has_file "$b" images/coco-kinds.f16.npy || missing="$missing $b"; done
    [ -z "$missing" ] && break
    if [ "$(date +%s)" -ge "$deadline" ]; then
      echo "=== $(date -u +%FT%TZ) going on without the extra set's vectors on:$missing" | tee -a "$LOG"
      break
    fi
    sleep 60
  done
fi
step "install" python3 -m pip install --quiet numpy scikit-learn || exit 1
mkdir -p out/committed && cp docs/eval/*.json out/committed/ 2>/dev/null; cp docs/EVAL.md out/committed/EVAL.md 2>/dev/null
step "fetch" python3 -I tools/eval/fetch.py "$ROOT" || exit 1
step "checks" python3 -I tools/eval/checks.py "$ROOT"
if [ -n "$WAIT" ]; then
  # An armed run exists to deliver the trained heads as soon as it can: Study 1, the sentence slots and the stand-in
  # are rerun by the other runs and are taken here as committed.
  TRAINS="alachua-pre2025"
else
  step "study 1" python3 -I tools/eval/study1.py "$ROOT" || exit 1
  TRAINS="sentences val"
  [ -f "$ROOT/lab/tinyclip-39m-16/images/alachua-pre2025.f16.npy" ] && [ -f "$ROOT/data/train/alachua-pre2025/manifest.csv" ] && TRAINS="$TRAINS alachua-pre2025"
fi
for t in $TRAINS; do
  step "study 2: $t" env SKIP_FETCH=1 SKIP_STUDY1=1 bash tools/eval/run.sh "$ROOT" "$t"
done
step "report" python3 -I tools/eval/report.py
mkdir -p out/rerun && cp docs/eval/*.json docs/eval/*.md out/rerun/ && cp docs/EVAL.md out/rerun/EVAL.md
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
