# Draft spec for jumper (claude-sonnet-5-5)

Compiled from 400 records. Not offered; a person judges it on a phone through `?try=jumper`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| gaze.ior | 5000 | i | True |  |  |
| gaze.saccade | [0,6.7] | g | True | jumper.jsonl:Land 1969 | 0.1 s divided by 15 degrees is about 6.7 ms a degree, with a base of 0, an upper bound. |
| gaze.sweep | [2,1.5] | i | True |  |  |
| gaze.twist | [25,2000,3500] | i | True |  |  |
| matrices.FRONT | [[0.1783,0.50901,0.23464,0.07804],[0.1783,0.50901,... | g | True | jumper.jsonl:Blest 1981, jumper.jsonl:Zurek 2015 | The peaks are 360 nm as in R73 and 530 nm as in R54. |
| matrices.SIDE | [[0.20215,0.50744,0.21355,0.07686],[0.20215,0.5074... | g | True | jumper.jsonl:Yamashita 1976, spider-day.jsonl:Varma 2019 | The one pigment peak of 535 nm lies in the 535 to 540 nm range of R53 and equals the 535 nm of R78. |
| params.M | "SIDE" | g | True | jumper.jsonl:Yamashita 1976, spider-day.jsonl:Varma 2019 | The name points to a matrix built from the single 535 nm peak that the records give for the side eyes, so the mapping is the app's and the grade is at most g. |
| params.cpd | 1.3 | m | False | spider-day.jsonl:Shepeleva 2021 | The record gives 1.3 cycles a degree for the antero-lateral eyes of Evarcha blancardi, the best side eye figure. |
| params.fov | 360 | m | False | jumper.jsonl:Land 1969 | The record says the side eyes between them cover almost the entire 360 degrees around the animal. |
| params.gate | 0.85 | i | True |  |  |
| params.living | 1.5 | i | True |  |  |
| zones[0].cpd | 3.8 | m | False | jumper.jsonl:Harland 2012 | R2 gives 3.8 cycles a degree for the principal eye of Phidippus johnsoni, from an inter-receptor angle of 0.13 degrees. |
| zones[0].deg | [2,21] | m | False | jumper.jsonl:Land 1969 | R14 gives 2 degrees across and R45 gives 21 degrees tall for one principal retina. |
| zones[0].uv | [0.8,0] | i | True |  |  |

## Warnings
- params.cpd: the floor run found this parameter invisible near 0.75

## Records dropped before sending
- log lines: 282
- table lines: 4962
