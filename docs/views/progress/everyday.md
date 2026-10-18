# Progress: everyday (burst 13, the species people photograph at home)

Prompt: `docs/tracks/prompts/burst13-everyday.md`. Branch: `agent/everyday`. Clone: `/home/claude/wt-everyday`.
The first agent started on 18 October 2026 at 19:02 UTC and handed off at 19:47 UTC, when its context passed 100,000 tokens. The second agent started at 19:46 UTC with a limit of 150 minutes (22:16 UTC).

## Done and pushed

- Steps 1 to 4 as the first agent left them: `tools/species/EVERYDAY.md`, the list and its photos (`data/everyday/`), the build, pocket and manifest tools, the workflow, the page's `home` share, the Python prior, the `gotCloser` fix with its `kindOnly` check, and the typed names.
- `run/everyday/build-pub-1` succeeded (`runs/everyday/4-build` on `ci`) and every mark passed: kind right 97.1% and species right 75.6% in each photo's own zone, 97.1% and 76.4% in Alachua's, and world-test drops of 0.11, 0.26 and 0.23 points. Beta 30 was chosen.
- `pub/naturalist-everyday` at `dfc7154` is pinned as `pin/naturalist-everyday-dfc7154`, its files match `stage-parts.json`, and `models/naturalist/manifest.json` points at them (commit `fce6a161`).
- `run/everyday/pocket-1` succeeded (`runs/everyday/5-pocket`): the pocket's kind was right on 89.9% in the county's zone and 82.8% away.
- `origin/main` merged in; `BUILD` is 34 (hardening holds 33 on its branch), and the `kindOnly` comment says build 34.
- Results written in `tools/species/EVERYDAY.md`.
- Local checks at build 34: `build.py`, `--check`, `check4.js try`, `check_rec.js large`, `check_make_slot.py` and `test_place.py` passed. The other sections of `check_rec.js` were running at 20:13 UTC.

## Next

1. When every section of `check_rec.js` passes, fetch `main` and `agent/hardening` again, merge `main`, and set `BUILD` to the larger of theirs plus one if either passed 33.
2. Add the dated entry to `docs/LOG.md` and the everyday row to `docs/STATUS.md`, then merge to `main` and push.
