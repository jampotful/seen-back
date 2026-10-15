# Precision audit 9, 15 October 2026

Three parts. (a) A random sample of 20 evidence records, each opened at its source and checked for value, grade, partial flag and a verbatim quote: 10 from sweep-66 to sweep-69, 8 from oa-6 (one per source paper, skipping lines superseded by recheck-7 or recheck-8) and 2 from oa-3. (b) Four lines of `docs/views/wanted/sweep-66.jsonl` to `sweep-69.jsonl`, checked for authors, year or DOI that no opened page confirms. (c) The batch recheck that an error rate above 5% calls for.

Method as in audits 6 to 8: each source opened with WebFetch and asked first whether the exact quote string appears, then for the page's own sentence in consecutive pieces of at most about 125 characters, with split points in `where`; corrected quotes are 40 words or fewer. Verdicts: `confirm`, `requote`, `correct`, `retract`, `unverifiable`. Typographic differences count as `confirm`; a change to the partial flag counts as `correct`. A value carried from a review or compilation table is a secondary citation and carries `partial: true` with the primary named, as audits 7 and 8 ruled. Corrections are in `docs/views/recheck/recheck-9.jsonl` in the recheck-5 schema. No evidence file and not `docs/views/audit/ALL.jsonl` was edited.

## Part (a): random sample

sweep-68 has no evidence file. sweep-66, 67 and 69 hold 18 records; two were drawn from each and four more from the remainder (Python `random`, seed 20261015). oa-6 lines were shuffled with the same generator and the first line from each new source paper was kept until there were eight; two oa-3 lines followed.

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
| sweep-66:2 | Chrysopelea paradisi / acuity_cpd | m | confirm | clause verbatim on the SICB page; the sentence continues ", and were observed chasing stimuli rotating at 48 deg/s"; the page prints "Friday, Jan. 6" and no year, as the record says |
| sweep-66:7 | Ceratosolen gravelyi / f_number | m | confirm | verbatim, 3.3 Optical Properties; calculated by the authors from their own measurements (section 2.4) |
| sweep-67:4 | Python bivittatus / pupil_shape | m | confirm | verbatim in the Figure 1 caption after "(A)"; no orientation stated |
| sweep-67:7 | Spermophilus beecheyi / acuity_cpd | m | correct | phrase verbatim, but the sentence ends "... particularly high temporal sensitivity [6]." (Jacobs, Blakeslee, McCourt and Tootell 1980, J Comp Physiol 136: 291-299). The note's "this sentence cites no measurement" is wrong; secondary, now `partial: true` |
| sweep-69:1 | Tetragonula carbonaria / acuity_cpd | m | confirm | verbatim in Results (pERG), same split |
| sweep-69:4 | Pelodiscus sinensis / receptor_classes | g | confirm | verbatim; the sentence ends "(Emerling, 2017b)"; already `partial: true` with the primary named |
| sweep-66:1 | Chrysopelea ornata / acuity_cpd | m | confirm | as sweep-66:2 |
| sweep-67:6 | Philodryas patagoniensis / pupil_shape | m | confirm | verbatim on Wikipedia, no citation on the sentence; already `partial: true`. An encyclopedia sentence graded `m` is weak, left for the desk |
| sweep-66:5 | Ceratosolen gravelyi / interommatidial_deg | m | confirm | verbatim, the second piece of a sentence in 3.2 that opens "The average length of an ommatidium is 54.3 ± 4.3 µm" |
| sweep-67:5 | Iberolacerta cyreni / lambda_max_nm | g | confirm | Table 4 row verbatim; the Discussion says all 30 sequenced species carry the UV substitutions |
| oa-6:648 | Columba livia / lambda_max_nm | m | correct | verbatim, but the sentence cites the P400 label to Yokoyama et al. 1998 (FEBS Letters 423: 155-158); a review value without `partial: true`, now partial with the primary named |
| oa-6:310 | Falco peregrinus / cff_hz | m | unverifiable (flag corrected) | the S10 spreadsheet could not be opened (PLOS fetch error; Europe PMC 429). The value matches the primary's press release (Lund University: "can register 129 Hz (blinks per second) provided the light intensity is high"). A compilation value without `partial: true`; flag set from the record's own provenance |
| oa-6:348 | Dasyatis sabina / binocular_deg | m | confirm | verbatim in the abstract of the FAU lab copy (elasmolab.fau.edu/pdfs/mk08.pdf), "72°" for "72 degrees "; Europe PMC answered 429 |
| oa-6:494 | Spheniscus humboldti / binocular_vertical_extent_deg | m | unverifiable | Table 1 of Martin and Katzir 1999 is an image, and the image URL was refused. A review table row without `partial: true`; primary not known, so no row written |
| oa-6:10 | Strix aluco / optic_axes_divergence_deg | m | unverifiable | Europe PMC and PubMed answered 429; ScienceDirect refused |
| oa-6:388 | Papilio xuthus / filter_pigments | m | correct | verbatim (the sentence opens "Additionally, "); a review statement whose next sentence cites Arikawa and Stavenga 1997 and Arikawa 2003; now `partial: true` with those named |
| oa-6:352 | Pseudemys scripta elegans / wavelength_discrimination_min_nm | m | unverifiable | Europe PMC 429; PubMed fetch error |
| oa-6:14 | Palaemonetes vulgaris / polarization | m | unverifiable | Europe PMC 429; PubMed fetch error; already `partial: true` |
| oa-3:193 | Apis mellifera / cff_hz | g | unverifiable (flag corrected) | S10 not reachable; a compilation value with the primary named in the note, now `partial: true` |
| oa-3:82 | Mugil cephalus / cff_hz | g | unverifiable (flag corrected) | as oa-3:193. Flag: the method reads "ERG" while the primary (Bullock et al. 1990) is on tectal visual evoked potentials, and the conditions give 10^5-10^6 lux while the quoted row reads "Unknown \| NA" |

