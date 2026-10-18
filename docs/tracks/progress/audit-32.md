# Precision audit 32, 17 October 2026

Scope: the evidence records that `repair/codex-17oct` (the three closed Codex branches combined, with the partial-flag fixes file `docs/views/fixes/codex-partial.jsonl` and the repair ledger `recheck-rp1.jsonl`) adds over `origin/main` in oa-1, oa-2, oa-5, oa-6, oa-9, oa-10 and harvest-c1 to c6. The branch carries no `docs/views/searched/harvest-c*` files, so there are no harvest-c search records to check against the harvest queries. Each record was judged in its repaired view (original line plus the partial flag the repair set). The repair never rewrites quotes, authors or journal fields (it only lists them for the desk), so those faults stay in the repaired view.

Draw: Python `random.seed(32)`. One `random.choice` per file (12 records), then `random.choice` over the pooled added lines until 20 were reached; because errors were found, 15 more by the same stream. The first 20 include six requote candidates (oa-5:1085, harvest-c1:4, harvest-c4:21, harvest-c5:17, oa-9:2275, oa-1:9300) and three lines whose partial flag the repair set (harvest-c1:4, oa-1:7027, oa-2:9634).

Method as in audit 16. Sources came from WebSearch results, then WebFetch. No library login, proxy or shadow library was used and no paper text was committed. A record is `unverifiable` when its source page or data file would not open (PubMed Central permission step, Figshare, NHM and GitHub CSV files, Springer truncation, Oxford and publisher supplements). A record is counted as an error for any of: a quote that is not one complete sentence or does not end where the sentence ends, a missing `partial: true` on a table, appendix or compiled read, a grade above what the quote supports, a journal field without volume, issue or pages as the page prints them, or a shortened author list. Journal-only errors are listed apart so the desk can see both rates.

## Table, first 20

