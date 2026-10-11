#!/usr/bin/env bash
# Wait until a commit's results appear on the `ci` branch, then print their INDEX lines.
# Usage: bash ci/wait.sh <commit sha> [how many result lines to expect, default 1] [seconds to wait, default 540]
# Exit 0 when the expected number of lines is there, 3 when the wait ran out (run it again to keep waiting).
set -uo pipefail
sha="$1"; want="${2:-1}"; limit="${3:-540}"; t0=$(date +%s)
short="${sha:0:12}"
while :; do
  n=0
  if git fetch -q origin ci 2>/dev/null; then
    n=$(git show FETCH_HEAD:INDEX.txt 2>/dev/null | grep -c " $short" || true)
  fi
  if [ "${n:-0}" -ge "$want" ]; then git show FETCH_HEAD:INDEX.txt | grep " $short"; exit 0; fi
  if [ $(( $(date +%s) - t0 )) -ge "$limit" ]; then
    echo "still waiting: ${n:-0} of $want result lines for $short"
    git show FETCH_HEAD:INDEX.txt 2>/dev/null | grep " $short" || true
    exit 3
  fi
  sleep 15
done
