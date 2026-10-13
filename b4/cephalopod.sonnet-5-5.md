# Draft spec for cephalopod (claude-sonnet-5-5)

Compiled from 400 records. Not offered; a person judges it on a phone through `?try=cephalopod`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| matrices.single_pigment_485 | [[0.03083,0.37707,0.49324,0.09886],[0.03083,0.3770... | g | True | cephalopods.jsonl:Chung 2016 | The pigment peak of 485 nanometres equals the value in both records. |
| params.M | "single_pigment_485" | g | True | cephalopods.jsonl:Chung 2016 | Names the matrix built from the single 485 nanometre pigment peak that both records give. |
| params.cpd | 6.56 | m | True | cephalopods.jsonl:Turnbull 2014 | The squid acuity is 6.56 cycles per degree. |
| params.fov | 322 | m | True | cephalopods.jsonl:Sugimoto 2026 | The field of a squid 28 days old is 322 degrees in the table row. |
| params.sheen | 0 | i | True |  |  |
| zones[0].cpd | 10.9 | g | True | cephalopods.jsonl:Hanke 2020, cephalopods.jsonl:Turnbull 2014 | 6.56 times the square root of 55000 over 20000 (the middle of 18000 to 22000) is 6.56 times 1.658, which is about 10.9. |

## Warnings
- params.cpd: the floor run found this parameter invisible near 3.35

## Records dropped before sending
- table lines: 1562
