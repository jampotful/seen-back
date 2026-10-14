# Open-access batch 2

Checkpoint 2026-10-14. The 79 entries (ranks 80 through 158) were checked with the prescribed discovery script. It saved responses outside the repository in `/tmp/oa`. There are 38 entries with free-copy candidates and 39 entries with no location returned by the queried indexes. Ranks 87 and 120 remain unresolved: their DOI-free entries did not yield the required title, first-author and year match. Negative index results are recorded in `docs/views/sources/oa-none-2.jsonl`.

Read: rank 80, the complete amphibian pupil CSV and its documentation. Logged 2,240 records, all checked against the downloaded CSV with `quotecheck.py`: 1,385 pupil classifications (1,293 adult and 92 larval), 648 binary activity classifications and 207 eye diameters. No NA cell was treated as a measurement. Adult and larval records are separate. The larval `none` entry for Rhinoderma darwinii was not interpreted as an observed pupil absence.

Reading continues in batch order. Rank 81 has a free PMC manuscript, but the XML service failed and the PMC page returned a bot challenge. Rank 83's repository API resolves the correct title. Rank 84's full XML is retrieved, with its supplements still being fetched. No inaccessible candidate is marked as read. App setup and app checks were skipped under `AGENTS.md` and the task instruction.

Next: finish the access attempts for ranks 81 and 83, read rank 84 and its supplement, and continue with the next accessible entry. Only the four files authorized by `oa-pass.md` are changed. PDFs, full text, metadata caches and extraction scripts stay outside the repository.
