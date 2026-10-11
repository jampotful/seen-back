# Log

Newest first. Times are US Eastern.

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
