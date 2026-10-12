# tools/world

Photos from every continent for the base app's group head and for the full database's world test (`docs/COVERAGE.md`, steps 3 and 8 of its order of work). Everything comes from iNaturalist's open-data snapshot in its public bucket, with no API.

- `groups.py` gives every iNaturalist taxon one of the 33 groups of creatures (the fourteen kinds of eye with views and the nineteen groups with none yet), or `person` or `other`. Its rules are those of `tools/species/eyes.py` for the fourteen and those of `docs/views/world-orders.csv` as `docs/COVERAGE.md` merges them for the nineteen; `test_groups.py` checks them on 63 lineages.
- `continents.py` gives each half-degree cell of the world a continent, from Natural Earth's countries (public domain). Islands and lands overseas take the continent of the nearest mainland, and cells at sea that of the nearest land.
- `select.py pick` ranks candidates for each set, spread across continents, then orders, then species, with at most 30 photos from one observer in a group's set; `select.py finish` keeps the ranked observations whose first photo passes the licence rule `nc` and writes the manifests and `SUMMARY.md`.
- `ci/world/world.sh` runs it all on a build machine: it streams `observations.csv.gz` once (keeping at most three research-grade observations of a species on a continent before 2025, three from 2025 on and two casual ones, more in the groups with fewest species, and an even sample from 2025 on) and `photos.csv.gz` once (keeping the photos of the ranked observations). Push a commit to `run/world/<label>` (`.github/workflows/world.yml`). The manifests go to the branch `pub/data-world`; the summary and the log come back on `ci` as `runs/world/<run>`.

The sets, in `pub/data-world`:

| File | What it holds |
|---|---|
| `fit.csv` | up to 3,000 photos a group, research grade, dated through 2024, for fitting the group head |
| `tune.csv` | 300 photos a group, research grade, dated 2025 or later, for choosing settings |
| `test.csv` | 300 photos a group, research grade, dated 2025 or later, sharing no observation with `tune.csv`; they choose nothing |
| `casual.csv` | up to 300 photos a group of casual grade (captive or cultivated, or missing evidence), for pets, zoos and gardens |
| `species.csv` | 500 photos a continent, research grade, dated 2025 or later, at most two a species, chosen by observation, for the full database's world test |

Columns: `set, group, continent, inat_taxon, sci, rank, order, class, phylum, kingdom, date, obs_url, photo_url, licence`. No names of people are written; the observation's page names its observer.

A local run on small made-up files: serve a folder holding `observations.csv.gz`, `photos.csv.gz`, `taxa.csv.gz` and Natural Earth's `ne_50m_admin_0_countries.geojson`, then `S3_BASE=http://127.0.0.1:<port> NE_URL=http://127.0.0.1:<port>/ne_50m_admin_0_countries.geojson bash ci/world/world.sh`. It stops before checking photo addresses and before publishing.
