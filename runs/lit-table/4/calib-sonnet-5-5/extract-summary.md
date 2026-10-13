# The literature table

Made by `tools/lit/extract.py` with claude-sonnet-5-5 through the Message Batches API on 2026-10-13 18:44 UTC.


## Cost estimate per topic (batch prices, US dollars)

| Topic | works | full texts | abstracts only | passages | estimate (expected) | estimate (ceiling) |
|---|---:|---:|---:|---:|---:|---:|
| calib | 188 | 60 | 120 | 505 | 3.01 | 6.58 |
| all (works found under several topics are counted in each, sent once) | 188 | 60 | 120 | 505 | 3.01 | 6.58 |

Whole run, each work sent once: 505 requests, 1.1 million input tokens, expected $3.01, ceiling $6.58.
The expected figure assumes the system prompt is read from the cache; the ceiling assumes it never is and that every reply is long. Token counts are estimated at 2.3 tokens a word.

## Actual usage

| | tokens |
|---|---:|
| input_tokens | 1139831 |
| output_tokens | 773432 |
| cache_creation_input_tokens | 4113 |
| cache_read_input_tokens | 2072952 |

Spent: **$5.12** at batch prices.

## Spend and records per topic (a work found under several topics is charged to the first)

| Topic | spent (US$) | records kept (works under several topics are listed in each) |
|---|---:|---:|
| calib | 5.119 | 1800 |

## What the check pass did

| | count |
|---|---:|
| dropped_duplicate | 6 |
| records_kept | 1800 |
| records_proposed | 1806 |
| replies_cut_off | 1 |
| replies_salvaged_after_cut_off | 1 |
| requests_succeeded | 505 |
