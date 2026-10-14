# Draft spec for bee (claude-sonnet-5-5)

Compiled from 400 records. Not offered; a person judges it on a phone through `?try=bee`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| matrices.BEE | [[0.22664,0.50311,0.19444,0.07581],[0.00084,0.1108... | g | True | bee.jsonl:Land 2012, bee.jsonl:van der Kooi 2021 | The matrix takes its three peaks from the cited records: 344 nm (R55), 436 nm (R84) and 540 nm (R85), mapped by the app to camera colours. |
| params.M | "BEE" | g | True | bee.jsonl:Land 2012, bee.jsonl:van der Kooi 2021 | The matrix is built from the measured peaks 344 nm (R55), 436 nm (R84) and 540 nm (R85); the mapping from camera colours is the app's. |
| params.cpd | 0.26 | m | False | bee.jsonl:Land 1997 | The record gives 0.26 cycles per degree as the highest frequency honeybees reliably resolved. |
| params.fov | 312 | g | True | bee.jsonl:Taylor 2019 | Each eye reaches back 156 degrees from straight ahead, so 2 x 156 = 312 degrees. |
| params.rate | 0.3 | g | True | bee.jsonl:Srinivasan 1984 | A person's 60 hertz divided by the bee's 200 hertz flicker limit gives 0.3. |
| params.uvBlue | 0.8 | i | True |  |  |
| remap.blindAt | 180 | g | True | bee.jsonl:Taylor 2019 | Both eyes stop 156 degrees back from straight ahead, so the blank wedge is centred straight behind at 180 degrees. |
| remap.blindDeg | 48 | g | True | bee.jsonl:Taylor 2019 | 360 - 2 x 156 = 48 degrees of blank wedge behind the bee. |
| remap.blindSoft | 6 | i | True |  |  |

## Warnings
- params.fov: 312 differs from the nearest view's 320 by less than the floor 10.2, so nobody will see the change
- params.cpd: the floor run found this parameter invisible near 0.75

## Records dropped before sending
- dropped: retracted by the audit: 1
- log lines: 267
- table lines: 8820
