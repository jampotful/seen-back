# Handoff

This file is for whoever carries this work on next, a person or an assistant. It describes the repository as it stood at build 8 (commit `8037aec`) on 11 October 2026. `docs/CONTRACTS.md` holds the formats and rules in full, and `docs/LOG.md` says what happened and when; read both before changing anything.

Private working notes are kept outside this repository. An assistant working for the owner will find them in the owner's Claude project, in the document `claude/seen-back-working-notes.md`.

## The map

| Where | What it holds |
|---|---|
| `src/` | The parts of the page: the eye models and their graded lines (`cam.a.js`), the picture engine (`cam.b.js`), the app's state and flow (`cam.c1.js`, `cam.c2.js`), the record and the word table for typed names (`cam.r.js`), the recognizers in the page (`cam.rec.js`), the self-test (`cam.selftest.js`), the markup (`cam.head.html`), the service worker (`sw.template.js`), and one town's sixty most recorded species (`cam.g60.js`) |
| `build.py` | Joins `src/` into `index.html`, `sw.js`, `selftest.js` and `dist/seen-back.artifact.html`. These built files are committed, because the site serves them as they are |
| `vendor/` | ONNX Runtime Web 1.30.0 (`vendor/ort/`) and the worker that runs a recognizer (`rec-worker.js`) |
| `models/pocket/`, `models/naturalist/` | The two recognizer slots the page loads: manifest, kind rows, species rows and table; the pocket slot also holds its 41 MB encoder, and the larger model's encoder is fetched in parts from a pinned commit |
| `labels/kinds.json` | The phrases for the sixteen kinds of eye and for `none` |
| `data/` | The species list (`regions/us-fl-alachua/`), and the manifests and summaries of the evaluation photos (`eval/alachua-2025/`), the training photos (`train/alachua-pre2025/`, whose manifest is published on `pub/data-alachua` only) and the extra photos from COCO (`extra/coco-kinds/`) |
| `tools/species/` | The scripts that build the species list and the photo manifests, and the rule that maps a species to its kind of eye (`eyes.py`) |
| `tools/lab/` | The model laboratory: label rows, image vectors and browser-ready ONNX files for each model |
| `tools/eval/` | The evaluation, from fetching the published vectors to writing `docs/EVAL.md` |
| `tools/fusion/` | The page's arithmetic written in Python (`fuse.py`) and the check that the page agrees with it (`parity.py`) |
| `service/` | The species service (BioCLIP 2 behind a small Gradio app), built and undeployed |
| `test/` | The browser checks: `check4.js` (the record, the word table, the viewer, the edges, the sweep of every kind of eye), `rec/check_rec.js` (the recognizers, against a stand-in model), and `engines/` (runs on the build machines) |
| `ci/`, `.github/workflows/` | The build machines' scripts and workflows |
| `docs/` | The plan, the log, the contracts, the evaluation, the sources, the licences, and this file |

## Building and checking

```
python3 -I build.py                                  # index.html, sw.js, selftest.js, dist/
python3 -I -m http.server 8765 --bind 127.0.0.1      # serve the repository root
NODE_PATH=<playwright> node test/check4.js lex|record|viewer|edge|sweep|film
node test/rec/serve.js 8782 &
NODE_PATH=<playwright> node test/rec/check_rec.js [section ...]   # SLOW=3 on a busy machine
```

- `main` is served at https://jampotful.github.io/seen-back/ about a minute after every push, so it receives only work that builds and passes its checks.
- Headless Chromium needs `--use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader --ignore-gpu-blocklist` where there is no graphics chip; the checks pass these already. Software graphics are slow, so the checks ask for a small picture with `?side=420`.
- On a local address, `?big=off` switches the larger model off and `?big=<slot>` points it at another slot; a public address accepts neither (`docs/CONTRACTS.md`).
- The page has two wrappers. `index.html` is the standalone app. `dist/seen-back.artifact.html` is for Claude's artifact viewer, which allows fonts only from Google Fonts, allows no network calls except to itself, and refuses the camera. Inside that viewer the page can ask Claude to name a photo and keeps the record in the viewer's private store.
- Nothing is called done that has only run in software graphics. Say what was run, and on what.

## Build machines

The working sandbox reaches little of the internet, so anything that needs the open network runs on GitHub's build machines.

- **Start a run** by pushing a commit to a branch named `run/<workflow>/<label>`, for example `git push -f origin HEAD:refs/heads/run/engines/dev`. The workflow file is read from the pushed commit. A newer push to the same branch cancels the run in progress.
- **Read the results** on the `ci` branch, under `runs/<name>/<run number>[-shard]/`, with a line for each result in `INDEX.txt`. `bash ci/wait.sh <commit> [lines expected] [seconds]` waits for them; it exits 3 when the wait runs out, and can be run again. The logs on github.com cannot be read without signing in, so every job writes its own log into the directory it returns.
- **The laboratory** reads its orders from `ci/lab/runs/<label>.json` when that file exists in the pushed commit, and from `ci/lab/run.json` only otherwise.
- **Reading a public page**: list its address in `ci/fetch/list.txt` and push to `run/fetch/<label>`; the text comes back under `runs/fetch/`.
- **Limits**: 20 jobs at once, 5 of them on macOS; six hours a job; under 25 MB returned to `ci` by one job; under 95 MB for one file in git.
- The engines workflow runs the checks and the self-test on Linux (Chromium, Firefox, WebKit) and on macOS (WebKit, Safari, Safari in the iPhone simulator); a branch named `run/engines/live-<anything>` checks only the live address (`.github/workflows/engines.yml`).

