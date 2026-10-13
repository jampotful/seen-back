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
- Firefox (`runs/engines/39-big-linux/big-summary.txt`) kept and verified the model, and then spent 130.7 of its 146.9 seconds before "ready" in the first run of the model (8.3 s to make the session). The larger model then answered none of the three photos tried: each ended as "slow", and the pocket model took 11.4 to 11.9 seconds a photo beside it, where it took 0.6 to 0.7 in Chromium (`runs/engines/35-big-linux`). The page had closed by the time of the second visit, so that was not measured; no crash was reported. All of Firefox's browser processes together peaked at 3,028 MiB. An earlier attempt with the three browsers on one machine (`runs/engines/35-big-linux`) lost the Firefox page before its figures were read, and returned none.
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
