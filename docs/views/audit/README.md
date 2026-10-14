# The audit of the evidence logs

`ALL.jsonl` holds one row for each of the 4,622 records in the 18 evidence logs that were audited (the logs on `research/<unit>` on 13 October 2026). A record is identified by its unit and its line number in `docs/views/evidence/<unit>.jsonl`, written "bee:156". The audit asked whether each record says what its source says. It decided nothing about the animals.

The per-unit decision files that stood here before (`<unit>.jsonl`, from the first full run) are replaced by this file; 935 of their rows said "no usable verdict" because of a script bug, now fixed.

## How the verdicts were made

The first pass is Claude Haiku 5.5 (Message Batches API). It sees the record, its quote and a card for the work from the literature index (title, year, venue, the taxa named in the title and abstract, the start of the abstract). It answers whether the quote supports the value, whether the units and any conversion are right, whether the grade is honest and whether the taxon is right. A script checks the numbers of the value against the quote on its own. The grade question asks whether the measured taxon is the record's taxon; it does not ask whether the quote repeats the species name.

The second pass is Claude Sonnet 5.5. It takes each flagged record, finds the source in the literature collection (`pub/lit-t1`) by DOI, cuts a passage of about 5,000 characters around the quote from the full text (or the abstract when only that exists), and says confirm, correct, retract or unverifiable. A script checks that the passage it cites is in the text it was shown.

Code: `tools/lit/audit.py` (both passes), `tools/lit/audit_compare.py` (first-pass comparison), `tools/lit/audit_all.py` (builds `ALL.jsonl`), `tools/views/apply_audit.py` (applies it). The runs are on the `ci` branch: `runs/lit-audit/3` (first pass with the old prompt, and the first second pass), `4` (first pass with the new prompt), `5` and `6` (second pass on the records the first round left undecided).

## What each verdict means

| verdict | meaning | what to do to the log |
|---|---|---|
| `stands` | The first pass found no problem. Nobody read the paper. | Nothing. |
| `confirm` | The second pass read the passage and the record is right as logged. | Nothing. |
| `correct` | The passage supports a value for this trait but a field is wrong. `corrected_record` is the whole record with the fix; `reason` says what changed and `passage_quote` gives the words that decided it. | Replace the record with `corrected_record`. |
| `retract` | The passage does not state this value or trait for this animal, or states the opposite. | Drop the record. |
| `unverifiable` | The passage the second pass was given (mostly an abstract) does not reach the quoted figures. The flag stays open. | Keep the record; check it against the paper when the paper is read. |
| `flagged_unchecked` | The first pass flagged it and no second pass settled it. `reason` says why: the source has no text or abstract in the collection (467), the source is not in the collection (179), or the reply could not be read (17). | Keep the record. `flags` and `first_pass` say what the first pass saw. |
| `unseen` | Never audited: the quote is empty or the source is a book. | Nothing. |

Rows also carry `flags` (the first-pass reasons: `supports:partly`, `supports:no`, `units`, `grade`, `taxon`, `number_not_in_quote`), `grade` as logged and, for `correct`, `grade_final`.

Most corrections are grade changes. Of the 1,152 corrections, 975 change the grade (820 from `m` to `g`, 146 from `g` to `m`, 9 between other grades). The second pass applies the rule that a species-level record whose passage names only a genus, family or common name, or reports other studies, is `g`. The rule is in `SYSTEM_ADJ` in `tools/lit/audit.py`. A sample of the 820 is worth reading before they are applied.

## How to apply it to a log

```
python3 -I tools/views/apply_audit.py docs/views/evidence/bee.jsonl --all docs/views/audit/ALL.jsonl --out bee.corrected.jsonl
```

The script writes a corrected copy and never edits the log. It refuses to write over the log, and over an existing file without `--force`. Corrected records gain an `audit` field holding the old values of the fields that changed (`--no-mark` leaves it out). Retracted records are dropped (`--retracted keep` keeps them, marked). Records the audit left open (`flagged_unchecked`, `unverifiable`) gain an `audit` field with their reason, so the flag travels with them. A row is applied only when the log's line still holds the taxon, trait and value the audit saw; a line edited since is copied unchanged and reported, and the script exits with status 1. Its check is `python3 -I tools/views/test_apply_audit.py`. The research branches are applied later by their owners.

## Counts

