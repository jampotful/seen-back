# Progress: the literature table, burst 4 (track lit, branch agent/pipeline)

Started 13 October 2026, 18:00 UTC; stops at 120 minutes. Spend allowance $60; Console workspace capped at $150.

## Done
- Read STATUS, the burst files and run 3's summaries.
- Defects fixed in `tools/lit/extract.py`: reply limit raised from 4,000 to 12,000 tokens, and a reply that is still cut off keeps its complete records; a source with no doi takes its url from the index record (landing page, pdf, PubMed Central, PubMed, OpenAlex, Europe PMC); the cost estimate now uses the measured 2.3 tokens a word and 700 output tokens a passage (it printed $0.17 for spider-night, the observed cost, where it printed $0.09). Prices for Sonnet 5.5 added. Per-topic spend and records in the summary. 11 tests pass.
- `ci/lit/table.env` gains LIT_MODEL, LIT_STRONG_MODEL and LIT_STRONG_TOPICS, LIT_CALIB_MODELS, LIT_SKIP_TABLE, LIT_KEEP.
- Plan for all 34 topics on Haiku: 99,937 requests, expected $28.4, ceiling $62.9. Sonnet costs 20 times as much (spider-night: $3.4 against $0.17).

## Calibration (run 4 on `ci`, runs/lit-table/4, 13 Oct 18:45 UTC)
| | Haiku 5.5 (fixed) | Sonnet 5.5 | Haiku, run 3 |
|---|---:|---:|---:|
| same trait and value | 153 of 361 (42%) | 164 (45%) | 138 (38%) |
| plus another value form | 243 (67%) | 262 (73%) | 221 (61%) |
| records on these sources | 1,431 | 1,800 | 1,077 |
| additions (match no logged record) | 1,206 | 1,558 | 875 |
| spent | $0.24 | $5.12 | $0.23 |
Sonnet gains 3 points of strict recovery and 6 with the loose reading at 21 times the cost, under the 10-point bar, so Haiku is used everywhere. Replies cut off: 1 of 505 (was 21), and that one was salvaged.

## Full run (Haiku 5.5; each push keeps what pub/lit-table already holds)
- fullA done (run 5 on `ci`, 13 Oct 20:20 UTC): 13 topics, 34,467 requests, $7.71 (estimate $9.95), 22,376 records kept. Per topic spend and records are in `runs/lit-table/5/SUMMARY-fullA-haiku-5-5.md`. 7 replies cut off, all salvaged.
- fullBC (`run/lit-table/fullBC`, ceiling $45) was queued behind fullA and holds the other 21 topics; it adds to `pub/lit-table` when it ends, and its summary returns to `ci` as the next run number. Expected about $18.
- Spent so far: $0.24 + $5.12 (calibration) + $7.71 = $13.07.

## Next
1. When fullBC returns, read its SUMMARY and check that `pub/lit-table` holds 34 topic files.
2. The batch audit of the table (queue 6).
