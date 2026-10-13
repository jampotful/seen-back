# The literature table

Made by `tools/lit/extract.py` with claude-haiku-5-5 through the Message Batches API on 2026-10-13 22:06 UTC.


## Cost estimate per topic (batch prices, US dollars)

| Topic | works | full texts | abstracts only | passages | estimate (expected) | estimate (ceiling) |
|---|---:|---:|---:|---:|---:|---:|
| arachnids-other | 3699 | 327 | 1871 | 3626 | 1.03 | 2.28 |
| bats | 2729 | 359 | 945 | 3178 | 0.95 | 2.05 |
| bees-wasps | 3970 | 343 | 1824 | 3947 | 1.12 | 2.48 |
| beetles-bugs-others | 6935 | 334 | 2511 | 4519 | 1.23 | 2.79 |
| birds-other | 4723 | 340 | 1686 | 3725 | 1.06 | 2.35 |
| birds-raptors-owls | 3601 | 274 | 1973 | 3479 | 0.95 | 2.15 |
| butterflies-moths | 4333 | 345 | 1741 | 3783 | 1.07 | 2.38 |
| carnivores | 3168 | 297 | 2129 | 3753 | 1.04 | 2.33 |
| cephalopods | 2424 | 320 | 773 | 2509 | 0.75 | 1.61 |
| crocodilians-reptiles | 7210 | 362 | 2759 | 4720 | 1.27 | 2.90 |
| dragonflies | 1298 | 120 | 885 | 1529 | 0.43 | 0.96 |
| flies | 4793 | 333 | 1366 | 3897 | 1.15 | 2.49 |
| frogs | 3034 | 327 | 901 | 3080 | 0.93 | 1.99 |
| insects-general | 2775 | 320 | 734 | 2793 | 0.85 | 1.81 |
| marine-mammals | 3827 | 350 | 1783 | 4036 | 1.18 | 2.57 |
| plants-light | 2842 | 297 | 908 | 2981 | 0.90 | 1.92 |
| plants-touch | 2741 | 360 | 826 | 3165 | 0.96 | 2.05 |
| primates | 4609 | 267 | 1730 | 3764 | 1.07 | 2.36 |
| rodents-lagomorphs | 7626 | 316 | 2284 | 4445 | 1.24 | 2.77 |
| ungulates | 4930 | 346 | 1865 | 3733 | 1.04 | 2.33 |
| methods | 7322 | 518 | 2888 | 6548 | 1.88 | 4.13 |
| all (works found under several topics are counted in each, sent once) | 88589 | 6855 | 34382 | 77210 | 22.08 | 48.71 |

Whole run, each work sent once: 69180 requests, 123.7 million input tokens, expected $19.60, ceiling $43.47.
The expected figure assumes the system prompt is read from the cache; the ceiling assumes it never is and that every reply is long. Token counts are estimated at 2.3 tokens a word.

## Actual usage

| | tokens |
|---|---:|
| input_tokens | 128023461 |
| output_tokens | 31139043 |
| cache_creation_input_tokens | 0 |
| cache_read_input_tokens | 284537340 |

Spent: **$15.61** at batch prices.

## Spend and records per topic (a work found under several topics is charged to the first)

| Topic | spent (US$) | records kept (works under several topics are listed in each) |
|---|---:|---:|
| arachnids-other | 0.711 | 2040 |
| bats | 1.076 | 4981 |
| bees-wasps | 0.994 | 4132 |
| beetles-bugs-others | 0.987 | 4711 |
| birds-other | 0.934 | 3726 |
| birds-raptors-owls | 0.534 | 1585 |
| butterflies-moths | 0.878 | 4052 |
| carnivores | 0.649 | 1655 |
| cephalopods | 0.561 | 1562 |
| crocodilians-reptiles | 0.792 | 3078 |
| dragonflies | 0.288 | 980 |
| flies | 0.950 | 4448 |
| frogs | 0.672 | 2017 |
| insects-general | 0.312 | 4688 |
| marine-mammals | 0.961 | 4035 |
| plants-light | 0.718 | 1191 |
| plants-touch | 0.632 | 765 |
| primates | 0.871 | 3570 |
| rodents-lagomorphs | 0.828 | 2949 |
| ungulates | 0.562 | 1769 |
| methods | 0.698 | 7055 |

## What the check pass did

| | count |
|---|---:|
| dropped_check_py | 60 |
| dropped_duplicate | 143 |
| dropped_no_quote | 3 |
| dropped_quote_not_found | 516 |
| dropped_quote_too_long | 61 |
| records_kept | 50286 |
| records_proposed | 51069 |
| replies_cut_off | 14 |
| replies_salvaged_after_cut_off | 16 |
| replies_unparseable | 2 |
| requests_succeeded | 69180 |

check.py reasons: source needs authors and year x38; unknown trait # (say # in note to add one) x22
