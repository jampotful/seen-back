# Burst 3: the engine's next modules (Opus)

Start with `burst2-common.md`. Your track is `engine`; continue from `docs/views/progress/engine.md` and `docs/ENGINE-DESIGN.md` (section 6 and the module table), starting from `main` (build 26 or later). Stop after 150 minutes.

1. Build module 2, `spectrum` (the colour channels from the animal's pigments, with the invented ultraviolet channel), then the clock, sun and moon parts of `light`, then module 4, `pace` (flicker and the animal's pace), then module 5, `motion` (the phone's motion sensors). Each gets its tuning sliders and a `&draw=` option for every way the atlas offers that is feasible on the web build, the default first.
2. Use the new modules in the jumper view, and write or extend specs for the views that wait on them (fungus needs `slow`, `motion`; bird, insect, bee and every dichromat need `spectrum`). Convert the fourteen existing views from grade `?` only where a sheet's graded statement gives the value.
3. Finish the visibility floor: read `run/engines/linux-floor-jumper2`'s results from the `ci` branch, record them in `docs/views/floor.json`, and say which parameters research may stop refining.
4. Every check passes before any merge to `main`; everything new stays behind `?try=`. Merge `main` in again before pushing. Never kill processes by name.

Final report, at most 300 words: what works on the live page with addresses, what needs the owner's phone, and your last commit.
