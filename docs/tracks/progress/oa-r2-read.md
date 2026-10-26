# oa-r2: reading pass over oa-10, oa-11 and oa-12 (26 October 2026)

Lookups used (latest successful run per batch that covers the whole batch, from `INDEX.txt` on `ci`): `runs/oa/1-oa-10` (55 entries), `runs/oa/11-oa-11` (47) and `runs/oa/19-oa-12` (79). Later runs of these batches on `ci` hold only one to fourteen entries each.

Of the 65 entries whose `read.kind` is pdf, xml or html, 60 already have evidence on `main` under their DOI in `docs/views/evidence/oa-*.jsonl`. One more, oa-11 entry 4 (Johnson and Rutowski 2022, ants), is logged in `oa-2.jsonl` under its Dryad dataset DOI (63 records) and in `canon-8.jsonl`, so it is skipped as already logged. That leaves four entries for this pass: oa-10 entry 31, oa-12 entries 29, 48 and 73. The first three were read on 18 October with `"records": 0`.

Run branch `run/oa/read-r2` (commit 47baf9a4) carries this unit's own public key, `ci/oa/list.jsonl` cut to those four entries, and the matrix `[oa-10, oa-11, oa-12]`.

`docs/views/sources/oa-none-r2.jsonl` lists the 35 entries of the three batches whose lookup located a free copy that then failed to give its text and that no sources file on `main` lists yet.

## Result (run 26, all three batch jobs succeeded at 06:27 to 06:28 UTC)

| entry | paper | outcome |
|---|---|---|
| oa-10 31 | Ishida, Kono and Sakai 2009, brood-site pollination in Macaranga | read whole (Europe PMC PDF); visitor counts, pollen loads and nectary feeding, no BRIEF trait; 0 records |
| oa-12 29 | Yamashita and Tsuihiji 2022, hard and soft eye tissues in lizards | read whole (Europe PMC XML); museum-specimen dimensions (scleral ring, lens, pupil diameter, eyeball) and regressions, no BRIEF trait; 0 records |
| oa-12 48 | Shenkutie, Nagano and Hughes 2024, Sorghum phyB crystallization | read whole (Europe PMC XML); recombinant protein from E. coli, no living-plant response (point 10a); 0 records |
| oa-12 73 | Guillén, Rico and Castroviejo 2005, Potentilla reproductive biology | not read: the Dialnet PDF is a different paper of the same issue (Gasteromycetes of Costa Rica) and never names Potentilla; listed in `oa-none-r2.jsonl` |

Papers read: 3. Records: 0 (no grades, no partials), so no evidence file and no new `ci/oa/sources-r1.jsonl` lines (all four entries already have one). `docs/views/sources/oa-r2.jsonl` holds the three read papers with `"records": 0`; `oa-none-r2.jsonl` holds 36 lines (35 earlier retrieval failures and the Potentilla mismatch). The 60 entries already logged on `main` were not reread, as the launch prompt asked.
