# desk-d428 progress

Angle: eye-size records, wider net, twenty-third round. 36 records from four open Pensoft papers (log docs/views/evidence/desk-d428.jsonl). check.py and check.py --require-evidence-kind: 0 problems.

## Filed
- ZooKeys 1219: 61-72 (10.3897/zookeys.1219.137354; Wang L-Y, Mu Y-N, Yang L-X, Zhang Z-S, 2024; Cicurinidae): Cicurina chengkou, C. dabashan and Longicicurina longihamata (printed as Cicurina longihamata; WSC moved it to Longicicurina, logged 2026-05-28), male and female each, 24 records, eye_diameter_mm (Methods: 'Eye sizes were measured as the maximum dorsal diameter.').
- BDJ 12: e124006 (10.3897/BDJ.12.e124006; Zheng C-B, Mu Y-N, 2024; Phrurolithidae): Otacilia wuxi male holotype, 4 records, eye_diameter_mm (same Methods sentence).
- BDJ 12: e116569 (10.3897/BDJ.12.e116569; Liu B, Zhang F, 2024; Gnaphosidae): Xizangiana plankton male holotype and female paratype, 8 records, sensory_anatomy (Methods define no eye dimension). desk-d386 had dropped this species under the old trait rule and desk-d400 excluded it; no record of it existed.

## Weak spots
- All text came through the fetch tool as consecutive pieces of the Pensoft article_preview pages (each eye sentence joined from two pieces). The Cicurina paper's 'Taxonomy' heading was not returned; none of the three papers prints a Class or Order heading.
- Every Cicurina eye sentence prints a comma after the label ('PLE, 0.11'); values are unambiguous, recorded as printed.
- C. dabashan female: sub-heading 'Female paratypes (SWUC-T-CI-11-02, Fig. 4B) total length 3.33–4.95 (N = 2)' covers two paratypes; the eye sentence is tied only through that code. C. chengkou female: the sub-heading prints no code; the single type-list paratype SWUC-T-CI-10-02 is named by elimination.
- Otacilia wuxi: the BDJ page prints the holotype as a Darwin Core table with no catalogue number; WSC lists the holotype without a number.
- Xizangiana plankton: the quote carries figure dashes (U+2012) as returned.
- Crossref version of record not reached for any paper (UNCHECKED); licence sentences are the publisher pages' own CC BY 4.0 text as returned.
- WSC pages opened: spec-data 70775, 70776, 70777 (Cicurina), 69585 (Otacilia wuxi), 69200 (Xizangiana plankton). All accepted. Family pages not opened.

## Already on main, skipped
ZooKeys 1254 Hahnia dabashan and Sinahahnia chengkou (desk-d379); Pholcus yajiyagama BDJ 14 e193642 (desk-d382); Scytodes tanjiashui; Thelcticopis lini and Olios sericeus (desk-d409).

## Leads not filed
- Arachnology 20(1): 121-131 Trabea hirsuta, T. obscura (bioone page returned no text).
- EJT 1004 Cybaeodes (Liocranidae; only PDF links offered, none in my search results); EJT 1022 Neischnocolus tiputini (only Plazi copies reached); EJT 976 Tanasevitch Micronetinae (landing page only).
- Zoological Systematics 51(1): 1-73 Araneidae of Qomolangma, 21 new species (WSC pages only; no publisher page in my search results).
- ASP 84: 95-121 Caipira mineira, C. baiana (Pholcidae): eye values printed in micrometres, not filed.
- ZooKeys 1232 Solenysa (XML ended before the Description), ZooKeys 1229 Trilacuna (no eye sizes), ZooKeys 1245 Amaurobius/Sinoamaurobius (avoid list).
- Mutatus gen. nov. (Phrurolithidae; probably ZooKeys 1224, avoid list).
- Animals 15(2707) Eresus rubrocephalus (only repository and news copies reached).
