#!/usr/bin/env bash
# The audit of the evidence logs: tools/lit/audit.py over the research branches, run by .github/workflows/lit-audit.yml.
# Results go to out/ (returned to the ci branch by the workflow) and, when the run finishes, to the branch pub/lit-audit.
set -uo pipefail
[ -f ci/lit/audit.env ] && . ci/lit/audit.env
label="${GITHUB_REF_NAME#run/lit-audit/}"
mkdir -p out ev pub

if [ "${AUDIT_PLAN_ONLY:-0}" != "1" ] && [ -z "${ANTHROPIC_API_KEY:-}" ]; then
  msg="ANTHROPIC_API_KEY is not set. Nothing was sent."
  echo "$msg" >&2; echo "$msg" > out/FAILED.txt; exit 2
fi
export AUDIT_MAX_USD="${AUDIT_MAX_USD:-3}" AUDIT_ADJ_MAX_USD="${AUDIT_ADJ_MAX_USD:-8}" AUDIT_WAIT_MIN="${AUDIT_WAIT_MIN:-150}"

mode="${AUDIT_MODE:-first}"      # first: the first pass (and the second, when AUDIT_ADJUDICATE=1); second: only the second pass
prompt="${AUDIT_PROMPT:-v2}"
pubbranch="${AUDIT_PUB_BRANCH:-pub/lit-audit}"
mkdir -p audit-out

# the literature collection: the whole of it for the second pass, only the index files for a first pass with work cards
get_lit() {
  git fetch -q --depth 1 origin pub/lit-t1 || { echo "cannot fetch pub/lit-t1" >&2; exit 2; }
  if [ "$1" = full ]; then
    git worktree add -q --detach lit FETCH_HEAD || { echo "cannot check out pub/lit-t1" >&2; exit 2; }
  else
    for f in $(git ls-tree -r --name-only FETCH_HEAD | grep '/index.jsonl$'); do
      mkdir -p "lit/$(dirname "$f")"; git show "FETCH_HEAD:$f" > "lit/$f"
    done
  fi
}

# files from an earlier run on the ci branch
from_ci() {   # from_ci <path on ci> <local file>
  git fetch -q --depth 1 origin '+refs/heads/ci:refs/remotes/origin/ci' && git show "origin/ci:$1" > "$2" 2>/dev/null && [ -s "$2" ] \
    || { echo "cannot read $1 from the ci branch" >&2; echo "cannot read $1 from ci" > out/FAILED.txt; exit 2; }
}

if [ "$mode" = second ]; then
  status=0
  from_ci "${AUDIT_FLAGGED_REF}/flagged.jsonl" audit-out/flagged.jsonl
  from_ci "${AUDIT_RETRY_REF}/adjudicated.jsonl" retry-from.jsonl
  echo "second pass only: flagged from ${AUDIT_FLAGGED_REF}, undecided rows from ${AUDIT_RETRY_REF}" | tee out/units.txt
  get_lit full
  ids=(); [ -n "${AUDIT_IDS_FILE:-}" ] && ids=(--ids "$AUDIT_IDS_FILE")
  python3 -I tools/lit/audit.py adjudicate --lit lit --out audit-out --flagged audit-out/flagged.jsonl --retry-from retry-from.jsonl "${ids[@]}" \
    --model "${AUDIT_ADJ_MODEL:-claude-sonnet-5-5}" 2>&1 | tee out/audit-second.log.txt
  status="${PIPESTATUS[0]}"
  cp audit-out/*.md out/ 2>/dev/null || true
  cp audit-out/adjudicated.jsonl out/ 2>/dev/null || true
  if [ "$status" -eq 0 ] && [ -f audit-out/adjudicated.jsonl ]; then
    cp audit-out/adjudicated.jsonl audit-out/SUMMARY-second.md pub/ 2>/dev/null || true
    bash ci/put_branch.sh "$pubbranch" pub "the second pass of the audit, $label"
  fi
  exit "$status"
fi

# the logs
units="${AUDIT_UNITS:-all}"
if [ "$units" = "all" ]; then
  units="$(git ls-remote --heads origin 'refs/heads/research/*' | sed 's#.*refs/heads/research/##' | paste -sd, -)"
fi
have=""
for u in $(echo "$units" | tr ',' ' '); do
  if git fetch -q --depth 1 origin "+refs/heads/research/$u:refs/remotes/origin/research/$u" 2>/dev/null \
     && git show "origin/research/$u:docs/views/evidence/$u.jsonl" > "ev/$u.jsonl" 2>/dev/null && [ -s "ev/$u.jsonl" ]; then
    have="$have,$u"
  else
    rm -f "ev/$u.jsonl"; echo "no evidence log on research/$u; skipped" | tee -a out/skipped.txt
  fi
done
have="${have#,}"
echo "units audited: $have" | tee out/units.txt
[ -z "$have" ] && { echo "no logs" >&2; echo "no logs" > out/FAILED.txt; exit 2; }

cmd=run; [ "${AUDIT_PLAN_ONLY:-0}" = "1" ] && cmd=plan
limit=(); [ "${AUDIT_LIMIT:-0}" != "0" ] && limit=(--limit "$AUDIT_LIMIT")
lit=(); [ "$prompt" = v2 ] && { get_lit index; lit=(--lit lit); }
python3 -I tools/lit/audit.py "$cmd" --ev ev --out audit-out --units "$have" --prompt "$prompt" "${lit[@]}" "${limit[@]}" 2>&1 | tee out/audit-first.log.txt
status="${PIPESTATUS[0]}"

if [ "$status" -eq 0 ] && [ "$cmd" = run ] && [ "${AUDIT_ADJUDICATE:-0}" = "1" ]; then
  rm -rf lit; git worktree prune; get_lit full
  python3 -I tools/lit/audit.py adjudicate --lit lit --out audit-out --units "$have" --model "${AUDIT_ADJ_MODEL:-claude-sonnet-5-5}" 2>&1 | tee out/audit-second.log.txt
  status="${PIPESTATUS[0]}"
fi

cp audit-out/*.md out/ 2>/dev/null || true
cp audit-out/*.jsonl out/ 2>/dev/null || true
if [ "$cmd" = run ] && [ "$status" -eq 0 ]; then
  cp audit-out/*.jsonl audit-out/*.md pub/ 2>/dev/null || true
  # raw batch results are not published
  bash ci/put_branch.sh "$pubbranch" pub "the audit of the evidence logs, $label"
fi
exit "$status"
