# Audit 90: desk-c12 (16 plant genera; branch origin/research/desk-c12, head 47867368)

Status: in progress (gate, queries and chased done; searches running).

## Lines judged

No sample was drawn: the launch prompt asks for the whole unit, so error lines can simply be dropped.
- Search records: all 21 lines of docs/views/searched/desk-c12.jsonl.
- Evidence records: all 8 lines of docs/views/evidence/desk-c12.jsonl.
- Wanted lines: all 7, listed and not counted.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on a copy of the searched file (21 lines) with the wanted file (7 lines) prints "0 problems".

## Queries and chased

`harvest_get.py` (origin/ci, no network) for the ten harvest genera with records (Rumex, Lunaria, Ficaria, Urtica, Daucus, Ficus, Lespedeza, Cenchrus, Cerastium, Carex): a script compared every record's unprefixed `queries` with the output's `query` and `family review` lines. All 15 harvest records (lines 1 to 15) match word for word and in order, with the "web: " lines after them. No harvest shows "gave up". Salix, Olea and Coccoloba (lines 16 to 21) are in no harvest run and list "web: " lines only. Every harvest record's `chased` names exactly the citation-step DOIs its output prints.
