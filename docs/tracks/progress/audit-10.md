# Precision audit 10, 15 October 2026

Four parts. (a) A random sample of 20 evidence records from sweep-70 to sweep-75, each opened at its source and checked for value, grade, partial flag and a verbatim quote. (b) Three of the 26 ant diel rows in `canon-8.jsonl`, checked against Table 1 of Johnson and Rutowski 2022 (PLoS ONE 17(9): e0257779), and then the rest of those rows. (c) The four Futahashi et al. 2015 rows in `canon-9.jsonl`. (d) Six spot checks of the recheck-9 partial flags on the Bowmaker, Wilkie and Hunt 1999 and Lu and Kronforst 2026 records in `recheck-9-fixed.jsonl`.

Method as in audits 6 to 9: each source opened with WebFetch and asked first whether the exact quote string appears, then for the page's own sentence in consecutive pieces of at most about 125 characters, with split points in `where`; corrected quotes are 40 words or fewer. Verdicts: `confirm`, `requote`, `correct`, `retract`, `unverifiable`. Typographic differences count as `confirm`; a change to the partial flag counts as `correct`. A value carried from a review or compilation table is a secondary citation and carries `partial: true` with the primary named. Corrections are in `docs/views/recheck/recheck-10.jsonl` in the recheck-5 schema. No evidence file and not `docs/views/audit/ALL.jsonl` was edited.

## Part (a): random sample of sweep-70 to sweep-75

The six files hold 25 records (sweep-72 has one, sweep-74 has 13). Two were drawn from each file (the one record of sweep-72) and nine more from the remainder (Python `random`, seed 20261015). Not drawn: sweep-74:2, 74:3, 74:6, 74:11 and 75:2.

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
| sweep-70:1 | Glis glis / acuity_cpd | m | confirm | verbatim in the abstract (Lynx PDF), line break after "ca."; the sentence before gives the ganglion cell densities for the fat dormouse |
| sweep-70:2 | Glis glis / receptor_classes | m | confirm | verbatim except "shortwavesensitive" (hyphen lost at a line end), same split |
| sweep-71:2 | Dermochelys coriacea / fovea | m | correct | phrase verbatim, but the sentence ends "called the "area temporalis" (Oliver LJ et al, Mar Fresh Behav Physiol 2000;33:233–48)." An editorial reporting a cited value, without `partial: true`; now partial. The PMC page also prints a DOI (10.1136/bjo.2005.082172) that the note says is absent |
| sweep-71:1 | Dermochelys coriacea / binocular_deg | m | confirm | both pieces verbatim on the Inter-Research abstract; the second sentence continues ", which might explain why they are prone to entanglement ..."; post-hatchlings; no DOI value printed after the page's "DOI:" label, as the note says |
| sweep-72:1 | Hydrochoerus hydrochaeris / fovea | m | confirm | verbatim in the Cambridge Core abstract; total population 368,840 as in the conditions |
| sweep-73:1 | Meroles knoxii / lambda_max_nm | g | confirm | Table 4 row verbatim (publisher PDF, backtick in "Knox`s"). The table is on p. 2904, where the record says p. 2905; metadata row written, not counted |
| sweep-73:2 | Francolinus francolinus / fovea | m | confirm | verbatim in the abstract; the next sentence reads "This shallow fovea was characterized by the presence of all retinal layers in the pit ..." |
| sweep-74:10 | Centris pallida / interommatidial_deg | m | confirm | Table 2 cell verbatim, large-morph males column; the Methods give ΔΦG from Land's (1997) formula for a hemispheric field. The female cell does print "31.51°", as the note says |
| sweep-74:4 | Helicops angulatus / lambda_max_nm | m | confirm | verbatim (Results); the sentence names H. angulatus |
| sweep-75:5 | Elaiophis inornatus / pupil_shape | m | confirm | verbatim in the diagnosis of Elaiophis gen. n.; the paper does not say vertical or horizontal; no DOI printed (a ZooBank LSID only) |
| sweep-75:4 | Hydrophis major / fovea | m | confirm | verbatim in the Macquarie abstract; D. major was among the three species used for ganglion cell stereology |
| sweep-74:8 | Helicops / fovea | g | confirm | verbatim (Introduction); the sentence continues "associated with specific visually guided behaviors ..." and carries no citation |
| sweep-74:12 | Sirex noctilio / lambda_max_nm | m | confirm | verbatim; the sentence opens "ERG measurements revealed", so the method's "recording method is not stated on the page read" is wrong. Metadata row written for 74:11 to 74:13, not counted |
| sweep-74:13 | Sirex noctilio / receptor_classes | m | confirm | as sweep-74:12 |
| sweep-75:1 | Ameivula ocellifera / fovea | m | confirm | verbatim (Salford repository copy); the sentence continues ", the relative contributions of lifestyle and phylogeny to its absence are unclear." The authors sectioned A. ocellifera eyes themselves |
| sweep-75:3 | Lapemis curtus / acuity_cpd | m | confirm | verbatim, abstract; already `partial: true` |
| sweep-74:5 | Helicops leopardinus / lambda_max_nm | m | confirm | verbatim; the UV cone came from one of the two individuals and the violet cone from the other |
| sweep-74:9 | Centris pallida / interommatidial_deg | m | confirm | Table 2 cell verbatim, small-morph males column |
| sweep-74:7 | Helicops / receptor_classes | g | confirm | verbatim; the sentence continues "with two distinct SWS1 opsins conferring sensitivity in the UV and the violet spectrum ..." |
| sweep-74:1 | Helicops angulatus / lambda_max_nm | m | confirm | verbatim; the sentence opens "In the H. angulatus individual, we recorded" |

