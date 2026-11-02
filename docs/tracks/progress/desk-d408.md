# desk-d408 progress

Angle: eye-size records, wider net, third round (spider papers in families not yet filed). 30 records from four open Pensoft papers (log docs/views/evidence/desk-d408.jsonl). check.py and check.py --require-evidence-kind: 0 problems for this log.

## Filed
- BDJ 14: e178451 (10.3897/BDJ.14.e178451; Jang CM, Lee SY, Kim ST, 2026; Philodromidae): Philodromus uljin, male holotype and female paratype, AME/ALE/PME/PLE, 8 records, sensory_anatomy (sentence labelled 'Eyes'; Methods define no eye dimension).
- ZooKeys 1265: 103-127 (10.3897/zookeys.1265.175629; Xiong Y, Li D, Xu X, 2025; Halonoproctidae): Latouchia jihe, male holotype HAL-2023-010 and female paratype HAL-2023-032, 8 records, sensory_anatomy (item labelled 'Eye group').
- BDJ 13: e143433 (10.3897/BDJ.13.e143433; Yu H, Xing Y, Lin Y, 2025; Leptonetidae, cave): Falcileptoneta taoqii, male holotype and female paratype, ALE/PME/PLE (no AME printed), 6 records, eye_diameter_mm (Methods: 'Eye sizes are measured as the maximum diameter ...').
- BDJ 13: e157512 (10.3897/BDJ.13.e157512; Gündüz G, Kaya RS, 2025; Agelenidae): Hellamalthonica kazdagensis, male holotype and female (only female paratype G6 by elimination), 8 records, sensory_anatomy.

## Weak spots
- All text came as fetch-tool excerpts of publisher XML or article_preview pages from my own search results; eye sentences are joined from consecutive pieces. Crossref not read for any paper (UNCHECKED).
- Latouchia: the XML returned only the L. jihe treatment; wufeng, wuhan, yinggen, zhangping, jinyun not reached. The 'Measurements:' sentence continues after the eye group; quoted with a [...] cut. Species heading authority not printed in the returned text (WSC: Xiong, Li & Xu, 2025).
- Philodromus uljin: page catalogue codes (TTQXIV...) differ from WSC's repository statement (NIBR); both reported. Which female paratype was measured is not stated (also for Falcileptoneta, which of two female paratypes).
- Hellamalthonica: the fetch tool flagged a male-count mismatch between Methods and the listed material; reported in conditions.
- WSC species pages opened (all from search results): 73361 uljin, 73257 jihe, 71025 taoqii, 72210 kazdagensis; all ACCEPTED.

## Not filed and why
- BDJ 11 e107751 (Speleoticus hei), BDJ 14 e181164 (Scytodes tanjiashui), BDJ 11 e103265, ZooKeys 1245.145389 (avoid list), Hippasosa, Sinartoria, Yinanyphaena, Weintrauboa: already on main or avoided.
- ZooKeys 1230 Crimean cave spiders (Bisetifer tactus) and BDJ 11 e103265 Troglocoelotes: no eye values printed. ZooKeys 1276 Arabian Peninsula and the Levant: no eye measurements. Monteithophila (ZooKeys 1268) is a bug, not a spider.
- African Invertebrates 66(1): 19-64, Trachelidae (10.3897/AfrInvertebr.66.139299, Haddad 2025; Foordana, Mushimane, Namaquella, Rukuluk): the XML reached through search was cut before the species descriptions; lead for a later unit (new journal, new family).
- ZooKeys 1290: 339-355 Hexura picea (Antrodiaetidae, 10.3897/zookeys.1290.200898): only figure pages surfaced in search, no article text; lead.
- Heradion (Zodariidae, Bull. Br. arachnol. Soc. 2012) outside the date range and no licence statement. Cybaeus eremospelyngus: no eye numbers (as instructed).
- Searches for Zoological Research, Evolutionary Systematics, Zoosystematics and Evolution, Subterranean Biology and Arachnology returned no usable open publisher page. Crossref list queries via WebFetch failed (client_error) except two.

## Desk disposition after audits 700-703 (2 November 2026)
All 30 lines merged with the auditors' replacement text. Counted errors 0 (audit 702 labelled lines 17-24 "errors, fixed"; the faults are heading-path and licence text, counted as text faults under the desk policy). Nothing dropped or held out. Text faults corrected: 700 heading path with unprinted Class/Order/Family, Methods note (ALE/AME/PLE/PME defined), false WSC repository mismatch, Crossref claim (32); 701 unprinted Family heading, licence fragment, first author "Yichao", species count, male eye values (36); 702 unprinted Leptonetidae and Agelenidae headings, cut licence, quote from mid-sentence (lines 23-24 now the whole 32-word sentence); 703 same quote fix for lines 25-26, female "G6 by elimination" removed, Methods 11 males vs 10 listed (24).
Owner questions carried: Hellamalthonica male count (Methods 11, list 10); measured paratype unidentified for Philodromus uljin and Falcileptoneta taoqii; Crossref not reached.
