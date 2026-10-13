# Track C: the picture engine and new effects

Read this whole file, then `docs/HANDOFF.md` and `docs/CONTRACTS.md`.

## What the owner asked for

Views that are "accurate, beautiful, and dynamic", built from evidence, with new effects and new ways of drawing welcome. On technology: "deploy absolutely every technology you need … spare no expense … just make sure that when you incorporate the new tools, they get optimized so that the app still runs smooth as butter." On size: as large as needed, provided the app runs "beautifully and responsively", with "clever workarounds for compressing information" where needed.

On jumping spiders, the owner passed on a specialist's account: the two large front eyes see colour (ultraviolet among it), the smaller side eyes act more like motion detectors that inform the whole picture, nobody knows exactly how the eyes' information comes together, and an ordinary scene for a jumping spider is something like Times Square, full of signals calling for attention. The owner asked for great care before drawing anything as a split view. `docs/views/drafts/jumper.md` turns the evidence so far into one continuous frame.

## Your machine and your branch

The cloud machine can be replaced without warning, and a replacement deletes everything on it. Clone with `git clone --depth 1 https://github.com/jampotful/seen-back /home/claude/seen-back` (allow ten minutes), work on the branch `agent/engine`, and push it (`git push origin HEAD:refs/heads/agent/engine`) within 15 minutes and then at least every 30 minutes. Commit as `git -c user.name=Claude -c user.email=noreply@anthropic.com commit` with your session's attribution lines. Never push to `main`, and leave `BUILD` in `src/cam.a.js` alone: the app's own thread merges your branch, gives it a build number and checks it on the owner's phone. Before each push, `git fetch origin main` and rebase onto it if it moved.

## The code

`build.py` joins `src/` into `index.html`, `sw.js`, `selftest.js` and `dist/seen-back.artifact.html`; run `python3 -I build.py` after every change and commit the built files with the sources. The views are `EYES` in `src/cam.a.js`, read through `paramsOf` and blended by `mix`. The engine is `src/cam.b.js`: WebGL2, three passes (a ring of past camera frames, a time pass for trails, held gazes and slowed moments, and a space-and-colour pass). The flow is `src/cam.c1.js` and `src/cam.c2.js` (`setEyes` changes the view).

Checks, in headless Chromium (`/opt/pw-browsers`, Playwright in `/opt/node-tools/node_modules`):

```
python3 -I -m http.server 8785 --bind 127.0.0.1 &          # from the repository root
NODE_PATH=/opt/node-tools/node_modules PORT=8785 node test/check4.js typed   # also lex, record, lent, viewer, edge, sweep, film
node test/rec/serve.js 8786 &
PORT=8786 BIG_PORT=8789 SVC_PORT=8790 NODE_PATH=/opt/node-tools/node_modules node test/rec/check_rec.js   # every section; takes a while, run it in the background
```

All of them pass on `main` at build 22, and all must still pass on your branch.

## What to build, in this order

1. **Measure first.** A frame-time probe: GPU time through `EXT_disjoint_timer_query_webgl2` where the browser offers it, and frame intervals otherwise, shown in the About sheet's block. A `perf` mode in `test/check4.js` that runs every view for a fixed number of frames on a fixed clip and prints a table. Headless software rendering is slow, so its numbers are only for comparing views and changes with each other.
2. **General, data-driven engine fields**, each documented in a new `docs/ENGINE.md` with the evidence it serves:
   - *Zones*: up to four regions in one view (strip, ellipse, annulus, band or the whole field), each with its own sharpness, colour matrix, saturation, pace, motion gating and gain, blended with soft edges in a single pass.
   - *Salience*: a small motion-energy map (about 64 by 64) from differences in the frame ring, with the phone's own movement removed (from the mean motion of the image, or from the motion sensors), and a cue for the motion of living things: local motion that is coherent over a small patch and changes rhythmically.
   - *Gaze*: a controller that moves a zone to the most salient place outside an inhibition-of-return mask, with a fast jump, a dwell, small scanning sweeps (jumping spider retinas scan; see the log), and a mask that fades over about five seconds (Ferrante et al. 2024 in the log). Read the map back asynchronously (a pixel buffer and a fence in WebGL2) at a few reads a second, so the frame never waits.
   - *Phone inputs*: device motion and orientation (iOS asks for permission on a tap, through `DeviceMotionEvent.requestPermission`) for the phone's own movement; the microphone, with the person's consent asked in plain words first, mapped to ripples for creatures that sense vibration and air movement. Each input stays behind a flag until the app thread turns it on, and nothing asks for a permission without the person's own action.
3. **The `jumper` view** from `docs/views/drafts/jumper.md`, reached with `?try=jumper` and offered nowhere else yet: the surround coarse and green, with motion glowing; living motion brighter in the front 100 degrees; a narrow, sharp, coloured gaze strip that jumps to the strongest glow, scans it and holds, while the surround forgets that place for about five seconds; colour per genus; an invented ultraviolet false colour; twitching of the gaze in bouts when the phone lies still in the dark. Its rows can be placeholders graded `i`; the research thread writes the real rows.
4. **Then, as time allows**, prototypes of the strongest effects proposed in `docs/views/sheets/*.md` and in the drafts that arrive on the `research/*` branches (`git fetch origin 'refs/heads/research/*:refs/remotes/origin/research/*'`), each behind `?try=<group>`.
5. **Optimize.** Keep every view's frame time near today's; reuse framebuffers; no synchronous reads; lower the salience map's size before lowering the picture's. Respect `prefers-reduced-motion`. No new network requests at run time; vendor any library under `vendor/` with its licence.

Anything a person reads follows the writing rules in `docs/views/research/BRIEF.md` ("How the rows are written").

## Your report

At most 400 words: what you built, the frame-time table before and after, what needs a real phone to judge, and the commit you pushed last. Put screenshots (small PNGs) in `test/shots/engine/` and name them in the report.
