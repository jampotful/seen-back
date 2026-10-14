# Draft spec for rabbit (sonnet-5-5)

Compiled from 177 records. Not offered; a person judges it on a phone through `?try=rabbit`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| matrices.rabbit_cones | [[0.09158,0.47995,0.34372,0.08476],[0.09158,0.4799... | g | True | rodents-lagomorphs.jsonl:Caldwell 1978, rodents-lagomorphs.jsonl:Radlwimmer 1998 | from_pigments lists 465 nm from R5 and 509 nm from R6. |
| matrices.rabbit_rod | [[0.06366,0.44901,0.39846,0.08886],[0.06366,0.4490... | g | True | rodents-lagomorphs.jsonl:Ribelayga 2010 | from_pigments lists the rod-driven peak near 500 nm from R9. |
| params.M | "rabbit_cones" | g | True | rodents-lagomorphs.jsonl:Caldwell 1978, rodents-lagomorphs.jsonl:Radlwimmer 1998 | The matrix is built from the two cone peaks 465 nm (R5) and 509 nm (R6). |
| params.cpd | 2.1 | g | True | rodents-lagomorphs.jsonl:Grzywacz 1994, rodents-lagomorphs.jsonl:Wyk 2006 | Ganglion cell spacing of 35 micrometers (middle of 30-40) at 1.9 micrometers per 46 arcseconds is 35/1.9 x 46 = 847 arcseconds = 14.1 arcminutes; 30 / 14.1 = 2.1 cycles per degree. |
| params.fall | 2 | i | True |  |  |
| params.fov | 360 | g | True | rodents-lagomorphs.jsonl:Hughes 1982, rodents-lagomorphs.jsonl:Wong 2008 | The whole field of both eyes with the overlap counted once is given as 360 degrees in the freeze position (R1) and as nearly 360 (R2); no arithmetic beyond taking that total, which is also the engine's maximum. |
| params.glow | 0.6 | i | True |  |  |
| params.topoS | 1 | i | True |  |  |
| spectrum.adaptAt | [-3,-1] | i | True |  |  |

## Warnings
- added the row 'Settings the app chose', which names 2 invented parameters the reply left unnamed
- params.cpd: the floor run found this parameter invisible near 2.05
- checked offline by compile.py check

## Records dropped before sending
- dropped: retracted by the audit: 15
- log lines: 1081
- table lines: 2949
