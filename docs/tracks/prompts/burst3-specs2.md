# Burst 3: the rest of the specs, and the specialist's sheet (Sonnet)

Start with `burst2-common.md`. Your track is `specs`; continue from `docs/views/progress/specs.md` on `agent/specs` (last commit `6db59e1`) and from `docs/tracks/prompts/burst2-specs.md`, whose steps stand. Seven groups have specs (fungus, slime, fish, shark, spider, snail, sealife), and the engine track has merged module 0 into `main` (build 26, `views/<key>.json`, a checker run by the build). Merge `main` into `agent/specs` first and keep the engine track's own shark and spider specs, which keep the prototypes' effects. Stop after 100 minutes.

1. Write specs for crab, mammal, salamander, worm, bat, tick and flying fox, from their sheets and drafts as the progress note says.
2. Run the build's checker on every spec, then render each with `?try=<key>` in headless Chromium and confirm no GL errors. Merge the passing specs to `main`, reachable only with `?try=`.
3. Write the jumper review sheet `docs/views/review/jumper.md` and its PDF, and upload it to Drive as `burst2-specs.md` step 4 says. The Drive folder id is in your launch prompt only.

Final report, at most 250 words: the specs merged, the groups needing a new mechanism, the PDF's place in Drive, and your last commit.
