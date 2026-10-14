# Progress: views (burst 7)

Started 13 October 2026, 20:39 US Eastern; branch `agent/views`. Console spend about $3 of the $10.

## Done and pushed
- **The `try` check.** On `main` the check did not fail for `jumper` (14 of 14 rows) or `spider` (8 of 8): the sheet (`openInfo` in `src/cam.c2.js`) shows every row of a spec whatever drawing option is on, so no row is hidden. The check now requires the sheet to show exactly the rows the spec holds, and loads each view again for every drawing option its `draw` block names past the first of each category, requiring the same view, the same rows, no error and no GL error (`OPTIONS=0` skips it, `OPTION_SECS` sets the wait). A view with a movement map needs `TRY_SECS` of 10 or more (the default is 30). Run on all 32 views that `?try=` reached before the four new ones, and on the four: all pass. `hawk` is not reached by `?try=` (it has no trial block).
- **The glossary.** `views/PARAMS.md` (every whole-picture setting, zone key, gaze key and block key, with units and which eye or region the value comes from, and an entry "which eye" that states the rule). `tools/views/compile.py` reads it (`read_glossary`, `glossary_text`) and sends all of it in each view's request, before the example spec. It also gives gaze, zone and block keys the widest range any spec gives them (the jumper draft was refused for a `gaze.twist` range the model made up). Tests in `tools/views/test_compile.py` check that every setting the engine reads has an entry.
- **Four specs.** `views/primate.json`, `whale.json`, `scorpion.json`, `cephalopod.json`, from the b6 Sonnet drafts on `pub/views-draft`, corrected against the records (see the final report in the merge commit).

## Compiler agreement with the hand-made specs (same value within 10%)
Sonnet 5.5, five samples each before (b1, b3 to b6) and with the glossary (g1 to g4, g7); Haiku 5.5, five before and three with it (g5, g6, g7).

| | before | with the glossary |
|---|---|---|
| Sonnet, jumper | 13 of 31 shared parameters (42%); 6.2 shared a run; 11.2 drafted | 19 of 51 (37%); 10.2 shared; 15.4 drafted |
| Sonnet, bee | 8 of 19 (42%); 3.8 shared | 10 of 27 (37%); 5.4 shared |
| Haiku, jumper | 12 of 28 (43%); 5.6 shared | 39 of 47 (83%); 15.7 shared |
| Haiku, bee | 5 of 21 (24%); 4.2 shared | 5 of 14 (36%); 4.7 shared |

The glossary roughly doubles the parameters a draft shares with the hand-made spec. Sonnet's share that agrees does not rise. Haiku's rises sharply on the jumper. The whole-picture `cpd` is still wrong in Haiku (3.8, the front eyes' value; the hand-made 0.5) and Sonnet gives 0.8 to 1.3 (graded `i` or `m`). Samples are few.
