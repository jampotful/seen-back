# OA reading pass, batch oa-14 (26 October 2026)

Prompt: `docs/tracks/prompts/oa-read.md` and `oa-pass.md`, with the desk's launch prompt for oa-14 and the stricter rules learned on oa-13 (`oa-13b-part1.md`, `oa-13b-part2.md`, `oa-13c-recheck.md`, `audit-oa-13.md`, desk-screen point 10). Branch `research/oa-14`, cut from `main` at 7ee4d07f.

## Batch

`docs/tracks/batches/oa-14.json` holds 76 papers: every line of `docs/views/wanted/*.jsonl` on main with a DOI or a full title, less the papers an earlier oa batch covers (oa-1 to oa-12 on main, oa-13 on `origin/research/oa-13`, matched by DOI or normalised title; 1,529 lines), less the papers with evidence on main by DOI (85 lines), with 3 duplicate wanted lines kept once. Ten of the 76 have no DOI and were looked up by title. The order is their rank in `docs/views/wanted-merged.csv`. `ci/oa/list.jsonl` gains the 76 oa-14 lines.

## Fetch

- Run branch `run/oa/read-r14` (from main): own public key, the 76 oa-14 lines, the batch file, matrix `[oa-14]`, and library proxy hosts (ezproxy, libproxy, elogim, idm.oclc.org, proxy.) added to the banned list in `ci/oa/oa.py` so that the job could not open one. No read url is on a proxy, ResearchGate or academia.edu host.
- The job returned as `runs/oa/31-oa-14` (success). 36 texts came back; all 36 decrypted and matched their checksums.
- `ci/oa/sources-r1.jsonl` gained 36 oa-14 lines from the lookup's Crossref objects (HTML tags stripped from 4 titles). Authors, year or journal were filled from the papers' own first pages for entries 21, 26, 29, 51, 56, 57 and 59, each with a `metadata_note`.
- `docs/views/sources/oa-none-14.jsonl` holds 42 lines: the 40 papers with no text, and entries 28 and 43, whose copies are Springer abstract pages behind a subscription.
- The decrypted texts stay in `/tmp/oa14key/txt` on the build machine for the recheck unit. No paper text, PDF, XML, .bin or key is in the repository.

## Counts

- Papers read in full: 34 (every copy, in lookup order, entries 3 to 75). Abstract pages: 2 (entries 28 and 43).
- Records logged: 123 in `docs/views/evidence/oa-14.jsonl`. Grades: m 113, g 10, i 0. Partial: 30 (27 cited values, 3 abstract values from entry 43).
- Records by trait: lambda_max_nm 49, sense_chemical 23, sense_light_nonvisual 23, polarization 8, behaviour_vision 7, diel 4, receptor_classes 2, and one each of sense_thermal, cff_hz, acuity_cpd, ommatidia_count, photoreceptor_tiers, oil_droplets and photoreceptor_mix.
- `check.py` reports 0 problems; every quote passes `quotecheck.py` against its own text (verbatim, or as a table row of the layout text for entries 64 and 75).

## Papers with no record (`"records": 0`), and why

- Excised tissue or cultures, which the oa-14 rules leave out of plant sense_chemical: entry 13 (shoot explants in vitro), 20 (detached, halved leaves floated on jasmonic acid), 26 (BY-2 and grapevine cell lines; thesis), 29 (detached leaves; preprint), 36 (detached leaves in glass jars), 48 (cell suspension cultures).
- Essential oils from collected inflorescences (point 10a): entry 53.
- No BRIEF trait: entry 32 (guard-cell photosynthetic efficiency and stomatal responses to humidity), 34 (pink-cell mutation counts in Tradescantia stamen hairs), 51 (flowering months, no time of day), 57 (removal of toluene and xylene by foliage plants).

## Notes for the audit

- Entry 4 (Campanula floral scent): the Methods say "fresh inflorescences" were enclosed, without saying they stayed on the plant, so no scent record was logged; the three records are the bee's behaviour and antennal sensitivity.
- Entry 9 is a line-numbered author manuscript; each … in its quotes marks a line number the text inserts.
- Entries 33 and 40 are OCR texts with columns run together; their quotes mark the other column's words with …, as each note says.
- Entry 64: Table 3 (MSP λmax of four colubrines) is logged row by row as table rows; the PDF text prints ± as "+" and = as "¼", and each note reads the cell out. Table 2 (compiled from earlier studies) gives only the Telescopus fallax row (diel and photoreceptor types, partial).
- Entry 75: Table 1's λmax column is logged row by row (31 records); values with a source footnote (b, d, f, g, h, i, k) are partial and name the source. The Asterocampa value (footnote c, measured from A. leilia) is quoted from the Results sentence because the table row names A. celtis. Apodemia mormo carries footnote j (Bernard et al. 1988), while the Results report its two pigments as this study's measurements; both records are unflagged and the note says so.
- Entry 56: only the abstract's dipterocarp sentence is logged (graded g). The 165-species screening table (leaf isoprene and monoterpene emission, extrafloral nectaries) is not logged species by species, since constitutive leaf emission is a borderline case for point 10a's "volatiles as a signal".
- Entry 59: the lion's 13.42 cpd is a value the paper took from Melin et al. 2016 to filter its stimuli; it is logged partial with that source named. The other simulation acuities (7.84 and 4.60 cpd), one of them an average the authors made, are not logged.
- Entry 63: the cited trichromacy sentence names its source by reference number only, because the Europe PMC XML holds no reference list.

## Next

1. Recheck the 123 records against `/tmp/oa14key/txt` (desk's recheck unit).
2. Decide whether entry 56's Table 1 and entry 64's Table 2 should be logged species by species.
3. The 40 papers without a copy and entries 28 and 43 stay on the wanted lists for the owner's library.
