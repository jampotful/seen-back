# audit-362: desk-d270, evidence lines 1 to 4

Audited 1 November 2026 from the desk-d270 files present untracked in the worktree (docs/tracks/progress/desk-d270.md and docs/views/evidence/desk-d270.jsonl, 9 lines; neither committed here, neither edited). Lines 5 to 9 go to another auditor. Worktree HEAD and origin/main 6d94bb12 (merge of d267 after audit 360). `python3 -I tools/senses/check.py | grep 'd270\.'`: "docs/views/evidence/desk-d270.jsonl: 9 records, 0 problems". Quote lengths (`len(q.split())`): 20, 20, 24, 24, all within 40. Non-ASCII in quotes: "±" (U+00B1) in all four; "μ" (U+03BC, Greek mu) twice and "…" (U+2026, inside the cut mark "[…]") in lines 3 and 4; units field of lines 3 and 4 is "µm" with the micro sign U+00B5, as main writes it. Format model audit-358.md; desk-audit.md evidence clause (40-word limit, no 125-character limit); abutting pieces judged under the six conditions of audit-324.md, cuts under audit-331.md.

Confirmed by reading the file: lines 1 to 4 are Arge similis (Wen et al. 2022, Insects 13(2): 152, 10.3390/insects13020152): line 1 ommatidia_count 2022 male, line 2 ommatidia_count 2223 female, line 3 facet_diameter_um 17.4 male, line 4 facet_diameter_um 18.26 female.

Sources opened (WebFetch): www.mdpi.com/2075-4450/13/2/152 (four passes); api.crossref.org/v1/works/10.3390/insects13020152 (first try rate-limited, second answered; not robots_disallowed); zenodo.org/records/12760232 (Plazi treatment record). Two Plazi GgServer pages returned only a redirect notice and gave nothing. PMC (ncbi.nlm.nih.gov/pmc/PMC8880150), the rcastoragev2 blob PDF (third-party copy), ouci.dntb.gov.ua, Wikipedia and its mirrors were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 2 WebSearches.

## Bibliographic and licence

- Crossref: Chao Wen, Zijian Pan, Shiping Liang, Liming Shen, Xiujun Wen, Cai Wang, in that order; title "Fine Structure of the Visual System of Arge similis (Hymenoptera, Argidae)", identical to the record; Insects, volume 13, issue 2, article 152; issued and published online 2022-01-30; journal-article; one licence entry, https://creativecommons.org/licenses/by/4.0/, content-version vor, delay 0, start 2022-01-30; relation empty ({}), no update-to.
- Page: byline the same six names in the same order; citation line verbatim "Insects 2022, 13(2), 152; https://doi.org/10.3390/insects13020152". The page prints no article licence sentence; it carries MDPI's site-wide permissions text ("For articles published under an open access Creative Common CC BY license" ...) and rights metadata http://creativecommons.org/licenses/by/3.0/. Under the LICENCE ruling (CC BY 3.0 page vs CC BY 4.0 Crossref vor) accepted, and the desk's note describes this correctly.
- source.authors "Wen C, Pan Z, Liang S, Shen L, Wen X, Wang C", year 2022 (printed), journal "Insects 13(2): 152", DOI and URL right; access "open" right. Bibliographic faults 0; licence faults 0.

## Names

- docs/views/gaps/gbif-names.tsv line 414: "Arge similis	EXACT	ACCEPTED	Arge similis	Arge	5868174". Accepted, not a synonym.
- The paper's own abstract prints "Arge similis (Vollenhoven, 1860)". The Zenodo/Plazi treatment record gives "Arge similis (Snellen van Vollenhoven, 1860)", family Argidae, order Hymenoptera, no synonym statement (tool summary of the record's metadata; the source publication is a 2021 paper in the Bulletin of the National Museum of Nature and Science, Series A, Zoology 47(4), whose author list I did not verify). The authority is Snellen van Vollenhoven, 1860, not Fallén; the records carry no authority, so nothing to fix.
- Family Argidae and order Hymenoptera: the paper's title "(Hymenoptera, Argidae)" and the Plazi record agree. Name faults 0.

