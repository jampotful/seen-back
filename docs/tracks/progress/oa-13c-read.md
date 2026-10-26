# OA reading pass, unit oa-13c (26 October 2026)

Branch `research/oa-13c`, cut from `origin/main`. This unit reads the oa-13 papers left unread by `research/oa-13-read`: the 39 entries after entry 294 whose run 25 lookup has a free copy (entries 296 to 370). The texts are the decrypted run 25 texts (`runs/oa/25-oa-13`, branch `run/oa/read-r13`), still on the reading machine with its key. The older oa-13 evidence file is not touched.

## Setup

- `ci/oa/sources-r1.jsonl` gains the 159 oa-13 source lines from `research/oa-13-read`, including the metadata that unit filled from first pages. This unit fills four more the same way (entries 337, 349, 362, 363), each with a `metadata_note`.
- Records: `docs/views/evidence/oa-13c.jsonl` (unit oa-13c). Sources lines: `docs/views/sources/oa-13c.jsonl`.

## Checks added after audit oa-13b (parts 1 and 2 on `main`)

Before each append, besides `oa_lint.py --text`, `quotecheck.py` and `check.py`:
- A script stops the append when any quote opens with a cut.
- Each value was read against its quote and trimmed to the quote's words. Facts from a neighbouring sentence go in `note` or `method`, never in `value`.
- Values the authors assume or derive from an assumption are not logged. For example, entry 370's f-number of 0.95 rests on an assumed focal length of 0.6 × axial length, so it is left out.
- Plant chemistry of extracts, distillates or harvested tissue is not logged (point 10a): entries 296, 297, 322, 328 and 331.
- Counts follow the paper's own count. Where a paper names only a group or a presumed channel, the record is graded g.

## Counts

- Papers read: 39 (all remaining). One of them (entry 326) is an abstract-only repository page: its two records carry `access: abstract` and `partial: true`, and it has no sources line. Sources lines: 38.
- Records: 137. Grades: m 125, g 12, i 0. Partial: 99, mostly compiled or cited values from reviews (entries 310, 311, 343, 361, 369).
- Papers with no BRIEF measurement (`"records": 0`): 19. They are food and plant-extract chemistry, taxonomy, gene-duplication surveys without species values, a model of the zebra-stripe illusion and a fisheries vision model whose inputs are not given in the text. One is a moth eye-size thesis (entry 356). Entry 303 is a review whose values sit in columns interleaved with tables, so no quote could be taken whole. Entry 365's Cry1 labelling is logged as nothing because the paper calls a magnetic role only compatible with its result.
- Largest traits: lambda_max_nm 28, behaviour_vision 24, diel 17, acuity_cpd 16, interommatidial_deg 11, acceptance_deg 9, binocular_deg 8, fov_h_deg 6.

## Notes for the audit

- Lamp comparisons follow desk-screen points 9 and 10(c). Entries 335 (green-light suppression of activity), 359 (pooled catches at three LEDs) and 361 (phototaxis wavelengths and arrival hours from a review) are logged as behaviour_vision or diel, never as spectral_range_nm. Entry 359's species-by-lamp counts are in supplementary tables that were not read.
- Entry 361's Table 4 rows are logged only where a row names one species and one time window. Rows that join two windows into one cell (for example "18:00-19:005:00-6:00") are left out.
- Entries 323 and 337 are an accepted manuscript and a preprint with line numbers in the text. Their quotes mark each line break with a cut, and the note says so.
- Entry 369's Table 1 and Table 3 rows are review compilations, so they are partial and name the row's reference.

## Next

All 159 oa-13 papers with a free copy are now read across `research/oa-13-read` and `research/oa-13c`. Open leads are entry 359's supplementary species tables, entry 154's Chapter IV SWS1 table and entry 113's Table 6-1 (both on the older branch), and the Dryad CSV files of entries 9 and 12.
