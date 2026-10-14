# Open-access pass, batch 6

Updated 14 October 2026. Work follows `AGENTS.md` and `docs/tracks/prompts/oa-pass.md`. No app setup, build, server or app checks were run. Lookup responses, downloaded papers, extracts and temporary scripts stay outside the repository under `/tmp/oa/6`.

- Papers in batch: 79. Lookup pass attempted for all 79.
- Papers with indexed free-copy candidates: 20.
- Papers read in full and marked read: 2.
- Evidence records logged: 190; 42 are explicitly abstract-only.
- Papers with no free copy located by completed lookups: 24.
- Incomplete lookups: 35.
- Indexed free-copy candidates that could not be read: 15.

OpenAlex returned HTTP 429 at batch index 34 (owner rank 430); further requests to that host stopped. Europe PMC and Semantic Scholar were still checked for supplied DOIs. No-DOI entries require a matching OpenAlex title, first author and year before a DOI is accepted. Incomplete and inaccessible statuses are distinct from `no free copy`; none is marked read. Publisher HTTP 403 responses, broken links, bot-check pages, and Europe PMC HTTP 500 responses were retained as access failures.

Full reads so far:
- Cellular innovations and diversity in the lepidopteran compound eye: 62 records.
- Ultra-rapid vision in birds: 86 records.

The butterfly review records are secondary evidence with original-study attribution. Opsin gene counts in its supplementary table were not treated as receptor-class measurements. For the rapid-vision bird paper, the raw supplemental FFF values agree with main-text means, which differ from the abstract.

Next: read the remaining retrieved papers in batch order (yellow-poplar, mantises, comparative flicker review), log every supported measurement with verified quotations, and finalize source statuses.
