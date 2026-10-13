# Burst 4: the engine's remaining modules and the check fixes (Opus)

Start with `burst2-common.md`. Your track is `engine`; continue from `docs/views/progress/engine.md` and `docs/ENGINE.md` on `main` (build 28 or later). Stop after 150 minutes.

1. **The `try` check** fails for the views the specs track added (fish, tick, sealife, bat and others) because its "zone programs compiled" item is wrong for views without zones. Fix the check so that a view with no zones passes it, and make `lent` wait for the look to open instead of a fixed 1.2 s, so that it passes on a loaded machine.
2. **Module 12, `slow`** (growth time and long exposure, for the fungus view and the atlas's entries 7 and 24), with its tuning sliders and a `&draw=` option for each way the atlas offers that fits the web build. Then tilt and heading for the views that need them (atlas 2 and 21), the pigment peaks for cat, deer, rabbit, squirrel and insect in `tools/views/pigments.py` (find them in the sheets and logs, grep, and mark any without a source `invented`), and the third visibility-floor run for the parameters after `gaze.floor`, with a moving test clip for the parameters the still render could not move.
3. **Specs for the views these modules unlock.** Use the new modules in the fungus, cat, deer, rabbit, squirrel and insect specs, grade only what a sheet states, and keep every new view behind `?try=`.
4. Every check passes before any merge to `main`. Merge `main` in again before you push. Never kill processes by name.

Final report, at most 300 words: what works on the live page with addresses, what needs the owner's phone, and your last commit.
