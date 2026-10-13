# Draft spec for primate (claude-sonnet-5-5)

Compiled from 400 records. Not offered; a person judges it on a phone through `?try=primate`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| matrices.PRIMATE_TRI | [[0.32957,0.46264,0.13475,0.07303],[0.1783,0.50901... | g | True | primates.jsonl:Baylor 1987, primates.jsonl:Carvalho 2017, primates.jsonl:Kawamura 2000 | Peaks 430, 530 and 561 nm each lie within 2 nm of a cited record's value. |
| params.M | "PRIMATE_TRI" | g | True | primates.jsonl:Baylor 1987, primates.jsonl:Carvalho 2017, primates.jsonl:Kawamura 2000 | The matrix is built from the peaks 430 (macaque blue cone), 530 (howler monkey) and 561 (marmoset red pigment) nanometres. |
| params.cpd | 24 | m | True | primates.jsonl:Laughlin 2008, primates.jsonl:Yarczower 1966 | The value 24 lies between the stumptail macaque's 21.4 and the young rhesus monkey's 26.3 cycles per degree. |
| params.fov | 152 | g | True | primates.jsonl:Denion É 2016 | 180 x 115 / 136.1 = 152, scaling a person's 180 degrees by the Pan-like to human ratio of lateral field. |

## Warnings
- params.cpd: the floor run found this parameter invisible near 3.35

## Records dropped before sending
- table lines: 3570
