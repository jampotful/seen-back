# desk-d442 progress

Angle: eye-size records, wider net, thirty-seventh round. 52 records from three open papers (log docs/views/evidence/desk-d442.jsonl). check.py and check.py --require-evidence-kind: 0 problems for this file. About 37 WebSearches used. Pensoft article_preview and XML pages returned "Site under maintenance" for part of the unit (ZooKeys 1239, Evolutionary Systematics 196576), and worked for the rest.

## Filed
- ZooKeys 1034: 199-236 (10.3897/zookeys.1034.60411; Mi X, Li S, 2021; Araneidae), publisher article_preview page (CC BY 4.0 sentence printed): Eriovixia zhengi, E. yinae, E. yaoi, E. wangchengi, male holotype and female paratype each, AME/ALE/PME/PLE, 32 records, sensory_anatomy (sentence prints 'Eye sizes and interdistances'; the 14 Methods sentences define no eye dimension). WSC species pages 65763, 65761, 65760, 65759 opened (accepted). Complements desk-d440 (E. ganae, E. liuhongi, E. tangi).
- ZooKeys 1233: 139-193 (10.3897/zookeys.1233.128056; Acuña DC et al., 2025; Theraphosidae): Selenobrachys ustromsupasius (male holotype UST-ARC 0002) and S. philippinus (male PASI ara0006, first description of the male per WSC), 8 records, eye_diameter_mm (Methods: 'Eye diameter is measured through the widest point or the major axis.'). WSC pages 71558 and 44350 opened (accepted).
- PeerJ 12: e16781 (10.7717/peerj.16781; Yu K-P, Kuntner M, 2024; Dolomedes, WSC family Dolomedidae, paper prints Pisauridae): Dolomedes bedjanic (male holotype, female paratype) and D. hydatostella (male holotype printed 'collected as sub adult'), 12 records, sensory_anatomy (label 'Diameters of AME', no Methods definition). WSC pages 69344 and 69345 opened (accepted).

## Weak spots
- The fetch tool paraphrases or refuses long verbatim passages; eye sentences and type lines were obtained by narrow repeated requests and rejoined from pieces (marked in conditions). E. wangchengi type lines are partly summarised from the XML reading (marked 'summarised'); E. yaoi paratype list stops after two entries; E. zhengi later paratype entries abbreviated.
- The Subfamily line above 'Tribe Yamiini' in ZooKeys 1233 was not returned; no Class or Order heading is printed in any of the three papers' text.
- Dolomedes: the eye sentences are over 40 words, quoted to the semicolon with the cut marked [...] and the cut text given in conditions. The PeerJ HTML page returned no licence line; the licence line 'Distributed under Creative Commons CC-BY 4.0' was read on the publisher PDF (URL from my search results). Family field uses the current WSC family Dolomedidae.
- Crossref not read for any paper (UNCHECKED); DOIs are those printed on the pages.
- Eriovixia male zhengi: the tool returned the eye sentence in two lines; a follow-up request confirmed the comma after 'PME–PLE 0.35'.

## Not filed and why
- Eriovixia pengi (ZooKeys 1034): Description reads 'See Mi et al. (2010)', no eye values.
- Dolomedes gregoric (PeerJ 12 e16781): eye sentences read (male holotype AME 0.41, ALE 0.30, PME 0.57, PLE 0.61; female paratype 0.49, 0.32, 0.65, 0.63) but no WSC species page appeared in my search results; D. rotundus and the D. hydatostella female: text not reached.
- Idiosoma ganbarrga, I. garrawarla (AJT 118): only eye-separation ratios. Herennia (Diversity 18(1): 54): all filed species already on main; H. tsoi male prints PME 0.73 (probable typo), left out. ZooKeys 1241, 1257, 1137, 1072, 1215 (Trachelas): every species already on main. ZooKeys 1218 and 1169: avoid list. ZooKeys 993 Trachelas crewsae (2020): outside the window and no eye values. ZooKeys 460 Linyphiidae (2014): outside the window.
- Not reached to publisher text: ZooKeys 1173 Araneus yuboi, shii, wanghuai, yangchuandongi (only Plazi, figure and WSC pages); ZooKeys 1239 Houcosa and the other two wolf-spider genera (maintenance); ZooKeys 1226 and ZooKeys 1159 Pseudopoda deformis (figure pages only); Ctenus igatu (BioOne page returns metadata only); Evolutionary Systematics article 196576 (maintenance).

## Leads
- PeerJ 12 e16781: Dolomedes gregoric once its WSC species page is reached (the PDF text is in two windows: HTML text at offset 0 and 60000 shows bedjanic/hydatostella, the PDF at offset 52000 shows kalanoro and gregoric).
- ZooKeys 1034: Eriovixia yaoi paratype list beyond two entries.

## Desk disposition after audits (2 November 2026)

Audits 857-863 judged all 52 lines (Eriovixia zhengi, E. yinae, E. yaoi, E. wangchengi, ZooKeys 1034: 199-236; Selenobrachys ustromsupasius male holotype and S. philippinus male, ZooKeys 1233: 139-193; Dolomedes bedjanic male and female and D. hydatostella male, PeerJ 12: e16781). No wrong taxa, quotes or values and nothing dropped. WSC species pages confirmed accepted for all species (Dolomedes in Dolomedidae while the paper prints Pisauridae). The Selenobrachys Methods define eye diameter in mm, so eye_diameter_mm stands for lines 33-40; the Eriovixia and Dolomedes Methods define no eye dimension, so sensory_anatomy stands. Text faults corrected by replacement text: incomplete or summarised type-material blocks (Eriovixia zhengi, E. yaoi, E. wangchengi), missing printed Family and Subfamily headings (Selenobrachys), missing Species group headings (Dolomedes), a lead-in cut without a cut mark, an inferred "(not a type)" and stale main commit citations. All 52 merged.
