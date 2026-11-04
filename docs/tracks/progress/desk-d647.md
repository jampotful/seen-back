# desk-d647 progress

Angle: eye_diameter_mm for amphibian and reptile species with a pupil_shape row but no eye_diameter_mm row on main. Log: docs/views/evidence/desk-d647.jsonl, trait eye_diameter_mm, evidence_kind anatomical_measurement. check.py plain and --require-evidence-kind: 0 problems for this file (19 records so far).

## Filed
- Odorrana leishanensis (ZooKeys 1192: 57-82, 10.3897/zookeys.1192.114315): Table 4 ED row; holotype 4.94, male mean 4.5 (SD 0.3, n = 6), female (n = 1) 5.8; Methods define ED. Holotype ratio ED 0.73 SL agrees with table (4.94/6.73).
- Rhacophorus medogensis (ZSE 101(2): 437-447, 10.3897/zse.101.142297): Table 2 ED row, 8 specimens (holotype, 6 adult male paratypes, one subadult); ED defined in Table 1 of the Methods.
- Charadrahyla viruela (Herpetozoa 39: 49-79, 10.3897/herpetozoa.39.e184954): Table 3 ED row, 8 specimens (holotype and 7 paratypes); the paratype heading prints n = 6 but seven are listed (noted).

## Skipped
- Boulenophrys youran (ZSE 102(1): 53-70): only ED/SVL ratios in text and a p-value table; mm table is in a supplement not on the page.
- Goniurosaurus wuzhengjuni (ZSE 102(2): 611-620): no ED measurement defined or tabulated (SE and EE only).
- Indirana chiravasi (JoTT 6(10): 6293-6312, 10.11609/JoTT.o4068.6293-312): Methods define EL (eye length), not ED; the measurements table is on a separate page. Skipped.
- Boana marginata and Polypedates megacephalus: their only pupil_shape rows on main are from the dataset paper (10.5519/4q5uvvpa), not primary descriptions; skipped without searching.
- Remaining pupil_shape species without an ED row on main (computed over docs/**/*.jsonl): all are the d646-settled set, dataset or review-sourced rows, captive animals (Python bivittatus), or Zootaxa (Liuixalus feii); none searched further.

About 17 WebSearches in total (pool exhausted before the budget). No fetch or search was denied. No Crossref, no proxy hosts, no typed URLs. Scratch folder deleted.

## Desk disposition after audits (4 November 2026)

Audits 1354, 1355 and 1356 judged all 19 lines (eye_diameter_mm: Odorrana leishanensis 3, Rhacophorus medogensis 8, Charadrahyla viruela 8): no value errors, no repeats of main, none dropped; the auditors' replacement text was merged (19 records; check.py 0 problems both variants). By the auditors' count every line had fixable faults (26 in lines 1-8, 42 in lines 9-16, 15 in lines 17-19): page-reader tooltip expansions presented as printed text (row labels such as "ED (diameter of eye)" where the page prints "ED"; Methods items), caliper-sentence and holotype cuts without marks, paraphrased type lists labelled as printed, invented table group labels (the FEMALE and MALE labels in Charadrahyla viruela Table 3 are really a Sex row), a misread heading, missing Variation heading, and the Methods and table caption not read. The unit's worry on R. medogensis paratype code (text 0003603 against Table 2 0008603) was a page-reader misread: the page and XML print SWU 0008603 everywhere, so line 9 stands. The Charadrahyla viruela Table 3 columns were mapped independently by audits 1355 and 1356 (caption "All measurements in mm."; the holotype ratio agrees). The paratype heading prints n = 6 but seven are listed, as the record notes. Merged under the desk's practice for wording-only faults and disclosed as far above the 5% line.

Unit notes: no slip and no classifier denial; about 17 searches (the pool ran out). Skipped: Boulenophrys youran (mm table in Supplementary material 1 only), Goniurosaurus wuzhengjuni (no ED defined), Indirana chiravasi (EL, not ED; table on another page), Boana marginata and Polypedates megacephalus (pupil rows from a dataset paper, 10.5519/4q5uvvpa). The remaining species with a pupil_shape row and no eye_diameter_mm row are the d646-settled set, dataset- or review-sourced rows, captive animals (Python bivittatus) or Zootaxa (Liuixalus feii). Note: the d647 unit reached Pensoft article_preview pages normally, but the held d625 article (Herpetozoa 38, id 165173) still returned "Site under maintenance" when retested.
