# Audit 82: harvest-c22b (branch research/harvest-c22b, head d5808544)

Gate: `screen_candidates.py --check` on the 35 search records and 25 wanted lines prints "0 problems".

## Sample (seed 82)

`random.seed(82)` and `random.sample(lines, 20)` over the 35 search record lines (1-based) give, in draw order, 10, 32, 33, 19, 27, 26, 6, 30, 29, 22, 9, 31, 2, 14, 16, 34, 4, 7, 35 and 5. The draw was made before any record was read; the same call on the numbers 1 to 35 gives the same positions.
