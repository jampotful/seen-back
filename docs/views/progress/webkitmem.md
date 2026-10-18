# Progress: webkitmem (where WebKit's memory goes with the larger model)

Track `webkitmem`, branch `agent/webkitmem`, started 18 October 2026, 16:43 US Eastern. Brief: `docs/HANDOFF.md` and `docs/ENGINES.md` ("Memory of the larger model").

## Done

- Read the brief, `ci/engines/big.sh`, `test/engines/big.js`, `big_page.js`, the page's load path (`src/cam.rec.js`, `vendor/rec-worker.js`) and run `53-big-mac-ws` on `ci`.
- In run 53 (the external-data form, macOS) the largest WebKit process rose from about 780 MiB at the end of the download to about 1,890 MiB at "ready", and stayed near 1,950 to 2,050 MiB while photos were answered. The download itself added little.
- Trial tooling on the local branch `wm-exp`, pushed as `run/engines/bigwm-1` (`8fdca7e`) and `run/engines/bigwm-2` (`a424015`), not for `main`: `ci/engines/bigwm.sh` serves the commit's page on the build machine and runs `test/engines/big.js` once for each variant in `ci/engines/wm-variants.txt`; `ci/engines/memwatch2.py` samples each process's footprint and own peak four times a second; marks of each load step land in `window.__wm`; `ci/engines/bigwmsum.py` prints the tables.
- Run 81 (`runs/engines/81-big-linux`, WebKit 26.0 on Linux, WPE): all four variants (base, nodig, xfree, wheap) named the same species. The transfer of the model to the worker is a move (the page's buffer reads 0 bytes after `postMessage`). The runtime's heap is 818 MiB after the session is made, with or without the zero-copy path. The web process rose from about 1,015 MiB to 2,713 MiB while the page read the four kept parts into one buffer (base); nodig and xfree did not lower that step; wheap (the worker reads the parts straight into the runtime's heap) lowered the climb to ready from 2,713 to 2,307 MiB. The harness's own census of the caches (`cachesNow` in `big_page.js`) added about 470 MiB after ready, because WebKit reads a kept body into the page on every `match`; trial 2 turns that census off.

## Next

- Read runs 81 (macOS, WebKit and Safari) and 84 (trial 2: base, keys, wheap, wkeys, xfree with no census).
- If a variant lowers WebKit's peak substantially, make it the page's only path on `agent/webkitmem`, run `test/rec/check_rec.js`, `python3 build.py --check` and `node test/check4.js try`, and write the dated section in `docs/ENGINES.md`.
