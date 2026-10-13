# Progress: the literature table, burst 4 (track lit, branch agent/pipeline)

Started 13 October 2026, 18:00 UTC; stops at 120 minutes. Spend allowance $60; Console workspace capped at $150.

## Done
- Read STATUS, the burst files and run 3's summaries.
- Defects fixed in `tools/lit/extract.py`: reply limit raised from 4,000 to 12,000 tokens, and a reply that is still cut off keeps its complete records; a source with no doi takes its url from the index record (landing page, pdf, PubMed Central, PubMed, OpenAlex, Europe PMC); the cost estimate now uses the measured 2.3 tokens a word and 700 output tokens a passage (it printed $0.17 for spider-night, the observed cost, where it printed $0.09). Prices for Sonnet 5.5 added. Per-topic spend and records in the summary. 11 tests pass.
- `ci/lit/table.env` gains LIT_MODEL, LIT_STRONG_MODEL and LIT_STRONG_TOPICS, LIT_CALIB_MODELS, LIT_SKIP_TABLE, LIT_KEEP.
- Plan for all 34 topics on Haiku: 99,937 requests, expected $28.4, ceiling $62.9. Sonnet costs 20 times as much (spider-night: $3.4 against $0.17).

## Next
1. Calibration push `run/lit-table/calib`: Haiku (fixed) and Sonnet on the calibration set only.
2. Choose the model; full run in pushes of about half the topics each.
