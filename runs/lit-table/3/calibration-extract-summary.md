# The literature table

Made by `tools/lit/extract.py` with claude-haiku-5-5 through the Message Batches API on 2026-10-13 16:18 UTC.


## Cost estimate per topic (batch prices, US dollars)

| Topic | works | full texts | abstracts only | passages | estimate (expected) | estimate (ceiling) |
|---|---:|---:|---:|---:|---:|---:|
| calib | 188 | 60 | 120 | 505 | 0.08 | 0.21 |
| all (works found under several topics are counted in each, sent once) | 188 | 60 | 120 | 505 | 0.08 | 0.21 |

Whole run, each work sent once: 505 requests, 0.9 million input tokens, expected $0.08, ceiling $0.21.
The expected figure assumes the system prompt is read from the cache; the ceiling assumes it never is and that every reply is long. Token counts are estimated at 1.8 tokens a word.

## Actual usage

| | tokens |
|---|---:|
| input_tokens | 1139831 |
| output_tokens | 634430 |
| cache_creation_input_tokens | 0 |
| cache_read_input_tokens | 2077065 |

Spent: **$0.23** at batch prices.

## What the check pass did

| | count |
|---|---:|
| dropped_duplicate | 1 |
| dropped_quote_not_found | 3 |
| records_kept | 1077 |
| records_proposed | 1081 |
| replies_cut_off | 21 |
| replies_unparseable | 19 |
| requests_succeeded | 505 |
