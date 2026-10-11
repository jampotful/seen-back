# Plan

The aim is one app that works by itself on an iPhone, an Android phone and a computer: it recognizes what you photographed, changes your camera toward that creature's sight, and keeps a record of who you have met.

This file was brought up to date on 11 October 2026, when build 9 (commit `013bb77`) was live. A ticked line names its evidence: a commit, a file, or a run whose results are on the `ci` branch.

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

Still open: the page has not run on an iPhone, and installing it to a home screen has not been checked on any device. Chromium 141 on a build machine reports no reason against installing it (`runs/engines/40-big-linux`, `docs/ENGINES.md`).

## Phase 2: recognition on the device (the pocket recognizer)

Goal: the page itself tells a cat from a heron from an oak, with no network, in under a second on a recent phone.

- [x] Choose the image encoder. TinyCLIP 39M/16 (MIT licence, int8, 41.0 MB) ships in `models/pocket/` (commit `987c09b`, then builds 8 and 9). MobileCLIP will not ship, because its licence is for research only (`docs/LICENCES.md`). Applied to slots made from sentences, the rule written beforehand in `tools/eval/decide.py` gave a tie that falls to TinyCLIP 8M/16, an answer `docs/EVAL.md` calls provisional. On the stand-in slots with kind rows fitted on photos, TinyCLIP 39M/16 was ahead by 4.8 points (4.1 to 5.5) on the kind of eye, a second look that `docs/EVAL.md` counts as evidence outside the rule.
- [x] Build the label set: phrases for the sixteen kinds of eye and for `none` (`labels/kinds.json`), and rows for the 5,911 local species (`models/pocket/species.json`).
- [x] Compute the label rows once, offline, so that the phone downloads the image encoder and the row files and computes no text. *(`tools/eval/export_heads.py`; `models/pocket/kinds.f16.bin`, `species.f16.bin`, `species.bias.f32.bin`)*
- [x] Run it in the browser with ONNX Runtime Web, with the files served from this site and kept by the service worker. *(build 6, commit `68dc1cd`; `vendor/ort/`; the kept files are listed in `runs/engines/34-live/summary.json`)*
- [x] Map a recognized species to its kind of eye through taxonomy. *(`tools/species/eyes.py`, the `eyes` column of `data/regions/us-fl-alachua/species.json`.)* The word table in `src/cam.r.js` is still used for a name the person types.
- [x] Say "not sure" when the kind is uncertain, and offer the three likeliest kinds. *(build 8; `fusion.kind_at` in `docs/CONTRACTS.md`; the `notsure` section of `test/rec/check_rec.js`)*
- [x] Measure the kind of eye on held-out local research-grade photos, per kind, with the confusion tables. *(`docs/EVAL.md`, `docs/eval/model-<id>.md`.)* In build 9 the kind is right for 89.1% (88.2 to 90.1) of the 4,197 test photos, and for 96.9% (1,201) of 1,240 COCO test photos of people, pets, grazing animals and rooms (`docs/eval/decision-pocket-v3.json`).
- [ ] Measure the time a photo takes on a phone. It has been measured only on build machines (`docs/LOG.md`, 03:40).

Still open: the line above that carries no tick. `docs/EVAL.md` is behind build 9: its rows called "live" describe the pocket slot of build 7, some of its naming figures predate the rule that a species is named only under an asserted kind, and four of its figures were rounded twice (`docs/eval/audit.md`).

## Phase 3: species (the naturalist)

Goal: a species name for what was photographed, shown only when it is likely to be right.

