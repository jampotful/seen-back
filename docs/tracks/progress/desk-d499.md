# desk-d499 progress

Angle: reptiles (Reptile Database page from own results) and fish; no spiders. 11 records (log docs/views/evidence/desk-d499.jsonl), trait eye_diameter_mm, evidence_kind anatomical_measurement. check.py: 0 problems for this file (plain and --require-evidence-kind). About 38 WebSearches.

## Filed
- ZooKeys 1253: 255-275 (10.3897/zookeys.1253.161412) Calamaria synergis: holotype ANU ZR24046 EyeD 1.2 mm from the Description of the holotype sentence, cut with [...] (desk-d455 filed only the paratype because the sentence is over 40 words). Reptile Database page opened from a search result.
- ZooKeys 1253: 305-320 (10.3897/zookeys.1253.154757) Boulenophrys dalaolingensis (Megophryidae): holotype and 9 paratypes, Table 2 ED row (10 records). ASW page opened from a search result.

## Weak spots
- All text came through the WebFetch page reader on Pensoft article_preview pages; Table 2 column-to-code and sex mapping is the reader's cell-by-cell reading (header, ED and Sex rows each 10 cells).
- Table 2 caption prints no unit; mm comes from the 0.1 mm caliper sentence and a mm value in the holotype description.
- ASW prints the reference as ZooKeys 1235: 310; the article page prints 1253: 305-320 (DOI zookeys.1253.154757 agrees with 1253). Printed volume used.

## Not filed and why
- Scincella verecunda (Herpetozoa 39): found and filed, then dropped when a fetch of origin/main showed it already on main (desk-d477, d487, d489). My worktree had been behind main; rebased before the final greps.
- Boulenophrys yangchunensis (Herpetozoa 38: 345-357, 10.3897/herpetozoa.38.e171400, CC BY 4.0): Table 2 ED row 3.7 3.6 3.8 4.0 3.7 for GEP a168, a169, a170*(holotype), CIB 121751, SYS a009518, ED defined and caption in mm; held out because no Amphibian Species of the World page surfaced in my results (validity unchecked). Lead: file if an ASW page is reached. The article_preview URL for id 171400 returned a different paper on first fetch (as desk-d484 saw) and the right paper on a later fetch.
- Sphenomorphus lingnanensis (ZSE 102(2): 411-420): no eye diameter reported. Scincella qianica (ZSE 101(4)): already on main (d477). Calamaria similis, Hemidactylus kalinga, Cyrtodactylus nebulicola, Oligodon cicadophagus pages: on main or not reached beyond Plazi redirect stubs.
- Plazi treatment pages (Rhoptropus nivimontanus, Oedura atra, Raorchestes leiktho/khonoma, Boulenophrys yangchunensis) return only a redirect notice to the reader. Oedura atra and Raorchestes leiktho are Zootaxa (mapress), not open-licence. Protobothrops flavirostris (Herpetozoa 38: 43-60): article page not readable (permission refused for the article URL; preview returned another paper).
- Fish: the only Catalog of Fishes pages in results were reference-id pages with no paper text; no fish filed.

## Desk disposition after audits 993-994 (3 November 2026)
All 11 lines merged with the auditors' replacement text; nothing dropped. Audit 993 (lines 1-6): 0 errors, 6 faults (Calamaria synergis holotype note claimed a "preserved specimen" method the Methods do not state; Table 2 sits under Diagnosis; species-heading authority). Audit 994 (lines 7-11): 0 errors, 15 faults (heading path, cut mark on the holotype sentence, Methods heading). The page prints ZooKeys 1253: 305-320; ASW's "1235: 310" is ASW's own error. Lead for a later unit: Boulenophrys yangchunensis (Herpetozoa 38: 345-357), held out for want of an ASW page in the unit's results.
