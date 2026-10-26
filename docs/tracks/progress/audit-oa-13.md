# Audit of the oa-13 reading unit, 26 October 2026

Scope: branch `origin/research/oa-13-read` at 80e4a889, `docs/views/evidence/oa-13.jsonl` (1,095 records from 93 papers with records; 120 papers read). Prompt: `docs/tracks/prompts/oa-audit.md`, with the desk's changes: no new key, no run branch and no fetch; the decrypted run 25 texts already on the build machine (`/tmp/oar13key/txt/oa-13-<entry>.txt`) were read in place. No paper text, PDF, XML or key enters this branch. No library login, proxy, shadow library or unauthorized copy was used, and no DOI, author or year was typed from memory.

Rules applied: audit 31 for the error definition and for metadata faults (written down, not counted); audit 39 for the counting rule, under which `requote` counts as an error alongside `correct` and `retract`. Quotes with internal cuts marked " … " follow `oa-read.md`, which allows them; a quote that opens with a cut, and so starts mid-sentence, is a requote (audit 39, harvest-25:2).

## Sample (drawn before any record was checked)

Records were mapped to entries through the `source` objects of the oa-13 lines of `ci/oa/sources-r1.jsonl` (DOI, else title); all 1,095 mapped. `random.seed(1026)`; for every paper other than entry 1, in entry order, `random.sample` of up to 3 of its records (pool of 209); then `random.sample(pool, 40)`; then `random.sample` of 8 of the 604 Table 1 records of entry 1.

Non-entry-1 (40), as `oa-13:<line>` (entry): 644 (13), 940 (126), 933 (120), 693 (30), 707 (42), 680 (25), 632 (11), 697 (30), 870 (106), 719 (52), 690 (28), 1035 (196), 741 (66), 1089 (275), 874 (106), 736 (60), 979 (145), 685 (32), 702 (41), 839 (88), 750 (80), 1077 (253), 1050 (224), 1073 (248), 701 (41), 1078 (257), 872 (106), 679 (25), 943 (127), 682 (34), 711 (44), 955 (139), 628 (11), 947 (137), 1033 (196), 867 (103), 829 (83), 1058 (233), 748 (82), 681 (25).

Entry 1 (8): oa-13:261, 274, 589, 280, 561, 453, 393, 262.

## Method

Each record was run through `python3 -I tools/views/quotecheck.py` against its own text (48 of 48 pass verbatim). The sentence or table row around each quote was then read in the text, and the value, taxon, grade and partial flag were compared with it.

## Verdicts, non-entry-1

