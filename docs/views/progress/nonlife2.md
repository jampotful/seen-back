# Track nonlife2 progress

Started 18 October 2026, 19:04 US Eastern, on `agent/nonlife2` (prompt: the control room's, 18 October; read with `tools/world/NONLIFE.md`).

- Photos: `run/nonlife/1` searched Wikimedia Commons from a build machine (`tools/world/nonlife_real.py`), kept CC0, CC BY and public-domain JPEGs whose metadata name no living thing, fetched 1,525 (5 refused with 429), split them into tune and test by a hash of the id and published them with their licence, author and page to `pub/nonlife-real`. Every photo was then looked at; 525 were left out before any result was read (`tools/world/nonlife-real-review.csv`).
- Measurements: run 2 (`runs/nonlife/2-pocket` and `-big` on `ci`) on the 1,000 kept photos; run 1 on all 1,525; run 3 reported COCO's animals for the rule run 2 chose, with nothing chosen again. The larger model's answers come from run 1's `big-photos.jsonl`, split by the review.
- Rule: the probe at 0.9 passed the three marks stated before measuring (`e885403`), and the fourth stated after run 2 (COCO's animals, at most 5%). Shipped in build 39: `models/pocket/manifest.json` (`fusion.nonlife`), `src/cam.rec.js`, `tools/fusion/fuse.py`, `tools/fusion/parity.py` and `test/rec/fuse_page.js`.
- Next: a rule for the larger model (BioCLIP 2's vectors of the photos are on `ci` as `runs/nonlife/1-big/big.f16.npy`); the kept photos as `none` rows in the next fit of the pocket head.
