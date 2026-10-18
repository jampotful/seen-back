# Progress: everyday2 (the dog and the home share's weight)

Task: the two weak spots left by build 34 (`tools/species/EVERYDAY.md`, "Where it is weak"), within the marks of `docs/tracks/prompts/burst13-everyday.md`. Branch: `agent/everyday2`. Clone: `/home/claude/wt-everyday2`. Started 18 October 2026 at 20:35 UTC; time limit 150 minutes.

## Done

- The cause of the dog: GBIF lists `Canis familiaris` as a synonym, so build 34 gave the dog a new row of that name and put its home share there. The world row `Canis lupus` (English name Domestic Dog) matches dog photos better in BioCLIP 2 and had no home share. The dog's probability split between the two rows, the cat's single row took the rest, and the kinds head says `other` for most dog photos. A larger beta alone left the dog at 9 of 20.
- The pocket model's answer (`run/everyday/pocket-2`, `runs/everyday/6-pocket`): right on 17 of the 20 dog test photos away from the county (sure on 14) and on 18 in the county's zone, but sure there on only 2, because the county list has the cat and no dog.
- The fix in `tools/species/everyday_build.py`: a synonym takes the world row of its GBIF-accepted species when that row has the same English name (five species, 19 new rows), and beta is chosen on the tune photos among the betas the world test allows (up to 3,000 read; 100 chosen).
- `run/everyday/again-pub-1` (`runs/everyday/7-again`): every mark passed. Kind right 97.6% and species right 78.8% in each photo's own zone, 97.8% and 78.8% in Alachua's, world-test drops 0.11, 0.66 and 0.57 points, the dog's kind right on 19 of 20.
- `pub/naturalist-everyday2` at `fffd315`, pinned by `pin/naturalist-everyday2-fffd315`; its files match `stage-parts.json`, and a separate reading of them gave the dog the same numbers. `models/naturalist/manifest.json` points at them. `BUILD` is 36 (`main` held 34 and `agent/hardening` 35).
- Every check passed on the tree merged with `main` (build 35 from the hardening track): `build.py` and `--check`, `check4.js try` (14 runs, no errors), every section of `check_rec.js`, `check_ext.js`, `fits_test.js`, `check_make_slot.py`, `test_place.py` and `tools/species/test_everyday_build.py`.
- Merged to `main` as build 36 at 17:50 US Eastern.

## Open

- The pocket's county list needs a dog, which needs county records and a refit: in the county's zone the pocket is right on 18 of 20 dog photos but sure on only 2.
- The cat still takes some photos of the chinchilla, rabbit and guinea pig, and close relatives with a larger share still take `Rosa chinensis`, `Citrus reticulata`, `Bos indicus` and `Zoysia japonica`.
