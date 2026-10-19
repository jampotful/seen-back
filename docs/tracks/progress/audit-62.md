# Audit 62, 19 October 2026: harvest-47 (desk-screen unit)

Unit: branch research/harvest-47 at commit d8a8f320, 51 search records (docs/views/searched/harvest-47.jsonl) and 20 wanted lines (docs/views/wanted/harvest-47.jsonl). The copies at /tmp/au62/harvest-47.jsonl and /tmp/au62/harvest-47-wanted.jsonl are byte-identical to `git show d8a8f320:<path>` (checked with cmp), and d8a8f320 is the head of the remote branch. The audit worktree /tmp/wsau62 was cut from origin/main (09e7eab1).

## Gate (step 1)

`python3 -I tools/views/screen_candidates.py --check /tmp/au62/harvest-47.jsonl --wanted /tmp/au62/harvest-47-wanted.jsonl` printed "0 problems". The unit goes on to the sample.

## Sample (step 2)

I drew the sample from all 51 search record lines (1-based line numbers) with `random.seed(62)` and `random.sample(lines, 20)`, before reading any record. The file has no duplicate lines, and the same call on the numbers 1 to 51 gives the same positions.

The draw order is 37, 12, 5, 16, 30, 20, 43, 23, 11, 33, 50, 45, 1, 17, 40, 8, 2, 31, 34 and 35.

Sorted, the lines are 1, 2, 5, 8, 11, 12, 16, 17, 20, 23, 30, 31, 33, 34, 35, 37, 40, 43, 45 and 50.

The 31 lines left out are 3, 4, 6, 7, 9, 10, 13 to 15, 18, 19, 21, 22, 24 to 29, 32, 36, 38, 39, 41, 42, 44, 46 to 49 and 51. They are the pool of the 15-record extension (`random.seed(6201)`, `random.sample(<those 31 line numbers in ascending order>, 15)`), which runs only if the audit finds an error.
