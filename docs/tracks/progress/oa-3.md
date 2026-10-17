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

## 2026-10-16 research round: entries 42, 46, 52, 56 and 58

- **5 papers checked; 0 confirmed legal complete copies found/read; 1 complete legal supplement read; 32 records logged.** All additions are explicitly partial, grade g, sequence-inferred SWS1 types. **0 new no-free-copy determinations; all 5 assigned entries remain unresolved** because Semantic Scholar returned HTTP 429 on the first title lookup. It was not queried again. No source-read or no-copy retirement line was added for incomplete article reading/searches.
- **Cumulative evidence: 633 records**, including 32 new supplement records. The prior 11 complete-paper source entries and 61 historical no-copy entries are unchanged by this continuation.

The initial lookup script checked all five entries against OpenAlex and Europe PMC by title, then confirmed the four unambiguous title/first-author/year matches by DOI in both services. Both answered HTTP 200. Semantic Scholar returned HTTP 429 for entry 42; its checks for the other four entries were skipped. Responses and downloaded source material remain outside the repository under `/tmp/oa/oa-3-current`. Once the coordinator shared the round-wide service skip list, no further OpenAlex or Semantic Scholar requests were made. General web searches sought legal alternative copies without using ResearchGate, Academia.edu, library logins or proxies.

| Entry / rank | This round's result |
|---|---|
| 42 / 200 | Confirmed DOI `10.1016/j.anbehav.2010.11.014` through an exact OpenAlex title, author and 2011 match. Europe PMC has no DOI result; OpenAlex reports closed. The author's publications page links `https://estebanfj.bio.purdue.edu/papers/AB_2011.pdf`, and the retrieved PDF matches title and DOI. Its Elsevier cover explicitly prohibits posting the published copy to personal or institutional websites, so this round did not count it as a confirmed legal free copy or log its measurements. A second author's Vassar page links only the publisher. An authorized manuscript is still needed. |
| 46 / 204 | Exact title/first-author/2010 and DOI match in OpenAlex and Europe PMC. Both identify Wiley's free-PDF candidate, but the request returned HTTP 403. HAL metadata at `hal-00649940` matches the paper but the HAL API supplies no full-text file. Abstract supplies no species-specific pupil value. No further Wiley request followed the refusal. |
| 52 / 210 | The supplied CONICET record now opens and confirms the exact title, DOI `10.1080/01584197.2020.1857652`, first author **Belén Casalía**, and January 2021 publication. The batch's first-author initials are incorrect; OpenAlex's 2020 year differs from CONICET, so the loose title lookup alone was not accepted as identity. The original supplied repository record resolves identity. Its PDF is marked restricted (`isAllowed=n` / request access), and the publisher returned HTTP 403. The publisher's official Figshare supplement (`https://api.figshare.com/v2/articles/13521423`; download `https://ndownloader.figshare.com/files/25953891`) is CC BY 4.0 and was retrieved and read through all six pages, including Table S1 and the viewed image-only Figure S1. OpenAlex's green OA candidate is this supplement, **not the main article**. |
| 56 / 214 | Exact title/first-author/2008 and DOI `10.1002/cne.21626` confirmed in OpenAlex and Europe PMC. OpenAlex reports closed; Europe PMC lists subscription access and no PMC copy. General web search supplied no usable legal alternative. Existing abstract records were not duplicated, and no moose measurement was inferred. |
| 58 / 216 | Exact title/first-author/1980 and DOI `10.1126/science.7352290` confirmed in OpenAlex and Europe PMC. OpenAlex reports closed; Europe PMC lists subscription access and no PMC copy. General web search supplied no usable legal alternative. Existing abstract records were not duplicated. |

The 32 supplement records use the existing `sws1_type` extension, with an explicit new-trait explanation because measured spectral ranges, pigment peaks and behavioural colour vision would overstate gene-sequence predictions. They represent 21 newly sampled species and 11 additional taxa with cited comparison sequences (including one subspecies); all are grade g because visual-system type is inferred from tuning sites. The duplicated newly sampled individuals are consolidated into one prediction per species. Cardinalis cardinalis also has a prior comparison sequence, which agrees and is not double-counted. The supplement supports Ramphocelus carbo specifically; it does not sample the wanted Paroaria, Sicalis or Thraupis species. No family-wide measured claim was substituted for those absent species.

