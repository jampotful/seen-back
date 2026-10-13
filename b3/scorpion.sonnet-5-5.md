# Draft spec for scorpion (claude-sonnet-5-5)

Compiled from 163 records. Not offered; a person judges it on a phone through `?try=scorpion`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| haptic.edge | 1 | i | True |  |  |
| haptic.pattern | [18,28] | g | True | arachnids-other.jsonl:Briceño 2009 | A judder lasts 0.018 s and the interval is 0.028 s, so 18 ms on and 28 ms off. |
| params.M | "SCORPION" | i | True |  |  |
| params.cpd | 0.5 | i | True |  |  |
| params.fov | 360 | g | False | arachnids-other.jsonl:Gaffin 2022, arachnids-other.jsonl:Prévost 2020 | Both records state a 360 degree field of view for scorpions. |
| params.gain | 2.5 | i | True |  |  |

## Warnings
- params.cpd: the floor run found this parameter invisible near 0.75

## Records dropped before sending
- table lines: 2040
