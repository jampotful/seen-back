# OA batch 3

Research pass dated 2026-10-14, on `research/oa-3`, following `AGENTS.md` and `docs/tracks/prompts/oa-pass.md`. App setup, builds, servers, Playwright and app tests were skipped.

## Results

- **79 batch entries processed; 70 received lookup responses.** OpenAlex answered for ranks 159–186, returned HTTP 429 at rank 187, and was not requested again. Europe PMC and Semantic Scholar continued for DOI papers. Semantic Scholar requests were spaced by at least approximately one second.
- **23 papers had candidate free-copy links; 9 legal full copies were retrieved and read.** A candidate link alone is not a confirmed copy. All downloaded full papers were matched by their first-page titles. No unread successfully downloaded full paper remains.
- **552 evidence records**, covering 231 taxon labels: 166 grade m, 376 grade g, 10 grade i. There are **513 records from full-text reading and 39 explicitly partial/abstract-only records**. Most grade g records are a review's secondary measurements, not 376 newly opened primary studies.
- **61 no-readable-full-copy entries** in `oa-none-3.jsonl`: 47 with no candidate found by the responding services, and 14 with candidate links that did not yield readable full text. Of the former 47, 27 have incomplete OpenAlex lookups. Across all 61 entries, 38 are explicitly `lookup_incomplete`. Candidate retrieval failures have a separate `access_status`; the required `skipped: "no free copy"` label is not a claim that no legal copy exists anywhere.
- **9 title/book lookups remain unsearched**, because they lacked a confirmed DOI when OpenAlex stopped. They have no no-copy determination.

## Full papers read

| Rank | Paper | Evidence rows |
|---|---|---:|
| 163 | Potier et al. 2018, raptor visual fields | 30 |
| 164 | Dolan & Fernández-Juricic 2010, five ground-foraging birds | 31 |
| 166 | Potier et al. 2020, raptor flicker fusion | 29 |
| 167 | Moore et al. 2017, single-foveate birds and eye/head movement | 32 |
| 175 | Lafitte et al. 2022, systematic CFF review | 300 |
| 191 | Fernández-Juricic et al. 2011, Canada goose visual system | 45 |
| 202 | Martin & Piersma 2009, plover and red knot visual fields | 25 |
| 203 | Wright et al. 2023, Heliconius acuity | 13 |
| 230 | Mortimer et al. 2019, orb-web vibration information | 13 |

Rank 164's 31 rows include the five abstract-only records logged before its full PDF became available; the subsequent 26 full-text rows are separate. The nine other papers with abstract-only records are ranks 192, 193, 211, 217, 219, 224, 229, 236 and 237 (34 rows). None of these nine is marked fully read.

Rank 167's two PDF appendices were read, and the image-only phylogeny was viewed. Rank 175's S10 spreadsheet, its metadata and all retained CFF rows were read, along with the main paper, appraisal criteria and the scientific statistical supplement. Its 26 excluded rows were not logged. The retained 200 S10 rows produce 201 records: the yellowfin tuna's `60 - >100` range is split into a lower endpoint and a censored upper endpoint so it is never represented as a range bounded above by 100. Another 93 values come from S10 Comments and six maxima from the main text. Administrative screening lists were not treated as additional primary studies.

Rank 203's supplementary figure and image-analysis methods were read; sampled frames spanning its 24-second video were viewed. Rank 230 is an **accepted manuscript**: every record says so. Its four image-only supplementary figures, included at the end of the manuscript PDF, were viewed. Publisher supplement links for ranks 163 and 166 returned 403; those supplements were not read. Unlabeled raptor plot points were not digitized into invented exact values. Rank 163 provides labeled fields for eight newly measured species plus a few numerical extrema from previously published species.

## Findings needing desk review

- **Source conflict in rank 202:** the prose assigns cyclopean coverage of 325° to plovers and 340° to knots. The viewed, labeled Fig. 3 has rear blind wedges of 20° in plovers and 35° in knots, implying 340° and 325° respectively. Records following the figure show the arithmetic and flag the apparent transposition explicitly.
- **Retinal terminology:** rank 164 could not establish foveal pits because it did not take cross-sections; it reports single areae centrales. Rank 167 labels the overlapping species single-foveate. This is a difference in terminology/certainty, not a demonstrated presence-versus-absence contradiction. Rank 167's Appendix 1 and phylogeny say *Poecile atricapilla*, but the common name says Carolina Chickadee; no species-level record was assigned to that ambiguous row. Its Pipilo spelling was resolved from the viewed phylogeny. The retrieved article year is 2017, unlike the batch's 2016 metadata.
- **CFF review limitations:** flycatcher means in rank 175 are assigned oppositely to rank 166's comparative table. Some method/luminance labels also conflict. These are preserved as secondary values with warnings. The beetle pit-organ result is `sense_infrared`, not visual CFF; a pigeon's peak-response value is `behaviour_vision`, not CFF. Bounds, approximate readings, uncertainty and review risk-of-bias labels are retained.
- **Measured versus inferred:** three raptors in rank 166 never reached a demonstrated CFF; their highest tested FFFs are qualified as lower bounds. The corrected Heliconius male mean is hypothetical (grade i). Orb-web decoding mechanisms are model predictions (grade i), not demonstrated neural strategies in live spiders. The millipede acceptance angle is a conditional model upper bound, not a receptor recording.
- **Publication names:** source taxon spellings are retained or explicitly explained. No unidentified fly, cockatoo species, Arabidopsis species or hypothetical bird predator was assigned a fabricated species measurement.

