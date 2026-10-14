# Draft spec for bee (claude-haiku-5-5)

Compiled from 400 records. Not offered; a person judges it on a phone through `?try=bee`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| params.cpd | 0.26 | m | False | bee.jsonl:Land 1997 | The record states the highest resolved spatial frequency as 0.26 cycles a degree, and this value equals it. |
| params.dof | 0.5 | i | True |  |  |
| params.fall | 1.5 | i | True |  |  |
| params.fov | 312 | g | True | bee.jsonl:Taylor 2019 | Each eye reaches 156 degrees back from straight ahead, so the two together cover 2 x 156 = 312 degrees at the horizon; worked out from one record, so at most g and invented. |
| params.fovea | 1.2 | i | True |  |  |
| params.gain | 1.4 | i | True |  |  |
| params.glow | 0.9 | i | True |  |  |
| params.glowC | [0.78,1,0.62] | i | True |  |  |
| params.living | 0 | i | True |  |  |
| params.persist | 0.1 | i | True |  |  |
| params.rate | 0.3 | g | True | bee.jsonl:Srinivasan 1984, bees-wasps.jsonl:Ibarra 2014 | A person's flicker fusion of 60 hertz divided by the bee's 200 hertz in bright light (R135) gives 0.3; R138 gives 100 hertz for free-flying bees. Worked out, so at most g and invented. |
| params.sat | 0.8 | i | True |  |  |
| params.topoA | 0.3 | i | True |  |  |
| params.uvBlue | 0.8 | i | True |  |  |
| spectrum.neutral | 1 | i | True |  |  |
| zones[0].cpd | 0.5 | m | False | bees-wasps.jsonl:YS 2014 | The lateral ocellus resolves 2 degree gratings, which is 1/2 = 0.5 cycles a degree; the record states the 2 degree pattern as clearly resolved. |
| zones[0].deg | [20,20] | i | True |  |  |

## Warnings
- added the row 'Settings the app chose', which names 4 invented parameters the reply left unnamed
- params.fov: 312 differs from the nearest view's 320 by less than the floor 10.2, so nobody will see the change
- params.cpd: the floor run found this parameter invisible near 0.75

## Records dropped before sending
- dropped: retracted by the audit: 1
- log lines: 267
- table lines: 8820
