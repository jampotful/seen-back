# Burst 3: ship the county-bias head (Sonnet)

Start with `burst2-common.md`. Your track is `shiphead`. Stop after 90 minutes.

The branch `agent/head-ship` (`251f719`) holds a TinyCLIP head with a county bias that passed every pass mark on its first reading of the test photos (see `tools/world/RESULTS.md` and `docs/tracks/head.md` on `agent/world-head`; the report is in `docs/views/progress/worlddb.md` if present). It conflicts with `main` only in BUILD. The control room is the app's thread and allows you to merge it.

1. Merge `main` into `agent/head-ship`, resolve BUILD to the next free number, and run every check in full: all modes of `test/check4.js` and every section of `test/rec/check_rec.js`, plus `tools/fusion/parity.py`. Run them one at a time, since the machine has two cores and other agents' tests run at the same time. Never kill processes by name.
2. Because the Alachua test photos have been read three times, build a small fresh Alachua check if one can be made from photos not yet used (look at what `pub/data-*` and the tuning and test splits hold). If none exists, say so in the report and ship anyway only if the tuning-photo difference stays within the pass mark.
3. If everything passes, merge to `main`, and confirm the page behaves as before for a person who has not consented to the database download.

Final report, at most 250 words: the build number, the checks run, the fresh-photos result, and your last commit.
