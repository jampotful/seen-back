# Progress: the extraction pipeline (agent/pipeline)

Started 13 October 2026, 04:40 UTC. Stops at 75 minutes (about 05:55 UTC).

## Done
- Read STATUS, QUEUE, the brief, check.py, and the harvest job (found on `run/lit/t1`, not on `main`).

## Next
1. Confirm Batch and cache prices.
2. tools/lit/extract.py
3. Calibration against research/birds, cat-dog, ground-invertebrates.
4. .github/workflows/lit-table.yml and ci/lit/table.sh.

## Notes
- `tools/lit/harvest.py` and `ci/lit/*` exist only on `run/lit/t1`; `main` has `ci/put_branch.sh` and `ci/return.sh`.
- No ANTHROPIC_API_KEY in this session.
