# Audit 63, 19 October 2026: harvest-46 (desk-screen unit)

Unit: branch research/harvest-46 at commit d711cdfe, 61 search records (docs/views/searched/harvest-46.jsonl) and 7 wanted lines (docs/views/wanted/harvest-46.jsonl). The copies at /tmp/au63/harvest-46.jsonl and /tmp/au63/harvest-46-wanted.jsonl are byte-identical to `git show d711cdfe:<path>` (checked with cmp), and d711cdfe is the head of the remote branch. The audit worktree /tmp/wsau63 was cut from origin/main, and this report is the only file I change.

## Gate (step 1)

`python3 -I tools/views/screen_candidates.py --check /tmp/au63/harvest-46.jsonl --wanted /tmp/au63/harvest-46-wanted.jsonl` printed "0 problems". The unit goes on to the sample.

## Sample (step 2)

I drew the sample from all 61 search record lines (1-based line numbers) with `random.seed(63)` and `random.sample(lines, 20)`. The file has no duplicate lines, and the same call on the numbers 1 to 61 gives the same positions. This draw is committed before any record is read.

The draw order is 29, 61, 19, 17, 31, 43, 6, 25, 48, 55, 5, 56, 13, 59, 51, 41, 20, 40, 4 and 15.

Sorted, the lines are 4, 5, 6, 13, 15, 17, 19, 20, 25, 29, 31, 40, 41, 43, 48, 51, 55, 56, 59 and 61.

If the audit finds an error, the extension draws 15 more with `random.seed(6301)` and `random.sample(<the 41 remaining line numbers in ascending order>, 15)`.
