# Draft spec for jumper (claude-sonnet-5-5)

Compiled from 300 records. Not offered; a person judges it on a phone through `?try=jumper`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| gaze.sweep | [2,1.5] | i | True |  |  |
| matrices.SALTICID | null | m | True | jumper.jsonl:DeVoe 1975, jumper.jsonl:Zurek 2015 | Peaks of 370 nm (UV cells in Phidippus regius) and 530 nm (green class in Habronattus pyrrithrix) are taken directly from the two records. |
| params.cpd | 1.3 | m | True | spider-day.jsonl:Shepeleva 2021 | The record gives 1.3 cycles per degree for the antero-lateral eyes of Evarcha blancardi, used here for the whole wide picture. |
| params.fov | 360 | g | False | spider-day.jsonl:Lauren 2018 | The record states a 360 degree field of view for the four pairs of eyes combined. |
| params.gate | 1 | i | True |  |  |
| params.sat | 0 | i | True |  |  |
| zones[0].cpd | 3.8 | g | True | jumper.jsonl:Harland 2012 | Visual angle of 0.13 degrees gives 1/(2 x 0.13) = 3.85, which the record gives as 3.8 cycles per degree. |
| zones[0].deg | 5 | g | False | jumper.jsonl:De Agrò 2024 | The record gives a visual field of around 5 degrees for each principal eye. |
| zones[0].sat | 1 | i | True |  |  |

## Warnings
- params.cpd: the floor run found this parameter invisible near 0.75

## Records dropped before sending
- log lines: 282
- table lines: 4962
