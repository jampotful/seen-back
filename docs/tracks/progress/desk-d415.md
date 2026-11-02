# desk-d415 progress

Angle: eye-size records, wider net, tenth round. 59 records from five open Pensoft papers (log docs/views/evidence/desk-d415.jsonl). check.py and check.py --require-evidence-kind: 0 problems for desk-d415.jsonl (other files in the tree carry older problems, not touched).

## Filed
- ZooKeys 1248: 1-16 (10.3897/zookeys.1248.150650; Wang Z-J et al., 2025; Synotaxidae): Hamus qingming (male holotype, female paratype; 8 records) and Tekellina zhangziqingi (male holotype 4, female paratype 3). sensory_anatomy ('Eye sizes and interdistances'; Methods give no eye definition; units from Methods). WSC spec-data/72383 and 72384 opened (accepted).
- BDJ 11: e102450 (10.3897/BDJ.11.e102450; Wang C, Gan J, Mi X, 2023; Selenopidae): Siamspinops yejiei female holotype and male paratype, 8 records, sensory_anatomy ('Eye sizes'). WSC spec-data/67914 opened (accepted).
- BDJ 10: e82682 (10.3897/BDJ.10.e82682; Lin, Yan, Li, 2022; Theraphosidae): Haplocosmia sherwoodae male holotype IZCAS-Ar42679, 4 records, eye_diameter_mm (Methods: 'Eye sizes were measured as the maximum diameter'). WSC spec-data/66456 opened (accepted).
- ZooKeys 1080: 1-19 (10.3897/zookeys.1080.76876; Songsangchote et al., 2022; Theraphosidae): Taksinus bambus male holotype TAK1 and female paratypes TAK3, TAK2, 12 records, sensory_anatomy ('Eye sizes', mm printed in the sentence). WSC genus page (1 accepted species, type species T. bambus) opened; no species page reached.
- BDJ 13: e137852 (printed 'Biodiversity Data Journal 13', DOI string BDJ.12; Hao, Yu, Zhang, 2025; Halonoproctidae): Latouchia calcicola, L. linmufu (male holotype and female paratype each) and L. wenchuan (male holotype), 20 records, eye_diameter_mm (label 'Eye diameters and interdistance'; units from Methods). WSC spec-data/71020, 71022, 71023 opened (accepted).

## Weak spots
- All text came through the fetch tool, which cuts long sentences; eye sentences were joined from consecutive pieces. Crossref not read for any paper (UNCHECKED); years and DOIs as printed on the publisher pages.
- Tekellina zhangziqingi female prints ALE 0.5 (probably 0.05): ALE not filed.
- Latouchia: the page prints volume 13 but the DOI reads BDJ.12.e137852; journal string follows the printed citation. Siamspinops author initials were taken from the fetch summary of the page (WSC form Wang, Gan & Mi).
- Taksinus: unit 'mm' printed in the sentence; the male sentence is one of several semicolon-joined sentences (quoted from 'The anterior eye row').
- Haplocosmia sherwoodae sits on the 'Eye sizes and interdistances' label but the Methods define eye size as a maximum diameter.

## Not filed and why
- Selenops ab female (BDJ 13 e160680, Hu, Lin, Zhong 2025; Methods define eye size as maximum diameter; WSC spec-data/61375 accepted): read, not filed to stay within the 60-line cap; a lead for the next unit. Latouchia jinyun and L. yaoi (BDJ e137852): no WSC page / no eye text reached.
- ZooKeys 1264 Pholcus jiuzhai and P. pingwu: already on main (desk-d362). ZooKeys 1245, 1240, 1247, 1200, 1286: on the avoid list.
- ZooKeys 1180 Chilobrachys natanicharum: eye values sit inside one long semicolon-joined sentence and the Methods unit sentence covers body length, not eyes: skipped. ZooKeys 1279 Tetrablemmidae, ZooKeys 1239 Orchestina, ZooKeys 1258 Gamasomorpha, BDJ 10 e85946 Raveniola yangren (eyes absent), BDJ 11 e103265 Troglocoelotes sinanensis (no eye numbers): no eye measurements printed.
- Platnickina (Evolutionary Systematics 9) and Phlogiellus khampheng: only Plazi/aggregator pages reached, skipped.

## Desk disposition after audits 738-745 (2 November 2026)
All 59 lines merged with the auditors' replacement text. Nothing dropped or held out. Counted errors 4: lines 24-27 (BDJ 10 e82682 Haplocosmia sherwoodae male holotype) carried a quote ("Eye sizes: AME 0.16, ALE 0.09 ...") that is the Siamspinops sentence and does not contain the filed values; audits 740 and 741 replaced it with the printed sentence "Eye sizes and interdistances: ALE 0.40, AME 0.33, PLE 0.32, PME 0.37; ..." (the filed values were right, the quote was wrong). Other faults are text: Crossref remarks, licence fragments, unprinted "Genus" headings, Taksinus authorities and the "Paratype ♀ TAK3:" label (WSC species page read, year 2022), Siamspinops author list now as printed ("Wang C, Gan J, Xiaoqi M"; owner question because the authority "Wang, Gan & Mi" shows Mi as the surname), specimen code TRU-SN-005 and Cheng Wang as identifier, Tekellina female ALE 0.5 misprint correctly left out.
Desk ruling: audit 742 moved line 40 (Latouchia calcicola AME 0.15) to sensory_anatomy while audits 743-745 kept eye_diameter_mm on the other Latouchia lines because the quoted sentence prints the label "Eye diameters and interdistance"; the desk set line 40 back to eye_diameter_mm for consistency within the paper. Owner question: label-only evidence (see desk-d411, d412).
Owner questions carried: DOI conflict for the Latouchia paper (page and WSC print BDJ.12, publisher XML prints BDJ.13; the printed BDJ.12 is filed); Crossref not reached.
