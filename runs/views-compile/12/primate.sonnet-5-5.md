# Draft spec for primate (claude-sonnet-5-5)

Compiled from 400 records. Not offered; a person judges it on a phone through `?try=primate`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| matrices.PRIMATE_TRI | [[0.32957,0.46264,0.13475,0.07303],[0.1783,0.50901... | g | True | primates.jsonl:Baylor 1987, primates.jsonl:Carvalho 2017, primates.jsonl:Kawamura 2000 | The pigment peaks 430 nm (cynomolgus), 530 nm (howler) and 561 nm (marmoset) are each stated in a cited record. |
| params.M | "PRIMATE_TRI" | g | True | primates.jsonl:Baylor 1987, primates.jsonl:Carvalho 2017, primates.jsonl:Kawamura 2000 | The matrix is built from peaks 430, 530 and 561 nm stated in the three cited monkey records. |
| params.cpd | 26.3 | m | False | primates.jsonl:Laughlin 2008 | The value equals the 26.3 cycles per degree stated for rhesus monkeys. |
| params.fov | 152 | g | True | primates.jsonl:Denion É 2016 | 180 x 115 / 136.1 = 152, scaling a person's field by the Pan-like to human ratio of lateral eccentricity. |

## Warnings
- params.cpd: the floor run found this parameter invisible near 3.35

## Records dropped before sending
- table lines: 3570
