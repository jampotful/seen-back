# Progress: everyday (burst 13, the species people photograph at home)

Prompt: `docs/tracks/prompts/burst13-everyday.md`. Branch: `agent/everyday`. Clone: `/home/claude/wt-everyday`.
The first agent started on 18 October 2026 at 19:02 UTC and handed off at 19:47 UTC, when its context passed 100,000 tokens. The second agent started at 19:46 UTC and merged build 34 to `main` at 20:31 UTC (`d99fbf68`, deployed by Pages).

## Done, pushed and merged

- Steps 1 to 4 as the first agent left them: `tools/species/EVERYDAY.md`, the list and its photos (`data/everyday/`), the build, pocket and manifest tools, the workflow, the page's `home` share, the Python prior, the `gotCloser` fix with its `kindOnly` check, and the typed names.
- `run/everyday/build-pub-1` succeeded (`runs/everyday/4-build` on `ci`) and every mark passed: kind right 97.1% and species right 75.6% in each photo's own zone, 97.1% and 76.4% in Alachua's, and world-test drops of 0.11, 0.26 and 0.23 points. Beta 30 was chosen.
- `pub/naturalist-everyday` at `dfc7154` is pinned as `pin/naturalist-everyday-dfc7154`, its files match `stage-parts.json`, and `models/naturalist/manifest.json` points at them.
- `run/everyday/pocket-1` succeeded (`runs/everyday/5-pocket`): the pocket's kind was right on 89.9% in the county's zone and 82.8% away.
- `BUILD` is 34 (`main` held 32 and `agent/hardening` 33). Hardening must take 35 or more when it merges.
- Checks at build 34: `build.py`, `--check`, `check4.js try`, every section of `check_rec.js` (`camera` passed on a second run after its first timed out under load), `check_make_slot.py` and `test_place.py`.
- Results in `tools/species/EVERYDAY.md`, the entry in `docs/LOG.md` and the everyday row in `docs/STATUS.md`.

## Open

- The dog: the kind was right on 9 of 20 photos, and 8 were named `Canis lupus`.
- Beta 30 is the largest value tried and the species right still rose at that step; a larger beta needs the world test run again.
- The pocket's county list names no species since build 21; adding these species there needs research-grade county records and a refit.
