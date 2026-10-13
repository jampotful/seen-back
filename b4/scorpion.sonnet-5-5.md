# Draft spec for scorpion (claude-sonnet-5-5)

Compiled from 163 records. Not offered; a person judges it on a phone through `?try=scorpion`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| haptic.edge | 0.6 | i | True |  |  |
| haptic.pattern | [18,28] | g | True | arachnids-other.jsonl:Briceño 2009 | 0.018 s pulse and 0.028 s interval converted to 18 ms and 28 ms; using them as a phone vibration is the app's choice. |
| params.M | "SCORPION" | g | True | arachnids-other.jsonl:Forero 2026 | The matrix is built from the 470 nm and 525 nm peaks; the mapping to screen colours is the app's choice. |
| params.cpd | 0.3 | i | True |  |  |
| params.fov | 360 | g | False | arachnids-other.jsonl:Gaffin 2022, arachnids-other.jsonl:Prévost 2020 | Both records state a 360 degree field of view for scorpions. |
| params.gain | 2.5 | i | True |  |  |

## Warnings
- params.cpd: the floor run found this parameter invisible near 0.75

## Records dropped before sending
- table lines: 2040
