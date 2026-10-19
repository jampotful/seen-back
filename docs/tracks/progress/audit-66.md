# Audit 66, 19 October 2026: harvest-50 (desk-screen unit)

Unit: branch research/harvest-50 at commit 3441dc59, 65 search records (docs/views/searched/harvest-50.jsonl) and 14 wanted lines (docs/views/wanted/harvest-50.jsonl). The copies at /tmp/au66/harvest-50.jsonl and /tmp/au66/harvest-50-wanted.jsonl are byte-identical to `git show 3441dc59:<path>` (checked with cmp).

## Gate (step 1)

`python3 -I tools/views/screen_candidates.py --check /tmp/au66/harvest-50.jsonl --wanted /tmp/au66/harvest-50-wanted.jsonl` printed "0 problems".

## Sample (step 2)

I drew the sample from all 65 search record lines (1-based line numbers) with `random.seed(66)` and `random.sample(lines, 20)` before reading any record. The file has no duplicate lines, and the same call on the numbers 1 to 65 gives the same positions.

The draw order is 10, 40, 28, 60, 16, 51, 29, 19, 17, 56, 62, 36, 7, 48, 32, 12, 30, 34, 9 and 46.

Sorted, the lines are 7, 9, 10, 12, 16, 17, 19, 28, 29, 30, 32, 34, 36, 40, 46, 48, 51, 56, 60 and 62.

The 45 lines left out are the pool of an extension, if one is needed (`random.seed(6601)`, `random.sample(<those 45 line numbers in ascending order>, 15)`), which would draw 24, 37, 14, 64, 15, 38, 53, 45, 59, 23, 18, 25, 47, 2 and 55 (sorted: 2, 14, 15, 18, 23, 24, 25, 37, 38, 45, 47, 53, 55, 59 and 64).

(Verdicts follow.)
