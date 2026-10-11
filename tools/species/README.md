# tools/species

Unit tests (kind-of-eye rules): `python3 -m unittest discover -s tools/species -v` from the repository root, or `python3 -m unittest` inside this directory. A bare `python3 -m unittest` at the root finds nothing, because `tools/` is not a package.

Builders (`build_species.py`, `build_eval.py`, `build_train.py`) need api.gbif.org and run on a build machine through `.github/workflows/data.yml` and `traindata.yml`; each script's first lines say what it does. The evaluation build is pinned to `--end 2026-09-29` in `ci/data/run.sh`, so a rerun reads the same window.

`build_coco.py` builds the extra photo set for kinds the wildlife records lack (people, pets, livestock, nothing alive) from COCO 2017's annotations; it runs on a build machine through `.github/workflows/extradata.yml` (push to `run/extradata/<label>`), because the annotations come from images.cocodataset.org.

`check_train.py <manifest.csv>` checks a training manifest and `inat.json` independently of the builder (dates, overlap with the evaluation manifest, the promised row order, names); it needs no network.

Publishing: every data job publishes INTO `pub/data-alachua` with `ci/data/merge_pub.sh`, which reads the branch, replaces only that job's own paths, and pushes with a lease on the commit it read (retrying if the branch moved), so the species list, the evaluation and training manifests and the extra sets never erase each other. `ci/put_branch.sh` replaces a whole branch and is not used for `pub/data-alachua` any more.
