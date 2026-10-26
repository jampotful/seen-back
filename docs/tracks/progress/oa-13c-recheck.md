# oa-13c: whole-unit recheck of the oa-13c reading (26 October 2026)

Scope: all 137 records of `docs/views/evidence/oa-13c.jsonl` on `origin/research/oa-13c` at 30bd8f3c (21 papers with records, lookup entries 304 to 370). Each record was matched to its text through `/tmp/oar13-lookup.jsonl` by DOI (by title for the two theses without a Crossref DOI), run through `python3 -I tools/views/quotecheck.py` against `/tmp/oar13key/txt/oa-13-<entry>.txt` (137 of 137 passed verbatim before any fix), and read against the sentence or table row around its quote, and for compiled tables against the rows above it. Rules: `oa-audit.md`, `oa-read.md`, audits 31 and 39, the oa-13b part 1 and part 2 rechecks, desk-screen points 9 and 10, and BRIEF. The decrypted run 25 texts were read in place; no key was made, no build job ran, and no paper text, PDF or key enters this branch. The branch's own evidence file is untouched.

## Output

`docs/views/evidence/oa-13c-checked.jsonl`: 135 records (every record except the two retracted), `"unit": "oa-13c"`, the `source` object untouched, with the fixes below applied. `python3 -I tools/senses/check.py` reports 0 problems on it; all 135 quotes pass `quotecheck.py` verbatim, and no quote opens with a cut.

## Counts

| verdict | records |
|---|---|
| confirm | 118 |
| requote | 15 |
| correct | 2 |
| retract | 2 |
| **all** | **137** |

Errors (requote, correct, retract): 19 of 137, 13.9%. Wrong value, taxon, grade or partial flag (correct and retract only): 4 of 137, 2.9%. Fourteen of the fifteen requotes come from one table (entry 361, Table 4) and one word ("peak").

## Verdicts other than confirm

Line numbers are those of `oa-13c.jsonl` at 30bd8f3c.

| line | entry | taxon / trait | verdict | reason and fix |
|---|---|---|---|---|
| 41 | 337 | Aedes aegypti / behaviour_vision | requote | the cut, which the note said removed only line numbers, also removed 'and emitting their wingbeat sound', so the value set flashing light alone against constant light with sound; both assemblies emitted the sound. Quote now carries the sound clause (cut to 40 words) and the value names both assemblies' sound |
| 69 | 361 | Laodelphax striatellus / diel | requote | value called the cell 'peak phototactic activity'; the column is 'Phototactic rhythm of pests' and gives a time window. Value trimmed to 'phototactic rhythm at lamps: 18:00-19:00' |
| 70 | 361 | Sogatella furcifer / diel | requote | as 69 |
| 71 | 361 | Cnaphalocrocis medinalis / diel | requote | as 69 |
| 72 | 361 | Spodoptera litura / diel | requote | as 69 |
| 73 | 361 | Holotrichia perllela / diel | requote | as 69 (the review's own text gives this species 'mainly active between 19:00 and 21:00', against the table's 19:00-20:00, so the table gives a window that the prose does not call a peak) |
| 74 | 361 | Conogethes punctiferalis / diel | requote | as 69 |
| 75 | 361 | Ostrinia furnacalis / diel | requote | as 69 |
| 76 | 361 | Mythimna seperata / diel | requote | as 69 |
| 77 | 361 | Ectropis obliqua / diel | correct | the table prints 'Ectropis Obliqua Hypulina Wehrli'; 'Hypulina' is the subspecies epithet and was dropped with the authority. Taxon now Ectropis obliqua hypulina (subspecies), as line 86 of the same file already has it; value trimmed as 69 |
| 78 | 361 | Anomala corpulenta / diel | requote | as 69 |
| 79 | 361 | Euproctis pseudoconspersa / diel | requote | as 69 |
| 80 | 361 | Ectropis obliqua / diel | correct | as 77 |
| 81 | 361 | Anomala corpulenta / diel | requote | as 69 |
| 82 | 361 | Spoladea recurvalis / diel | requote | as 69 |
| 83 | 361 | Anomala corpulenta / diel | requote | as 69 |
| 84 | 361 | Empoasca flavescens / diel | requote | as 69 |
| 130 | 363 | Chrysocyon brachyurus / lambda_max_nm | retract | the abstract says 'the analyzed species' share the AHYTA profile at all five LWS tuning sites, but Results 6.1.2 says the five sites were sequenced in only two wild canids, Lycalopex vetulus and Cerdocyon thous; for C. brachyurus only exons 3 and 4 were sequenced (exon 5 not, samples exhausted), so the five-site prediction of 555 nm was not made for it |
| 131 | 363 | Speothos venaticus / lambda_max_nm | retract | as 130: exons 4 and 5 were amplified but the sequencing quality was too low for analysis (Results 6.1.2) |

Notes improved without a verdict (not counted): line 2 now names the source of the 'classical' 230 Hz flicker-fusion figure as the paper's reference 50, an electroretinogram estimate (Results); lines 53 and 54 name Ridgway et al. (1969) and line 55 Moein Bartol and Ketten (2006), the cited studies their notes only pointed to, and line 55 gains its condition (underwater sound stimuli).

## Fault patterns

1. **A gloss on a table column (14 records, 69 to 84 less 77 and 80, plus the two corrections).** Every Table 4 cell of entry 361 was logged as a 'peak', where the column gives a phototactic rhythm window and the review's prose sometimes gives a different window for the same species (Holotrichia perllela, 19:00 to 21:00 against the table's 19:00 to 20:00). It is the oa-13b pattern of a value carrying a word the quote lacks, repeated down a table.
2. **The abstract claims more than the Results (130, 131).** A thesis abstract states a five-site LWS prediction for all five canids; its Results say the five sites were read in only two wild species and the dogs. A record taken from an abstract needs the Results checked for the species it names.
3. **A cut described as harmless that removes a condition (41).** The note said the cuts marked only line numbers; one of them removed the clause that both lamp assemblies emitted sound, and the value then contrasted light alone with light and sound.
4. **A subspecies epithet dropped as an authority (77, 80).** 'Hypulina Wehrli' was read as authority text in two table rows, while a prose record from the same paper (86) kept the subspecies.

Faults the batch's sample flagged and that this unit does not repeat: no quote opens mid-sentence or with a cut, no author-assumed value is logged (the reader left out entry 370's assumed f-number), no plant chemistry of excised tissue is logged (point 10a), and receptor counts follow the paper's own counts. The point-object acuity values in entry 369's Table 3 are the review's stated conversion of a measured visual angle (caption note (a)), named in each note, and are confirmed.

Not counted, as in the earlier rechecks: trait keys used loosely (a qualitative 'limited spectral range with peak sensitivity at approximately 500 nm' for Dermochelys coriacea under `spectral_range_nm` at 64, a gene-loss string under `receptor_classes` at 29, a feeding choice presumed chemical under `sense_chemical` at 26, graded g); review notes that name a cited study by reference number (entries 311, 349 and 369). Entry 335's abstract pools both moths' peaks (360 nm and 500 to 550 nm); its Results give Helicoverpa armigera a secondary peak near 500 nm and Mamestra brassicae a main peak at 500 to 550 nm, both within the logged range, so lines 33 to 37 stand. Lamp comparisons follow points 9 and 10c: the pooled catches of entry 359 (67, 68) and the phototaxis wavelengths of entry 361 (85 to 88) are under `behaviour_vision`, and no light-trap catch table is logged in this unit.
