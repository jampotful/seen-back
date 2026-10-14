# Draft spec for squirrel (claude-sonnet-5-5)

Compiled from 318 records. Not offered; a person judges it on a phone through `?try=squirrel`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| matrices.DARK_502 | [[0.06933,0.45679,0.38602,0.08786],[0.06933,0.4567... | g | True | rodents-lagomorphs.jsonl:Green 1975 | The matrix is derived from the rod peak of 502 nm stated in R7. |
| matrices.SQUIRREL_DI | [[0.12916,0.50121,0.28844,0.0812],[0.12916,0.50121... | g | True | sweep-11.jsonl:Jacobs 1985 | The matrix is derived from the peaks 436.7 and 518.9 nm stated in R5. |
| params.M | "SQUIRREL_DI" | g | True | sweep-11.jsonl:Jacobs 1985 | The matrix is built from the two cone peaks 436.7 and 518.9 nm of R5, so the mapping is worked out by the engine and graded g. |
| params.cpd | 3.9 | m | False | intake-2.jsonl:Jacobs 1982 | The record gives a maximum of 3.9 cycles per degree in a gray squirrel, and the parameter equals it. |
| params.fall | 1 | i | True |  |  |
| params.rate | 0.92 | g | True | intake-6.jsonl:Inger 2014 | 60 Hz divided by the 65.0 Hz flicker fusion of the American red squirrel gives 0.92. |
| params.sat | 0.7 | i | True |  |  |
| params.topoS | 0.6 | i | True |  |  |
| spectrum.adaptAt | [-2,-0.5] | i | True |  |  |

## Warnings
- params.cpd: the floor run found this parameter invisible near 3.35

## Records dropped before sending
- dropped: retracted by the audit: 15
- log lines: 1081
- table lines: 2949
