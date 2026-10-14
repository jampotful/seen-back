# Progress: the spec compiler (track `compiler`, burst 6)

Started 13 October 2026, 22:25 UTC; stopped at the time limit. Spend about $6 of the $12 (every batch and trial together, by the usage blocks at batch prices).

## Built and pushed (branch `agent/compiler`)
- `tools/views/compile.py` (commands plan, run, check, compare), `tools/views/test_compile.py` (offline tests of every check; they run in the job), six job files in `tools/views/compile/` (jumper, bee, primate, whale, scorpion, cephalopod), and the job `views-compile` (`.github/workflows/views-compile.yml`, `ci/views/compile.sh`, `ci/views/compile.env`). `docs/views/COMPILER.md` section 7 lists where the build differs from the design.
- The branch's first commit brings in build 31 (`agent/engine`) and the audit's verdicts (`agent/audit`), neither on `main` yet. Nothing was merged to `main` or written to `views/`.

## Results
- Drafts: branch `pub/views-draft`, one folder a run (`b1`, `b3`, `b4`, `b5`, `b6`), each with `<key>.<model>.json` (the spec), `.md` (the report), `.reply.json` omitted, and `COMPARISON.md`. The same files, with each attempt's errors, are on `ci` under `runs/views-compile/<n>`.
- Five finished batch runs (b1, b3, b4, b5 with two attempts, b6 with up to three; six views and two models each): Sonnet 5.5 passed every check for 26 of 30 view-runs, Haiku 5.5 for 6 of 30 (a third attempt fixed none of Haiku's four remaining views). Haiku's failures are mostly grades without a claim, an m row whose parameters are all i, and a colour matrix named but not defined.
- Against the hand-made jumper (58 parameters), a Sonnet draft carries 9 to 12 parameters, 5 or 6 of them in the hand-made spec; 2 or 3 of those have the same value (within 10%) and 4 or 5 of the 6 the same grade when the draft is checked. Against the hand-made bee (10 parameters, most graded `?`), a Sonnet draft carries 3 or 4, all in the hand-made spec.

## Not done
- Run-to-run variation is large (Sonnet passed 6, 5, 5, 4 and 6 of 6 views in the five runs), so one run's comparison with a hand-made spec is one sample.
- A colour matrix given by pigment peaks still needs a claim as well as the peak check; the claim is redundant and could be dropped.
