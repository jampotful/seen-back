# audit-386: desk-d295, evidence lines 1 to 8

Audited 1 November 2026 from the desk-d295 files present untracked in the worktree (docs/tracks/progress/desk-d295.md and docs/views/evidence/desk-d295.jsonl, 8 lines; neither committed here, neither edited). Line numbers are the file's (1-based). HEAD equals origin/main (3f27de41). `python3 -I tools/senses/check.py | grep 'd295\.'`: "docs/views/evidence/desk-d295.jsonl: 8 records, 0 problems". Quote lengths (`len(q.split())`): 6, 2, 10, 12, 14, 17, 13, 1, all within 40; the only non-ASCII characters in any quote are en dashes (lines 3, 5, 7) and the "ø" of Møller (line 6), matching the pages.

Sources opened (WebFetch): mdpi.com/2076-2615/15/15/2216; www.mdpi.com/2076-2615/13/10/1712 (three passes); zookeys.pensoft.net/article_preview.php?id=21742; zse.pensoft.net/article/119520/download/xml/ (stopped before the Description) and zse.pensoft.net/article_preview.php?id=119520 (two passes); zookeys.pensoft.net/article_preview.php?id=186268 (two passes); zookeys.pensoft.net/article_preview.php?id=51373; zookeys.pensoft.net/article/158447/download/xml/; zookeys.pensoft.net/article_preview.php?id=131341; Crossref list queries (api.crossref.org/works?filter=prefix:...) for 10.3897 (1281, 1255, 744, 1228) and 10.3390 (both Animals DOIs). All article URLs were returned by a WebSearch first. PMC, Plazi, optimap, DOAJ, BHL, zobodat, bionames, FishBase and blog hits were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 10 WebSearches.

## Bibliographic and licence

- Line 1 (Liu, Mao, Sudasinghe, Chen, Yang, Meegaskumbura 2025). Page and Crossref same order; title identical (two pieces); Animals 15(15) 2216; issued 2025-07-28; Crossref CC BY 4.0 vor. Page prints no licence sentence; its metadata gives creativecommons.org/licenses/by/3.0/ (CC BY 3.0 page vs CC BY 4.0 Crossref, accepted by rules.md). Accepted.
- Line 2 (Wu, Wei, Lan, Du 2018). Page and Crossref same order; title identical; ZooKeys 744: 67-77, no issue; issued 2018-03-20; CC BY 4.0 vor. Page licence CC BY 4.0 sentence verbatim. Accepted.
- Line 3 (Li, Ge, Bao, Du, Luo, Zou 2023). Page and Crossref same order; title identical; Animals 13(10) 1712; issued 2023-05-22; CC BY 4.0 vor. Page "...distributed under the terms and conditions of the Creative Commons Attribution" (piece). Accepted.
- Line 4 (Shao, Cheng, Lu, Zhou, Zeng 2024). Page order matches; title identical (two pieces); Zoosystematics and Evolution 100(2): 515-529. Page licence CC BY 4.0 sentence verbatim (three pieces). Crossref list queries returned only figure components for this DOI and then client_error; no conflicting tag seen; accepted on the page sentence.
- Line 5 (Zhu, Yuan, Zhang, Zhao 2026). The unit's Crossref failure is cleared: Crossref list query gives Ting-Ting Zhu, Feng-Hua Yuan, Ren-Yi Zhang, Ya-Hui Zhao; ZooKeys 1281, 123-145; issued 2026-6-3; CC BY 4.0 vor. Page licence sentence verbatim; year 2026 printed. Accepted. The note's "the Crossref works fetch failed (client_error), so no Crossref confirmation" is now out of date (uncounted; optional replacement below).
- Line 6 (Hernández, Møller, Casane, García-Machado 2020). Page order matches; title identical; ZooKeys 946: 17-35. Page licence CC BY 4.0 sentence verbatim. The record's url is the download/xml copy; the article_preview page read here prints the same sentence. Crossref retry for this DOI hit rate limit then client_error; no conflicting tag seen; accepted on the page sentence.
- Line 7 (Chen, Mo, Du, Zhang 2025). The unit's Crossref failure is cleared: Crossref list query gives Zhuo-Ni Chen, Cai-Huan Mo, Li-Na Du, Li-Na Zhang; ZooKeys 1255, 365-377; issued 2025-10-15; CC BY 4.0 vor. XML licence CC BY 4.0 (tool summary of the sentence). Accepted. Note out of date as for line 5 (uncounted).
- Line 8 (Qin, Liu, Zhang, Shi, Du, Zhou 2025). Page and Crossref same order; title identical; ZooKeys 1228: 185-195; issued 2025-02-21; CC BY 4.0 vor. Page licence sentence verbatim. Accepted.

