# Draft spec for deer (claude-sonnet-5-5)

Compiled from 400 records. Not offered; a person judges it on a phone through `?try=deer`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| matrices.DEER | [[0.21189,0.50602,0.20567,0.07642],[0.21189,0.5060... | g | True | ungulates.jsonl:DR 2025 | The peaks 450 nm (low end of the 450 to 460 nm range in R24) and 537 nm (R26) are entered as pigment peaks; the turning of them into color rows is worked out by the engine and is the app's choice. |
| params.M | "DEER" | g | True | ungulates.jsonl:DR 2025 | The matrix is built from the 450 nm low end of the 450 to 460 nm short cone range (R24) and the 537 nm middle cone peak (R26); the mapping to screen colors is the app's. |
| params.cpd | 5 | m | False | ungulates.jsonl:Watson 2022 | The middle of the 4 to 6 cycles per degree that R3 estimates for white-tailed deer is 5. |
| params.fall | 1.2 | i | True |  |  |
| params.fov | 360 | g | False | ungulates.jsonl:Reimers 2021 | R4 states a combined visual field of both eyes of about 360 degrees for Rangifer and other deer. |
| params.gain | 1.4 | i | True |  |  |
| params.sheen | 0.5 | i | True |  |  |
| params.topoS | 0.7 | i | True |  |  |
| params.uvBlue | 0.4 | i | True |  |  |

## Warnings
- added the row 'Settings the app chose', which names 1 invented parameters the reply left unnamed
- params.cpd: the floor run found this parameter invisible near 3.35

## Records dropped before sending
- dropped: retracted by the audit: 15
- log lines: 1081
- table lines: 1769
