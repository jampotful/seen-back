# Log

Newest first. Times are US Eastern.

## 11 October 2026

- **04:27** Build 8 on `main`: two recognizers in the page. The pocket model (TinyCLIP 39M/16, 41 MB) answers every photo and now says so when it is not sure. Its kind rows were fitted on local wildlife photos together with photos of people, pets, grazing animals and rooms, and it asserts a kind of eye only from a level chosen on held-out photos. On the test photos its kind of eye is right for 87.3% of wildlife photos (86.3 to 88.3) and 98.2% of the photos of people, pets and rooms; it asserts a kind for 78.8% of wildlife photos and is then right 95.5% of the time. A larger model (BioCLIP 2, ViT-L/14, 310 MB) is offered as a download that happens once, runs on the device in the background, and corrects the first answer when its own arrives. Scored from the original model's vectors with the settings the page uses, it shows a species name for 84.7% of test photos and the name is right for 98.0% of those.
- **03:55** The larger model ran inside the page in the coordinator's sandbox with the real file: 27 local test photos, 6.2 to 6.8 seconds each on one thread, most named to species, and every photo the pocket model was unsure of answered. No phone has held it yet.
- **03:45** Laboratory merged. BioCLIP 2's image half was quantized for the browser's WASM runtime in five recipes and each was measured through that runtime. The one that ships (`hybrid-fc2-w8`, 309.8 MB, cut into four parts of at most 90 MB) names the species on 93.75% of 320 test photos against 94.06% for the original on the same photos, at 4.9 seconds a photo on one thread of a build machine. The parts are served from a pinned commit of this repository.
- **03:45** A mistake found: the laboratory workflow reads `ci/lab/runs/<label>.json` when that file exists, so a new plan pushed in `ci/lab/run.json` was ignored and two runs recomputed the wrong thing for half an hour. The run files were corrected.
- **03:40** Engines, on build machines, with the model that shipped in build 7: ready in 2.1 to 6.4 seconds, and a photo answered in 0.5 to 0.95 seconds on Chromium, WebKit and Safari (headless Firefox takes about 3.5).
- **03:11** Training photos published: `train/alachua-pre2025` on `pub/data-alachua`, 84,808 photos of 5,467 species, all dated before 2025, read from iNaturalist's open-data files with no API in the way. An extra set of 10,240 COCO photos (people, cats, dogs, grazing animals, rooms with nothing alive) gives the kind decision something other than wildlife to be tested on.
- **02:31** The first route to the training photos failed three times against GBIF's API: one run died on a page of unreadable JSON, the fix for that flooded the API with halved requests once it began refusing, and a patient third run was throttled until its two-hour limit. The open-data route replaced it.
- **02:26** Build 7: the first recognizer ships (TinyCLIP 39M/16, MIT licence, int8, sentence-made rows for the sixteen kinds of eye, for `none`, and for 5,911 local species). The settings first exported for it had been tuned on wildlife photos alone and called an astronaut, a coffee cup and a rocket plants. Hand-chosen interim settings went out with the build, and the proper repair (kind rows fitted with people and rooms among the photos, and an answer of "not sure") became the next round's work. The same build fixes the self-test race seen in Ecosia and a blank photo in macOS WebKit, where a bitmap was closed too early.
- **00:52** The Hugging Face account is new and free. A free account cannot host a Docker or Gradio space on plain processors, and may host one on shared graphics cards only once it is thirty days old. The species service (BioCLIP 2 behind a small Gradio app, 1.1 seconds a photo on a build machine's processor) therefore has no free home before about 10 November. Decision: the larger model moves onto the device, and the service stays in the repository, proven and undeployed.
- **00:50** The second round was merged: laboratory runs that can be cancelled and that publish only complete results, the scoring written once in numpy and checked against the page number for number, and an end date pinned for the evaluation build.
- **23:27 to 00:50** Lost time, the second and last of its kind: four resumed agents ran one after another instead of together, so most of that round's agents had a few minutes each. Every round since has been made of fresh agents started together with written briefs.

### What was checked on 11 October, and how

- `test/rec/check_rec.js` (nineteen sections, headless Chromium, a stand-in model whose answers Python computed first): the flow from photo to eyes, the answer "not sure", trained heads, parity with the numpy reference, progress, typing a name, the larger model (consent, a download in parts with a reload part-way, stopping, deleting, its answer arriving in the background, its failures in words), leaving and returning, no network, a new version, kept copies, missing and damaged files, a dying worker.
- `test/check4.js`: the word table, the record, the viewer, the edges and the sweep of every kind of eye.
- The evaluation (`docs/EVAL.md`) was reproduced on a clean build machine from the published vectors.
- The self-test ran on Chromium, Firefox, WebKit on Linux and macOS, Safari 26.6, and Safari on iOS 26.5 in an iPhone 17 simulator.

### What has not been checked on anything real

A real iPhone. The larger model on any phone: whether its browser will hold a 310 MB file and the memory to run it is unknown, and on iOS it is doubtful. How long the pocket model takes on a phone. The share sheet. Installing to a home screen.

## 10 October 2026

- **23:25** The self-test ran on real hardware for the first time. A phone with a Mali-G715 chip: 93 of 93 in Chrome 154 at 16.7 ms a frame at full size (699 by 1280); 92 of 93 in Ecosia, the one failure being the test sampling a clip's corner before the clip's first frame was in place. An Intel MacBook Pro with a Radeon Pro 5500M: 93 of 93 in Chrome 154 and in Safari 26.5, and Safari's window shows the picture, so the black window seen on the build machine belonged to its virtual display.
- **23:20** First look at the large biology models on the 4,197 test photos, scored against the 5,911 local species by scientific name: BioCLIP 2 names the species on 90%, 92% with the month prior, top five 97%; BioCLIP 2.5 (ViT-H/14) 93%, 94% and 98%. The kind of eye taken from the top species is right on 98%. These come from a quick script and are being redone with intervals by `tools/eval/`.
- **23:15** Training photos: `tools/species/build_train.py` builds a manifest of photos from before 2025, up to sixty a species, and iNaturalist's own names for each GBIF species.
- **22:25 to 23:11** Lost time: a trial message to one finished agent held the coordinator for 46 minutes while five other pieces of work waited. Batches now go out whole.
- **22:25** Build 6 on `main`: recognition inside the page (ONNX Runtime Web in a worker, exact Pillow resize, scoring with a place-and-season prior, versioned keeping for use with no signal). No model ships yet, so the page still asks; the model is chosen by measurement next.
- **22:10** First measurements on the held-out photos (4,197 test photos from 2025 and 2026, zero-shot, untuned): the best small permissively licensed model, TinyCLIP 39M/16, gets the kind of eye right 78% of the time and the species 21% (35% with the season prior). Too weak to ship as it is; heads trained on local photos from before 2025 come next.
- **22:05** Four areas of work came back and were merged: the species list for Alachua County (5,911 species, monthly counts through 2024) and 6,000 evaluation photos from 2025 onward; the model laboratory with eleven models measured; the self-test and cross-engine workflow (93 of 93 checks on WebKit, Safari 26.6, Safari on iOS 26.5 in a simulator, and Firefox); the recognizer in the page.
- **20:45** Work split into four areas with written contracts (`docs/CONTRACTS.md`), each on its own branch, using GitHub's build machines for anything that needs the open network.
- **20:35** Decisions: MobileCLIP will not ship (research-only licence). New World vultures take the generic bird eyes. Evaluation photos are dated 2025 onward, later than the 2024-05-01 GBIF snapshot behind BioCLIP 2's training data; the species list and its prior use records through 2024 only.
- **20:10** GitHub's build machines confirmed as the overnight compute (Linux, and macOS with Xcode 26.6 and iPhone 17 simulators). Results return on the `ci` branch.
- **19:55** Build 5. The app moves into this repository: sources in `src/`, a build script, browser checks, a web app manifest, icons, a service worker, and the typeface served from the site. The word table and the record flow pass against the repository build.
- **19:40** Build 4b. The sheet that asks what was photographed now asks for the kind of animal or plant. A word it does not know is caught and explained.
- **19:00** Sketch 4. The fifteen offered kinds are removed. Eyes come only from a named photograph. Every meeting is kept in a record; eyes already met can be reopened. A list of one town's sixty most recorded species appears as sixty blanks.
- **18:30** Sketch 3. One fluid camera: an opening screen, a full-screen finder, a change of eyes that closes to the shape of the animal's pupil and reopens in its view. WebGL 2 engine in three passes. Field of view, sharpness with retinal layout, pupil-shaped defocus, colour, and four motion signatures. Recording and stills.
- **Earlier** Sketches 1 and 2 on Canvas 2D, retired.

### What was checked that day, and how

Headless Chromium with software graphics, a looping fake camera, and a stand-in for the naming service: the live flow, the two-step flow where no live camera is allowed, the change of eyes at fixed instants, every kind of eye, hold-to-compare, tap-to-focus, recording, stills, every back step, a refused camera, refused storage, reduced motion, a browser with no WebGL 2, and a desktop window.

### What has not been checked on anything real

A phone's graphics chip, a real iPhone, a real Mac's Safari window (on the build machine's virtual display the picture reads back correctly and shows black on screen), Android Chrome, and the share sheet. WebKit, Safari and the iPhone simulator have now run the self-test on build machines.
