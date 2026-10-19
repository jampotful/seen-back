# Audit 52, 18 October 2026: harvest-37 (desk-screen unit)

Unit: branch research/harvest-37 at commit 9317f898: 51 search records (docs/views/searched/harvest-37.jsonl) and 17 wanted lines (docs/views/wanted/harvest-37.jsonl). I read both files with `git show 9317f898:<path>` after `git fetch origin research/harvest-37` and saved copies to /tmp/au52/ (byte-identical to the committed files, checked with `cmp`). The audit worktree /tmp/wsau52 was cut from origin/main and fast-forwarded to a9630210, the desk's commit that put 16 of the unit's wanted lines on main with registry authors; the audit reads the unit's own 17 lines at 9317f898 and uses main's list only to see what main already holds. The report is the only file this audit edits.

(Work in progress. This first commit holds the gate and the draw, written before any record was read.)

## Gate (step 1)

`python3 -I tools/views/screen_candidates.py --check /tmp/au52/harvest-37.jsonl --wanted /tmp/au52/harvest-37-wanted.jsonl` printed "0 problems". The unit goes on to the sample.

## Sample (step 2)

All 51 search record lines (1-based line numbers), `random.seed(52)`, `random.sample(lines, 20)`. The draw used the line count only. The same call (`random.sample(range(1, n + 1), 20)`) reproduces the draws printed in audits 43 and 50, which fixes the convention.

Draw order: 18, 4, 47, 33, 31, 24, 27, 3, 9, 11, 45, 12, 23, 29, 1, 44, 35, 25, 38, 37

Sorted: 1, 3, 4, 9, 11, 12, 18, 23, 24, 25, 27, 29, 31, 33, 35, 37, 38, 44, 45, 47

The 31 lines left out are 2, 5, 6, 7, 8, 10, 13, 14, 15, 16, 17, 19, 20, 21, 22, 26, 28, 30, 32, 34, 36, 39, 40, 41, 42, 43, 46, 48, 49, 50 and 51. They are the pool for a seed-5201 extension of 15 records if an error turns up.
