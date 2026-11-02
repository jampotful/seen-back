# desk-d364 progress

Angle: multi-species taxonomic papers outside spiders. 10 records filed (target 16), about 41 WebSearch/WebFetch calls.

## Filed (docs/views/evidence/desk-d364.jsonl)
- ZooKeys 1275: 81-115 (10.3897/zookeys.1275.158254; page-printed CC BY 4.0, Crossref CC BY 4.0 vor): eyes_count "8+8" for Lepidodens maculata, Lepidosira cheni, L. guilinensis, L. montis, Willowsia zhangi (Entomobryidae). 5 records.
- Subterranean Biology 34: 61-98 (10.3897/subtbiol.34.49586; page-printed CC BY 4.0, Crossref CC BY 4.0 vor): eyes_count (eye spots) for Parobisium motianense 4, qiangzhuang 4, sanlouense 4, tiani 2 (Neobisiidae). 4 records.
- ZooKeys 1255: 1-25 (10.3897/zookeys.1255.164170): Acherontiella palaciosi eye_type none. 1 record (A. nezamdoosti already on main, desk-d282).

## Weak spots
- Parobisium sentences are 43-44 words uncut; quotes cut the setae clause with an ellipsis. "Eye spots" is the paper's wording, filed as a count of spots.
- Collembola.org page opened only for genus-level checks; the new Entomobryinae species epithets are unchecked on a registry. No registry for A. palaciosi; its order was taken from main.
- All text read through a summarising fetch tool; ZooKeys XML downloads truncate (about 83k characters), article_preview pages returned whole Descriptions.
- Crossref list query for 49586 did not return the article; the direct works/ DOI URL did.

## Not filed
- Pseudosinella hartnerae (ZooKeys 1063, 73094): single new species, "With 5+5 eyes (ABCDH, ...)", not opened further.
- Tyrannochthonius, Guangxi, EJT 1058 (Zenodo 20445088): eleven new species, not opened.
- ZooKeys 1232, 1253 leads not reached.

## Desk disposition after audits 483 and 484 (2 November 2026)

Audit 483 (lines 1-5, ZooKeys 1275 Collembola, eyes 8+8) found 0 errors; its Replacement carries uncounted tidying only (note cuts marked, registry page truncation noted, depository added for line 4). Audit 484 (lines 6-10) found 2 of 5 in error (40%, 3 faults): the Parobisium motianense and P. tiani quotes dropped the run-in "Carapace (Figs ...):" label, so they started mid-sentence, and the P. tiani note called the eye spots "reduced", a word the paper does not use. Lines for P. qiangzhuang, P. sanlouense and Acherontiella palaciosi passed. The World Arachnida Catalog pages were not reopened by the auditor; new species names remain unverified on a registry page. Replacement lines merged (the two corrected quotes included); check.py 0 problems.
