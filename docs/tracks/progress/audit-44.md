# Audit 44, 18 October 2026: harvest-29 (desk-screen unit)

Unit: branch research/harvest-29, commit a7bc1581 (71 search records in docs/views/searched/harvest-29.jsonl, 56 wanted lines in docs/views/wanted/harvest-29.jsonl). The files were read with `git show a7bc1581:<path>` and saved to /tmp/au44/. The audit worktree /tmp/wsau44 was cut from origin/main and edits only this report.

## Gate

`python3 -I tools/views/screen_candidates.py --check <searched> --wanted <wanted>` on the unit's two files printed "0 problems". The unit goes on to the sample.

## Sample

`random.seed(44)`, then `random.sample(lines, 20)` over the 71 search record lines (1-based line numbers, in draw order):

53, 67, 15, 23, 49, 29, 38, 4, 69, 8, 37, 1, 7, 11, 50, 33, 45, 20, 55, 41

Sorted: 1, 4, 7, 8, 11, 15, 20, 23, 29, 33, 37, 38, 41, 45, 49, 50, 53, 55, 67, 69.

Verdicts follow in the next commit.