- [x] Build the local candidate list from GBIF: 5,911 species recorded in Alachua County through 2024, with counts by month and full taxonomy. *(commit `9ae44df`; `data/regions/us-fl-alachua/species.json` and its `SUMMARY.md`)*
- [x] Run BioCLIP 2 (ViT-L/14, MIT licence) against that list, with and without a place-and-season prior, on held-out local research-grade photos. Top-1 is 90.3% (89.4 to 91.3) without the prior and 92.4% (91.6 to 93.2) with it, and top-5 is 96.8% and 97.5% (`docs/EVAL.md`, `tools/eval/study1.py`). A clean build machine reproduced the evaluation from the published files (`runs/eval/4` on `ci`, `docs/eval/reproduction.txt`).
- [x] Build a species service. `service/` holds BioCLIP 2 behind a small Gradio app, which answered at 1.1 seconds a photo on a build machine's processor (`docs/LOG.md`, 11 October, 00:52). It has not been deployed: a free Hugging Face account cannot host a Docker or Gradio space on plain processors, and may host one on shared graphics cards only once the account is thirty days old, which is about 10 November.
- [x] Run the larger model on the device. Because the service had no free server, BioCLIP 2's image half was quantized for the browser's WASM runtime in five recipes and each was measured through that runtime (`docs/LOG.md`, 03:45; `docs/eval/variants.md`). The recipe `hybrid-fc2-w8` (309.8 MB, four parts fetched from a commit pinned by `pin/model-bioclip2-l14-462ecdc`) ships as `models/naturalist/` from build 8: the person is asked once, the file is kept in Cache Storage (`src/cam.rec.js`), and the model runs in a worker of its own, in the background, after the pocket recognizer has answered. As shipped, with `kind_at` 0.5, it names a species for 84.2% of the test photos and is right for 98.2% of those, scored from the original model's vectors (`tools/audit/results/recompute.json`, `docs/eval/audit.md`).
- [x] Fetch the larger model from the live address in real browsers. With build 8, through the page's own sheet, it was kept and answering in Safari 26.6 on macOS, Safari in an iPhone 17e simulator, WebKit 26.0 on macOS and on Linux, and Chromium 141 on Linux, all on build machines; nothing was fetched again after a reload, and with the network cut Chromium still ran it (`docs/ENGINES.md`).
- [x] Measure its memory. The largest browser process peaked at 1,501 MiB in Chromium and at 1,688 to 2,598 MiB in the Apple and WebKit browsers (`docs/ENGINES.md`). In the laboratory, the weights handed to the runtime as a data file beside a 2 MB graph file cut the WASM heap from 821 to 429 MiB and the renderer's peak from 1,330 to 953 MiB, with identical vectors (`ci/lab/mem/results.json`). That form is measured and published on `pub/model-bioclip2-l14-b` (commit `add8cf5`, kept by `pin/model-bioclip2-l14-b-add8cf5`), and the page does not use it yet.
- [x] Show uncertainty: under `offer_at` the page offers three species of the winning kind and lets the person choose. *(`docs/CONTRACTS.md`; `docs/EVAL.md`, "What the page would show")*

Still open:

- No phone has held the larger model, and whether a phone's browser will keep a 310 MB file and find the memory to run it is unknown.
- The page should load the larger model in its lighter form, with the weights as a data file beside a small graph file; the worker's side is written as `ci/lab/patches/worker-external-data.patch`, and the page's side is not.
- In WebKit, a reload while the larger model is arriving makes the page fetch a kept part again and then fail with "a part is no longer kept on this device" (`runs/engines/38-linux-firefox-webkit/rec/resume-webkit.json`). Chromium resumes in the same probe.
- After a reload with the larger model kept, the first photo waited 25 to 42 seconds for the pocket recognizer's answer in Chromium, where it otherwise comes in under a second on build machines (`docs/ENGINES.md`; `runs/engines/40-big-linux/big-chromium.json`; `docs/LOG.md`, 03:40). The pocket recognizer should answer first, in its usual time, whether or not the larger model is kept.
- With the larger model on the device, it should look at every photo the pocket recognizer called alive, also those the small model named. Where its name differs, its name should replace the small model's, and its "not sure" should never remove a name. A review on 11 October saw a name from the pocket recognizer stand with no second look; this is open.
- The species service has no home, and `service.json`, which would point the page at it, is absent.

## Phase 4: a regional pocket model

Goal: species-level recognition on the device, offline, for the region.

