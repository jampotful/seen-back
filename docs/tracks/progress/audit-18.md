# Precision audit 18, 16 October 2026

Scope: 23 records from evidence files that no audit table, recheck file or `ALL.jsonl` row had touched, plus audit 17's seven unverifiable sweep-5 records. Coverage check first: every record of sweep-6 (36), sweep-7 (18) and sweep-8 (24) already appears in audits 2 to 6 or in recheck-2, recheck-4 and recheck-5, so none was picked from them. canon-2 (118), canon-3 (724), canon-4 (400) and canon-5 (216) had no audited record; canon-6 is empty; canon-7 had four (7:4, 7:12, 7:38, 7:40). The 16 canon picks are one record per source paper, drawn at random within each source (seed 18), across amphibians, reptiles, birds, mammals, insects, crustaceans and plants.

Method as in audits 13 to 17: each source opened with WebFetch (WebSearch only to locate it) and asked first whether the exact quote string appears, then for the page's own sentence in consecutive pieces. Verdicts: `confirm`, `requote`, `correct`, `retract`, `unverifiable`. A change to the partial flag or the grade counts as `correct`. Compiled table values count as cited from another study, so they need `partial: true` and the primary source named. Corrections are in `docs/views/recheck/recheck-18.jsonl` in the recheck-5 schema. No evidence file, no wanted file and not `docs/views/audit/ALL.jsonl` was edited.

## Table

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
| sweep-5:1 | Xylocopa tenuiscapa / acuity_cpd 0.5 | m | unverifiable | PMC5249068 blocked at the permission step again; the Lund record found is a different Xylocopa paper (J Comp Physiol A 2008), with no file. Third attempt |
| sweep-5:2 | Astur cooperii / binocular_deg 36 | m | unverifiable | PMC2943905 blocked at the permission step; PubMed captcha; Crossref and Europe PMC rate-limited. Purdue e-Pubs holds Hawk Eyes II only |
| sweep-5:3 | Astur cooperii / fov_h_deg 300 | m | unverifiable | same paper; still a derived value (360 − 60) on a cut quote |
| sweep-5:4 | Astur cooperii / eye_movement | m | unverifiable | same paper; quote still a fragment to be checked |
| sweep-5:5 | Leucophaeus atricilla / lambda_max_nm | m | unverifiable | Hart 2001 closed (Elsevier); search found no author or repository copy |
| sweep-5:7 | Anemone coronaria / sense_light_nonvisual | m | correct | HUJI page opened this time: quote verbatim in the abstract (17 words), "critical day-length for dormancy induction was between 11 and 12 h" at 22/17 °C confirmed. Abstract only; `partial` set to true |
| sweep-5:11 | Cichorium intybus / diel | m | correct | Nature Institute page opened: quote verbatim. The essay says heads begin to close "before midday" and close "by midafternoon"; the value's "early afternoon" is corrected. Overcast-day sentence confirmed |
| canon-2:8 | Ambystoma tigrinum / lambda_max_nm | m | correct | Mohun & Davies 2019 Table 1 row confirmed (Frontiers). Compiled from Hárosi 1975 and Perry & McNaughton 1991; `partial` set to true |
| canon-2:51 | Ctenophorus ornatus / lambda_max_nm 440 | m | correct | quote a fragment; requoted to the whole 31-word sentence. Measurement is Barbour et al. 2002 (next sentence); `partial` set to true |
| canon-2:97 | Tadorna ferruginea / binocular_deg 27 | m | requote | quote began mid-sentence; requoted from the sentence start with the cut marked (the whole is about 49 words). Ruddy shelducks, n = 3, measured in the paper |
| canon-2:112 | Leptopelis aubryi / receptor_classes | g | requote | quote dropped "We also found that"; requoted to the whole 20-word sentence (UCL Discovery; PMC blocked) |
| canon-3:404 | Eristalis tenax / receptor_classes | m | correct | Briscoe & Chittka Table 1 row verbatim; from ref. 77, Horridge, Mimura & Tsukahara 1975. `partial` true, primary source added to the note |
| canon-3:148 | Archilochus alexandri / colour_vision | m | correct | Kelber et al. 2003 Table 2 row confirmed; cited from Goldsmith et al. 1981; `partial` set to true |
| canon-3:592 | Spilotes pullatus / diel | m | correct | the quote expanded the cell "D" to "Diurnal" and respelled "Spillotes"; requoted to the printed row. Activity pattern sourced to Marques et al. 2001 and Torello-Viera & Marques 2017; `partial` true |
| canon-3:81 | Sturnus vulgaris / binocular_deg | m | unverifiable | the record's only open copy sits on a third-party faculty site (illinoisstate.edu), which the access rules exclude; Birmingham repository holds no file; Springer rate-limited. A field-type range (20-30°) is not a species figure, so `g` should be checked when it opens |
| canon-3:715 | Tamiasciurus hudsonicus / cff_hz 60 | m | correct | quote rearranged the row; requoted as extracted (TARA). From ref. 10, Tansley, Copenhaver & Gunkel 1961 (ERG); `partial` true, primary source named |
| canon-3:656 | Populus deltoides x nigra / sense_chemical | m | unverifiable | eScholarship item page empty to the fetch tool; the PDF blocked at the permission step |
| canon-3:570 | Ardeidae / eye_movement | g | correct | quote stopped mid-sentence unmarked; requoted to the whole 34-word sentence. Cites Daanje 1951 and Fujita 2006; `partial` true |
| canon-3:547 | Lens culinaris / sense_light_nonvisual | m | correct | the sentence speaks "in general" of the galegoid clade with lentil as an example and cites Summerfield & Roberts 1985b; no lentil measurement. Grade to `g`, `partial` true, requoted with the cut marked (sentence is 55 words) |
| canon-4:235 | Glyphocrangon alispina / acuity_cpd 0.52 | m | correct | row verbatim (NSF PAR). From the compilation's ref. 33, not named in the open copy; 0.52 = 1/Δρ, likely calculated. `partial` set to true |
| canon-5:68 | Coturnix japonica / diel | g | confirm | CSV row 34 of 94 verbatim on Zenodo; the space after "9.33," in the quote is the join between the two pieces |
| canon-7:16 | red kangaroo / tapetum | g | correct | quote verbatim in the PubMed abstract (Results); abstract-only read of a review, `partial` set to true. Taxon should carry Osphranter rufus |
| canon-7:6 | Anax parthenope / opsin_gene_count 21 | m | confirm | sentence verbatim on PMC4371951, section "Diversity and Evolutionary Dynamics of Opsin Genes in the Odonata" |

