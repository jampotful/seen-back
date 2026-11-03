# desk-d477 progress

Angle: lizards, geckos, snakes and turtles with a Reptile Database page reached from my own search results, and fish with eye diameter in mm. No spiders. 23 records (log docs/views/evidence/desk-d477.jsonl), trait eye_diameter_mm, evidence_kind anatomical_measurement. check.py: 0 problems (plain and --require-evidence-kind). About 48 WebSearches.

## Filed
- Plagiopholis maculosa (ZSE 101(4): 2171-2180, 10.3897/zse.101.172706, CC BY 4.0): holotype ED 2.4 mm, Description sentence (1 record).
- Scincella verecunda (Herpetozoa 39: 127-143, 10.3897/herpetozoa.39.e188979, CC BY 4.0): holotype and 5 paratypes, Table 1 ED row (6 records).
- Trimeresurus loong (ZSE 101(4): 2267-2293, 10.3897/zse.101.175879, CC BY 4.0): holotype and 5 paratypes, Table 4 'ED (mm)' row (6 records).
- Scincella qianica (ZSE 101(4): 1495-1511, 10.3897/zse.101.157713, CC BY 4.0): holotype and 3 paratypes, Table 3 ED row and the holotype sentence (4 records). The non-type referred specimen CIB CB25GZ04 is not filed.
- Plagiopholis acuta (ZSE 101(4): 1775-1797, 10.3897/zse.101.152739, CC0): holotype and 3 paratypes, Table 4 ED row (4 records). The non-type juvenile QHU 2024012 is not filed.
- Achalinus zugorum (BDJ 13: e161176, 10.3897/BDJ.13.e161176, CC BY 4.0): first female KIZ2025021, Table 2 EyeD 1.1 mm (1 record).
- Achalinus hunanensis (BDJ 13: e138423, 10.3897/BDJ.13.e138423, CC BY 4.0): first female QHU 2024030, Table 2 ED row, 1.2 mm (1 record).

## Weak spots
- All text came through the WebFetch page reader (article_preview, XML and Pensoft CSV table exports). The reader returned the wrong paper for article_preview ids 185568/175246 and 127268 (it served other papers' text); every filed record rests on a returned text whose title and DOI were checked against the filed DOI.
- Pensoft CSV exports carry no unit or caption; units come from the preview captions or the holotype sentences (stated in each record). The reader returns quotes in pieces; pieces were joined and each is marked in the note.
- Licence sentences were returned partly or paraphrased for some papers (stated in each note). Crossref was refused, so not checked for any paper.
- Scincella qianica: the Reptile Database page lists two 2025 papers (this one and ZooKeys 1258: 9-33) and does not say which is the original description; the ZSE paper names it sp. nov.
- Plagiopholis acuta: the Reptile Database says paratypes 'n=2' but lists three; the three match the Table 4 columns.

## Not filed and why
- Gekko wuzhengjuni (ZSE 102(2): 719-729, 10.3897/zse.102.185568; ED 4.8, 4.5, 3.0 read from the XML and preview, CC BY 4.0): no Reptile Database page for Gekko wuzhengjuni in my search results. The Reptile Database page opened (Goniurosaurus wuzhengjuni, ZSE 102(2): 611-620, 10.3897/zse.102.177343) is a different species in a different paper and its tables have no ED row. Lead if a Gekko page appears.
- Gekko tesselatus (ZSE 101(4): 2221-2242, 10.3897/zse.101.175246): Reptile Database page reached, Pensoft CSV Table shows ED row (holotype CIB 119371 ED 3.89 and 13 paratypes), but the XML view stops inside Table 1 and the preview id returned another paper, so no Methods definition, caption or licence sentence for the copy was read. Lead.
- Scincella gigas (ZSE 102(4): 1047-1063, holotype ED 3.7), Plagiopholis yangi (Evolutionary Systematics 10(1): 85-92), Trimeresurus liqibini (ZSE 102(1), ED 3.54 and 2.94): no Reptile Database species page appeared in my results.
- Cyrtodactylus teraiensis (ZooKeys 1275: 15-42): Reptile Database page reached; only figure pages of the article reached.
- Scincella ngati (ZooKeys 1275, Table 3 ED 2.2-2.9): Methods define END and EL but not ED.
- Plagiopholis pluvialis (same paper as P. acuta, Table 6): holotype ED 2.26 beside paratype values of 3.88-4.65 that I could not reconcile.
- Achalinus hunanensis CIB 20160503, CIB 119039, CIB 119040: origin of the measurements (this study or Ma et al. 2023) not stated in the passages read.
- Hypselotriton oolong (ZSE 100(3): 1121-1134, 10.3897/zse.100.127268; amphibian, ASW page opened): CSV ED values for CIB 121430 (holotype), CIB 121429 and SYS a009274 exist, but the XML view stops before the measurement table; no caption, unit or type designation read.
- Opistognathus cryos (ZooKeys 1220): ED printed as 13.2 % SL only (the CSV row 13.2 is % SL, not mm).
- Fish with ED in mm: none found in about 8 searches; tables print % SL or % HL.
