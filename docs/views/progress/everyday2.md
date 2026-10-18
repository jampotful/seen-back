# Progress: everyday2 (the dog and the home share's weight)

Task: the two weak spots left by build 34 (`tools/species/EVERYDAY.md`, "Where it is weak"), within the marks of `docs/tracks/prompts/burst13-everyday.md`. Branch: `agent/everyday2`. Clone: `/home/claude/wt-everyday2`. Started 18 October 2026 at 20:35 UTC; time limit 150 minutes.

## Done

- The cause of the dog: GBIF lists `Canis familiaris` as a synonym, so build 34 gave the dog a new row of that name and put its home share there. The world row `Canis lupus` (English name Domestic Dog) matches dog photos better in BioCLIP 2 and had no home share. The dog's probability split between the two rows, the cat's single row took the rest, and the kinds head says `other` for most dog photos. A larger beta alone left the dog at 9 of 20.
- The pocket model's answer (`run/everyday/pocket-2`, `runs/everyday/6-pocket`): right on 17 of the 20 dog test photos away from the county (sure on 14) and on 18 in the county's zone, but sure there on only 2, because the county list has the cat and no dog.
- The fix in `tools/species/everyday_build.py`: a synonym takes the world row of its GBIF-accepted species when that row has the same English name (five species, 19 new rows), and beta is chosen on the tune photos among the betas the world test allows (up to 3,000 read; 100 chosen).
- `run/everyday/again-pub-1` (`runs/everyday/7-again`): every mark passed. Kind right 97.6% and species right 78.8% in each photo's own zone, 97.8% and 78.8% in Alachua's, world-test drops 0.11, 0.66 and 0.57 points, the dog's kind right on 19 of 20.
- `pub/naturalist-everyday2` at `fffd315`, pinned by `pin/naturalist-everyday2-fffd315`; its files match `stage-parts.json`, and a separate reading of them gave the dog the same numbers. `models/naturalist/manifest.json` points at them. `BUILD` is 36 (`main` held 34 and `agent/hardening` 35).
- `check4.js try` (14 runs, no errors), `check_make_slot.py` and `test_place.py` passed on the branch.

## Next

- Every section of `check_rec.js`, then fetch `main`, merge, build, check and push to `main`.
- Left for later: a dog in the pocket's county list (county records and a refit); the chinchilla, rabbit and guinea pig, which the cat still takes on some photos.
