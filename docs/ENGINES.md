# Engines: what ran where

This file records what the page has been run on, and what it has not. Every figure names the run it came from; runs are directories on the `ci` branch under `runs/`. Times are from build machines unless a line says otherwise, and a build machine is a server, so its times say little about a phone.

## Real devices (the owner's, 10 October 2026, build 6)

| Device | Browser | Self-test | Notes |
|---|---|---|---|
| An Android phone with a Mali-G715 graphics chip | Chrome 154 | 93 of 93 | 16.7 ms a frame at full size (699 by 1280) |
| The same phone | Ecosia | 92 of 93 | The one failure was the test's own (it sampled a clip before its first frame); fixed in build 7 |
| An Intel MacBook Pro, Radeon Pro 5500M | Chrome 154 | 93 of 93 | |
| The same Mac | Safari 26.5 | 93 of 93 | The window shows the picture |

No real device has run a build with a recognizer in it, and no real iPhone has run the page at all.

## Build 8 on build machines (11 October 2026)

Sources: `runs/engines/33-linux-chromium`, `33-linux-firefox-webkit`, `33-macos`, `34-live`.

| Engine | Recognizer checks (`test/rec/check_rec.js`, stand-in model) | Real pocket model against Python | Self-test |
|---|---|---|---|
| Chromium 141, Linux | all 18 sections pass | agrees | passes, phone and desktop sizes, 141 checks |
| Firefox 142, Linux (headed) | 15 pass; `service` and `large` fail | agrees | passes, 141 checks |
| WebKit 26.0, Linux | `service` fails; `notsure`, `large`, `offline`, `damaged` did not finish; the rest pass | agrees | passes, 141 checks |
| WebKit 26.0, macOS | `service` fails; `large`, `offline`, `damaged` did not finish; the rest pass | agrees | passes, 140 checks |
| Safari 26.6, macOS | not run there | 14 of 14 photos, cosine at least 0.9954 | passes, 140 checks |
| Safari, iPhone simulator | not run there | 14 of 14 photos, cosine at least 0.9963 | passes, 140 checks |

What the failures were:

- `service` in Firefox and WebKit was the check's fault. The page said the right things; the check only knew Chromium's wording for a refused cross-origin request. With the check corrected the section passes in all three (`runs/engines/37-linux-chromium`, `37-linux-firefox-webkit`).
- `offline` in WebKit was the check's fault. The test switch that cuts the network makes WebKit refuse to load anything; the live-address check cuts the network at a proxy and passes.
- `large` in WebKit: a reload while the larger model's second part is arriving made the page fetch the first part again, although it had been kept, and fail with "a part is no longer kept on this device" (`runs/engines/38-linux-firefox-webkit/rec/resume-webkit.json`). A trace of every Cache Storage call (runs 42 to 52) showed that the page deletes nothing. Where no service worker controls the page, which is how the probe and the checks run, Playwright's WebKit on Linux loses what the page before the reload had kept, and a second `put` to an address kept before is answered as done and keeps nothing. Deleting the address first makes the `put` stay. With the service worker in control, as at the live address, build 9 resumes correctly in the same WebKit (`runs/engines/50-linux-firefox-webkit`). A fix that deletes before every `put` passes the probe in WebKit and in Chromium (`ci/engines/patches/webkit-resume.patch`, runs 51 and 52); it is not in the page yet, because the recognizer's full checks have not been run with it. Safari itself was not put through this probe.
- Not yet explained: `damaged` in WebKit, `notsure` in WebKit on Linux, and three sub-checks of `large` in Firefox.

The live address (`runs/engines/34-live`): in Chromium, Firefox and WebKit the page loads as build 8, the service worker controls the first and second visits, and with the network cut the page starts and the pocket model is ready.

Build 9 at the live address (`runs/engines/41-live`): the same in Chromium 141, Firefox 142 and WebKit 26.0, with the new heads answering a test photo. Build 10 (`runs/engines/54-live`): the same again.

## The larger model, fetched from the live address through the page's own sheet (build 8)