| # | id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|---|
| 1 | oa-1:5792 | Thamnodynastes pallidus / spectral_sensitivity_prediction | i | unverifiable | Simões 2016 supplement S4 is not rendered by the fetch tool. Ten authors and 33(10): 2483-2495 match what is known |
| 2 | oa-2:5064 | Ingerophrynus galeatus / eye_diameter_mm 9.0 | m | unverifiable | Dryad page lists other CSV files and not frogs_analysis.csv; GitHub raw file not returned by search. Journal field lacks the issue |
| 3 | oa-5:1085 | Panthera leo / pupil_shape | m | correct | Springer page prints BMC Vet Res 22: 329; the record has no volume or article number. The sentence was not in the truncated page text (the page has "Pupil shape also differed among the examined animals"). The page lists authors with an ellipsis, so six names is probably short. Requote candidate not settled |
| 4 | oa-6:970 | Tyto alba / contrast_peak_cpd 1.0 | g | unverifiable | HAL page carries no Table 1; the Potier PDF has no barn owl peak. Seven authors match. Journal lacks the issue. `partial: true` right |
| 5 | oa-9:1949 | Ambystoma altamirani / pupil_shape | g | unverifiable | NHM CSV not reachable; dataset page confirms eight authors, 1,293 species |
| 6 | oa-10:255 | Fukomys mechowii / behaviour_vision | m | unverifiable | PMC blocked. DOAJ abstract confirms F. mechowii avoids green-yellow light; PLoS ONE 5(7): e11810 and three authors match. The quote begins "and green-yellow light (", so it cannot be a complete sentence (candidate detector did not list it) |
| 7 | harvest-c1:4 | Oxalis stricta / diel | m | correct | Maxapress page: the sentence is in Discussion, "Light promotes leaf unfolding", and runs on to the full moon, so the quote ends early. Journal lacks volume and article number (Technology in Horticulture 3: 11). `partial: true` set by repair, right. Authors (7) match |
| 8 | harvest-c2:3 | Pontederia crassipes / sense_chemical | m | unverifiable | Europe PMC search URL only; no page returned by search. `partial: true` right for an abstract read. Journal lacks the issue |
| 9 | harvest-c3:13 | Diospyros kaki / sense_chemical | m | requote | MDPI PDF: the sentence begins "At the 'ready to eat' stage" and ends "(Figure 3)"; the quote is the second clause. Not in the candidate list. Authors and 47(9): 689 match |
| 10 | harvest-c4:21 | Orgyia antiqua / acuity_cpd 0.2604 | i | requote | eje.cz PDF: the sentence continues "and were found to be statistically significantly different from each other (p < 0.001, Table 1)". Table 1: 1.92 and 3.03 deg; 0.2604 follows from the male value. Journal lacks the issue (104(2)) |
| 11 | harvest-c5:17 | Panicum miliaceum / sense_light_nonvisual | m | correct | Journal field empty; DOAJ gives Scientific Reports 14(1). Quote starts lowercase mid-sentence |
| 12 | harvest-c6:2 | Deilephila elpenor / corner_hz 6.1 | m | unverifiable | PMC blocked; Konstanz record confirms authors and 284(1857): 20170880 (issue missing in the record). The quote "50% cut-off at 6.1 + 1.2 Hz" is a fragment |
| 13 | oa-1:7027 | human / spectral_range_nm | g | unverifiable | Figure caption on PMC/BMC not reachable. `partial: true` set by repair. Journal lacks volume and article number |
| 14 | oa-9:4046 | Rhodanthe anthemoides / sense_light_nonvisual | i | correct | Journal lacks the issue (15(9), Western Sydney record). Raw CSV not opened |
| 15 | oa-9:2275 | Eucalyptus websteriana subsp. norsemanica | m | correct | Appendix S3 Table S3.1 row with no `partial`; repair did not flag it. Journal lacks the issue |
| 16 | oa-2:9634 | Tiliqua rugosa / acuity_cpd 6.8 | g | requote | IntechOpen chapter, section 1.2: the quote is a fragment of a longer sentence, citing New and Bull 2011 (primary abstract: "upper limit of visual acuity of 6.8 c/deg"). `partial: true` set by repair, right |
| 17 | oa-1:5182 | Mnais costalis / opsin_genes_detected | m | unverifiable | PMC blocked. Seven authors match; journal lacks the issue (112(10)) |
| 18 | harvest-c3:48 | Impatiens balsamina / sense_chemical | m | unverifiable | URI PDF opened (11 MB). The fetch found neither "Increments of NAA" nor "coordinated increase", and the table of contents puts Chapter VI as the Discussion at p. 144, not "Chemical Factors"; possible OCR noise, so not settled |
| 19 | oa-1:9300 | Apalone spinifera / opsin_status | m | requote | Whittier PDF, p. 667: sentence continues "(RH2 [rod-like cone opsin], LWS [long wavelength-sensitive opsin])". It covers four turtles, so `m` for one species should be `g`. Journal lacks the issue (34(3)) |
| 20 | oa-9:4107 | Syzygium crebrinerve / sense_light_nonvisual | m | correct | Journal lacks the issue (15(9)). Raw CSV not opened |

First 20: 10 unverifiable, 10 verifiable, 10 errors.

## Table, extension (15 more)

| # | id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|---|
| 21 | oa-1:9114 | Amelois transitella / lambda_max_nm 350 | g | confirm | Briscoe and Chittka 2001 PDF, p. 501: 350, 430, 530 with SpecPupil, ERG. `partial: true` set by repair. 46: 471-510 (Annual Reviews has no issues) |
| 22 | oa-1:6310 | Opheodrys aestivus / ocular_uva_transmission_percent | m | unverifiable | Simões Table S22 not rendered |
| 23 | oa-9:4133 | Tasmannia stipitata / sense_light_nonvisual | m | correct | Journal lacks the issue (15(9)) |
| 24 | oa-1:8825 | Melecta punctata / lambda_max_nm 336 | g | confirm | same PDF, p. 498: 336, 428, 540, IntCell. `partial: true` set by repair |
| 25 | oa-1:10385 | Pronolagus rupestris / orbit_frontation_1_deg | i | correct | Journal lacks the issue (Royal Society Open Science 13(4): 252149, Adelaide record). Figshare row not opened |
| 26 | oa-9:1295 | Boophis erythrodactylus / pupil_shape | g | unverifiable | NHM CSV |
| 27 | oa-1:5816 | Xenopeltis unicolor / lambda_max_nm 560 | i | unverifiable | Simões Table S5 |
| 28 | oa-9:1050 | Afrixalus knysnae / pupil_shape | g | unverifiable | NHM CSV |
| 29 | oa-1:6774 | Garrulus glandarius / opsin_tuning_residue | m | unverifiable | Ödeen additional file |
| 30 | oa-1:6411 | Morpho peleides / erg_half_amplitude_duration_s | i | unverifiable | Carleton thesis not returned by search |
| 31 | oa-2:9047 | Alouatta / lambda_max_nm >540 | g | unverifiable | PMC blocked; journal lacks the issue |
| 32 | oa-2:4910 | Gastrotheca pseustes / corneal_diameter_mm 4.9 | m | unverifiable | GitHub CSV |
| 33 | oa-1:10507 | Sylvilagus audubonii / orbit_frontation_2_deg | i | correct | Same journal fault as 25 |
| 34 | oa-9:2250 | Eucalyptus cloeziana / sense_light_nonvisual | m | correct | Appendix S3 table row with no `partial`; journal lacks the issue |
| 35 | oa-2:7626 | Haemulon carbonarium / eye_diameter_mm | g | unverifiable | GitHub CSV, compiled from Schmitz and Wainwright 2011; `partial: true` set by repair |

