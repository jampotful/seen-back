# Audit 57, 19 October 2026: harvest-41 (desk-screen unit)

Work in progress. The gate and the draw are recorded first, before any record is read.

## Gate (step 1)

`python3 -I tools/views/screen_candidates.py --check /tmp/au57/harvest-41.jsonl --wanted /tmp/au57/harvest-41-wanted.jsonl` printed "0 problems". The copies at /tmp/au57/ are byte-identical to the files at commit 5484fdd2 (checked with cmp).

## Sample (step 2)

All 69 search record lines (1-based line numbers), `random.seed(57)`, `random.sample(lines, 20)`. The draw depends on the line count only: the same call on the numbers 1 to 69 gives the same positions, and all 69 lines are distinct.

Draw order: 6, 48, 3, 29, 42, 62, 19, 28, 41, 54, 57, 25, 2, 56, 68, 11, 34, 39, 24, 58.

Sorted: 2, 3, 6, 11, 19, 24, 25, 28, 29, 34, 39, 41, 42, 48, 54, 56, 57, 58, 62, 68.

The 49 lines left out are 1, 4, 5, 7 to 10, 12 to 18, 20 to 23, 26, 27, 30 to 33, 35 to 38, 40, 43 to 47, 49 to 53, 55, 59 to 61, 63 to 67 and 69. The extension that desk-audit.md calls for after an error, `random.seed(5701)` and `random.sample(<those 49 line numbers in ascending order>, 15)`, gives in draw order 51, 60, 69, 31, 47, 17, 67, 9, 49, 32, 18, 64, 61, 35, 26 (sorted: 9, 17, 18, 26, 31, 32, 35, 47, 49, 51, 60, 61, 64, 67, 69). It runs only if the first 20 hold an error.
