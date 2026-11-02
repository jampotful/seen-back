# desk-d416 progress

Angle: eye-size records, wider net, eleventh round. 40 records (log docs/views/evidence/desk-d416.jsonl), one per labelled eye per sex. check.py: 0 problems for this file (also with --require-evidence-kind).

## Filed
- BDJ 13: e160680 (10.3897/BDJ.13.e160680; Hu, Lin & Zhong 2025; Selenopidae): Selenops ab female, 4 records, eye_diameter_mm (Methods: 'Eye sizes are measured as the maximum diameter from either the dorsal or frontal view.'). WSC species page blocked; validity rests on the WSC reference listing and the desk-d415 note.
- ZooKeys 1159: 133-150 (10.3897/zookeys.1159.101535; Zhang, Xing, Yang, Yu & Zhong 2023; Sparassidae): Sinopoda guiyang male holotype, S. xishui female holotype, S. horizontalis male topotype (first male), 12 records, eye_diameter_mm (Methods: 'Eye diameters were measured at the widest part.'). All three WSC pages opened, accepted.
- ZooKeys 1260: 111-122 (10.3897/zookeys.1260.158762; Zhang, Hu, Wang, Liu & Zhong 2025; Sparassidae): Pseudopoda rongxianensis male holotype, P. spiralis female (non-type, first female), 8 records, sensory_anatomy (no eye dimension defined). WSC pages opened, accepted.
- ZooKeys 1116: 121-132 (Sinopoda wuyiensis female, 4 records, sensory_anatomy; the male was filed in desk-d406).
- ZooKeys 1117: 71-94 (10.3897/zookeys.1117.89211; Liu, Ying & Li 2022; Phrurolithidae, new family): Edelithus puer male holotype and female, E. shenmiguo male holotype, 12 records, sensory_anatomy. WSC pages opened, accepted.

## Weak spots
- The fetch tool returns summaries and ~125-character pieces: every quote is a joined run of returned pieces, flagged in each record. Licence sentences are mostly tool paraphrases or pieces. Crossref was not read for any DOI (UNCHECKED); years for ZooKeys 1159 and 1260 come from WSC citations.
- Sinopoda xishui: printed ALE-PLE 1.44 looks like a slip (other interdistances 0.14-0.53); reported, not filed as a value.
- Edelithus puer male quote cut with [...] after the last interdistance (drops 'PME separated by slightly less than their diameters.'). E. puer female is an unidentified paratype.
- Selenops ab female is one of two non-type adults, no code printed.

## Not filed and why
- Part (a) checked: Shuqiangius (only S. chuan described), Orphnaecus (libmanan, tangcongvaca filed; O. pellitus gives eye index ranges only), ZooKeys 1116 (both species now filed).
- Scytodes tanjiashui (BDJ 14 e181164) already on main (desk-d383). Cheiracanthium (ZooKeys 1200), Phlogiellus khampheng (ZooKeys 1247) excluded list. ZooKeys 1282 Turkiye and ZooKeys 1276 Arabian Peninsula: no eye measurements printed. ZooKeys 1230 Bisetifer tactus: eyes reduced, no numbers. ZooKeys 1130 Anapistula sanjiao: no eye numbers (A. walayaku text not reached).
- Leads not reached to publisher text: ZooKeys 1159: 189-199 Pseudopoda deformis (97463; only a figure page), ZooKeys 1160 Araneus (Plazi only), Zootaxa 5679 Theraphosidae (not open), JoA 50(1) Ctenus igatu (bioone page empty), EJT 644 Bistriopelma peyoi and B. kiwicha (2020, outside the 2021-2026 window; sentences 'Eyes sizes and interdistances' with mm; open CC BY; a possible later file), Acta Arachnologica 54(2) Uloboridae (no eye numbers).

## Desk disposition after audits 746-750 (2 November 2026)
Filed 40, merged 40, counted errors 4 (Edelithus puer male quote lines 29-32 rewritten by audit 749 so the cut keeps the "diameters" clause). All other faults were text faults (licence paraphrased or cut, years credited to WSC when the page prints them, unprinted genus headings, an unreached WSC page) and are corrected from the auditors' Replacement blocks. Nothing dropped. Owner question stands: eye_diameter_mm vs sensory_anatomy where only a Methods or Description label defines eye diameters (kept eye_diameter_mm for BDJ 13 e160680 and ZooKeys 1159, sensory_anatomy for the rest). Lead: ZooKeys 1260 P. deformis female is described but not filed.
