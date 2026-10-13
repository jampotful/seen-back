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

## Next
1. Copy the floor results from the `ci` branch into `docs/views/floor.json` when the run finishes.
2. Merge to `main` as build 24 once the try checks pass.
