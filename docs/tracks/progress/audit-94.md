# Audit 94: desk-d4 (7 plant genera; branch origin/research/desk-d4, head c1dd31e2)

Work in progress; this skeleton is committed early and filled in as checks finish.

## Lines judged

No sample was drawn: the launch prompt asks for the whole unit.
- Search records: all 14 lines of docs/views/searched/desk-d4.jsonl.
- Evidence records: all 6 lines of docs/views/evidence/desk-d4.jsonl.
- Wanted lines: all 5, listed and not counted.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on copies of the searched file (14 lines) and wanted file (5 lines) prints "0 problems".
