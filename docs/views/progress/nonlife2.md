# Track nonlife2 progress

Started 18 October 2026, 19:04 US Eastern, on `agent/nonlife2` (prompt: the control room's, 18 October; read with `tools/world/NONLIFE.md`).

- Done: `tools/world/nonlife_real.py` (Wikimedia Commons manifest with licence and source per photo, tune or test by a hash of the id; pocket and BioCLIP 2 vectors; the larger model's answers), the probe rule and the 5% mark in `tools/world/nonlife.py`, `.github/workflows/nonlife.yml` with `ci/nonlife/*.sh`. The marks were stated in `NONLIFE.md` and pushed (`e885403`) before the first run.
- Running: `run/nonlife/1` (the photos, then the larger model's answers and the pocket's rule search). The photos go to `pub/nonlife-real`; the results come back on `ci` as `runs/nonlife/<run>-photos`, `-big` and `-pocket`.
- Next: read the results, write them into `NONLIFE.md`, and ship the rule only if it passes all three marks on the test photos.
