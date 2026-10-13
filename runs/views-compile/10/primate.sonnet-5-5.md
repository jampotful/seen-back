# Draft spec for primate (claude-sonnet-5-5)

Compiled from 400 records. Not offered; a person judges it on a phone through `?try=primate`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| matrices.primate_trichromat | [[0.32957,0.46264,0.13475,0.07303],[0.18301,0.5089... | g | True | primates.jsonl:Baylor 1987, primates.jsonl:Carvalho 2017, primates.jsonl:Kawamura 2000 | The peaks 430, 531 and 561 nm come from R31, and each lies within 2 nm of a cited peak (430 R31, 530 R32, 561 R23). |
| params.M | "primate_trichromat" | g | True | primates.jsonl:Baylor 1987, primates.jsonl:Carvalho 2017, primates.jsonl:Kawamura 2000 | The matrix name stands for a matrix built from the peaks 430, 531 and 561 nm that R31 gives for a cynomolgus monkey, with R32 giving 530 nm and R23 giving 561 nm. |
| params.cpd | 26.3 | m | True | primates.jsonl:Laughlin 2008 | The value equals the 26.3 cycles per degree that rhesus monkeys reached, which was the highest level the test assessed. |

## Warnings
- params.cpd: the floor run found this parameter invisible near 3.35

## Records dropped before sending
- table lines: 3570
