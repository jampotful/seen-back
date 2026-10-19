# Audit 64, 19 October 2026: harvest-48 (desk-screen unit)

Unit: branch research/harvest-48 at commit 99d0a08f, 56 search records (docs/views/searched/harvest-48.jsonl) and 17 wanted lines (docs/views/wanted/harvest-48.jsonl). The copies at /tmp/au64/harvest-48.jsonl and /tmp/au64/harvest-48-wanted.jsonl are byte-identical to `git show 99d0a08f:<path>` (checked with cmp), and `git ls-remote` shows 99d0a08f as the head of the remote branch. The audit worktree /tmp/wsau64 was cut from origin/main (c855b867).

## Gate (step 1)

`python3 -I tools/views/screen_candidates.py --check /tmp/au64/harvest-48.jsonl --wanted /tmp/au64/harvest-48-wanted.jsonl` printed "0 problems". The unit goes on to the sample.

## Sample (step 2)

I drew the sample from all 56 search record lines (1-based line numbers) with `random.seed(64)` and `random.sample(lines, 20)`, before reading any record. The file has no duplicate lines, and the same call on the numbers 1 to 56 gives the same positions.

The draw order is 31, 8, 41, 40, 26, 35, 44, 2, 14, 18, 46, 54, 13, 42, 10, 6, 27, 29, 50 and 49.

Sorted, the lines are 2, 6, 8, 10, 13, 14, 18, 26, 27, 29, 31, 35, 40, 41, 42, 44, 46, 49, 50 and 54.

The 36 lines left out are the pool of the extension, should an error call for it (`random.seed(6401)`, `random.sample(<those 36 line numbers in ascending order>, 15)`), which draws 15, 21, 28, 34, 16, 52, 25, 22, 56, 55, 30, 36, 48, 4 and 43 (sorted: 4, 15, 16, 21, 22, 25, 28, 30, 34, 36, 43, 48, 52, 55 and 56).

(Verdicts follow.)
