# Draft spec for jumper (claude-sonnet-5-5)

Compiled from 400 records. Not offered; a person judges it on a phone through `?try=jumper`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| gaze.ior | 5000 | i | True |  |  |
| gaze.iorDeg | 5 | i | True |  |  |
| gaze.sweep | [2,1.2] | i | True |  |  |
| gaze.twist | [25,2000,3500] | i | True |  |  |
| params.M | "SIDE" | g | True | jumper.jsonl:Yamashita 1976 | No arithmetic: the matrix SIDE is built from the single 535 nm peak of the lateral eyes (lower end of the 535 to 540 nm record), and R83 states these eyes have one receptor class. |
| params.cpd | 1.3 | m | False | spider-day.jsonl:Shepeleva 2021 | The record gives 1.3 cycles per degree for the antero-lateral eyes of Evarcha blancardi. |
| params.fov | 330 | m | False | spider-day.jsonl:Shepeleva 2021 | The record states about 330 degrees horizontally for the three pairs of secondary eyes of a jumping spider. |
| params.gate | 1 | i | True |  |  |
| params.living | 1 | i | True |  |  |
| zones[0].cpd | 3.8 | m | False | jumper.jsonl:Harland 2012 | The record gives 3.8 cycles per degree for the principal eyes of Phidippus johnsoni, from an inter-receptor angle of about 0.13 degrees. |
| zones[0].deg | [2,21] | m | False | jumper.jsonl:Land 1969 | R14 gives the retina's field as 2 degrees wide and R45 gives 21 degrees high, from the same statement of about 21 by 2 degrees. |
| zones[0].uv | [1,0] | i | True |  |  |

## Warnings
- params.cpd: the floor run found this parameter invisible near 0.75

## Records dropped before sending
- log lines: 282
- table lines: 4962
