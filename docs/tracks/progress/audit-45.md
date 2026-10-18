# Precision audit 45, 18 October 2026

Unit: harvest-31 (branch research/harvest-31, commit 8fb25f0a), a desk screening unit written under desk-screen.md. The unit file holds 77 search records for 15 genera and 14 wanted lines, with no evidence records. The desk holds back its Comarum and Phalaris records (1 and 3 records) because harvest steps for those genera failed on the build machine, so this audit covers the other 73 search records, in 13 genera (Dielis, Pentaglottis, Chelone, Pyrrhocorax, Echinargus, Acmispon, Alisterus, Gymnoscelis, Calliteara, Cercopis, Sitobolium, Gallirallus, Leptotila), and the unit's 14 wanted lines. The 73 records were saved to /tmp/au45/harvest-31-subset.jsonl and the wanted lines to /tmp/au45/harvest-31-wanted.jsonl. I checked that the subset is the original file in its original order with exactly four records removed (Comarum eye_type; Phalaris diel, eye_type and sense_chemical) and that the wanted file equals the unit's own. Lines are numbered as they stand in the subset file. The audit worktree /tmp/wsau45 was cut from origin/main (32449f18).

## Mechanical gate (step 1)

`python3 -I tools/views/screen_candidates.py --check /tmp/au45/harvest-31-subset.jsonl --wanted /tmp/au45/harvest-31-wanted.jsonl` printed "0 problems", so the unit goes on to the sample.

## Sample (step 2)

All 73 lines of the subset file, `random.seed(45)`, `random.sample(lines, 20)`. The draw used the line count only, and it is written here before any record was read or any search run. Line numbers in draw order:

35, 54, 63, 33, 11, 39, 44, 3, 10, 62, 1, 8, 19, 52, 64, 20, 55, 48, 42, 66

Sorted: 1, 3, 8, 10, 11, 19, 20, 33, 35, 39, 42, 44, 48, 52, 54, 55, 62, 63, 64, 66.

The 20 fall in 11 of the 13 genera (Chelone and Acmispon have no sampled line): Dielis 1, 3; Pentaglottis 8, 10, 11; Pyrrhocorax 19; Echinargus 20; Alisterus 33, 35; Gymnoscelis 39, 42; Calliteara 44, 48; Cercopis 52, 54; Sitobolium 55; Gallirallus 62, 63, 64; Leptotila 66. Four are plant lines (8, 10, 11, 55) and sixteen are animal lines.

Verdicts follow in the next commit.
