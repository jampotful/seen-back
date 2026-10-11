#!/usr/bin/env bash
# Send a job's results back as files on the `ci` branch, where they can be read with plain git.
# Usage: bash ci/return.sh <name> <dir> [shard]
set -uo pipefail
name="$1"; dir="$2"; shard="${3:-}"
dest="runs/$name/${GITHUB_RUN_NUMBER:-0}${shard:+-$shard}"
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
echo "$(date -u +%FT%TZ) $dest ${JOB_STATUS:-unknown}" >> INDEX.txt
git add -A
git commit -qm "results: $dest (${JOB_STATUS:-unknown})"
for i in 1 2 3 4 5 6 7 8; do
  if git push -q origin HEAD:ci; then echo "returned $dest"; exit 0; fi
  sleep $((RANDOM % 6 + 2))
  git fetch -q origin ci && git rebase -q FETCH_HEAD || { git rebase --abort 2>/dev/null; true; }
done
echo "could not return $dest" >&2; exit 1
