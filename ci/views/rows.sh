#!/usr/bin/env bash
# The rows pipeline: tools/views/rows.py over the views named in ci/views/rows.env, run by .github/workflows/views-rows.yml.
# Results go to out/ (returned to the ci branch by the workflow) and the drafts to the branch pub/rows-draft.
set -uo pipefail
[ -f ci/views/rows.env ] && . ci/views/rows.env
mkdir -p out

if [ "${ROWS_PLAN_ONLY:-0}" != "1" ] && [ -z "${ANTHROPIC_API_KEY:-}" ]; then
  msg="ANTHROPIC_API_KEY is not set. Add it under Settings, Secrets and variables, Actions, as a repository secret with that name, then push again. Nothing was sent."
  echo "$msg" >&2; echo "$msg" > out/FAILED.txt; exit 2
fi
if [ -z "${ROWS_VIEWS:-}" ]; then
  echo "ROWS_VIEWS is empty in ci/views/rows.env" | tee out/FAILED.txt >&2; exit 2
fi
export ROWS_MAX_USD="${ROWS_MAX_USD:-6}" ROWS_WAIT_MIN="${ROWS_WAIT_MIN:-200}" ROWS_MODEL="${ROWS_MODEL:-claude-sonnet-5-5}"

python3 -I tools/views/rows.py plan --views "$ROWS_VIEWS" --out out 2>&1 | tee out/plan.txt
status=0
if [ "${ROWS_PLAN_ONLY:-0}" != "1" ]; then
  direct=""; [ "${ROWS_DIRECT:-0}" = "1" ] && direct="--direct"
  python3 -I tools/views/rows.py run --views "$ROWS_VIEWS" --out out $direct 2>&1 | tee out/run.log.txt
  status="${PIPESTATUS[0]}"
  rm -rf out/_work/*.jsonl.tmp
  mkdir -p rows-draft
  cp out/*.rows_draft.json out/stats.json rows-draft/ 2>/dev/null || true
  bash ci/put_branch.sh pub/rows-draft rows-draft "row drafts, ${GITHUB_REF_NAME:-local}"
fi
exit "$status"
