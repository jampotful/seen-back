# Draft spec for whale (claude-sonnet-5-5)

Compiled from 400 records. Not offered; a person judges it on a phone through `?try=whale`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| matrices.SEA_L | [[0.14657,0.50601,0.26748,0.07994],[0.14657,0.5060... | g | True | marine-mammals.jsonl:Chi 2024 | The single peak of 523 nm lies inside the 522 to 524 nm range reported for dolphin and porpoise cones. |
| params.M | "SEA_L" | g | True | marine-mammals.jsonl:Chi 2024, marine-mammals.jsonl:Peichl 2001 | The matrix is built from one long-wavelength cone peak near 523 nm, since whales and seals studied lack the short-wavelength cone. |
| params.cpd | 3.95 | m | True | marine-mammals.jsonl:Bolin 2025 | The value 3.95 cycles per degree is the estimate for a humpback whale eye. |
| params.fov | 125 | m | True | marine-mammals.jsonl:JM 2022, marine-mammals.jsonl:Kremers 2016 | 125 degrees is the middle of the 120 to 130 degree field both records give. |
| params.gain | 3.16 | g | True | marine-mammals.jsonl:Madsen 1976 | A dolphin is 0.5 log units more sensitive than a person in low light, and 10^0.5 is about 3.16. |
| params.sheen | 0.5 | i | True |  |  |
| sound.k | 1 | i | True |  |  |

## Warnings
- params.cpd: the floor run found this parameter invisible near 3.35

## Records dropped before sending
- table lines: 4035