Sources: `runs/engines/35-big-mac-ws` (Safari), `35-big-mac-sim` (iPhone simulator), `36-big-mac-ws` (WebKit, macOS), `36-big-linux` (WebKit, Linux), `40-big-linux` (Chromium), `39-big-linux` (Firefox, headed on a virtual display). Memory is the resident size of the largest browser process, read with `ps` once a second.

| | Safari 26.6, macOS | Safari, iPhone 17e simulator | WebKit 26.0, macOS | WebKit 26.0, Linux | Chromium 141, Linux | Firefox 142, Linux |
|---|---:|---:|---:|---:|---:|---:|
| Download, "Get it" to last byte | 5.6 s | 9.9 s | 3.3 s | 2.3 s | 9.2 s | 5.3 s |
| Ready to answer after "Get it" | 18.5 s | 38.9 s | 15.2 s | 10.6 s | 21.9 s | 146.9 s |
| Seconds a photo (four photos) | 5.5 to 7.3 | 9.9 to 10.8 | 4.9 to 6.1 | 4.7 to 5.0 | 7.4 to 7.9 | no answer to any of three |
| Largest browser process at its peak | 2,077 MiB | 1,688 MiB | 2,178 MiB | 2,598 MiB | 1,501 MiB | 1,930 MiB |
| All four parts kept and verified | yes | yes | yes | yes | yes | yes |
| Fetched again after a reload | nothing | nothing | nothing | nothing | nothing | not reached |
| Tab died | no | no | no | no | no | no crash reported; the page closed before the second visit |

- The four parts come from `raw.githubusercontent.com` with status 200, no redirect, no compression, and a header that allows any origin. Each part's checksum, and the checksum of the four joined, matches the manifest.
- The iPhone simulator borrows the Mac's memory. A pass there does not show that a real iPhone holds the model.
- Firefox (`runs/engines/39-big-linux/big-summary.txt`) kept and verified the model, and then spent 130.7 of its 146.9 seconds before "ready" in the first run of the model (8.3 s to make the session). The larger model then answered none of the three photos tried: each ended as "slow", and the pocket model took 11.4 to 11.9 seconds a photo beside it, where it took 0.6 to 0.7 in Chromium (`runs/engines/35-big-linux`). The page had closed by the time of the second visit, so that was not measured; no crash was reported. All of Firefox's browser processes together peaked at 3,028 MiB. An earlier attempt with the three browsers on one machine (`runs/engines/35-big-linux`) lost the Firefox page before its figures were read, and returned none. These Firefox figures came from Playwright's own build of Firefox, whose WebAssembly runs about fifteen times slower than Mozilla's build of the same release (the section of 18 October on Firefox, below).
- The same four photos on every engine: a Little Blue Heron and a Green Treefrog named correctly; an American Bird Grasshopper right as the first answer and left unnamed, being under the level for a name; and one plant photo (Guinea Hen Weed) that sits on that level, named wrongly as Small-Flower Pawpaw by the three Apple engines and left unnamed by the other two.
- With the network cut after the model was kept, Chromium still started the page and the larger model still named the heron.
- After a reload with the larger model kept, the first photo's first answer took 25 to 42 seconds in Chromium on the build machine. The larger model is not the cause: it starts only after the pocket model's answer is on screen, and the same wait appears with no larger model at all. A build machine has no graphics chip and draws the page in software, and that drawing process took most of a processor while the photo waited. Which step of the page's own work costs the time was not measured, and no phone has been timed from choosing a photo to seeing its kind.

## Memory of the larger model (laboratory, 11 October 2026)

Sources: `ci/lab/mem/results.json`, runs `lab/32` to `lab/35`.