| id | entry | taxon / trait | grade, partial | verdict | reason |
|---|---|---|---|---|---|
| oa-13:644 | 13 | Trichoptera / receptor_classes | g, false | confirm | Results sentence verbatim; gene absence graded as a prediction |
| oa-13:940 | 126 | Macrolepidoptera / behaviour_vision | m, false | confirm | Abstract sentence verbatim; a statement about the pooled group |
| oa-13:933 | 120 | Lepidochelys olivacea / sense_chemical | g, false | confirm | 329 of 900 (36.6%) in the quoted sentence; genome prediction |
| oa-13:693 | 30 | Chenopodium album / sense_light_nonvisual | m, false | **requote** | The quote says only that C. album is light-requiring; the value's second half (inhibition under white light plus far-red) is in the next abstract sentence ("All species tested (except Digitalis purpurea) showed a marked inhibition …"), which the quote lacks, so the value says more than the quote |
| oa-13:707 | 42 | Oxalis corniculata / sense_light_nonvisual | m, false | confirm | Abstract sentence verbatim |
| oa-13:680 | 25 | Hypericum perforatum / sense_light_nonvisual | m, false | confirm | Marked cut at the sentence's end; "leaf" is borne out by the Results (leaves, Fig. 4) |
| oa-13:632 | 11 | Gerris lacustris / diel | m, false | confirm | "The first three species are strictly diurnal"; the preceding sentence lists G. lacustris third |
| oa-13:697 | 30 | Amaranthus caudatus / sense_light_nonvisual | m, false | confirm | Clause verbatim; the scan punctuates it as part of the preceding sentence |
| oa-13:870 | 106 | Oedipodinae / interommatidial_deg | g, false | confirm | 2.17° averaged over 98 individuals of three species; marked internal cut |
| oa-13:719 | 52 | Boiga irregularis / acuity_cpd | m, false | confirm | 20′ for both species; logged in arcmin with the unit stated, the conversion left in `note` as BRIEF asks |
| oa-13:690 | 28 | Digitalis purpurea / sense_light_nonvisual | m, false | confirm | Marked internal cuts; growth maxima under R:B 8:2 |
| oa-13:1035 | 196 | Rumex confertus / sense_chemical | m, false | confirm | Abstract sentence verbatim; KNO3 named in the abstract's method sentence |
| oa-13:741 | 66 | Schistocerca gregaria / sense_thermal | m, false | confirm | Figure 5 caption sentence stated in words |
| oa-13:1089 | 275 | Phalaris minor / sense_chemical | m, false | confirm | Abstract sentence verbatim; a living response to residue (point 10a) |
| oa-13:874 | 106 | Locusta migratoria / interommatidial_deg | m, true | **requote** | The quote opens with "… our values …", dropping the sentence's opening clause ("Although no studies have previously examined ΔΦs in North American species of band-winged grasshoppers,"), so it starts mid-sentence. Value 2.4°, m and partial (Burtt and Catton 1954) are right |
| oa-13:736 | 60 | Medicago sativa / sense_light_nonvisual | m, false | confirm | Results sentence verbatim; ranges span the two cultivars |
| oa-13:979 | 145 | Octodon degus / fov_h_deg | m, false | confirm | 166.6° at P5; line-number cut marked; the plane is unnamed and `eye` says so |
| oa-13:685 | 32 | Dipsacus fullonum / sense_thermal | m, false | confirm | Opening clause verbatim, marked cut before "(Table S2)" |
| oa-13:702 | 41 | Schistocerca gregaria / lambda_max_nm | m, false | confirm | Summary sentence verbatim (form note below: a class with no wavelength) |
| oa-13:839 | 88 | Podargidae / eye_movement | m, true | confirm | "frogmouths … as much as 40°; Wallman and Pettigrew 1985"; cited, so partial |
| oa-13:750 | 80 | Asparagus officinalis / sense_thermal | m, false | confirm | Results 3.4.2 sentence verbatim |
| oa-13:1077 | 253 | Milvus migrans / fovea | m, false | confirm | Abstract sentence verbatim |
| oa-13:1050 | 224 | Primula beesiana / sense_chemical | m, false | confirm | Limonene 41.2%; floral volatiles count under point 10a |
| oa-13:1073 | 248 | Chelonia mydas / sense_hearing | m, true | confirm | 60–100 Hz (Ridgway 1969) in a French review; the cut skips a stray "A" |
| oa-13:701 | 41 | Schistocerca gregaria / receptor_classes | m, false | **correct** | The quote lists five receptor *types*, two of which are blue (the DRA blue receptor and the main-eye blue receptor). BRIEF counts spectral classes, so the value should be 4 (UV, blue, green, blue/green broadband) |
| oa-13:1078 | 257 | Falco tinnunculus / behaviour_vision | m, true | confirm | Review sentence verbatim; Viitala et al. 1995 named |
| oa-13:872 | 106 | Oedipodinae / interommatidial_deg | g, false | confirm | Female species means 2.09°–2.21°; trailing cut marked |
| oa-13:679 | 25 | Hypericum perforatum / diel | m, false | confirm | Abstract sentence verbatim (form note below) |
| oa-13:943 | 127 | Oecophylla smaragdina / sense_thermal | m, false | confirm | Results sentence verbatim |
| oa-13:682 | 34 | Hypericum perforatum / diel | m, false | confirm | Abstract sentence verbatim (form note below) |
| oa-13:711 | 44 | Speyeria atlantis / behaviour_vision | m, false | confirm | "At 60 m, no unflashed S. atlantis were successful." |
| oa-13:955 | 139 | Mantodea / interommatidial_deg | m, true | confirm | Review sentence on mantises as a group; cited studies named |
| oa-13:628 | 11 | Panchlora nivea / rhabdom_um | m, true | confirm | Table 3 row verbatim; 114 µm with footnote c; literature-based, so partial |
| oa-13:947 | 137 | Tyto alba / receptor_classes | g, false | confirm | Abstract sentence verbatim (form note below: not a count) |
| oa-13:1033 | 196 | Rumex confertus / sense_light_nonvisual | m, false | confirm | Abstract sentence verbatim |
| oa-13:867 | 103 | Orgyia antiqua / tapetum | m, false | confirm | Abstract sentence verbatim |
| oa-13:829 | 83 | Apis mellifera / rhabdom_um | m, true | confirm | Table 3 row under "Apis mellifera drone", L = 280 µm, Menzel et al. 1991 |
| oa-13:1058 | 233 | Epargyreus clarus / acceptance_deg | m, false | confirm | Half-power beam width about 2° |
| oa-13:748 | 82 | Asparagus officinalis / sense_light_nonvisual | m, false | confirm | Abstract sentence verbatim |
| oa-13:681 | 25 | Hypericum perforatum / sense_light_nonvisual | m, false | confirm | Marked internal cut; 131 µg/g FW under blue light |

