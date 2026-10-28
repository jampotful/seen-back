# Audit 95: desk-d5 (7 plant genera; branch origin/research/desk-d5, head aa8b0bb3)

In progress. Whole unit judged: searched lines 1 to 9, evidence lines 1 to 14, wanted lines 1 and 2 (listed, not counted).

## Gate

`python3 -I tools/views/screen_candidates.py --check` on copies of the unit's searched (9 lines) and wanted (2 lines) files prints "0 problems".

## Queries

A script compared each record's unprefixed `queries` with the `query` and `family review` lines `harvest_get.py` prints: all 9 match (Teucrium and Tilia word for word and in order; Sassafras and Eryngium are in no harvest run and list "web: " lines only). Chased DOIs on lines 5, 6 and 9 are the printed citation steps.