Bibliographic faults 0; licence faults 0; source.access "open" right throughout.

## Names and higher taxa

All eight species are described as new in the cited papers; names rest on the original descriptions (Catalog of Fishes reference pages surfaced in search for the Triplophysa 1281 and Oreonectes 1255 papers but were not opened). None is a synonym, hybrid or hatchery stock; all type material is wild-collected. Higher taxa as printed in titles: Cyprinidae/Cypriniformes (lines 1, 4), Nemacheilidae/Cypriniformes (lines 2, 3, 5, 7), Bythitidae/Ophidiiformes (line 6; "Family Bythitidae" heading printed), Cobitidae/Cypriniformes (line 8). No class filed as an order. Names faults 0.

## Trait key

eye_type is on main; values "none (...)", "reduced", "degenerated" and descriptive strings follow main. No new key.

## Duplicates

`git grep -i` on origin/main (3f27de41) under docs/ (evidence, audit/corrected, audit/ALL, sheets, searched/ included) for the eight epithets and the eight DOI suffixes. Hits: "guiyang" only as a city name in desk-d282.jsonl line 4 and audit-372.md (Caridina zhaoi, Guiyang City); zookeys.1281.186268 in desk-d281.jsonl line 2 and audit-371.md (Triplophysa zhijinensis, a different species from the same paper); "dafangensis" only in desk-d281.md line 15, "Not filed (percent of head length is not an accepted unit key; could be a companion record)"; "gibarensis" only in desk-d280.md line 16, dropped because "diameter appears only as a semicolon list and a multi-column table with misaligned headers". Both hold-out reasons concern a diameter value; lines 5 and 6 log the state only and leave the diameter unlogged, so neither reason applies. Lucifuga elsewhere on main is Eurycea lucifuga (desk-d214), another taxon. Remote research/desk-* and research/audit-* branches (1467 remote branches; d295 and audit-386 excluded), docs/views/evidence, docs/tracks, docs/views/audit and docs/views/sheets, for the eight epithets and DOI suffixes: no hit outside the main files named above. Duplicate faults 0.

## Per line

### Line 1, Sinocyclocheilus wanlanensis, degenerate (dark spots) or absent

Species description, last sentence of the head paragraph: "Eyes degenerate (dark spots) or absent." **Quote MATCH.** Diagnosis concurs ("eyes absent or degenerated into dark spots"). Holotype "GXU2020000062, holotype, 86.7 mm SL"; paratypes "GXU2020000060 and GXU2020000061, 65.8–78.6 mm SL (two specimens), same data as the holotype"; underground river in a cave, Wanlan town, Zhenfeng county, 14 November 2020; no sex stated. Conditions match, including that the split between spots and absence is not given.

**Line 1 MATCH.**

### Line 2, Triplophysa anshuiensis, none (eyes absent)

Description: "Eyes absent." **Quote MATCH.** Holotype KIZ2012005747, 65.2 mm SL, Anshui Village, Lingyun County, 12 May 2012; paratype "KIZ 2012005746, 68.5 mm SL; collected with holotype"; "No sexual dimorphism was observed in the two specimens." Conditions match.

**Line 2 MATCH.**

### Line 3, Troglonectes canlinensis, reduced

Description: "Eyes reduced, eye diameter 7.5–11.6% of the lateral head length." **Quote MATCH**; value says no more. Paratypes verbatim: "Paratypes. KIZ-GXNU202207–09, 9 ex., 29.9–54.3 mm SL, collected with holotype." No sex stated anywhere for this species.

Error (omitted contrary statement / sample composition): the same paper describes this species' eye three ways and the record gives only one. Abstract: "Troglonectes canlinensis sp. nov. can be distinguished from its congener species by the following" / "combination of characteristics: eye degenerated into a black spot; ..." Diagnosis: distinguished "from T. lingyunensis and T. macrolepis by the eye being present (vs. eye reduced to black pigment)" (tool piece). The conditions and note do not mention either, and the conditions omit the printed paratype count (9 ex., 29.9-54.3 mm SL). Fixable.