## Duplicates

git grep on origin/main (6d94bb12) across the whole docs/ tree (including docs/views/audit/corrected, audit/ALL.jsonl, sheets, searched/, wanted) for "Arge similis", "13020152" and Argidae: main holds one Arge similis evidence record from this DOI, eye_type "apposition compound eyes" (external-2.jsonl line 4, corrected as recheck-26-fixed.jsonl line 3; audit/ALL.jsonl line 5240). Its conditions and note give no facet count or diameter, and no sheet, searched record or main-row note cites 2022, 2223, 17.40 or 18.26 for this paper (sweep-97.md says only that the paper "gives eye type and facet counts only"). The 154 remote branches matching origin/research/desk-d2* and origin/research/audit-3* hold no Arge similis record beyond what main has (only audit-300, which carries main's files). Lines 1 and 2, and lines 3 and 4, are distinct per-sex measurements from one sentence each, each value carrying only its own number. Duplicates 0.

## Trait keys

check.py TRAITS (main and this worktree are the same commit) contains neither ommatidia_count nor facet_diameter_um; line 32 admits an unlisted key when the note says "new trait", which all four notes do, so using them is allowed. Both keys are in use on main: ommatidia_count in oa-2, oa-3, oa-5, oa-6, oa-14, recheck files and audit/corrected/methods.jsonl (units "count" 15, "ommatidia/eye" 17, "ommatidia" 5, "ommatidia per compound eye" 1); facet_diameter_um in oa-2, oa-4, oa-5, oa-11 and recheck files (units "µm" in all 42). Lines 3 and 4 match main's units. Lines 1 and 2 use "facets per compound eye", a new spelling of main's "ommatidia/eye" (uncounted; replacement offered below). Trait-key faults 0.

## Per-record findings

### Lines 1 and 2, ommatidia_count, male 2022 and female 2223

Abstract sentence verbatim in one piece: "Each compound eye contains 2022 ± 89 (mean ± SE) facets in males and 2223 ± 52 facets in females." The sentence before ("External morphology and ultrastructure of the visual system of Arge similis (Vollenhoven, 1860) adults were investigated" ...) and after ("Arge similis has an apposition kind of compound eye composed of a cornea" ...) seen. **Quote MATCH**, 20 words, "±" with spaces as printed; whole sentence; value says no more (per eye, a mean, one sex each). Section 3.1 repeats it: "Each eye contains 2022 ± 89 facets in males and 2223 ± 52 facets in females (Table 1)."

Verified, verbatim: "Third instar larvae of A. similis were collected in the Wutong Mountain Scenic Spot" ... "(113°17' E, 22°23' N), Shenzhen, Guangdong, China."; "The collected insects were reared on leaves of Rhododendron simsii"; "Host plants and insects were kept under relatively constant conditions (temperature: 25 ± 2 °C;" ... "relative humidity: 75 ± 10%; photoperiod: 14:10 h [L:D])."; "The emerging insects were fed with a 20% honey-water solution each day."; "Adults of 3–5 days of age were collected and used for the analyses."; "For the SEM analysis, three females and three males of A. similis were used."; "Total numbers of ommatidia per eye, dimensions of compound eyes and facets," "were determined using SEM."; measurements in "Image J version 1.52". No collection month or year (tool summary), so "collection date not stated" is right. No statistical test named anywhere (tool summary), so "no test between them seen" is right; the Discussion states, untested, "Interestingly, the number of ommatidia and the area of compound eyes of females are larger than that of male A. similis." Method, n, lab-emerged from wild larvae, host plant and SE label all as recorded. How many eyes per insect went into the mean is not stated, and the note says so.

Uncounted additions: rearing temperature, humidity, photoperiod and adult diet; the Discussion's untested sex statement; units spelling.

**Lines 1 and 2 MATCH.**

### Lines 3 and 4, facet_diameter_um, male 17.4 and female 18.26

Section 3.1 sentence, verbatim in two abutting pieces in one response: "The average facet diameter in males is 17.40 ± 0.19 μm, while the average facet diameter of females is 18.26 ± 0.17 μm" | "(Table 1)."; a separate pass asked for the sentence's end returned "18.26 ± 0.17 μm (Table 1)." in one piece; the next sentence ("The vast majority of the facets are hexagonal" ...) seen. The record quotes the sentence with the trailing "(Table 1)" cut and marked "[…]", final full stop kept. **Quote MATCH**, 24 words. The cut drops only a table reference, no qualifier, and is acceptable under the quote rule and audit-331.md (answer to the desk's first owner question: yes). The whole sentence is 26 words and could be quoted whole; offered below as optional. The "±" is unlabelled in this sentence, as the conditions say; the abstract labels the count's ± as SE, and the Discussion repeats the diameters ("The diameter of the facet is 18.26 ± 0.17 μm for A. similis females and 17.40 ± 0.19 μm for males," ...) without a test. Value 17.4 for "17.40" is the same number; each value says no more than the quote. Design as lines 1 and 2; the facet sample (how many facets per eye were measured) is not stated in the text (tool summary), and Table 1 was not returned by the tool.

