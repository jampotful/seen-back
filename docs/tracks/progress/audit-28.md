# Precision audit 28, 17 October 2026

Scope: the evidence records that PR #18 adds to oa-1, oa-2, oa-3, oa-5 and oa-6 (8,061 lines present in the branch and absent from origin/main; oa-none-* are source-log files with no evidence records). Sample drawn with Python `random.seed(28)`, `random.sample` over those lines: 35 records, the first 20 as the main sample and the next 15 as the extension that the error rule triggered. The draw fell on oa-1 (17) and oa-2 (17), oa-6 (1) and no oa-3 or oa-5 record.

Method as in audit 16. Quotes from the archived CSV files were checked by exact string match and by reading the named column of the named row (raw.githubusercontent.com opened directly). Journal pages were opened by search and WebFetch. Metadata faults are written as rows that are not counted, as in audit 16. No evidence file, source file, `src/`, `views/*.json` or `ALL.jsonl` was edited.

## Table

| # | id (file:line) | taxon / trait | grade | verdict | note |
|---|---|---|---|---|---|
| 1 | oa-1:6076 | Lampropeltis californiae / opsin_sequences_recovered | g | unverifiable | Simões 2016 supplement S1 is appended to the manuscript PDF but the fetch tool returns only the article text |
| 2 | oa-2:7526 | Chaetodon striatus / eye_diameter_mm 11.19 | g | correct | row and Trans_diameter_mm cell match; secondary compilation (Schmitz and Wainwright 2011, original not opened) lacks `partial: true` |
| 3 | oa-1:6222 | Boiga forsteni / diel | g | unverifiable | supplement S2 not rendered. The main text confirms that sws1 amplification failed in B. forsteni, consistent with the S1 row |
| 4 | oa-2:5915 | Proceratophrys boiei / eye_diameter_mm 8.3 | m | confirm | frogs_analysis.csv row 487, ED_right_mm = 8.3 |
| 5 | oa-2:6337 | Stefania evansi / corneal_diameter_mm 7.5 | m | confirm | row 593, CD_right_mm = 7.5 |
| 6 | oa-2:7278 | Polysticta stelleri / eye_diameter_mm 10.8 | g | correct | cell matches; compiled from Hall and Heesy 2011 (confirmed as the bird source in Thomas et al.), original not opened, no `partial` |
| 7 | oa-1:6609 | Malurus amabilis / opsin_tuning_residue | g | unverifiable | Ödeen et al. additional file blocked (PMC bot challenge; BMC page permission unanswered) |
| 8 | oa-1:7005 | Dolichonyx oryzivorus / spectral_sensitivity_prediction | i | unverifiable | same file |
| 9 | oa-1:6236 | Chironius fuscus / diel | g | unverifiable | S2 not rendered |
| 10 | oa-2:6670 | Lithodytes lineatus / ocular_dimension_mm 5.15 | m | confirm | fresh_data.csv row 30, AD_mm_dissected = 5.15 |
| 11 | oa-2:5246 | Leptopelis parkeri / eye_diameter_mm 6.3 | m | confirm | row 313, ED_left_mm = 6.3 |
| 12 | oa-2:7700 | Lactophrys triqueter / eye_diameter_mm 10.16 | g | correct | cell matches; secondary compilation, no `partial` |
| 13 | oa-2:4865 | Gastrophryne carolinensis / corneal_diameter_mm 1.9 | m | confirm | row 216, CD_right_mm = 1.9 |
| 14 | oa-1:6878 | Mimus saturninus / opsin_tuning_residue | g | unverifiable | Ödeen file blocked |
| 15 | oa-1:6898 | Luscinia svecica / opsin_tuning_residue | m | correct | grade: residue read from sequence is opsin-inferred, g at most. Quote not rechecked (file blocked) |
| 16 | oa-1:6333 | Bogertophis subocularis / ocular_uva_transmission_percent 58.3 | m | unverifiable | S22 not rendered |
| 17 | oa-2:4653 | Dryophytes arenicolor / eye_diameter_mm 4.1 | m | confirm | row 163, ED_left_mm = 4.1 |
| 18 | oa-1:6485 | Eolophus roseicapilla / opsin_tuning_residue | g | unverifiable | Ödeen file blocked |
| 19 | oa-2:8344 | Trichechus inunguis / eye_diameter_mm 13.5 | g | correct | cell matches; Howland et al. 2004 compilation (original not opened), no `partial` |
| 20 | oa-6:808 | Helictotrichon pubescens / sense_light_nonvisual | m | requote | the quote ends inside an unclosed parenthesis in the species list, so it is a cut sentence with no cut marked, and the list runs to the cut. PMC page not opened (permission unanswered), so the value was not rechecked. Journal field lacks 73(12): 4079-4093 (from the NMBU repository record) |
| 21 | oa-1:6224 | Boiga forsteni / retinal_photoreceptor_morphology | g | unverifiable | S2 not rendered |
| 22 | oa-2:6412 | Telmatobius culeus / corneal_diameter_mm 5.4 | m | confirm | row 612, CD_right_mm = 5.4 |
| 23 | oa-1:6687 | Lichenostomus flavescens / opsin_tuning_residue | g | unverifiable | Ödeen file blocked |
| 24 | oa-1:6799 | Eopsaltria australis / opsin_tuning_residue | m | correct | same grade fault as 15 |
| 25 | oa-1:5378 | Tribolium castaneum / opsin_genes_detected | g | unverifiable | Fig. 4 is an image; PMC text gives the caption and the citation (112(11): E1247-E1256) but not the cell. `partial: true` is present |
| 26 | oa-2:4779 | Espadarana prosoblepon / eye_diameter_mm 3.8 | m | confirm | row 195, ED_right_mm = 3.8 |
| 27 | oa-2:3410 | Bos taurus / behaviour_vision 71.7 | m | unverifiable | the scanned Table 1 reaches the tool as garbled text; the extract shows a five-value line without the "----" and cannot place 71.7 under heifer 5 |
| 28 | oa-1:5720 | Amphisbaena alba / spectral_sensitivity_prediction | i | unverifiable | S4 not rendered |
| 29 | oa-1:5929 | Enhydris innominata / opsin_sequences_recovered | g | unverifiable | S1 not rendered |
| 30 | oa-2:4888 | Gastrophryne olivacea / eye_diameter_mm 2.1 | m | confirm | row 222, ED_left_mm = 2.1 |
| 31 | oa-2:8800 | Ptychozoon kuhli / eye_diameter_mm 5.4 | g | correct | cell matches; Werner and Seifan 2006 compilation, no `partial` |
| 32 | oa-2:4021 | Acris gryllus / corneal_diameter_mm 2.3 | m | confirm | row 3, CD_left_mm = 2.3 |
| 33 | oa-2:7150 | Rhinella ocellata / pupil_shape | g | correct | traits_analysis.csv row 188 matches; the note itself calls it a secondary compiled classification, no `partial` |
| 34 | oa-2:8205 | Canis lupus f. familiaris / eye_diameter_mm 17.0 | g | correct | cell matches (Pekingese row); Howland compilation, no `partial` |
| 35 | oa-1:6211 | Thamnodynastes pallidus / diel | g | unverifiable | S2 not rendered |

