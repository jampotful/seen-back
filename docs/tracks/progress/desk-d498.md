# desk-d498 progress

evidence_intake: evidence-kind-v2
intake_base: 1adca712ede7afb1cb22b4401e16c5bb1a7e8651

Angle: reptiles (no spiders) from open-licence Pensoft papers with a Reptile Database species page reached from my own search results; fish searched for tables printing eye diameter in mm. 23 records (log docs/views/evidence/desk-d498.jsonl): 14 eye_diameter_mm and 9 sensory_anatomy (orbital diameter), all evidence_kind anatomical_measurement. check.py: 0 problems (plain and --require-evidence-kind). About 34 WebSearches.

## Filed
- ZooKeys 1253: 131-160 (10.3897/zookeys.1253.161933) Cyrtodactylus makwanpurgadhiensis: six paratypes NHM 2025/384-389 from the combined Table 2 ED row (desk-d451 filed only the holotype and C. chure; its note says 384-389 were left).
- ZooKeys 1253: 195-218 (10.3897/zookeys.1253.149459) Cyrtodactylus arnei: nine type specimens, Table 2 OD row, filed as sensory_anatomy because the paper defines OD as orbital diameter and its row labelled ED is ear length.
- ZooKeys 1245: 289-310 (10.3897/zookeys.1245.153769) Gekko fengshanensis: five paratypes from Table 7 ED row (holotype already on main, desk-d334).
- ZooKeys 1189: 257-273 (10.3897/zookeys.1189.112784) Achalinus nanshanensis: holotype (description sentence plus Table 4) and two paratypes.

## Weak spots
- All text came through the WebFetch page reader on Pensoft article_preview pages; sentences over about 125 characters came back in pieces and were joined; column-to-code mapping is the reader's cell reading. Licence sentences came as opening clauses with the remainder paraphrased.
- Achalinus nanshanensis Table 4 prints two decimals while the Methods say calipers to 0.1 mm; logged as printed. Its table caption prints no unit (taken from 'ED 1.11 mm').
- Reptile Database pages print no explicit 'valid'; the name as its own entry with the original citation was taken as accepted. Crossref not read.
- Pensoft article_preview pages were opened by id taken from figure-page URLs in search results (same domain and id).

## Not filed and why
- Lycodon cathaya (ZooKeys 954: 85-108, holotype ED 2.2, paratype 3.0): the Reptile Database URL in my results returned 'Species Lycodon cathaya was not found'; no species page.
- Trimeresurus liqibini (ZSE 102(1), 3.54 and 2.94): no Reptile Database page in results again (Catalogue of Life, Wikispecies only).
- Plagiopholis yangi (Evol. Syst. 10(1), holotype ED 2.6): no Reptile Database page in results.
- Trimeresurus nujiang (holotype ED 4.4) and Hebius shantianfangi (EDH/EDV, four specimens): already on main (desk-d493, desk-d475).
- Hebius citrinoventer and Gloydius lateralis: d497 filed them. Achalinus hunanensis (ZooKeys 1166: 315-331): ED printed as unexplained paired values (1.42 / 1.41), sides not stated. Achalinus zugorum (BDJ 13): on main, d477.
- Sphenomorphus tamchucensis (ZooKeys 1266): only eye length (EL, eyelid corners), no ED. Trimeresurus salazar (ZSE 96): DEYE ratio only. Hebius/Boulenophrys yezhongensis (Herpetozoa 38): summary statistics only. Eublepharis jhuma (Herpetozoa 39: 161-176, Table 4 OD 9.1, 8.7, 7.7): lead only, not checked against main or the Reptile Database.
- Fish: Microphysogobio punctatus, Rhinogobius spp., Sinocyclocheilus zhenningensis, all % HL or % SL, no mm. Scincella jinchuanensis/maerkangensis: no ED. Cyrtodactylus nebulicola: on main (d476).
- Catalog of Fishes getref pages appeared in results but gave references only; no fish with ED in mm found.
