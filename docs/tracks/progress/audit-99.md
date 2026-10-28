# Audit 99: desk-d8 (12 plant genera; branch origin/research/desk-d8, head 2a3a044c)

Work in progress. Verdicts follow as they are checked.

## Lines judged

No sample was drawn. The launch prompt asks for the whole unit, so that error lines can simply be dropped.
- Search records: all 26 lines of docs/views/searched/desk-d8.jsonl (1 to 26). (The progress note says 25; the file holds 26.)
- Evidence records: all 12 lines of docs/views/evidence/desk-d8.jsonl (1 to 12).
- Wanted lines: all 3, listed and not counted.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on copies of the searched file (26 lines) and the wanted file (3 lines) prints "0 problems".
