# Draft spec for jumper (claude-sonnet-5-5)

Compiled from 400 records. Not offered; a person judges it on a phone through `?try=jumper`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| gaze.examine | [20000,40000] | i | True |  |  |
| gaze.ior | 5000 | g | True | spider-day.jsonl:Ferrante 2024 | R243 gives about 5 seconds of reduced detection at the inspected place, and 5 s x 1000 = 5000 ms. |
| gaze.iorDeg | 5 | i | True |  |  |
| gaze.saccade | [0,6.7] | g | True | jumper.jsonl:Land 1969 | A 15 degree saccade finishes within 0.1 s, so 100 ms / 15 degrees = 6.7 ms per degree, with the base set to 0 by the app. |
| gaze.sweep | [2,1.5] | i | True |  |  |
| gaze.twist | [25,2000,3500] | i | True |  |  |
| params.M | "SIDE" | g | True | jumper.jsonl:Yamashita 1976 | The side eyes have one green class peaking at 535 nm (the low end of 535-540), so a one-peak matrix at 535 nm is built from that record with the camera mapping chosen by the app. |
| params.cpd | 1.3 | m | True | spider-day.jsonl:Shepeleva 2021 | R8 gives 1.3 cycles a degree for the antero-lateral eye of Evarcha blancardi, the sharpest side eye measured. |
| params.fov | 360 | g | False | jumper.jsonl:Harland 2012, spider-day.jsonl:Lauren 2018 | Both records state a field of 360 degrees, or close to it, for the eyes combined. |
| params.gate | 1 | g | True | jumper.jsonl:Land 1971 | The record says the side eyes act as completely blind to stationary objects, which the app maps to a gate of 1. |
| params.glow | 0.8 | i | True |  |  |
| params.living | 1 | i | True |  |  |
| params.sat | 0 | g | True | jumper.jsonl:Goté 2019, jumper.jsonl:Yamashita 1976 | A single receptor type (one class) is mapped to a saturation of 0, a mapping the app chose. |
| params.uvBlue | 0.8 | i | True |  |  |
| zones[0].M | "FRONT" | g | True | jumper.jsonl:Blest 1981, jumper.jsonl:Zurek 2015 | The matrix takes a UV peak of 360 nm (R73) and a green peak of 530 nm (R54) and the camera mapping is the app's. |
| zones[0].cpd | 3.8 | m | False | jumper.jsonl:Harland 2012 | The record gives 3.8 cycles a degree for Phidippus johnsoni, from an inter-receptor angle of 0.13 degrees. |
| zones[0].deg | [2,21] | m | False | jumper.jsonl:Land 1969 | The records give the retinal field as about 21 by 2 degrees, written here as width 2 and height 21. |
| zones[0].sat | 0.7 | i | True |  |  |

## Warnings
- added the row 'Settings the app chose', which names 3 invented parameters the reply left unnamed
- params.cpd: the floor run found this parameter invisible near 0.75

## Records dropped before sending
- log lines: 282
- table lines: 4962
