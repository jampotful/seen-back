# desk-d495 progress

Angle: lizards, geckos, snakes and turtles with a Reptile Database page reached from my own search results, then fish with eye diameter in millimetres. No spiders. 6 records (log docs/views/evidence/desk-d495.jsonl), trait eye_diameter_mm, evidence_kind anatomical_measurement. check.py: 0 problems (plain and --require-evidence-kind). About 38 WebSearches.

## Filed
- Hemidactylus kalinga (Gekkonidae), Herpetozoa 38: 365-378, 10.3897/herpetozoa.38.e175753, CC BY 4.0 sentence printed on the preview: Table 3 row ED for holotype ZSI-R-27672 (7.3) and paratypes ZSI-R-28076 (6.9), -28932 (5.7), -29007 (7.0), -29247 (5.9), -29248 (5.7). Methods define 'eye diameter (ED; greatest diameter of orbit)'. Reptile Database page reached from search. Not on main as a record (d478's progress line says "already on main" but no evidence line or other doc holds the species or DOI).

## Weak spots
- All text came through the WebFetch reader on the Pensoft article_preview page (table read cell by cell, requested twice, same ED row both times). Reader returned Methods sentences only as fragments, so the type-material text is paraphrase and the quote is the whole ED table row.
- The Table 3 caption prints no unit; the unit comes from the Methods precision sentences. Cross-check: holotype ED 7.3 / ES 12.2 = 0.60 and the text's 'ED/ES ratio 0.6'; ED/HL 0.25 against 'OD/HL ratio 0.3'.
- Reptile Database prints no explicit 'valid'. Crossref not checked.

## Not filed and why
- Cyrtodactylus shenbagathoppuensis and C. kalakadensis (Vertebrate Zoology 76): no Reptile Database page in two searches (only the article preview and plazi/zoobank).
- Thamnophis ahumadai (Herpetozoa 37: 157-179): Reptile Database page reached, but the article page returned has no ED table or definition.
- Gekko wuzhengjuni (ZSE 102(2) 719-729; ED 4.8, 4.5, 3.0): Reptile Database has only Goniurosaurus wuzhengjuni (a different paper); no Gekko page.
- Philodryas pseudomamba (VZ 76: 93-119) and Ovophis langbianus (Herpetozoa 39): no Reptile Database page in results.
- Eublepharis jhuma, Scincella verecunda, Trimeresurus loong: already on main. Dasypeltis albigularis (no ED in table), Calotes thailandensis/C. maehongsonensis (Methods list no ED), Gekko asahi and Sphenomorphus lingnanensis (no eye data): dead.
- Fish: ZooKeys CSVs reached (Johnius javaensis on main; Opistognathus cryos and a Parapercis/Pseudochromis-type table print % SL or % HL only; a Garra/loach CSV prints % HL). Rhinogobius mengyangensis: Catalog of Fishes page not reached.
- Mesalina bishnoi, Trimeresurus hongheensis, Calamaria hunanensis: venues outside the accepted list (Records of the ZSI, Zoological Research: Diversity and Conservation).
- Blocked: novataxa label pages for ZSE and VZ (robots_disallowed / provenance); herpetozoa XML for 175753 (provenance).
