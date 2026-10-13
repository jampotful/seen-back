# The literature table

Made by `tools/lit/extract.py` with claude-haiku-5-5 through the Message Batches API on 2026-10-13 20:19 UTC.


## Cost estimate per topic (batch prices, US dollars)

| Topic | works | full texts | abstracts only | passages | estimate (expected) | estimate (ceiling) |
|---|---:|---:|---:|---:|---:|---:|
| fungi-slime | 2867 | 325 | 883 | 3101 | 0.95 | 2.02 |
| fish | 5176 | 314 | 1563 | 3785 | 1.09 | 2.40 |
| sharks-rays | 2858 | 355 | 849 | 2819 | 0.84 | 1.82 |
| spider-general | 2179 | 306 | 925 | 2598 | 0.76 | 1.66 |
| spider-night | 650 | 42 | 406 | 638 | 0.17 | 0.39 |
| spider-day | 990 | 96 | 617 | 1112 | 0.32 | 0.70 |
| spider-web-tarantula | 1277 | 112 | 870 | 1396 | 0.39 | 0.87 |
| snails-molluscs | 4229 | 310 | 1946 | 3822 | 1.07 | 2.38 |
| sea-life | 4796 | 332 | 2078 | 4058 | 1.13 | 2.53 |
| crustaceans | 4450 | 271 | 1445 | 3013 | 0.84 | 1.88 |
| mammals-other | 6375 | 340 | 2582 | 4697 | 1.34 | 2.96 |
| worms-myriapods | 3056 | 340 | 1156 | 3665 | 1.11 | 2.38 |
| salamanders | 2378 | 221 | 979 | 2548 | 0.75 | 1.63 |
| all (works found under several topics are counted in each, sent once) | 41281 | 3364 | 16299 | 37252 | 10.77 | 23.62 |

Whole run, each work sent once: 34467 requests, 65.3 million input tokens, expected $9.95, ceiling $21.84.
The expected figure assumes the system prompt is read from the cache; the ceiling assumes it never is and that every reply is long. Token counts are estimated at 2.3 tokens a word.

## Actual usage

| | tokens |
|---|---:|
| input_tokens | 68909546 |
| output_tokens | 14066473 |
| cache_creation_input_tokens | 423639 |
| cache_read_input_tokens | 141339132 |

Spent: **$7.71** at batch prices.

## Spend and records per topic (a work found under several topics is charged to the first)

| Topic | spent (US$) | records kept (works under several topics are listed in each) |
|---|---:|---:|
| fungi-slime | 0.701 | 1257 |
| fish | 1.086 | 4369 |
| sharks-rays | 0.576 | 1784 |
| spider-general | 0.636 | 2118 |
| spider-night | 0.095 | 781 |
| spider-day | 0.120 | 1214 |
| spider-web-tarantula | 0.188 | 849 |
| snails-molluscs | 0.628 | 1368 |
| sea-life | 0.637 | 1592 |
| crustaceans | 0.651 | 2983 |
| mammals-other | 0.880 | 2769 |
| worms-myriapods | 0.976 | 3155 |
| salamanders | 0.538 | 1136 |

## What the check pass did

| | count |
|---|---:|
| dropped_check_py | 18 |
| dropped_duplicate | 49 |
| dropped_quote_not_found | 170 |
| dropped_quote_too_long | 24 |
| records_kept | 22376 |
| records_proposed | 22637 |
| replies_cut_off | 7 |
| replies_salvaged_after_cut_off | 7 |
| replies_unparseable | 1 |
| requests_succeeded | 34467 |

check.py reasons: unknown trait # (say # in note to add one) x16; source needs authors and year x2