## Verdicts, entry 1 (Nowinszky et al. 2022, Table 1)

| id | row | taxon | column | verdict | reason |
|---|---|---|---|---|---|
| oa-13:261 | 172 | Diaphora mendica | C (network) E | confirm | row verbatim, value equal |
| oa-13:274 | 179 | Chelis maculosa | D (Nagytétény) BL | confirm | row verbatim, value BL |
| oa-13:589 | 372 | Xestia xanthographa | C BL | confirm | row verbatim, value BL |
| oa-13:280 | 184 | Lithosia quadra | C E | confirm | row verbatim, value equal |
| oa-13:561 | 356 | Agrotis cinerea | C E | confirm | row verbatim, value equal |
| oa-13:453 | 289 | Oligia latruncula | C E | confirm | row verbatim, value equal |
| oa-13:393 | 253 | Episema glaucina | D E | confirm | row verbatim, value equal |
| oa-13:262 | 172 | Diaphora mendica | D BL | confirm | row verbatim, value BL |

### Table structure against the records

A script parsed every numbered row of Table 1 in the text and matched the 604 Table 1 records to their row and column.

- Rows 1 to 381, none missing. Column C: E 235, BL 123, V 23. Column D: BL 172, "—" 156, E 29, V 22, N 2. Cells holding BL, V or E: 381 + 223 = **604, equal to the 604 records**. Every such cell has one record, no cell has two, and every record's quote is its row verbatim with a value matching its cell.
- E cells are logged (264 records), as point 9 requires. The two "N" cells (rows 148 and 155, column D) are left out, which the legend supports (it defines N only as the serial number).
- Single specimens (point 9): the table gives no specimen counts, only the number of trap pairs (column B, minimum 4) and the Mann–Whitney result, so the single-specimen exclusion cannot be applied from this table and no record breaks it.
- **Duplicate rows (new finding, not in the reader's note).** The chapter says Table 1 holds 378 species, and it prints 381 rows because three rows repeat earlier ones exactly: row 53 repeats row 50 (Scopula rubiginata), row 54 repeats row 51 (Scopula marginepunctata), and row 301 repeats row 234 (Ammoconia caecimacula). 381 less 3 gives the stated 378. The six records of the repeated rows double-count one result each and should be dropped: **oa-13:79, oa-13:80, oa-13:81, oa-13:82, oa-13:473, oa-13:474**. These are a structural fault of the transcription and are not counted in the rate (none was drawn).
- Rows 258 ("Hoplodrina respersa Hbn.", C BL, D V) and 260 ("Hoplodrina respersa Den. et Schiff.", C E) give one binomial two conflicting rows (oa-13:402, 403, 406). The table itself gives no way to say which name is meant, so the desk should hold the Hoplodrina cell until the owner decides.

## Error count and rate

- Non-entry-1: 40 checked; confirm 37, requote 2, correct 1, retract 0. **Errors 3 of 40, 7.5%.** Wrong value, taxon, grade or partial: 1 of 40 (2.5%).
- Entry 1: 8 checked, 8 confirm. **Errors 0 of 8, 0%.** Structure: 604 of 604 cells logged once; 6 redundant records from the chapter's repeated rows.

Errors, by exact record:
1. `docs/views/evidence/oa-13.jsonl:693` (entry 30), requote: add the next abstract sentence, or cut the value to "light-requiring".
2. `docs/views/evidence/oa-13.jsonl:874` (entry 106), requote: quote the whole sentence from "Although no studies …".
3. `docs/views/evidence/oa-13.jsonl:701` (entry 41), correct: `value` 5 to 4 (spectral classes UV, blue, green, blue/green broadband; the DRA blue receptor repeats the blue class).

The non-entry-1 rate is above 5%, so these are the papers with errors whose records the desk may drop (sources from `ci/oa/sources-r1.jsonl`):
- entry 30: Lambton PA 1985, "The photo-inhibition of seed germination and the induction of secondary dormancy" (thesis, no DOI), 6 records.
- entry 41: Schmeling F 2015, "Polarized light vision in the eye of the desert locust, Schistocerca gregaria - An electrophysiological and histological approach", 10.17192/z2015.0394, 6 records.
- entry 106: Duncan AB, Salazar BA, Garcia SR, Brandley NC 2021, "A Sexual Dimorphism in the Spatial Vision of North American Band-Winged Grasshoppers", 10.1093/iob/obab008, 8 records.

The 95% interval on 3 of 40 is wide (roughly 2% to 20%), so the rate sits above the line on a thin margin. A repair of the three records is cheaper than dropping 20 records whose other 17 were not faulted in this draw.

## Fault patterns

1. **The value outruns the quote** (oa-13:693): a value built from two adjacent sentences while the quote carries one. The value is true in the paper; the quote fails to show it.
2. **A leading cut** (oa-13:874): an opening ellipsis that drops a subordinate clause, so the quote starts mid-sentence. `quotecheck.py` passes such a quote, because it checks only that each part is present; a lint for quotes beginning with "…" would catch the pattern.
3. **Receptor types counted as spectral classes** (oa-13:701): a count copied from the paper's wording where BRIEF asks for something narrower.
4. **Trait keys used loosely (not counted, as audit 31 counts no trait-key fault).** Plant melatonin rhythms under `diel` (oa-13:679, 682); plant germination and freezing tolerance under `sense_thermal` (685, 750); a colour class with no wavelength under `lambda_max_nm` (702); an RH2 pseudogenization string under `receptor_classes`, whose key asks for an integer (947). None states anything the paper lacks; each still sits where a consumer of the key would misread it.

Metadata, not counted: oa-13:943 repeats "bioRxiv preprint" in `note`. `ci/oa/sources-r1.jsonl` line 171 (entry 142) carries Crossref's raw `<i>` markup and line breaks inside the title, and line 262 (entry 349, unread) labels a bioRxiv preprint as "accepted manuscript" from its OpenAlex location.

## Source lines checked against the lookups

Drawn with `random.Random(1026)` after the record sample.

`docs/views/sources/oa-none-13.jsonl`, against `/tmp/oar13-lookup.jsonl` (run 24, 370 lines):

| line | lookup entry | check | verdict |
|---|---|---|---|
| 7 | 10 | PLOS S1 Table component; lookup `found` empty | confirm |
| 122 | 195 | lookup `found` empty | confirm |
| 69 | 114 | no DOI, title search; lookup `found` empty | confirm |
| 100 | 167 | two candidate urls match `found`; `failed` gives 200 and short text for both, as the note says | confirm |
| 178 | 301 | candidate urls match; `failed` gives 403 and 200-short, as the note says | confirm |

`ci/oa/sources-r1.jsonl`, against `runs/oa/25-oa-13/lookup.jsonl` on `origin/ci` (159 lines):

| line | entry | check | verdict |
|---|---|---|---|
| 182 | 168 | authors, year, DOI and url match; issue 2 and pages 22–28 match Crossref; `metadata_note` names the first-page fill | confirm |
| 171 | 142 | all fields match Crossref and the Europe PMC url; the title keeps Crossref's markup (metadata row) | confirm |
| 262 | 349 | fields match the posted-content record; journal empty as Crossref gives none; `copy` says accepted manuscript (metadata row) | confirm |
| 221 | 276 | fields match; year 2023 with volume 13 as Crossref gives them | confirm |
| 230 | 289 | fields match; volume and pages listed in `metadata_gaps` | confirm |

## Recommendation

Merge the unit after three repairs and one cut: requote oa-13:693 and oa-13:874, set oa-13:701 to 4, and drop the six repeated-row records oa-13:79–82 and 473–474. Hold the Hoplodrina respersa cell (oa-13:402, 403, 406) for the owner. If the desk applies the 5% rule mechanically instead, drop the 20 records of entries 30, 41 and 106.
