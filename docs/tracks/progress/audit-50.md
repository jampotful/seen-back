# Audit 50, 18 October 2026: harvest-35 (desk-screen unit)

Unit: branch research/harvest-35 at commit 0bd180b8, 54 search records (docs/views/searched/harvest-35.jsonl) and 15 wanted lines (docs/views/wanted/harvest-35.jsonl). The files were read with `git show 0bd180b8:<path>` and saved to /tmp/au50/ (byte-identical to the committed files, checked with cmp). The audit worktree /tmp/wsau50 was cut from origin/main (75c4cb08) and edits only this report.

## Gate (step 1)

`python3 -I tools/views/screen_candidates.py --check /tmp/au50/harvest-35.jsonl --wanted /tmp/au50/harvest-35-wanted.jsonl` printed "0 problems". The unit goes on to the sample.

## Sample (step 2)

All 54 search record lines (1-based line numbers), `random.seed(50)`, `random.sample(lines, 20)`. The draw used the line count only, and it is written here before any record was read.

Draw order: 32, 18, 24, 41, 16, 45, 31, 22, 6, 35, 21, 15, 36, 46, 10, 23, 7, 39, 44, 43

Sorted: 6, 7, 10, 15, 16, 18, 21, 22, 23, 24, 31, 32, 35, 36, 39, 41, 43, 44, 45, 46

The 34 lines left out are 1, 2, 3, 4, 5, 8, 9, 11, 12, 13, 14, 17, 19, 20, 25, 26, 27, 28, 29, 30, 33, 34, 37, 38, 40, 42, 47, 48, 49, 50, 51, 52, 53 and 54. They are the pool for a seed-5001 extension of 15 records, which runs only if the first 20 hold an error.
