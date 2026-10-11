# tools/species

Unit tests (kind-of-eye rules): `python3 -m unittest discover -s tools/species -v` from the repository root, or `python3 -m unittest` inside this directory. A bare `python3 -m unittest` at the root finds nothing, because `tools/` is not a package.

Builders (`build_species.py`, `build_eval.py`, `build_train.py`) need api.gbif.org and run on a build machine through `.github/workflows/data.yml` and `traindata.yml`; each script's first lines say what it does. The evaluation build is pinned to `--end 2026-09-29` in `ci/data/run.sh`, so a rerun reads the same window.