**Lines 3 and 4 MATCH.**

Answer to the desk's second owner question: per-sex records from one sentence are what audits 358 and 331 accepted for distinct measurements; keeping the sexes separate, with the other sex's value in conditions, is right.

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Arge similis, ommatidia_count 2022 (male) | MATCH | conditions, units (uncounted) | abstract sentence whole (20); mean ± SE labelled; n 3 + 3 SEM; lab-emerged from wild larvae |
| 2 | Arge similis, ommatidia_count 2223 (female) | MATCH | conditions, units (uncounted) | as line 1 |
| 3 | Arge similis, facet_diameter_um 17.4 (male) | MATCH | conditions, quote (optional) | Section 3.1 sentence, trailing "(Table 1)" cut and marked (24); ± unlabelled, as stated |
| 4 | Arge similis, facet_diameter_um 18.26 (female) | MATCH | conditions, quote (optional) | as line 3 |

Errors 0 of 4 audited records (0%), under the 5% bar; none held out. Bibliographic 0; licence 0; names 0; duplicates 0 against main and the 154 desk-d2*/audit-3* branches; trait keys 0; quotes 0; omitted results 0.

Unchecked: Table 1 (not returned by the tool), so its column labels, any per-row n and any table footnote on SE or SD; whether the page prints Greek mu (U+03BC) or the micro sign (U+00B5) in "μm" (the tool may normalise); how many eyes per insect and how many facets per eye were measured; the Plazi source paper's author list.

## Replacement text

None counted. Optional, uncounted. Each old string occurs exactly once in its field in the lines named (checked with `str.count` on the desk file).

Lines 1 to 4, each:
- `conditions`: "reared on Rhododendron simsii;" -> "reared on Rhododendron simsii at 25 ± 2 °C, 75 ± 10% RH, 14:10 h L:D, adults fed 20% honey-water;"

Lines 1 and 2, each:
- `conditions`: "sexes kept as separate records, no test between them seen" -> "sexes kept as separate records, no test between them seen (the Discussion states, untested, that females have more ommatidia and larger eye area than males)"
- `units`: "facets per compound eye" -> "ommatidia/eye"

Lines 3 and 4, each (optional; the marked cut is acceptable as filed):
- `quote`: "18.26 ± 0.17 μm […]." -> "18.26 ± 0.17 μm (Table 1)."
- `note`: "Quote ends with the sentence's table reference, cut and marked […]." -> "Quote is the whole sentence, returned in two abutting pieces split before \"(Table 1).\" and confirmed in a second pass (audit 362)."
- `conditions`: "sexes kept as separate records, no test between them seen" -> "sexes kept as separate records, no test between them seen; facets measured per eye not stated"
