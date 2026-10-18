# Hardening (burst 12) progress

Started 18 October 2026, 14:56 US Eastern, on `agent/hardening`. Stop by 17:55.

Pushed:
- Item 2 (`77e4feb`): `tools/world/nonlife.py`, `nonlife_make.py`, `NONLIFE.md`, `nonlife-report.json`. No rule ships.
- Item 3 (`429f081`, build 33): `bigFits` in `src/cam.rec.js`, `test/rec/fits_test.js` (18 cases pass), section `memory` of `test/rec/check_rec.js` (passes).

Running:
- Item 1: `test/check4.js` on fresh `main` (build 32), port 18765, `SLOW=3`, headless Chromium 141, software graphics. lex, lent, typed, record, viewer, edge, film, sweep, try and still pass; floor and perf are running. Nothing has failed so far.
- Item 4: `try` with all 44 specs for 3 seconds, on the scene clip and on the fake camera (`CAM=1`, new), with and without `OPTIONS=0`; then `perf` over every view. The `try` check now also measures the canvas and fails a view whose canvas is one flat color.
- The full `test/rec/check_rec.js` on build 33.

Prepared, not pushed: the lighter form of the larger model (`agent/rec-b`) on build 34 in a third worktree, with `check_ext.js` updated to today's wording; it ships only if `check_rec.js`, `check_ext.js` and the page's other checks pass.

Next: commit items 1 and 4, then the extra item, then fetch `main`, merge, check and merge to `main`.
