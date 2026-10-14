# Draft spec for insect (claude-sonnet-5-5)

Compiled from 400 records. Not offered; a person judges it on a phone through `?try=insect`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| matrices.insect_uvbg | [[0.22664,0.50311,0.19444,0.07581],[0.00122,0.1280... | g | True | intake-2.jsonl:Swihart 1969, sweep-7.jsonl:Sison-Mangus 2006 | Pigment peaks 360 nm (Lycaena rubidus), 440 nm and 540 nm (Epargyreus clarus) are each stated in a cited record. |
| params.M | "insect_uvbg" | g | True | intake-2.jsonl:Swihart 1969, sweep-7.jsonl:Sison-Mangus 2006 | The matrix is built from peaks 360, 440 and 540 nm, each equal to a peak stated in these records. |
| params.cpd | 0.5 | g | True | sweep-22.jsonl:Wright 2023, sweep-26.jsonl:Ogawa 2023 | 0.5 lies between 0.49 cycles per degree in Heliconius erato cyrbia and 0.52 in Oecophylla smaragdina. |
| params.fov | 300 | g | True | insects-general.jsonl:A 2016, insects-general.jsonl:Freas 2022 | Three records give a visual field of about 300 degrees for ants, and the parameter equals that figure. |
| params.pupil | "none" | i | True |  |  |
| params.rate | 0.3 | g | True | intake-2.jsonl:Swihart 1969, intake-3.jsonl:Chatterjee 2020 | Flicker fusion of about 200 Hz lies in 180 to 200 Hz (skipper) and 184 to 204 Hz (nymphalids); 60 / 200 = 0.3. |
| params.uvBlue | 0.6 | i | True |  |  |

## Warnings
- params.cpd: the floor run found this parameter invisible near 0.75

## Records dropped before sending
- dropped: retracted by the audit: 15
- log lines: 1081
- table lines: 18879
