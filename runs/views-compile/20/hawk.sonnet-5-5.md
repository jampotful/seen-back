# Draft spec for hawk (claude-sonnet-5-5)

Compiled from 289 records. Not offered; a person judges it on a phone through `?try=hawk`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| gaze.examine | [2000,5000] | g | True | birds-raptors-owls.jsonl:Tucker 2000 | Lower bound 2000 ms from the 2 s head-movement interval of hawks and falcons, upper bound 5000 ms from the 5 s interval of bald eagles. |
| params.cpd | 40 | g | True | birds-raptors-owls.jsonl:Potier 2018, intake-2.jsonl:Potier 2020 | A Harris's hawk reached 62.3 cycles per degree and ranged 27.4 to 60; the engine accepts at most 40, so 40 is chosen inside that range. |
| params.fall | 1 | i | True |  |  |
| params.fov | 280 | g | True | birds-raptors-owls.jsonl:Martin 1999, birds-raptors-owls.jsonl:O'Rourke 2010, sweep-5.jsonl:O'Rourke 2010 | Middle of 300 degrees (Cooper's hawk, 360 minus a 60 degree blind area) and 260 degrees (short-toed eagle), which is close to 360 - 82 = 278 for a red-tailed hawk. |
| params.rate | 0.77 | g | True | intake-2.jsonl:Potier 2020 | 60 Hz divided by a Harris's hawk's flicker fusion of 77.7 Hz is 0.772, rounded to 0.77. |
| params.sat | 1 | g | True | birds-raptors-owls.jsonl:Mitkus 2017, birds-raptors-owls.jsonl:NA 2022 | Four spectral types of single cone against a human's three, so color is not muted and the value is 1. |
| params.topoA | 1 | i | True |  |  |
| remap.blindAt | 180 | i | True |  |  |
| remap.blindDeg | 71 | g | True | birds-raptors-owls.jsonl:O'Rourke 2010 | Middle of 60 degrees (Cooper's hawk) and 82 degrees (red-tailed hawk), which is 71. |
| remap.blindSoft | 6 | i | True |  |  |

## Warnings
- params.cpd: the floor run found this parameter invisible near 3.35

## Records dropped before sending
- dropped: retracted by the audit: 15
- log lines: 1081
- table lines: 1585
