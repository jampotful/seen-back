# desk-d476 progress

Angle: lizards, geckos, snakes and turtles with a Reptile Database species page reached from the unit's own search results, plus fish with eye diameter in millimetres. No spiders. 21 records (log docs/views/evidence/desk-d476.jsonl), trait sensory_anatomy, evidence_kind anatomical_measurement, one record per labelled specimen. check.py: 0 problems (plain and --require-evidence-kind). About 40 WebSearches.

## Filed
- ZooKeys 1278: 317-338 (10.3897/zookeys.1278.186655) Cyrtodactylus nebulicola (Gekkonidae): 7 type specimens, Table 3 OD row; orbital diameter, not eye diameter (7 records).
- Herpetozoa 39: 161-176 (10.3897/herpetozoa.39.e183441) Eublepharis jhuma (Eublepharidae): holotype 9.1 and paratypes 8.7 and 7.7 mm, Table 4 OD row; orbital diameter, not eye diameter (3 records). Paratype ZSI-R-29345 sex conflict (female in Type materials and Table 4, male in Variation) stated in each note.
- ZooKeys 1266: 263-279 (10.3897/zookeys.1266.176724) Sphenomorphus tamchucensis (Scincidae): holotype and 10 paratypes, Table 1 EL row; eye length, not eye diameter (11 records).

## Weak spots
- Table cell-to-column mappings and licence sentences are the WebFetch reader's output; two licence sentences came back with the closing clause cut and the notes say so.
- Table captions for nebulicola and jhuma print no unit; mm is read from the Methods precision sentences (stated in the notes).
- The Pensoft article_preview endpoint returned another paper's text for ids 175246 (gave 185568 content) and 178507 (gave 188050 content); every filed paper's title and DOI were checked against the page on each read.
- Reptile Database pages print no explicit 'valid'.

## Not filed and why
- Plagiopholis yangi (Evolutionary Systematics 10(1)), Scincella gigas (ZSE 102(4): 1047-1063; holotype ED 3.7 on the page, CC BY 4.0), Sphenomorphus puhoatensis (ZooKeys 1279; only EL 2.2): five searches turned up no Reptile Database species page; dropped as the brief directs.
- Gekko wuzhengjuni (ZSE 102(2): 719-729; ED 4.8, 4.5, 3.0 in Table 2): no Reptile Database page for it in results (only Goniurosaurus wuzhengjuni). Lead if a page is reached.
- Gekko tesselatus (ZSE 101(4): 2221-2242): Reptile Database page opened but the article text (preview and XML) was not reachable.
- Cyrtodactylus teraiensis (ZooKeys 1275): Reptile Database page opened, article text not reachable.
- Fish: Rhinogobius mengyangensis (ZooKeys 1280, Catalog of Fishes reference page opened) prints ED only as % HL; Balitora tiandengensis (ZooKeys 1267) XML shows no morphometric table; Formosania tangi, Claea dafangensis and Oreonectes jinxiuensis not read.

## Desk disposition after audits 951-953 (3 November 2026)
Audited by three fresh Opus agents. 18 of 21 records merged (Cyrtodactylus nebulicola orbital diameter, 7 specimens, ZooKeys 1278; Sphenomorphus tamchucensis eye length, 11 specimens, ZooKeys 1266; both sensory_anatomy, Reptile Database pages reached). Dropped as repeats of main: the 3 Eublepharis jhuma orbital-diameter lines (8-10), because the conditions of desk-d353 on main already list all three millimetre values. Faults corrected with the auditors' replacement text: cut licence sentences, a comma in the C. nebulicola title, the Table 3 heading path, cut Methods sentences, the main-repeat note and Reptile Database fields.
