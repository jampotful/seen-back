# Progress: everyday (burst 13, the species people photograph at home)

Prompt: `docs/tracks/prompts/burst13-everyday.md`. Branch: `agent/everyday`. Clone: `/home/claude/wt-everyday`.
Started 18 October 2026, 19:02 UTC. The time limit of 210 minutes ends at 22:32 UTC.

## Done

- Step 1: `tools/species/EVERYDAY.md` says where a species must be added on each path (pocket list, pocket kinds head, the larger model's rows, its prior, its kinds head, the kind of eye, typed names, the service).
- Step 2: `tools/species/everyday_list.csv` (175 queries) resolved on build machines by `tools/species/everyday.py resolve` (runs `runs/everyday/1-resolve` and `3-resolve` on `ci`): `data/everyday/species.csv` (174 species with GBIF keys, names, ranks and lineages from api.gbif.org, kinds from `eyes.py`, iNaturalist taxa, English names and counts of captive or cultivated observations) and `data/everyday/photos.csv` (5,209 photos, 1,675 tune and 3,534 test).
- Step 3 code: `tools/species/everyday_build.py` (new rows made as the world rows were, the home share, the page's arithmetic in numpy, the world test before and after, the staged files), `ci/everyday/build.sh`, `.github/workflows/everyday.yml` (resolve, embed in six shards, build, pocket). The page reads `home` from the table (`readTable`), adds it in `placeOf`, and keeps home rows out of the encounter rule; `tools/world/place.py` and `prior.py` mirror it; the world stand-in carries a home row.
- Step 4: `gotCloser` in `src/cam.c2.js` shows the kind's name when the larger model is sure of the kind and unsure of the species and the name on screen is the small model's species. `test/rec/check_rec.js large` checks it (`kindOnly`): it passes with the fix and fails without it (the name stayed "great blue heron").
- Typed names: `LEX` in `src/cam.r.js` knows pothos, monstera, hydrangea, geranium, lawn and others; `check4.js lex` passes (106 tried, 0 wrong).

## Pushed

- `agent/everyday` up to the pocket job. Runs: `run/everyday/build-pub-1` (started 19:39 UTC), `run/everyday/pocket-1` (19:43 UTC).

## Next

- Read `runs/everyday/<n>-build` and `<n>-pocket` on `ci`; if the marks pass, pin `pub/naturalist-everyday`, point the manifest at it with `tools/species/everyday_manifest.py`, bump `BUILD`, run every check, merge to `main`, and write `docs/LOG.md` and the results in `EVERYDAY.md`. If a mark fails, ship nothing on that path and write the measurement down.
