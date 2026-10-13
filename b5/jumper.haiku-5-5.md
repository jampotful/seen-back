# Draft spec for jumper (claude-haiku-5-5)

Compiled from 400 records. Not offered; a person judges it on a phone through `?try=jumper`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| matrices.UVG | [[0.2,0.1,0.3],[0.0,0.9,0.1],[0.1,0.9,0.0]] | i | True |  |  |
| params.cpd | 12.4 | m | False | jumper.jsonl:Williams 1980 | The view's sharpness is the measured 12.4 cycles per degree of Portia fimbriata's principal eyes. |
| params.fall | 2.6 | i | True |  |  |
| params.fov | 300 | g | False | spider-day.jsonl:Lauren 2018, spider-day.jsonl:Rößler 2021 | Whole-animal field set between the near 300 degrees of the six secondary eyes and the 360 degrees for all four pairs. |
| params.fovea | 2.2 | i | True |  |  |
| params.gain | 1.6 | i | True |  |  |
| params.gate | 0.6 | i | True |  |  |
| params.persist | 0.15 | i | True |  |  |
| params.rate | 0.3 | g | True | jumper.jsonl:Tan 2023, spider-day.jsonl:Tan 2023 | Flicker up to 40 Hz against a 60 Hz screen gives a rate well below a person's; graded g because it is a family figure. |
| params.sat | 0.9 | i | True |  |  |
| zones[0].cpd | 12.4 | m | False | jumper.jsonl:Williams 1980 | The sharp strip uses the same measured 12.4 cycles per degree. |
| zones[0].mag | 2 | i | True |  |  |

## Warnings
- added the row 'Settings the app chose', which names 3 invented parameters the reply left unnamed
- params.fov: 300 differs from the nearest view's 300 by less than the floor 8.09, so nobody will see the change
- params.cpd: the floor run found this parameter invisible near 3.35

## Records dropped before sending
- log lines: 282
- table lines: 4962
