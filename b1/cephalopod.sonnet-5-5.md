# Draft spec for cephalopod (claude-sonnet-5-5)

Compiled from 300 records. Not offered; a person judges it on a phone through `?try=cephalopod`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| by.order.Octopoda.params.pupil | "h" | m | True | cephalopods.jsonl:Hanke 2020 | The octopus record says the pupil constricts to a horizontal slit in bright light. |
| params.cpd | 8 | g | True | cephalopods.jsonl:Taniguchi 2015 | The cuttlefish acuity record states about 8 cycles per degree. |
| params.fov | 282 | m | True | cephalopods.jsonl:Sugimoto 2026, cephalopods.jsonl:Watanuki 2000 | 282 lies at the middle of 253 degrees for one cuttlefish eye and 311 degrees for a young squid. |
| params.sat | 0 | g | True | cephalopods.jsonl:Hanke 2021, cephalopods.jsonl:How 2017 | The records say most cephalopods are colour blind with one visual pigment, which the app maps to a saturation of 0. |
| params.topoS | 0.6 | i | True |  |  |

## Warnings
- params.cpd: the floor run found this parameter invisible near 3.35

## Records dropped before sending
- table lines: 1562
