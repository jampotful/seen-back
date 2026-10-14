# Draft spec for bee (claude-sonnet-5-5)

Compiled from 400 records. Not offered; a person judges it on a phone through `?try=bee`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| params.M | "BEE" | i | True |  |  |
| params.cpd | 0.26 | m | False | bee.jsonl:Land 1997 | The record states the highest spatial frequency reliably resolved by honeybees as 0.26 cycle per degree. |
| params.fov | 312 | g | True | bee.jsonl:Taylor 2019 | Each eye reaches 156 degrees back from straight ahead at the horizon, so 2 x 156 = 312 degrees. |
| params.rate | 0.3 | g | True | bee.jsonl:Srinivasan 1984 | A person's flicker fusion of 60 Hz divided by the honeybee's 200 Hz gives 0.3. |
| params.uvBlue | 0.7 | i | True |  |  |
| remap.blindAt | 180 | i | True |  |  |
| remap.blindDeg | 48 | g | True | bee.jsonl:Taylor 2019 | 360 degrees minus the two fields of 156 degrees each (312 degrees) leaves a blind wedge of 48 degrees. |
| remap.blindSoft | 8 | i | True |  |  |

## Warnings
- params.fov: 312 differs from the nearest view's 320 by less than the floor 10.2, so nobody will see the change
- params.cpd: the floor run found this parameter invisible near 0.75

## Records dropped before sending
- dropped: retracted by the audit: 1
- log lines: 267
- table lines: 8820
