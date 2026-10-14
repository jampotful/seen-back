# Draft spec for cephalopod (claude-sonnet-5-5)

Compiled from 400 records. Not offered; a person judges it on a phone through `?try=cephalopod`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| by.order.Octopoda.params.rate | 0.83 | g | True | cephalopods.jsonl:Hanke 2020 | A person's flicker limit of about 60 Hz divided by the octopus 72 Hz gives 0.83. |
| matrices.CEPHALOPOD_ONE | [[0.02336,0.3491,0.52395,0.10358],[0.02336,0.3491,... | g | True | cephalopods.jsonl:Hubbard 1965 | The single pigment peak of 480 nanometres equals the octopus value in R37. |
| params.M | "CEPHALOPOD_ONE" | g | True | cephalopods.jsonl:How 2017, cephalopods.jsonl:Hubbard 1965 | The matrix is built from the 480 nanometre pigment peak of R37, and R60 says most cephalopods have only one visual pigment. |
| params.cpd | 6.56 | m | True | cephalopods.jsonl:Turnbull 2014 | The value equals the squid acuity of 6.56 cycles per degree. |
| params.fov | 320 | g | True | cephalopods.jsonl:Sugimoto 2026 | 320 lies between 311 (R23) and 329 (R31), both measured in young oval squid. |
| zones[0].cpd | 12.23 | g | True | cephalopods.jsonl:Turnbull 2014 | The value equals the octopus acuity of 12.23 cycles per degree. |
| zones[0].frac | 0.3 | i | True |  |  |

## Warnings
- params.cpd: the floor run found this parameter invisible near 3.35

## Records dropped before sending
- table lines: 1562
