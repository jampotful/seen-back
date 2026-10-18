# Progress: everyday (burst 13, the species people photograph at home)

Prompt: `docs/tracks/prompts/burst13-everyday.md`. Branch: `agent/everyday`. Clone: `/home/claude/wt-everyday`.
Started 18 October 2026, 19:02 UTC; the time limit of 210 minutes ends at 22:32 UTC. Stopped at 19:47 UTC by the rule of `burst2-common.md`, because the first agent's context passed 100,000 tokens. Nothing is merged to `main` yet.

## Done and pushed

- Step 1: `tools/species/EVERYDAY.md` says where a species must be added on each path and how the measurement works. Its results section is still to be written.
- Step 2: `tools/species/everyday_list.csv` (175 queries) was resolved on build machines by `tools/species/everyday.py resolve` (runs `runs/everyday/1-resolve` and `3-resolve` on `ci`). That gave `data/everyday/species.csv` (174 species: GBIF keys, names, ranks and lineages from api.gbif.org, kinds from `eyes.py`, iNaturalist taxa, English names and counts of captive or cultivated observations) and `data/everyday/photos.csv` (5,209 photos: 1,675 tune and 3,534 test).
- Step 3 code: `tools/species/everyday_build.py` makes the new rows the way the world rows were made, adds the home share, runs the page's arithmetic in numpy, runs the world test before and after, and stages the changed files. Also `ci/everyday/build.sh` and `.github/workflows/everyday.yml` with jobs `resolve`, `embed` (six shards), `build` and `pocket`. `tools/species/everyday_pocket.py` measures the pocket model's kind. `tools/species/everyday_manifest.py` points the manifest at the published files. The page reads `home` from the table (`readTable` in `src/cam.rec.js`), adds it in `placeOf`, and keeps home rows out of the encounter rule. `tools/world/place.py` and `prior.py` do the same in Python, and `tools/world/test_place.py` tests it (0 failed). The world stand-in (`test/rec/make_world_standin.py`, regenerated) carries one home row.
- Step 4: in `gotCloser` (`src/cam.c2.js`), when the larger model is sure of the kind and unsure of the species and the name on screen is the small model's species, the kind's name replaces it. The `kindOnly` check in `test/rec/check_rec.js large` covers it. It passed with the fix and failed without it, where the name stayed "great blue heron" from the small model.
- Typed names: `LEX` in `src/cam.r.js` now knows pothos, monstera, hydrangea, geranium, lawn and more. `node test/check4.js lex` passed (106 tried, 0 wrong). `python3 -I build.py` and `--check` passed at build 32.

## Running when the first agent stopped

- `run/everyday/build-pub-1` (commit `444f7105`, started 19:39 UTC). Its results land on `ci` as `runs/everyday/<n>-build/` (`everyday.json`, `stage-parts.json`, `log.txt`). It publishes the changed files to `pub/naturalist-everyday`.
- `run/everyday/pocket-1` (commit `70cf77a4`, started 19:43 UTC). Its results land as `runs/everyday/<n>-pocket/pocket.json`.
- Two local checks were also running and had not reported: `check_rec.js large` with the regenerated world stand-in (with the home row) and `check4.js try`. Run both again.

## Next, in order

1. Wait with `bash ci/wait.sh $(git rev-parse 444f7105) 1 3000`, then read `everyday.json`: `marks` (`own`, `alachua`, `world_test_no_drop_over_1_point`), `test`, `test_beta0`, `beta`, `world_drop_points`, `route_check_cosine` (should be about 1) and `by_species`. If the job failed, read `log.txt`, fix it and push to `run/everyday/build-pub-2`.
2. If every mark passes, run `git fetch --depth 1 origin pub/naturalist-everyday` and pin that commit with `git push origin FETCH_HEAD:refs/heads/pin/naturalist-everyday-<first 7 of sha>`. Then run `python3 -I tools/species/everyday_manifest.py --parts stage-parts.json --commit <sha> --results everyday.json`. Only the last rows part, the scale, the table and the place file move; the other parts and the zones stay on `9ae0806`. If a mark fails, leave `models/naturalist/manifest.json` as it is (the page's `home` code does nothing without a `home` list), ship the rest, and write the measurement down.
3. Read `pocket.json` and write the pocket model's kind on these photos into `EVERYDAY.md`. The pocket's county list is not extended: it names no species since build 21, and its rows need research-grade county records and a refit.
4. Fetch `main` and `agent/hardening`. Hardening has `BUILD = '33'` on its branch and changes `src/cam.rec.js` and `test/rec/check_rec.js`. Merge `origin/main`, then set `BUILD` in `src/cam.a.js` to the larger of the two plus one. The `kindOnly` comment in `check_rec.js` says "build 33"; fix it to the shipped number.
5. Run `python3 -I build.py`, `python3 -I build.py --check`, `node test/check4.js try`, and every section of `node test/rec/check_rec.js` (with `node test/rec/serve.js 8782` running and `NODE_PATH=/home/claude/.npm-global/lib/node_modules`). The `large` section alone takes about 8 minutes.
6. Merge to `main`. Add a dated entry to `docs/LOG.md`, give the results in `EVERYDAY.md`, and add an everyday row to `docs/STATUS.md` (only that row).
