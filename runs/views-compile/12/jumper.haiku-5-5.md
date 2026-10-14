# Draft spec for jumper (claude-haiku-5-5)

Compiled from 400 records. Not offered; a person judges it on a phone through `?try=jumper`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| matrices.JUMP | [[0,0.3,0.7],[0,0.3,0.7],[0.5,0.5,0]] | i | True | jumper.jsonl:Blest 1981, jumper.jsonl:DeVoe 1975, jumper.jsonl:Glenszczyk 2021, jumper.jsonl:Yamashita 1976, jumper.jsonl:Zurek 2015 |  |
| params.cpd | 12.4 | m | False | jumper.jsonl:Williams 1980, spider-day.jsonl:Shepeleva 2021 | The app's sharpness of 12.4 cycles per degree equals the principal eye acuity Williams 1980 gives for Portia fimbriata. |
| params.fall | 2.6 | i | True |  |  |
| params.fov | 300 | g | False | spider-day.jsonl:E 2023, spider-day.jsonl:Rößler 2021 | The whole-animal field of 300 degrees lies between the near 300 degree figure for the six smaller eyes and the almost 360 degree figure for the three other pairs. |
| params.fovea | 2.2 | i | True |  |  |
| params.gate | 0.8 | i | True |  | Metaphidippus harfordi side eyes ignored stationary targets, which the value describes as near-total fading of still things. |
| params.glow | 0.6 | i | True |  |  |
| params.glowC | [0.78,1,0.62] | i | True |  |  |
| params.noGreen | 0 | i | True |  |  |
| params.persist | 0.1 | i | True |  |  |
| params.sat | 0.9 | i | True |  |  |
| params.topoA | 1 | i | True |  |  |
| params.uvBlue | 1 | i | True |  |  |

## Warnings
- added the row 'Settings the app chose', which names 2 invented parameters the reply left unnamed
- params.cpd: the floor run found this parameter invisible near 3.35
- params.fov: 300 differs from the nearest view's 300 by less than the floor 8.09, so nobody will see the change

## Records dropped before sending
- log lines: 282
- table lines: 4962
