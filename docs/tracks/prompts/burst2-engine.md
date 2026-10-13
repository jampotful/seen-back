# Burst 2: the engine from the design (Opus)

Start with `burst2-common.md`. Your track is `engine`.

Read `docs/tracks/engine.md` (the code, the checks, the rules), `docs/ENGINE-DESIGN.md` in full, the entries 1, 4, 5, 7, 9, 10 and 12 of `docs/views/ATLAS.md`, and the parameter table in `docs/views/drafts/jumper.md`. Start from the branch `agent/engine`, which holds six commits that are not on `main` (several gazes per view, water colour, a sideways sweep, a shimmer, prototypes behind `?try=reef`, `?try=shark` and `?try=spider`, jumper colours from receptor fits). Merge `main` into it first, keep what fits the design, and work on `agent/engine`. Stop after 150 minutes.

Build in the order of the design's section 6.

1. **Module 0** with the spec checker. Convert the existing fourteen views to `views/<key>.json` by script with no change to the picture: every check in `test/check4.js` passes and the screenshots match before and after. The prototypes on `agent/engine` become specs too. Merge this step to `main` as soon as it passes, because a specs agent is writing `views/<key>.json` for the fourteen waiting groups on `agent/specs` at the same time and tests against your loader. Fetch `agent/specs` before your last merge and include every spec that passes the checker, reachable only with `?try=`.
2. **The tuning panel and the compare slider** (section 4), shown only with `&tune=1`.
3. **Modules `light`, `zones`, `spectrum`, `salience` and `gaze`**, and the jumper view as `views/jumper.json` from the parameter table, every value with the grade, source and `invented` flag the table gives.
4. **Drawing options.** The owner judges them by looking on a phone, so each is switchable with `&draw=`, the default first.
   - Gaze: the hunting strip with stamps of attention. Each past fixation stays as a sharp thumbnail where it was taken and fades over the measured time a place is ignored after a look (about 5 s). `&draw=strip` gives the strip alone, and `&draw=face` gives being looked at through the front camera.
   - Sharpness: the painted map. While a thumb is held on the screen the strip follows it, and when the thumb lifts the salience rule takes over again.
   - Colour: the strip carries the principal eyes' two classes and the surround the side eyes' single class. `&draw=palm` adds the ultraviolet felt in the hand (vibration on Android, a fine moving grain on iOS).
   - Surround: the coarse picture with movement glowing faintly. `&draw=pond` lets still things fade out.
   Mark in the spec what is invented.
5. **The visibility floor harness** (section 5), run on the jumper's parameters, on a build machine if the workflow pattern allows and otherwise locally on a few parameters, with results in `docs/views/floor.json`. The design cites a colour-difference threshold of 2.3 from memory; check it against a source you can reach, or mark it unverified.
6. **Checks.** Every existing check passes. `?try=jumper` draws with no GL errors, the gaze moves to a moving target in a test clip, and each `&draw=` option draws.

Merge to `main` when every check passes and today's views look the same; everything new stays behind `?try=`. Number the build as `docs/HANDOFF.md` describes. Report the frame times from the About block in headless Chromium for today's views and for `jumper`.

Final report, at most 300 words: what works on the live page, with the address for `?try=jumper&tune=1`; the frame times; what needs the owner's phone to judge (the design lists four phone checks); and your last commit.
