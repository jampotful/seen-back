# desk-d382 progress

Angle: unopened leads from d381. 44 records from three open Pensoft papers (unit name d382; log docs/views/evidence/desk-d382.jsonl). check.py: 0 problems. Values were extracted by script from each record's own eye label (interdistances and CH excluded).

## Filed
- ZooKeys 1292: 141-157 (10.3897/zookeys.1292.196539; page prints CC BY 4.0; Crossref CC BY 4.0 vor): Pseudopoda chengkouensis, liyihangi, maolanensis (Sparassidae), male and female, AME/ALE/PME/PLE; 24 records, eye_diameter_mm (Methods: 'Eye diameters were taken at the widest point.').
- ZooKeys 1296: 63-75 (10.3897/zookeys.1296.205589; page prints CC BY 4.0; Crossref CC BY 4.0 vor): Poeciloneta duinanensis and jidingensis (Linyphiidae), male holotype and female paratype, four eyes each; 16 records, eye_diameter_mm (Methods: 'Eye sizes were measured at the maximum dorsal diameter.').
- BDJ 14: e193642 (10.3897/BDJ.14.e193642; page prints CC BY 4.0; Crossref CC BY 4.0 vor): Pholcus yajiyagama, male holotype and female paratype, PME and AME; 4 records, eye_diameter_mm (the sentence prints 'Eye interdistances and diameters'). WSC spec-data/73639 opened (Pholcidae, accepted).

## Weak spots
- All text came through WebFetch answers in line pieces; two pieces of each eye line were joined (stated in each note). Punctuation (en dashes, the printed 'AME–ALE, 0.07,' comma in two Poeciloneta female sentences) is as returned.
- The article_preview pages for 196539 and 205589 were fetched without that exact URL appearing in a search result (id taken from the DOI suffix); the pages themselves printed the DOI and licence. Disclosed in each note.
- WSC species pages for the three Pseudopoda and two Poeciloneta species were not found in search: UNCHECKED, owner question in each note.
- Methods were read through fetch-tool lists, not the full printed section; notes say so. Pseudopoda female specimen codes are not given in the Description (paratype series listed).
- Pholcus yajiyagama type-locality lines were not read.

## Not filed
- Scytodes tanjiashui (BDJ 14: e181164, 10.3897/BDJ.14.e181164; WSC spec-data/73360 opened, accepted; page prints CC BY; Crossref unreachable): PME/ALE/PLE for male holotype ASM-JGSU-Ara6782 and female paratype ('Eye sizes and interdistances' sentence, sensory_anatomy) collected but not filed to keep to the target; a ready lead.
- Shaanxinus (ZooKeys 1296: 10.3897/zookeys.1296.213068; Irfan, Rehman, Wang, Zhang; 5 new species, 'Eye sizes were measured as the maximum dorsal diameter.'; about 36 records of 'Eye sizes and interdistances' sentences, males of baitianhe, kuankuoshui, liangdang, micangshan, zhongzhai and females of liangdang, micangshan): opened, not filed. Lead for the next unit.
- Tetrablemmidae (ZooKeys 1279.189587) and Zora (ZooKeys 1287.203444): no numeric eye sizes. Dropped.
- Other leads (BDJ e183760, e182063, ZooKeys 1276/1282 faunistic): not opened.

## Desk disposition after audits 553-558 (2 November 2026)
4 of 44 records merged (Pholcus yajiyagama, BDJ 14: e193642, lines 41-44, with audit 558's replacement lines; all 4 in error in conditions and the unit field, none in value, quote or trait). The other 40 records are DROPPED (held out, not merged; the jsonl on main holds only the 4). Cause: the desk fetched the ZooKeys 1292 (10.3897/zookeys.1292.196539) and ZooKeys 1296 (10.3897/zookeys.1296.205589) article pages at URLs built from the DOI suffix that never appeared in a search result, and five auditors (553-557, 70 searches in all) could not reach either publisher page from search results, so the quotes, dashes, specimen codes, Methods and licence on the exact copy could not be verified (a record whose page the auditor cannot open is held out). Dropped: Pseudopoda chengkouensis (1-8), liyihangi (9-16), maolanensis (17-24), Poeciloneta duinanensis (25-32), jidingensis (33-40). The values matched the Plazi/Zenodo copies (CC0) where the auditors could read them, so these remain leads for a later unit that reaches the publisher pages through search results: ZooKeys 1292: 141-157 and ZooKeys 1296: 63-75. Audit findings worth keeping: Pseudopoda paratype series lack 'Qianle Lu & Luyu Wang leg.' in the desk's conditions; the DOI 10.3897/zookeys.1292.196539 appears in two progress files as a lead only; the Poeciloneta jidingensis female code SWUC-T-LIN-39-02 is unverified; the World Spider Catalog pages for the Pseudopoda and Poeciloneta species are unchecked.
Owner question: none new. Lesson for units: open WebFetch pages only at URLs returned by a WebSearch of the same unit; set the unit field to desk-dNNN.
