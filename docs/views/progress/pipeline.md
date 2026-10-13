# Progress: the extraction pipeline (agent/pipeline)

Started 13 October 2026, 04:40 UTC. Stops at 75 minutes (about 05:55 UTC).

## Done
- Read STATUS, QUEUE, the brief, check.py, and the harvest job (found on `run/lit/t1`, not on `main`).

- Prices read (13 Oct): Haiku 5.5, `claude-haiku-5-5`, batch $0.05 in / $0.25 out per million tokens; cache read $0.005 (derived), 1 hour write $0.10 (derived).
- tools/lit/extract.py written (plan, run, collect, check) with stdlib only; tools/lit/test_extract.py passes (7 tests, no key needed).
- Plan on spider-night: 650 passages, expected $0.09, ceiling $0.25.

## Next
1. Calibration set up (agent records vs collection).  
2. Calibrate with the grep and format checks; the API part waits for the key.
3. Calibration against research/birds, cat-dog, ground-invertebrates.
4. .github/workflows/lit-table.yml and ci/lit/table.sh.

## Notes
- `tools/lit/harvest.py` and `ci/lit/*` exist only on `run/lit/t1`; `main` has `ci/put_branch.sh` and `ci/return.sh`.
- No ANTHROPIC_API_KEY in this session.
- The checkout at /home/claude/seen-back is shared with other agents (its branch changed under me); I work in a private clone.
