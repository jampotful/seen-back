# Draft spec for jumper (claude-sonnet-5-5)

Compiled from 300 records. Not offered; a person judges it on a phone through `?try=jumper`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| gaze.ior | 5000 | i | True |  |  |
| gaze.sweep | [2,1.2] | i | True |  |  |
| matrices.JUMPER | null | g | True | jumper.jsonl:DeVoe 1975, jumper.jsonl:Zurek 2015 | The pigment peaks 370 nm and 530 nm match R39 (UV cells at 370 nm) and R38 (green at 530 nm). |
| params.cpd | 1.3 | m | True | spider-day.jsonl:Shepeleva 2021 | The record gives 1.3 cycles per degree for the antero-lateral eyes of Evarcha blancardi. |
| params.fov | 330 | m | False | spider-day.jsonl:Shepeleva 2021 | The record gives about 330 degrees horizontally for the three pairs of secondary eyes of Trite planiceps. |
| params.gate | 1 | i | True |  |  |
| zones[0].at | [0.5,0.5] | i | True |  |  |
| zones[0].cpd | 3.8 | g | True | jumper.jsonl:Harland 2012 | A receptor angle of 0.13 degrees gives 1 / (2 x 0.13) = 3.8 cycles per degree. |
| zones[0].deg | [2,21] | m | False | jumper.jsonl:Land 1969 | The records give the retina's subtense as about 21 degrees high by 2 degrees wide, written as [2, 21]. |

## Warnings
- params.cpd: the floor run found this parameter invisible near 0.75

## Records dropped before sending
- log lines: 282
- table lines: 4962
