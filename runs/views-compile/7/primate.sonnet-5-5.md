# Draft spec for primate (claude-sonnet-5-5)

Compiled from 300 records. Not offered; a person judges it on a phone through `?try=primate`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| by.Aotus.params.sat | 0 | g | True | primates.jsonl:Jacobs 1996, primates.jsonl:Kawamura 2016 | The records state owl monkeys lack colour vision with a single cone type, which the app maps to a saturation of 0. |
| by.Microcebus murinus.params.cpd | 4.9 | m | False | primates.jsonl:Melin 2016 | R5 states 4.9 cycles per degree for Microcebus murinus. |
| by.Pan.params.fov | 152 | g | True | primates.jsonl:Denion É 2016 | 180 x 115 / 136.1 = 152.1, using the Pan-like and human lateral eccentricities in R18 against the app's 180 for a person. |
| matrices.PRIMATE_TRI | null | g | True | primates.jsonl:Baylor 1987, primates.jsonl:Carvalho 2017, primates.jsonl:Kawamura 2000 | The peaks 430, 530 and 561 nm are the values of R31 (cynomolgus), R32 (howler monkey) and R23 (marmoset). |
| params.M | "PRIMATE_TRI" | g | True | primates.jsonl:Baylor 1987, primates.jsonl:Carvalho 2017, primates.jsonl:Kawamura 2000 | The matrix named is built from peaks 430, 530 and 561 nm, each stated by one of these records for a primate. |
| params.cpd | 30 | m | True | primates.jsonl:Solomon 2014, primates.jsonl:Troilo 1993 | Both records state about 30 cycles per degree at the marmoset fovea, and the value equals that. |

## Warnings
- params.cpd: the floor run found this parameter invisible near 3.35

## Records dropped before sending
- table lines: 3570
