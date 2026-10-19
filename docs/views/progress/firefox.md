# Progress: firefox (the larger model's first answer in Firefox)

Started 18 October 2026, 19:04 US Eastern; merged to `main` at about 19:45. Time limit 120 minutes.

Done:
- A bench of the runtime alone (`test/engines/ffbench.html`, `ffbench_worker.js`, `ffbench.js`, `ci/engines/ffbench.sh`, the job `ffx` for `run/engines/ffx-*`), and a copy of the page that drives itself in a Firefox started by hand (`ff-page`).
- The cause: Playwright's own build of Firefox 142 runs WebAssembly about fifteen times slower than Mozilla's build of the same release, through Playwright or started by hand; with its baseline compiler off it has no WebAssembly compiler at all. Mozilla's builds of 140 ESR to 157 run at Chromium's pace with identical answers, and the page's flow in Firefox 157 was ready 39 s after "Get it". The figures are in `docs/ENGINES.md` (18 October, Firefox).
- No change to the page, so no new build number: `bigFits` keeps offering Firefox the full database. `docs/HANDOFF.md`, `docs/STATUS.md` and a comment in `ci/engines/big.sh` say so.
- Checked: `python3 build.py --check`, `node test/check4.js try` (port 8797), `node test/rec/fits_test.js`.

Still running at the merge: `ffx-g1` (`ff-pagepw`, the page's flow through Playwright) and `big-lx-firefox-base1` (the live page through Playwright). Neither can change the finding.

Next: a Firefox figure on a build machine comes from Mozilla's build started by hand (`run/engines/ffx-g<label>`); a real device with Firefox has not run the larger model.
