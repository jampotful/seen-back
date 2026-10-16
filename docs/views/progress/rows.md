# Progress: the rows track (burst 10)

Branch `agent/rows`. Prompt: `docs/tracks/prompts/burst10-rows.md`. Started 16 October 2026.

## Done and pushed

- Item 1, the four false live rows, one commit per view (deer, wader, bird, squirrel, bigcat). Each commit message names the records behind the correction. `node test/check4.js try` with `TRY=deer,wader,bird,squirrel,bigcat` and `python3 -I tools/views/check_spec.py` pass.
- Item 2, `tools/views/voice_check.py` and `tools/views/test_voice_check.py`; the counts are in `docs/views/voice/REPORT.md`.
- Item 3, `tools/views/rows.py`, `tools/views/test_rows.py`, the job `views-rows` (`.github/workflows/views-rows.yml`, `ci/views/rows.sh`, `ci/views/rows.env`, plan-only on `main`). A smoke run on the cat view (direct, $0.07) passed 6 of 7 rows on the first attempt and 7 of 7 after the retry.

## Next

- Collect the batch on `run/views-rows/burst10` from the `ci` branch (`runs/views-rows/<n>/`), run `rows.py apply` and `rows.py report`, rebuild with `python3 -I build.py`, merge to `main`.
