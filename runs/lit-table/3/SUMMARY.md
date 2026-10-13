# The literature table

Made by `tools/lit/extract.py` with claude-haiku-5-5 through the Message Batches API on 2026-10-13 16:09 UTC.


## Cost estimate per topic (batch prices, US dollars)

| Topic | works | full texts | abstracts only | passages | estimate (expected) | estimate (ceiling) |
|---|---:|---:|---:|---:|---:|---:|
| spider-night | 650 | 41 | 424 | 650 | 0.09 | 0.25 |
| all (works found under several topics are counted in each, sent once) | 650 | 41 | 424 | 650 | 0.09 | 0.25 |

Whole run, each work sent once: 650 requests, 0.8 million input tokens, expected $0.09, ceiling $0.25.
The expected figure assumes the system prompt is read from the cache; the ceiling assumes it never is and that every reply is long. Token counts are estimated at 1.8 tokens a word.

## Actual usage

| | tokens |
|---|---:|
| input_tokens | 1010379 |
| output_tokens | 435969 |
| cache_creation_input_tokens | 12339 |
| cache_read_input_tokens | 2661111 |

Spent: **$0.17** at batch prices.

## What the check pass did

| | count |
|---|---:|
| dropped_check_py | 91 |
| dropped_quote_not_found | 1 |
| dropped_quote_too_long | 1 |
| records_kept | 644 |
| records_proposed | 737 |
| replies_cut_off | 4 |
| replies_unparseable | 4 |
| requests_succeeded | 650 |

check.py reasons: source needs a doi or a url x91

Files over 95 MB are dropped from the branch:
