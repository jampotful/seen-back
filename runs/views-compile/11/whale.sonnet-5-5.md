# Draft spec for whale (claude-sonnet-5-5)

Compiled from 400 records. Not offered; a person judges it on a phone through `?try=whale`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| matrices.WHALE_L_CONE | [[0.15096,0.50683,0.26256,0.07965],[0.15096,0.5068... | g | True | marine-mammals.jsonl:Chi 2024 | The pigment peak of 524 nanometres is the top of the published 522 to 524 nanometre range for the dolphin long-wavelength cone. |
| params.M | "WHALE_L_CONE" | g | True | marine-mammals.jsonl:Chi 2024, marine-mammals.jsonl:Peichl 2001 | The matrix keeps a single cone near 524 nanometres (R37) because the blue-sensitive cone is absent in all whales and seals studied (R46). |
| params.cpd | 5 | m | True | marine-mammals.jsonl:Hanke 2009, marine-mammals.jsonl:Lisney 2018 | The value 5 lies between the Bryde's whale estimate of 4.8 cycles per degree and the harbour seal estimate of 8.7 in air. |
| params.fov | 125 | m | True | marine-mammals.jsonl:JM 2022, marine-mammals.jsonl:Kremers 2016 | The value 125 is the middle of the 120 to 130 degree visual field given for the bottlenose dolphin. |
| params.gain | 3.16 | g | True | marine-mammals.jsonl:Madsen 1976 | 0.5 log units more sensitive than a person means 10^0.5, about 3.16 times, which is used as the brightness gain. |
| params.sheen | 0.6 | i | True |  |  |

## Warnings
- added the row 'Settings the app chose', which names 1 invented parameters the reply left unnamed
- params.cpd: the floor run found this parameter invisible near 3.35

## Records dropped before sending
- table lines: 4035
