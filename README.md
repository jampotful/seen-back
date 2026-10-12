# World photos

Lists of iNaturalist photos for fitting, tuning and testing the base app's group head on the 33 groups of
docs/COVERAGE.md, and for the full database's world test. Made by tools/world/select.py through ci/world/world.sh
from iNaturalist's open-data snapshot of Sun, 27 Sep 2026 16:10:27 GMT. Each row gives the observation's address,
the photo's address and the photo's licence; the photographer is named on the observation's page.

- fit.csv, tune.csv, test.csv, casual.csv, species.csv: the sets (SUMMARY.md says what each holds).
- records-by-group.tsv: research-grade (F through 2024, E from 2025) and casual (C) observations by group and continent.
- lab/world-fit, lab/world-eval, lab/world-species: the same rows as manifests for tools/lab (an id and a split added).
- continents-0.5deg.tsv: the continent of each half-degree cell, from Natural Earth's countries at 1:50 million
  (public domain, https://www.naturalearthdata.com), as tools/world/continents.py makes it.
