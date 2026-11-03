# desk-d497 progress

Angle: reptiles (and frogs) from older open-access Pensoft descriptions, no spiders. 21 records (log docs/views/evidence/desk-d497.jsonl), trait eye_diameter_mm, evidence_kind anatomical_measurement, one record per labelled specimen measurement. check.py: 0 problems (plain and --require-evidence-kind). About 38 WebSearches. No fish filed.

## Filed
- ZooKeys 1226: 1-24 (10.3897/zookeys.1226.138464) Cnemaspis enneaporus (Gekkonidae): holotype and paratype, Table 2 ED row ('eye diameter (ED), as the maximum horizontal diameter of the eyeball').
- Zoosystematics and Evolution 98: 165-180 (10.3897/zse.98.73162) Leptobrachella shimentaina (Megophryidae): 6 males (holotype and 5 paratypes) and 2 female paratypes, Table 2 EYE rows (EYE defined as eye diameter). Read on the Pensoft article_preview; the Zobodat PDF that came up in search was not used as the source copy.
- ZooKeys 1114: 59-76 (10.3897/zookeys.1114.79709) Gloydius lateralis (Viperidae): holotype and 4 paratypes with an ED value, Table 1 ED column (22 cells per row, ED/HL cross-checks ED over HL). Four SAFS paratypes print a dash and are not filed.
- ZooKeys 1206: 255-274 (10.3897/zookeys.1206.123841) Hebius citrinoventer (Natricidae): holotype adult female and crushed subadult male paratype, Table 4 ED row.
- ZooKeys 959: 113-135 (10.3897/zookeys.959.54601) Acanthosaura liui (Agamidae): holotype and 3 paratypes, Table 3 EYE row (abbreviation EYE, not ED).

## Weak spots
- All text came through the WebFetch page reader (article_preview pages and, for A. liui, the Pensoft XML download). Row and column mapping is the reader's cell-by-cell reading; reader outputs were paraphrased in places (licence sentences came in pieces or as paraphrase).
- Gloydius lateralis, Hebius citrinoventer: the table captions print no unit; mm comes from the Methods precision sentences (and, for H. citrinoventer, the holotype sentence 'ED 3.5 mm').
- Leptobrachella shimentaina: issue number of ZSE 98 not seen, so the journal string carries volume and pages only. Paratype specimen numbers were not reproduced by the reader; the Table 2 male and female blocks match 'five paratype males and two paratype females' plus the holotype.
- A. liui record source URL is the Pensoft XML download; the reader did not return the Taxon classification block.

## Not filed and why
- Cnemaspis lokugei (ZSE 97: 191-209, Methods define ED as horizontal diameter of the eye ball): Tables 2 and 3 never came back from the XML reader across six offsets; the holotype description prints SVL only.
- Cnemaspis sathuragiriensis and C. vangoghi (ZooKeys 1196: 209-242): the XML returned only the molecular methods and the voucher table; no Reptile Database page opened; morphology text not reached.
- Acanthosaura tongbiguanensis (ZooKeys 888: 105-132): EYE defined as eye diameter and a Reptile Database page opened, but Tables 3 and 4 were not in any XML window returned.
- Hebius citrinoventer XML and Pensoft pages for ZooKeys 1196: see above; the XML downloads often repeat the front matter and the voucher table.
- Cyrtodactylus limajalur (Zootaxa), C. evanquahi (Zootaxa), C. ngati (Zootaxa), C. hamidyi (Zootaxa), C. kanyakumariensis and Cnemaspis geethaiyerae (J. Nat. Hist.), Scincella ouboteri (Zootaxa): non-open or non-Pensoft venues.
- Selvasaura candesi, S. evasa, Enyalioides feiruzae (Evolutionary Systematics): Methods print no ED and the tables have no eye column.
- Diploderma limingense, D. shuoquense, D. yongshengense (ZooKeys 1131): no ED; only snout-eye length.
- Achalinus hunanensis (ZooKeys 1166) already on main (d477); Scincella ngati and the 146533 lead already on main (d343/d487).
- No fish paper with eye diameter in mm and an Eschmeyer page was reached.

## Desk disposition after audits 986-989 (3 November 2026)
All 21 lines merged with the auditors' replacement text; nothing dropped. Audit 986 (2 lines): 0 errors, 4 faults (eye side, licence paraphrase). Audit 987 (8 lines): 0 errors, 33 faults (issue number, heading path, licence, paratype list). Audit 988 (7 lines): 7 errors, 29 faults (family Natricidae corrected to Colubridae (Natricinae) per Reptile Database and main; printed heading paths; cut marks). Audit 989 (4 lines): 4 errors, 12 faults (eye side stated as left in Methods; licence cut mark; type material). All errors fixable. Owner question unchanged: eye_diameter_mm vs sensory_anatomy for label-only evidence (here every paper printed a diameter definition).
