# Draft spec for bird (claude-sonnet-5-5)

Compiled from 400 records. Not offered; a person judges it on a phone through `?try=bird`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| matrices.PASSERINE | [[0.33891,0.45753,0.13066,0.07291],[0.04908,0.3641... | g | True | birds-met.jsonl:Hart 2001 | Peaks 369, 449, 503 and 563 are rounded means over four songbird families and each lies within 2 nm of a cited record (R63, R82, R90, R96). |
| params.M | "PASSERINE" | g | True | birds-met.jsonl:Hart 2001 | Means over starling, blackbird, blue tit and canary: ultraviolet (362+373+371+369)/4=368.75, short (449+454+448+444)/4=448.75, middle (504+504+503+500)/4=502.75, long (563+557+563+571)/4=563.5, rounded to 369, 449, 503, 563. |
| params.cpd | 8 | g | True | sweep-19.jsonl:Jarvis 2009, sweep-6.jsonl:Moore 2015 | 8 cycles a degree lies between 7.0 for domestic chickens (R3) and 8.35 for the eastern towhee (R5). |
| params.fall | 1.0 | i | True |  |  |
| params.fov | 300 | g | False | birds-other.jsonl:Eckmeier 2013 | The record states the zebra finch field covers about 300 degrees of azimuth. |
| params.rate | 0.45 | g | True | birds-other.jsonl:Boström 2016 | Mean flicker limit (130.3+128.1+138.2)/3=132.2 hertz; 60/132.2=0.454, rounded to 0.45. |
| params.topoA | 1 | i | True |  |  |
| params.uvBlue | 0.5 | i | True |  |  |

## Warnings
- added the row 'Settings the app chose', which names 1 invented parameters the reply left unnamed
- params.cpd: the floor run found this parameter invisible near 3.35

## Records dropped before sending
- dropped: retracted by the audit: 15
- log lines: 1081
- table lines: 3726
