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
- `large` in WebKit is the page's fault, and it is open. A reload while the larger model's second part is arriving makes the page fetch the first part again, although it had been kept, and when all parts are in the page fails with "a part is no longer kept on this device" (`runs/engines/38-linux-firefox-webkit/rec/resume-webkit.json`). Chromium resumes and finishes in the same test. A download that is not interrupted works in every WebKit tried (next section).
- Not yet explained: `damaged` in WebKit, `notsure` in WebKit on Linux, and three sub-checks of `large` in Firefox.

The live address (`runs/engines/34-live`): in Chromium, Firefox and WebKit the page loads as build 8, the service worker controls the first and second visits, and with the network cut the page starts and the pocket model is ready.

## The larger model, fetched from the live address through the page's own sheet (build 8)

Sources: `runs/engines/35-big-mac-ws` (Safari), `35-big-mac-sim` (iPhone simulator), `36-big-mac-ws` (WebKit, macOS), `36-big-linux` (WebKit, Linux), `40-big-linux` (Chromium). Memory is the resident size of the largest browser process, read with `ps` once a second.

| | Safari 26.6, macOS | Safari, iPhone 17e simulator | WebKit 26.0, macOS | WebKit 26.0, Linux | Chromium 141, Linux |
|---|---:|---:|---:|---:|---:|
| Download, "Get it" to last byte | 5.6 s | 9.9 s | 3.3 s | 2.3 s | 9.2 s |
| Ready to answer after "Get it" | 18.5 s | 38.9 s | 15.2 s | 10.6 s | 21.9 s |
| Seconds a photo (four photos) | 5.5 to 7.3 | 9.9 to 10.8 | 4.9 to 6.1 | 4.7 to 5.0 | 7.4 to 7.9 |
| Largest browser process at its peak | 2,077 MiB | 1,688 MiB | 2,178 MiB | 2,598 MiB | 1,501 MiB |
| All four parts kept and verified | yes | yes | yes | yes | yes |
| Fetched again after a reload | nothing | nothing | nothing | nothing | nothing |
| Tab died | no | no | no | no | no |

- The four parts come from `raw.githubusercontent.com` with status 200, no redirect, no compression, and a header that allows any origin. Each part's checksum, and the checksum of the four joined, matches the manifest.
- The iPhone simulator borrows the Mac's memory. A pass there does not show that a real iPhone holds the model.
- Firefox had not returned its figures when this was written (`runs/engines/39-big-linux`).
- The same four photos on every engine: a Little Blue Heron and a Green Treefrog named correctly; an American Bird Grasshopper right as the first answer and left unnamed, being under the level for a name; and one plant photo (Guinea Hen Weed) that sits on that level, named wrongly as Small-Flower Pawpaw by the three Apple engines and left unnamed by the other two.
- With the network cut after the model was kept, Chromium still started the page and the larger model still named the heron.
- After a reload with the larger model kept, the first photo's first answer took far longer than usual in Chromium (25 to 42 seconds before the pocket model answered). This is open.

## Memory of the larger model (laboratory, 11 October 2026)

Sources: `ci/lab/mem/results.json`, runs `lab/32` to `lab/35`.

| Form of the model | WASM heap | Renderer at its peak (headless Chromium, the page's worker) | Vectors against the shipped file |
|---|---:|---:|---|
| One 310 MB file (what build 8 and 9 fetch) | 821 MiB | 1,330 MiB | the same file |
| A 2 MB graph file with the weights beside it as a data file (`pub/model-bioclip2-l14-b`) | 429 MiB | 953 MiB | identical |

No setting of the runtime alone changes the heap without changing the answers. The second form needs a change in the page and its worker.

## Home screen

Chromium 141 against the live address (`runs/engines/40-big-linux`): the browser reports no reason against installing; the manifest gives the name "Seen Back", a standalone display, and icons of 192 and 512 pixels with a maskable one. Installing on a phone has not been tried.

## Native shells (an experiment; nothing is in a store)

Sources: `runs/native/1-android` to `5-ios`, and `native/README.md`.

| Shell | Where it ran | Self-test | Pocket model | Larger model |
|---|---|---|---|---|
| Android WebView app, debug build, 55.8 MB | Android 14 emulator, WebView 113 | 98 of 98 | ready in 7.5 s; 0.5 to 1.9 s a photo | fetched, kept and run; 22 to 29 s a photo on the emulator; the WebView's process peaked at 1,585 MB |
| iPhone WKWebView app, built for the simulator | iPhone 17 simulator, iOS 26.5 | 98 of 98 | ready in 1.7 s; 0.5 to 0.65 s a photo | fails while the page is served from the app's own address scheme (Cache Storage accepts only http and https addresses); works when the same app loads the page over http |

The simulator has no camera, so the camera inside the iPhone shell is untested. Neither shell has run on a real phone.
