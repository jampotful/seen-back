# Draft spec for whale (claude-sonnet-5-5)

Compiled from 400 records. Not offered; a person judges it on a phone through `?try=whale`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| matrices.marine_mono | [[0.15096,0.50683,0.26256,0.07965],[0.15096,0.5068... | g | True | marine-mammals.jsonl:Chi 2024, marine-mammals.jsonl:Peichl 2001 | The single pigment peak of 524 nm is the upper end of the 522 to 524 nm range in R37. |
| params.M | "marine_mono" | g | True | marine-mammals.jsonl:Chi 2024, marine-mammals.jsonl:Peichl 2001 | One cone peak at 524 nm (upper end of R37's 522 to 524 nm) with no S-cones (R46) gives a single-sensor matrix, which is the app's mapping. |
| params.cpd | 4.05 | m | True | marine-mammals.jsonl:Lisney 2018 | The value 4.05 is the middle of 3.3 cycles per degree (humpback whale) and 4.8 (Bryde's whale). |
| params.fov | 125 | m | True | marine-mammals.jsonl:JM 2022 | Both records give 120 to 130 degrees and 125 is the middle of that range. |
| params.gain | 3.16 | g | True | marine-mammals.jsonl:Madsen 1976 | 10 raised to 0.5 log units of extra sensitivity gives a factor of about 3.16. |
| params.sheen | 0.6 | i | True |  |  |

## Warnings
- params.cpd: the floor run found this parameter invisible near 3.35

## Records dropped before sending
- table lines: 4035
