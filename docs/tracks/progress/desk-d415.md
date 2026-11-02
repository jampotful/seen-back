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
