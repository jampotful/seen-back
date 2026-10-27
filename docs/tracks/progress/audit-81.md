# Audit 81: harvest-c23b (branch research/harvest-c23b, head 8f0cfe10)

Gate: `screen_candidates.py --check` on the 37 search records and 9 wanted lines prints "0 problems".

## Sample (seed 81)

`random.seed(81)` and `random.sample(lines, 20)` over the 37 search record lines (1-based) give, in draw order, 33, 30, 22, 25, 31, 2, 6, 5, 15, 35, 34, 20, 1, 11, 10, 12, 8, 23, 36 and 3. The draw was made before any record was read.

## Verdicts (in progress)

First draw drafted: errors at lines 20 (Helleborus sense_light_nonvisual: Herranz Ferrer et al. 2023, Acta Physiol Plant 45: 137, light-temperature requirements of H. foetidus germination) and 36 (Oncosiphon sense_chemical: Perez-Ochoa and de la Rosa, Cal-IPC 2019 poster, smoke raised stinknet germination). The other 18 drafted ok. 2 of 20, so the extension runs: `random.seed(8115)` over the 17 undrawn lines gives 13, 26, 24, 21, 16, 4, 27, 28, 17, 19, 9, 37, 7, 14, 32. 36 WebSearches used.
