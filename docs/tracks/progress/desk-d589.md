# desk-d589 progress

evidence_intake: evidence-kind-v2
intake_base: 407e221cb6eaee2fd219117704172cec77c8b4b2

Angle: 2022-2025 amphibian, lizard and mammal per-specimen table rows (tympanum, ear opening, ear length) from open-licence papers. Log docs/views/evidence/desk-d589.jsonl, 32 records. check.py plain and with --require-evidence-kind: 0 problems. About 40 WebSearches (unfiltered descriptive or species-name searches; the Pensoft article_preview pages were reached from the results).

## Filed
- Eleutherodactylus franzi (Eleutherodactylidae), Herpetozoa 36: 95-111, 10.3897/herpetozoa.36.e104707: 30 records from Table 2 (15 type specimens, all adult males; holotype INIRENA 2900, paratypes INIRENA 2895-2898, 2901-2910). 15 TW (width of tympanum) records under sensory_anatomy and 15 ED records under eye_diameter_mm. Each quote is the whole TW or ED row. The reader gave the column-to-specimen mapping; it was cross-checked against the printed TW/ED ratio row (agrees in all 15 columns). ED of INIRENA 2901 (3.74) is high relative to the other columns but matches its printed ratio. ASW species page opened (family not printed; family follows the paper title).
- Pristimantis vrazi (Craugastoridae per ASW URL path; paper says Strabomantidae), ZooKeys 1219: 143-163, 10.3897/zookeys.1219.129773: 2 ED records (holotype MUSM 41581 adult female 3.7 mm; paratype MUSM 41582 subadult male 2.3 mm) from running-text measurement lines; no type-series table. The tympanum value (TY) is not defined in the Methods, so no tympanum record.

## Weak spots
- All text came through the WebFetch page reader in pieces; table rows and column mappings are the reader's cell-by-cell reading. Page of E. franzi was read to 100000 of 105808 characters (tail is references).
- E. franzi Methods measurement list returned only as a summary with tooltip-style definitions ('width of tympanum (TW)', 'diameter of eye (ED)').
- P. vrazi paratype code: Variation sentence prints MUSM 41582, the Figure 6 caption reading 48582 (reader); the Variation sentence is used.
- Crossref not used.

## Not filed and why
- Already on main or merged: Gracixalus huaping (d583), Leptobrachella weixinensis (d451), Odorrana yangi (d457), Raorchestes hekouensis (d580), Soriculus beibengensis (d586), Soriculus dexingensis (d347), Murina medogensis and milinensis, Scincella truongi, Sphenomorphus lingnanensis (d581).
- Boulenophrys binchuanensis (BDJ 13: e165212): Table 1 TD and ED rows for 4 males, but the reader flagged the Description SVL range (34.5-39.3) disagreeing with the table maximum (38.6); text contradicts table, held out.
- Amolops dafangensis wumengmontis (ZooKeys 1257: 39-54): a subspecies, not filed.
- Diploderma danbaense, donglangense (ZooKeys 1148: 167-207): Tables 2 and 3 have no tympanum, ear or eye rows; jiulongense and tachengense type tables not reached (page text cut at 100000).
- Myotis cf. davidii/aurascens (ZooKeys 1262: 191-201): cf. identification, ear length given as two unlabelled values.
- Calotes iadina (Vertebrate Zoology 74: 169-192): only the article front page and figure pages in my results; no Methods or table text reached.
- Pseudoromicia principis: Journal of Mammalogy, outside the brief's journals.
- Unnamed ZooKeys csv (article 146533): table of Holotype/Males/Females with no species name and a holotype ED (1.0) inconsistent with the male range (1.8-2.2); held out.
- Kalophrynus minutus, Rhacophorus boeadii: only Plazi pages reached; no publisher page.
- Leptobrachella xishuiensis, Odorrana/others from d588 leads not reached through a publisher page.

## Desk disposition after audits 1157 to 1161 (4 November 2026)
No value, specimen code or sex was wrong: all 32 lines match the publisher Table 2 and the running-text lines. Counted errors: 7 (audit 1160, lines 24 to 30: heading path, type material dashes and omitted CIG numbers); all other faults were wording (Results heading, type-material quoting, ASW family note, Methods eye passage, species heading authority). The high E. franzi ED 3.74 mm (INIRENA 2901) agrees with its own printed ratio and is kept as printed with a wider disclosure; auditor 1157 suspects an error in the paper itself. Pristimantis vrazi paratype code MUSM 41582 is right (48582 in the Figure 6 caption is a typo). 32 of 32 merged.
