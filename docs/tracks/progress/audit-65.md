# Audit 65, 19 October 2026: harvest-49 (desk-screen unit)

Unit: branch research/harvest-49 at commit c9a5ceed, 66 search records (docs/views/searched/harvest-49.jsonl) and 13 wanted lines (docs/views/wanted/harvest-49.jsonl). The copies at /tmp/au65/harvest-49.jsonl and /tmp/au65/harvest-49-wanted.jsonl are byte-identical to `git show c9a5ceed:<path>` (checked with cmp).

## Gate (step 1)

`python3 -I tools/views/screen_candidates.py --check /tmp/au65/harvest-49.jsonl --wanted /tmp/au65/harvest-49-wanted.jsonl` printed "0 problems".

## Sample (step 2)

Drawn from all 66 search record lines (1-based) with `random.seed(65)` and `random.sample(lines, 20)` before any record was read. The file has no duplicate lines, and the same call on the numbers 1 to 66 gives the same positions.

The draw order is 54, 37, 65, 33, 55, 15, 29, 30, 34, 60, 36, 22, 53, 41, 28, 61, 5, 56, 59 and 17.

Sorted, the lines are 5, 15, 17, 22, 28, 29, 30, 33, 34, 36, 37, 41, 53, 54, 55, 56, 59, 60, 61 and 65.

The 46 lines left out are 1 to 4, 6 to 14, 16, 18 to 21, 23 to 27, 31, 32, 35, 38 to 40, 42 to 52, 57, 58, 62 to 64 and 66. If an error is found, the extension draws from them with `random.seed(6501)` and `random.sample(<those 46 line numbers in ascending order>, 15)`, which gives 64, 52, 23, 10, 39, 14, 9, 35, 38, 62, 21, 12, 48, 50 and 20 (sorted: 9, 10, 12, 14, 20, 21, 23, 35, 38, 39, 48, 50, 52, 62 and 64).

(Report in progress.)
