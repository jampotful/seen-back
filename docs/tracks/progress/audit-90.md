# Audit 90: desk-c12 (16 plant genera; branch origin/research/desk-c12, head 47867368)

Status: in progress.

## Scope

All 21 search records (docs/views/searched/desk-c12.jsonl) and all 8 evidence records (docs/views/evidence/desk-c12.jsonl) are judged, so any error line can simply be dropped. No sample was drawn.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on copies of the searched (21 lines) and wanted (7 lines) files prints "0 problems".

## Queries and chased

`harvest_get.py` (origin/ci, no network) for the ten harvest genera: every record's unprefixed `queries` equal the output's `query` and `family review` lines word for word and in order, with the "web: " lines after them. No harvest shows "gave up". Salix, Olea and Coccoloba are in no harvest run and list "web: " lines only. Every harvest record's `chased` names the citation-step DOIs its output prints.
