# Progress: the spec compiler (track `compiler`, burst 6)

Started 13 October 2026, 22:25 UTC. Time limit 120 minutes (to 00:25 UTC). Spend ceiling $12; the compiler's requests cost a few cents each.

## Done and pushed
- `tools/views/compile.py` (plan, run, check, compare), `tools/views/test_compile.py` (offline tests of every check), job files `tools/views/compile/<key>.json` for jumper, bee, primate, whale, scorpion and cephalopod.
- Job `.github/workflows/views-compile.yml`, `ci/views/compile.sh`, `ci/views/compile.env`. A push to `run/views-compile/<label>` runs it; drafts go to `pub/views-draft/<label>/`, the summary and the comparison come back on `ci`.
- The branch holds build 31 (from `agent/engine`) and the audit's verdicts (from `agent/audit`) in its first commit, since neither is on `main` yet.

## Next
- A first trial run in direct mode on jumper and bee, then a batch run, then the four views that have no spec (primate, whale, scorpion, cephalopod), then the comparison write-up.
