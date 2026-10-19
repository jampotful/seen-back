# Audit 67, 19 October 2026: harvest-51 (desk-screen unit)

## Sample (step 2)

I drew the sample from all 62 search record lines of /tmp/au67/harvest-51.jsonl (1-based line numbers) with `random.seed(67)` and `random.sample(lines, 20)`, before reading any record. The file has no duplicate lines, and the same call on the numbers 1 to 62 gives the same positions.

The draw order is 5, 8, 50, 27, 30, 59, 18, 39, 28, 32, 40, 56, 14, 42, 3, 43, 12, 19, 48 and 11.

Sorted, the lines are 3, 5, 8, 11, 12, 14, 18, 19, 27, 28, 30, 32, 39, 40, 42, 43, 48, 50, 56 and 59.

The 42 lines left out are the pool of the extension (`random.seed(6701)`, `random.sample(<those 42 line numbers in ascending order>, 15)`), which would draw 10, 57, 44, 15, 17, 6, 37, 9, 24, 2, 54, 22, 55, 21 and 26. It runs only if I find an error.