First pass with the new prompt: 2,983 of the 4,166 records sent were flagged (71.6%), against 3,223 (77.4%) with the old prompt. 456 records were never sent.

Settled by the second pass: 1,776 (599 confirm, 1,152 correct, 25 retract), up from 1,077. A further 746 are `unverifiable` and 663 stay `flagged_unchecked`.

| unit | records | stands | confirm | correct | retract | unverifiable | flagged_unchecked | unseen |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| bee | 267 | 40 | 44 | 84 | 1 | 79 | 14 | 5 |
| birds | 218 | 54 | 49 | 46 | 1 | 3 | 64 | 1 |
| birds-met | 77 | 10 | 11 | 5 | 1 | 3 | 47 | 0 |
| cat-dog | 178 | 35 | 26 | 14 | 0 | 5 | 62 | 36 |
| fish-shark | 187 | 47 | 56 | 40 | 0 | 6 | 27 | 11 |
| ground-invertebrates | 197 | 48 | 27 | 74 | 1 | 2 | 36 | 9 |
| herps | 220 | 72 | 32 | 72 | 0 | 1 | 24 | 19 |
| herps-met | 38 | 2 | 6 | 30 | 0 | 0 | 0 | 0 |
| insect | 523 | 71 | 38 | 166 | 5 | 182 | 31 | 30 |
| insects-met | 52 | 33 | 13 | 4 | 0 | 2 | 0 | 0 |
| jumper | 282 | 74 | 50 | 24 | 0 | 48 | 46 | 40 |
| mammal-groups | 209 | 90 | 59 | 24 | 4 | 6 | 22 | 4 |
| mammals-met | 15 | 7 | 4 | 3 | 0 | 1 | 0 | 0 |
| methods | 1159 | 85 | 7 | 342 | 0 | 371 | 149 | 205 |
| plant-fungus-slime | 202 | 39 | 48 | 57 | 3 | 5 | 32 | 18 |
| sea-invertebrates | 307 | 110 | 49 | 78 | 2 | 7 | 25 | 36 |
| spider | 320 | 96 | 51 | 38 | 5 | 23 | 67 | 40 |
| squirrel-deer-rabbit | 171 | 68 | 29 | 51 | 2 | 2 | 17 | 2 |
| **all** | 4622 | 981 | 599 | 1152 | 25 | 746 | 663 | 456 |

