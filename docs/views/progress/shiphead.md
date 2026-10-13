# Progress: shiphead (burst 3, 13 October 2026)

Done and pushed
- Merged `main` (build 26) into `agent/head-ship`. The conflicts were more than BUILD: `src/cam.rec.js` (the manifest checks of main's database for the world against this branch's `known()` and `county_bias`), `src/cam.a.js` (BUILD), and the built files. The manifest checks keep main's lines with `known(l)` in place of `EYES[l]`. BUILD is 27. Pushed as `3c6350e`.
- Machine note: port 8765 was already in use by another agent's server (build 24), so my first run of `test/check4.js` was against the wrong page. Those results were discarded. All runs now use a server on port 8791.

Next
- Every mode of `test/check4.js`, every section of `test/rec/check_rec.js`, `tools/fusion/parity.py`, one at a time.
- Fresh Alachua photos: none can be made from this machine (GBIF and the iNaturalist photo host refuse the proxy; `pub/data-alachua` holds manifests only). Decision is by the tuning photos (+0.24 points, mark above -2).
