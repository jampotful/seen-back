# desk-d391 progress

Angle: open-access Pensoft papers on small-eyed araneomorph families printing per-sex 'Eye sizes and interdistances' sentences. One paper filed: 45 records (log docs/views/evidence/desk-d391.jsonl), check.py 0 problems.

## Filed
- ZooKeys 1187: 91-134 (Chu C, Lin Y, Li S, 2023; Hahniidae; New genera and new species of Hahniidae (Araneae) from China, Laos, Myanmar, and Vietnam). Species: Goblinia tiane (M, F), Myahnia kanpetlet (M, F; no AME in the sentences), Troglohnia dafang, qiubei, wuding (M, F), Troglohnia shidian (F), Typhlohnia banlaksao (F; no AME). Trait eye_diameter_mm because the Methods print 'Eye sizes are measured as the maximum diameter from either the dorsal or the frontal view.' Every value was checked by script against the number printed after its own label in the quote; no value is 0.

## Weak spots
- Fetch tool returns the page in pieces and expands abbreviations in parentheses (AME (anterior median eye) 0.05); quotes are filed without the parentheses on the inference that these are tooltips (UNCHECKED against HTML).
- DOI is not in source: Crossref queries were refused or failed, so the page-printed DOI (10.3897/zookeys.1187.112936) sits in the note only; version of record UNCHECKED.
- Headings higher than the species heading were returned only for Goblinia, Myahnia and T. dafang; the others assert the species heading only. Sex sub-headings were not returned for shidian, wuding, banlaksao (heading 'Description' only); measured specimen not tied to a code for wuding and shidian.
- WSC accepted: dafang, qiubei, shidian, wuding, banlaksao, Myahnia kanpetlet; Goblinia tiane seen only on the genus list page (no status text).

## Not filed and why
- Typhlohnia rongshui, T. sondoong, T. suiyang (same paper): page excerpt cut off before their eye sentences. T. kaiyang: eyes absent (no sentence). Lead: re-read later part of ZooKeys 1187 for these three.
- Pholcus fengmeii (ZooKeys 1193.115640): sentence is 'Eye interdistances and sizes', no PLE, ALE not sized. Orchestina (ZooKeys 1195.117666): eyes 'well developed, nearly equal-sized', no numbers. Hahnia dabashan/Sinahahnia chengkou/S. eyu/fanjingshan and Hahnia jiangkou: already on main (desk-d379, d311) or listed in desk-d292.
- Zoosystematics and Evolution 100 papers (zobodat copies) not used: third-party copy.
- No Ochyroceratidae, Telemidae, Nesticidae, Leptonetidae, Linyphiidae publisher pages for 2022-2026 reached in search results.

## Desk disposition after audits 604-609 (2 November 2026)
All 45 lines (ZooKeys 1187: 91-134, Chu, Lin & Li 2023, Hahniidae: Goblinia tiane, Myahnia kanpetlet, Troglohnia dafang/qiubei/shidian/wuding, Typhlohnia banlaksao) were audited by fresh Opus agents (audits 604 to 609). Quotes and values were exact on every line; the abbreviation expansions that the fetch tool showed are xlink:title tooltips in the article XML, so the unexpanded quotes are what is printed. Counted errors: 12 lines (Troglohnia shidian and wuding specimen statements said "not named"/no code where the page prints "Female (holotype ...)", "Male (holotype ...)", "Female (paratype IZCAS-Ar44695; ...)"). Faults on all lines: incomplete where paths, DOI missing from source. Every line was replaced with the auditor's corrected text and merged; none dropped. The DOI 10.3897/zookeys.1187.112936 is in source on the strength of the publisher page (Crossref was not reached by the unit or the auditors): owner question whether a page-printed DOI suffices where Crossref cannot be reached. Trait eye_diameter_mm confirmed (Methods: "Eye sizes are measured as the maximum diameter"). Leads: Typhlohnia rongshui, sondoong, suiyang in the same paper (eye sentences not read).
