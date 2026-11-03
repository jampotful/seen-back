# desk-d506 progress

Angle: lizards, geckos, snakes and turtles with a Reptile Database species page reached from my own search results, from open-licence descriptions printing eye diameter (ED) in millimetres per named specimen; fish as a second strand (nothing filed). No spiders. 55 records (log docs/views/evidence/desk-d506.jsonl), trait eye_diameter_mm, evidence_kind anatomical_measurement, one record per labelled specimen column. check.py: 0 problems (plain and --require-evidence-kind). About 40 WebSearches.

## Filed (all Vertebrate Zoology, CC BY 4.0 on the page, Reptile Database page opened for every species)
- 73: 887-913 (10.3897/vz.73.e110512) Cnemaspis pakkamalaiensis (6 specimens) and Cnemaspis cavernicola (5), Table 3 ED row.
- 72: 385-422 (10.3897/vz.72.e82343) Cnemaspis azhagu (9, Table 3) and Cnemaspis mundanthuraiensis (9, Table 6).
- 73: 205-236 (10.3897/vz.73.e90979) Cnemaspis jayaweerai (3) and Cnemaspis nanayakkarai (3), Table 3.
- 72: 81-94 (10.3897/vz.72.e76046) Hemidactylus easai (4), Table 2.
- 73: 499-512 (10.3897/vz.73.e104494) Hemidactylus pakkamalaiensis (5), Table 2.
- 73: 475-498 (10.3897/vz.73.e102602) Cyrtodactylus irulaorum (8) and Cyrtodactylus relictus (3), Table 3.

## Weak spots
- All text came through the WebFetch reader on Vertebrate Zoology article_preview pages. Table cell-to-code mappings are the reader's; the XML downloads were cut before the descriptions.
- Gingee Hills paper: the Table 3 Type row puts "Holotype" over NRC-AA-1289 (a female) for C. cavernicola while the text names NRC-AA-1286 as holotype; those five records are labelled by code and sex and the type status is not relied on.
- Sri Lanka paper: specimen numbers and sexes in Table 3 are taken from the Systematics text (asterisked in the table).
- Hemidactylus easai and H. pakkamalaiensis tables print no unit; mm comes from the Methods calliper sentence. Methods sentences were partly paraphrased by the reader, so method text quotes only the fragments the reader returned.
- Reptile Database pages print no explicit "valid"; each page is the species' own entry with the description citation. Crossref not checked.
- Which eye was measured is not stated in any of the papers (only a body side for the calliper work).

## Not filed and why
- Cyrtodactylus six new species NE India (VZ 74: 453-486, 10.3897/vz.74.e124752): orbit diameter given only as OD/SO ratio.
- Sphenomorphus lingnanensis (ZSE 102(2) 183764, RDB page opened): Table 1 has no ED row. Gekko asahi (ZSE 102(2)), Gonyosoma (Evol. Syst. 5(1)), Pareas xuelinensis, Trimeresurus ayeyarwadyensis, Enyalioides feiruzae: no ED measurement or definition. Hemiphyllodactylus (ZSE 101(1) 138964): already on main as H. laowozhenensis (desk-d483).
- Fish: Yunnanilus mentibarbatus (ZSE 101(4)) and a Triplophysa cave species print eye diameter only as % HL. Catalog of Fishes pages reached but no mm eye table found.
- Cnemaspis kalakadensis (third species in the Kalakad paper): its table was past the reader's cut.
- Cnemaspis cavernicola/Dixonius (Evol. Syst. 105850): XML fetch denied (permission unanswered); not retried.

## Next three
1. Other Khandekar/Thackeray/Agarwal and Deepak Vertebrate Zoology gecko papers (Cnemaspis anuradhae and relatives) with ED in mm.
2. Vertebrate Zoology Heliobolus (85269) and Angolan Hemidactylus (64781) tables.
3. Fish papers whose tables print eye diameter in mm.
