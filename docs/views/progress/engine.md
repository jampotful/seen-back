# Progress: the engine track, burst 2

Started 13 October 2026, 09:31 US Eastern, on `agent/engine` with `main` merged in (no conflicts).

## Done (all pushed to `agent/engine`)
- Module 0: `views/<key>.json` for every view, `build.py` inlines them after `tools/views/check_spec.py` passes; `viewOf` in `src/cam.a.js`. The fourteen offered views are identical to build 23 field by field (`tools/views/same_views.js`) and pixel by pixel on a still photo (`node test/check4.js still`, against `main`).
- The tuning panel and the compare slider (`src/cam.tune.js`, `?try=<view>&tune=1`).
- `views/jumper.json` graded from the parameter table (`tools/views/grade_jumper.py`).
- Drawing options behind `&draw=`: stamps (default), strip, face; paint; two, palm; glow, pond.
- The light module's read-back (`LIGHT`) and curves against light.
- The floor harness (`node test/check4.js floor`, `tools/views/delta_e.py`), on a build machine through `run/engines/linux-floor-jumper1`; results return on the `ci` branch.
- Specs from `agent/specs` for fish, fungus, sealife, slime and snail included behind `?try=`. Its shark and spider are not taken: the prototypes' specs here keep their effects (salience, shimmer, sweep, ripples), which the specs track's drafts leave out.

- Build 26 merged to `main` (13 Oct, about 11:50): every check in `test/check4.js` (typed, lex, record, lent, viewer, edge, sweep, film, try, still) and every section of `test/rec/check_rec.js` passed on the merged build. `lent` failed three times and passed three times on the same page: it waits a fixed 1.2 s after a tap, which is short on a loaded machine.
- `docs/views/floor.json` holds the first floor run (engines run 72, 21 parameters of the jumper view, three values each).

## Next
1. A second floor run is on `run/engines/linux-floor-jumper2` (it skips the parameters already measured). Copy its `floor.json` from the `ci` branch (`runs/engines/<run>-linux-chromium/floor.json`) into `docs/views/floor.json` under `floor.jumper`, adding to what is there, and record the run in `runs`.
2. Parameters that act only on movement read as invisible on the still harness; a moving-clip version of the floor is the next step for them.
3. The specs track's shark and spider were not taken (the prototypes' specs keep their effects); reconcile the two when that track finishes.
4. Modules not built: `spectrum` (matrices from pigment peaks), the clock, sun and moon of `light`, and everything after `gaze` in the design's order.
