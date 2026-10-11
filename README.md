# Seen Back

Seen Back is a web app in which you photograph something alive and your camera view changes toward what is known of how that creature sees: its field of view, where its sight is sharp, the shape of its pupil, its colours and the pace at which it takes in movement. A recognizer inside the page names the kind of eye and, when it is sure enough, the species, from the 5,911 species recorded in Alachua County, Florida, through 2024. Every meeting is kept in a record in the browser (`src/cam.r.js` keeps up to 300), and eyes you have met can be looked through again.

The app is served at https://jampotful.github.io/seen-back/ . The page there is build 8 (commit `8037aec`). "Seen Back" is a working title.

## What works today, and where it was checked

| Part | Checked on | Not yet checked on |
|---|---|---|
| The picture engine (WebGL 2) | The page's self-test on a phone with a Mali-G715 graphics chip (Chrome 154) and on an Intel MacBook Pro (Chrome 154, Safari 26.5); on build machines in Chromium, Firefox and WebKit on Linux and macOS, in Safari 26.6, and in Safari on iOS 26.5 in an iPhone 17 simulator | An iPhone; any other phone |
| The pocket recognizer (TinyCLIP 39M/16, 41 MB, answers every photo) | Chromium, Firefox and WebKit on Linux build machines, and Safari on a macOS build machine | Any phone |
| The larger model on the device (BioCLIP 2, 310 MB, downloaded once if the person agrees) | Headless Chromium in a development sandbox, and Node with ONNX Runtime Web on a Linux build machine | Any phone; any other browser |
| The record of meetings, and looking again | Headless Chromium with software graphics | Any phone; any other browser |
| Use with no network | Headless Chromium, Firefox and WebKit on a Linux build machine, against the live address | Any phone; the larger model with no network |

What stands behind each row:

- On 10 October the self-test passed 93 of 93 checks on the phone in Chrome and on the MacBook Pro in both browsers. In Ecosia on the same phone it passed 92 of 93, because the test sampled a clip before the clip's first frame was in place, and build 7 fixed that race (`docs/LOG.md`, 23:25 and 02:26).
- With the model that shipped in build 7, the pocket recognizer was ready in 2.1 to 6.4 seconds and answered a photo in 0.5 to 0.95 seconds in Chromium, WebKit and Safari on build machines, and in about 3.5 seconds in headless Firefox (`docs/LOG.md`, 03:40). How long it takes on a phone is unmeasured.
- The larger model answered 27 local test photos inside the page at 6.2 to 6.8 seconds each on one thread (`docs/LOG.md`, 03:55). In Node with onnxruntime-web 1.30.0 it took 4.9 seconds a photo on one thread of a build machine (laboratory run 25, recorded in `models/naturalist/manifest.json`). Whether a phone's browser will hold a 310 MB file and the memory to run it is unknown, and on iOS it is doubtful.
- Against the live address with build 8, after one visit, the service worker served the page with the network off in headless Chromium 141, Firefox 142 and WebKit 26.0, and the pocket recognizer named a kind for a photo in each (`runs/engines/34-live/summary.json` on the `ci` branch).
- Before build 8 went out, `test/rec/check_rec.js` (nineteen sections, against a stand-in model) and `test/check4.js` (the record, the word table, the viewer, the edges and the sweep of every kind of eye) passed in headless Chromium.
- Installing the page to a home screen has not been checked on any device.

## How accurate it is

On the 4,197 test photos of `data/eval/alachua-2025` (research-grade iNaturalist photos from Alachua County dated 2025 and 2026, none of them used to fit or tune a recognizer), the pocket recognizer in build 8 gets the kind of eye right for 87.3% (86.3 to 88.3), names a species for 14.2% and is right for 92.0% (89.6 to 94.0) of the names it gives. Its rows, which `docs/EVAL.md` calls a stand-in, were fitted on two thirds of the evaluation set's `val` photos and on COCO photos, and on 1,240 COCO test photos of people, cats, dogs, grazing animals and rooms (`data/extra/coco-kinds`) it gets the kind right for 98.2% (97.3 to 98.8), a figure that says nothing about a hand, a toy animal, a painting of a bird or a screen showing a heron. The larger model names a species for 84.6% (83.4 to 85.6) of the test photos and is right for 98.1% (97.6 to 98.5) of those names, scored from the original model's vectors; on 320 test photos the int8 file that the page runs put the right species first for 93.75%, against 94.06% for the original. Research-grade photos are ones that people on iNaturalist had already agreed on, often with iNaturalist's own suggestion in front of them, so a photo taken in passing will do worse, and every number holds for one county and its own list of species. No comparison with iNaturalist's own model is possible, because its computer-vision route needs an application or user token and is left out of its published documentation, and the accuracy it publishes was measured on other photos by rules its posts do not fully state (`docs/eval/others.md`).

Each figure is from `docs/EVAL.md`, where `tools/eval/shipped.py` reads a slot's own files and sends every photo through `tools/fusion/fuse.py`, the reference for the page's arithmetic. The brackets hold 95% bootstrap intervals over photos.

## Build it and run the checks

```
python3 -I build.py                                  # writes index.html, sw.js, selftest.js and dist/
python3 -I -m http.server 8765 --bind 127.0.0.1      # serve the repository root, then open http://127.0.0.1:8765/
NODE_PATH=<where playwright lives> node test/check4.js record     # also lex, viewer, edge, sweep, film
node test/rec/serve.js 8782 &                        # the recognizer's checks have their own server
NODE_PATH=<where playwright lives> node test/rec/check_rec.js     # every section, or name the sections to run
```

A page may use a live camera only at an `https` address or on `localhost`. Opened as a file on a phone, it falls back to a photo of who you met and a clip of your own view. The page runs its self-test when its address carries `?selftest=1`. The checks on other browsers and on macOS run on GitHub's build machines, as `docs/HANDOFF.md` describes.

## Where things are

- `src/` holds the parts of the page, and `build.py` joins them into `index.html`, `sw.js`, `selftest.js` and `dist/seen-back.artifact.html`.
- `models/pocket/` and `models/naturalist/` hold the two recognizers' files. The larger model's 310 MB encoder is fetched in four parts from a pinned commit of this repository.
- `docs/PLAN.md` is the plan and `docs/LOG.md` the running log. `docs/CONTRACTS.md` says how the parts fit together, `docs/EVAL.md` holds the evaluation, `docs/SOURCES.md` the sources behind every graded line about an animal's sight, `docs/LICENCES.md` the licences, and `docs/HANDOFF.md` what someone carrying the work on needs.
- `data/` holds the species list and the manifests of the evaluation, training and extra photos, each with a `SUMMARY.md`. `service/` holds a species service that is built and has not been deployed.

## What is measured and what is invented

Each line the app shows about an animal's sight carries a grade: measured in this animal, measured in a relative or a wider group, a guess, or left out. `docs/SOURCES.md` lists the source for every measured line and names the conventions that are this project's own invention, among them sharpness drawn against the viewer's own eye, a faster eye suggested by slowing the picture, depth guessed from height in the frame, and ultraviolet drawn as violet or blue.

## Licences

Every model, data set, library and font that ships or was used is listed in `docs/LICENCES.md`, with its licence and where the licence was read. The typeface is Instrument Serif, under the SIL Open Font License 1.1 (`fonts/OFL-Instrument-Serif.txt`). No licence has been chosen for this code yet.