**Rate: 14 errors in 16 verifiable records, 88%** (7 unverifiable). sweep-5: 2 in 2 verifiable. canon files: 12 in 14. By verdict: 2 requote, 12 correct, 0 retract; 2 confirm.

## Checks

- **Partial flag on compiled values.** The canon units logged table rows from reviews and compilations at `m` without `partial`. Nine of the twelve `correct` verdicts are this one fault (canon-2:8, 2:51, 3:148, 3:404, 3:592, 3:715, 3:570, 4:235, 7:16). The canon files hold about 1,500 records of the same kind, so a mechanical pass setting `partial: true` on every compiled row whose `note` says "Compiled in" is the obvious next step; the audit does not make it, since it may not edit evidence files.
- **Grade.** canon-3:547 was `m` on a clade-level generalization; lowered to `g`. canon-3:81 holds a field-type range at `m` and needs the same look once its source opens.
- **Complete sentences.** Five quotes were fragments or rearranged rows (canon-2:51, 2:97, 2:112, 3:570, 3:715); one expanded a table code (canon-3:592).
- **Values.** Every opened value stood except sweep-5:11 (closing time).

## Rows written

`recheck-18.jsonl`: 14 rows: sweep-5:7, sweep-5:11, canon-2:8, canon-2:51, canon-3:404, canon-3:148, canon-3:592, canon-3:715, canon-3:570, canon-3:547, canon-4:235, canon-7:16 (`correct`); canon-2:97, canon-2:112 (`requote`).

## Blocked pages

- Permission step not answered: pmc.ncbi.nlm.nih.gov (PMC2943905, PMC5249068), frontiersin.org/articles/10.3389/fevo.2019.00321/full (the frontiersin.org/journals/... form opened), escholarship.org PDF qt3921m35r, the first TARA bitstream request (opened on retry after the item page).
- Rate limited (HTTP 429): Europe PMC REST, api.crossref.org, doi.org for Springer.
- pubmed.ncbi.nlm.nih.gov/20877645 captcha (14738502 opened).
- Not attempted by rule: the illinoisstate.edu faculty-site copy of Martin 2007.

## Patterns (this run)

1. The canon units are compilations read from tables. Their values hold up; the errors are the missing partial flag and the primary source left out of `note`.
2. The PLoS pair (Xylocopa, Hawk Eyes I) has now failed three runs on tooling. The owner could drop both open-access PDFs into the papers folder and settle four records at once.
