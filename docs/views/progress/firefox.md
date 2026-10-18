# Progress: firefox (the larger model's first answer in Firefox)

Started 18 October 2026, 19:04 US Eastern. Time limit 120 minutes.

Done:
- A bench of the runtime alone (`test/engines/ffbench.html`, `ffbench_worker.js`, `ffbench.js`, `ci/engines/ffbench.sh`, the job `ffx` for `run/engines/ffx-*`).
- Runs 92 (`ffx-1`), 94 (`ffx-p1`) and 95 (`ffx-g1`): Playwright's Firefox 142 runs the pocket model in 3.9 to 6.3 s and the larger model in 46 to 70 s a run, against 0.29 s and 3.9 s in Chromium, whatever the graph optimization level, the wasm bytes' path, the lazy-tiering pref or headed against headless; with the baseline compiler switched off it cannot start the runtime at all ("no WebAssembly compiler available"). The machine's own Firefox 157, started by hand with no automation, runs them in 0.35 to 0.52 s and 4.5 s, and the page's own flow there was ready 39 s after "Get it" and named all four photos (about 10 s each). Playwright's Firefox 142 binary started by hand is as slow as under Playwright.
- Answers identical in every variant at the page's optimization level (`all`); `basic` and `disabled` change them.

Pushed: all of the above on `agent/firefox`.

Next: run `ffx-v1` (Mozilla's builds of releases 140 ESR to 156 started by hand, and Playwright's build's default prefs) says whether Firefox 142 itself or only Playwright's build of it is slow; `ffx-s1` puts every browser on one machine. Then the dated section in `docs/ENGINES.md`.
