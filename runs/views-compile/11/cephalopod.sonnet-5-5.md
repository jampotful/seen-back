# Draft spec for cephalopod (claude-sonnet-5-5)

Compiled from 400 records. Not offered; a person judges it on a phone through `?try=cephalopod`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| matrices.cephalopod_one_pigment | [[0.03083,0.37707,0.49324,0.09886],[0.03083,0.3770... | g | True | cephalopods.jsonl:Chung 2016 | The single pigment peak of 485 nm equals the peak stated for Hapalochlaena maculosa and Octopus australis. |
| params.M | "cephalopod_one_pigment" | g | True | cephalopods.jsonl:Chung 2016 | The matrix is built from one pigment peak at 485 nm, the peak stated for Hapalochlaena maculosa and Octopus australis. |
| params.cpd | 8 | g | True | cephalopods.jsonl:Taniguchi 2015 | The cuttlefish acuity record states about 8 cycles per degree, and the view uses 8 for the group. |
| params.fov | 291 | g | True | cephalopods.jsonl:Sugimoto 2026, cephalopods.jsonl:Watanuki 2000 | (253 + 329) / 2 = 291 degrees, the middle of the cuttlefish uniocular field and the 35 day squid field. |
| params.pupil | "h" | g | True | cephalopods.jsonl:Hanke 2020 | The octopus pupil constricts to a horizontal slit in bright light, drawn as the horizontal slit shape. |
| params.sheen | 0 | i | True |  |  |
| params.topoA | 0.2 | i | True |  |  |
| params.topoS | 0.8 | i | True |  |  |

## Warnings
- added the row 'Settings the app chose', which names 1 invented parameters the reply left unnamed
- params.cpd: the floor run found this parameter invisible near 3.35

## Records dropped before sending
- table lines: 1562