## Published data and models

- A branch named `pub/...` holds one published thing and keeps no history: `bash ci/put_branch.sh <branch> <dir>` replaces it whole, and `bash ci/data/merge_pub.sh` adds to a `pub/data-*` branch without removing what other jobs put there.
- `pub/data-alachua` holds the manifests of the evaluation, training and extra photos.
- `pub/lab-<model>` holds one model's files: `card.json`, label rows under `text/`, image vectors under `images/`, and ONNX files under `onnx/` for a model that is a candidate for the page.
- `pub/model-bioclip2-l14` holds the larger model's int8 file in parts, with `parts.json`.
- `pub/heads-<fitting set>-<model>` holds a slot exported by the evaluation, in the layout of `models/<slot>/`. The heads in build 8 came from `pub/heads-val-tinyclip-39m-16` and `pub/heads-naturalist-bioclip2-l14`; heads fitted on the training photos are on `pub/heads-alachua-pre2025-tinyclip-39m-16` and `-8m-16` and are not in build 8.
- A branch named `pin/<what>-<commit>` keeps a commit alive that something outside depends on. `pin/model-bioclip2-l14-462ecdc` keeps the commit from which every browser fetches the larger model's four parts (`raw.githubusercontent.com/jampotful/seen-back/462ecdc.../vision.int8.onnx.part00` to `part03`). Leave it in place: `pub/` branches keep no history, and this branch is what keeps that commit (`docs/CONTRACTS.md`).
- Photos themselves are never committed or republished. Manifests carry each photo's address and licence, and the build machines download photos when a run needs them.

## How a slot is assembled and shipped

1. The laboratory computes a model's label rows, image vectors and ONNX files and publishes them on `pub/lab-<model>`.
2. The evaluation fits heads and chooses settings on `val` (`tools/eval/study2.py`), writes a slot in the layout of `models/<slot>/` (`tools/eval/export_heads.py`), and sets `name_at`, `offer_at` and `kind_at` while scoring the slot as the page would, through `tools/fusion/fuse.py` (`tools/eval/shipped.py`). For the larger model, `tools/eval/naturalist.py` writes the head files and lists the encoder's parts from the laboratory's `parts.json` in the manifest's `vision` block. A build-machine run publishes the slots as `pub/heads-<fitting set>-<model>`.
3. To ship a slot, copy its files into `models/<slot>/`. The pocket slot's encoder comes from the branch its manifest names in `vision.from`. Run `python3 -I build.py`, then `test/rec/check_rec.js` and `test/check4.js`, and merge to `main`.
4. In build 8 the page keeps a slot's files under an address made from a fingerprint of the slot's manifest (`src/cam.rec.js`), so any change to the manifest, new heads or a new threshold, makes every phone download all of that slot's files again, the 41 MB encoder among them.
5. A manifest that names a rule or a field the page does not know is refused, and the person is asked to type the kind (`docs/CONTRACTS.md`).

## Rerunning the evaluation

```
bash tools/eval/run.sh ROOT sentences          # slots made from sentence rows
bash tools/eval/run.sh ROOT val                # the stand-in for trained heads, as in build 8
bash tools/eval/run.sh ROOT alachua-pre2025    # heads fitted on the training photos
```

The steps one at a time, and what each writes, are listed at the end of `docs/EVAL.md`. Pushing to `run/eval/<label>` reruns everything on a clean build machine, returns the files and a comparison with the committed numbers under `runs/eval/` on `ci`, and publishes the exported slots. `tools/eval/compare.py` says whether two runs give the same numbers.

## Secrets

One secret exists, by name only: `HF_TOKEN`, a Hugging Face token with write access, which workflows read as `${{ secrets.HF_TOKEN }}`. Never print it, and never write it to a file that a job returns. Secrets never enter the repository, and `.gitignore` keeps out `hf-token.txt`, `*.token` and `.env`.

## Rules the work is held to

- A claim about an animal ships with a grade and a source, or it is marked as a guess.
- A number in a document comes from a script in this repository, and the document says which.
- The repository is public. Private notes, names of collaborators, photographers' names, e-mail addresses and plans for approaching other organizations stay out of it.

## Waiting on the owner

- The rule for which photos heads may be fitted on, which the coordinator set on 11 October pending the owner's decision (`docs/LICENCES.md`).
- A licence for this project's code; none has been chosen.
- The rule of the finding game (`docs/PLAN.md`, Phase 5).
- A run of the page on an iPhone, and of the larger model on a phone.
- A home for the species service. A free Hugging Face account can host it on shared graphics cards from about 10 November, when the account is thirty days old (`docs/LOG.md`, 11 October, 00:52).