- [x] Gather training photos. `train/alachua-pre2025` holds 84,808 photos of 5,467 species, all dated before 2025, read from iNaturalist's open-data files (commit `2850053`; `data/train/alachua-pre2025/SUMMARY.md`; the manifest is on `pub/data-alachua`).
- [x] Fit heads on the pocket encoder's vectors of those photos, and measure them on the held-out photos. *(evaluation run 25, `runs/eval/25/` on `ci`; the heads under the licence rule in `docs/eval/shipped-alachua-pre2025-nc-tinyclip-39m-16.json`)*
- [x] Ship heads fitted under the licence rule of 11 October, with the list of photos they were fitted on published beside them as the attribution. *(build 9, commit `013bb77`: heads from `pub/heads-pocket-v3` at `f0c2544`, fitted on 83,348 photos and chosen by a rule fixed before their numbers existed, `docs/eval/decision-pocket-v3.json`; the list is `fitted_on.csv` there, `docs/LICENCES.md`)* On the test photos they name a species for 20.1% and are right for 93.3% of those (788 of 845), where the heads of build 8 named 13.3% and were right for 92.3% (`docs/eval/shipped-alachua-pre2025-nc-tinyclip-39m-16.json`, `docs/eval/audit.md`).
- [ ] Teach a small encoder from BioCLIP 2 (distillation) on openly licensed iNaturalist photos of the region's species.
- [ ] Write a model card for the shipped slot, stating its data, licences, accuracy by group and known failures. The slot manifests carry an `evaluation` block, and `docs/eval/model-<id>.md` gives breakdowns by kind and the commonest mistakes for each model measured.

Still open: the two lines above that carry no tick.

## Phase 5: the game, sharing, and review

- [ ] Decide the rule of the finding game (kept, lent, sealed eyes, or held open for a town). The decision is awaited.
- [ ] Share a still or a clip through the phone's own share sheet. The page calls `navigator.share` (`src/cam.c2.js`), and the share sheet has not been checked on any phone (`docs/LOG.md`).
- [ ] Have a vision scientist review the sixteen eye models, and fold the corrections back into `docs/SOURCES.md`.
- [ ] Build for the iPhone and Android stores, if the web app proves the case for them.

Still open: every line of this phase. Thin app shells around the built page ran on build machines as an experiment (`native/README.md`): an Android WebView app on an Android 14 emulator and an iPhone WKWebView app in an iPhone 17 simulator each passed the page's self-test, 98 checks of 98. In the iPhone shell the larger model cannot be kept, because the app serves the page from its own address scheme and Cache Storage accepts only http and https addresses. No Android file has been published yet that the owner could put on a phone.

## What comes next, in order

1. An iPhone comes first. The page has never run on one, and nobody knows yet whether a phone's browser will keep the 310 MB model and run it, or how long the pocket recognizer takes on a phone. On build machines the Apple and WebKit browsers reached 1,688 to 2,598 MiB while running the larger model, and in WebKit a reload during its download breaks it.
2. A server for phones that cannot hold the larger model comes next. The service in `service/` was proven on a build machine and has not been deployed, the page reads its address from `service.json` at the site's root (`docs/CONTRACTS.md`), and a free home on Hugging Face becomes possible at about 10 November.
3. A wider set of photos with nothing alive in them comes third. The only such photos the recognizers were tuned and tested on are COCO's rooms, and in the page before build 9 shipped the pocket recognizer called a brick wall a reptile and named a photo of old coins as a fungus (`docs/LOG.md`, 05:52).
4. Then domestic animals and cultivated plants join the species list. The list was built from records of wild things, so it holds no dog, cattle or sheep, most houseplants or common garden flowers, and every name the app gives one of them is wrong; on COCO photos the pocket recognizer named 43 of 73 cows, each wrongly (`docs/eval/audit.md`, `docs/eval/pets-livestock.json`).
5. A student model small enough for every phone follows. Distilling BioCLIP 2 into a small encoder needs a graphics card, and the build machines used so far have none.
6. More regions come after that. The species list, the evaluation photos and the training photos are built for one region by the scripts in `tools/species/`, and every number so far holds for Alachua County alone.
7. The game comes last, once its rule is decided.
