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

## Entry 1 and point 10(c): records kept under spectral_range_nm

The coordinator asked on 26 October that the 604 light-trap records of entry 1 be moved to a behaviour trait under desk-screen point 10(c). I re-read points 9 and 10(c) on `main` before changing anything. Point 9 says a light-trap table comparing catches at lamps of different spectra "counts under spectral_range_nm for every species it lists", an "E" row included, and names this table (canon-22). Point 10(c) moves only activity comparisons under lamps (Briolat et al. 2026) to behaviour and ends "point 9's light-trap catch tables still count". The 604 records therefore stay under spectral_range_nm, and no corrected file was written. If the owner reads 10(c) the other way, a script can rewrite the trait on the lines whose source DOI is 10.5772/intechopen.102718 and whose `where` names Table 1 before the branch is merged. None of the other papers has the same fault: the two other lamp comparisons (entries 126 and 132) pool species and are logged as behaviour_vision.

## Second session (26 October, after the coordinator's message)

- Papers read: 50 more, entries 171 to 294 in lookup order (positions 71 to 120 of the 159). Entries 296 onward (39 papers) are unread. The private key and the decrypted run 25 texts were still on the machine.
- Records added: 66 (m 54, g 12; partial 14). Totals for the branch: 120 papers read, 1,095 records, m 1,016, g 79, partial 180.
- Papers with no BRIEF measurement in this session: 17 (`"records": 0` lines), mostly plant chemistry of extracts or harvested tissue (desk-screen point 10a), gene-function work, pollination studies with no sensory value, and two copies that held no text (entry 197, a truncated portal abstract; entry 219, front matter and references of a book).
- Entries 242 and 243 are repository pages with abstracts only. Entry 242 (an image-analysis method) has no value; entry 243's four tapetum records carry `access: abstract` and `partial: true`, and neither has a sources line, as earlier readers did for abstract-only copies.
- Preprints and a Turkish journal paper (entries 210, 236, 273) had the journal string filled from their own first pages, in the records and in `ci/oa/sources-r1.jsonl`.

## Next

1. Read entries 296 to 370 of the lookup that have a free copy (39 papers), in lookup order, from the same decrypted run 25 texts.
2. Log entry 154's Chapter IV SWS1 table and entry 113's Table 6-1 if the desk wants them.
3. Fetch the Dryad CSV files of entries 9 and 12, which hold λmax values for many species.