All **32 new quotes passed quotecheck** against the literal `pdftotext -layout` export of the supplement; the two rows that fail the PDF reading-order export because of split table cells or an accented spelling pass the unchanged layout export. `addlog.py` validated all additions. The source spells *Thlypopsis sórdida*; the log normalizes it to *Thlypopsis sordida* and explains the spelling. Only this batch's evidence and progress files were changed, and no paper, source text or lookup response was committed.

Next: resolve Semantic Scholar checks after the rate limit clears, retrieve authorized full manuscripts for entries 42 and 52, and obtain the refused entry-46 publisher copy through an accessible legal repository. Entries 56 and 58 still need a complete unblocked lookup before any final no-copy determination.


## 2026-10-16 continuation: lawful-manuscript searches for entries 42, 46, 52, 56 and 58

- **5 papers checked; 0 new complete free copies found; 0 papers read; 0 evidence records added; 4 no-free-copy outcomes recorded.** Entries **42, 52, 56 and 58** now have qualified no-copy search outcomes. Entry **46 remains unresolved** because Europe PMC identifies a free publisher PDF on an already refused host; a technical block does not establish no free copy.
- **Cumulative files:** 633 evidence records, 11 fully read sources and 65 no-copy outcomes. The earlier 32 partial supplement predictions are retained without duplication. Four queue entries advance; the sole remaining batch entry is 46.

This continuation first inspected the preceding progress note and `/tmp/oa/oa-3-current`, then ran fresh Europe PMC DOI checks for all five entries. General web searches used each exact title with PDF, manuscript and repository terms, followed by targeted institutional searches. Initial direct Google requests delivered a JavaScript challenge and supplied no evidence; the available web-search tool then supplied substantive search results. No OpenAlex, Semantic Scholar or already refused publisher-host request was repeated.

Entry 42 searches found the already excluded Purdue published PDF and citations, with no authorized accepted manuscript. Entry 52's CONICET record was reopened and explicitly retains `restrictedAccess` and `isAllowed=n` for its main PDF; the open supplement does not complete that article. Entry 56 searches included the three relevant Vienna university domains; entry 58 searches included Yale and publisher/JSTOR routes. Europe PMC lists only subscription access and no PMC copy for entries 56 and 58. The four no-copy lines mean no legal complete copy located by these searches and explicitly preserve provider-limit and partial-reading limitations.

For entry 46, fresh HAL API metadata confirms `hal-00649940v1`, the exact title and DOI, but offers only an external Wiley free-PDF link and no deposited manuscript file. Further legal author/repository alternatives are being checked. All responses remain outside the repository in `/tmp/oa/oa-3-followup`. No source-read line was added and no full text committed. These metadata-only changes require JSON validation, not quote checking; all four new source lines parse successfully.

Entry 46 follow-up exhausted the available alternative leads: exact-title/DOI/author searches and targeted Sydney, Macquarie, HAL and CEBC searches found no separate manuscript. The opened CEBC 2010 publications page and corresponding-author page supplied no link for this paper; Macquarie's indexed record offers the DOI only, and HAL's API exposes the external Wiley PDF only. Search indexing additionally labels the Wiley version “Free Access”, reinforcing why this entry remains technically blocked rather than receiving a no-copy determination. The search-indexed Table S1 filename was identified, but no independently accessible legal supplement location was found. No new host refusal occurred and no already refused host was retried. The next useful step is an accessible authorized main paper and its Table S1; the latter holds pupil shapes for 127 snake species. No further measurement or completed-source claim has been made.


## 2026-10-16 continuation: entry 46, remaining metadata and author leads

