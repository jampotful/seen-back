# Draft spec for scorpion (claude-sonnet-5-5)

Compiled from 163 records. Not offered; a person judges it on a phone through `?try=scorpion`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| matrices.SCORPION | [[0.1554,0.50752,0.25771,0.07937],[0.1554,0.50752,... | g | True | arachnids-other.jsonl:Forero 2026 | Pigment peaks 470 and 525 nm are taken directly from the two records and turned into a colour matrix by the app. |
| params.M | "SCORPION" | g | True | arachnids-other.jsonl:Forero 2026 | The matrix is built from the two peaks, 470 nm (R5) and 525 nm (R9), that the records give; the mapping to screen colours is the app's. |
| params.cpd | 1 | i | True |  |  |
| params.fov | 360 | g | True | arachnids-other.jsonl:Gaffin 2022, arachnids-other.jsonl:Prévost 2020 | Both records state a 360 degree field of view for scorpions. |
| params.gain | 2 | i | True |  |  |

## Warnings
- added the row 'Settings the app chose', which names 1 invented parameters the reply left unnamed
- params.cpd: the floor run found this parameter invisible near 0.75

## Records dropped before sending
- table lines: 2040
