# Precision audit 43, 18 October 2026 (in progress)

Unit: harvest-30, branch research/harvest-30, commit 45b2a346 (37 search records for 12 genera, 26 wanted lines). The files were read with `git show 45b2a346:<path>` and saved to /tmp/au43/. The audit worktree /tmp/wsau43 was cut from origin/main (965e2f01). No evidence, searched or wanted file, no src/ file and no views/*.json file was edited.

## Mechanical gate

`python3 -I tools/views/screen_candidates.py --check harvest-30.searched.jsonl --wanted harvest-30.wanted.jsonl` printed "0 problems", so the unit passes step 1.

## Sample (step 2)

All 37 lines of the searched file, `random.seed(43)`, `random.sample(lines, 20)`. Line numbers in draw order: 3, 19, 10, 30, 24, 7, 15, 20, 16, 34, 1, 17, 14, 36, 12, 28, 18, 25, 13, 6. Sorted: 1, 3, 6, 7, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 24, 25, 28, 30, 34, 36.

The 20 fall in 10 of the 12 genera (Cocculus and Masticophis have no sampled line): Heliotropium 1, 3; Nekemias 17, 18, 19, 20; Botrypus 10; Riparia 28, 30; Vipera 24; Cistothorus 6, 7; Monobia 12, 13, 14, 15, 16; Lerema 34; Pyrgus 36; Asparagus 25.
