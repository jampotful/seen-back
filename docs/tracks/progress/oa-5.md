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

Round in progress. All 19 assigned entries checked in a single discovery script before reading. Semantic Scholar returned HTTP 429 at entry 36 and was stopped. OpenAlex and Europe PMC continued successfully. Five full papers verified so far; one paper read and 41 records logged and quote-checked. One book/chapter has no free copy after the prompt’s one-check exception. Entries with an unavailable required provider or blocked indexed copies remain queued.
