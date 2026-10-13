# Track A2: the full database for the whole world

Read this whole file, then `docs/COVERAGE.md` ("The owner's decisions" and "The full database"), `docs/HANDOFF.md`, `docs/CONTRACTS.md`, `docs/LICENCES.md`, `tools/coverage/` and `tools/world/README.md`.

## The owner's decisions (12 October 2026)

The full database holds every species, about 700 MB with its encoder. The app learns the place from the phone's time zone and from the creatures already met. It never reads a photo's location, and it never asks.

## What exists

- The full database today is the slot `models/naturalist/`: BioCLIP 2 L/14, its encoder fetched in parts from a pinned commit, with rows for the county's species. The page downloads it only with the person's consent (`docs/CONTRACTS.md`).
- `tools/coverage/` made the lists (`lists.py`, from iNaturalist's open-data snapshot), the text rows (`text.py`) and the scores (`score.py`) in `docs/COVERAGE.md`: 433,156 world rows at one byte a number is 332.7 MB; the prior `alpha * log(share)` of an area's records; a 400 km circle round the photo is the prior that holds up for every list size.
- `tools/world/` and the branch `pub/data-world`: photos of the 33 groups worldwide, with `test.csv` (continents interleaved) and lab manifests.
- The time-zone rule for the pocket model's county list is on `agent/world-head` (`zoneNear` in `src/cam.c2.js`).

## What to do

1. **World rows.** Text rows for all 433,156 species with GBIF's names (the county rows use GBIF's names, and `docs/COVERAGE.md` explains why), one sentence a species as in run 1, one byte a number with a scale per row, made on build machines in shards and published to `pub/naturalist-world` in parts under 95 MB each, with a manifest and checksums.
2. **A prior on a grid.** For each cell of a world grid (choose the size from the data; 1 degree is a start), the research-grade record counts of each species through 2024, stored sparsely and compressed, small enough to download with the rows. A first guess from the time zone alone: the cells a zone covers, from public-domain data (the tz database's `zone1970.tab` gives each zone's countries and a point).
3. **The encounter rule.** As the person meets creatures that the app names with confidence, weigh the cells where those species are recorded (a Bayesian update over cells, kept on the device). Write it first in Python (`tools/world/place.py`) with tests.
4. **A world test.** 500 photos per continent from `pub/data-world`'s test set, scored with L/14 (the lab makes the vectors: `tools/lab`, `ci/lab`), top-1 right with no prior, with the time zone's prior, with the time zone and three creatures met, and with the true 400 km prior. Report the table.
5. **The page.** On the branch `agent/world-db` from `main`: the full database's rows from the world parts, the consent sheet's size updated, the prior from the time zone and the encounters, and `test/rec/check_rec.js` (section large) passing. Do not merge to `main`; the app's thread ships it.

## Your machine and your branches

The cloud machine can be replaced without warning, which deletes everything on it. Clone with `git clone --depth 1 https://github.com/jampotful/seen-back /home/claude/seen-back` (allow ten minutes), fetch other branches with bounded fetches, and push your work at least every 30 minutes. Build machines: a push to `run/<workflow>/<label>` runs a workflow; results return to the branch `ci` under `runs/`; large outputs go to `pub/*` branches through `ci/put_branch.sh`; GitHub refuses any single file over 100 MB. Commit as `git -c user.name=Claude -c user.email=noreply@anthropic.com commit` with your session's attribution lines. Never push to `main`.

## Your report

At most 400 words: the sizes, the world test table, what the page now does on your branch, and the branches and commits you pushed.
