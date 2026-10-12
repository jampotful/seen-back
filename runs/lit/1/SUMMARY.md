# The senses literature

Gathered by `tools/lit/harvest.py` from OpenAlex and Europe PMC. Each topic's folder holds `index.jsonl` (one work a line: citation, OpenAlex's abstract, licence, addresses, and `text` where the full text of an openly licensed work was kept) and `text/`. `all.jsonl` joins the topics, one line per work with the topics it was found under. Full texts are kept only for works under a Creative Commons licence or in the public domain; every other work keeps its citation, abstract and addresses.

| Topic | works | with an abstract | full texts |
|---|---:|---:|---:|
| arachnids-other | 3699 | 2088 | 327 |
| bats | 2729 | 1103 | 359 |
| bees-wasps | 3970 | 2030 | 344 |
| beetles-bugs-others | 6935 | 2706 | 330 |
| birds-other | 4723 | 1902 | 337 |
| birds-raptors-owls | 3601 | 2202 | 289 |
| butterflies-moths | 4333 | 2048 | 344 |
| carnivores | 3168 | 2410 | 302 |
| cephalopods | 2424 | 933 | 323 |
| crocodilians-reptiles | 7210 | 2984 | 341 |
| crustaceans | 4450 | 1600 | 266 |
| dragonflies | 1298 | 1023 | 127 |
| fish | 5176 | 1765 | 314 |
| flies | 4793 | 1534 | 313 |
| frogs | 3034 | 947 | 337 |
| fungi-slime | 2867 | 1042 | 325 |
| insects-general | 2775 | 786 | 347 |
| mammals-other | 6375 | 2760 | 338 |
| marine-mammals | 3827 | 1972 | 347 |
| methods | 7322 | 3053 | 326 |
| plants-light | 2842 | 1033 | 298 |
| plants-touch | 2741 | 969 | 363 |
| primates | 4609 | 1870 | 252 |
| rodents-lagomorphs | 7626 | 2456 | 284 |
| salamanders | 2378 | 1128 | 227 |
| sea-life | 4796 | 2320 | 337 |
| sharks-rays | 2858 | 967 | 363 |
| snails-molluscs | 4229 | 2119 | 310 |
| spider-day | 990 | 754 | 101 |
| spider-general | 2179 | 1097 | 308 |
| spider-night | 650 | 470 | 41 |
| spider-web-tarantula | 1277 | 1019 | 113 |
| ungulates | 4930 | 2062 | 344 |
| worms-myriapods | 3056 | 1355 | 336 |

All topics: 118116 works, 8568 full texts.
860M	corpus
dropped (too large): corpus/all.jsonl
