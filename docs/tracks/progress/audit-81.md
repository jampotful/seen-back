# Audit 81: harvest-c23b (branch research/harvest-c23b, head 8f0cfe10)

Gate: `screen_candidates.py --check` on the 37 search records and 9 wanted lines prints "0 problems".

## Sample (seed 81)

`random.seed(81)` and `random.sample(lines, 20)` over the 37 search record lines (1-based) give, in draw order, 33, 30, 22, 25, 31, 2, 6, 5, 15, 35, 34, 20, 1, 11, 10, 12, 8, 23, 36 and 3. The draw was made before any record was read.

Audit in progress.
