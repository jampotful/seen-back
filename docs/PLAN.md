# Plan

The aim is one app that works by itself on an iPhone, an Android phone and a computer: it recognizes what you photographed, changes your camera toward that creature's sight, and keeps a record of who you have met.

## Standards every phase is held to

- **Checked, or labelled as unchecked.** Every claim the app makes about an animal carries a grade and a source. Every number in an evaluation comes from a script in this repository that anyone can rerun.
- **Tested on real engines.** Chromium and WebKit, on a phone-sized screen and a desktop one, before a build is called done.
- **Private by default.** Photos stay on the device. Anything that sends a photo elsewhere says so first and can be turned off.
- **Usable with no signal.** The app opens offline, and recognition of the kind of creature works offline.
- **Licences recorded.** Every model, dataset and font is listed with its licence before it ships.

## Phase 1: an address, and an app that installs

- [x] Standalone page with the typeface served from this site.
- [x] Web app manifest, icons, and a service worker that keeps the app shell and large files.
- [ ] Served at an https address. *(waiting on push access)*
- [ ] Checked on Android Chrome, desktop Chrome, desktop Safari, and iPhone Safari.

## Phase 2: recognition on the device (the pocket recognizer)

Goal: the page itself tells a cat from a heron from an oak, with no network, in under a second on a recent phone.

- [ ] Choose the image encoder. Candidates are small image-and-text models that run in a browser. The choice turns on licence, size, and measured accuracy on local photos. MobileCLIP-S0 (11.8 MB quantized) is the first candidate; its licence must be read before it ships.
- [ ] Build the label set: the sixteen kinds of eye, each written several ways, plus the species most recorded locally.
- [ ] Compute the label embeddings once, offline, so the phone downloads only the image encoder.
- [ ] Run it in the browser with ONNX Runtime Web, files served from this site and kept by the service worker.
- [ ] Map a recognized species to its kind of eye through taxonomy (class, order, family), replacing the word table.
- [ ] Acceptance: kind-of-eye accuracy on a held-out set of local research-grade photos, reported per kind, with the confusion table. Latency measured on each engine.

## Phase 3: species (the naturalist)

Goal: a species-level name for what was photographed, with an honest confidence.

- [ ] Build the local candidate list from GBIF: every species recorded around the test town, with counts by month and full taxonomy.
- [ ] Run BioCLIP 2 (ViT-L/14, MIT licence) zero-shot against that list, with and without a place-and-season prior, and measure top-1 and top-5 accuracy on held-out local research-grade photos.
- [ ] Serve it: a small service the app can call when there is signal. The kind of eye still comes from the device at once; the species name arrives after.
- [ ] Show uncertainty: when the top candidates are close, the app says "one of these" and lets the person choose.

## Phase 4: a regional pocket model

Goal: species-level recognition on the device, offline, for the region.

- [ ] First step: a classifier head trained on the pocket encoder's features for the most recorded local species. Small, quick to train, and a fair baseline.
- [ ] Then distillation: a small encoder taught by BioCLIP 2 on openly licensed iNaturalist photos of regional species.
- [ ] Evaluation against the Phase 3 numbers on the same held-out photos. A model card stating data, licences, accuracy by group, and known failures.

## Phase 5: the game, sharing, and review

- [ ] The rule of the finding game (kept, lent, sealed eyes, or held open for a town). *(awaiting a decision)*
- [ ] Sharing a still or clip from the phone's own share sheet.
- [ ] Review of the sixteen eye models by a vision scientist; corrections folded back into `docs/SOURCES.md`.
- [ ] iPhone and Android store builds, if the web app proves the case for them.