## Candidate copies not read in full

| Ranks | Outcome |
|---|---|
| 171, 174, 180, 192, 217, 224 | Publisher/repository 403 responses or metadata pages without an accessible full text. |
| 193 | Semantic Scholar's alleged copy is a Publons/Web of Science peer-review redirect, not a confirmed article PDF. |
| 211 | Semantic Scholar supplied a PDF URL containing DOI `10.1002/cne.23657`, different from requested `10.1002/cne.23637`; it was not accepted as this paper. |
| 219, 226, 229, 233 | ScienceDirect/Cell requests were refused by the network proxy (403). The returned Cell HTTP URLs were also tried over normal HTTPS; access remained denied. |
| 236 | Europe PMC XML/PDF retrieval returned 500, including a later PDF attempt. Abstract only. |
| 237 | Listed preprint redirected to bioRxiv and returned 429; no further bioRxiv requests. Abstract only. |

Ranks 171 and 233 had abstracts without extractable trait values; rank 226 had no abstract text in the returned core record. No full-read status was written for an abstract, failed download, repository metadata page, wrong-DOI URL or browser-check page.

The nine entries without a successful title/book lookup are **188, 195, 200, 204, 210, 214, 216, 228 and 234**. Their exact titles and metadata remain in `docs/tracks/batches/oa-3.json`.

## Verification and continuation

Every final record passed `tools/views/quotecheck.py` against its corresponding paper text, abstract, or literal spreadsheet-cell export: **552 passed, 0 failed**. PDF prose and table quotations were checked against reading-order/layout exports of that same PDF. Manuscript line numbers were removed for quote matching, without rewriting the source prose. `addlog.py` validated each extraction before appending it; final JSON files were parsed and source counts reconciled. Only this batch's four permitted files were changed. No PDF, XML, supplement, complete paper text, or lookup script is committed; source material and raw lookup responses are outside the repository under `/tmp/oa`, with scratch scripts in ignored `work/`.

Next steps:
1. Resume the nine missing title/book lookups when OpenAlex is available, accepting only title/first-author/year matches.
2. Resolve the 14 candidate-copy failures through legal copies, checking identities before reading. The source-status files preserve the distinction between unsuccessful search and inaccessible candidate.
3. Desk-review a sample of the records, especially the transposed field diagram/prose, secondary CFF assignments and model-versus-measurement qualifiers, before merging. The owner opens the pull request; none was opened here.

## 2026-10-14 continuation: nine missing title/book entries

This continuation checked only entries **30, 37, 42, 46, 52, 56, 58, 70 and 76** (ranks **188, 195, 200, 204, 210, 214, 216, 228 and 234**). The repository was already updated by the round coordinator. No app setup or app checks were run.

- **9 papers checked; 2 free full copies retrieved and read; 49 records added.** Entry 30 supplied 40 full-text/supplement records. Entries 37, 56 and 58 supplied 1, 2 and 6 explicitly partial abstract records, respectively. Entry 76 supplied zero sensory measurements.
- **2 entries newly completed; 7 remain unresolved.** No new no-free-copy determination was added to `oa-none-3.jsonl`. That file retires papers from the queue even when an extra field says lookup incomplete, so blocked searches remain here only.
- **Cumulative files:** 601 evidence records (553 full-text, 48 partial; 206 grade m, 385 grade g, 10 grade i), 11 read-source entries and the unchanged 61 historical no-copy entries. This leaves **72 of 79 queue entries recorded as read or previously skipped, with 7 entries remaining**. The historical no-copy entries retain the limitations described above; their presence does not make their incomplete historical searches conclusive.

