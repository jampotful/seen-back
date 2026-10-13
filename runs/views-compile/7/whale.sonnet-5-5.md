# Draft spec for whale (claude-sonnet-5-5)

Compiled from 300 records. Not offered; a person judges it on a phone through `?try=whale`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| matrices.CONE_L | null | g | True | marine-mammals.jsonl:Chi 2024 | The pigment peak of 524 nm is the upper end of the 522 to 524 nm range given for dolphin and porpoise long-wavelength pigment. |
| params.M | "CONE_L" | g | True | marine-mammals.jsonl:Chi 2024, marine-mammals.jsonl:Peichl 2001 | The matrix name stands for one cone pigment near 524 nm (R37) with no blue-sensitive cone (R46); turning that into a matrix is the app's mapping. |
| params.cpd | 4 | m | True | marine-mammals.jsonl:Lisney 2018 | 4 lies between the humpback whale value of 3.3 and the Bryde's whale value of 4.8 cycles per degree. |
| params.fov | 125 | m | True | marine-mammals.jsonl:JM 2022 | 125 is the middle of the 120 to 130 degrees given for the bottlenose dolphin. |
| params.gain | 3.16 | g | True | marine-mammals.jsonl:Madsen 1976 | A dolphin is 0.5 log units more sensitive than a person in dim light, and 10 to the power 0.5 is about 3.16. |
| params.sheen | 0.5 | i | True |  |  |
| sound.k | 1 | i | True |  |  |

## Warnings
- added the row 'Settings the app chose', which names 1 invented parameters the reply left unnamed
- params.cpd: the floor run found this parameter invisible near 3.35

## Records dropped before sending
- table lines: 4035