## Error rate

- Verifiable records: 20 (13 confirm, 7 not confirm). 15 records were unverifiable.
- Counted errors under the stated rule (grade, quote, partial flag): 10 of 20, 50 per cent. These are 2 grade faults (15, 24), 1 requote (20) and 7 missing `partial` flags (2, 6, 12, 19, 31, 33, 34).
- Counted errors without the `partial` flag: 3 of 20, 15 per cent.
- Both figures exceed the 5 per cent threshold, and the 15-record extension did find further faults, so the error stands.

## Systematic faults

1. Grade m on opsin-inferred values. 171 `opsin_tuning_residue` records in oa-1 carry `m`, although the oa-2 progress note says genotype-based tuning was assigned `g` and 237 sibling rows are `g`. The pattern is that rows the paper newly sequenced got `m` and rows from earlier studies got `g`. A tuning residue is read off sequence, so `g` is the ceiling. A mechanical pass over oa-1 would fix them. The 189 `opsin_genes_detected` records at `m` are a related case for the desk to rule on.
2. Compiled and secondary rows without `partial: true`. oa-1 sets the flag on its secondary genome-comparison rows (Futahashi) but oa-2 does not on its secondary vertebrate compilations (original papers named in `conditions` and "original not opened"). The oa-2 compilation rows number in the thousands; the pool shows 2,350 `g` rows without the flag.
3. Journal field without volume, issue or pages. Fjellheim 2022 has the journal name only (it is 73(12): 4079-4093); Ödeen 2011 has the name only (volume 11, article 313); Thomas 2020 has "287: 20201393" and no issue; Futahashi has "112: E1247-E1256" and no issue (11). These are metadata rows that are not counted. The Ödeen source title is also extended with "Additional files 1 to 3 (species list with site-90 residue)", which the paper does not print.
4. Quotes that are table or CSV lines, not sentences. This is the pipeline's convention for data rows and each CSV quote matched exactly, so it is recorded here and not counted.
5. Thin verification for the supplementary tables. Eleven of the 15 unverifiable records are rows of supplements appended to PDFs or held in DOCX files; the fetch tool does not return them. A desk member with the files should open Simões S1, S2, S4 and S22 and Ödeen's Additional file 1.

## Blocked pages

pmc.ncbi.nlm.nih.gov for PMC9232202, PMC7542830 and PMC3225180 (bot challenge or permission unanswered); bmcevolbiol.biomedcentral.com article page (permission unanswered); api.crossref.org and the Europe PMC REST host (egress proxy 403). The Dryad and GitHub CSVs, the PNAS PMC page, the NSF accepted-manuscript copy of Thomas et al. and the USU thesis PDF opened.

## Rows written

`docs/views/recheck/recheck-28.jsonl`: 9 rows, all `correct`: 2 grade rows (oa-1:6898, oa-1:6799) and 7 `partial` rows (oa-2:7526, 7278, 7700, 8344, 8800, 7150, 8205). The requote for oa-6:808 has no row because the source page did not open and the full sentence could not be copied. The 171 remaining residue records are not listed row by row.

## Recommendation

Do not merge PR #18 as it stands. Fix the grade of the opsin-residue rows and decide the `partial` rule for compiled rows, then merge.
