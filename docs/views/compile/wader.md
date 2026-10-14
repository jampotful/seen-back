# Draft spec for wader (claude-sonnet-5-5)

Compiled from 400 records. Not offered; a person judges it on a phone through `?try=wader`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| matrices.WADER | [[0.32957,0.46264,0.13475,0.07303],[0.0416,0.35551... | m | True | intake-3.jsonl:Porter 2014 | The pigment list is the whooping crane's four cone peaks. |
| params.M | "WADER" | m | True | intake-3.jsonl:Porter 2014 | The matrix is built from the whooping crane's four cone peaks, 404, 450, 499 and 561 nm. |
| params.cpd | 11.04 | g | False | birds-other.jsonl:Rounsley 2005 | The pigeon's peak average acuity of 11.04 cycles per degree stands in for an unmeasured wader. |
| params.fov | 320 | m | False | birds-other.jsonl:Katzir 1998 | The black-crowned night heron's cyclopean field in the horizontal plane is 320 degrees. |
| params.hold | 20 | i | True |  |  |
| params.rate | 0.78 | g | True | intake-6.jsonl:Inger 2014 | 60 Hz for a human divided by the pigeon's 77 Hz flicker fusion is about 0.78. |
| params.thrust | 50 | i | True |  |  |
| remap.blindAt | 180 | i | True |  |  |
| remap.blindDeg | 40 | g | True | birds-other.jsonl:Katzir 1998 | A full circle of 360 degrees minus the night heron's 320 degree cyclopean field leaves about 40 degrees. |

## Warnings
- params.cpd: the floor run found this parameter invisible near 3.35

## Records dropped before sending
- dropped: retracted by the audit: 15
- log lines: 1081
- table lines: 3726
