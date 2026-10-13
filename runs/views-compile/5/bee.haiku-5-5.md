# Draft spec for bee (claude-haiku-5-5)

Compiled from 300 records. Not offered; a person judges it on a phone through `?try=bee`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| matrices.BEE | "app convention following R175" | i | True |  |  |
| params.cpd | 0.26 | m | False | bee.jsonl:Land 1997 | The honeybee worker behavioural limit is 0.26 cycles per degree. |
| params.fov | 300 | g | False | bees-wasps.jsonl:Paffhausen 2021 | Bees are given a field of view of about 300 degrees horizontally. |
| params.fovea | 1 | i | True |  |  |
| params.glow | 0.9 | i | True |  |  |
| params.glowC | [0.78,1,0.62] | i | True |  |  |
| params.rate | 2 | g | True | bee.jsonl:Srinivasan 1984 | Honeybee flicker fusion of about 200 Hz against a person's near 60 Hz gives roughly a double rate; graded g because the person figure is not in the records. |
| params.sat | 1 | i | True |  |  |
| params.topoS | 0.6 | i | True |  |  |

## Warnings
- added the row 'Settings the app chose', which names 3 invented parameters the reply left unnamed
- params.cpd: the floor run found this parameter invisible near 0.75

## Records dropped before sending
- dropped: retracted by the audit: 1
- log lines: 267
- table lines: 8820