**Rate: 3 errors in 13 verifiable records, 23%** (7 unverifiable). By part: sweeps 1 of 10 (10%); oa-6, 2 of 3 opened. All three errors are one kind: a value the source cites from elsewhere, filed without `partial: true`. The quotes themselves are clean (13 of 13 on the page). Three of the unverifiable records (oa-6:310, oa-3:193, oa-3:82) carry the same flag defect on their face, and rows were written for them; they are not counted in the rate.

## Part (b): wanted lines

Four of the seven lines were drawn (seed 20261015).

| line | result |
|---|---|
| sweep-66:2 | **not confirmed.** The book (Wild and Exotic Animal Ophthalmology, Volume 2: Mammals, 2022, DOI 10.1007/978-3-030-81273-7) exists, but neither the Springer book page nor two catalogue pages list chapters, so the chapter title, its authors (Mowat FM, Peichl L) and pages 181-214 rest on no opened page. The desk should mark the authors and pages unconfirmed |
| sweep-67:2 | confirmed: "Ophthalmology of Serpentes: Snakes", Nicholas J. Millichamp, 2022, pp. 231-269, DOI 10.1007/978-3-030-71302-7_13 (OUCI record); the reference list names Python regius, P. molurus, Boa constrictor and Epicrates, as the line says |
| sweep-69:2 | confirmed: Walls GL, 1942, Cranbrook Institute of Science, Bloomfield Hills (Internet Archive record) |
| sweep-68:1 | names no authors, year or DOI ("authors not read", year 0) and says they are unconfirmed; passes |

Also opened: sweep-69:1 (Bage 1912, Q J Microsc Sci 57: 305-328, BHL part 201144), confirmed.

## Part (c): batch recheck

The errors came from sweep-67 and from two oa-6 source papers, so those were rechecked whole.

- **sweep-67** (7 records): 67:1, 67:2 (Peichl et al. 2022, Lynx) and 67:3 (Silveira et al. 2018, UNESP repository) confirmed, the first with "shortwavesensitive" broken at a line end. No further error.
- **Bowmaker, Wilkie and Hunt 1999** (85 further live records, oa-6:547 to 650) and **Lu and Kronforst 2026** (85 further, oa-6:361 to 446): every record is a review value without `partial: true`. All 170 are corrected to `partial: true`, with the citation the review prints at that sentence named in the note. The citations were read with the fetch tool in a few bulk passes, not one by one, so a name could be misplaced: Lu and Kronforst's sentence "as many as 15 distinct spectral sensitivities" (Graphium sarpedon) came back as Pirih et al. 2022, where Chen et al. 2016 would be expected. Bowmaker Table 1 rows (oa-6:547 to 604) name no primary, because the footnotes are in the table image, which was not readable; their quotes were not re-read for the same reason. Every Lu and Kronforst quote and every Bowmaker prose quote was found on the page.

Not acted on, the same defect at larger scale:

- Lafitte et al. 2022 S10 rows: 310 live oa-6 records and 289 live oa-3 records lack `partial: true` (303 and 283 of them name the primary in the note). The S10 could not be opened, so no batch rows were written beyond the three sampled; the flag can be set mechanically once the desk agrees.
- Martin and Katzir 1999 Table 1: 97 oa-6 records of the same shape; the table is an image.
- About 30 recheck-7 `correct` rows that rest on the Bowmaker review (the "Aves" and "Gallus gallus" taxon fixes of oa-6:605 to 625) also lack `partial: true`.
- sweep-66:3 (Leptailurus serval, pupil_shape) reads Banks et al. 2015's character matrix; it is the authors' classification, and whether it was compiled from earlier sources was not checked.

## Rows written

`recheck-9.jsonl`: 176 rows, all `correct`. Sample: sweep-67:7, oa-6:648 and oa-6:388 (counted), and oa-6:310, oa-3:193 and oa-3:82 (flag only, uncounted). Batch: 170 partial-flag rows for the Lu and Kronforst and Bowmaker records.

## Blocked pages

Europe PMC REST and PubMed answered 429 for the abstract records (oa-6:10, 348, 352, 14); the PLOS S10 file returned a fetch error; the Martin and Katzir Table 1 image and several Springer, Crossref and Semantic Scholar URLs were refused on permission; journals.biologists.com redirected to its crawl-prevention page. The shell has no route to these hosts.

## Patterns (this run)

1. Quotes are clean again (13 of 13). Every error is a secondary value without `partial: true`, the shape audits 7 and 8 found in sweeps, here at the scale of whole reviews.
2. The Codex round (oa-6, oa-3) logged review and compilation values as if read at the primary. After this run about 700 live records still lack the flag (Lafitte 599, Martin and Katzir 97), on top of the 176 corrected here. The oa-pass prompt asks for `partial` only on abstract-level records, so the round followed its own instructions; the desk needs to settle the rule for review-read records and apply it in one pass.
3. One sweep note asserts the absence of a citation that the sentence carries (sweep-67:7); reading the sentence to its end catches it.
