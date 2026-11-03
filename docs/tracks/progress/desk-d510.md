# desk-d510 progress

Angle: reptile eye_diameter_mm (spider pool not touched; fish not filed). 32 records (log docs/views/evidence/desk-d510.jsonl), trait eye_diameter_mm, evidence_kind anatomical_measurement, one record per labelled specimen column. check.py: 0 problems (plain and --require-evidence-kind). About 33 WebSearches.

## Filed
- ZooKeys 1211: 101-130 (10.3897/zookeys.1211.122563) Cyrtodactylus khlonghatensis: holotype and 5 paratypes (6), Table 3 ED row; ED defined in Methods; Table 2 caption prints mm and repeats the values.
  Search query (allowed_domains zookeys.pensoft.net): "Cyrtodactylus khlonghatensis ZooKeys 1211 karst-dwelling bent-toed gecko eye diameter Table 3" gives https://zookeys.pensoft.net/article/122563/ ; page read: https://zookeys.pensoft.net/article_preview.php?id=122563
- ZooKeys 1240: 73-115 (10.3897/zookeys.1240.139691) Cyrtodactylus kampingpoiensis: holotype and 7 paratypes (8), Table 4 ED row (unit from the 'Morphometric characters (mm)' row-group heading).
  Query (allowed_domains zookeys.pensoft.net, zse.pensoft.net, herpetozoa.pensoft.net): "new species Cyrtodactylus Laos OR Cambodia OR Myanmar OR Thailand holotype ZMKU eye diameter ED horizontal eyeball" gives https://zookeys.pensoft.net/article/139691/element/5/31/ ; page read: article_preview.php?id=139691
- ZooKeys 1125: 115-158 (10.3897/zookeys.1125.94060) Cnemaspis samui: holotype and 17 paratypes (18), Table 5 ED row (specimens are columns).
  Query (no domain filter): "Cnemaspis samui reptile-database" gives https://zookeys.pensoft.net/article_preview.php?id=94060 ; the XML https://zookeys.pensoft.net/article/94060/download/xml also appears for (allowed_domains zookeys.pensoft.net) "Cnemaspis siamensis group new species Thailand ZMKU holotype eye diameter".
Reptile Database species pages (Cyrtodactylus khlonghatensis, C. kampingpoiensis, Cnemaspis samui) were opened from my own search results; none prints an explicit 'valid'.

## Weak spots
- All text through the WebFetch page reader (Pensoft article_preview pages); column-to-code and sex rows are its cell-by-cell reading. The sexes agree with each paper's type-material paragraph and with the Reptile Database holotype entries.
- Licence sentences for the first two papers arrive in pieces and are joined; for C. samui the reader paraphrased it. Crossref not checked. Heading paths for Tables 3 and 4 not read.
- Cnemaspis samui quote is the whole 18-value ED row (19 words); a clipped copy of the row is not used.

## Not filed and why
- Amolops cuongi (ZooKeys 1256: 235-257, 10.3897/zookeys.1256.158846, CC BY 4.0, ASW page opened): the Description prints 'SE 5.0 mm, ED 5.3 mm' for the holotype IEBR A.5139, but the preview's Table 1 ED row starts with 5.0; the XML cut before the table. Conflict unresolved: held out. Lead for an auditor with the table.
- Lycodon anakradaya (same paper as L. truongi, VZ 72: 371-384): Reptile Database says 'Species Lycodon anakradaya was not found!'; the L. truongi page does not name it. Not filed. Text and Table 3 also disagree on specimen codes (SIEZC 20247 vs NAT21-11).
- Cyrtodactylus luci (ZooKeys 1192: 83-102): the Methods define ED as ear length. Gekko wuzhengjuni (ZSE 102: 719-729, ED 4.8/4.5/3.0) and Gekko asahi (EL only, molecular), Goniurosaurus wuzhengjuni: no Reptile Database page for the Gekko name; Gekko qiannanensis (ZSE 102(4): 973-987): per-specimen data only in a supplement, no Reptile Database page. Dixonius fulbrighti: XML ends before the morphometric table, no holotype designated in the text read, no Reptile Database page in results.
- Cyrtodactylus phamiensis, Panaspis ericae/mundavambo, Oligodon churahensis, Enyalioides feiruzae: no ED mm in the text reached (previews returned other papers or the XML was cut). Cyrtodactylus arunachalensis (OD) and Hemidactylus pfindaensis skipped as briefed.
- Fish: Epinephelus tankahkeei (orbit diameter as % SL) and Scolopsis lacrima (% SL) printed no mm; no Catalog of Fishes page reached.

## Desk disposition after audits 1023-1026 (3 November 2026)
Audits judged 32 lines with 0 value errors and about 140 text faults, all corrected from the auditors' replacement blocks. Lines 7-14 (Cyrtodactylus kampingpoiensis, ZooKeys 1240) are dropped: two auditors could not reach the publisher full text in their own search results (16 and 10 searches). 24 records merged (C. khlonghatensis 6, Cnemaspis samui 18).
