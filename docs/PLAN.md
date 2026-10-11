# Plan

The aim is one app that works by itself on an iPhone, an Android phone and a computer: it recognizes what you photographed, changes your camera toward that creature's sight, and keeps a record of who you have met.

This file was brought up to date on 11 October 2026, when build 8 (commit `8037aec`) was live. A ticked line names its evidence: a commit, a file, or a run whose results are on the `ci` branch.

## Standards every phase is held to

- **Checked, or labelled as unchecked.** Every claim the app makes about an animal carries a grade and a source. Every number in an evaluation comes from a script in this repository that anyone can rerun.
- **Tested on real engines.** A build runs in Chromium and WebKit, on a phone-sized screen and a desktop one, before it is called done.
- **Private by default.** Photos stay on the device. Anything that sends a photo elsewhere says so first and can be turned off.
- **Usable with no signal.** The app opens offline, and recognition of the kind of creature works offline.
- **Licences recorded.** Every model, dataset and font is listed with its licence before it ships.

## Phase 1: an address, and an app that installs

- [x] The page stands alone and serves its typeface from this site. *(build 5, commit `8f22787`; `fonts/`)*
- [x] The page has a web app manifest and icons, and a service worker keeps the app shell and the large files. *(`manifest.webmanifest`, `icons/`, `src/sw.template.js`; on the live address the worker controlled the second visit in Chromium, Firefox and WebKit, `runs/engines/34-live/summary.json`)*
- [x] The page is served at an https address, https://jampotful.github.io/seen-back/ . *(`runs/engines/34-live/summary.json` read build 8 there)*
- [x] The self-test passed on desktop Chrome and desktop Safari. *(93 of 93 on an Intel MacBook Pro in Chrome 154 and Safari 26.5, `docs/LOG.md`, 10 October, 23:25)*
- [x] The self-test passed in Chrome on a phone. *(93 of 93 in Chrome 154 on a phone with a Mali-G715 graphics chip, the same entry; the log does not name the phone's operating system)*
- [ ] The self-test has yet to run in Safari on an iPhone. It has run only in Safari on iOS 26.5 in an iPhone 17 simulator on a build machine (`docs/LOG.md`, 11 October).

Still open: the page has not run on an iPhone, and installing it to a home screen has not been checked on any device.

## Phase 2: recognition on the device (the pocket recognizer)

Goal: the page itself tells a cat from a heron from an oak, with no network, in under a second on a recent phone.

- [x] Choose the image encoder. TinyCLIP 39M/16 (MIT licence, int8, 41.0 MB) ships in `models/pocket/` (commit `987c09b`, then build 8). MobileCLIP will not ship, because its licence is for research only (`docs/LICENCES.md`). Applied to slots made from sentences, the rule written beforehand in `tools/eval/decide.py` gave a tie that falls to TinyCLIP 8M/16, an answer `docs/EVAL.md` calls provisional. On the stand-in slots with kind rows fitted on photos, TinyCLIP 39M/16 was ahead by 4.8 points (4.1 to 5.5) on the kind of eye, a second look that `docs/EVAL.md` counts as evidence outside the rule.
- [x] Build the label set: phrases for the sixteen kinds of eye and for `none` (`labels/kinds.json`), and rows for the 5,911 local species (`models/pocket/species.json`).
- [x] Compute the label rows once, offline, so that the phone downloads the image encoder and the row files and computes no text. *(`tools/eval/export_heads.py`; `models/pocket/kinds.f16.bin`, `species.f16.bin`, `species.bias.f32.bin`)*
- [x] Run it in the browser with ONNX Runtime Web, with the files served from this site and kept by the service worker. *(build 6, commit `68dc1cd`; `vendor/ort/`; the kept files are listed in `runs/engines/34-live/summary.json`)*
- [x] Map a recognized species to its kind of eye through taxonomy. *(`tools/species/eyes.py`, the `eyes` column of `data/regions/us-fl-alachua/species.json`.)* The word table in `src/cam.r.js` is still used for a name the person types.
- [x] Say "not sure" when the kind is uncertain, and offer the three likeliest kinds. *(build 8; `fusion.kind_at` in `docs/CONTRACTS.md`; the `notsure` section of `test/rec/check_rec.js`)*
- [x] Measure the kind of eye on held-out local research-grade photos, per kind, with the confusion tables. *(`docs/EVAL.md`, `docs/eval/model-<id>.md`.)* In build 8 the kind is right for 87.3% (86.3 to 88.3) of the 4,197 test photos, and for 98.2% (97.3 to 98.8) of 1,240 COCO test photos of people, pets, grazing animals and rooms.
- [ ] Measure the time a photo takes on a phone. It has been measured only on build machines (`docs/LOG.md`, 03:40).

Still open: the pocket recognizer in build 8 carries stand-in heads, fitted on two thirds of the evaluation set's `val` photos and on COCO photos of every licence. Heads fitted on the training photos were measured in evaluation run 25 (`runs/eval/25/rerun/shipped-alachua-pre2025-tinyclip-39m-16.json` on `ci`, published as `pub/heads-alachua-pre2025-tinyclip-39m-16`): on the same test photos the kind of eye was right for 88.5% (87.5 to 89.5), the top species for 53.4%, and a species was named for 24.9% and right for 88.2% (86.2 to 90.0) of those. They are not in build 8. On 11 October the coordinator set a rule for which photos heads may be fitted on, pending the owner's decision (`docs/LICENCES.md`), and the heads in build 8 predate it. The time a photo takes on a phone is unmeasured.

## Phase 3: species (the naturalist)

Goal: a species name for what was photographed, shown only when it is likely to be right.

- [x] Build the local candidate list from GBIF: 5,911 species recorded in Alachua County through 2024, with counts by month and full taxonomy. *(commit `9ae44df`; `data/regions/us-fl-alachua/species.json` and its `SUMMARY.md`)*
- [x] Run BioCLIP 2 (ViT-L/14, MIT licence) against that list, with and without a place-and-season prior, on held-out local research-grade photos. Top-1 is 90.3% (89.4 to 91.3) without the prior and 92.4% (91.6 to 93.2) with it, and top-5 is 96.8% and 97.5% (`docs/EVAL.md`, `tools/eval/study1.py`). A clean build machine reproduced the evaluation from the published files (`runs/eval/4` on `ci`, `docs/eval/reproduction.txt`).
- [x] Build a species service. `service/` holds BioCLIP 2 behind a small Gradio app, which answered at 1.1 seconds a photo on a build machine's processor (`docs/LOG.md`, 11 October, 00:52). It has not been deployed: a free Hugging Face account cannot host a Docker or Gradio space on plain processors, and may host one on shared graphics cards only once the account is thirty days old, which is about 10 November.
- [x] Run the larger model on the device. Because the service had no free server, BioCLIP 2's image half was quantized for the browser's WASM runtime in five recipes and each was measured through that runtime (`docs/LOG.md`, 03:45; `docs/eval/variants.md`). The recipe `hybrid-fc2-w8` (309.8 MB, four parts fetched from a commit pinned by `pin/model-bioclip2-l14-462ecdc`) ships in build 8 as `models/naturalist/`: the person is asked once, the file is kept in Cache Storage (`src/cam.rec.js`), and the model runs in a worker of its own after the pocket recognizer has named the kind. Scored from the original model's vectors with the page's settings, it names a species for 84.6% (83.4 to 85.6) of the test photos and is right for 98.1% (97.6 to 98.5) of those (`docs/EVAL.md`).
- [x] Show uncertainty: under `offer_at` the page offers three species of the winning kind and lets the person choose. *(`docs/CONTRACTS.md`; `docs/EVAL.md`, "What the page would show")*

Still open: no phone has held the larger model, and whether a phone's browser will keep a 310 MB file and find the memory to run it is unknown (on iOS it is doubtful). The species service has no home, and `service.json`, which would point the page at it, is absent.

## Phase 4: a regional pocket model

Goal: species-level recognition on the device, offline, for the region.

- [x] Gather training photos. `train/alachua-pre2025` holds 84,808 photos of 5,467 species, all dated before 2025, read from iNaturalist's open-data files (commit `2850053`; `data/train/alachua-pre2025/SUMMARY.md`; the manifest is on `pub/data-alachua`).
- [x] Fit heads on the pocket encoder's vectors of those photos, and measure them on the held-out photos. *(evaluation run 25, `runs/eval/25/` on `ci`; the figures are under Phase 2)*
- [ ] Ship heads fitted under the licence rule of 11 October, with the list of photos they were fitted on published beside them as the attribution.
- [ ] Teach a small encoder from BioCLIP 2 (distillation) on openly licensed iNaturalist photos of the region's species.
- [ ] Write a model card for the shipped slot, stating its data, licences, accuracy by group and known failures. The slot manifests carry an `evaluation` block, and `docs/eval/model-<id>.md` gives breakdowns by kind and the commonest mistakes for each model measured.

Still open: the three lines above that carry no tick.

## Phase 5: the game, sharing, and review

- [ ] Decide the rule of the finding game (kept, lent, sealed eyes, or held open for a town). The decision is awaited.
- [ ] Share a still or a clip through the phone's own share sheet. The page calls `navigator.share` (`src/cam.c2.js`), and the share sheet has not been checked on any phone (`docs/LOG.md`).
- [ ] Have a vision scientist review the sixteen eye models, and fold the corrections back into `docs/SOURCES.md`.
- [ ] Build for the iPhone and Android stores, if the web app proves the case for them.

Still open: every line of this phase.

## What comes next, in order

1. An iPhone comes first. The page has never run on one, and nobody knows yet whether a phone's browser will keep the 310 MB model and run it, or how long the pocket recognizer takes on a phone.
2. A server for phones that cannot hold the larger model comes next. The service in `service/` was proven on a build machine and has not been deployed, the page reads its address from `service.json` at the site's root (`docs/CONTRACTS.md`), and a free home on Hugging Face becomes possible at about 10 November.
3. A student model small enough for every phone follows. Distilling BioCLIP 2 into a small encoder needs a graphics card, and the build machines used so far have none.
4. More regions come after that. The species list, the evaluation photos and the training photos are built for one region by the scripts in `tools/species/`, and every number so far holds for Alachua County alone.
5. The game comes last, once its rule is decided.
