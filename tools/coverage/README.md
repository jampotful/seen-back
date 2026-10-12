# tools/coverage

Scripts behind `docs/COVERAGE.md`: how far the app's two recognizers reach beyond the sixteen groups it has views for and beyond the one county its species list holds.

- `split_other.py` fits the pocket model's group head with today's seventeen labels and again with `other` split into proposed new groups, and scores both on the same test photos. It needs no network: give it a directory holding the Alachua manifests (from `pub/data-alachua`) and TinyCLIP 39M/16's published vectors (from `pub/lab-tinyclip-39m-16`), laid out as its first lines say.
- `ci/coverage/counts.sh` streams iNaturalist's open-data `observations.csv.gz` once and counts research-grade and casual observations per taxon, worldwide and in regions round Gainesville. `lists.py` turns the counts into species lists of growing size. `text.py` makes BioCLIP 2's text rows for every species on them, in shards. `score.py` scores the Alachua test photos against each list. All four run on build machines through `.github/workflows/coverage.yml` (push to `run/coverage/<label>`).
- `score.py` reproduces the published figure for the larger model on the Alachua list (top-1 with no prior, 90.4% on the test photos) when it is given the live rows, which is how it was checked.
