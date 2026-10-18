# Progress: iosgate (18 October 2026)

The task: until a real iPhone has run it, the page does not offer the full database on iOS or iPadOS (`bigFits` in `src/cam.rec.js`, `by: 'ios-untested'`), and the owner can lift the gate for a test with `?bigios=1`.

- Started 23:03 UTC from `main` at `e4bd36c1` (build 37), branch `agent/iosgate`.
- Done and pushed: the gate in `bigFits`, its facts (`ua`, `touch`, `iosTest`) passed in by `deviceNow()`, the switch `?bigios=1` kept under `seenback.bigios.v1` until `?bigios=0` (`iosTestNow`), the diagnostic line `no ios-untested`, build 38. Cases: `test/rec/fits_test.js` (34, 16 new) and four in the section `memory` of `test/rec/check_rec.js` (an iPhone, an iPad asking for desktop sites, an iPhone with the gate lifted, an iPhone played with `&bigmem=heap-yes`). The probes that run the model in WebKit or an iPhone simulator open the page with `bigios=1` (`check_rec.js` in WebKit only, `test/engines/big.js`, `test/engines/resume_probe.js`, `ci/native/ios.sh`). Documents: `docs/HANDOFF.md`, `docs/ENGINES.md`, `docs/CONTRACTS.md`, `docs/LOG.md`, the engine row of `docs/STATUS.md`.
- Checked in headless Chromium: `node test/rec/fits_test.js`, `check_rec.js memory` (twice), `python3 build.py --check`; an ad hoc check that the kept lift holds on a visit with no query and that `?bigios=0` removes it.
- Next: `node test/check4.js try`, then rebase on `main` and merge.
- Not checked: how many touch points Playwright's WebKit reports with `hasTouch` (this sandbox has only Chromium), and the build-machine probes themselves.
