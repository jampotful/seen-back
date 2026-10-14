# Draft spec for cat (claude-sonnet-5-5)

Compiled from 181 records. Not offered; a person judges it on a phone through `?try=cat`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| gaze.saccade | [25,3.1] | g | True | carnivores.jsonl:Park 2020 | The second element 3.1 ms per degree is the measured slope in R154; the first element 25 ms is the app's choice. |
| matrices.CAT | [[0.3057,0.47473,0.14613,0.07344],[0.3057,0.47473,... | g | True | carnivores.jsonl:Crocker 1980, carnivores.jsonl:Narfström 2011 | The matrix is built from the measured peaks 450 nm (R8) and 556 nm (R11) for the two cone classes (R12). |
| params.M | "CAT" | g | True | carnivores.jsonl:Crocker 1980, carnivores.jsonl:Narfström 2011 | The matrix is worked out from two cone peaks, 450 nm (R8) and 556 nm (R11), with two cone classes (R12). |
| params.cpd | 8.1 | g | True | carnivores.jsonl:Clark 2013 | Snellen 20/74 converted to cycles per degree as 600 / 74 = 8.1. |
| params.fall | 1.0 | i | True |  |  |
| params.gain | 1.6 | i | True |  |  |
| params.pupil | "v" | g | False | carnivores.jsonl:Goldfinger 2004, carnivores.jsonl:Tabin 2024 | R178 states the constricted pupil of domestic cats is vertical and R21 states the ancestral felid had vertical pupils, written here as an upright slit. |
| params.sat | 0.6 | i | True |  |  |
| params.sheen | 0.6 | i | True |  |  |
| params.topoA | 1 | i | True |  |  |

## Warnings
- added the row 'Settings the app chose', which names 1 invented parameters the reply left unnamed
- params.cpd: the floor run found this parameter invisible near 3.35

## Records dropped before sending
- dropped: retracted by the audit: 15
- log lines: 1081
- table lines: 1655
