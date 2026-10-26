# OA reading pass, batch oa-13 (26 October 2026)

Prompt: `docs/tracks/prompts/oa-read.md`, with the desk's launch prompt for oa-13 (reading unit oa-13-read). Branch `research/oa-13-read`, cut from `main`.

## Setup

- The run branch `run/oa/read-r13` (from `main`) carried a new public key, the 159 oa-13 lines of `ci/oa/list.jsonl` whose run 24 lookup has a free copy, the oa-13 batch file and a matrix of `[oa-13]`. The job returned as `runs/oa/25-oa-13` (success). All 159 texts decrypted and matched their checksums; none failed.
- `ci/oa/sources-r1.jsonl` gained 159 oa-13 lines built from the Crossref records of the lookup. `docs/views/sources/oa-none-13.jsonl` holds the 211 entries without a free copy (124 with no open location or no title match, 87 with an open location that the job could not retrieve, each with its HTTP statuses and candidate urls).
- Every record passed `oa_lint.py --text`, `quotecheck.py` and `check.py` against its own text before it was appended. No paper text, PDF, XML, .bin or key file is in the repository.

## Counts

- Papers read: 70, the first 70 of the 159 in lookup order (entries 1 to 170). Entries 171 onward are unread.
- Records logged: 1,029. Grades: m 962, g 67, i 0. Partial: 166.
- Papers with no BRIEF measurement (sources line with `"records": 0`): 9, namely entries 9 and 12 (Dryad landing pages; the CSV files were not fetched), 90 (essential-oil chemistry and phytotoxicity of distilled oils, not counted under desk-screen point 10a), 93 (metabolomics of harvested spears), 102 (general histology), 123 (membrane potentials only), 128 (taxonomic eye measurements), 158 (repository landing page, no text) and 161 (review with no species values).
- Records by trait, largest first: spectral_range_nm 611, lambda_max_nm 49, sense_light_nonvisual 46, behaviour_vision 43, rhabdom_um 40, interommatidial_deg 40, f_number 26, diel 23, receptor_classes 19, eye_movement 19, polarization 18, sws1_opsin_type 14, others 81.

## Notes for the audit

- Entry 1 (Nowinszky et al. 2022, Table 1) gives 604 spectral_range_nm records, one per species for the national network (column C) and one more per species for Nagytétény (column D) where that column holds BL, V or E, as desk-screen point 9 reads light-trap catch tables. Rows 148 and 155 hold "N" in column D, which the legend does not define, so only their column C record is logged. Five cited values from the chapter's Introduction are partial.
- Entries 83, 112, 147 and 151 log table rows. Entry 147 skips species with fewer than 5 individuals over three years and Maniola jurtina, whose row has a blank cell. Entry 112 quotes stop before a final dash cell that the text joins to the next line.
- Two-column or line-numbered texts (entries 53, 109, 145, 157) are quoted with "…" at column breaks, line numbers or unreadable control characters where no words are left out; each record's note says so.
- Theses and preprints without Crossref metadata (entries 30, 41, 52, 80, 82, 88, 95, 101, 108, 113, 127, 145, 146, 154) had authors, year and the thesis or preprint string filled from their own first pages, in both the records and `ci/oa/sources-r1.jsonl` (`metadata_note`). Entry 14's Crossref pages read "0-0" and entry 168's journal lacked its issue; both were filled from the papers' first pages.
- sws1_opsin_type (entries 151, 154) follows the earlier oa-4 key and is graded g because the class is predicted from sequence.
- The 134-species SWS1 comparison of entry 154 (Chapter IV) and the compiled Table 6-1 of entry 113 were not logged species by species; both would add many records.

## Next

1. Read entries 171 to 370 of the lookup that have a free copy (89 papers), in lookup order, from the same decrypted run 25 texts.
2. Log entry 154's Chapter IV SWS1 table and entry 113's Table 6-1 if the desk wants them.
3. Fetch the Dryad CSV files of entries 9 and 12, which hold λmax values for many species.
