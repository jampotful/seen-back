# Track A1: the pocket model's group head

Read this whole file, then `docs/COVERAGE.md` (the pass marks are in "Pass marks, set before the runs"), `docs/HANDOFF.md` and `docs/CONTRACTS.md`.

## The aim

The pocket model should name, as a group, every one of the nineteen new groups that it can name well enough (at least 75% of a group's photos named and at least 75% right when called), keep the sixteen old kinds as good as today on Alachua and on world photos (the 95% interval of the paired difference stays above −2 points), keep COCO (people, pets, livestock, empty rooms) within 1 point, and give a view to under 10% of the photos in `other`. A group that fails stays in `other`. The owner approved a larger image encoder if it helps, with the condition that the app stays fast.

## Where things are

- Branch `agent/world-head`: `tools/world/head.py` (fitting, the page's rule in vectors, the fold, the settle step, the reports), `ci/world/head.sh` and `.github/workflows/worldhead.yml` (a push to `run/worldhead/<label>` runs it on a build machine and publishes to `pub/heads-world-<label>`; results come back to the branch `ci` as `runs/worldhead/<n>-<label>`), `tools/world/encoders.py` with `ci/world/encoders.sh` and `.github/workflows/worldenc.yml` (the encoder comparison), and the page's time-zone rule (`zoneNear` in `src/cam.c2.js`, `known()` in `src/cam.rec.js`), which is not on `main`.
- `tools/world/exp.py` and `tools/world/EXPERIMENTS.md` on the same branch: the trials on tuning photos and their results.
- The vectors: `pub/lab-tinyclip-39m-16` and `pub/lab-bioclip-b16` (`images/<set>.f16.npy` with `.ids.json`, and `wasm-int8-per-channel` variants), made by `tools/lab` and `ci/lab` (configs in `ci/lab/runs/`; runs 42 to 45 made the B/16 sets, see `runs/lab/4*` on `ci`).

## Results so far

| | Head run 2 | Head run 3 | Merge trial (tuning photos only) |
|---|---|---|---|
| Groups carried | 19 | 3 (primate, whale, bat) | 3 of a 19-row head |
| Groups passing | 5 | 3 of 3 | 3 |
| Old kinds, world photos | +5.6 points | +2.83 (+1.67 to +3.98) | +3.9 |
| Old kinds, Alachua photos | −2.87 (−3.64 to −2.12), fails | −5.58 (−6.54 to −4.68), fails | −0.36 |
| COCO | passes | passes | +0.39 alone, +0.55 fused |
| `other` given a view | 25%, fails | 10.18%, fails | 10.8% |

The merge trial's recipe: no reweighting by count (power 0), Alachua rows weighted 3 and COCO rows 10 in the fit, per-group bias offsets calibrated on world tuning photos (coordinate ascent on the sum over groups of the smaller of named and right-when-called), the probability of every failing group merged into `other` with no refit, then the grid of `t_kind` in {0.5, 1, 2} and `w_kind` in {0.5, 0.7, 0.9, 1.0} for Alachua with COCO within 1 point; best at `t_kind` 1.0, `w_kind` 0.7.

The encoder comparison (`runs/worldenc/1`): TinyCLIP 39M/16, 0.710 right on test photos, 4 groups pass after the fold; BioCLIP B/16 (86.2M image parameters, int8 file 89.8 MB), 0.785 right, 10 pass after the fold (slime, spider, jumper, salamander, scorpion, tick, primate, whale, bat, flying fox).

## What to do

1. Port the merge recipe into `head.py` as options, keeping the test photos unread until the recipe and settings are fixed on tuning photos, then read them once (and a second time only if a carried group fails on test and is put back, keeping both readings, as `head.py` already does).
2. Run it on a build machine for TinyCLIP, and report it against every pass mark.
3. Make `head.py` take the model as a setting and fit the same recipe on the B/16 vectors. Measure B/16's time per photo in headless Chromium with the WASM build (one thread and four), against TinyCLIP's, using the lab's int8 file.
4. If files over 100 MB stop a publish (GitHub refuses them; lab run 39 failed this way), split arrays into parts in the publish step.
5. If a head passes every mark, prepare it on the branch `agent/head-ship` from `main`: the slot files, the time-zone rule and `known()` from `agent/world-head`, `tools/fusion/fuse.py` and the page agreeing (`tools/fusion/parity.py`), and `test/rec/check_rec.js` passing. Do not merge to `main`; the app's thread ships it.

## Your machine and your branches

The cloud machine can be replaced without warning, which deletes everything on it. Clone with `git clone --depth 1 https://github.com/jampotful/seen-back /home/claude/seen-back` (allow ten minutes) and fetch the branches you need with bounded fetches (`git fetch --depth 50 origin agent/world-head`). Push your work at least every 30 minutes. Commit as `git -c user.name=Claude -c user.email=noreply@anthropic.com commit` with your session's attribution lines. Never push to `main`. Build-machine runs take minutes to hours; while one runs, prepare the next step.

## Your report

At most 400 words: the table of pass marks for each model and recipe, your recommendation, the speed of B/16 against TinyCLIP, and the branches and commits you pushed.
