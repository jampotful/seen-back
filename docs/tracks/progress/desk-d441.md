# desk-d441 progress

Angle: eye-size records, wider net, thirty-sixth round. 40 records (log docs/views/evidence/desk-d441.jsonl), check.py 0 problems for the file (the one problem the repo-wide --require-evidence-kind run prints is sweep-98.jsonl, not this unit).

Note: the brief named the worktree /tmp/dcd440, which does not exist; the worktree that does exist on branch research/desk-d441 is /tmp/dcd441, and all work was done there.

## Filed
- ZooKeys 1191: 75-88 (10.3897/zookeys.1191.117592; Gea jingdong, Araneidae): male holotype and female paratype, four eyes each (8 records), sensory_anatomy ('Eye sizes and interdistances', Methods give no eye-size definition). WSC page 62762 accepted.
- ZooKeys 1157: 163-176 (10.3897/zookeys.1157.99674; Wu, Chen, Zhang 2023; Clubionidae): Clubiona bidactylina, C. camela, C. subhuiming, male and female, 24 records, eye_diameter_mm because the Methods say 'Eye sizes were measured as the maximum diameter of the lens in dorsal or frontal view.' WSC pages 67886 (camela) and 67887 (subhuiming) accepted; C. bidactylina WSC page not reached (UNCHECKED).
- Biodiversity Data Journal 12: e137014 (10.3897/BDJ.12.e137014; Otacilia subshanxi, Phrurolithidae): male holotype, female paratype (8 records), sensory_anatomy; Methods print the millimetres sentence. WSC page 70533 accepted. desk-d332 had listed this paper among those dropped for bare values; the unit sentence is in the Methods.

## Weak spots
- All text came through the fetch tool's summaries, so eye sentences were requested in consecutive pieces and rejoined; Clubiona type lines were cut by the tool at about 125 characters (stated in conditions). Female measured specimens are not named in the Clubiona paper.
- Licence for Clubiona and Otacilia is the tool's summary of the CC BY 4.0 line, not a verbatim sentence (stated in notes). Crossref not read for any paper.
- Class and Order headings were not printed in the text returned (stated in conditions).

## Not filed and why
- Eriovixia pengi, wangchengi, yaoi, yinae, zhengi (ZooKeys 1034): the XML and preview pages returned stop before the descriptions; no eye sentences reached.
- Sinahahnia (ZooKeys 1197), Cheiracanthium bannaensis and bifurcatum (ZooKeys 1200): already on main.
- Zangaraneus zhishengi (BDJ 14 e199306) and Spartaeus yingdeensis (ZooKeys 1282): on the brief's skip lists.

## Desk disposition after audits (2 November 2026)

Audits 852-856 judged all 40 lines (Gea jingdong, ZooKeys 1191: 75-88; Clubiona bidactylina, C. camela, C. subhuiming, ZooKeys 1157: 163-176; Otacilia subshanxi, BDJ 12: e137014). No wrong taxa, quotes or values and nothing dropped. WSC species pages were opened for all five species (accepted). The Clubiona Methods print the lens-diameter definition and "All measurements are in millimetres", so eye_diameter_mm stands for lines 9-32; the Gea and Otacilia Methods define no eye dimension, so sensory_anatomy stands. Text faults corrected by replacement text: licence quoted from the fetch summary instead of the printed CC BY 4.0 sentence (Clubiona, Otacilia), doubled "male male" and "female female" wording, unsourced Crossref claims, WSC marked unchecked, heading paths missing the printed classification block, type-block fragments not copied as printed. All 40 merged.
