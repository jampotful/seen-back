# Draft spec for bee (claude-sonnet-5-5)

Compiled from 400 records. Not offered; a person judges it on a phone through `?try=bee`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| matrices.BEE | [[0.22664,0.50311,0.19444,0.07581],[0.00084,0.1108... | g | True | bees-wasps.jsonl:Nouvian 2020, bees-wasps.jsonl:Z 2020, insects-met.jsonl:Randolf Menzel 1988 | from_pigments lists 344, 436 and 540 nm, each equal to a cited peak. |
| params.M | "BEE" | g | True | bees-wasps.jsonl:Nouvian 2020, bees-wasps.jsonl:Z 2020, insects-met.jsonl:Randolf Menzel 1988 | A three-class matrix built from peaks 344 nm (honeybee UV, R43), 436 nm (mason bee blue, R46) and 540 nm (bumblebee green, R31). |
| params.cpd | 0.35 | g | False | insects-met.jsonl:Todd Macuda 2001 | Bombus impatiens resolved gratings at 0.35 cycles per degree, used here for every bee. |
| params.fall | 1 | i | True |  |  |
| params.fov | 285 | g | True | bees-wasps.jsonl:M 2017, bees-wasps.jsonl:Paffhausen 2021 | The middle of 300 degrees for bees and 270 degrees for the honeybee is 285. |
| params.pupil | "none" | i | True |  |  |
| params.rate | 0.46 | g | True | bees-wasps.jsonl:Ibarra 2014, bees-wasps.jsonl:Meyer‐Rochow 1981, intake-6.jsonl:Inger 2014 | 60 Hz divided by about 130 Hz (bumblebee, between honeybee figures of 100 and 200 Hz) gives 0.46. |
| params.topoA | 1 | i | True |  |  |
| params.uvBlue | 0.7 | i | True |  |  |

## Warnings
- params.cpd: the floor run found this parameter invisible near 0.75

## Records dropped before sending
- dropped: retracted by the audit: 15
- log lines: 1081
- table lines: 8820
