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

Rechecked only assigned entries **10, 36, 44, 47, 52, 59, 63, 65, 66, 68, 70, 76 and 79** (ranks 326, 352, 360, 363, 368, 375, 379, 381, 382, 384, 386, 392, 395). This round adds **13 papers checked, 2 confirmed free-version candidates found but inaccessible, 0 full copies retrieved, 0 full papers read, and 37 abstract-only records** from 10 papers. Twelve available abstracts/summaries were reviewed; the exact 2005 crane article has no abstract on either Europe PMC or USGS. The no-copy ledger gains **11 limited-search “no free copy” statuses and 2 “free copy inaccessible” statuses**, each explicitly retaining unread/manual-acquisition status. No full-read ledger entry was added. Date follows the owner's 16 October research round; execution was 17 October UTC.

One discovery script checked Europe PMC and Crossref across all 13 entries before evidence extraction. OpenAlex and Semantic Scholar were skipped because their earlier HTTP 429 refusals were recorded for the round. Europe PMC returned no PMC full copy. Crossref supplied exact-title matches for papers missing DOIs; its entry-63 title query returned HTTP 429. The initial script completed its other DOI requests before that result was reviewed; no further Crossref requests were initiated afterward. This limitation is explicit in each new status. Exact-title web searches and available publisher/repository/author pages supplemented discovery. The 1998 Phlox, 1988 fish and 1988 harvestman values come only from actually retrieved publisher-deposited Crossref abstracts, with that provenance, retrieval URL, partial:true and abstract access in every record.

The 2005 crane and 2012 cuttlefish articles have open-access version-of-record licenses in Crossref, but publisher/linking hosts were already refusing access, and Elsevier's legal API refused the crane retrieval with proxy CONNECT HTTP 403. The cuttlefish repository provides its abstract only. The skink ANU PDF link returns DSpace login HTML and request-a-copy; no login was attempted. Nature PDF URLs return subscription landing HTML. Springer pages provide summaries and explicitly require subscription for full text. The Neitz author bibliography returned HTTP 465 and was stopped. Known publisher refusals were not retried; ResearchGate and other excluded uploads were not used.

All **37 new quotes passed quotecheck.py verbatim against the extracted abstract/summary actually retrieved**, and addlog.py validated each append. The dragonfly's five ventral-eye peaks are receptor sensitivity peaks, not purified pigment absorbance; the jumping-spider colour result retains the brightness caveat; unnamed salticid and bibionid results remain group grade; fish cone densities are not converted into acuity; no harvestman spectral wavelengths or visual fields are inferred. Source files and scratch scripts remain outside the repository under /tmp/oa/oa-5/round-20261016. No app, build or test command ran.

This assigned subset is complete as a documented search pass, with all 13 full papers still unread and available for manual acquisition. A future retrieval pass should start with the legally free crane/cuttlefish articles, then the restricted ANU skink candidate. Earlier unresolved entries outside this assignment are unchanged.
