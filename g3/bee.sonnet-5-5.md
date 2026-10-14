# Draft spec for bee (claude-sonnet-5-5)

Compiled from 400 records. Not offered; a person judges it on a phone through `?try=bee`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| matrices.BEE | [[0.3057,0.47473,0.14613,0.07344],[0.00084,0.11082... | g | True | bee.jsonl:Land 2012 | The matrix is built from the three honeybee receptor peaks 344, 436 and 556 nm, and the mapping to phone colours is the app's. |
| params.M | "BEE" | g | True | bee.jsonl:Land 2012 | The matrix is built from the three honeybee receptor peaks 344, 436 and 556 nm, and the mapping to phone colours is the app's. |
| params.cpd | 0.26 | m | False | bee.jsonl:Land 1997 | The parameter equals the honeybee grating acuity of 0.26 cycles per degree in R1. |
| params.fov | 312 | g | True | bee.jsonl:Taylor 2019 | Each eye reaches 156 degrees back from straight ahead, so the two together cover 2 x 156 = 312 degrees at the horizon. |
| params.rate | 0.3 | g | True | bee.jsonl:Srinivasan 1984 | A person's 60 Hz flicker fusion divided by the honeybee's 200 Hz gives 60 / 200 = 0.3. |
| params.uvBlue | 0.8 | i | True |  |  |
| remap.blindAt | 180 | g | True | bee.jsonl:Taylor 2019 | Both eyes reach back 156 degrees from straight ahead, so the uncovered wedge is centred on 180 degrees. |
| remap.blindDeg | 48 | g | True | bee.jsonl:Taylor 2019 | The eyes cover 2 x 156 = 312 degrees, which leaves 360 - 312 = 48 degrees behind. |
| remap.blindSoft | 6 | i | True |  |  |

## Warnings
- params.fov: 312 differs from the nearest view's 320 by less than the floor 10.2, so nobody will see the change
- params.cpd: the floor run found this parameter invisible near 0.75

## Records dropped before sending
- dropped: retracted by the audit: 1
- log lines: 267
- table lines: 8820
