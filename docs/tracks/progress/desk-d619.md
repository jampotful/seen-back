# desk-d619 progress

Angle: Asian and Neotropical snakes and amphibians, eye diameter (ED) in mm per specimen (trait eye_diameter_mm, evidence_kind anatomical_measurement). OLD-ANGLE paragraph ignored. Started 4 Nov 2026. No records filed yet; searches in progress.

## Filed
- Vertebrate Zoology 73: 915-930 (10.3897/vz.73.e100889) Boulenophrys hengshanensis: 22 type specimens, Table 2 ED column, one record per specimen (22 lines).
- ZooKeys 1196: 149-175 (10.3897/zookeys.1196.114861) Rhinella kumanday: 9 specimens, Table 2 ED row (specimens as columns; 3 of the 9 are outside the type series, stated in each record). 9 lines.
- ZSE 100(2): 625-643 (10.3897/zse.100.118879) Rhacophorus qiongica: 8 paratypes, Table 3 rows. The holotype row is not filed: the holotype description prints ED 4.4 mm and Table 3 prints 4.7 mm. 8 lines.

Total: 39 records (3 papers), check.py 0 problems for desk-d619.jsonl (plain and --require-evidence-kind). About 40 WebSearches. Each paper was reached by an unfiltered title search after a filtered discovery search; authority pages (ASW) opened from my own results for B. hengshanensis, R. kumanday and R. qiongica.

## Not filed and why
- Hypselotriton huanggangensis (ZooKeys 1208: 331-346; holotype ED 3.63, Methods define ED): ASW page returned robots_disallowed on my fetch; not retried or worked around. Same as d608/d610/d612.
- Nidirana guibeiensis (ZooKeys 1135): only a male range plus one female cell in a summary row; no ASW page reached. Already rejected by d603/d605.
- Theloderma hekouense (ZooKeys 1099): named on main as covered; Table 2 ED row cut off in the XML read.
- Gracixalus huaping (ZSE 101: 369-388) and Gracixalus patkaiensis (Vertebrate Zoology 73: 557-574): no per-specimen ED (EL only for patkaiensis; no table for huaping).
- Pareas temporalis, Kalophrynus minutus, Microhyla sundaica/peninsularis, Gonyosoma coeruleum, Naja fuxi, Achalinus sheni female, Opisthotropis hungtai, Hyloscirtus and Dendropsophus papers: no ED definition or no per-specimen ED table in what the publisher pages returned; several publisher article pages return headings only.
- Rhacophorus qiongica holotype YU000691: left out because the holotype description (4.4 mm) and Table 3 (4.7 mm) disagree.

## Desk disposition after audits (4 November 2026)
Six audits (1247-1252) judged all 39 lines. Kuang et al. 2025 (Animals 15(2745), cited on the ASW page for B. hengshanensis) states that the type series of B. hengshanensis mixed two species and assigns the 2021 CSUFT specimens to the new species B. gutu. Lines 1-16 (CSUFT males) and 19-22 (CSUFT females) are therefore taxon-ambiguous and were dropped (audits 1247 and 1249 named them for dropping; audit 1248 judged lines 9-16 fixable and missed the split; the desk applied the rule for taxon-ambiguous rows to all 20). Merged: lines 17-18 (B. hengshanensis HNNU holotype and paratype, with the auditor's correction that the holotype is a male per Kuang et al.), all nine Rhinella kumanday lines (23-31) and all eight Rhacophorus qiongica lines (32-39), with the auditors' wording fixes (reader-expanded labels removed, heading paths with Family and Genus, paratype blocks as printed). Owner question: the dropped CSUFT lines cannot be refiled under B. gutu from this source because the 2025 paper does not individually re-identify them.
