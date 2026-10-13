#!/usr/bin/env bash
# The literature table: tools/lit/extract.py over the topics named in ci/lit/table.env, run by
# .github/workflows/lit-table.yml. Results go to out/ (returned to the ci branch by the workflow) and, when the
# extraction finishes, to the branch pub/lit-table.
set -uo pipefail
[ -f ci/lit/table.env ] && . ci/lit/table.env
label="${GITHUB_REF_NAME#run/lit-table/}"
mkdir -p out lit-table

if [ "${LIT_PLAN_ONLY:-0}" != "1" ] && [ -z "${ANTHROPIC_API_KEY:-}" ]; then
  msg="ANTHROPIC_API_KEY is not set. Add it under Settings, Secrets and variables, Actions, as a repository secret with that name, then push again. Nothing was sent."
  echo "$msg" >&2; echo "$msg" > out/FAILED.txt; exit 2
fi
if [ -z "${LIT_TABLE_TOPICS:-}" ]; then
  echo "LIT_TABLE_TOPICS is empty in ci/lit/table.env; name the topics or write all." >&2
  echo "LIT_TABLE_TOPICS is empty in ci/lit/table.env" > out/FAILED.txt; exit 2
fi
export LIT_MAX_USD="${LIT_MAX_USD:-25}" LIT_WAIT_MIN="${LIT_WAIT_MIN:-330}"

# the collection
if [ -n "${LIT_DIR:-}" ]; then      # a checkout you already have (for trials from your own machine)
  ln -s "$LIT_DIR" lit
else
  git fetch -q --depth 1 origin pub/lit-t1 || { echo "cannot fetch pub/lit-t1" >&2; exit 2; }
  git worktree add -q --detach lit FETCH_HEAD
fi
topics="$LIT_TABLE_TOPICS"
if [ "$topics" = "all" ]; then
  topics="$(ls -d lit/*/ | xargs -n1 basename | grep -v '^methods$' | paste -sd, -)"
  topics="$topics,methods"
fi
mode=run; [ "${LIT_PLAN_ONLY:-0}" = "1" ] && mode=plan

status=0
python3 -I tools/lit/extract.py "$mode" --lit lit --topics "$topics" --out lit-table 2>&1 | tee out/extract.log.txt
status="${PIPESTATUS[0]}"
cp lit-table/SUMMARY.md out/SUMMARY.md 2>/dev/null || true

# calibration against the agents' hand-made logs
if [ "${LIT_CALIBRATE:-0}" = "1" ]; then
  mkdir -p ev
  for u in birds cat-dog ground-invertebrates; do
    git fetch -q --depth 1 origin "research/$u" && git show FETCH_HEAD:"docs/views/evidence/$u.jsonl" > "ev/$u.jsonl" \
      || { echo "cannot read the evidence log of research/$u" >&2; echo "cannot read research/$u" >> out/FAILED.txt; exit 2; }
  done
  python3 -I tools/lit/calibrate.py build --lit lit --evidence ev/*.jsonl --out calib
  python3 -I tools/lit/calibrate.py offline --lit lit --evidence ev/*.jsonl --out out
  if [ "$mode" = run ] && [ "$status" -ne 2 ]; then
    python3 -I tools/lit/extract.py run --lit calib --topics calib --out calib/table 2>&1 | tee out/calibration-extract.log.txt
    python3 -I tools/lit/calibrate.py compare --evidence ev/*.jsonl --table calib/table/calib.jsonl --calib calib --out out
    cp calib/table/SUMMARY.md out/calibration-extract-summary.md 2>/dev/null || true
  fi
fi

# the table, to its own branch (only when the extraction finished)
if [ "$mode" = run ] && [ "$status" -eq 0 ]; then
  rm -f lit-table/_work/passages.jsonl lit-table/_work/results.jsonl
  cp -R lit-table/_work out/_work 2>/dev/null || true
  { echo; echo "Files over 95 MB are dropped from the branch:"; find lit-table -type f -size +95M -print -delete; } | tee -a out/SUMMARY.md
  bash ci/put_branch.sh pub/lit-table lit-table "the literature table, $label"
elif [ "$mode" = run ]; then
  cp -R lit-table/_work out/_work 2>/dev/null || true
  rm -f out/_work/passages.jsonl out/_work/results.jsonl
fi
exit "$status"
