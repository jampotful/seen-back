# Audit 60, 19 October 2026: harvest-44 (desk-screen unit)

Unit: branch research/harvest-44 at commit 2fd34d76, 62 search records (docs/views/searched/harvest-44.jsonl) and 11 wanted lines (docs/views/wanted/harvest-44.jsonl). The copies at /tmp/au60/harvest-44.jsonl and /tmp/au60/harvest-44-wanted.jsonl are byte-identical to `git show 2fd34d76:<path>` (checked with cmp), and 2fd34d76 is the head of the remote branch. The audit worktree /tmp/wsau60 was cut from origin/main (6edf1581).

## Gate (step 1)

`python3 -I tools/views/screen_candidates.py --check /tmp/au60/harvest-44.jsonl --wanted /tmp/au60/harvest-44-wanted.jsonl` printed "0 problems". The unit goes on to the sample.

## Sample (step 2)

I drew the sample from all 62 search record lines (1-based line numbers) with `random.seed(60)` and `random.sample(lines, 20)`, before reading any record. The file has no duplicate lines, and the same call on the numbers 1 to 62 gives the same positions.

The draw order is 20, 19, 37, 10, 17, 15, 52, 31, 30, 22, 3, 51, 6, 43, 12, 59, 25, 56, 16 and 41.

Sorted, the lines are 3, 6, 10, 12, 15, 16, 17, 19, 20, 22, 25, 30, 31, 37, 41, 43, 51, 52, 56 and 59.

The 42 lines left out are 1, 2, 4, 5, 7 to 9, 11, 13, 14, 18, 21, 23, 24, 26 to 29, 32 to 36, 38 to 40, 42, 44 to 50, 53 to 55, 57, 58 and 60 to 62. They are the pool of the 15-record extension that runs if the audit finds an error (`random.seed(6001)`, `random.sample(<those 42 line numbers in ascending order>, 15)`), which draws 35, 54, 21, 1, 50, 45, 60, 62, 53, 24, 44, 29, 23, 33 and 38 (sorted: 1, 21, 23, 24, 29, 33, 35, 38, 44, 45, 50, 53, 54, 60 and 62).