| Form of the model | WASM heap | Renderer at its peak (headless Chromium, the page's worker) | Vectors against the shipped file |
|---|---:|---:|---|
| One 310 MB file (what build 8 and 9 fetch) | 821 MiB | 1,330 MiB | the same file |
| A 2 MB graph file with the weights beside it as a data file (`pub/model-bioclip2-l14-b`) | 429 MiB | 953 MiB | identical |

No setting of the runtime alone changes the heap without changing the answers. The second form needs a change in the page and its worker.

That change is written and waits on the branch `agent/rec-b`. In headless Chromium, with the real files and the page's own flow, six photos got the same kinds, names and probabilities in both forms, digit for digit (`ps` read once a second; the largest renderer process):

| | One file | Graph and weights | 
|---|---:|---:|
| While the model is fetched and started | 1,390 MiB | 1,060 MiB |
| While it answers photos | 1,281 MiB | 936 MiB |

A trial on build machines then served that branch's own page and ran the larger-model check on it (`run/engines/bigb-a`, commit `2fecb34`; `runs/engines/53-big-mac-ws`). In Safari 26.6 and in WebKit 26.0 on macOS the new form was fetched from `raw.githubusercontent.com`, verified, kept and run, with the same names as the live form (Little Blue Heron at 0.988 for the first photo), ready 16.4 and 14.8 seconds after "Get it". The largest process still peaked at 2,044 MiB in Safari and 2,046 MiB in WebKit on the first visit, against 2,077 and 2,178 MiB for the live form: in WebKit the weight lies outside the WASM heap, and this form does not remove it. The iPhone simulator's job could not start Safari (`runs/engines/53-big-mac-sim`), and the Linux job had not returned when this was written (`runs/engines/53-big-linux`). The new form is therefore correct in three engines and lighter in one, and the form that five engines have run stays live.

## Where WebKit's memory goes with the larger model (18 October 2026, builds 34 to 37)

Sources: runs `81`, `84`, `85`, `86`, `87` and `88` on `ci` (`runs/engines/<run>-big-mac-ws` and `<run>-big-linux`), from the trial branches `run/engines/bigwm-1` to `bigwm-6`. A branch named `run/engines/bigwm-<label>` builds the pages named in `ci/engines/wm-variants.txt` on the build machine (`main` is a build of `origin/main`; any other name is the pushed commit's page, which may read `?wm=<name>`), serves each on a port of its own so that nothing one kept is found by the next, and runs `test/engines/big.js` on each: in Playwright's WebKit 26.0 and in Safari 26.6.2 on macOS 26.6.2 (a machine with 7 GB of memory), and in Playwright's WebKit 26.0 (the WPE port) on Linux (`ci/engines/bigwm.sh`). The model is the live one, with the world's species rows in four parts (328 MB) and 675 MB in all. Its encoder was one file in four parts (310 MB) in build 34 (runs 81 and 84, and the fix of runs 85 to 87) and is a 2 MB graph with its weights in four parts (308 MB) from build 35 (`main` in runs 85 to 88, and the fix of run 88). `ci/engines/memwatch2.py` reads every browser process four times a second. On macOS it reads the physical footprint and the footprint's lifetime maximum, which the kernel keeps (`proc_pid_rusage`); the footprint is the figure iOS counts against an app's memory limit (Apple, WWDC 2018 session 416, "iOS Memory Deep Dive"). On Linux it reads the resident size and its peak (`VmHWM`). `ci/engines/bigwmsum.py` prints the tables. The trial pages of runs 81 and 84 put marks of each step of the load, with the size of the runtime's heap, in `window.__wm`.

### Two corrections to the earlier figures

- The figures above this section are resident sizes read with `ps`. On macOS the system compresses pages a process has not touched lately; they leave the resident size and stay in the footprint. In run 81, Safari's largest process peaked at 1,703 MiB resident and 2,993 MiB of footprint on the same first visit, and the kernel's record of its peak said 3,348 MiB. The earlier figures for WebKit and Safari are lower bounds for what an iPhone would count.
- `test/engines/big.js` took a census of the caches after the model was ready and again on the later visit (`cachesNow` in `big_page.js`). In WebKit a kept body that is matched with `cache.match()` is brought into the page's memory, so the census itself added about 470 MiB to the Linux web process in run 81. `NOCACHES=1` now skips it, and runs 84 to 88 were made without it.

### What the measurements show

- The page read the encoder's four kept parts from Cache Storage, joined them into one buffer, checked the whole's checksum and handed the buffer to the worker. In Linux WebKit the web process rose from 1,015 MiB to 2,713 MiB while the parts were read (run 81). The worker then copied the buffer into the runtime's heap, which grew to 818 MiB for a model of 310 MB while the session was made.
- The hand-over itself is a move: the page's buffer reads 0 bytes after `postMessage` in WebKit and Safari.
- The runtime's heap is 818 MiB once the session is made, in every variant of build 34, and it did not grow while photos were answered. On macOS `vmmap` shows no region of its own for it; the region "WebKit Malloc", where WebKit's own allocations are counted, grew by about that much while the session was made. JavaScript's buffers are the region "JS VM Gigacage".
- At the end of the load in Playwright's WebKit on macOS (run 81, `vmmap`), build 34's page held 1,359 MB in "WebKit Malloc" and 714 MB in "JS VM Gigacage". With the encoder read by the worker straight into the heap the figures were 1,244 MB and 258 MB.
- The web process ran 16 to 24 threads on macOS and 37 to 42 on Linux in every variant. The runtime runs one thread (`numThreads` 1, since the page is not cross-origin isolated), so threads do not explain the memory.
- Build 35's external-data form, with its weights still read into the page and handed over, peaked about as high as build 34 in WebKit (`main` in runs 85 to 88), as run 53 had found on 11 October.

### What each change did, one at a time (build 34)

The peak of the largest web-content process on the first visit, in MiB: the footprint and, in brackets, the kernel's lifetime maximum on macOS; the resident size and, in brackets, `VmHWM` on Linux. Run 81 still had the census; run 84 did not. The answers were the same in every variant and engine.

| Change | Safari (81) | Safari (84) | WebKit, macOS (81) | WebKit, macOS (84) | WebKit, Linux (84) |
|---|---:|---:|---:|---:|---:|
| None (the page of build 34) | 2,993 (3,348) | 3,116 (3,151) | 2,958 (2,958) | 2,346 (2,346) | 2,713 (2,882) |
| `nodig`: no checksum of the joined whole | 3,506 (3,508) | | 2,948 (2,949) | | |
| `xfree`: every buffer let go with `transfer(0)` once used | 3,141 (3,146) | 2,120 (2,156) | 2,895 (2,896) | 2,222 (2,227) | 2,667 (2,671) |
| `keys`: presence asked with `cache.keys()`, which returns no body | | 3,311 (3,311) | | 3,241 (3,241) | 2,678 (2,678) |
| `wheap`: the worker reads the encoder's parts from Cache Storage straight into the runtime's heap, and the runtime makes the session from there without copying it | 2,059 (2,107) | 1,926 (1,929) | 2,685 (2,685) | 1,884 (1,885) | 2,440 (2,441) |
| `wkeys`: `wheap` and `keys` | | 1,772 (1,849) | | 1,927 (1,936) | 2,423 (2,424) |

The same page measured twice on macOS differed by as much as 600 MiB between runs (build 34's page in WebKit: 2,958 and 2,346 in runs 81 and 84), so only a change that holds in every run counts. `wheap` lowered the peak in every run and engine; `nodig`, `xfree` and `keys` did not do so consistently. Reading the species rows in the worker as well lowered the peak a little further (run 86: Safari 1,909 to 1,799, WebKit on macOS 1,945 to 1,821, Linux 2,466 to 2,397).

### The cause, as far as the evidence shows it

The encoder's 310 MB passed through JavaScript on their way into the runtime's heap. In WebKit a kept body that the page matches is brought whole into the web process (the census of the caches alone added about 470 MiB), and what the page read stayed in the process's footprint through the load, beside the joined buffer and then beside the heap the runtime filled from it. When the bytes stay out of JavaScript the peak falls by about 900 to 1,200 MiB in Safari, 600 MiB in WebKit on macOS and 500 MiB on Linux (runs 85 to 88), which is two to four times the encoder's size. Letting buffers go by hand (`xfree`) did not do as much, which suggests that the copies that mattered were WebKit's own, behind the kept bodies, and out of JavaScript's reach; that is an inference, since no breakdown separates them. Chromium was not measured in these runs. The rest of the footprint is needed by the design: the runtime's heap (818 MiB for the single file, which never shrinks), the species rows (328 MB, which the worker scores every photo against), the species table and the place files, and the page with the pocket model (about 400 to 750 MiB of footprint before and during the download).

### What shipped (build 37)

- The page asks whether a part is kept with `cache.keys()` (`has` in `src/cam.rec.js`), in `survey()`, `get()` and `staleParts()`; `staleParts()` in build 35 matched every kept part to learn that it was there.
- The worker reads the larger model's parts from Cache Storage itself, one chunk at a time (`readParts` in `vendor/rec-worker.js`). A single-file encoder goes straight into a block of the runtime's heap, and the runtime makes the session from that block: it takes a model that already lies in its heap without copying it, and frees the block once the session is made (`intoHeap`; the runtime's module object is noted when it first sets its view of the heap, and the runtime is started first with a model of 67 bytes so that the heap exists). Weights of their own (the live form) go into one buffer of the worker, handed to the runtime as its external data and let go with `transfer(0)` as soon as the session is made. The species rows in parts go into the worker's memory. The page never holds these bytes.
- The first load after a download checks each whole against the manifest's checksum as before. The worker works it out as the parts stream in, with a streaming SHA-256, because WebCrypto needs the whole in one buffer and a block of the runtime's heap is shared memory, which `digest()` refuses. A mismatch fails as damaged and the page lets every part go (`check_rec.js large`, `badWhole`).
- If the worker cannot read the parts (no store in the worker, no access to the runtime's heap, a part gone), the page loads them as before, once.

The page of `main` against the page with these changes, on the same machines and the same model, in MiB: the highest sample of the largest web-content process, with the process's own record of its peak in brackets where there is one. The later visit is a reload of the page with the model kept.

| | `main` (build 35), first visit | Build 37's page, first visit | `main`, later visit | Build 37's page, later visit |
|---|---:|---:|---:|---:|
| Safari 26.6.2, macOS: footprint (the kernel's lifetime maximum on the first visit) | 2,946 (2,947) | 1,564 (1,761) | 2,302 | 1,722 |
| WebKit 26.0, macOS: footprint (lifetime maximum) | 2,460 (2,467) | 1,729 (1,976) | 2,628 | 1,773 |
| WebKit 26.0, Linux: resident size (`VmHWM`) | 2,938 (2,981) | 2,166 (2,170) | 3,263 (3,348) | 2,322 (2,327) |

These are run 88. The first-visit peaks fell by 1,186 MiB in Safari, 491 MiB in WebKit on macOS and 811 MiB on Linux, counting each process's own record of its peak, which also catches what falls between two samples. The first two changes, and then all of them, on build 34's single-file form (runs 85 to 87) gave 1,758 to 1,913 MiB in Safari, 1,821 to 1,974 MiB in WebKit on macOS and 2,397 to 2,466 MiB on Linux, against 2,612 to 2,973, 2,523 to 2,605 and 2,916 to 2,994 MiB for `main`.

Every engine named the same species with both pages in every run (a Little Blue Heron, an American Bird Grasshopper, a Green Treefrog, and on the Apple engines the plant as Small-Flower Pawpaw). Checked: `test/rec/check_rec.js` in every section, `test/rec/check_ext.js`, `python3 build.py --check`, `node test/check4.js try`.

What this does not settle: no iPhone has run the larger model, and the simulator borrows the Mac's memory. With the fix the footprint still peaks near 1.7 to 1.9 GiB on macOS. The page's own test of whether a device can hold the model (`bigFits`) still assumes a peak of 2,600 MiB. The next levers are the pocket model's worker, which stays alive beside the larger one, and the species table, which the page parses into one object a species. The runtime's loader asks for a shared memory with a maximum of 4 GiB. That reserves address space, which the footprint does not count; a phone has less address space, and a smaller maximum was not tried.

On 18 October 2026 (build 38) the page stopped offering the full database on iPhones, iPads and iPods until a real iPhone has run it (`bigFits` in `src/cam.rec.js`, `by: 'ios-untested'`). iOS ends a tab that passes its memory limit, and neither the simulator, which borrows the Mac's memory, nor a granted 1 GiB heap shows where that limit lies, so an iPhone could download the model and then lose the page. The page knows such a device by its user agent (iPhone, iPad or iPod) or by a Mac's user agent with more than one touch point, which is what iPadOS sends when it asks for desktop sites. The owner lifts the gate for a test on a real iPhone with `?bigios=1`, which the browser keeps until `?bigios=0`. Playwright's WebKit gives a Mac's user agent on Linux and on macOS (`ua` in `runs/engines/88-big-linux/fix/big-webkit.json` and `runs/engines/88-big-mac-ws/fix/big-webkit.json` on `ci`), and the checks give its pages touch, so the checks and probes that run the model in WebKit or an iPhone simulator now open the page with `bigios=1` (`test/rec/check_rec.js` in WebKit, `test/engines/big.js`, `test/engines/resume_probe.js`, `ci/native/ios.sh`). How many touch points WebKit reports there was not checked, since this sandbox has only Chromium.

## The larger model in Firefox (18 October 2026)

Sources: runs `92`, `94`, `95`, `96` and `97` on `ci` (`runs/engines/<run>-ffx-<variant>`), from the trial branches `run/engines/ffx-1`, `ffx-p1`, `ffx-g1`, `ffx-s1` and `ffx-v1` (commits `32b4d2a`, `5397639`, `8d8977f`, `b787399` and `b883790` on `agent/firefox`). A branch named `run/engines/ffx-<label>` starts the job `ffx` (`ci/engines/ffbench.sh`), which gives each variant a fresh `ubuntu-latest` machine with four cores. Most variants open `test/engines/ffbench.html`, which runs ONNX Runtime Web 1.30.0 in a worker with the page's settings (the `wasm` backend, one thread, graph optimization `all`) on the pocket model (one file of 41 MB) and on the larger model (a 2 MB graph and 308 MB of weights from `raw.githubusercontent.com`). It runs one fixed input five times through the pocket model and twice through the larger one, and reports the time to make the session, the time of each run, and the first six values of the answer with a weighted sum of all of them. A Firefox "started by hand" is launched from the shell on a fresh profile with no automation attached, and the page posts its figures to `ci/engines/serve.py`.

### What the earlier figure measured

Run 39 timed Playwright's own build of Firefox 142, which `test/engines/big.js` drives. That build runs WebAssembly at a fraction of the speed of Mozilla's build of the same release, whether Playwright is attached or not. On one machine (run 96, `same-3`, an AMD EPYC 9V45), in milliseconds:

| Browser, and how it was started | Pocket model: session | Pocket model: five runs | Larger model: session | Larger model: two runs |
|---|---:|---:|---:|---:|
| Chromium 141 (Playwright's build), through Playwright | 330 | 250, 207, 205, 202, 208 | 820 | 2,846 and 2,698 |
| Firefox 142 (Playwright's build), through Playwright | 605 | 3,842 to 3,971 | 2,379 | 44,525 and 44,527 |
| The same Firefox 142, started by hand | 568 | 3,802 to 3,912 | 2,291 | 44,137 and 44,056 |
| Firefox 157 (the machine's own), started by hand | 439 | 291, 294, 298, 251, 255 | 752 | 2,816 and 2,799 |

All four gave the same answer to every digit reported, for both models. Mozilla's own builds of ten releases from `archive.mozilla.org` (140 ESR, 142, 143, 144, 146, 148, 150, 152, 154 and 156) and the machine's own Firefox 157, each started by hand on one machine (run 97, `vers`, an AMD EPYC 7763), ran the pocket model in 362 to 677 ms a run, each faster at its fourth run than at its first. Playwright's build of 142, started by hand on the same kind of machine (run 97, `vers-pw`), took 6,216 to 6,307 ms a run, and the same when its `user.js` asked for the optimizing compiler.

### Where the time went in Playwright's Firefox

- Nothing the page chooses changed it (run 92, each variant on a machine of its own). Graph optimization `disabled`, `basic` or `extended`, the runtime's bytes handed over as the page hands them (`wasmBinary`), a headed window against a headless one, and the preference `javascript.options.wasm_lazy_tiering` turned off all left the pocket model at 3.8 to 6.4 s a run, the spread being that of the machines. The levels `disabled` and `basic` also change the answer; `extended` gives the same answer as `all`.
- With its baseline compiler turned off (`javascript.options.wasm_baselinejit` false), Playwright's Firefox could not start the runtime at all and said "no WebAssembly compiler available". With its optimizing compiler turned off it ran as slowly as with the defaults (6.2 to 6.3 s). In that build, then, the optimizing compiler for WebAssembly is out of use, and every function runs as the baseline compiler made it. Why the build is so was not found; its `playwright.cfg` sets nothing about WebAssembly or the JIT.
- WebAssembly SIMD is present in every Firefox tried. Relaxed SIMD is missing in 142 and present in 157, and it makes no difference here, since the runtime's WebAssembly file uses no relaxed SIMD instruction (`wasm-opcodecnt` from WABT 1.0.36 counts none; its one dot product is `i32x4.dot_i16x8_s`).
- Threads were tried in Playwright's Firefox with the bench served cross-origin isolated (COOP and COEP headers from the test server) and four threads: the pocket model took 1.8 to 2.0 s a run and the larger model 21.6 and 21.9 s (run 92, `ff-coi`), about twice as fast as one thread on a machine of the same kind. GitHub Pages cannot send those headers, and threads were not tried in Mozilla's builds.

### The page's own flow in Firefox with no automation

In run 95 (`ff-page`) the job served the page of this commit (build 37) and started the machine's Firefox 157 by hand, headed on Xvfb, on a copy of the page that drives itself with `test/engines/big_page.js`: the offer under the heron photo, "Get it", then four photos. The larger model was downloaded in 18.5 s and was ready 39.1 s after "Get it", 20.6 s after the last byte (4.9 s for the species rows, 6.5 s to make the session and 8.3 s for the first run). The photo in hand was answered 9.4 s after the model was ready, and each of the four photos took 9.7 to 10.0 s from being chosen to the larger model's answer, of which the pocket model took 0.63 to 0.67 s. The three animals got the names that WebKit and Safari gave them in run 88 (Little Blue Heron at 0.992, American Bird Grasshopper at 0.929, Green Treefrog at 0.998). The plant was left unnamed, with Small-Flower Pawpaw first at 0.80, under the level for a name; the Apple engines named it.

### What this changes

On these machines Firefox, as Mozilla builds it, answers with the larger model about as fast as Chromium. The page needs no change for Firefox, and `bigFits` goes on offering Firefox the full database where a 1 GiB heap is granted. The figures for Firefox in the build 8 table above came from Playwright's build. The Firefox runs of `test/rec/check_rec.js` use the same build; that the three failing sub-checks of `large` in Firefox were waits of this kind is likely and was not checked. A Firefox figure from a build machine should come from Mozilla's build started by hand: `run/engines/ffx-g<label>` for the page's flow, and `ffx-s<label>` or `ffx-v<label>` for the runtime alone. No real device has run Firefox with the larger model.

## Home screen

Chromium 141 against the live address (`runs/engines/40-big-linux`): the browser reports no reason against installing; the manifest gives the name "Seen Back", a standalone display, and icons of 192 and 512 pixels with a maskable one. Installing on a phone has not been tried.

## Native shells (an experiment; nothing is in a store)

Sources: `runs/native/1-android` to `7-ios`, and `native/README.md`.

| Shell | Where it ran | Self-test | Pocket model | Larger model |
|---|---|---|---|---|
| Android WebView app, debug build, 54 MB as published | Android 14 emulator, WebView 113 | 98 of 98 | ready in 7.5 s; 0.5 to 1.9 s a photo | fetched, kept and run; 22 to 29 s a photo on the emulator; the WebView's process peaked at 1,585 MB |
| iPhone WKWebView app, built for the simulator | iPhone 17 simulator, iOS 26.5 | 98 of 98 | ready in 1.7 s; 0.5 to 0.65 s a photo | fetched, kept and run (7.5 to 10 s a photo) once the app serves the page from a small http server of its own on 127.0.0.1; found again after the app is closed and reopened (`runs/native/7-ios`) |

The Android file is published for trying on one's own phone: `seen-back-debug.apk` on the branch `pub/app-android`, with `built.json` (the commit, the page's build, the file's bytes and checksum) and a README beside it. It is signed with a throwaway key made on the build machine, it is not a store release, and a newer file cannot be installed over an older one without removing the app first. Before a file is published, the page's self-test runs in the emulator on a twin of it that carries the test photos (`runs/native/6-pub`).

The simulator has no camera; the shell's camera request was granted and the page showed the simulator's test pattern. Neither shell has run on a real phone.
