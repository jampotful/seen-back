# canon-2: logging open-access canon compilations (14 October 2026)

Worktree /tmp/wscanon2, branch research/canon-2. Evidence goes to docs/views/evidence/canon-2.jsonl, wanted lines to docs/views/wanted/canon-2.jsonl.

## Route
Only WebFetch reaches the web (curl to datadryad.org etc. is refused by the egress proxy; Dryad file_stream downloads refuse robots). So: HTML tables on PMC, Frontiers, nature.com, PLOS, eLife, IntechOpen. Supplement spreadsheets cannot be read; those compilations go on the wanted list with "canon": true.

## Status by compilation (unlogged ones, biggest first)
- 10.5061/dryad.3xsj3txq7 avian eye morphology (3,475 spp): Dryad download refused (robots). WANTED.
- 10.1038/s42003-021-01688-z Lepidoptera opsins (175 spp): species data only in Supplementary Data xlsx and Dryad. WANTED.
- 10.3389/fevo.2019.00321 amphibian photoreception: Table 1 read in full, 39 records (λmax). DONE.
- 10.3389/fevo.2019.00352 reptile photopigments: no tables; species sentences logged (43 records). DONE.
