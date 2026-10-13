# Progress: shiphead (burst 3, 13 October 2026)

Done and pushed
- Merged `main` (build 26) into `agent/head-ship`. The conflicts were more than BUILD: `src/cam.rec.js` (the manifest checks of main's database for the world against this branch's `known()` and `county_bias`), `src/cam.a.js` (BUILD), and the built files. The manifest checks keep main's lines with `known(l)` in place of `EYES[l]`. BUILD is 27. Pushed as `3c6350e`.
- Machine note: port 8765 was already in use by another agent's server (build 24), so my first run of `test/check4.js` was against the wrong page. Those results were discarded. All runs now use a server on port 8791.

Next
- Every mode of `test/check4.js`, every section of `test/rec/check_rec.js`, `tools/fusion/parity.py`, one at a time.
- Fresh Alachua photos: none can be made from this machine (GBIF and the iNaturalist photo host refuse the proxy; `pub/data-alachua` holds manifests only). Decision is by the tuning photos (+0.24 points, mark above -2).

Update 13:28 (stopped at 90 minutes; NOT merged to main)
- Branch `agent/head-ship` now has `main` (build 27) merged in and is numbered build 28.
- Passed on build 27 pre-merge (own server): check4 typed, record, viewer, edge, lex, sweep, film. `lent` fails here and on unmodified `main` (build 27) under load: its fixed 1200 ms wait ends before the look opens. Not caused by the merge.
- Build 28: `tools/fusion/parity.py` ok (3,337 cases, 0 differ; 9 photos). `check_rec.js` (SLOW=3): ok for all sections except `service` and `away` (did not finish, machine load 5 on two cores) and `zone` (FAILED; its five readings look as designed, so a further condition in the check failed; the detail was not read).
- Still to do: rerun `check_rec.js service away zone` alone on a quiet machine, read why `zone` fails, rerun check4 `record`/`typed` on build 28, then merge.
- Fresh Alachua photos: none can be made here.

Burst 4 (13 October 2026): done. Merged main (build 29) into the branch, numbered build 30, fixed `known` shadowing (renamed `knownKind` in src/cam.rec.js), fixed the stale `zone` check (names are lowercase since build 16), `lent` check waits for the look. All check_rec sections ok, check4 typed/record/lent/viewer/edge/lex/sweep/film ok (lent needs SLOW=10 under load), parity ok (3,337 cases, 0 differ). Merged to main.
