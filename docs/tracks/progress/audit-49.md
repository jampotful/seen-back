# Audit 49, 18 October 2026: harvest-34 (desk-screen unit)

The unit is branch research/harvest-34 at commit e5d06b5d: 44 search records (docs/views/searched/harvest-34.jsonl) and 22 wanted lines (docs/views/wanted/harvest-34.jsonl). I read both files with `git show e5d06b5d:<path>` and saved copies to /tmp/au49/ (byte-identical to the committed files, checked with `cmp`). The last commit of the unit (e5d06b5d) is the desk's own mechanical fix that put zero-hit harvest queries back into `queries`; this audit reads the unit as it stands after that fix. The audit worktree /tmp/wsau49 was cut from origin/main and fast-forwarded to c5d604d0 (desk-screen.md point 7, the same rule as the fix); it edits only this report.

## Gate

`python3 -I tools/views/screen_candidates.py --check /tmp/au49/harvest-34.jsonl --wanted /tmp/au49/harvest-34-wanted.jsonl` printed "0 problems". The unit goes on to the sample.

## Sample

All 44 search record lines (1-based line numbers), `random.seed(49)`, `random.sample(lines, 20)`. The draw used the line count only, and it is written here before any record was read. The method reproduces the draws of audits 43 and 46 for their line counts.

Draw order: 5, 23, 27, 8, 21, 36, 33, 4, 3, 18, 10, 30, 39, 40, 35, 17, 41, 20, 34, 19

Sorted: 3, 4, 5, 8, 10, 17, 18, 19, 20, 21, 23, 27, 30, 33, 34, 35, 36, 39, 40, 41

The 24 lines left out are 1, 2, 6, 7, 9, 11, 12, 13, 14, 15, 16, 22, 24, 25, 26, 28, 29, 31, 32, 37, 38, 42, 43 and 44. They are the pool for a seed-4901 extension of 15 records if the first 20 hold an error.
