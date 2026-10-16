# Precision audit 17, 15 October 2026

Scope: every evidence record in harvest-3 (4; `docs/views/wanted/harvest-3.jsonl` is empty) and every record of sweep-5 (16), 20 records in all. The desk named sweep-90, sweep-91, sweep-92 and sweep-96 as unaudited, but audits 14 and 15 already cover all 16 of their records, so the 16 places went to the oldest evidence file with no record in any audit, recheck or `ALL.jsonl`: sweep-5 (13 October). The intake files are older still but come from the owner's closed-access PDFs, which this audit cannot open. No sampling; every source was requested.

Method as in audits 13 to 16: each source opened with WebFetch and asked first whether the exact quote string appears, then for the page's own sentence in consecutive pieces. Verdicts: `confirm`, `requote`, `correct`, `retract`, `unverifiable`. Typographic differences count as `confirm`; a change to the partial flag or the grade counts as `correct`. Corrections are in `docs/views/recheck/recheck-17.jsonl` in the recheck-5 schema. No evidence file, no wanted file and not `docs/views/audit/ALL.jsonl` was edited.

## Table

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
| harvest-3:1 | Pinus elliottii / sense_light_nonvisual | m | confirm | verbatim, last sentence of the abstract (OUP page, abstract only; "only available as a PDF"). "P. menziesii" in the quote is Pseudotsuga menziesii (title). Both species measured separately, so `m` holds; `partial: true` right. The page prints the DOI as 10.1093/jxb/50.335.831; the record's jexbot form resolves to the same article |
| harvest-3:2 | Pinus pinaster / sense_light_nonvisual | m | confirm | verbatim in the abstract on the CIRAD Agritrop record (Springer rate-limited, PMC and the Agritrop PDF blocked at the permission step). The lamp type and the 314-494 µmol m⁻² s⁻¹ in `value` come from the Methods and were not checked; ninth author is Plomion C (record ends "et al.") |
| harvest-3:3 | Quercus variabilis / sense_light_nonvisual | m | confirm | verbatim (MDPI); the next sentence, "Seedling ground diameter elongation is stimulated by all light quality treatments, except for the BL treatment.", backs the blue-light exception. Full text is on the page; `partial: true` is conservative and stands |
| harvest-3:4 | Geranium pyrenaicum / sense_light_nonvisual | m | confirm | verbatim on PMC (hyphen in "shade‐avoiding" is U+2010). Plant Direct 2(8): e00066, 2018; full text on the page, `partial: true` conservative |
| sweep-5:1 | Xylocopa tenuiscapa / acuity_cpd 0.5 | m | unverifiable | PLoS served an unrelated article to the fetch tool, doi.org and Europe PMC rate-limited, PMC blocked at the permission step; IISc and IAS repositories hold the abstract only |
| sweep-5:2 | Astur cooperii / binocular_deg 36 | m | unverifiable | as sweep-5:1 (PLoS served an unrelated article; PMC2943905 blocked; PubMed captcha) |
| sweep-5:3 | Astur cooperii / fov_h_deg 300 | m | unverifiable | same paper; also a derived value (360 − 60) whose quote is cut mid-sentence. Recheck when PMC opens |
| sweep-5:4 | Astur cooperii / eye_movement | m | unverifiable | same paper; the quote is a sentence fragment and should be checked with the others |
| sweep-5:5 | Leucophaeus atricilla / lambda_max_nm | m | unverifiable | Hart 2001, closed (Elsevier); no open copy found. The quote is a table row, which the 40-word sentence rule does not fit |
| sweep-5:6 | Dryocopus pileatus / spectral_range_nm | m | correct | verbatim in the abstract (UNL Digital Commons; USGS blocked). Abstract-only read without `partial: true`; set to true |
| sweep-5:7 | Anemone coronaria / sense_light_nonvisual | m | unverifiable | HUJI page blocked at the permission step; AGRIS holds only Ben-Hod's 1987 thesis record. The sister paper (Sci. Hortic. 40: 247-258, 1989) confirms "summer dormancy inducible by long days (LD) and/or high temperatures" but not this quote |
| sweep-5:8 | Rosa hybrida / diel | m | correct | verbatim (AGRIS abstract; HUJI blocked); cv. Fragrant Cloud confirmed. `partial` set to true |
| sweep-5:9 | Salvia occidentalis / sense_light_nonvisual | m | correct | the quote is a mid-sentence fragment; requoted to the whole AGRIS sentence (25 words) and `partial` set to true |
| sweep-5:10 | Solidago altissima / sense_chemical | m | correct | the quote is the middle of a Conclusions sentence of about 45 words; requoted to the abstract HIPV sentence (25 words) and `partial` set to true |
| sweep-5:11 | Cichorium intybus / diel | m | unverifiable | natureinstitute.org blocked at the permission step; no other copy |
| sweep-5:12 | Aphelocoma californica / eye_movement | m | requote | the quote is a fragment; requoted to the whole Results sentence (38 words) from the author's open PDF. 7.31, SE 0.55° confirmed |
| sweep-5:13 | Platalea leucorodia / eye_movement | g | requote | the quote stops at "14"; requoted to the whole sentence. Pooled over four species, two birds each, so `g` is right |
| sweep-5:14 | Daucus carota / sense_light_nonvisual | m | correct | verbatim (maxapress PDF preview); 16L/8D highest chlorophyll confirmed. `partial` set to true |
| sweep-5:15 | Viola / sense_light_nonvisual | m | retract | the quote is the title; the visible preview gives the aim and cites V. fimbriatula from earlier work, with no result of the author's own. A genus filed at `m` also breaks the grade rule |
| sweep-5:16 | Dryopteris filix-mas / sense_light_nonvisual | m | correct | the quote stops at a semicolon; requoted to the whole Summary sentence (20 words), which carries the red-light half of the value. `partial` set to true |

