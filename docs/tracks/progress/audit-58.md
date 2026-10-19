# Audit 58, 19 October 2026: harvest-43 (desk-screen unit)

Work in progress. The sample was drawn and committed before any record was read.

## Gate (step 1)

`python3 -I tools/views/screen_candidates.py --check /tmp/au58/harvest-43.jsonl --wanted /tmp/au58/harvest-43-wanted.jsonl` printed "0 problems".

## Sample (step 2)

All 72 search record lines (1-based line numbers), `random.seed(58)`, `random.sample(lines, 20)`.

Draw order: 26, 27, 72, 6, 25, 58, 52, 46, 37, 66, 57, 17, 29, 63, 40, 71, 19, 38, 7, 1

Sorted: 1, 6, 7, 17, 19, 25, 26, 27, 29, 37, 38, 40, 46, 52, 57, 58, 63, 66, 71, 72

The 52 lines left out are 2 to 5, 8 to 16, 18, 20 to 24, 28, 30 to 36, 39, 41 to 45, 47 to 51, 53 to 56, 59 to 62, 64, 65 and 67 to 70. The extension that runs only after an error, `random.seed(5801)` and `random.sample(<those 52 line numbers in ascending order>, 15)`, gives in draw order 33, 62, 55, 43, 24, 9, 5, 53, 44, 15, 67, 30, 61, 32, 59 (sorted: 5, 9, 15, 24, 30, 32, 33, 43, 44, 53, 55, 59, 61, 62, 67).
