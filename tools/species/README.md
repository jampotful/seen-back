# tools/species

Unit tests (kind-of-eye rules): `python3 -m unittest discover -s tools/species -v` from the repository root, or `python3 -m unittest` inside this directory. A bare `python3 -m unittest` at the root finds nothing, because `tools/` is not a package.

Builders (`build_species.py`, `build_eval.py`, `build_train.py`) need api.gbif.org and run on a build machine through `.github/workflows/data.yml` and `traindata.yml`; each script's first lines say what it does. The evaluation build is pinned to `--end 2026-09-29` in `ci/data/run.sh`, so a rerun reads the same window.

`build_coco.py` builds the extra photo set for kinds the wildlife records lack (people, pets, livestock, nothing alive) from COCO 2017's annotations; it runs on a build machine through `.github/workflows/extradata.yml` (push to `run/extradata/<label>`), because the annotations come from images.cocodataset.org.

`check_train.py <manifest.csv>` checks a training manifest and `inat.json` independently of the builder (dates, overlap with the evaluation manifest, the promised row order, names); it needs no network.

The training manifest in use (`train/alachua-pre2025/` on `pub/data-alachua`) comes from the second route, `build_train_s3.py`, which reads iNaturalist's open-data files with no API in the way: `ci/data/train_s3.sh` streams `observations.csv.gz` and `photos.csv.gz` from the public bucket through awk filters (about ten minutes on a build machine; push to `run/traindatas3/<label>`), and the builder matches observations to the species list by name, or through the iNaturalist name that most of a key's evaluation photos sit under. `check_train_s3.py <manifest.csv>` checks that route's manifest (empty `gbif_id`, observation addresses ending in UUIDs, ranking by photo id).

`build_inat.py` writes `inat.json`: the evaluation observations looked up in iNaturalist's API for the species each sits under today, the taxonomy archive by exact name for the other keys, and iNaturalist's preferred English names (place Florida) where the name differs from GBIF's. Each entry also carries `n` (observations behind `share`) and `via` (`observations` or `name`; `share` is null for `name`). It runs on a build machine through the same workflow when `ci/data/job.txt` says `inat` (`ci/data/inat.sh`).

Publishing: every data job publishes INTO `pub/data-alachua` with `ci/data/merge_pub.sh`, which reads the branch, replaces only that job's own paths, and pushes with a lease on the commit it read (retrying if the branch moved), so the species list, the evaluation and training manifests and the extra sets never erase each other. `ci/put_branch.sh` replaces a whole branch and is not used for `pub/data-alachua` any more.
