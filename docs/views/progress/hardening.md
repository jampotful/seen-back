# Hardening (burst 12) progress

Started 18 October 2026, 14:56 US Eastern, on `agent/hardening`. Stop by 17:55.

Pushed:
- Item 2 (`77e4feb`): `tools/world/nonlife.py`, `nonlife_make.py`, `NONLIFE.md`, `nonlife-report.json`. No rule ships.
- Item 3 (`429f081`, build 33): `bigFits` in `src/cam.rec.js`, `test/rec/fits_test.js` (18 cases pass), section `memory` of `test/rec/check_rec.js` (passes).

Running:
- Item 1 (done, nothing to fix): `test/check4.js` on fresh `main` (build 32), port 18765, `SLOW=3`, headless Chromium 141, software graphics, on a two-core machine shared with another agent (load 7 to 10). lex 2 s, lent 13 s, typed 20 s, record 103 s, viewer 67 s, edge 70 s, film 257 s, sweep 188 s, try (jumper, reef, shark, spider, 30 s each) 245 s, still 141 s and perf 728 s pass with no page error. floor did not finish within the 25 minutes given it (it bisects every scalar of jumper and had measured 20); that is the length of the measurement on this machine, and no check failed. sweep files a typed "mushroom" under plant eyes, which it records and does not assert. perf: 200 to 1,030 ms a frame for every view, mostly the machine's load.
- Item 4: `try` with all 44 specs for 3 seconds, on the scene clip and on the fake camera (`CAM=1`, new), with and without `OPTIONS=0`; then `perf` over every view. The `try` check now also measures the canvas and fails a view whose canvas is one flat color.
- The full `test/rec/check_rec.js` on build 33.

Prepared, not pushed: the lighter form of the larger model (`agent/rec-b`) on build 34 in a third worktree, with `check_ext.js` updated to today's wording; it ships only if `check_rec.js`, `check_ext.js` and the page's other checks pass.

Next: commit items 1 and 4, then the extra item, then fetch `main`, merge, check and merge to `main`.
