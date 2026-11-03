# desk-d488 progress

Angle: lizards, geckos, snakes, turtles and fish with a Reptile Database / Catalog of Fishes page reached from my own search results; no spiders. 19 records (log docs/views/evidence/desk-d488.jsonl), trait eye_diameter_mm, evidence_kind anatomical_measurement. check.py: 0 problems for this file (plain and --require-evidence-kind). 30 WebSearches.

## Filed
- ZooKeys 1275: 15-42 (10.3897/zookeys.1275.178507), CC BY 4.0 on the preview copy. Cyrtodactylus teraiensis (Gekkonidae): holotype NHM 2025/390 ED 2.8 mm (1 record; quote is the mensural sentence with marked cuts; unit from the Methods caliper sentence). Cyrtodactylus nebulosus: Table 3 'Mensural data (in mm)' ED row, 18 specimens (lectotype, 3 paralectotypes, 14 topotypes), one record per specimen, whole-row quote.

## Weak spots
- All text came through the WebFetch reader on the Pensoft preview (XML is cut before the description). Table 3 has specimens as columns; the ED and Sex rows were read twice with identical values.
- The holotype ED sentence came back in pieces; the quote joins them with [...] cuts. Reptile Database page for C. nebulosus does not yet list the lectotype designation.
- Table 3 pairs a paralectotype 'subadult female' with sex code F and two juveniles with '?'.

## Not filed and why
- Ablepharus tuolinensis: Reptile Database page reached (AHR 16(3): 261-271, DOI 10.3724/ahr.2095-0357.2025.0011); the sciengine article URL was permission-blocked, no open page reached.
- Plagiopholis yangi (Evol. Syst. 10(1): 85-92, holotype ED 2.6, CC BY 4.0) and Gekko wuzhengjuni: no Reptile Database species page in my results (Goniurosaurus wuzhengjuni page only).
- Trimeresurus hongheensis (Zool. Res. Divers. Conserv. 2(3)): page metadata says CC BY 3.0, PDF prints a Non-Commercial licence sentence (conflict); only VED printed for the holotype; Reptile Database lists status unclear (no ZooBank).
- Hemiphyllodactylus puncak / jeraiensis (Vertebrate Zoology 76: 1-32): Reptile Database pages exist, but the article page and XML return no Methods or morphometrics.
- Lycodon duytan (ZooKeys 1251): no Reptile Database page, no ED defined. Trachischium lalremsangai (Herpetozoa 39): no ED. Hemiphyllodactylus pakhaensis: no Reptile Database page.
- Sinocyclocheilus zhenningensis (ZooKeys 1238, fish): eye diameter printed as %SL only. Oreonectes jinxiuensis and Claea dafangensis (ZSE): text cut before tables.
- Sphenomorphus lingnanensis, Eublepharis jhuma, Scincella ngati: dead or already-known leads. MDPI items (Scincella heishuiensis, Ptyctolaemus tongbiguanensis) not tried because of the licence route.

## Desk disposition after audits 976-978 (3 November 2026)
- Audit 976 (lines 1-7): 1 error, 13 faults. Line 1 (Cyrtodactylus teraiensis holotype NHM 2025/390, ED 2.8) wrongly said no paratype ED is printed and that the paragraph gives no unit; the paper prints ED = 2.9 for paratype NHM 2025/391 and "All measurements in mm"; it also added an unprinted "Holotype" heading. Corrected from the auditor's replacement. Lines 2-7: section path missing; sexes of lines 3-5 matched to codes the text leaves unmatched (corrected).
- Audit 977 (lines 8-13): 0 errors, 6 faults (eye side: Methods print "on the left side of the body whenever possible").
- Audit 978 (lines 14-19): 0 errors, 12 faults (heading path; "topotype" not given as printed: "Referred material (topotypes)" in the table, "Additional material" in the text).
- All 19 lines merged with the auditors' replacement text; nothing dropped.
- Open lead: the paratype NHM 2025/391 ED 2.9 for Cyrtodactylus teraiensis is printed in the paper but is not filed (a missing record); a later unit may file it with its own Mensural data sentence.
- Correction: desk-d481.md wrongly calls C. teraiensis "on main"; before d488 it was not.
