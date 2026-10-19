# Audit 61, 19 October 2026: harvest-45 (desk-screen unit)

Unit: branch research/harvest-45 at commit ada967ae, 61 search records (docs/views/searched/harvest-45.jsonl) and 8 wanted lines (docs/views/wanted/harvest-45.jsonl). The copies at /tmp/au61/harvest-45.jsonl and /tmp/au61/harvest-45-wanted.jsonl are byte-identical to `git show ada967ae:<path>` (checked with cmp), and ada967ae is the head of the remote branch. The audit worktree /tmp/wsau61 was cut from origin/main (d5d5140e).

## Gate (step 1)

`python3 -I tools/views/screen_candidates.py --check /tmp/au61/harvest-45.jsonl --wanted /tmp/au61/harvest-45-wanted.jsonl` printed "0 problems". The unit goes on to the sample.

## Sample (step 2)

I drew the sample from all 61 search record lines (1-based line numbers) with `random.seed(61)` and `random.sample(lines, 20)` before reading any record. The file has no duplicate lines, and the same call on the numbers 1 to 61 gives the same positions.

The draw order is 32, 12, 36, 14, 52, 21, 19, 56, 57, 45, 2, 61, 23, 49, 5, 26, 30, 22, 11 and 44.

Sorted, the lines are 2, 5, 11, 12, 14, 19, 21, 22, 23, 26, 30, 32, 36, 44, 45, 49, 52, 56, 57 and 61.

The 41 lines left out are 1, 3, 4, 6 to 10, 13, 15 to 18, 20, 24, 25, 27 to 29, 31, 33 to 35, 37 to 43, 46 to 48, 50, 51, 53 to 55 and 58 to 60. They are the pool of the 15-record extension that runs only if the audit finds an error (`random.seed(6101)`, `random.sample(<those 41 line numbers in ascending order>, 15)`), which would draw 40, 6, 9, 31, 8, 18, 17, 54, 60, 42, 25, 50, 47, 15 and 48 (sorted: 6, 8, 9, 15, 17, 18, 25, 31, 40, 42, 47, 48, 50, 54 and 60).

Verdicts follow in a later commit.