**Line 3 FIXABLE.**

### Line 4, Sinocyclocheilus guiyang, absent in 5; highly reduced and partly skin-covered in 2

Description: "Eyes absent (5) or highly reduced and partially covered with skin (2)." then "Eye orbits located in dorsal anterior part of head, filled with soft tissue." **Quote MATCH.** Abstract: "eye absent (or highly reduced)". The parenthetical numbers are not defined anywhere read (tool summary); the record says so.

Error (sample composition): the conditions say "plus seven paratypes" and that the counts "sum to seven, the number of paratypes". The page lists six paratypes: "IHB 201911140001, 1 specimen, 57.5 mm SL"; "IHB 202012250002, 1 specimen, 86.4 mm SL; collected with holotype"; "IHB 202207260001, GXU 202207260002–04, 4 specimens, 124.3–174.1 mm SL" (tool summary of the last line). Table 2 heads its column "Holotype + Paratypes (n = 7)". Seven is the whole type series, holotype included. Table 2 also gives the paratype range as 57.5-144.1 mm, against 124.3-174.1 for the last lot in the text (tool summary). Fixable.

**Line 4 FIXABLE.**

### Line 5, Triplophysa dafangensis, degenerated

Description: "Eyes degenerated; eye diameter 5.3–7.1% of head length; interorbital width 33.4–38.4% of head length." **Quote MATCH**; Abstract and Diagnosis "eye reduced, with diameter of HL (head length) 5.3–7.1%". Holotype "GZNUSLS202501291 (Fig. 6), 73.0 mm SL"; paratypes "Six specimens from the same locality as the holotype." 288-290 (37.6-71.9 mm) and 292-294 (48.1-52.6 mm); Zengjiazhai Village, Yuchong Town, Dafang County; "No secondary sexual characteristics were observed in the collected specimens."

Error (omitted variation): the Discussion says, verbatim in two pieces, "Additionally, both new species show notable intraspecific variation in pigmentation and eye development," / "ranging from moderately pigmented individuals with eyespots to fully de-pigmented and eyeless forms." "Both new species" includes T. dafangensis. No per-species split is given, and the Description range implies every measured type has an eye, but the record says nothing of eyeless forms. The conditions also say "sexes not reported" where the page says no secondary sexual characteristics were observed (uncounted, folded into the replacement). Fixable.

**Line 5 FIXABLE.**

### Line 6, Lucifuga gibarensis, pigmented eyes

Description: "Eyes pigmented (similar to the condition present in L. spelaeotes and L. lucayana (Møller et al. 2006))." **Quote MATCH**, accent kept. Holotype "MFP 18.000420, 89.3 mm SL, female, Aguada de Macigo cave"; paratypes MFP 18.000399 (69.3 mm, male, Tanque Azul cave), MFP 18.000278 (89.2 mm, male, Aguada de Macigo cave), ZMUC P771732 (45.0 mm, male, Cueva El Baga). Diameter 1.1-1.9% SL (Diagnosis) is not logged and the conditions say so. Conditions match; the paratype caves are not named (uncounted).

**Line 6 MATCH.**

### Line 7, Oreonectes qinae, normal (contrast)

Description: "Eyes normal, interorbital width greater than eye diameter, eye diameter 13.0%–22.5% of HL." **Quote MATCH.** It is a species-level statement in the Description of O. qinae, not a genus or pooled statement. Holotype KIZ2024010559, 78.6 mm SL, female; paratypes KIZ2024010560-563 (four females, 46.3-70.5 mm SL) and KIZ2024010564 (male, 52.1 mm SL); Gutingshan Forest Park, Liuzhou; collected in small surface streamlets; Discussion proposes a mainly subterranean life (tool summary). Table 1 eye diameter: females 13.0-22.5% HL, males 17.9-18.7% (tool summary); Table 1 gives the holotype as 77.0 mm SL against 78.6 in the text (tool summary). Conditions match on the points that bear on the value.

**Line 7 MATCH.**

### Line 8, Protocobitis longibarba, none (eyeless)

