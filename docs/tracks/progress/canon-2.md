# canon-2: logging open-access canon compilations (14 October 2026)

Worktree /tmp/wscanon2, branch research/canon-2. Evidence goes to docs/views/evidence/canon-2.jsonl, wanted lines to docs/views/wanted/canon-2.jsonl.

## Route
Only WebFetch reaches the web (curl to datadryad.org etc. is refused by the egress proxy; Dryad file_stream downloads refuse robots). So: HTML tables on PMC, Frontiers, nature.com, PLOS, eLife, IntechOpen. Supplement spreadsheets cannot be read; those compilations go on the wanted list with "canon": true.

## Status by compilation (unlogged ones, biggest first)
- 10.5061/dryad.3xsj3txq7 avian eye morphology (3,475 spp): Dryad download refused (robots). WANTED.
- 10.1038/s42003-021-01688-z Lepidoptera opsins (175 spp): species data only in Supplementary Data xlsx and Dryad. WANTED.
- 10.3389/fevo.2019.00321 amphibian photoreception: Table 1 read in full, 39 records (λmax). DONE.
- 10.3389/fevo.2019.00352 reptile photopigments: no tables; species sentences logged (43 records). DONE.
- 10.1093/molbev/msae049 frog opsins: species λmax only in supplement S2; WANTED (a few text values to log).
- 10.1038/s41598-017-00061-7 beetle opsins: supplement only. WANTED.
- 10.1098/rspb.2023.0664 owls, 10.1098/rspb.2023.1213 Anatidae: read Birmingham repository PDFs; species values in figshare supplements (fetch refused); text extremes logged (16 records, partial). WANTED.
- PMC started returning reCAPTCHA after one fetch; use repository PDFs or publisher pages instead.
- 10.1093/molbev/msw148 snake vision: City Research Online manuscript read; no tables (SI only); 6 species records (partial). WANTED.
- 10.1242/jeb.015396 nocturnal bees: HTML had no table; 4 text records (partial). WANTED (PDF).
- 10.1371/journal.pone.0057702 honeybee eyes: Table 1 is an image; nothing logged. WANTED (PDF).
- 10.7554/eLife.15675: elifesciences.org returned a JavaScript challenge page. Not read.
- 10.1098/rstb.2009.0044 (PMC2781856), 10.1098/rspb.2023.0664 (PMC10581762): PMC now serves reCAPTCHA; Europe PMC REST and figshare/doi.org collection links need a permission the session did not get.

## Stopped (14 October)
Two HTTP 429 refusals from the fetch proxy (link.springer.com for 10.1007/s10336-007-0213-6, then doi.org/10.5772/intechopen.74645). Per the brief, stopped at once. 118 records, 9 wanted lines.

## Next (for a restart), not yet tried
Hall & Ross 2007 eye shape mammals (Proc B), Thomas et al. 2020 frog eye size (10.1098/rspb.2020.1393), Land 2015 eye movements (10.1007/s00359-014-0964-5), Necker 2007 head-bobbing (10.1007/s00359-007-0281-3), Nityananda & Read 2017 stereopsis (10.1242/jeb.143883), Cronin & Bok 2013 (10.1016/j.cub.2013.10.019), Nilsson 2013 (10.1017/S0952523813000035), Jacobs 2009 (10.1098/rstb.2009.0039), Ollivier 2004 tapetum (10.1111/j.1463-5224.2004.00318.x), Heesy 2011, Brischoux 2010, Emerling 2017 (10.1093/molbev/msw265), Healy 2013 figshare Flicker_fusion_values.csv, Kelber 2003, 1KP, phytochrome diversity (10.1038/ncomms8852), legume flowering (10.3389/fpls.2015.00207, Frontiers HTML likely has Table 1), ant eyes Dryad nzs7h44v8, gulls Ibis 10.1111/ibi.13360, Martin 2007 (Springer 429). Route that worked: doi.org redirect, then fetch the publisher page; repository PDFs (research.birmingham.ac.uk, openaccess.city.ac.uk); Frontiers HTML tables extract well when asked for JSON rows.
