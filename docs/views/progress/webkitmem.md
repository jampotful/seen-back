# Progress: webkitmem (where WebKit's memory goes with the larger model)

Track `webkitmem`, branch `agent/webkitmem`, started 18 October 2026, 16:43 US Eastern. Brief: `docs/HANDOFF.md` and `docs/ENGINES.md` ("Memory of the larger model"). The findings are in `docs/ENGINES.md`, "Where WebKit's memory goes with the larger model (18 October 2026, builds 34 to 37)".

## Done

- Tooling: `ci/engines/bigwm.sh` (pages against each other on build machines, from `run/engines/bigwm-<label>`), `ci/engines/memwatch2.py` (each process's footprint and its own peak), `ci/engines/bigwmsum.py` (tables), and `NOCACHES=1` for `test/engines/big.js`.
- Trials: runs 81 (`bigwm-1`: base, nodig, xfree, wheap on build 34, with the harness's census of the caches), 84 (`bigwm-2`: base, keys, wheap, wkeys, xfree, with no census), 85 to 87 (`bigwm-3` to `bigwm-5`: main, which had become build 35, against the fix on build 34) and 88 (`bigwm-6`: main against the fix on build 35). The trial pages with the variants and the marks of each load step are on the local branch `wm-exp`, pushed as `run/engines/bigwm-1` and `bigwm-2`.
- The fix on build 34 (`298d24c`, `ee8bca9`, `60517a4` on `agent/webkitmem-rows`) and on build 35 (`c0a3e53` on `agent/webkitmem-35`), which became build 37.
- Checks on this machine: on `c0a3e53`, `check_ext.js` (20 of 20) and `check_rec.js` in every section (ports 8882 and 8888); on the build 37 tree, `check_rec.js large` again with the parts on port 8788, so that its `kindsHead` part ran too, `check4.js try` after the last merge of `main`, and `build.py --check`. Merged to `main` as build 37 (`04d2246`).

## Next

- An iPhone. The pocket model's worker while the larger one runs, and the species table's objects, are the next things to measure. `bigFits` still assumes a peak of 2,600 MiB.
