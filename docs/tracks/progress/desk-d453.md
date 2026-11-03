# desk-d453 progress

Angle: eye-size records, wider net, round 45. 36 records from two open Pensoft papers in Zoosystematics and Evolution 100(1) (log docs/views/evidence/desk-d453.jsonl). check.py on the file: 0 problems.

## Filed (trait eye_diameter_mm: the printed sentence is 'Eye interdistances and diameters'; AME and PME only, male holotype and female paratype each)
- ZSE 100(1): 279-289 (10.3897/zse.100.115633; Yang L, He Q, Yao Z, 2024; Pholcidae): Pholcus ankang, P. baoji (8 records). WSC species pages 69405 and 69406 opened (accepted).
- ZSE 100(1): 199-221 (10.3897/zse.100.116759; Yang L, Fu C, Zhang Y, He Q, Yao Z, 2024): Pholcus jiaozuo, P. luonan, P. luoyang, P. lushan, P. shangluo, P. weinan, P. yuncheng (28 records). WSC species pages 69306, 62834, 69308/62835, 62836, 69310, 62838, 69312 opened (accepted).

## Weak spots
- Fetch tool returns summaries with sentences in pieces; eye sentences, type lines and neighbouring sentences are rejoined pieces. The P. luonan type line came only as a paraphrase (flagged in conditions).
- The species-group heading above P. luoyang, lushan, shangluo, weinan, yuncheng was not returned (only jiaozuo under the taishan group and luonan under the yichengicus group were seen); the where field omits it and conditions say so.
- Female paratype headings print a code only in the 279-289 paper (SYNU-Ar00401, -00405); in 199-221 the heading is 'Female (paratype)' with no code.
- WSC page 62835 was reached as the luoyang page and 62836 as the lushan page (the fetch tool named them); Crossref not read (DOIs as printed on the publisher page).
- Methods define no eye measurement; sentence label 'diameters' is the basis for eye_diameter_mm.

## Not filed and why
- ZooKeys 1255 Qianlingula, 1236 Belisana (avoid list). Animals 16(12) 1884 Pholcus chengkou, P. yanan (MDPI page not in search results). Acta Arachnologica 75(1) Gnaphosa hamabe (no J-STAGE article page reached). ZooKeys 1193 Pholcus fengmeii, 1282, 1276, Subterranean Biology 52 (no numeric eye values on pages reached). ZooKeys 1229 Atypus, 1255 etc. already on main.

## Desk disposition after audits (2 November 2026)
Audits 898-902 judged all 36 lines: no value, specimen, taxon, licence or repeat errors. The faults were heading paths ("Taxonomic accounts", the printed Pholcus yichengicus species group heading, the authority in species headings), run-in labels, neighbour sentences and unmarked cuts in conditions. The auditors' corrected lines replace the originals and nothing is dropped. The Methods print no eye-diameter definition; all 36 lines stay eye_diameter_mm because the quoted sentence prints "Eye interdistances and diameters" (same open owner question as d446, d447 and d452). Counted errors: 0.
