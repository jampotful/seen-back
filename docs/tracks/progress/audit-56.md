# Audit 56, 19 October 2026: harvest-39 (desk-screen unit)

Unit: branch research/harvest-39 at commit e0a8b5dc, 67 search records (docs/views/searched/harvest-39.jsonl) and 7 wanted lines (docs/views/wanted/harvest-39.jsonl). I read both files with `git show e0a8b5dc:<path>`, and they are byte-identical (checked with cmp) to the copies saved at /tmp/au56/harvest-39.jsonl and /tmp/au56/harvest-39-wanted.jsonl. The audit worktree /tmp/wsau56 was cut from origin/main (37af6218) and edits only this report.

This first commit holds the gate and the sample, written before any record was read. The verdicts follow in later commits.

## Gate (step 1)

`python3 -I tools/views/screen_candidates.py --check /tmp/au56/harvest-39.jsonl --wanted /tmp/au56/harvest-39-wanted.jsonl` printed "0 problems". The unit goes on to the sample.

## Sample (step 2)

All 67 search record lines (1-based line numbers), `random.seed(56)`, `random.sample(lines, 20)`. The draw depends on the line count only (the same call on the numbers 1 to 67 gives the same positions).

Draw order: 2, 61, 39, 54, 46, 15, 7, 24, 40, 5, 22, 42, 17, 37, 14, 67, 49, 64, 53, 4

Sorted: 2, 4, 5, 7, 14, 15, 17, 22, 24, 37, 39, 40, 42, 46, 49, 53, 54, 61, 64, 67

The 47 lines left out are 1, 3, 6, 8 to 13, 16, 18 to 21, 23, 25 to 36, 38, 41, 43 to 45, 47, 48, 50 to 52, 55 to 60, 62, 63, 65 and 66. They are the pool of the 15-record extension (`random.seed(5601)`, `random.sample(<those 47 line numbers in ascending order>, 15)`), which runs only if the first 20 turn up an error.
