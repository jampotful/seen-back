# Audit of the evidence logs, first pass


Records: 4622 in the logs, 4166 sent, 456 unseen (empty quote or book source). Estimate expected $0.23, ceiling $1.11; spent $0.2804.

Replies with no usable verdict: bad fields: taxon_ok x1

## Share flagged by unit

| unit | sent | unseen | flagged | no | partly | units | grade | taxon | number not in quote |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| bee | 262 | 5 | 209 (79.8%) | 5 | 111 | 1 | 150 | 18 | 2 |
| birds | 217 | 1 | 145 (66.8%) | 2 | 104 | 5 | 67 | 17 | 3 |
| birds-met | 77 | 0 | 60 (77.9%) | 1 | 15 | 1 | 47 | 2 | 0 |
| cat-dog | 142 | 36 | 103 (72.5%) | 2 | 60 | 13 | 73 | 21 | 2 |
| fish-shark | 176 | 11 | 125 (71.0%) | 2 | 104 | 9 | 50 | 28 | 6 |
| ground-invertebrates | 188 | 9 | 156 (83.0%) | 1 | 132 | 6 | 91 | 28 | 1 |
| herps | 201 | 19 | 141 (70.1%) | 3 | 115 | 19 | 54 | 27 | 5 |
| herps-met | 38 | 0 | 36 (94.7%) | 0 | 22 | 0 | 30 | 3 | 3 |
| insect | 493 | 30 | 429 (87.0%) | 4 | 182 | 9 | 361 | 49 | 19 |
| insects-met | 52 | 0 | 30 (57.7%) | 0 | 29 | 0 | 4 | 1 | 0 |
| jumper | 242 | 40 | 182 (75.2%) | 1 | 167 | 13 | 51 | 41 | 6 |
| mammal-groups | 205 | 4 | 129 (62.9%) | 4 | 102 | 20 | 46 | 17 | 4 |
| mammals-met | 15 | 0 | 9 (60.0%) | 0 | 7 | 1 | 2 | 0 | 0 |
| methods | 954 | 205 | 831 (87.1%) | 3 | 519 | 2 | 731 | 37 | 1 |
| plant-fungus-slime | 184 | 18 | 154 (83.7%) | 3 | 134 | 12 | 64 | 25 | 3 |
| sea-invertebrates | 271 | 36 | 184 (67.9%) | 3 | 145 | 16 | 78 | 21 | 6 |
| spider | 280 | 40 | 207 (73.9%) | 5 | 173 | 11 | 77 | 29 | 4 |
| squirrel-deer-rabbit | 169 | 2 | 93 (55.0%) | 2 | 62 | 11 | 48 | 11 | 3 |
| **all** | 4166 | 456 | 3223 (77.4%) | 41 | 2183 | 149 | 2024 | 375 | 68 |

## Share flagged by trait

| trait | sent | flagged | share |
|---|---:|---:|---:|
| lambda_max_nm | 1346 | 1180 | 87.7% |
| behaviour_vision | 257 | 202 | 78.6% |
| acuity_cpd | 267 | 176 | 65.9% |
| colour_vision | 176 | 130 | 73.9% |
| receptor_classes | 153 | 120 | 78.4% |
| interommatidial_deg | 134 | 112 | 83.6% |
| sense_light_nonvisual | 113 | 95 | 84.1% |
| fovea | 127 | 86 | 67.7% |
| sense_vibration | 93 | 69 | 74.2% |
| cff_hz | 149 | 64 | 43.0% |
| absolute_sensitivity | 74 | 61 | 82.4% |
| motion | 87 | 60 | 69.0% |
| eye_type | 69 | 60 | 87.0% |
| eye_movement | 71 | 54 | 76.1% |
| sense_chemical | 61 | 53 | 86.9% |
| polarization | 63 | 50 | 79.4% |
| eye_role | 62 | 48 | 77.4% |
| fov_h_deg | 72 | 46 | 63.9% |
| eyes_count | 58 | 43 | 74.1% |
| spectral_range_nm | 44 | 38 | 86.4% |
| binocular_deg | 55 | 34 | 61.8% |
| sense_hearing | 49 | 34 | 69.4% |
| sense_touch | 36 | 30 | 83.3% |
| tapetum | 44 | 30 | 68.2% |
| depth_cue | 38 | 28 | 73.7% |
| sense_electric | 32 | 26 | 81.2% |
| filter_pigments | 48 | 26 | 54.2% |
| sense_airflow | 30 | 26 | 86.7% |
| interreceptor_deg | 27 | 21 | 77.8% |
| diel | 23 | 20 | 87.0% |
| acceptance_deg | 41 | 19 | 46.3% |
| sense_echolocation | 24 | 18 | 75.0% |
| sense_magnetic | 21 | 16 | 76.2% |
| fov_v_deg | 16 | 15 | 93.8% |
| sense_infrared | 15 | 13 | 86.7% |
| sense_gravity | 14 | 13 | 92.9% |
| pupil | 18 | 12 | 66.7% |
| oil_droplets | 14 | 11 | 78.6% |
| f_number | 18 | 10 | 55.6% |
| circadian | 11 | 10 | 90.9% |
| rhabdom_um | 11 | 9 | 81.8% |
| corner_hz | 10 | 9 | 90.0% |
| light_environment | 10 | 9 | 90.0% |
| ocular_media_t50_nm | 49 | 8 | 16.3% |
| pupil_shape | 8 | 6 | 75.0% |

## Share flagged by grade the researcher gave

| grade | sent | flagged | share |
|---|---:|---:|---:|
| m | 3499 | 2745 | 78.5% |
| g | 638 | 455 | 71.3% |
| i | 17 | 12 | 70.6% |
| x | 12 | 11 | 91.7% |

## Main problem named by the reviewer (flagged records)

| kind | count |
|---|---:|
| grade | 1831 |
| quote_loose | 798 |
| wrong_taxon | 175 |
| context_needed | 125 |
| value_absent | 114 |
| wrong_trait | 77 |
| units | 49 |
| conversion | 30 |
| none | 15 |
| wrong_eye | 8 |

## Grade changes the reviewer suggests (given grade, suggested)

| given | suggested | count |
|---|---|---:|
| m | g | 1820 |
| g | m | 108 |
| m | i | 33 |
| g | i | 10 |
| x | i | 5 |
| x | g | 4 |
| i | g | 2 |
| x | m | 2 |
| i | m | 1 |
