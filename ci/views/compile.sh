#!/usr/bin/env bash
# The spec compiler: tools/views/compile.py over the jobs named in ci/views/compile.env, run by .github/workflows/views-compile.yml.
# Results go to out/ (returned to the ci branch by the workflow) and the drafts to the branch pub/views-draft.
set -uo pipefail
[ -f ci/views/compile.env ] && . ci/views/compile.env
label="${GITHUB_REF_NAME#run/views-compile/}"
mkdir -p out plan views-draft

if [ "${COMPILE_PLAN_ONLY:-0}" != "1" ] && [ -z "${ANTHROPIC_API_KEY:-}" ]; then
  msg="ANTHROPIC_API_KEY is not set. Add it under Settings, Secrets and variables, Actions, as a repository secret with that name, then push again. Nothing was sent."
  echo "$msg" >&2; echo "$msg" > out/FAILED.txt; exit 2
fi
if [ -z "${COMPILE_JOBS:-}" ]; then
  echo "COMPILE_JOBS is empty in ci/views/compile.env" | tee out/FAILED.txt >&2; exit 2
fi
export COMPILE_MAX_USD="${COMPILE_MAX_USD:-3}" COMPILE_WAIT_MIN="${COMPILE_WAIT_MIN:-200}" COMPILE_MODELS="${COMPILE_MODELS:-claude-haiku-5-5}" COMPILE_ATTEMPTS="${COMPILE_ATTEMPTS:-2}"

git fetch -q --depth 1 origin pub/lit-table || { echo "cannot fetch pub/lit-table" | tee out/FAILED.txt >&2; exit 2; }
git worktree add -q --detach lit-table FETCH_HEAD
# the audit's verdicts: docs/views/audit/ on this checkout when main holds them, else the branch agent/audit
if [ ! -d docs/views/audit ] || [ -z "$(ls docs/views/audit 2>/dev/null)" ]; then
  git fetch -q --depth 1 origin agent/audit && git worktree add -q --detach audit-src FETCH_HEAD && mkdir -p docs/views && cp -R audit-src/docs/views/audit docs/views/audit
fi
jobs=""
for j in $(echo "$COMPILE_JOBS" | tr ',' ' '); do jobs="$jobs${jobs:+,}tools/views/compile/$j.json"; done

python3 -I tools/views/compile.py plan --jobs "$jobs" --table lit-table --out plan --models "$COMPILE_MODELS" 2>&1 | tee out/plan.txt
status=0
if [ "${COMPILE_PLAN_ONLY:-0}" != "1" ]; then
  direct=""; [ "${COMPILE_DIRECT:-0}" = "1" ] && direct="--direct"
  python3 -I tools/views/compile.py run --jobs "$jobs" --table lit-table --out out --models "$COMPILE_MODELS" $direct 2>&1 | tee out/run.log.txt
  status="${PIPESTATUS[0]}"
  python3 -I tools/views/compile.py compare --out out 2>&1 | tail -3
fi

if [ "${COMPILE_PLAN_ONLY:-0}" != "1" ]; then
  if [ "${COMPILE_KEEP:-0}" = "1" ] && git fetch -q --depth 1 origin pub/views-draft; then
    git worktree add -q --detach prior FETCH_HEAD
    cp -R prior/. views-draft/ 2>/dev/null; rm -f views-draft/_made.txt
  fi
  mkdir -p "views-draft/$label"
  cp out/*.json out/*.md views-draft/"$label"/ 2>/dev/null || true
  rm -f views-draft/"$label"/*.reply.json
  cp -R tools/views/compile views-draft/jobs 2>/dev/null || true
  bash ci/put_branch.sh pub/views-draft views-draft "view drafts, $label"
fi
exit "$status"