Description: "anterior nostril in short tube." / "Eyeless." / "Suborbital spine bifid, relatively thick and short, with strong mediolateral process in front of cavity of eye". **Quote MATCH.** Holotype "KIZ2024000004, male, 44.0 mm standard length (SL)," Yangcun Village, Luolou Town, Lingyun County; paratypes "KIZ2024000001–3, female, 51.1–51.9 mm SL", KIZ2024000005 male, ZJFRF2402010 male 53.5 mm, "KIZ2024000006–7, male, 39.5–43.1 mm SL" from Liangfeng Cave, Fengshan County. Three females and four males, 39.5-53.5 mm, as the conditions say. The holotype habitat ("subterranean tributary of the Hongshui River") was not returned in the passes read (uncounted).

**Line 8 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Sinocyclocheilus wanlanensis, degenerate or absent | MATCH | none | quote MATCH (6); type block matches; CC BY 3.0 page + CC BY 4.0 vor |
| 2 | Triplophysa anshuiensis, none | MATCH | none | quote MATCH (2); two specimens, no dimorphism observed |
| 3 | Troglonectes canlinensis, reduced | FIXABLE | conditions | quote MATCH (10); Abstract "degenerated into a black spot" and Diagnosis "eye being present" omitted; 9 paratypes not stated |
| 4 | Sinocyclocheilus guiyang, absent 5 / reduced 2 | FIXABLE | conditions | quote MATCH (12); six paratypes, not seven; n = 7 is holotype + paratypes |
| 5 | Triplophysa dafangensis, degenerated | FIXABLE | conditions | quote MATCH (14); Discussion's eyeless forms in both new species omitted |
| 6 | Lucifuga gibarensis, pigmented eyes | MATCH | none | quote MATCH (17); type block and sexes match |
| 7 | Oreonectes qinae, normal | MATCH | none | quote MATCH (13); species-level Description sentence, surface-stream types |
| 8 | Protocobitis longibarba, none | MATCH | none | quote MATCH (1); 3 female and 4 male paratypes as stated |

Errors 3 of 8 audited records (37.5%). By kind: quotes 0; value meaning 0; omitted variation / contrary statement 2 (lines 3, 5); sample composition 2 (lines 3, 4; line 3 counted once); bibliographic 0; licence 0; names 0; duplicates 0. All fixable; nothing unfixable, nothing held out. Verdict: merge lines 1-8 with the Replacement applied (lines 3, 4, 5 required; notes of lines 5 and 7 optional).

Unchecked: figures not viewed; the guiyang last paratype lot and Table 2 range, the canlinensis Diagnosis wording, the O. qinae licence sentence, habitat and Table 1, and the Protocobitis holotype habitat rest on tool summaries; Crossref was not reached for ZooKeys 946 and Zoosystematics and Evolution 100 (page sentences only, no conflicting tag); no checklist opened for current status of the eight names.

## Replacement

Each old string occurs exactly once in its field in the line named (checked with `str.count` on the desk file).

Line 3:
- `conditions`: "paratypes KIZ-GXNU202207-09" -> "paratypes KIZ-GXNU202207-09 (printed as 9 ex., 29.9-54.3 mm SL)"
- `conditions`: "is not logged, only the state" -> "is not logged, only the state; the paper words the eye differently elsewhere: the Abstract lists \"eye degenerated into a black spot\" among the distinguishing characters, and the Diagnosis separates it from T. lingyunensis and T. macrolepis \"by the eye being present (vs. eye reduced to black pigment)\""

Line 4:
- `conditions`: "plus seven paratypes (57.5-174.1 mm SL)" -> "plus six paratypes (57.5-174.1 mm SL in the text; Table 2 gives 57.5-144.1)"
- `conditions`: "(they sum to seven, the number of paratypes, but the paper does not say so)" -> "(they sum to seven, the holotype plus six paratypes, which Table 2 heads \"Holotype + Paratypes (n = 7)\"; the paper does not define the parenthetical numbers)"

Line 5:
- `conditions`: "is not logged, only the state" -> "is not logged, only the state; no secondary sexual characteristics were observed; the Discussion says both new species of the paper show intraspecific variation in pigmentation and eye development, \"ranging from moderately pigmented individuals with eyespots to fully de-pigmented and eyeless forms\", without a per-species split"

Line 5 (uncounted):
- `note`: "the Crossref works fetch failed (client_error), so no Crossref confirmation" -> "Crossref (audit-386 list query) CC BY 4.0 (vor), authors in page order, issued 2026-6-3"

Line 7 (uncounted):
- `note`: "the Crossref works fetch failed (client_error), so no Crossref confirmation" -> "Crossref (audit-386 list query) CC BY 4.0 (vor), authors in page order, issued 2025-10-15"