**Rate: 9 errors in 13 verifiable records, 69%** (7 unverifiable). harvest-3: 0 in 4. sweep-5: 9 in 9 verifiable. By verdict: 2 requote, 6 correct, 1 retract.

## Checks

- **Abstract-only reads carry `partial: true`.** All four harvest-3 records do. sweep-5 predates the flag: six of its abstract records lack it (sweep-5:6, 8, 9, 10, 14, 16, set here) and so does the retracted sweep-5:15.
- **Grade.** sweep-5:13 (pooled) is `g`. sweep-5:15 (genus Viola) was `m`, retracted. Every other record names one measured species.
- **Complete sentences.** sweep-5 quotes are often fragments (5:3, 5:4, 5:9, 5:10, 5:12, 5:13, 5:16) or a title (5:15). harvest-3 quotes are all whole sentences.
- **Encyclopedia and database sources.** None. sweep-5:11 is a magazine essay, labelled as such in `method` and `note`.

## Rows written

`recheck-17.jsonl`: 9 rows, all counted: sweep-5:6, 8, 9, 10, 14, 16 (`correct`), 12, 13 (`requote`), 15 (`retract`).

## Blocked pages

- Permission step not answered: pmc.ncbi.nlm.nih.gov (PMC3017815, PMC2943905), agritrop.cirad.fr PDF, usgs.gov publication page, cris.huji.ac.il (both records), maxapress.com article page, natureinstitute.org, agris.fao.org (en record 6511ae115e14514d9dddb642; the ar copy opened).
- Rate limited (HTTP 429): link.springer.com (BMC Plant Biology), doi.org for PLoS, Europe PMC REST.
- journals.plos.org returned unrelated articles for both PLoS DOIs; hal.inrae.fr bot wall; pubmed.ncbi.nlm.nih.gov captcha.

## Patterns (this run)

1. sweep-5, the earliest sweep, was written before the 40-word whole-sentence rule and the partial flag. Its errors are format errors: every verifiable value stood except Viola, whose only support was a title.
2. The seven unverifiable records are all in sweep-5 and all blocked by tooling (PLoS, PMC, HUJI, Nature Institute), apart from Hart 2001, which is closed. A rerun with PMC open would settle four of them.
