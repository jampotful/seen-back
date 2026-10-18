# oa-2 reading pass, reader A (18 October 2026)

Prompt: `docs/tracks/prompts/oa-read.md`. Reading branch `agent/oa-read-a`; fetch branch `run/oa/read-a` (oa job run 7, batch oa-2). Every text's sha256 in run 7 equals run 1's, so the sources lines keep the prompt's "control-room oa job run 1" wording. The private key stayed in `/tmp/oa-a` on the reading machine (a letter-specific folder, so readers sharing a machine cannot overwrite each other's key) and was never committed or printed. No paper text, PDF, XML, `.bin` or `.pem` file was staged.

## Papers read (batch oa-2, in launch order)

| entry | paper | copy read | records | m | g | i | partial |
|---|---|---|---|---|---|---|---|
| 2 | Karl et al. 2018, caiman retinal ultrastructure | PMC HTML, NIH author manuscript | 30 | 7 | 22 | 1 | 23 |
| 13 | Ritland and Ausprey, avian eye morphology (Dryad dataset) | Dryad landing page and README | 0 | | | | |
| 22 | Johnson and Rutowski 2022, ant eyes | PLoS ONE PDF (plain and layout text) | 63 | 31 | 32 | 0 | 47 |
| 24 | Toomey et al. 2016, avian C-type oil droplets | Europe PMC XML | 18 | 2 | 16 | 0 | 13 |
| 26 | Klećkowska-Nawrot et al. 2026, felid eyes | Europe PMC XML | 41 | 35 | 6 | 0 | 11 |
| 30 | Hunt et al. 2009, review | PMC HTML (published version) | 178 | 69 | 79 | 30 | 178 |
| 31 | Jacobs 2009, review | PMC HTML (published version) | 111 | 3 | 98 | 10 | 111 |
| 34 | Nilsson 2013, review | Europe PMC XML | 59 | 4 | 55 | 0 | 59 |
| | **total** | | **500** | **151** | **308** | **41** | **442** |

Traits: lambda_max_nm 171, receptor_classes 64, diel 54, tapetum 43, colour_vision 25, eye_type 25, eyes_count 24, oil_droplets 19, sense_light_nonvisual 14, eye_role 13, filter_pigments 11, pupil_shape 7, behaviour_vision 6, acuity_cpd 5, fov_h_deg 5, fovea 4, and one or two each of interommatidial_deg, polarization, binocular_deg, absolute_sensitivity, depth_cue, motion, acceptance_deg and sense_touch.

## Papers with no measurement

- Entry 13: the free copy is the Dryad landing page with its README. The data file it describes (`Ritland_eyes_raw_FINAL.csv`, eye sizes of 3,475 bird species) was not fetched, and eye size is not a BRIEF trait. Its sources line says so, with `"records": 0`.

## Parts not read, and why

- Entry 22: the Dryad data files and the S1 Table (DOCX) were not fetched. Per-species interommatidial angles, eye parameters and visual field spans are printed only inside the images of Figs 10 to 12, so only the text's range (3.5 to 7°), maxima (128° and 121°) and group means (98.8° and 73.0°) were logged.
- Entry 24: Supplementary files 1 and 2 (the species tables of retinal apocarotenoids and cone parameters) are not in the Europe PMC XML.
- Entry 26: the XML carries no reference list and no Supplementary Table S1, so cited studies are named by their reference numbers.
- Entry 2: the copy is an NIH author manuscript; every record's note says so.

## Grading

The control room's correction of 18 October is applied to every line this branch adds: a cited or compiled value on the record's own named species is `m` with `partial: true`; groups, genera, presumptions ("suggested", "generally assumed") and common-name-only taxa stay `g`; values the paper infers from genes, sequences or pigment complements are `i`, with the inference in `method`. Common-name-only species (rat, humans, polar bear and others) and undescribed ant species stay `g` because the lint's species check needs a formal binomial; their notes say why.

## Checks

`quotecheck.py`: 500 of 500 verbatim. `oa_lint.py` with `--text` on each paper and `--since-main HEAD`: 500 records, 0 faults. `check.py` passes on `docs/views/evidence/oa-2.jsonl`.

## Notes for the audit

- Entry 22's Table 1 is scrambled in the plain text, so its rows are quoted from the layout text, with the genus heading, joined across the row's two printed lines; `where` says so.
- Entry 30's two λ sentences that begin with the symbol λ (section 3(a)(ii) and (iii)) are quoted with the preceding sentence, because the lint reads a lower-case first letter as a mid-sentence start.
- `pupil_shape` is logged as a new trait (7 records): BRIEF's table has no pupil key, the engine has a `pupil` field, and earlier logs use this key.
- `eyes_count` carries strings where a paper reports the presence of ocelli or an eye arrangement rather than a count; each note says so.
