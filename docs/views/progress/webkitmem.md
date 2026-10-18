# Progress: webkitmem (where WebKit's memory goes with the larger model)

Track `webkitmem`, branch `agent/webkitmem`, started 18 October 2026, 16:43 US Eastern. Brief: `docs/HANDOFF.md` and `docs/ENGINES.md` ("Memory of the larger model").

## Done

- Read the brief, `ci/engines/big.sh`, `test/engines/big.js`, `big_page.js`, the page's load path (`src/cam.rec.js`, `vendor/rec-worker.js`) and run `53-big-mac-ws` on `ci`.
- In run 53 (the external-data form, macOS) the largest WebKit process rose from about 780 MiB at the end of the download to about 1,890 MiB at "ready", and stayed near 1,950 to 2,050 MiB while photos were answered. The download itself added little.

## Next

- A sampler that reads each process's own peak (macOS: physical footprint and its lifetime maximum; Linux: VmHWM and a breakdown from smaps) and marks inside the page and worker at each load step.
- Trial branches `run/engines/bigwm-*` that serve this branch's page on the build machines and try one change at a time in WebKit and Safari.
