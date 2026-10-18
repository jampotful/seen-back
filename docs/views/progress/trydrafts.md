# Progress: trydrafts (18 October)

Branch `agent/trydrafts-1018`. The task: `rows_draft` rows in the voice of `docs/views/VOICE.md` for the views behind `?try=`, from the evidence, through `tools/views/rows.py` on a build machine. The control room took `jumper` and `spider` out of this run (they have drafts from the rows pass and the rewrite track), so the run covers the other 26.

## Done

- `rows.py` could not draft these views, because `docs/views/gaps/rows.json` and the gap table's cells cover only the offered views. Added:
  - `docs/views/gaps/try-rows.json`: every live row about the animal in the 26 views (193 rows), mapped to the traits it rests on; rows about the drawing or the app's choices are left out. A row about one group (elephants, cheetahs, chitons) carries `taxa`, and a row whose title named the picture carries its `live` title.
  - `tools/views/try_species.py` and `docs/views/gaps/try-species.json`: the species that borrow each view (the 60 most recorded of the view's world group, or of its taxa where the world rows have no group, plus the measured species of the view). The world groups hold some animals of the narrower views (harvestmen in `scorpion`, woodlice in `crab`, millipedes in `worm`), so the script also places species by their known order and by English name. The build machine checks out one branch, so the list is committed.
  - `rows.py` reads both files for views the gap table lacks, drafts a group's row for that group's species, and does not send a row with no evidence record whose live row claims something (m, g or x). `report --block rows-try` writes their own block of `docs/views/voice/REPORT.md`. `rows_live.py` covers the 42 views. A test covers the new paths.
- Run 5 of `views-rows` (`run/views-rows/trydrafts-1018`, results in `runs/views-rows/5` on `ci`): 185 rows sent, 100 passed first time (54%), 174 after the retry (94%), 11 failed, 8 not sent, $1.94 at batch prices.
- Drafts applied to the 26 views (`rows_draft` only; every spec is otherwise unchanged, checked by comparing each file with `main`). The four specs with compact parameter lines (reef, sealife, shark, snail) got the block appended as text so that no other line changed.
- `docs/views/voice/try-1018.md`: one line for each of the 28 views. The drafts would make nine views ready to offer: bat, duck, fish, flyingfox, fox, harvestman, snail, whale, worm.
- `python3 build.py --check` passes with `index.html` unchanged, so `rows_draft` stays out of the page. `node test/check4.js try` passes. Its first run failed `shark` on two timing counts (the movement map read 3 times and no gaze jump) at a load average near 6 on the shared machine; `shark` alone and a second full run passed, and the page is byte for byte the one on `main`.

## Next

- The owner reads the drafts. Some pass the checks and still read clumsily (owl Sharpness, snail Eyes).
- The 19 rows without a passing draft (11 failed, 8 not sent) need a decision each: keep the live row after a voice edit, or drop it.
- `try-rows.json` and the genus tables in `try_species.py` are own construction where they name subgroup taxa; a check against GBIF would firm them up.