The required batch lookup script saved raw responses outside the repository under `/tmp/oa/oa-3`. OpenAlex returned HTTP 429 (shared IP budget exhausted). The initial script sent all nine OpenAlex queries before the responses were inspected; no further OpenAlex requests were made. Crossref and Semantic Scholar later also returned 429 during title resolution. The scripts had already sent later requests in those loops before the responses were inspected; no further calls to either API followed. Europe PMC remained accessible. A Google title lookup returned a JavaScript challenge rather than research results and supplied no evidence.

### Papers read

- **Entry 30 / rank 188:** *Simple and complex, sexually dimorphic retinal mosaic of fritillary butterflies*, DOI `10.1098/rstb.2021.0276`. Europe PMC XML returned 500, but its PDF endpoint delivered the complete eight-page paper. The first-page title, year and author set match the batch; the batch's author order is wrong: the paper is **Ilić et al.**, not Belušič et al. The paper's Dryad identifier agrees with the batch, resolving identity without accepting a loose title-search match. The complete 12-page Figshare supplement was retrieved and read. Figure 3 and image-only supplementary Figures S2 and S5 were viewed. Forty records cover spectral peaks, sex differences in receptor classes, tapeta and screening pigments, plus clearly identified reanalysis of earlier red-receptor data. Exact printed spectral labels were used, without digitizing curves. The three *Speyeria aglaja* female peaks are printed inside an image-only graph: their quotes are its exact caption, and their notes identify the visually checked numerical labels. A putative copied red curve for *A. sagana* is not logged as a measured peak. The inferred sixth class in male *A. sagana* is grade g and explicitly qualified. No behavioural red-colour discrimination is asserted.
- **Entry 76 / rank 234:** *Floral scent of eastern skunk cabbage (Symplocarpus foetidus: Araceae)*, DOI `10.1016/j.phytochem.2024.114111`, Goodrich and Gibernau, 2024. The HAL accepted manuscript was confirmed by its title and DOI and read through all 34 PDF pages, including all six main figures and the included Supplemental Figure 1. It measures volatile emission, not chemoreception or another BRIEF sensory trait, so **records: 0** is intentional. Supplemental Table 1 is not in the manuscript or the HAL API's file list; the publisher API request was blocked by the network proxy with HTTP 403. The table was not extracted or claimed read.

### Unresolved entries

| Entry / rank | Retrieved identity and remaining obstacle |
|---|---|
| 37 / 195 | DOI `10.1086/691404`, Tyrrell and Fernández-Juricic, 2017, confirmed through Crossref and Europe PMC. Semantic Scholar reports closed; Europe PMC lists subscription access. Dryad landing page opens but supplies data files, not the article. One abstract-only bifoveate-retina record is graded g for the group named in the abstract; the abstract does not identify its scientific species. OpenAlex lookup remains blocked. |
| 42 / 200 | Exact and shortened Europe PMC title queries returned no results. Crossref and Semantic Scholar title queries were rate limited. DOI and legal full copy remain unconfirmed. |
| 46 / 204 | DOI `10.1111/j.1420-9101.2010.02046.x`, Brischoux et al., 2010, confirmed. Europe PMC and Semantic Scholar identify a publisher free-PDF candidate, but it returned HTTP 403. The opened abstract has no species-level pupil measurements. OpenAlex lookup remains blocked. |
| 52 / 210 | CONICET repository link returned HTTP 503. Europe PMC title query had no result; Crossref and Semantic Scholar title queries were rate limited. DOI and full-copy status remain unconfirmed. |
| 56 / 214 | DOI `10.1002/cne.21626`, Schiviz et al., 2008, confirmed through Europe PMC. Semantic Scholar reports closed, Europe PMC subscription access. Two partial cone-class records retain the abstract's artiodactyl and African-elephant group scope; no moose measurement was inferred. OpenAlex lookup remains blocked. |
| 58 / 216 | DOI `10.1126/science.7352290`, Goldsmith, 1980, confirmed through Europe PMC. Semantic Scholar reports closed, Europe PMC subscription access. Six partial behavioural records describe the two UV discrimination tests in each of the three explicitly named hummingbird species. A tested wavelength is not treated as a spectral limit or receptor peak. OpenAlex lookup remains blocked. |
| 70 / 228 | Book chapter DOI is in the batch. Its single required OpenAlex lookup returned HTTP 429. No no-copy determination is possible from that response. |

All **49 new quotes passed quotecheck** against the retrieved full-paper, supplement or abstract text exports. `addlog.py` validated all additions. Only this batch's evidence, source and progress files were changed. The no-copy file is unchanged. No downloaded paper, full text, metadata response or script was committed.

Commits before this progress update: `3a0dd6a` (fritillary paper and supplement), `b122af7` (partial records and zero-record skunk-cabbage reading). Next: retry the seven unresolved entries when the lookup services are available; retrieve the refused publisher candidate for entry 46 and resolve the missing identities for entries 42 and 52.
