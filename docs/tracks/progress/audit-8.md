# Precision audit 8, 15 October 2026

Three parts. (a) A random sample of 20 records from sweep-58 to sweep-65, each opened at its source and checked for value, grade and a verbatim quote. (b) A check of every carry record in those files (a value logged for a genus from a congener, a group, a clade or a family) against the carry rules: a group, clade or family taxon is held to `g`; an opsin-inferred value is held to `g`; a year taken from a file name or a session date is flagged, since the year must come from the source. (c) Three DOIs drawn from the `chased` fields of `docs/views/searched/sweep-62.jsonl` to `sweep-65.jsonl`, opened to see that the work exists and whether it names the genus or its relatives.

Method as in audits 6 and 7: each source opened with WebFetch and asked first whether the exact quote string appears, then for the page's own sentence in consecutive pieces of at most about 125 characters, with split points recorded in `where`; corrected quotes are 40 words or fewer. Verdicts: `confirm`, `requote`, `correct`, `retract`, `unverifiable`. Typographic differences count as `confirm`; a change to the partial flag counts as `correct`, as in audit 7. Corrections are in `docs/views/recheck/recheck-8.jsonl` in the recheck-5 schema. No evidence file and not `docs/views/audit/ALL.jsonl` was edited.

## Part (a): random sample of sweep-58 to sweep-65

sweep-60 does not exist. The seven files with records hold 43 records (2 to 8 each). Two were drawn from each file and six more from the remainder (Python `random`, seed 20261015).

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
| sweep-58:2 | Ctenophorus pictus / fovea | m | confirm | sentence verbatim in the abstract (Macquarie portal), same split point; all six species named |
| sweep-58:7 | Ctenophorus vadnappa / fovea | m | confirm | as sweep-58:2 |
| sweep-58:3 | Ctenophorus nuchalis / fovea | m | confirm | as sweep-58:2 |
| sweep-59:8 | Malpolon monspessulanus / filter_pigments | m | confirm | sentence verbatim in the Sci.News report (20 September 2016), same three pieces; already `partial: true` |
| sweep-59:4 | Thomomys bottae / receptor_classes | m | confirm | clause verbatim in the Springer abstract; the sentence opens "Electroretinogram recording revealed the presence of three types of photopigments," |
| sweep-59:3 | Thomomys bottae / lambda_max_nm | m | confirm | as sweep-59:4 |
| sweep-59:1 | Thomomys bottae / lambda_max_nm | m | confirm | as sweep-59:4 |
| sweep-61:1 | Atta cephalotes / interommatidial_deg | m | correct | row verbatim in Table 1; the caption says all angles are "reported from the literature (Table S2)" and the row cites ref. 1, unopened, so the record is secondary and now `partial: true`. Flag: 0.26° is implausibly small for an ant eye |
| sweep-61:2 | Atta cephalotes / acceptance_deg | m | retract | the caption: "Bold values for acceptance angle and CPD are reported from the literature, otherwise value provided is calculated." 0.52 is exactly 2 × Df, the pattern of the calculated rows; the reported Apis row (2.60 against 0.80) breaks it. Bold could not be read in the extracted text, so the retraction rests on that pattern |
| sweep-62:1 | Rhea americana / lambda_max_nm | g | confirm | sentence verbatim with the same OCR artefacts; the preceding sentence ("Both species possess rods ...") confirms the values are pooled for ostrich and rhea, so `g` is right |
| sweep-62:2 | Boiga irregularis / acuity_cpd | m | confirm | clause verbatim; the sentence continues "whereas some similar sized semi-arboreal, diurnal rat snakes had values two to four times greater." Inferred year flagged in the note |
| sweep-63:7 | Rhabdomys pumilio / receptor_classes | m | confirm | verbatim in the author manuscript PDF, Results, "Rhabdomys SWS and MWS-cone opsins"; the sentence ends "(Fig 2a)." |
| sweep-63:4 | Sirex noctilio / receptor_classes | m | confirm | verbatim in the nature.com abstract: "ERG measurements revealed two photoreceptor types in the compound eye, maximally sensitive to 527 and 364 nm." |
| sweep-63:5 | Sirex noctilio / lambda_max_nm | m | confirm | as sweep-63:4 |
| sweep-63:2 | Geronticus eremita / binocular_deg | m | confirm | verbatim in the Discussion, same split; the sentence ends "(Fig. 1)." and the preceding sentence names the Northern Bald Ibis |
| sweep-64:5 | Caenophidia / acuity_cpd | g | confirm | both sentences verbatim on the SICB page; 8 caenophidians tested |
| sweep-64:4 | Henophidia / acuity_cpd | g | confirm | both verbatim; the second continues ", whereas some small burrowing specialists such as sand boas had values of only 0.25 cpd."; 9 henophidians tested |
| sweep-64:2 | Euglossa dilemma / receptor_classes | m | confirm | sentence verbatim (UMSL record), same split |
| sweep-65:4 | Lacertidae / lambda_max_nm | g | confirm | verbatim in the publisher PDF; the sentence is on p. 2902 (the record says p. 2904) and rests on "a crude extrapolation" from Anolis and Gekko data. Metadata-only row written, not counted |
| sweep-65:7 | Coturnix japonica / spectral_range_nm | m | confirm | row verbatim in Table 1 (Vilnius University repository copy; the JEB page served a captcha). Note defect left for the desk: the § on "Japanese quail" marks data original to this study (figshare 10.6084/m9.figshare.16634977), and the reference column is headed "References for data not obtained in this study", so the note's "cites Olsson et al. 2016 for transmittance" is doubtful |