- **1 paper checked; 0 new free full copies retrieved; 0 papers read; 0 evidence records added; 0 no-free-copy outcomes added; 1 entry remains unresolved.** Cumulative totals stay at 633 evidence records, 11 fully read sources and 65 historical no-copy outcomes.
- This pass read the preceding progress and both retained lookup directories before trying unused leads. Fresh OpenAIRE DOI metadata identifies the same Wiley free PDF and supplies no author manuscript or institutional full-text alternative. The opened Mendeley catalogue independently labels the paper free to access, but its embedded PDF URL is again the already refused Wiley URL; it was not followed. These confirmations preserve entry 46 as technically blocked, rather than evidence that no legal free copy exists.
- The opened OIEau catalogue supplies only a broken `/eaudoc/node/` record link for this title. The historical Sydney Shine-lab address redirects to a malformed university URL returning 404. Targeted CEBC WordPress media searches for `pupil` and `JEB23` return empty lists. Additional indexed searches targeted La Trobe, CORE, ecoevo.com.br, Figshare, Zenodo and OSF without locating this manuscript or Table S1. Unrelated citing papers and unauthorized upload sites were not treated as copies.
- New refusals: CORE returned HTTP 403, and the web-search service reported a non-retryable robots.txt block for `ses.library.usyd.edu.au`; neither was retried. Existing round-wide refusing services were skipped. Responses remain outside the repository in `/tmp/oa/oa-3-unused-leads`. No full-read line, no-copy retirement line or species-level pupil claim was added.

The next useful input remains the authorized publisher PDF or an accessible author manuscript, together with Table S1. Metadata/search snippets cannot replace reading those sources. This progress-only update requires no app checks or quote checking.

## 2026-10-16 continuation: entry 46, repository version checks

- **1 paper checked; 0 new complete free copies retrieved; 0 papers read; 0 evidence records added; 0 no-copy outcomes added; 1 entry remains unresolved.** Cumulative totals remain 633 evidence records, 11 fully read sources and 65 historical no-copy outcomes.
- After reading the earlier progress and retained `/tmp/oa/oa-3-current`, `/tmp/oa/oa-3-followup` and `/tmp/oa/oa-3-unused-leads` artifacts, this pass checked additional repository-version routes. Targeted indexed searches of Newcastle's institutional domains and La Trobe/OPAL supplied no usable manuscript link. Figshare's public search API returned HTTP 200 and empty lists for the exact article title, the known `JEB_2046_sm_Table-S1` supplement filename and the paired author names. These are search outcomes, not proof that those repositories contain no copy.
- The already identified free publisher copy remains blocked by the round's existing host refusal. No refusing service was retried, no unauthorized upload was opened and no new refusal occurred. No complete-source line, no-copy retirement line or inferred species-level pupil measurement was added. Figshare responses remain outside the repository under `/tmp/oa/oa-3-version-leads`; no paper text was committed.

The remaining need is an accessible authorized main article and its Table S1. This progress-only update does not require quote checking or app checks.


## 2026-10-16 continuation: entry 46, metadata relations and advertised TDM link

- **1 paper checked; 0 new complete free copies retrieved; 0 papers read; 0 evidence records added; 0 no-copy outcomes added; 1 entry remains unresolved.** Cumulative totals remain 633 evidence records, 11 fully read sources and 65 historical no-copy outcomes.
- This pass inspected the preceding progress and retained entry-46 lookup artifacts before checking unused metadata routes. Crossref returned HTTP 200 for DOI `10.1111/j.1420-9101.2010.02046.x`; its `relation` object is empty. It supplies only the Wiley publisher PDF and Wiley TDM link, with a migrated Oxford Academic primary landing page. Already refused publisher landing-page/PDF hosts were not requested. DataCite returned HTTP 200 and zero results for this DOI as a related identifier; this checks registered relations, not every possible repository copy.
- The actual `api.wiley.com` TDM URL retrieved from Crossref was tried once by an ordinary unauthenticated request. It returned **HTTP 400 with an empty body**, so it supplied no paper. No credentials were sought and no retry followed. Additional indexed author-publication/manuscript and repository searches supplied no new usable authorized copy; repeated catalogue results, unrelated citing papers and unauthorized uploads were excluded.
- Responses, request status and the search ledger remain outside the repository under `/tmp/oa/oa-3-relations`. No new HTTP 403/429 or robots refusal occurred. The known free publisher copy remains technically inaccessible, so no no-copy retirement line, full-read claim or species-level pupil record was added. This progress-only update requires no quote checking or app checks.

The remaining need is an accessible authorized main article and its Table S1. Crossref's advertised TDM route did not provide an alternative in this environment.
