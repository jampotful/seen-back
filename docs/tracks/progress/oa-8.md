# OA batch 8 (14 October 2026)

Batch contains 79 papers. Work is on `research/oa-8`; only batch 8 evidence, source status, and this progress note will be committed. No app setup, builds, or app tests are run.

The required lookup script is running across the batch in order, querying OpenAlex, Europe PMC, and Semantic Scholar by DOI. Title-only entries require title, first author, and year agreement. Book entries receive one OpenAlex check. Responses and downloaded papers stay outside Git under `/tmp/oa/8`; the lookup script is in ignored `work/`.

No papers have been read and no measurements have been logged yet. Next: finish all lookups; retrieve and identify legal free copies; read in batch order and verify every quote with `quotecheck.py` before adding evidence.
