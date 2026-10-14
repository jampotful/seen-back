# Draft spec for bee (claude-sonnet-5-5)

Compiled from 400 records. Not offered; a person judges it on a phone through `?try=bee`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| params.M | "BEE" | m | True | bee.jsonl:van der Kooi 2021 | The matrix peaks 346, 430 and 540 nm are the UV, blue and green values these records state for the worker honeybee. |
| params.cpd | 0.26 | m | False | bee.jsonl:Land 1997 | The honeybee grating limit of 0.26 cycles per degree is used as stated. |
| params.fov | 312 | g | False | bee.jsonl:Taylor 2019 | The record gives 312 degrees for the two eyes together at the horizon. |
| params.rate | 0.3 | g | True | bee.jsonl:Srinivasan 1984 | 60 hertz for a person divided by the bee's 200 hertz gives 0.3. |
| params.uvBlue | 0.7 | i | True |  |  |
| remap.blindAt | 180 | g | True | bee.jsonl:Taylor 2019 | The two eyes each end 156 degrees from straight ahead, so the gap between them is centred at 180 degrees. |
| remap.blindDeg | 48 | g | True | bee.jsonl:Taylor 2019 | Each eye reaches 156 degrees back, so the fields total 312 and 360 minus 312 leaves a wedge of 48 degrees. |

## Warnings
- params.fov: 312 differs from the nearest view's 320 by less than the floor 10.2, so nobody will see the change
- params.cpd: the floor run found this parameter invisible near 0.75

## Records dropped before sending
- dropped: retracted by the audit: 1
- log lines: 267
- table lines: 8820
