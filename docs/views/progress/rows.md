# Progress: the rows track (burst 10)

Branch `agent/rows`. Prompt: `docs/tracks/prompts/burst10-rows.md`. Started 16 October 2026.

## Done

- Item 1, the four false live rows, one commit per view (deer, wader, bird, squirrel, bigcat). Each commit message names the records behind the correction. `TRY=deer,wader,bird,squirrel,bigcat OPTIONS=0 node test/check4.js try` and `python3 -I tools/views/check_spec.py` pass.
- Item 2, `tools/views/voice_check.py` and `tools/views/test_voice_check.py`; the counts, per rule and per view, are in `docs/views/voice/REPORT.md` with the figures from before and after the corrections.
- Item 3, `tools/views/rows.py`, `tools/views/test_rows.py`, the job `views-rows` (`.github/workflows/views-rows.yml`, `ci/views/rows.sh`, `ci/views/rows.env`, plan-only on `main`). Two batch runs on the build machine (Sonnet 5.5): the eight views with the most records (`runs/views-rows/2` on `ci`, $0.40) and the other eight offered views (`runs/views-rows/3`, $0.29). The drafts are the `rows_draft` blocks of `views/<key>.json`; the pass rates, the rows that failed and ten drafts beside the live rows are in `docs/views/voice/REPORT.md`.

## How to rerun

`git push origin <branch>:run/views-rows/<label>` with `ROWS_PLAN_ONLY=0` in `ci/views/rows.env` on that branch; the results come back on `ci` and on `pub/rows-draft`. Then `python3 -I tools/views/rows.py apply --views <list> --from <dir>[,<dir>]` and `... report --from <dir>[,<dir>]`.

## Open

- The jumping spider and the spiders have no `rows.json` entry; their row slots are the `SLOTS` table in `rows.py`. The owner or the research thread may rename them.
- The drafts' species lists come from the gap table (`docs/views/gaps/cells.jsonl`), which counts the 1,200 most recorded species of a big view; the request names the first 32.
- `rows_draft` adds about 80 kB to `index.html`.
