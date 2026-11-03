# desk-d500 progress

Angle: non-spider unit. Reptiles and amphibians with a species page (Reptile Database or Amphibian Species of the World) reached from my own search results, open-licence Pensoft papers that print eye diameter (ED/EyeD) in millimetres per named specimen; fish tables checked and none usable. 17 records (log docs/views/evidence/desk-d500.jsonl), trait eye_diameter_mm, evidence_kind anatomical_measurement, one record per labelled measurement. check.py: 0 problems (plain and --require-evidence-kind). About 33 WebSearches. Main grepped by species and DOI before every filing.

## Filed
- ZooKeys 1167: 353-382 (10.3897/zookeys.1167.103713, CC0) Hemiphyllodactylus lungcuensis (Gekkonidae): six paratypes (IEBR R.5151, VNUF R.2021.03, R.2023.01, R.2023.02, IEBR R.5152, VNUF R.2021.08), Table 8 EyeD row. desk-d343 holds only the holotype (1.8 mm); its conditions cite just the range 1.8-2.5. Judgment call: three filed paratype values (1.8, 1.8, 2.5) coincide with the range endpoints cited there; they are different specimens and are filed as such.
- ZooKeys 1241: 105-137 (10.3897/zookeys.1241.149552, CC BY 4.0) Cyrtodactylus peninsularis (Gekkonidae): eight paratypes (LSUHC 09633, 10048, 10230, 11136, 11152, 11267, 11979, 12386), Table 7 ED row (mm from the section row 'Morphometric characters (mm)'). desk-d343 holds the holotype and cites 8.1 for LSUHC 11137 as the largest, so 11137 is not refiled. The paper prints LSUHC 9333 in the type list and 09633 in Table 7; recorded in the conditions.
- Zoosystematics and Evolution 100(3): 1121-1134 (10.3897/zse.100.127268, CC BY 4.0) Hypselotriton oolong (Salamandridae): holotype CIB 121430 and paratypes CIB 121429, SYS a009274 (all male), Table 2 whole specimen rows; caption 'Measurements (in mm)'. ASW page reached from my own search. Earlier desks (d477, d481) reached only the CSV or a wrong paper for this id; the article_preview now returned the right paper and title and DOI were checked.

## Not filed and why
- Boulenophrys yangchunensis (Herpetozoa 38: 345-357, lead from d499): two searches, no Amphibian Species of the World page for it appeared (only B. yangmingensis, changyangensis, youran, fengshunensis, yunkaiensis).
- Cyrtodactylus phnomchiensis (ZooKeys 926): d343 conditions already cite the paratype values 5.1, 4.8, 4.8, 4.5.
- Cyrtodactylus thongphaphumensis (ZooKeys 1141: 93-118, CC BY 4.0, RDB page reached): Table 5 ED row prints no unit, and neither Methods nor the Table 1 and Table 5 captions give mm for ED; held out.
- Oligodon sublineatus (ZSE 91(1): 71-80, lectotype 1.7, paralectotype 1.4, RDB page reached): Table 1 caption and rows print no unit, the text gives ED only as % of HL; only the caliper (+/-0.1 mm) sentence implies mm; held out.
- Hypselotriton orphicus rows of the same Table 2: not type specimens of the new species and no ASW page for the name was reached.
- Cyrtodactylus arnei (ZooKeys 1253) and C. menglianensis (ZooKeys 1084): ED there is ear diameter, not eye.
- Diploderma bifluviale (ZooKeys 1251): no ED (snout-eye length only); Hebius malnatei (ZSE 102(1)): no ED; Eublepharis jhuma: already on main (d353), orbital diameter; Pristimantis pluvialis: d343 audit found Table 1 values offset against labels; Gekko tesselatus and Rhinophis siruvaniensis: all specimens already on main (d479, d487); Hemiphyllodactylus laowozhenensis: on main (d483).
- Zootaxa papers (Dixonius hinchangsi, Hemiphyllodactylus diaoluoshanensis, Gekko shiva, Rhoptropus nivimontanus): not open licence.
- Fish: Pensoft CSV tables reached (Triplophysa, Opistognathus, Stolephorus, Alburnus-type, Enteromius) print eye diameter only as % SL or % HL, or as ranges and means without specimen codes.

## Weak spots
- All text came through the WebFetch page reader. Table values and column-to-code mappings are the reader's cell-by-cell reading of the publisher's CSV exports; sexes agree with the type-material text in each paper.
- Crossref was not checked (blocked by a permission prompt); licence sentences are the page-printed ones as returned by the reader.

## Desk disposition after audits 995-997 (3 November 2026)
16 of 17 lines merged with the auditors' replacement text. Dropped: line 8 (Cyrtodactylus peninsularis LSUHC 10048, 6.9), a repeat of main: the desk-d343 conditions text reads "paratypes range 6.9-8.1 mm (n = 9 paratypes; female LSUHC 11137 largest at 8.1)" and only LSUHC 10048 measures 6.9. Audit 995 (6 lines, H. lungcuensis): 0 counted errors, 24 faults (eye side printed as left; caption cut; type material paraphrased); lines 3-5 (1.8, 1.8, 2.5) are not repeats because d343's conditions give only the range 1.8-2.5. Audit 996 (8 lines): 1 error, 24 faults (author "Kaatz A" not "Kaatz AE"; licence sentence not whole; conditions inferred LSUHC 9333 = 09633, removed). Audit 997 (3 lines, Hypselotriton oolong): 0 errors, 9 faults. Owner question: d343's lungcuensis row quote holds the whole Table 8 row, so the six paratype values are printed in main's quote text; if the owner rules that a whole-row quote on main already files every cell in it, lines 1-6 of this unit are repeats and should be removed.
