# Draft spec for dog (claude-sonnet-5-5)

Compiled from 188 records. Not offered; a person judges it on a phone through `?try=dog`.

| Parameter | Value | Grade | Invented | Records | How |
|---|---|---|---|---|---|
| matrices.DARK_508 | [[0.08817,0.47704,0.34962,0.08517],[0.08817,0.4770... | m | True | carnivores.jsonl:Jacobs 1993 | The peak 508 nm is the record's rod pigment value. |
| matrices.DOG | [[0.30084,0.477,0.14861,0.07355],[0.30084,0.477,0.... | m | True | carnivores.jsonl:Jacobs 1993 | Peaks 430 and 555 nm come from the two cone pigment records. |
| params.M | "DOG" | m | True | carnivores.jsonl:Jacobs 1993 | The matrix is built from the two cone peaks of 555 nm and 430 nm. |
| params.cpd | 7.5 | i | True |  |  |
| params.fall | 1.2 | i | True |  |  |
| params.fov | 240 | g | False | carnivores.jsonl:Park 2020 | The record states a field of 240 degrees for dogs. |
| params.gain | 1.5 | i | True |  |  |
| params.pupil | "o" | g | False | carnivores.jsonl:Araujo 2019, carnivores.jsonl:Paszta 2021 | Both records state a round pupil, one in the painted dog and one in the domestic dog. |
| params.rate | 0.8 | g | True | intake-6.jsonl:Inger 2014 | A human flicker fusion of 60 Hz divided by the dog's 75 Hz gives 0.8. |
| params.sat | 0.7 | i | True |  |  |
| params.sheen | 0.5 | i | True |  |  |
| params.topoS | 0.6 | i | True |  |  |
| params.uvBlue | 0.3 | i | True |  |  |
| spectrum.adaptAt | [-2.5,-1] | i | True |  |  |

## Warnings
- added the row 'Settings the app chose', which names 2 invented parameters the reply left unnamed
- params.cpd: the floor run found this parameter invisible near 3.35

## Records dropped before sending
- dropped: retracted by the audit: 15
- log lines: 1081
- table lines: 1655
