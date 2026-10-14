# Draft spec for jumper (claude-sonnet-5-5)

Compiled from 400 records. Not offered; a person judges it on a phone through `?try=jumper`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| gaze.ior | 5000 | g | True | jumper.jsonl:Ferrante 2024, spider-day.jsonl:Ferrante 2024 | The records give about 5 seconds of reduced detection at the inspected place, and 5 x 1000 = 5000 milliseconds. |
| gaze.iorDeg | 5 | i | True |  |  |
| gaze.sweep | [2,1.5] | g | True | jumper.jsonl:Land 1969, spider-day.jsonl:Land 1969 | The 2 degrees is the minimum scan width in R134 and 1.5 seconds is the middle of the 1 to 2 second period in R129. |
| gaze.twist | [25,2000,3500] | g | True | jumper.jsonl:Land 1969 | 25 degrees is the middle of 20 to 30 degrees, 2000 ms is the 2 second turn, and 3500 ms is the middle of the 2 to 5 second hold, all from R142. |
| params.M | "SALTICID" | i | True |  |  |
| params.cpd | 0.8 | i | True |  |  |
| params.fov | 360 | g | False | jumper.jsonl:Harland 2012, spider-day.jsonl:Lauren 2018 | Both records give the combined field of the eyes as close to 360 degrees. |
| params.gate | 1 | i | True |  |  |
| params.sat | 0 | i | True |  |  |
| params.uvBlue | 1 | i | True |  |  |
| zones[0].at | [0,0] | i | True |  |  |
| zones[0].cpd | 3.8 | g | True | jumper.jsonl:Harland 2012 | A typical species has receptors 0.13 degrees apart, so acuity is 1 / (2 x 0.13) = 3.8 cycles per degree. |
| zones[0].deg | [5,20] | m | False | spider-day.jsonl:Shepeleva 2021 | The record gives the principal-eye field as 5.0 degrees horizontally and 20 degrees vertically. |
| zones[0].sat | 1 | i | True |  |  |

## Warnings
- params.cpd: the floor run found this parameter invisible near 0.75

## Records dropped before sending
- log lines: 282
- table lines: 4962