**Part (a) rate: 2 errors in 20 verifiable records, 10%** (0 unverifiable). Both errors are in sweep-61, a two-record file whose records were both in the sample, so the batch recheck that a rate above 5% calls for is complete with the sample itself.

## Part (b): carry records in sweep-58 to sweep-65

All 43 records were read for carry claims. Grades on group, clade and family taxa (sweep-64:1, 64:4, 64:5, 65:4, 65:5) are `g`; opsin- or sequence-inferred records (sweep-62:4, 62:5, 63:1, 65:3, 65:4) are `g`; the three SICB records (sweep-62:2, 64:4, 64:5) carry a year of 2017 that the page does not print (it gives only "Thursday, Jan. 5"), and each note flags the year as inferred. Those rules hold. Defects found:

| id | taxon / trait | action | note |
|---|---|---|---|
| sweep-59:5 | Cryptoblepharus boutonii / fovea | correct | congener carry; the thesis sentence ends "(Röll, 2001)" (checked in the Adelaide PDF), so the record is secondary and now `partial: true` |
| sweep-59:6 | Cryptoblepharus boutonii / oil_droplets | correct | as sweep-59:5 |
| sweep-64:1 | South American camelids / tapetum | correct | taxon was a common name; now "Lama and Vicugna", as audit 7 accepted for sweep-50:6 |

Flagged, not acted on: sweep-65:8 (Bos taurus, depth_cue) says the gayal and yak cells "can take this as a genus-level reading" without naming the grade; any such carry must be `g`. sweep-61:1 says Atta cephalotes "carries within the genus" to Atta mexicana; the same holds, and the value itself needs its primary opened first.

## Part (c): three chased DOIs

Drawn from the 205 DOIs in `chased` fields of searched sweep-62 to sweep-65 (seed 20261015).

| log | genus | DOI | result |
|---|---|---|---|
| sweep-62:40 | Urocerus | 10.1038/s41598-021-95107-2 | exists (Guignard et al. 2021). **The log's claim "names no Urocerus" is wrong**: the Discussion reads "A blue photoreceptor was also not found in the sawfly Urocerus gigas (Siricoidea) and in the woodwasp X. camelus (Xiphidrioidea)", citing Peitsch et al. 1992 (J Comp Physiol A 170: 23-40). Urocerus gigas already has intracellular spectral data in canon-3 (via Briscoe and Chittka 2001), and the searched traits (acuity, flicker, corner frequency, interommatidial angle) are untouched by it, so no evidence cell changes; the `chased` text and its "nothing carries to Urocerus" should be corrected by the desk |
| sweep-63:1 | Psammophis | 10.1016/j.visres.2020.04.004 | unverifiable: doi.org answered 429 and the two repository records a search returned were other Vision Research items |
| sweep-63:33 | Philothamnus | 10.3389/fevo.2019.00352 | exists (Katti, Stacey-Solis, Coronel-Rojas and Davies 2019, "The Diversity and Adaptive Evolution of Visual Photopigments in Reptiles", Front Ecol Evol 7); only the abstract was reachable, and it names no snake genus, so the log's list of named genera (Thamnophis, Pituophis, Philodryas) could not be checked |

## Rows written

`recheck-8.jsonl`: 6 rows. Sample: sweep-61:1 (correct, partial) and sweep-61:2 (retract), both counted; sweep-65:4 (correct, metadata only, not counted). Carry check: sweep-59:5, sweep-59:6 (partial) and sweep-64:1 (taxon).

## Blocked pages

journals.biologists.com served a captcha for both JEB papers (publisher PDF and repository copies used instead); the Europe PMC REST search and doi.org for 10.1016/j.visres.2020.04.004 and 10.3389/fevo.2019.00352 answered 429; frontiersin.org's article page timed out on permission; sciencedirect.com refused by robots rule; par.nsf.gov could not be reached from the shell to read bold formatting.

## Patterns (this run)

1. Quotes are clean: 20 of 20 quotes are on the page as given. The two errors are both in what a compilation table's row means, which a verbatim quote check cannot catch: a secondary value without `partial: true`, and a calculated cell filed as reported.
2. The silent secondary citation that audit 7 named recurs in the carry records (sweep-59:5, 59:6): a thesis sentence ending in a citation, quoted to the comma before it.
3. The `chased` step can misread an opened paper. In one of the two checkable cases the log says a paper does not name the genus when its Discussion does.
