# Audit 48, 18 October 2026: harvest-36 (desk-screen unit)

The unit is branch research/harvest-36 at commit 65a864fc: 81 search records for 14 genera (docs/views/searched/harvest-36.jsonl) and 9 wanted lines (docs/views/wanted/harvest-36.jsonl), which name 15 genera because the four Helicoverpa lines (6 to 9) belong to a genus with no search record. I read both files with `git show 65a864fc:<path>` and saved byte-identical copies to /tmp/au48/. The audit worktree /tmp/wsau48 was cut from origin/main (b9cad8cd) and edits only this report.

## Gate

`python3 -I tools/views/screen_candidates.py --check /tmp/au48/harvest-36.jsonl --wanted /tmp/au48/harvest-36-wanted.jsonl` printed "0 problems". The worktree holds main's stricter test (it fails a record while a harvest step of its genus errored). The unit goes on to the sample.

## Sample

All 81 search record lines (1-based line numbers), `random.seed(48)`, `random.sample(lines, 20)`. The draw used the line count only and was written here before any record was read.

Draw order: 71, 41, 17, 72, 69, 39, 65, 25, 56, 22, 20, 14, 64, 29, 28, 66, 81, 61, 70, 2

Sorted: 2, 14, 17, 20, 22, 25, 28, 29, 39, 41, 56, 61, 64, 65, 66, 69, 70, 71, 72, 81

(Report body follows as the checks finish.)
