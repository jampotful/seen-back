# Draft spec for whale (claude-sonnet-5-5)

Compiled from 400 records. Not offered; a person judges it on a phone through `?try=whale`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| matrices.CONE_L | [[0.14224,0.50505,0.27248,0.08024],[0.14224,0.5050... | g | True | marine-mammals.jsonl:Chi 2024 | The one pigment peak, 522 nm, is the low end of the published 522 to 524 nm range for dolphin and porpoise cone pigment. |
| params.M | "CONE_L" | g | True | marine-mammals.jsonl:Chi 2024 | The single cone pigment peak named by the matrix, 522 nm, is the low end of the published 522 to 524 nm range. |
| params.cpd | 3.95 | m | True | marine-mammals.jsonl:Bolin 2025 | The value 3.95 cycles per degree is the humpback whale estimate in this record. |
| params.gain | 3.16 | g | True | marine-mammals.jsonl:Madsen 1976 | A sensitivity gain of 0.5 log units is 10 to the power 0.5, which is about 3.16 times. |
| params.sheen | 0.5 | i | True |  |  |

## Warnings
- params.cpd: the floor run found this parameter invisible near 3.35

## Records dropped before sending
- table lines: 4035