Extension: 9 unverifiable, 6 verifiable (2 confirm, 4 errors).

## Error rate

- First 20: 10 errors in 10 verifiable records.
- Both draws: **14 errors in 16 verifiable records, 87.5%**; 19 of 35 unverifiable.
- Without journal-only faults (records 3, 14, 20, 23, 25, 33): 8 errors in 16, 50%. The eight are 7, 9, 10, 11, 16 and 19 (quotes that stop early or start mid-sentence; 19 also has a grade fault) and 15 and 34 (table rows read without `partial`).
- Every partial flag the repair set on a sampled record (harvest-c1:4, oa-2:9634, oa-1:7027, oa-1:9114, oa-1:8825, oa-2:7626) fits the record's note or source type. The repair works on the fault it targets; the other faults remain.
- The 5% threshold is not met on any counting. No pull request yet.

## Remaining systematic faults (counts.json, and heuristic counts from this audit)

1. Unmarked or partial-sentence quotes: `requote:start` 220, `requote:end` 688, `requote:both` 327 (1,235 candidates in `requote-candidates.jsonl`; the repair writes no replacement text). Of the 20 first-draw records, 6 were listed and 4 more faulty quotes (oa-10:255, harvest-c3:13, harvest-c6:2, oa-2:9634) were not; a scan of the added lines finds 84 prose quotes that begin lowercase and 191 that end without terminal punctuation and are absent from the candidate list.
2. Journal field without volume, issue or pages: `journal` 1,194 in `crossref-todo.jsonl` and 189 empty. A scan of the added lines finds about 13,200 journal fields with no issue; 2,010 are Perrin et al. 2025 (`Ecology and Evolution 15: e71923`, should be 15(9)) and 990 are Kraatz et al. 2026 (should be 13(4)), so two lookups fix 3,000 lines. The scan also counts journals that print no issue, so treat it as an upper bound.
3. Authors: `authors` 1,204 in the Crossref list (shortened or "et al."); oa-5:1085 is one more that the page shows is short.
4. Table, appendix and supplement reads without `partial: true` that the script missed: 268 Perrin Appendix S3 rows, 339 Simões supplement rows (a scan of `where`; the Simões manuscript includes its SI, so the desk should decide), with `partial_set` 6,275 already set.
5. Grade: pooled-species quotes graded `m` (oa-1:9300). `audit_unmatched` lists five audited lines (oa-6:296, oa-6:89, oa-6:523, oa-1:3400, oa-3:67) with no match in the combined set.
6. The sources most of these lines rest on (NHM and GitHub CSV files, Figshare, Simões and Ödeen supplements, PMC) did not open, so 54 percent of this sample could not be checked at all.

## Corrections

`docs/views/recheck/recheck-32.jsonl`: 13 rows in the recheck-27 schema, all counted: requote harvest-c3:13, harvest-c4:21, oa-1:9300 (with grade g and partial); journal rows for harvest-c1:4, harvest-c5:17, oa-5:1085; partial and journal rows for oa-9:2275 and oa-9:2250; journal rows for oa-9:4046, 4107, 4133, oa-1:10385 and 10507. The quotes of harvest-c5:17, oa-6 and oa-2:9634 are not rewritten because the full sentence was not seen.

## Blocked pages

pmc.ncbi.nlm.nih.gov (PMC2911378, PMC5489734, PMC2781854, PMC12391026: bot challenge), nature.com (Wang 2024: permission unanswered), Dryad and GitHub raw CSV files, data.nhm.ac.uk CSV, Figshare, Springer text beyond the abstract (Klećkowska-Nawrot).
