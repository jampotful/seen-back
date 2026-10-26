#!/usr/bin/env bash
# Send a job's results back as files on the `ci` branch, where they can be read with plain git.
# Usage: bash ci/return.sh <name> <dir> [shard]
# The results land in runs/<name>/<run number>[-shard]/ with a _meta.txt beside them, and one line is
# added to INDEX.txt: time, path, job status, the first twelve characters of the commit, and the branch.
# Keep results small: text, tables, and a few compressed pictures. Anything over 25 MB is refused.
#
# Many jobs return at once, and every one of them adds a line to the end of INDEX.txt, so a rebase would
# conflict there every time. Each try therefore starts again from the branch as it stands now, copies the
# results in, adds the line, and pushes; a push that loses the race is simply tried again.
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
  find "$dir" -type f ! \( -name '*.txt' -o -name '*.json' -o -name '*.md' -o -name '*.csv' -o -name '*.log' -o -name '*.jsonl' -o -name '*.jsonl.gz' \) -delete
  echo "oversize=${size_kb}kB, binary files dropped" >> "$dir/_meta.txt"
fi
src="$(cd "$dir" && pwd)"
origin_url="$(git remote get-url origin)"
auth="$(git config --get-all http.https://github.com/.extraheader || true)"
line="$(date -u +%FT%TZ) $dest ${JOB_STATUS:-unknown} ${sha:0:12} ${GITHUB_REF_NAME:-}"
for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15; do
  tmp="$(mktemp -d)"
  (
    cd "$tmp" || exit 9
    git init -q .
    git config user.name "github-actions[bot]"
    git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
    [ -n "$auth" ] && git config http.https://github.com/.extraheader "$auth"
    if git fetch -q --depth 1 "$origin_url" ci 2>/dev/null; then
      git checkout -q -b ci FETCH_HEAD
    else
      git checkout -q --orphan ci
    fi
    mkdir -p "$dest"
    cp -R "$src"/. "$dest/" || exit 8   # a failed copy must not be committed as a returned result
    echo "$line" >> INDEX.txt
    git add -A
    git commit -qm "results: $dest (${JOB_STATUS:-unknown})"
    git push -q "$origin_url" HEAD:ci
  ) && { echo "returned $dest"; rm -rf "$tmp"; exit 0; }
  rm -rf "$tmp"
  sleep $((RANDOM % 8 + 2))
done
echo "could not return $dest" >&2; exit 1
