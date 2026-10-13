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
export LIT_MODEL="${LIT_MODEL:-claude-haiku-5-5}"
short() { echo "$1" | sed 's/^claude-//'; }

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

# LIT_KEEP=1 starts from the tables already on pub/lit-table, so that a full run can be sent in several pushes, each
# with its own spend ceiling, and the branch ends up holding all of them.
if [ "${LIT_KEEP:-0}" = "1" ] && git fetch -q --depth 1 origin pub/lit-table; then
  git worktree add -q --detach prior FETCH_HEAD
  cp prior/*.jsonl prior/SUMMARY-*.md lit-table/ 2>/dev/null || true
  echo "kept from pub/lit-table: $(ls lit-table/*.jsonl 2>/dev/null | xargs -n1 basename | paste -sd' ' -)"
fi

status=0
if [ "${LIT_SKIP_TABLE:-0}" = "1" ]; then
  echo "LIT_SKIP_TABLE=1: only the calibration runs" | tee out/extract.log.txt
else
  # topics named in LIT_STRONG_TOPICS are read by LIT_STRONG_MODEL, the rest by LIT_MODEL; both go to lit-table/
  strong=""; rest="$topics"
  if [ -n "${LIT_STRONG_MODEL:-}" ] && [ -n "${LIT_STRONG_TOPICS:-}" ]; then
    strong="$LIT_STRONG_TOPICS"
    rest="$(echo ",$topics," | tr ',' '\n' | grep -v '^$' | grep -vxF -f <(echo "$strong" | tr ',' '\n') | paste -sd, -)"
  fi
  if [ -n "$strong" ]; then
    python3 -I tools/lit/extract.py "$mode" --lit lit --topics "$strong" --out lit-table --model "$LIT_STRONG_MODEL" \
      --summary "SUMMARY-$label-$(short "$LIT_STRONG_MODEL").md" 2>&1 | tee out/extract-strong.log.txt
    status="${PIPESTATUS[0]}"
    cp lit-table/SUMMARY-*.md out/ 2>/dev/null || true
  fi
  if [ -n "$rest" ] && [ "$status" -eq 0 ]; then
    python3 -I tools/lit/extract.py "$mode" --lit lit --topics "$rest" --out lit-table --model "$LIT_MODEL" \
      --summary "SUMMARY-$label-$(short "$LIT_MODEL").md" 2>&1 | tee out/extract.log.txt
    status="${PIPESTATUS[0]}"
  fi
  cp lit-table/SUMMARY-*.md out/ 2>/dev/null || true
fi

# calibration against the agents' hand-made logs, once for each model named in LIT_CALIB_MODELS
if [ "${LIT_CALIBRATE:-0}" = "1" ]; then
  mkdir -p ev
  for u in birds cat-dog ground-invertebrates; do
    git fetch -q --depth 1 origin "research/$u" && git show FETCH_HEAD:"docs/views/evidence/$u.jsonl" > "ev/$u.jsonl" \
      || { echo "cannot read the evidence log of research/$u" >&2; echo "cannot read research/$u" >> out/FAILED.txt; exit 2; }
  done
  python3 -I tools/lit/calibrate.py build --lit lit --evidence ev/*.jsonl --out calib
  python3 -I tools/lit/calibrate.py offline --lit lit --evidence ev/*.jsonl --out out
  if [ "$mode" = run ] && [ "$status" -ne 2 ]; then
    for m in $(echo "${LIT_CALIB_MODELS:-$LIT_MODEL}" | tr ',' ' '); do
      d="$(short "$m")"; mkdir -p "out/calib-$d"
      python3 -I tools/lit/extract.py run --lit calib --topics calib --out "calib/table-$d" --model "$m" 2>&1 | tee "out/calib-$d/extract.log.txt"
      python3 -I tools/lit/calibrate.py compare --evidence ev/*.jsonl --table "calib/table-$d/calib.jsonl" --calib calib --out "out/calib-$d"
      cp "calib/table-$d/SUMMARY.md" "out/calib-$d/extract-summary.md" 2>/dev/null || true
    done
  fi
fi

# the table, to its own branch (only when the extraction finished)
if [ "$mode" = run ] && [ "$status" -eq 0 ] && [ "${LIT_SKIP_TABLE:-0}" != "1" ]; then
  find lit-table -path '*_work*' \( -name passages.jsonl -o -name results.jsonl \) -delete
  for w in lit-table/_work*; do cp -R "$w" "out/$(basename "$w")" 2>/dev/null || true; done
  { echo; echo "Files over 95 MB are dropped from the branch:"; find lit-table -type f -size +95M -print -delete; } | tee -a out/SUMMARY.md
  bash ci/put_branch.sh pub/lit-table lit-table "the literature table, $label"
elif [ "$mode" = run ] && [ "${LIT_SKIP_TABLE:-0}" != "1" ]; then
  for w in lit-table/_work*; do cp -R "$w" "out/$(basename "$w")" 2>/dev/null || true; done
  find out -path '*_work*' \( -name passages.jsonl -o -name results.jsonl \) -delete
fi
exit "$status"
