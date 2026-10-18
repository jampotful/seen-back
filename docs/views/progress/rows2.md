# Progress: rows2 (burst 11b)

Branch agent/rows2. Started 17 October 2026, continued 18 October.

## Done

- The 14 views whose requests changed (partial flags now read from docs/views/fixes) were re-drafted by the job on run/views-rows/rows2 (run 4 on the ci branch): 49 requests, 48 drafts passed (25 on the first attempt), 1 failed (bee, Red: a "Y, not X" contrast), $0.73. The drafts are applied to `rows_draft` in those 14 views. Cat and spider keep their burst 10 drafts, since their requests did not change.
- `tools/views/rows_live.py` compares each live row with the evidence and writes the block `live-disagreement` of docs/views/voice/REPORT.md. No live row was changed.
- build.py --check passes; rows_draft stays out of the page.

## Next

Promotion of drafts over live rows waits for the owner.
