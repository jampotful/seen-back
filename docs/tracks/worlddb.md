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

## Where it stands (13 October 2026, branch `agent/world-db`)

Every figure here names the script and the run (on `ci`) that made it.

1. **World rows** (`tools/world/names.py`, `tools/coverage/text.py`, `tools/world/pack.py`; runs `runs/worlddb/1-names`, `1-text-*`, `1-pack`). The 433,156 species of the coverage study's world list take GBIF's names from its backbone (the archive of 28 August 2023, whose keys match the county list's): 379,409 as iNaturalist names them, 1,371 doubtful kept, 15,189 synonyms renamed to their species and 2,424 to the species above a subspecies, 34,703 that the backbone lacks and 51 found only in another kingdom kept as iNaturalist names them. GBIF lumps 11,083 of the species into 5,090 names, so there are 427,163 rows. One sentence a species, one byte a number with a scale a row: 328,061,184 bytes in four parts of 90, 90, 90 and 58.1 MB, a 1.7 MB scale file and a 21.0 MB table of names (English names, from iNaturalist's taxonomy archive, for 134,149 rows). The packed rows' cosine to the half-precision ones is 0.99997 on average and 0.99978 at the least. Published on `pub/naturalist-world`.
2. **A prior on a grid** (`tools/world/grid.py`, `tools/world/prior.py`, `tools/world/zones.py`; runs `runs/worlddb/2-grid`, `3-test`). 114,367,325 research-grade records dated through 2024 have a place; 113,322,735 are of a species with a row. Pairs of a cell and a species: 14.9 million at half a degree, 9.2 million at 1 degree, 5.5 million at 2, 4.0 million at 3. The world test scored 1 and 2 degrees alike (below), so the page gets 2 degrees: `place.bin` 13.2 MB and `zones.json` 1.2 MB (at 1 degree, 22.2 and 3.9 MB). The time zone's first guess comes from the tz database 2026b (`zone.tab`, `backward`) and Natural Earth's countries; in a country of several zones, a zone's share of a cell follows its offset from UTC against the cell's longitude, and its distance from the zone's point.
3. **The encounter rule** (`tools/world/place.py`, checked by `tools/world/test_place.py`): a Bayesian update over cells by the share of each confidently named species within 400 km of each cell, with 2% of the first guess left to the whole world so that a wrong guess can be overturned.
4. **The world test** (`tools/world/worldtest.py`, run `runs/worlddb/3-test`): 3,500 photos, 500 a continent, dated 2025 or later; 97.9% of them are of a species with a row. Right species first, the prior's weight chosen for each continent on the other six. A photo's time zone is the one timezone-boundary-builder's polygons give its place (measurement only). The three creatures met are its observer's own research-grade records in the same zone, the latest on or before the photo's date first (3,312 photos), filled out with later ones or other people's from the same one-degree cell; each is taken as named right, which flatters this column by the share of the app's names that are wrong.

| Continent | No prior | Time zone | Time zone and three creatures met | The true 400 km circle |
|---|---:|---:|---:|---:|
| Africa | 65.6% | 79.6% | 80.4% | 82.2% |
| Asia | 63.8% | 78.8% | 80.8% | 82.0% |
| Europe | 76.2% | 90.6% | 91.2% | 90.0% |
| North America | 79.0% | 90.6% | 91.0% | 91.2% |
| Oceania | 69.2% | 83.0% | 84.2% | 84.6% |
| South America | 66.2% | 78.0% | 78.4% | 79.4% |
| Antarctica | 26.8% | 32.0% | 33.4% | 42.0% |
| All, 3,500 | 63.8% (62.2 to 65.4) | 76.1% (74.7 to 77.4) | 77.1% (75.7 to 78.5) | 78.8% (77.5 to 80.1) |

The time zone and creatures columns are for the 2-degree files the page downloads; at 1 degree they are 75.9% and 77.2%. Naming at the level that was right 97 times in 100 on the other six continents, the time zone and three creatures name 64.2% of photos, and 96.8% of those names are right. Every continent holds 97 in 100 but Antarctica (74.4%), with Asia at 97.0% and South America at 97.2%; with the time zone alone Asia falls to 96.6% and Antarctica is at 75.5%. So the pass mark of `docs/COVERAGE.md`, 97 names in 100 on every continent, is not met in Antarctica. The plainer reading: most of the gain comes from knowing the continent and the country, which the time zone gives; the creatures add a point.

5. **The page** (`src/cam.rec.js`, `vendor/rec-worker.js`, `src/cam.r.js`, `src/cam.c2.js`). `models/naturalist/manifest.json` names the world rows, their scale and table and the place files on a pinned commit of `pub/naturalist-world` (`tools/world/manifest.py`); the consent sheet, the progress line and the About block count every file. The worker scores rows at one byte a number; the prior is the share of each species where the phone probably is, from the time zone (`Intl`) and the creatures the full database named with confidence in that zone, kept on the device under their scientific names (`seenback.place.v1`) and taken back when a name is corrected. Nothing reads a photo's location or asks for one. `test/rec/check_rec.js large` covers it with a stand-in (`test/rec/make_world_standin.py`): the same answers as `tools/world/place.py`, a time zone and an alias deciding between two look-alike species, and a creature met deciding where the zone does not.
