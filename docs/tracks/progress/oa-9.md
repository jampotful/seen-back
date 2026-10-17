# oa-9 progress

## 2026-10-16

Round counts so far: 56 entries checked through EuropePMC REST, with OpenAlex, Semantic Scholar and Crossref excluded after round-wide rate limits. Exact-title web/repository discovery also ran across the batch before reading. Entries 1–2 resolved for this pass: 0 full papers read, 1 abstract-only record logged, 1 limited-search no-free-copy outcome, 1 known-free inaccessible dataset. Neither outcome retires the owner's wanted item.

Pending entries 3–56: accessible papers are cached under `/tmp/oa/oa9`; discovery/retrieval metadata and scripts are under `work/oa9`. Cached full copies are not marked read. EuropePMC XML candidates 26,50,53 returned HTTP500; these remain unread, with alternate legal retrieval still needed. Entry 14 SCIRP returned HTTP503, entry 32 Smith-Kettlewell returned HTTP406, entry 21 RNGR returned HTTP502. Full read, supplements, per-species evidence and quote checks remain necessary before full-read ledger entries.
