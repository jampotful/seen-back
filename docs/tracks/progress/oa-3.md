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

## 2026-10-14: remaining-entry follow-up

This round addressed only list positions **30, 37, 42, 46, 52, 56, 58, 70 and 76** (batch ranks 188, 195, 200, 204, 210, 214, 216, 228 and 234). Counts below are additions to the earlier pass, not replacement totals.

- **9 entries checked; 2 legal main-paper copies found and read; 43 records added**: 31 from the full fritillary paper and its supplement, plus 12 explicitly partial abstract records from entries 37 (2), 56 (4), and 58 (6).
- **2 no-free-copy determinations** were added: entry 42 after successful OpenAlex, Europe PMC and Semantic Scholar responses, and entry 70 after the permitted single successful OpenAlex book-chapter check.
- **5 entries remain pending**: positions **37, 46, 52, 56 and 58**. Failed or incomplete API requests were not classified as absence of a free copy. A supplement alone was not marked as a fully read main paper.
- Cumulative batch totals are now **11 main papers read, 595 evidence records, and 63 no-copy status lines**. The prior pass's incomplete lookup flags and candidate-access limitations remain in force.

### Newly read papers

**30 / rank 188, Ilić et al. 2022, DOI 10.1098/rstb.2021.0276:** The exact title and full author list were confirmed through Crossref and Europe PMC; the batch had listed the authors in a different order. Read the full PMC HTML and the 12-page Figshare supplement, including the viewed Fig. 3 and supplementary Figs. S2 and S5. **31 records** cover *Argynnis paphia*, *A. sagana* and female *Speyeria aglaja*. The numerical spectral peaks were read from the original labelled figure panels, not digitized from curves; the records identify the panel and use its exact caption as the checked quotation. The 615-nm red peak in male *A. paphia* was measured indirectly, and the record preserves that distinction. The sixth male class in *A. sagana* is inferred from opponent responses and is grade g. Receptor classes are physiological substrates, not a behavioural demonstration of colour dimensionality. No facet size or interommatidial angle was found. The supplemental species table includes *Agraulis vanillae* in the comparative eyeshine phylogeny, but supplies no species-specific peak for it; no peak was transferred to *Dione*.

**76 / rank 234, Goodrich and Gibernau 2024, DOI 10.1016/j.phytochem.2024.114111:** Confirmed the previously unknown author/year metadata through HAL and Europe PMC, and read the 34-page HAL manuscript, its six figures and included Supplemental Figure 1. **0 sensory records.** The study measures emitted floral scent and its two chemotypes; it does not test chemical detection by *Symplocarpus foetidus*. Emitting a volatile does not establish the plant senses that volatile. Supplemental Table 1 is referenced but not included in the deposit; it was not read. The source-status note states this scope.

### Pending papers and recovered metadata

| Position / rank | Confirmed DOI | Remaining limitation |
|---|---|---|
| 37 / 195 | 10.1086/691404 | Crossref and Europe PMC confirm title, Tyrrell first author and 2017. Publisher PDF returned 403; OpenAlex title lookup returned 429. Abstract read, 2 group-level partial records; the abstract names swallows without naming a measured species. Its 100° arc is the span containing four foveae, not full field width. |
| 46 / 204 | 10.1111/j.1420-9101.2010.02046.x | Europe PMC confirms title, authors and 2010, and supplies a Wiley free-PDF candidate; both Wiley page/PDF attempts returned 403. OpenAlex and Crossref title requests returned 429. Abstract has no species table or numerical sensory measurement. |
| 52 / 210 | 10.1080/01584197.2020.1857652 | Crossref lists print year 2020 and online publication 2021-01-04, explaining the batch/OpenAlex year difference; first author is Belén Casalía. Figshare article 13521423 supplies only the eight-page supplementary PDF, not the main paper. CONICET repository returned 503. The supplement identifies *Ramphocelus carbo* among the sequenced UVS-type species, but does not contain *Paroaria*, *Sicalis* or *Thraupis*. No measured pigment peak or behavioural UV sensitivity was inferred from a gene sequence. |
| 56 / 214 | 10.1002/cne.21626 | Europe PMC confirms title, authors and 2008; Wiley page returned 403; OpenAlex/Crossref title requests returned 429. Abstract read, 4 group-level partial records. The 25-species assertion was not assigned to *Alces alces*, whose inclusion the abstract does not establish. |
| 58 / 216 | 10.1126/science.7352290 | OpenAlex confirms Goldsmith/1980 and reports closed access; Europe PMC supplied the abstract. Semantic Scholar returned 429, so the required lookup remains incomplete. Six partial behavioural records cover the three named hummingbird species, including 370-nm detection. The 20-nm stimulus half bandwidth was not misrepresented as the whole visual spectral range. |

The first lookup script saved responses for all nine positions before reading began. OpenAlex/Crossref responses mixed successes and 429 errors within that script; after inspecting those errors, no further calls were made to those services. Semantic Scholar also returned 429 and was not retried. Raw responses, paper files and extraction scripts stay under `/tmp/oa/oa3-round`, outside the repository. The 43 added records passed quote checks against the retrieved full text, supplement or abstracts, and `addlog.py` validated them. App builds and app tests were not run.
