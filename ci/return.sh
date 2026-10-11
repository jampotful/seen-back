#!/usr/bin/env bash
# Send a job's results back as files on the `ci` branch, where they can be read with plain git.
# Usage: bash ci/return.sh <name> <dir> [shard]
# The results land in runs/<name>/<run number>[-shard]/ with a _meta.txt beside them, and one line is
# added to INDEX.txt: time, path, job status, the first twelve characters of the commit, and the branch.
# Keep results small: text, tables, and a few compressed pictures. Anything over 25 MB is refused.
set -uo pipefail
name="$1"; dir="$2"; shard="${3:-}"
dest="runs/$name/${GITHUB_RUN_NUMBER:-0}${shard:+-$shard}"
sha="${GITHUB_SHA:-$(git rev-parse HEAD)}"
mkdir -p "$dir"
{
  echo "sha=$sha"
  echo "ref=${GITHUB_REF_NAME:-}"
  echo "workflow=${GITHUB_WORKFLOW:-}"
  echo "run_id=${GITHUB_RUN_ID:-}"
  echo "run_number=${GITHUB_RUN_NUMBER:-}"
  echo "attempt=${GITHUB_RUN_ATTEMPT:-}"
  echo "shard=$shard"
  echo "status=${JOB_STATUS:-unknown}"
  echo "finished=$(date -u +%FT%TZ)"
} > "$dir/_meta.txt"
size_kb=$(du -sk "$dir" | cut -f1)
if [ "$size_kb" -gt 25600 ]; then
  echo "results are ${size_kb} kB, over the 25 MB limit; returning only text files" >&2
  find "$dir" -type f ! \( -name '*.txt' -o -name '*.json' -o -name '*.md' -o -name '*.csv' -o -name '*.log' \) -delete
  echo "oversize=${size_kb}kB, binary files dropped" >> "$dir/_meta.txt"
fi
git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
tmp="$(mktemp -d)"
if git fetch -q origin ci 2>/dev/null; then
  git worktree add -q "$tmp" FETCH_HEAD
else
  git worktree add -q --detach "$tmp"
  ( cd "$tmp" && git checkout -q --orphan ci-new && git rm -rfq . 2>/dev/null; true )
fi
mkdir -p "$tmp/$dest"
cp -R "$dir"/. "$tmp/$dest/" 2>/dev/null || true
cd "$tmp"
echo "$(date -u +%FT%TZ) $dest ${JOB_STATUS:-unknown} ${sha:0:12} ${GITHUB_REF_NAME:-}" >> INDEX.txt
git add -A
git commit -qm "results: $dest (${JOB_STATUS:-unknown})"
for i in 1 2 3 4 5 6 7 8 9 10; do
  if git push -q origin HEAD:ci; then echo "returned $dest"; exit 0; fi
  sleep $((RANDOM % 6 + 2))
  git fetch -q origin ci && git rebase -q FETCH_HEAD || { git rebase --abort 2>/dev/null; true; }
done
echo "could not return $dest" >&2; exit 1
