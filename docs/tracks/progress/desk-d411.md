# desk-d411 progress

Angle: eye-size records, wider net, sixth round. 60 records from three open Pensoft papers (log docs/views/evidence/desk-d411.jsonl). check.py and check.py --require-evidence-kind: 0 problems. Every value was also checked by script against the number printed after its label in its own quote.

## Filed
- Evolutionary Systematics 10(2): 217-261 (10.3897/evolsyst.10.196576; Dupérré N, Tapia E, Salazar-Valenzuela D, 2026; Theraphosidae): Yunka suenos, Y. guasaganda, Y. baboso (all new) and Homoeomma josti, each male holotype and female paratype, AME/ALE/PME/PLE, 32 records, sensory_anatomy (label 'Eyes'; Methods define no eye dimension). WSC: Yunka suenos page 73916 opened (accepted); refincluded/19246 lists all five new species as original descriptions. Yunka suenos female AME 0.88 is far above the printed ALE 0.56; filed as printed and flagged in conditions.
- Biodiversity Data Journal 10: e91350 (10.3897/BDJ.10.e91350; Lu Y, Chu C, Yao Z, Li S, 2022; Ctenidae): Anahita menglun, Bowie haiphong, Bowie mengla, Bowie zhengi (males) and B. zhengi female, plus the first female description of Sinoctenus zhui, 24 records, eye_diameter_mm (sentence prints 'Eye diameters and interdistances'). WSC pages for A. menglun, B. haiphong, B. zhengi opened (accepted); B. mengla only through refincluded/16721.
- Biodiversity Data Journal 10: e90967 (10.3897/BDJ.10.e90967; Wu Y, Li Z, Yang Y, Yang Z, 2022; Macrothelidae): male holotype of Macrothele washanensis (WSC name now Orientothele washanensis), 4 records, sensory_anatomy ('Eye sizes and inter-distances'). WSC page for O. wuliangensis (60779) opened; washanensis only through refincluded/16823.

## Not filed and why
- Macrothele washanensis female: print truncated ('PLE-PME 0.') and 'ALE-AME0.24'. M. wuliangensis male prints 'PME0.45'; female sentence complete but left out with the male to keep the paper to the clean sentence (lead for a later unit: wuliangensis female AME 0.58, ALE 0.70, PME 0.50, PLE 0.56).
- Romopelma chirapa (same Evolutionary Systematics paper): male sentence prints 'ALE 0.39 PME 0.26' without a comma; both sexes are a lead (Eyes on low mound: male AME 0.27, ALE 0.39, PME 0.26, PLE 0.36; female AME 0.33, ALE 0.37, PME 0.29, PLE 0.35).
- Shuqiangius: only S. chuan is new in ZooKeys 1261 (S. rarobulbus is a new combination). Orphnaecus: the third species is a redescription.
- ZooKeys 1230 (Crimean cave spiders): no numeric eye data. Pholcidae papers (ZSE 100(1) 279-289; ZooKeys 1156): not opened for eye text. Scytodes tanjiashui is on main (desk-d383). ZooKeys 1245/1247/1255/1210 are on the avoid list.
- Acta Arachnologica and Zoological Research searches reached only index or aggregator pages.

## Weak spots
- Fetch tool returns pieces of at most about 125 characters; eye sentences were joined from consecutive pieces. Sentences following the eye sentence were not returned for most Yunka records (said in conditions).
- Licence statements are the pieces returned (first clauses for e91350). Crossref not read for any paper (UNCHECKED); no Crossref claim made.
- Class heading is not printed in any of the three papers; the printed Order or species headings are given.
- Branch greps of research/desk-d405 to d410 evidence logs were run with short time limits and returned no match.
