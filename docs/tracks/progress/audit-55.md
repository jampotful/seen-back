# Audit 55, 19 October 2026: harvest-40 (desk-screen unit)

Unit: branch research/harvest-40 at commit 8d6e396d, 48 search records (docs/views/searched/harvest-40.jsonl) and 24 wanted lines (docs/views/wanted/harvest-40.jsonl). I read both files with `git show 8d6e396d:<path>`; the copies at /tmp/au55/ are byte-identical to the committed files (checked with cmp). The audit worktree /tmp/wsau55 was cut from origin/main and edits only this report.

## Gate (step 1)

`python3 -I tools/views/screen_candidates.py --check /tmp/au55/harvest-40.jsonl --wanted /tmp/au55/harvest-40-wanted.jsonl` printed "0 problems". The unit goes on to the sample.

## Sample (step 2)

All 48 search record lines (1-based line numbers), `random.seed(55)`, `random.sample(lines, 20)`. The draw used the line count only, and it is written here before any record was read.

Draw order: 6, 13, 10, 20, 48, 12, 45, 44, 23, 31, 35, 25, 37, 33, 26, 21, 28, 18, 36, 38

Sorted: 6, 10, 12, 13, 18, 20, 21, 23, 25, 26, 28, 31, 33, 35, 36, 37, 38, 44, 45, 48

The 28 lines left out are 1, 2, 3, 4, 5, 7, 8, 9, 11, 14, 15, 16, 17, 19, 22, 24, 27, 29, 30, 32, 34, 39, 40, 41, 42, 43, 46 and 47. If the 20 turn up an error, desk-audit.md calls for 15 more: `random.seed(5501)` and `random.sample(<those 28 line numbers in ascending order>, 15)` give, in draw order, 15, 9, 22, 34, 17, 4, 40, 1, 5, 30, 16, 43, 42, 19, 39 (sorted: 1, 4, 5, 9, 15, 16, 17, 19, 22, 30, 34, 39, 40, 42, 43). This extension draw is also written here before any record was read, and it runs only if the first 20 hold an error.
