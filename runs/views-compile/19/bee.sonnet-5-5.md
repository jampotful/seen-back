# Draft spec for bee (claude-sonnet-5-5)

Compiled from 400 records. Not offered; a person judges it on a phone through `?try=bee`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| params.M | "BEE" | g | True | bee.jsonl:Land 2012 | The matrix is built from the three honeybee peaks 344, 436 and 556 nm, and the camera channel mapping is the app's own. |
| params.cpd | 0.26 | m | False | bee.jsonl:Land 1997 | The honeybee grating limit in R1 is 0.26 cycles per degree and the parameter equals it. |
| params.fov | 312 | g | True | bee.jsonl:Taylor 2019 | Each eye reaches 156 degrees back from straight ahead, so 2 x 156 = 312 degrees at the horizon. |
| params.rate | 0.3 | g | True | bee.jsonl:Srinivasan 1984 | A person's flicker fusion of 60 Hz divided by the honeybee's 200 Hz gives 0.3. |
| params.uvBlue | 0.7 | i | True |  |  |
| remap.blindAt | 180 | g | True | bee.jsonl:Taylor 2019 | Each eye reaches 156 degrees back, so the gap between them is centred straight behind at 180 degrees. |
| remap.blindDeg | 48 | g | True | bee.jsonl:Taylor 2019 | 360 - 2 x 156 = 48 degrees of blind wedge. |
| remap.blindSoft | 8 | i | True |  |  |

## Warnings
- params.fov: 312 differs from the nearest view's 320 by less than the floor 10.2, so nobody will see the change
- params.cpd: the floor run found this parameter invisible near 0.75

## Records dropped before sending
- dropped: retracted by the audit: 1
- log lines: 267
- table lines: 8820
