# oa-9 progress

## 2026-10-16

Round counts so far: 56 entries checked through EuropePMC REST, with OpenAlex, Semantic Scholar and Crossref excluded after round-wide rate limits. Exact-title web/repository discovery also ran across the batch before reading. Entries 1–2 resolved for this pass: 0 full papers read, 1 abstract-only record logged, 1 limited-search no-free-copy outcome, 1 known-free inaccessible dataset. Neither outcome retires the owner's wanted item.

Pending entries 3–56: accessible papers are cached under `/tmp/oa/oa9`; discovery/retrieval metadata and scripts are under `work/oa9`. Cached full copies are not marked read. EuropePMC XML candidates 26,50,53 returned HTTP500; these remain unread, with alternate legal retrieval still needed. Entry 14 SCIRP returned HTTP503, entry 32 Smith-Kettlewell returned HTTP406, entry 21 RNGR returned HTTP502. Full read, supplements, per-species evidence and quote checks remain necessary before full-read ledger entries.

Entries 3–4: NHM1293-row amphibian pupil dataset, ReadMe and reference DOCX retrieved. Logged2033 conservative g records:1293 adult pupil classifications,92 larval pupil classifications and648 binary activity-period classifications, with row-specific original source attribution. Non-diurnal is preserved and does not mean nocturnal; NA and larval `none` are not converted into pupil absence. This Jan2022 preprint-associated release differs from the published1294-species dataset. Published main PDF retrieved from City and read, but OUP supplementary parts A–F remain unavailable under the round-wide publisher refusal; no full-read ledger line is added for entry3. Its requested raw dataset is accessible and fully parsed, not skipped.

Entry4 fully read;7 records logged, including4 measured species/adaptation-specific temporal corner frequencies. All2041 records added so far pass quotecheck; evidence schema check passes. Current counts:56 discovery-checked;1 paper fully read;1 dataset fully parsed (paper supplement incomplete);2041 evidence records (1 abstract-only);1 no-free-copy and1 inaccessible outcome. Remaining:entry3 published supplements and entries5–56.
