# Handoff

This file is for whoever carries this work on next, a person or an assistant. It describes the repository as it stood at build 9 (commit `013bb77`) on 11 October 2026; the first section says where the night's work stopped, at build 10. `docs/CONTRACTS.md` holds the formats and rules in full, and `docs/LOG.md` says what happened and when; read both before changing anything.

Private working notes are kept outside this repository. An assistant working for the owner will find them in the owner's Claude project, in the document `claude/seen-back-working-notes.md`.

## Where the night of 10 to 11 October stopped

`main` is at build 10. Three pieces of work are finished and deliberately not in the page. Each is the next thing to pick up.

- **The lighter form of the larger model.** The branch `agent/rec-b` (commit `39136ac`) lets the page load the model as a 2 MB graph file with its weights beside it as a data file (`pub/model-bioclip2-l14-b` at `add8cf58`, kept alive by `pin/model-bioclip2-l14-b-add8cf5`). In headless Chromium the answers are identical to the live form's and the renderer's peak is a quarter lower. To ship it: merge the branch, raise `BUILD` (the worker's address carries it), run `test/rec/check_rec.js` and `test/rec/check_ext.js`, and replace `models/naturalist/manifest.json` with the manifest the branch's author left (its `vision` block names the graph and the weights' parts). A trial on real engines (`run/engines/bigb-a`, commit `2fecb34`, which serves that branch's own page on build machines; results under `runs/engines/53-big-*` on `ci`) showed the new form correct in Safari and WebKit on macOS and no lighter there: the largest process peaks at about 2,045 MiB with either form. So merging it helps Chromium, and an iPhone needs the cause of WebKit's memory found first (`docs/ENGINES.md`).
- **The WebKit fix.** `ci/engines/patches/webkit-resume.patch` deletes an address before every `put` to it. It passes the resume probe in WebKit and Chromium. It touches the same functions as the branch above, so apply it after that merge, and run the recognizer's full checks with it.
- **The Android file.** A push of `main` to `run/native/pub-final` (any label beginning with `pub`) rebuilds `seen-back-debug.apk` from that commit and replaces the branch `pub/app-android`. Each file is signed with a new throwaway key, so a phone must remove the older app before installing a newer file.

Known and open: in Firefox the larger model is too slow to answer within the page's time limit (`docs/ENGINES.md`); the pocket model can give an odd photo of objects a confident wrong answer (a photo of coins was named as a fungus), which wants a wider set of photos with nothing alive in them; cattle, dogs, sheep, most houseplants and common garden flowers are missing from the species list; the name a small model gave stands when the larger model is sure of the kind and unsure of the species.

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
| `tools/audit/` | An independent recomputation of the headline numbers, with its results in `tools/audit/results/` and its findings in `docs/eval/audit.md` |
| `service/` | The species service (BioCLIP 2 behind a small Gradio app), built and undeployed |
| `native/` | Two thin app shells around the built page, an Android WebView app and an iPhone WKWebView app, run on build machines as an experiment; `native/README.md` says what they showed |
| `test/` | The browser checks: `check4.js` (the record, the word table, the viewer, the edges, the sweep of every kind of eye), `rec/check_rec.js` (the recognizers, against a stand-in model), and `engines/` (runs on the build machines) |
| `ci/`, `.github/workflows/` | The build machines' scripts and workflows |
| `docs/` | The plan, the log, the contracts, the evaluation (`EVAL.md`, `eval/`) and its audit (`eval/audit.md`), what ran on which engine (`ENGINES.md`), the sources, the licences, and this file |

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
- **Limits**: at most 20 jobs run at once, 5 of them on macOS; a job may run six hours; one job returns under 25 MB to `ci`; and a file in git stays under 95 MB.
- The engines workflow runs the checks and the self-test on Linux (Chromium, Firefox, WebKit) and on macOS (WebKit, Safari, Safari in the iPhone simulator); a branch named `run/engines/live-<anything>` checks only the live address (`.github/workflows/engines.yml`). What it found is in `docs/ENGINES.md`.
- The native workflow (`.github/workflows/native.yml`) starts on a push to `run/native/<label>`. A label starting with `android` runs only the Android job, one starting with `ios` only the iOS job, and one starting with `ios-big` runs the larger model's probe in the iPhone shell; other labels run both jobs. The Android job builds the page, packs it into a debug APK, and runs the self-test, the camera and the larger model in an Android 14 emulator; the iOS job compiles the shell and runs the self-test in an iPhone 17 simulator. Results come back under `runs/native/<run number>-android/` and `runs/native/<run number>-ios/` on `ci`, and `native/README.md` gives the commands for building either shell by hand.

## Published data and models

- A branch named `pub/...` holds one published thing and keeps no history: `bash ci/put_branch.sh <branch> <dir>` replaces it whole, and `bash ci/data/merge_pub.sh` adds to a `pub/data-*` branch without removing what other jobs put there.
- `pub/data-alachua` holds the manifests of the evaluation, training and extra photos.
- `pub/lab-<model>` holds one model's files: `card.json`, label rows under `text/`, image vectors under `images/`, and ONNX files under `onnx/` for a model that is a candidate for the page.
- `pub/model-bioclip2-l14` holds the larger model's int8 file in parts, with `parts.json`. `pub/model-bioclip2-l14-b` holds the same model as a 2 MB graph file with its weights beside it as a data file in four parts, and its `parts.json` gives every checksum and the call that loads it; the page does not use that form yet.
- `pub/heads-<fitting set>-<model>` holds a slot exported by the evaluation, in the layout of `models/<slot>/`. The pocket heads in build 9 came from `pub/heads-pocket-v3` (commit `f0c2544`), which also holds `fitted_on.csv`, the list of the photos they were fitted on, and `measured.json`; the larger model's came from `pub/heads-naturalist-bioclip2-l14`. The pocket heads of build 8 came from `pub/heads-val-tinyclip-39m-16`.
- A branch named `pin/<what>-<commit>` keeps a commit alive that something outside depends on, because `pub/` branches keep no history (`docs/CONTRACTS.md`). Three are in use, and each must stay in place. `pin/model-bioclip2-l14-462ecdc` keeps the commit from which every browser fetches the larger model's four parts (`raw.githubusercontent.com/jampotful/seen-back/462ecdc.../vision.int8.onnx.part00` to `part03`). `pin/heads-pocket-v3-f0c2544` keeps the commit that holds `fitted_on.csv`, which the page's About block links to. `pin/model-bioclip2-l14-b-add8cf5` keeps the external-data form of the larger model.
- Photos themselves are never committed or republished. Manifests carry each photo's address and licence, and the build machines download photos when a run needs them.

## How a slot is assembled and shipped

1. The laboratory computes a model's label rows, image vectors and ONNX files and publishes them on `pub/lab-<model>`.
2. The evaluation fits heads and chooses settings on `val` (`tools/eval/study2.py`), writes a slot in the layout of `models/<slot>/` (`tools/eval/export_heads.py`), and sets `name_at`, `offer_at` and `kind_at` while scoring the slot as the page would, through `tools/fusion/fuse.py` (`tools/eval/shipped.py`). For the larger model, `tools/eval/naturalist.py` writes the head files and lists the encoder's parts from the laboratory's `parts.json` in the manifest's `vision` block. A build-machine run publishes the slots as `pub/heads-<fitting set>-<model>`.
3. To ship a slot, copy its files into `models/<slot>/`. For pocket v3, `tools/eval/decide_v3.py` applied a rule written before the candidate was measured (`docs/eval/decision-pocket-v3.json`), and `tools/eval/pocket_v3.py` assembled the files that replace the heads in `models/pocket/` and the files published on `pub/heads-pocket-v3`. On `main`, `models/pocket/` holds no copy of `fitted_on.csv`; its manifest gives the list's address on the pinned commit. The pocket slot's encoder comes from the branch its manifest names in `vision.from`. Run `python3 -I build.py`, then `test/rec/check_rec.js` and `test/check4.js`, and merge to `main`.
4. The page keeps a slot's files under an address made from a fingerprint of the slot's manifest (`src/cam.rec.js`), so any change to the manifest, new heads or a new threshold, makes every phone download that slot's files again. From build 9 the page keeps an encoder whose checksum the manifest gives under that checksum, so new heads no longer cost a second download of the pocket's 41 MB encoder.
5. A manifest that names a rule or a field the page does not know is refused, and the person is asked to type the kind (`docs/CONTRACTS.md`).

## Rerunning the evaluation

```
bash tools/eval/run.sh ROOT sentences          # slots made from sentence rows
bash tools/eval/run.sh ROOT val                # the stand-in for trained heads, as in build 8
bash tools/eval/run.sh ROOT alachua-pre2025    # heads fitted on the training photos
```

The steps one at a time, and what each writes, are listed at the end of `docs/EVAL.md`. Pushing to `run/eval/<label>` reruns everything on a clean build machine, returns the files and a comparison with the committed numbers under `runs/eval/` on `ci`, and publishes the exported slots. `tools/eval/compare.py` says whether two runs give the same numbers.

Pushing to `run/eval/licence<anything>` reruns only the heads fitted under the licence rule, the pocket v3 decision, the last check of the assembled files and the pets and livestock check, and compares them with the committed files; it publishes nothing (`ci/eval/run.sh`).

## Rechecking the numbers: the audit

`tools/audit/` recomputes the headline numbers of the evaluation with code of its own, which imports nothing from `tools/eval/` or `tools/fusion/`. Fill a directory `ROOT` from the `pub/*` branches as the table in `tools/audit/README.md` lays out, then run, from a checkout of this repository:

```
nice -n 10 env OMP_NUM_THREADS=1 python3 -I tools/audit/recompute.py ROOT . tools/audit/results/recompute.json
nice -n 10 env OMP_NUM_THREADS=1 python3 -I tools/audit/softspots.py ROOT . tools/audit/results/softspots.json
```

On two shared cores the first took about a minute and the second about forty seconds (`tools/audit/README.md`). The comparison of the shipped int8 file's browser vectors is a short script in the last block of the same README. `docs/eval/audit.md` lists what disagreed and why, and the soft spots it measured, among them near-copies between the test and `val` photos, names for species with few local records, a bar chosen after the test outcomes of three bars were seen, and what the species list lacks.

## Secrets

One secret exists, by name only: `HF_TOKEN`, a Hugging Face token with write access, which workflows read as `${{ secrets.HF_TOKEN }}`. Never print it, and never write it to a file that a job returns. Secrets never enter the repository, and `.gitignore` keeps out `hf-token.txt`, `*.token` and `.env`.

## Rules the work is held to

- A claim about an animal ships with a grade and a source, or it is marked as a guess.
- A number in a document comes from a script in this repository, and the document says which.
- The repository is public. Private notes, names of collaborators, photographers' names, e-mail addresses and plans for approaching other organizations stay out of it.

## Waiting on the owner

- The owner has yet to decide on the rule for which photos heads may be fitted on, which the coordinator set on 11 October and under which the heads of build 9 were fitted (`docs/LICENCES.md`).
- No licence has been chosen for this project's code.
- The rule of the finding game awaits a decision (`docs/PLAN.md`, Phase 5).
- The build machines have no phone, so a real phone waits on the owner. The page has yet to run on an iPhone, and the larger model on any phone. `native/README.md` gives the steps for putting the iPhone shell on the owner's own iPhone from Xcode with a free Apple ID; its provisioning profiles expire seven days after they are issued, so the app has to be installed again every week.
- The species service needs a home. A free Hugging Face account can host it on shared graphics cards from about 10 November, when the account is thirty days old (`docs/LOG.md`, 11 October, 00:52).
- Whether to take the app shells toward the stores is the owner's call. A Play Console account costs US$25 once, and a personal account created after 13 November 2023 must first run a closed test with at least 12 testers for at least 14 days. The Apple Developer Program costs 99 USD a year (`native/README.md`).