**Rate: 1 error in 20 verifiable records, 5%** (0 unverifiable). The rate is not above 5%, so no batch recheck is required; sweep-71 holds two records, both in the sample. Quotes are clean (20 of 20 on the page). The one error is the recurring kind: a value an editorial cites from a primary, filed without `partial: true`.

## Part (b): ant diel rows in canon-8

Three rows drawn from the 26 (seed 20261015): canon-8:7 (Myrmecocystus navajo), canon-8:15 (Temnothorax neomexicanus), canon-8:16 (T. tricarinatus). Read in the Europe PMC full-text XML (the PLOS page answered first with an unrelated article, then without Table 1; PMC served a captcha).

| id | value | verdict | note |
|---|---|---|---|
| canon-8:7 | nocturnal, crepuscular in cooler months | correct | cell verbatim; Table 1's References column reads "[30, 60]" |
| canon-8:15 | crepuscular | correct | cell verbatim; References: "S.P. Cover, pers. comm." |
| canon-8:16 | crepuscular | correct | as canon-8:15 |

Every value and species cell is on the page, but Table 1 has a References column the records leave out, and the Methods say foraging times were gleaned "from literature, personal observations, and personal communications." Three of three are secondary values without `partial: true`, so all 26 rows were read against that column:

- 21 rows cite only literature or personal communications and are corrected to `partial: true` with the cell's citation in the note (canon-8:1 to 13, 15 to 17, 19, 20, 22, 25, 26).
- 5 rows include "R.A. Johnson, pers. obs." (an author's own observation) and stand: canon-8:14 (sp. BCA-5), 18 (V. chamberlini), 21 (V. lariversi, author observation only), 23 (V. pergandei) and 24 (RAJ-pseu).
- The reference list could not be read (Europe PMC's XML stops in the Discussion; the references endpoint answered 429), so only [30] is resolved, by the text, as Snelling's revision of Myrmecocystus. [48] and [60] to [68] are left as numbers.
- Footnote markers in the cells ("nocturnal*", "variable+", "Snelling#") are dropped in the quotes; typographic.

## Part (c): Futahashi et al. 2015 rows in canon-9

The abstract sentence is verbatim (PMC4371951). It speaks of the three Libellulidae together, but "consistently identified" already says each survey found the set, and the Results state it per species, in the subsection "Identification of 20 Opsin Genes in Dragonflies of the Family Libellulidae":

- Orthetrum albistylum: "... in the same way, wherein 67 million HiSeq reads and 2.4 million MiSeq reads (Table S1) yielded the same set of 20 opsin genes (Fig. 3A; accession nos. LC009076–LC009095)."
- Ladona fulva: "... identified the same set of 20 opsin genes (Fig. 3A; accession nos. BR001237–BR001256), and confirmed no other opsin genes in the genome."

"The same set" refers to the Sympetrum frequens set the abstract breaks down as 1 UV, 5 SW and 10 LW, so SW 5 and LW 10 follow for each species. **Verdict: confirm, all four rows; no retraction.** Grade `g` stands, as the note gives it. The per-species sentences would support `m` if quoted beside the abstract sentence; left to the desk. Note: L. fulva's set comes from a tBLASTn search of a draft genome, with no RNA sequencing; the method field covers both.

## Part (d): recheck-9 partial-flag spot checks

Three Bowmaker Table 1 rows and three Lu and Kronforst rows were drawn from `recheck-9-fixed.jsonl` (seed 20261015).

| fixed line | supersedes | taxon / where | result |
|---|---|---|---|
| 7 | oa-6:361 | Papilionoidea, main text | matches: "(Exner 1891; Nilsson 1989; Land and Nilsson 2012; Meyer-Rochow and Lindström 2025)" ends the sentence (Springer page) |
| 11 | oa-6:365 | Aglais urticae, Fig. 1 caption | matches: the caption ends "adapted from (Kolb 1985)." |
| 67 | oa-6:422 | Apaturini, main text | matches: "Nymphalini (Briscoe and Bernard 2005) and Apaturini (Pirih et al. 2022)" |
| 116 | oa-6:571 | Coturnix japonica, Table 1 green | flag right; note names no primary |
| 118 | oa-6:573 | Coturnix japonica, Table 1 rod | as line 116 |
| 147 | oa-6:602 | Sturnus vulgaris, Table 1 red | flag right; note names no primary |

The Lu and Kronforst citations match as named. The Bowmaker table footnotes are in an image (S45.3_table_1.gif), which was refused again, so the table's own citation could not be compared. The review's prose does name the MSP source for both species: "the closely related Japanese Quail Coturnix coturnix japonica (Bowmaker et al. 1993)" (Vision Research 33: 571-578) and "Starling Sturnus vulgaris (Hart et al. 1998)" (J Exp Biol 201: 1433-1446). Note-only `correct` rows name these for the ten Table 1 rows of the two species (oa-6:569 to 573, 599 to 603), with the caveat that the footnote was not read. These are not counted as errors. The prose row oa-6:645 (starling, Bennett et al. 1997) matches the page and was left alone.

## Rows written

`recheck-10.jsonl`: 36 rows, all `correct`.

- Sample: sweep-71:2 (partial and DOI; counted). sweep-73:1 (page) and sweep-74:11 to 74:13 (method names ERG) are metadata only, not counted.
- Ant diel: 21 partial-flag rows from canon-8, three of them sampled.
- Bowmaker: 10 note-only rows naming the primary from the review's prose.

## Blocked pages

- Europe PMC REST answered 429 for the canon-8 references endpoint and for the Lu and Kronforst full text (Springer used instead).
- pmc.ncbi.nlm.nih.gov served a captcha for PMC9499225.
- The PLOS article page returned an unrelated article (Imperial cormorants) once, then the right article cut off before the reference list.
- The Bowmaker table image was refused on permission; the shell has no route to that host or to Europe PMC.

## Patterns (this run)

1. Sweep quotes are clean again (20 of 20). The single sample error is the familiar secondary value without `partial: true`, here an editorial with an inline citation.
2. Compilation tables with a References column are being logged as primary. The canon-8 ant rows quote the species and value cells and skip the citation cell beside them. A table row should be read across to its last column before it is filed.
3. Method fields can claim a page is silent on something it states (Sirex: "not stated", where the abstract opens "ERG measurements"). This kind of slip changes no value, but it misleads the desk about what the page offers.
