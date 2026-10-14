# Draft spec for frog (claude-sonnet-5-5)

Compiled from 400 records. Not offered; a person judges it on a phone through `?try=frog`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| matrices.FROG | [[0.37036,0.43871,0.11821,0.07271],[0.06933,0.4567... | g | True | frogs.jsonl:Matthews 1983, herps-met.jsonl:Schott 2022, intake-8.jsonl:Schott 2022 | from_pigments lists 433, 502 and 570 nm, each equal to the value of a cited record. |
| params.M | "FROG" | g | True | frogs.jsonl:Matthews 1983, herps-met.jsonl:Schott 2022, intake-8.jsonl:Schott 2022 | Peaks 570 nm (bullfrog LWS, R10), 433 nm (toad green rod, R25) and 502 nm (Bufo bufo rod 1, R15) form the matrix; the mapping to camera colors is the app's. |
| params.cpd | 4.3 | m | False | frogs.jsonl:Aho 1997 | Equals the common frog optomotor acuity of 4.3 cycles per degree, the best of the acuity records. |
| params.fall | 1.33 | g | True | frogs.jsonl:Pushchin 2019 | Peak acuity 2.1 (R5) over peripheral 0.9 (R3), both in air in Hyla japonica, gives R = 2.33; fall = R - 1 = 1.33. |
| params.fov | 300 | i | True |  |  |
| params.gate | 0.6 | i | True |  |  |
| params.glow | 0.8 | i | True |  |  |
| params.topoS | 1 | i | True |  |  |

## Warnings
- added the row 'Settings the app chose', which names 1 invented parameters the reply left unnamed
- params.cpd: the floor run found this parameter invisible near 3.35

## Records dropped before sending
- dropped: retracted by the audit: 15
- log lines: 1081
- table lines: 2017
