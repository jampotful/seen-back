# Audit 59, 19 October 2026: harvest-42 (desk-screen unit)

Unit: branch research/harvest-42 at commit ec9a85a4, 72 search records (docs/views/searched/harvest-42.jsonl) and 6 wanted lines (docs/views/wanted/harvest-42.jsonl). The copies at /tmp/au59/harvest-42.jsonl and /tmp/au59/harvest-42-wanted.jsonl are byte-identical to `git show ec9a85a4:<path>` (checked with cmp). The audit worktree /tmp/wsau59 was cut from origin/main (3a2073ce) and edits only this report. The report is in progress; this first commit holds the gate and the sample, drawn before any record was read.

## Gate (step 1)

`python3 -I tools/views/screen_candidates.py --check /tmp/au59/harvest-42.jsonl --wanted /tmp/au59/harvest-42-wanted.jsonl` printed "0 problems". The unit goes on to the sample.

## Sample (step 2)

I drew the sample from all 72 search record lines (1-based line numbers) with `random.seed(59)` and `random.sample(lines, 20)`. The file has no duplicate lines, and the same call on the numbers 1 to 72 gives the same positions.

The draw order is 29, 11, 59, 3, 18, 39, 69, 2, 63, 25, 32, 52, 58, 35, 20, 49, 71, 47, 38 and 22.

Sorted, the lines are 2, 3, 11, 18, 20, 22, 25, 29, 32, 35, 38, 39, 47, 49, 52, 58, 59, 63, 69 and 71.

The 52 lines left out are 1, 4 to 10, 12 to 17, 19, 21, 23, 24, 26 to 28, 30, 31, 33, 34, 36, 37, 40 to 46, 48, 50, 51, 53 to 57, 60 to 62, 64 to 68, 70 and 72. They are the pool of the 15-record extension (`random.seed(5901)`, `random.sample(<those 52 line numbers in ascending order>, 15)`), which runs only if the first 20 turn up an error.
