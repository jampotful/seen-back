# Draft spec for whale (claude-haiku-5-5)

Compiled from 300 records. Not offered; a person judges it on a phone through `?try=whale`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| matrices.whale_mono | [[1,0,0],[1,0,0],[1,0,0]] | i | True |  |  |
| params.cpd | 3.3 | m | True | marine-mammals.jsonl:Lisney 2018, marine-mammals.jsonl:Murayama 1995, marine-mammals.jsonl:Murayama 1998 | The value 3.3 is the upper value of the humpback whale resolving power (R4), sits inside the 2.6 to 3.3 range of R2, and matches the upper end of the 2.6 cycles per degree of R10, taken as a middle value across inside taxa. |
| params.fov | 125 | m | True | marine-mammals.jsonl:JM 2022, marine-mammals.jsonl:Kremers 2016 | The value 125 is the middle of the 120 to 130 degree panoramic field stated for dolphins in R19. |
| params.gain | 1.5 | i | True |  |  |

## Warnings
- added the row 'Settings the app chose', which names 3 invented parameters the reply left unnamed
- params.cpd: the floor run found this parameter invisible near 3.35

## Records dropped before sending
- table lines: 4035
