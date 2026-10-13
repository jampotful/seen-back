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
export AUDIT_MAX_USD="${AUDIT_MAX_USD:-3}" AUDIT_ADJ_MAX_USD="${AUDIT_ADJ_MAX_USD:-8}" AUDIT_WAIT_MIN="${AUDIT_WAIT_MIN:-100}"

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

mkdir -p audit-out
cmd=run; [ "${AUDIT_PLAN_ONLY:-0}" = "1" ] && cmd=plan
limit=(); [ "${AUDIT_LIMIT:-0}" != "0" ] && limit=(--limit "$AUDIT_LIMIT")
python3 -I tools/lit/audit.py "$cmd" --ev ev --out audit-out --units "$have" "${limit[@]}" 2>&1 | tee out/audit-first.log.txt
status="${PIPESTATUS[0]}"

if [ "$status" -eq 0 ] && [ "$cmd" = run ] && [ "${AUDIT_ADJUDICATE:-0}" = "1" ]; then
  git fetch -q --depth 1 origin pub/lit-t1 && git worktree add -q --detach lit FETCH_HEAD || { echo "cannot fetch pub/lit-t1" >&2; exit 2; }
  python3 -I tools/lit/audit.py adjudicate --lit lit --out audit-out --units "$have" --model "${AUDIT_ADJ_MODEL:-claude-sonnet-5-5}" 2>&1 | tee out/audit-second.log.txt
  status="${PIPESTATUS[0]}"
fi

cp audit-out/*.md out/ 2>/dev/null || true
cp audit-out/*.jsonl out/ 2>/dev/null || true
if [ "$cmd" = run ] && [ "$status" -eq 0 ]; then
  cp audit-out/*.jsonl audit-out/*.md pub/ 2>/dev/null || true
  # raw batch results are not published
  bash ci/put_branch.sh pub/lit-audit pub "the audit of the evidence logs, $label"
fi
exit "$status"
