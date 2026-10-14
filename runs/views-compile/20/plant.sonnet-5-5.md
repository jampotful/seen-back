# Draft spec for plant (claude-sonnet-5-5)

Compiled from 297 records. Not offered; a person judges it on a phone through `?try=plant`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| matrices.plant_light | [[0.52237,0.23491,0.1361,0.10662],[0.01737,0.32004... | g | True | plants-light.jsonl:Briggs 1983, plants-light.jsonl:Péter 2024, plants-light.jsonl:Spalding 2003 | The peaks 660 nm, 475 nm and 360 nm are the values stated by R5, R6 and R7. |
| params.M | "plant_light" | g | True | plants-light.jsonl:Briggs 1983, plants-light.jsonl:Péter 2024, plants-light.jsonl:Spalding 2003 | The named matrix is built from peaks 360, 475 and 660 nm, which are the values of R7, R6 and R5; the mixing is chosen. |
| params.field | 1 | i | True |  |  |
| params.gain | 2 | i | True |  |  |
| params.persist | 20 | i | True |  |  |
| params.pupil | "none" | i | True |  |  |
| params.uvBlue | 0.6 | i | True |  |  |
| slow.everyMs | 3000 | i | True |  |  |
| slow.rightS | 20 | i | True |  |  |
| slow.windowS | 600 | i | True |  |  |

## Warnings
- added the row 'Settings the app chose', which names 1 invented parameters the reply left unnamed

## Records dropped before sending
- dropped: retracted by the audit: 15
- log lines: 1081
- table lines: 1956
