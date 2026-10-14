# Open-access batch 6

## 2026-10-14

Checkpoint through entry 32: 4 papers settled, 75 of 79 remaining. Entries 1 and 2 have complete required lookups and no free copy. Entry 18 was read in full from its HAL publisher-version PDF, with the S10 XLSX dataset and S11 statistical supplement. It contributes 325 records; 14 further abstract-only records from entries 4, 13, 15 and 17 carry `partial: true`. Entry 32 contributes another 86 full-text records. Additional partial evidence from entries 19, 25, 26, 30 and 31 contributes 21 records. Total evidence: 446 records (411 full-text, 35 partial).

The required script processed all 79 entries, saving API responses outside the repository under `/tmp/oa/oa-6`. OpenAlex returned HTTP 429 at entry 3, and further requests to that host stopped. Later papers without a verified free copy remain unresolved; failed or skipped API calls are not evidence that no free copy exists. Europe PMC and Semantic Scholar were queried for the available DOIs; no additional requests will be sent to Semantic Scholar after the coordinator reported its shared throttle.

Entry 18's batch title is a French description; the linked HAL record identifies the published English article, *A flashing light may not be that flashy*, DOI 10.1371/journal.pone.0279718. The source marker retains the exact batch title. The dataset includes 200 retained and 26 excluded rows: one excluded row gives no value; the other 225 rows have records with risk-of-bias codes and original-study metadata. Ninety additional values stated in comment cells and ten group aggregates are logged separately. Excluded results are explicitly marked as such. Genus and aggregate records have grade `g`. The beetle 300–500 Hz value is infrared pit-organ temporal response, not visual flicker fusion; the source's fps sheep value also retains fps. Every record passed quotecheck against the downloaded PDF or faithful spreadsheet text extraction, then addlog validation. No app checks were run.

Entry 32 was read from both the Europe PMC XML and publisher PDF, with its spreadsheet supplement and the eye-type symbols in Figure 2 visually checked. The supplement reports gene-copy numbers rather than measured receptor classes, so these were not converted to spectral-class counts. All 86 records passed quotecheck.

Continuing in batch order at entry 33. Unresolved earlier entries: 3–17 except the abstract-only evidence noted above. Scratch downloads are not committed.
