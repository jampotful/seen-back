# desk-d626 progress

Angle: tympanum columns of older frog papers already audited on main (amphibian eye_diameter_mm rows from desk units with no tympanum row for the same species and DOI, plus species whose ED rows cover more specimens than the TD rows on main); the OLD-ANGLE paragraph (reptiles and fish) was not followed. 45 records (log docs/views/evidence/desk-d626.jsonl), unit field desk-d626, evidence_kind anatomical_measurement, one record per labelled measurement, shaped on desk-d623, desk-d624 and desk-d625. check.py: 0 problems for this file (plain and --require-evidence-kind). About 35 WebSearches. Every paper was reached through an own unfiltered search (exact title or species plus journal) that returned the Pensoft article_preview (or XML) URL; the page was read through WebFetch, the licence sentence read in pieces (CC BY 4.0 everywhere), the ASW page opened from an own search result and its comment read for splits. Crossref was not used.

Step 1 (python over docs/views/evidence on origin/main, scratch folder untracked): 46 species+DOI pairs have amphibian eye_diameter_mm rows and no tympanum row; a second pass (ED rows more numerous than TD rows) found Leptobrachella huynhi, Zhangixalus yunnanensis and Gephyromantis lomorina (plus the held-out Cophixalus rajampatensis and Boulenophrys dalaolingensis, and Brachytarsophrys wui, whose tympanum is hidden).

## Filed
- Chimerella mira, Evolutionary Systematics 7(2): 195-209 (10.3897/evolsyst.7.102950): TD of the holotype and the paratype from the two measurement sentences (2 records; same sentences as the desk ED rows).
- Leptobrachella jinzhongshanensis, ZSE 102(4): 1089-1105 (10.3897/zse.102.195575): label TMP (defined in the Methods; TD not used): holotype from the holotype list, and the Table 3 male (n = 2) and female (n = 8) mean cells (3 records, each summary says what it pools).
- Pristimantis mallii, ZooKeys 832: 113-133 (10.3897/zookeys.832.30874): holotype TD from the holotype sentence and the Table 1 TD means for females (n = 8, pools the holotype and seven paratypes) and males (n = 12) (3 records).
- Choerophryne crucifer (5 records, all five types, Table 1 TyD row) and Choerophryne multisyllaba (6 records, Table 2 TyD row), ZSE 93(2): 265-279 (10.3897/zse.93.11576). Main had only the dimensionless ED/SUL ratios (desk-d366) for this paper.
- Leptobrachella huynhi, BDJ 12: e136491 (10.3897/BDJ.12.e136491): TD of the three paratypes (holotype TD is on main, desk-d583) (3 records).
- Zhangixalus yunnanensis, ZSE 100(1): 183-197 (10.3897/zse.100.113850): TD of eight paratypes from Table 2 (holotype TD on main, desk-d583; ED rows desk-d596); TD defined as the greater of the vertical and horizontal diameters (8 records).
- Gephyromantis lomorina, ZSE 94(2): 247-261 (10.3897/zse.94.21037): TD of 15 paratypes from Table 1 (holotype TD on main, desk-d575; ED rows desk-d609) (15 records).
Each record quotes the whole printed sentence or table row (cut marked where the ED-record form used a cut), names the specimen or sample by the column or row read, and states type material and the table header in conditions.

## Weak spots
- Every cell and column-to-specimen mapping is the WebFetch page reader's reading of the Pensoft preview or XML; the reader expands abbreviations in labels (not quoted). Chimerella mira quotes use the unexpanded form printed in the article XML (as the ED rows on main), whereas the preview returns the sentence with expanded abbreviations.
- Choerophryne multisyllaba Table 2: the sixth data column header is printed 'ZMB 8433' (truncated); that cell (0.6) is not filed. Choerophryne bisyllaba Table 3 (11 TyD cells) was read once in full and once returned cut off; not filed. Choerophryne crucifer was read three times, multisyllaba twice with identical cells.
- Z. yunnanensis Table 2 header (17 columns) was read once; the ED and TD cells agree with the values already filed from the same table in desk-d596 and desk-d583.
- Leptobrachella jinzhongshanensis: holotype list TEY 2.3 conflicts with the Table 3 male TEY range 1.1-1.2 (outside the tympanum diameter, not filed). Gephyromantis lomorina: UADBA 60294 TD 2.7 is high relative to its ED 3.4 but printed so; the Table sexes disagree with the Paratypes paragraph (as noted in desk-d609).

## Not filed and why
- Pristimantis pulchridormientes (ZooKeys 610): Methods list no tympanum measurement; TD = 0.5 appears only in the holotype list and conflicts with the text ratios; held out.
- Pristimantis pluvialis (ZooKeys 594): Table 1 'Tympanum diameter' row (3.0-3.7) sits next to an 'Eye diameter' row of 0.8-1.1 that desk-d458/audit 458 found misaligned with its label; TY has no separate definition; held out.
- Pristimantis cajanuma and P. quintanai (ZooKeys 864): TD in the holotype lists is on main inside the ED quotes but the Pensoft preview never appeared in own results (only PMC, optimap, orbi and plazi), so no publisher page was read.
- Pensoft ZSE and ZooKeys pages returned 'Site under maintenance' on two attempts each late in the unit: Gracixalus damingshanensis (ZSE 102(4)), Brachytarsophrys guilinensis (ZSE 101(4)), Stumpffia lynnae (ZooKeys 1104). Not filed; no non-Pensoft copy used.
- Choerophryne bisyllaba (see weak spots), Brachytarsophrys wui (tympanum hidden, desk-d574).
- Dead as briefed: Zootaxa, Phyllomedusa, salamander DOIs, Odontophrynus toledoi, Dendropsophus bilobatus, Nidirana guangdongensis, Leptobrachella shimentaina and the others in the brief.

## Desk disposition after audits (4 November 2026)

Nine fresh Opus audits (1285 to 1293) covered all 45 lines. Every value matched its paper; the faults were wording (Methods passages taken from the page reader, uncut caption cuts, missing heading statements, type material not as printed, ASW strings, and pooling stated as fact for the Pristimantis mallii and Leptobrachella jinzhongshanensis means). All were corrected with the auditors' replacement text. Line 17 (Choerophryne multisyllaba holotype TyD 0.8 mm) was dropped: the value is already carried in the conditions text of the desk-d366 TyD/ED row. Audit 1285 noted that main row d601 nests the Chimerella mira species account under Bioacoustics where the page shows it at the same heading level (owner question; not edited). Gephyromantis lomorina line 39 keeps an unresolved sex conflict (text gives 3 females, Table 1 has 4 "f" rows) stated in the record. Merged 44 of 45.
