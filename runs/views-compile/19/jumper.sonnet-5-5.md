# Draft spec for jumper (claude-sonnet-5-5)

Compiled from 400 records. Not offered; a person judges it on a phone through `?try=jumper`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| gaze.ior | 5000 | i | True |  |  |
| gaze.iorDeg | 5 | i | True |  |  |
| gaze.saccade | [0,6.7] | g | True | jumper.jsonl:Land 1969 | A 15 degree saccade complete within 0.1 s gives 100/15 which is about 6.7 ms per degree, with no base time. |
| gaze.sweep | [2,1.2] | i | True |  |  |
| gaze.twist | [25,2000,3500] | i | True |  |  |
| params.M | "SIDE" | g | True | jumper.jsonl:Yamashita 1976 | The matrix is built from the 535 nm single peak of the lateral eyes by the app's own mapping to screen colours. |
| params.cpd | 0.8 | i | True |  |  |
| params.fov | 330 | m | False | spider-day.jsonl:Shepeleva 2021 | The record states about 330 degrees for the three pairs of secondary eyes together. |
| params.gate | 1 | i | True |  |  |
| params.glow | 0.8 | i | True |  |  |
| params.sat | 0 | g | True | jumper.jsonl:Yamashita 1976 | The lateral eyes have one receptor class, and one class carries no colour contrast, so saturation is set to 0. |
| zones[0].M | "PRINCIPAL" | g | True | jumper.jsonl:Blest 1981, jumper.jsonl:Zurek 2015 | The matrix uses the 360 nm ultraviolet peak and the 530 nm green peak by the app's own mapping to screen colours. |
| zones[0].cpd | 3.8 | m | False | jumper.jsonl:Harland 2012 | The record gives 3.8 cycles per degree for Phidippus principal eyes, from a 0.13 degree visual angle. |
| zones[0].deg | [2,21] | m | False | jumper.jsonl:Land 1969 | The retina subtends about 2 degrees by 21 degrees in object space, so the zone is 2 wide and 21 tall. |
| zones[0].sat | 0.7 | i | True |  |  |
| zones[0].uv | 0.7 | i | True |  |  |

## Warnings
- params.cpd: the floor run found this parameter invisible near 0.75

## Records dropped before sending
- log lines: 282
- table lines: 4962
