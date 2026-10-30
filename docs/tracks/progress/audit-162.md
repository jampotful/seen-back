# audit-162: desk-d72 (2 evidence records, no search records, no wanted lines)

Audited 29 October 2026 from the desk-d72 files copied untracked into the worktree (progress note and 2 evidence lines; neither is committed here). Sources checked on publisher, indexer, GBIF and WFO pages reached through the records' own URLs or WebSearch results; 7 WebSearches used. Duplicates: git grep on origin/main (c6fbbe3b) finds no "yingeri" or "hayatae" anywhere in the repository, and neither 10.2503/hortj.MI-104, 10.11623/frj.2025.33.2.04 nor the KoreaScholar article key 442783 in docs/views/evidence. Nothing is repeated or contradicted. Quote lengths counted here: 71 and 110 characters.

| line | taxon | verdict | reason |
|---|---|---|---|
| 1 | Hosta yingeri | ERROR | The J-STAGE page (opened) and the AGRIS record 675c337f0ce2cede71d40723 (opened) agree on Kim, Choi, Kim in order, The Horticulture Journal 85(3): 248-253, 2016, DOI 10.2503/hortj.MI-104, and the quote, which is whole and verbatim at 71 characters. J-STAGE labels it an Original Article. GBIF 2771232 (opened) is Hosta yingeri S.B.Jones, species, accepted. The fault is an omitted later flowering result: the abstract's last sentence says four-week-old H. yingeri required at least 26 weeks of LD duration to reach more than 50% flowering, and another sentence gives bud-bearing percentages falling from 50% to 0% as initial SD lengthened. Filed alone, "no plants flowered" under initial LD reads as long days blocking flowering, while the same abstract reports flowering after long LD exposure and a decline with longer SD. Neither the value nor the conditions carry either result, so the value misstates the study's photoperiod response |
| 2 | Aster hayatae | OK (fault noted) | KoreaScholar 442783 (opened) prints Nam Hyun Im, Dong Min Lee, Myung Suk Ahn, Hyo Beom Lee, Joonwoo Lee in order, 화훼연구 (Flower Research Journal) 33(2): 78-82, 2025, and the title as filed. The quote is whole and verbatim at 110 characters with a direction, and the SNU floriculture lab page (opened) prints the same sentence. The abstract gives three-month-old plants propagated from cuttings under 9, 12, 14 and 16 h photoperiods and A. hayatae flowering under all conditions at 92%, 85%, 65% and 27%, so method, conditions and "facultative short-day plant" are all supported, and the record carries the flowering at every photoperiod that would otherwise be an omitted exception. A set-photoperiod trial under sense_light_nonvisual. WFO wfo-0000013092 (opened) is Aster hayatae, species, accepted under Aster, with Aster ciliosus as its synonym, so the id is the species' own and the name is not moved to Kalimeris, Heteropappus or another genus there. Grade m and partial true hold |

Errors: 1 of 2 (50%). Error line: 1.

Pooled with audits 159 to 161: 1 of 11 evidence records (9.1%; audit 159 0 of 3, audit 160 0 of 2, audit 161 0 of 4, audit 162 1 of 2).

Verdict: pass on line 2 only. Line 2 can be merged; line 1 should be dropped or refiled with the 26-week LD flowering result and the bud-percentage decline in its value or conditions.

Unconfirmed names: Hosta yingeri on POWO and Aster hayatae on POWO. Both POWO pages were blocked here, as they were for the desk. GBIF 2771232 and WFO wfo-0000013092 were opened and each is the accepted species itself. The other GBIF page for Aster hayatae (5387480, opened) states no status.

Faults noted, not counted:
- Line 2: author order is confirmed by one indexer page only. The SNU lab page (opened) prints "NH Im, DM Lee, HB Lee, JW Lee", dropping Myung Suk Ahn; the four names it shares keep the same order as KoreaScholar, so the pages agree apart from the omission. No journal page was reached to settle the fifth author.
- Line 2: the SNU page prints DOI 10.11623/frj.2025.33.2.04, which the record names in its "where" field and leaves out of source.doi; my search for that DOI string returned no matching page, so the url filed instead stands.
- Line 2: the article type is not printed on KoreaScholar; Flower Research Journal is the Korean Society for Floricultural Science journal and the page carries a standard research abstract. Neither page says whether the cuttings came from wild plants or a selection; no cultivar is named.
- Line 1: the conditions field holds a growth result (height, leaves, leaf length) rather than a condition of the flowering trial.

Blocked: powo.science.kew.org/taxon/urn:lsid:ipni.org:names:181380-1 (provenance refusal; WFO read instead). worldfloradb.net results were left alone. wfoplantlist.org/taxon/wfo-4000018320-2025-06 is the genus Hosta, accepted, and gives no species status. No library proxy, ResearchGate, academia.edu or Sci-Hub page opened.

Stray files: none committed; the two desk-d72 copies stay untracked.
