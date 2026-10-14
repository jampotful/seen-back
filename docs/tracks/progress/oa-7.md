# Open-access pass, batch 7

14 October 2026. The pass reached the end of the 79-paper batch.

- Papers checked in the initial script: **79**. OpenAlex returned 200 for all 79; Europe PMC returned 200 for all 59 applicable DOI lookups. Strict title, first-author and year matching was used for entries without a DOI.
- Free-copy candidates located: **20**. Confirmed full main-paper copies retrieved and read: **13**, including **one preprint** and **one accepted manuscript**.
- Evidence records logged with `addlog.py` and quote-checked: **1,375**. Of these, **1,324** come from full main texts or supplements, and **51** are explicitly marked `partial: true` from **13** abstract-only papers.
- No free-copy candidate returned: **59**, provisionally recorded in `oa-none-7.jsonl`. Another **7** papers had candidate copies that could not be retrieved; their entries say so, rather than asserting that no free copy exists.
- Two fully read papers produced no new sensory measurements: the photography methods paper (position 9) and the alpaca clinical ophthalmology study (position 62).

Full main texts read, by batch position: 9, 26, 39, 41, 46, 48, 51, 55, 56, 61, 62, 66, 76. The source ledger gives each paper's record count, version and supplement limitations. The largest extractions cover all 131 germination-study taxa and all 38 rows of the whale biosonar table.

Semantic Scholar returned one successful lookup and then HTTP 429 on two concurrent requests. The 56 subsequent Semantic Scholar lookups were skipped. `checked` lists only successful services, and the affected entries preserve the rate-limit limitation. Thus the 59 no-candidate results are not exhaustive negative findings.

Copies still inaccessible:

| Batch position | Access outcome |
| --- | --- |
| 33 | Repository landing page has a bot challenge; public repository API returned HTTP 403. |
| 35 | Publisher PDF and DOI target returned HTTP 403; no full text retrieved. |
| 36 | Publisher PDF and DOI target returned HTTP 403; abstract-only evidence logged. |
| 38 | Indexed journal PDF redirects to an unrelated travel domain and returns 404; current publisher destination denied access. No full text retrieved. |
| 49 | Europe PMC XML/PDF failed; publisher page is a subscription preview, not full text; author-hosted PDF returned HTTP 406. Abstract-only record retained. |
| 59 | Publisher and institutional repository returned bot challenges; no full text retrieved. Camera FOV in abstract was not logged as a measured honeybee FOV. |
| 69 | Linked article PDF returns a bot challenge. A different downloaded PDF was an unrelated repository guide and was rejected after checking its first page. Repository abstract read; quail species unspecified. |

The bat preprint supplement and supplements for positions 48, 55, 66 and 76 were not retrieved; the main texts were read and the source ledger preserves these limits. No per-species wasp facet numbers were invented. The visual-pigment scan was read by OCR, with its main measurement table checked against the page image. Source inconsistencies are flagged within affected records. The quail abstract is not assigned to an assumed genus, and an ambiguous finless-porpoise table row is retained only at genus rank.

Only the four batch-7 output files were changed. No app setup, build, server, browser test or self-test was run. No PDF, XML, downloaded full text, workbook, or intermediate script was added to the repository.

Follow-up: retry the blocked copies and missing supplements through legal public routes; complete the rate-limited discovery lookups; resolve the explicitly flagged source inconsistencies before using those values in profiles.
