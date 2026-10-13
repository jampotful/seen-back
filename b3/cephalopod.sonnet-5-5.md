# Draft spec for cephalopod (claude-sonnet-5-5)

Compiled from 400 records. Not offered; a person judges it on a phone through `?try=cephalopod`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| by.family.Sepiidae.params.rate | 0.5 | g | True | cephalopods.jsonl:Taniguchi 2015 | 30 Hz from R84 divided by an assumed person's pace of 60 Hz is 0.5. |
| matrices.single_pigment | [[0.03083,0.37707,0.49324,0.09886],[0.03083,0.3770... | g | True | cephalopods.jsonl:Chung 2016 | The matrix is built from one pigment peak at 485 nm, which equals the peak in R46 and R47, and the weighting into a colour matrix is the app's own. |
| params.M | "single_pigment" | g | True | cephalopods.jsonl:Chung 2016 | A single pigment peaking at 485 nm, the peak given for Hapalochlaena maculosa in R46 and Octopus australis in R47, is turned into a one-channel colour matrix. |
| params.cpd | 8 | g | True | cephalopods.jsonl:Taniguchi 2015, cephalopods.jsonl:Turnbull 2014 | The value 8 equals the cuttlefish figure in R14 and lies between the squid figure in R6 and the octopus figure in R7. |
| params.fov | 312 | m | True | cephalopods.jsonl:Sugimoto 2026 | The value 312 degrees is the visual field of 14 day old oval squid in R25. |
| params.rate | 0.85 | g | True | cephalopods.jsonl:GJP 2026 | 50.8 Hz from R82 divided by an assumed person's pace of 60 Hz is about 0.85. |
| params.topoA | 0.7 | i | True |  |  |

## Warnings
- params.cpd: the floor run found this parameter invisible near 3.35

## Records dropped before sending
- table lines: 1562
