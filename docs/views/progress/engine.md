# Progress: the engine track

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

# Burst 3 (started 13 October 2026, 12:01 US Eastern, from `main` at `d8f981f`; stops by 14:30)

## Plan
1. Module 2, `spectrum`; the clock, sun and moon of `light`; module 4, `pace`; module 5, `motion`. Each with sliders and `&draw=` options.
2. The jumper view uses them; specs for the views that wait on them.
3. The floor's second run recorded in `docs/views/floor.json`.

## Done (pushed to `agent/engine`)
- The floor: run 73 (from `run/engines/linux-floor-jumper2`) recorded in `docs/views/floor.json`; 56 jumper parameters in all. Its browser closed after `gaze.floor`, so parameters after that wait for a third run. A `verdict` block says which parameters research may stop refining for the jumper view (invisible on the still picture while still changing it): `params.cpd`, `zones.front.deg` (both), `zones.front.soft`, `zones.gaze.deg[1]`, `zones.fovea.cpd`, `zones.fovea.mag`. Eleven have a floor; 38 never changed the still render and wait for a moving clip.
- Module 2, `spectrum`: 3 by 4 matrices, `tools/views/pigments.py`, the wheel, the neutral band, dark adaptation (`docs/ENGINE.md`).
- Module 3's clock, sun and moon; module 4's replayed second; module 5's locked world and arm as the neck.
- Specs: jumper (neutral band, replay), snail (420 and 480 nm, dark adaptation), sealife (tonight's moon), and `trial` blocks on dog, bee and bird. The fourteen offered views are the same objects as on `main`.
- The tuning panel lists the new blocks' parameters.

## Next
1. Build 28 merged to `main` at about 14:15 after every check passed (see `docs/LOG.md`). The owner's phone checks are listed in `docs/STATUS.md`. The `try` check fails for the specs track's views on build 27 as on build 28; that track owns it.
2. Fungus waits on `slow` (module 12), not built. Cat, deer, rabbit, squirrel and insect have no pigment peaks in the logs yet; they get trials once research supplies them. No sheet gives a graded value for any of the fourteen offered views, so none was converted from `?`.
3. A third floor run for the parameters after `gaze.floor`, and a moving-clip floor.
4. Module 4's strobe and quarter-resolution ring; module 5's tilt, heading and knock side for `field` and `overlay`.
