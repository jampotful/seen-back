# OA batch 5 — 2026-10-14

In progress. All 79 entries went through the one-script lookup pass before reading. 31 papers had candidate free locations; 17 complete papers retrieved. OpenAlex returned HTTP 429 at index 41 (rank 358); no further OpenAlex requests were sent. Europe PMC and Semantic Scholar continued. The Animal Eyes title query returned HTTP 400. NCBI BioC returned HTTP 429 during fallback retrieval and was stopped.

Full papers read: 17 (batch indices [3, 5, 6, 11, 24, 27, 28, 38, 42, 44, 45, 47, 49, 50, 54, 70, 74]; ranks [320, 322, 323, 328, 341, 344, 345, 355, 359, 361, 362, 364, 366, 367, 371, 387, 391]). Records logged: 937 (928 full-text records, 9 partial abstract records). The source ledger includes zero-record reads and exactly preserves batch titles. Every appended quote passed the named quote-check procedure. Image-only table/figure values were checked visually; independently OCRed figure text is included in the source text used for reef-fish quote verification.

Negative lookup lines: 24. They mean no free location found in completed lookups, not proof none exists. Unresolved entries excluded from oa-none-5: [18, 32, 35, 41, 51, 52, 53, 55, 56, 57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 69, 71, 75, 76, 78]. Fourteen candidate papers have inaccessible or unverified copies and are excluded from the negative ledger. No unread copy is marked read.

Downloaded papers still to read, in batch order: [] (ranks []). Next: continue at the first pending paper, then the next two.

Source caveats: red drum FFF is 54 Hz in the reef-fish table and 53 Hz in its Discussion; both are retained. The Harris’s hawk workbook/main-text subject-label discrepancy is recorded. Motion-neuron temporal tuning is distinct from CFF. Pigment-template peaks, opsin-derived peaks, pooled taxa and secondary values are labelled by method/note/grade. Camel OCT fovea terminology is retained as an author identification, not converted to acuity. Supplementary material coverage is described in the source ledger.

PDFs, XML, source texts, supplementary files, API responses and extraction scripts remain outside the repository (/tmp/oa and /workspace/work/oa-5). Only batch-5 evidence, source ledgers and this progress note are edited. No app setup, build, prepare.py, server, browser or app checks run.
