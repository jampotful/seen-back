# Progress: trydrafts (18 October)

Branch `agent/trydrafts-1018`. The task: `rows_draft` rows in the voice of `docs/views/VOICE.md` for the views behind `?try=`, from the evidence, through `tools/views/rows.py` on a build machine. The control room took `jumper` and `spider` out of this run (they have drafts from today's rows pass and another agent may be rewriting them), so the run covers the other 26.

## Done

- `rows.py` could not draft these views: `docs/views/gaps/rows.json` and the gap table's cells cover only the offered views. Added:
  - `docs/views/gaps/try-rows.json`: every live row about the animal in the 26 views, mapped to the traits it rests on; rows about the drawing or the app's choices are left out. A row about one group (elephants, cheetahs, chitons) carries `taxa`, and a row whose title named the picture carries its `live` title.
  - `tools/views/try_species.py` and `docs/views/gaps/try-species.json`: the species that borrow each view (the 60 most recorded of the view's world group, or of its taxa where the world rows have no group, plus the measured species of the view). The build machine checks out one branch, so the list is committed.
  - `rows.py` reads both files for views the gap table lacks, drafts a group's row for that group's species, and does not send a row with no evidence record whose live row claims something (m, g or x); those are listed as not sent. `report --block rows-try` writes their own block of `docs/views/voice/REPORT.md`. A test covers the new paths.
- Plan: 185 requests, 8 rows not sent, estimate $0.54 at batch prices before retries.

## Next

1. The run on `run/views-rows/trydrafts-1018` (batch, ceiling $6), results on the `ci` branch and `pub/rows-draft`.
2. `rows.py apply` for the 26 views, `report --block rows-try`, `rows_live.py` over all 42 views, `docs/views/voice/try-1018.md`.
3. `python3 build.py --check`, `node test/check4.js try`, fetch and merge `main`, merge to `main`.