| trait | records | stands | confirm | correct | retract | unverifiable | flagged_unchecked | unseen |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| lambda_max_nm | 1446 | 163 | 46 | 505 | 1 | 427 | 204 | 100 |
| acuity_cpd | 310 | 72 | 32 | 57 | 2 | 12 | 92 | 43 |
| behaviour_vision | 274 | 69 | 73 | 63 | 1 | 16 | 35 | 17 |
| colour_vision | 184 | 54 | 32 | 51 | 0 | 22 | 17 | 8 |
| receptor_classes | 183 | 36 | 37 | 43 | 0 | 19 | 18 | 30 |
| cff_hz | 150 | 68 | 16 | 46 | 0 | 6 | 13 | 1 |
| fovea | 140 | 42 | 31 | 27 | 0 | 20 | 7 | 13 |
| interommatidial_deg | 135 | 19 | 5 | 9 | 0 | 98 | 3 | 1 |
| sense_light_nonvisual | 118 | 31 | 25 | 35 | 1 | 4 | 17 | 5 |
| eye_movement | 99 | 19 | 18 | 10 | 1 | 7 | 16 | 28 |
| sense_vibration | 97 | 31 | 21 | 14 | 1 | 1 | 25 | 4 |
| fov_h_deg | 96 | 25 | 11 | 12 | 4 | 8 | 12 | 24 |
| motion | 93 | 27 | 23 | 11 | 2 | 15 | 9 | 6 |
| absolute_sensitivity | 86 | 16 | 21 | 20 | 1 | 5 | 11 | 12 |
| eye_role | 78 | 21 | 6 | 19 | 0 | 3 | 13 | 16 |
| eye_type | 77 | 15 | 14 | 25 | 1 | 4 | 10 | 8 |
| polarization | 71 | 20 | 16 | 17 | 1 | 3 | 6 | 8 |
| eyes_count | 64 | 21 | 10 | 19 | 0 | 2 | 6 | 6 |
| sense_chemical | 62 | 18 | 12 | 15 | 0 | 0 | 16 | 1 |
| binocular_deg | 61 | 16 | 10 | 15 | 1 | 2 | 11 | 6 |
| interreceptor_deg | 51 | 4 | 2 | 6 | 0 | 10 | 5 | 24 |
| tapetum | 51 | 19 | 7 | 7 | 0 | 0 | 11 | 7 |
| spectral_range_nm | 50 | 5 | 9 | 15 | 2 | 2 | 11 | 6 |
| acceptance_deg | 49 | 8 | 4 | 4 | 0 | 24 | 1 | 8 |
| sense_hearing | 49 | 14 | 12 | 9 | 0 | 1 | 13 | 0 |
| ocular_media_t50_nm | 49 | 34 | 6 | 0 | 0 | 0 | 9 | 0 |
| filter_pigments | 48 | 19 | 13 | 3 | 1 | 2 | 10 | 0 |
| depth_cue | 45 | 15 | 5 | 9 | 0 | 4 | 5 | 7 |
| sense_touch | 41 | 7 | 5 | 13 | 0 | 3 | 8 | 5 |
| sense_electric | 32 | 10 | 11 | 8 | 1 | 0 | 2 | 0 |
| diel | 30 | 6 | 4 | 9 | 0 | 2 | 2 | 7 |
| sense_airflow | 30 | 6 | 11 | 6 | 0 | 6 | 1 | 0 |
| f_number | 27 | 8 | 2 | 3 | 0 | 3 | 2 | 9 |
| sense_echolocation | 24 | 5 | 9 | 7 | 0 | 2 | 1 | 0 |
| sense_magnetic | 21 | 7 | 9 | 3 | 0 | 1 | 1 | 0 |
| pupil | 21 | 3 | 2 | 1 | 0 | 4 | 8 | 3 |
| fov_v_deg | 20 | 1 | 4 | 4 | 0 | 2 | 5 | 4 |
| optical_sensitivity | 17 | 0 | 0 | 0 | 0 | 0 | 0 | 17 |
| sense_infrared | 16 | 4 | 7 | 4 | 0 | 0 | 0 | 1 |
| oil_droplets | 15 | 4 | 3 | 1 | 0 | 0 | 6 | 1 |
| sense_gravity | 15 | 3 | 2 | 6 | 0 | 0 | 3 | 1 |
| light_environment | 14 | 0 | 4 | 0 | 0 | 0 | 6 | 4 |
| rhabdom_um | 11 | 4 | 0 | 4 | 1 | 1 | 1 | 0 |
| circadian | 11 | 2 | 0 | 6 | 0 | 0 | 3 | 0 |
| corner_hz | 10 | 2 | 2 | 2 | 3 | 1 | 0 | 0 |
| integration_time_ms | 9 | 0 | 0 | 0 | 0 | 1 | 0 | 8 |
| pupil_shape | 8 | 2 | 2 | 3 | 0 | 1 | 0 | 0 |
| sense_thermal | 5 | 2 | 2 | 1 | 0 | 0 | 0 | 0 |
| retina_tiers | 5 | 0 | 2 | 1 | 0 | 1 | 1 | 0 |
| contrast_sensitivity | 3 | 2 | 0 | 1 | 0 | 0 | 0 | 0 |
| leaf_reflectance | 3 | 0 | 0 | 1 | 0 | 0 | 0 | 2 |
| refraction | 2 | 0 | 1 | 0 | 0 | 0 | 1 | 0 |
| accommodation | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 2 |
| lens_chromatic_aberration | 2 | 0 | 0 | 1 | 0 | 0 | 1 | 0 |
| habitat | 2 | 1 | 0 | 0 | 0 | 0 | 1 | 0 |
| temporal_response | 2 | 0 | 0 | 0 | 0 | 0 | 2 | 0 |
| lens_optics | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| eye_axial_mm | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| optical_sensitivity_um2sr | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| rendering_method | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| response_time_ms | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| ommatidia_count | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| eye_diameter_mm | 1 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
| receptor_count | 1 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |

## Spend

First pass with the new prompt $0.31. Second pass on the 1,282 flagged records among the 1,513 left undecided $3.76. Second pass on the 253 records only the new prompt flags $0.78. With the earlier $7.3 the audit has cost about $12.2.
