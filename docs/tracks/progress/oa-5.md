# OA batch 5 — 2026-10-14

Pass completed for the copies retrievable in this session. All 79 batch entries went through the single-script availability pass before reading; 31 had indexed free-copy candidates. Seventeen legal full copies were retrieved and their main papers read, in batch order. The full-read ledger contains 17 entries, including two zero-record papers. No unread paper is marked read.

Logged **1,047 quote-verified records**: 928 from full sources and 119 abstract-only records from 28 papers. Thirty-three abstracts were reviewed; five supplied no sufficiently specific additional values. Every appended record passed the prompt's quote checker and evidence append validation. Table/figure values were also checked visually where needed; reef-fish figure OCR came from the retrieved paper.

Full-read ranks: 320, 322, 323, 328, 341, 344, 345, 355, 359, 361, 362, 364, 366, 367, 371, 387, 391.

The no-copy ledger has **43 entries**: 24 completed negative lookups, plus 19 additional abstract-only papers counted as having no full copy, as the prompt requires. These statuses mean no full copy found or retrieved here, not proof none exists. Known indexed copies, blocked retrievals and incomplete provider coverage are identified in the abstract-only entries. A further 19 entries remain unresolved or have inaccessible/unverified indexed copies and are excluded from that ledger. Across the batch, 14 indexed candidates could not be retrieved or verified; some also have abstract-only evidence.

Availability limits: OpenAlex returned HTTP 429 at rank 358, so no more requests were sent to it. Title queries at ranks 335, 349 and 352 returned HTTP 400. Europe PMC and Semantic Scholar continued where a DOI was available. NCBI BioC fallback also returned HTTP 429 and was stopped. Older Europe PMC XML requests sometimes returned HTTP 500; legal Europe PMC PDFs recovered several of those papers. API failures are not evidence of paywalls.

Source caveats: the red-drum FFF table says 54 Hz and its Discussion says 53 Hz; both are retained. Harris's hawk workbook/main-text subject labels differ. Motion tuning, electrical CFF, gene-derived pigment predictions and model-only predictions are distinguished. Camel OCT fovea identification is not converted into acuity. Abstract taxa without a reliable species identity retain their reported scope. The flower-scent paper and chromatic-aberration critique yield zero sensory records. Frog data include all twelve accessible supplementary appendices; other supplementary coverage is recorded in the source ledger. Gymnadenia and cephalopod-model supplements were unavailable. Hawk head-motion videos were inspected through full-duration sampled contact sheets, with no measurements inferred from them.

No retrieved paper remains pending. For a future pass, the first three unresolved/inaccessible entries in batch order are:

- Rank 326: Flowering of Phlox paniculata is influenced by photoperiod and cold treatment

- Rank 335: Animal Eyes, second edition: chapter 5, Lens eyes on land (pp. 94-128), and chapter 9, Movements of the eyes (pp. 215-241, head-bobbing in birds p. 227)

- Rank 349: Descriptive comparative morphology of the eye and ocular adnexa in Felidae: observations from a clouded leopard (Neofelis nebulosa), African lion (Panthera leo) and Pallas's cat (Otocolobus manul)

Remaining ranks (no full read and no no-copy ledger entry): 326, 335, 349, 352, 358, 360, 363, 365, 368, 375, 379, 381, 382, 384, 385, 386, 392, 394, 395.

PDFs, XML, full texts, supplements and API caches remain under /tmp/oa, outside the repository; scratch scripts are under /workspace/work/oa-5. Only the four permitted batch-5 files changed. App setup, builds, servers and app tests were skipped.

## 2026-10-16

Checked all **19 assigned entries** (positions 10, 19, 33, 36, 42, 44, 47, 49, 52, 59, 63, 65, 66, 68, 69, 70, 76, 78, 79) in one availability script before reading. Retrieved and verified **5 legal free full papers**, read **5 papers**, and added **199 quote-verified records**, all from full sources. **1 paper/book has no free copy** under the prompt’s book/chapter exception. **6 entries resolved; 13 remain queued.** This round adds 5 full-read ledger lines and 1 no-free ledger line; cumulative batch totals are 22 full reads, 44 no-free entries and 1,246 evidence records.

Full reads this round: entry 33/rank 349 (felid anatomy, 41 records), 42/358 (Hawk Eyes I, 47), 49/365 (jumping-spider motion accepted manuscript, 21), 69/385 (fish spectral review, 54), and 78/394 (Spider vision primer, 36). The felid corresponding-author correction and supplementary literature overview were read. The fish review includes the author university PDF’s complete supplemental PDF and linked Table S1 workbook, including both summary and detailed sheets. No paper was marked read from an abstract, search result or blocked download.

The no-free result is entry 19/rank 335, the requested Animal Eyes book chapters: one successful OpenAlex title search, as allowed for a book/chapter, returned book reviews or unrelated works and no matching legal open book/chapter copy. It is not a claim that no legal copy can ever be found.

Semantic Scholar succeeded for entry 10 but returned **HTTP 429 at entry 36** and was stopped for the remainder of this round. Entries after that point were not silently counted as successful Semantic Scholar checks. OpenAlex and Europe PMC otherwise returned usable discovery responses; DOI-free entries 33 and 59 initially needed further metadata resolution. Provider failures, blocked indexed candidates and unverified files are not no-free results. The remaining queue is unchanged for those cases.

Remaining entries/ranks: **10/326, 36/352, 44/360, 47/363, 52/368, 59/375, 63/379, 65/381, 66/382, 68/384, 70/386, 76/392, 79/395**. Specifically, entry 10’s indexed Phlox publisher PDF returned 403; entries 44 and 47’s indexed Cell PDFs were inaccessible; entry 59’s ANU download returned a login HTML page, not a PDF, while its indexed Wiley PDF returned 403 (the UWA page only linked the publisher); entry 66’s author publications page listed a PDF but could not be retrieved to verify its target. These remain queued, alongside papers lacking indexed candidates while the required third provider was unavailable. The first three next actions are to recover the Phlox publisher copy, resume entry 36’s missing provider lookup after rate limiting, and retrieve the crane letter’s legal open archive copy.

Evidence caveats: felid dimensions and pupil geometry describe only four post-mortem individuals; technical repeats are not independent animals. Raptor horizontal overlap, vertical extent and all-elevation means are separate; Cooper’s bill-obscured reconstructed overlaps are graded i. Raptor figure-only printed labels were manually transcribed from rendered source images and visually verified, without estimating continuous curves. The jumping-spider manuscript’s inconsistent male Weibull parameters and hypothetical displacement examples are recorded separately. Review-level spider/fish values retain genus/family/group scope and grade g; explicit pigment predictions remain i, and gene-copy counts are not presented as functional receptor-class counts. The spider primer’s angular resolution conversion is approximate and is not a new measured grating cutoff.

All 199 new quotes passed quotecheck against the retrieved source text/PDF or an explicitly identified visual figure-label transcription; all appended records passed addlog validation. Downloads, source text, figures, workbook extraction and API caches remain outside the repository under `/tmp/oa/oa-5`. The quotecheck manifest is `/tmp/oa/oa-5/quotecheck-manifest.json`; scratch scripts remain untracked under `work/oa-5/`. Only the four permitted batch-5 files were committed. No app setup, builds, servers or app tests were run.
