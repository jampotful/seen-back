#!/usr/bin/env bash
# Publish files INTO a pub/data-* branch without removing what other jobs put there.
#
# ci/put_branch.sh replaces a whole branch, so two jobs that each publish part of pub/data-alachua (the species list,
# the training manifest, the extra photo sets) would erase each other. This script instead:
#   1. fetches the branch's current commit and checks out its files,
#   2. deletes the paths named after the message (each job's own directories, so renamed files do not linger),
#   3. copies <dir> over the result (same path: replaced; every other file: kept),
#   4. commits the merged tree as a new commit with no parent (the branch keeps no history, as with put_branch.sh),
#   5. pushes with --force-with-lease pinned to the commit read in step 1, so if anyone published in between the push
#      is refused and the whole read-merge-push starts again (up to 8 times). Nobody's files are lost to a race.
# _made.txt keeps one line per publish (newest last): what was published, from which commit, when, by which run.
#
# Usage: bash ci/data/merge_pub.sh <branch> <dir> <message> [path-to-replace ...]
#   e.g. bash ci/data/merge_pub.sh pub/data-alachua stage "extra photo set coco-kinds" extra/coco-kinds
set -uo pipefail
branch="$1"; dir="$2"; msg="$3"; shift 3
case "$branch" in pub/*) ;; *) echo "refusing: $branch is not a pub/ branch" >&2; exit 2;; esac
[ -d "$dir" ] || { echo "no directory $dir" >&2; exit 2; }
src="$(cd "$dir" && pwd)"
sha="${GITHUB_SHA:-$(git rev-parse HEAD)}"
origin_url="$(git remote get-url origin)"
auth="$(git config --get-all http.https://github.com/.extraheader || true)"
for attempt in 1 2 3 4 5 6 7 8; do
  tmp="$(mktemp -d)"
  git -C "$tmp" init -q -b "$branch" .
  git -C "$tmp" config user.name "github-actions[bot]"
  git -C "$tmp" config user.email "41898282+github-actions[bot]@users.noreply.github.com"
  [ -n "$auth" ] && git -C "$tmp" config http.https://github.com/.extraheader "$auth"
  old=""
  if git -C "$tmp" ls-remote --exit-code "$origin_url" "refs/heads/$branch" >/dev/null 2>&1; then
    git -C "$tmp" fetch -q --depth 1 "$origin_url" "refs/heads/$branch" || { echo "fetch failed (attempt $attempt)"; sleep 5; continue; }
    old="$(git -C "$tmp" rev-parse FETCH_HEAD)"
    git -C "$tmp" read-tree FETCH_HEAD && git -C "$tmp" checkout-index -a -f
    echo "read $branch at ${old:0:12}: $(git -C "$tmp" ls-files | wc -l) files"
  else
    echo "$branch does not exist yet; creating it"
  fi
  for p in "$@"; do
    case "$p" in ""|/*|*..*) echo "refusing to remove path '$p'" >&2; exit 2;; esac
    rm -rf "${tmp:?}/$p"
  done
  cp -R "$src"/. "$tmp/"
  printf 'published=%s made_from=%s made_at=%s workflow=%s run_number=%s\n' "$(echo "$msg" | tr ' ' '_')" "$sha" \
    "$(date -u +%FT%TZ)" "${GITHUB_WORKFLOW:-}" "${GITHUB_RUN_NUMBER:-}" >> "$tmp/_made.txt"
  git -C "$tmp" add -A
  tree="$(git -C "$tmp" write-tree)"
  commit="$(git -C "$tmp" commit-tree "$tree" -m "$msg (from ${sha:0:12}; merged into ${old:0:12})")"
  if git -C "$tmp" push -q --force-with-lease="refs/heads/$branch:$old" "$origin_url" "$commit:refs/heads/$branch"; then
    echo "published into $branch: ${commit:0:12} (was ${old:-nothing}); files now:"
    git -C "$tmp" ls-tree -r --name-only "$commit" | sed 's/^/  /'
    rm -rf "$tmp"
    exit 0
  fi
  echo "push refused (the branch moved, or the network failed); reading it again (attempt $attempt)"
  rm -rf "$tmp"
  sleep $((RANDOM % 8 + 3))
done
echo "could not publish into $branch" >&2; exit 1
