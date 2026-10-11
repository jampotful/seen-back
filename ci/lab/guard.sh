#!/usr/bin/env bash
# Guard model branches against a slow older run's publish, and name the shipping file in pocket models' cards.
# Usage: bash ci/lab/guard.sh <older run number> <minutes to watch> <comma-separated models> <comma-separated pocket models>
# 1. Now: each pocket model's card.json gets "ship" (onnx/vision.int8-per-channel.onnx) and its sha256, and every
#    branch gets _files.json (which run wrote each file), then is republished.
# 2. Then, every 20 seconds, each branch is fetched. While its _made.txt names another run, the guard keeps a snapshot
#    of it. When it names the older run, that run has just published over it: the guard restores every file the older
#    run changed from the snapshot (keeping files the older run added), merges card.json with the snapshot's values
#    winning, and republishes.
set -uo pipefail
older="$1"; minutes="$2"; IFS=, read -r -a models <<< "$3"; IFS=, read -r -a pockets <<< "${4:-}"
mkdir -p ret snap
L=ret/log.txt
say() { echo "[$(date -u +%T)] $*" | tee -a "$L"; }
made_run() { git show "$1:_made.txt" 2>/dev/null | sed -n 's/^run_number=//p'; }
is_pocket() { local m; for m in "${pockets[@]}"; do [ "$m" = "$1" ] && return 0; done; return 1; }
publish() { bash ci/put_branch.sh "pub/lab-$1" "$2" "lab guard: $1 ($3)" >> "$L" 2>&1; }
declare -A done_
for m in "${models[@]}"; do
  git fetch -q --depth 1 origin "pub/lab-$m" || { say "no pub/lab-$m"; done_[$m]=1; continue; }
  rn=$(made_run FETCH_HEAD)
  if [ "$rn" = "$older" ]; then say "pub/lab-$m already published by run $older; nothing to snapshot, not repaired"; done_[$m]=1; continue; fi
  d="work_$m"; rm -rf "$d"; mkdir -p "$d"; git archive FETCH_HEAD | tar -x -C "$d"
  if is_pocket "$m" && [ -f "$d/onnx/vision.int8-per-channel.onnx" ]; then
    python3 -u tools/lab/lab.py ship --model "$m" --file onnx/vision.int8-per-channel.onnx --out "$d" >> "$L" 2>&1
  fi
  python3 -u tools/lab/lab.py provenance --out "$d" >> "$L" 2>&1
  if publish "$m" "$d" "ship and provenance"; then say "republished pub/lab-$m with _files.json$(is_pocket "$m" && echo ' and ship')"; fi
  cp "$d/card.json" "ret/$m.card.json" 2>/dev/null
done
t0=$(date +%s)
while :; do
  left=0
  for m in "${models[@]}"; do
    [ -n "${done_[$m]:-}" ] && continue
    left=$((left + 1))
    git fetch -q --depth 1 origin "pub/lab-$m" 2>/dev/null || continue
    sha=$(git rev-parse FETCH_HEAD); rn=$(made_run FETCH_HEAD)
    if [ "$rn" = "$older" ]; then
      say "pub/lab-$m was just published by run $older ($sha); repairing from snapshot $(cat "snap/$m.sha" 2>/dev/null)"
      rm -rf "cur_$m" "fix_$m"; mkdir -p "cur_$m"; git archive FETCH_HEAD | tar -x -C "cur_$m"
      if python3 -u tools/lab/lab.py repair --snapshot "snap/$m" --current "cur_$m" --out "fix_$m" --older-run "$older" --run "${GITHUB_RUN_NUMBER:-0}" --report "ret/$m.repair.json" >> "$L" 2>&1 \
         && publish "$m" "fix_$m" "repaired after run $older"; then
        say "repaired pub/lab-$m"; cp "fix_$m/card.json" "ret/$m.card.json" 2>/dev/null
      else say "REPAIR FAILED for pub/lab-$m"; fi
      done_[$m]=1
    elif [ "$(cat "snap/$m.sha" 2>/dev/null)" != "$sha" ]; then
      rm -rf "snap/$m"; mkdir -p "snap/$m"; git archive FETCH_HEAD | tar -x -C "snap/$m"; echo "$sha" > "snap/$m.sha"
      say "snapshot pub/lab-$m at $sha (run $rn)"
    fi
  done
  [ "$left" -eq 0 ] && { say "all branches handled"; break; }
  [ $(( $(date +%s) - t0 )) -ge $(( minutes * 60 )) ] && { say "stopped watching after $minutes minutes; $left branches never saw run $older publish"; break; }
  sleep 20
done
