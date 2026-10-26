#!/usr/bin/env bash
# Publish a directory as the whole content of a branch, replacing whatever the branch held before.
# For files too large or too binary for the `ci` branch: model files, embeddings, data sets.
# The branch keeps no history, so replacing it does not grow the repository.
# Usage: bash ci/put_branch.sh <branch> <dir> [message]
set -uo pipefail
branch="$1"; dir="$2"; msg="${3:-publish $1}"
case "$branch" in main|ci|gh-pages) echo "refusing to replace $branch" >&2; exit 2;; esac
sha="${GITHUB_SHA:-$(git rev-parse HEAD)}"
origin_url="$(git remote get-url origin)"
auth="$(git config --get-all http.https://github.com/.extraheader || true)"
[ -d "$dir" ] && [ -n "$(ls -A "$dir" 2>/dev/null)" ] || { echo "nothing to publish: $dir is missing or empty" >&2; exit 2; }
tmp="$(mktemp -d)"
cp -R "$dir"/. "$tmp/" || { echo "could not copy $dir" >&2; rm -rf "$tmp"; exit 3; }
cd "$tmp"
git init -q -b "$branch" .
git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
[ -n "$auth" ] && git config http.https://github.com/.extraheader "$auth"
printf 'made_from=%s\nmade_at=%s\nworkflow=%s\nrun_number=%s\n' "$sha" "$(date -u +%FT%TZ)" "${GITHUB_WORKFLOW:-}" "${GITHUB_RUN_NUMBER:-}" > _made.txt
git add -A
git commit -qm "$msg (from ${sha:0:12})"
for i in 1 2 3 4 5; do
  if git push -q -f "$origin_url" "HEAD:refs/heads/$branch"; then echo "published $branch"; exit 0; fi
  sleep $((RANDOM % 6 + 2))
done
echo "could not publish $branch" >&2; exit 1
