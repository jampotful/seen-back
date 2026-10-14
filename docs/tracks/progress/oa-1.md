# Open-access pass, batch 1

2026-10-14. Work in progress; base `de54993`.

- Batch entries: 79. The discovery pass processed all 79 before any paper was read.
- Candidate free-copy locations: 35; retrieval and identity verification are in progress.
- Papers read: 2 (entries 3 and 4); records logged: 395.
- Completed lookups with no free copy located: 10 (in `docs/views/sources/oa-none-1.jsonl`).
- Incomplete lookups or unresolved title-only identity: 34. These are pending, not declared unavailable.

OpenAlex returned HTTP 429 during an additional title lookup for entry 2. All further OpenAlex calls stopped, as the brief requires. The primary pass had saved OpenAlex responses through entry 37. Europe PMC and Semantic Scholar were queried for DOI entries afterward, with Semantic Scholar requests spaced by at least one second. Raw provider responses, status codes, candidate URLs, and the lookup script remain under `/tmp/oa`, outside the public repository. No papers or full texts are committed.

Pending lookup entry numbers: 2, 12, 35, 36, 37, 38, 41, 42, 43, 44, 45, 46, 47, 49, 51, 52, 53, 54, 55, 57, 58, 62, 63, 64, 65, 69, 72, 73, 74, 75, 76, 77, 78, 79. For title-only entries, exact title, first author and year must agree before accepting a match; incomplete citations were not guessed. Books and chapters receive only the permitted OpenAlex check.

Next: retrieve and verify candidate copies; read them in batch order, including available supplements; quote-check and append evidence with `addlog.py`, committing between papers. Only the four batch-1 output paths will change. No app setup, build, server, browser, or app tests ran.

Entry 3: 89 records, all passed PDF quotecheck verbatim and addlog validation. Review-derived measurements explicitly cite Katti et al.; primary studies were not opened. Reconstituted A1 spectra are distinguished from native A2 spectra, genetic complement is not logged as measured color vision, and pooled ranges remain assigned to the measured species group rather than individual species. No supplementary material was indicated in the review.

Entry 4: Lund University Publications linked the publisher-formatted PDF after the Figshare catalog page failed; first-page title and DOI confirmed. Read pp. 81–118, both tables and appendices. Logged 306 records: 296 table records quote-checked against the PDF layout text, 10 prose records quote-checked against the PDF. The p. 84 and p. 93 tables were also viewed to confirm 12+ receptor classes and ≥3 participating classes. Suggestive tests, model-derived class/mechanism counts, historical taxon-label conflicts, and the review's contradictory turtle/cat entries are explicitly qualified. No supplement was indicated. Next readable candidate: entry 6 (Anatidae), with its species data in supplementary material.
