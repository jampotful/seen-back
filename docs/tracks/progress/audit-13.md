# Precision audit 13, 15 October 2026

Scope: every evidence record in sweep-84, sweep-86 and sweep-87. sweep-85 has no evidence file. Audit 12 covered all 16 records of sweep-80 to sweep-82 (sweep-80: 2, sweep-81: 4, sweep-82: 10) and sweep-83 has none, so nothing from that range was left over. The audit covers 13 records (sweep-84: 7, sweep-86: 5, sweep-87: 1). No sampling; all were opened.

Method as in audit 12: each source opened with WebFetch and asked first whether the exact quote string appears, then for the page's own sentence in consecutive pieces of at most about 125 characters, with split points in `where`; corrected quotes are 40 words or fewer. Verdicts: `confirm`, `requote`, `correct`, `retract`, `unverifiable`. Typographic differences count as `confirm`; a change to the partial flag or the grade counts as `correct`. Corrections are in `docs/views/recheck/recheck-13.jsonl` in the recheck-5 schema. No evidence file and not `docs/views/audit/ALL.jsonl` was edited.

## Table

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
| sweep-84:1 | Octodon lunatus / binocular_deg 100 | m | correct | abstract quote verbatim (U. Chile repository), split after "found in". The full text is open on journals.plos.org and the repository links an open PDF. Results, "Visual field measurements": "the region of maximum binocular overlap of O. lunatus was two times larger than that of O. degus (up to 100° width)". Flag set to `partial: false`, requoted to Results |
| sweep-84:2 | Octodon degus / binocular_deg 50 | m | correct | as 84:1; the 50° is the authors' own measurement: "the region of maximum binocular overlap had an extension of 50°", between 30° and 60° elevation. Flag set to `partial: false`, requoted |
| sweep-84:3 | Octodon degus / receptor_classes 2 | m | confirm | verbatim (UC repository), including the page's "run" for "nm"; the sentence opens "The degu's photopic sensitivity had a lambda(max) at 500.6 +/- 1.2 nm". Metadata row: Chávez et al. 2003, IOVS 44(5): 2290-2296 |
| sweep-84:4 | Octodon degus / lambda_max_nm 500 | m | confirm | as 84:3 |
| sweep-84:5 | Octodon degus / lambda_max_nm 360 | m | confirm | as 84:3; "approximately 360" logged as 360, as stated |
| sweep-84:6 | Psammomys obesus / receptor_classes | g | correct | quote verbatim (Springer abstract), preceded by "P. obesus showed a high percentage of cones, 41% of total photoreceptor numbers". One named species, no pooling, so grade `g` was wrong; set to `m` |
| sweep-84:7 | Graphiurus sp. / receptor_classes | g | confirm | verbatim (Národní muzeum page), split after "high rod density,"; metadata matches (Lynx 53(1): 185-205, 10.37520/lynx.2022.013). The page links a full-text PDF, which the fetch tool refused, so the flag was left as filed |
| sweep-86:1 | Micaelamys namaquensis / receptor_classes 2 | m | confirm | verbatim (UP repository PDF), p. 8, Results, "Cone photoreceptors"; "OS-2 positively labelled short wave sensitive opsins in both species". Ratios 1:7.8 and 1:12.4 and peak 5766/mm² all in the paper |
| sweep-86:2 | Pentalagus furnessi / tapetum | m | confirm | verbatim after "In the Amami rabbit,". The full-text page's metadata names Tanaka A only; the publisher's article description page prints "Muko R, Matsuda H and Tanaka A", as the record has it. Body text not reached, flag kept |
| sweep-86:3 | Liuixalus feii / pupil_shape | m | confirm | verbatim, p. 252, holotype description; full Zootaxa PDF, 3990(2): 247-258 |
| sweep-86:4 | Pelophryne murudensis / pupil_shape | m | confirm | verbatim, p. 437; the clause continues "tympanum visible, its annulus indistinct, oval". No orientation stated, as the note says |
| sweep-86:5 | Pelophryne linanitensis / pupil_shape | m | confirm | verbatim, p. 439, the same wording as 86:4 |
| sweep-87:1 | Neofelis nebulosa / tapetum | m | confirm | verbatim (link.springer.com/10.1186/...), Results, "The eyeball morphology"; the sentence opens "Macroscopically, the tapetum lucidum". One clouded leopard from Wrocław Zoo; BMC Vet Res 22: 329 |

**Rate: 3 errors in 13 verifiable records, 23%** (0 unverifiable). Every quote is verbatim. The errors are two flags set on an open-access paper and one grade.

## Checks the desk asked for

- **Abstract-only records carry `partial: true`.** Yes for all six records filed from abstract pages (84:3 to 84:7, 86:2). Two records carry the flag without cause: 84:1 and 84:2 cite a PLoS ONE paper whose full text is open and holds the authors' own visual field measurements (corrected). 84:7 links a full-text PDF on the publisher page; the fetch tool refused it, so the flag stays until someone reads the PDF.
- **Pooled or unnamed-species records are `g`.** Graphiurus sp. (84:7) is `g` and correctly so. Psammomys (84:6) was `g` for a reason the rule does not give (a misspelled title); corrected to `m`. No other record pools species.
- **Encyclopedia and database sources.** No record uses one. The three sweep-86 pupil records come from original species descriptions (Zootaxa, Raffles Bulletin), which is the kind of source audit 12 asked for after its pupil retractions.
- **Values quoted from another study.** No such record was found. The O. degus 50° (84:2) sits in an O. lunatus sentence of the abstract, but the Results show the authors measured it themselves.
- **Converted or estimated values.** No record converts or estimates a value. 84:5 logs "approximately 360" as 360 with the qualifier in the note.
- **Metadata.** 84:3 to 84:5 had no authors, journal or DOI; filled (see rows). 86:2 authors confirmed on the publisher's description page. All other metadata matches the source.
- **Audit-7 items.** The cat Vantoi and Riva 1995 blood-flow records and the Macaca radiata evoked-potential records sit in oa-6 and oa-3; neither string occurs in sweep-80 to sweep-87, so they are out of scope here and still await a desk decision.

## Rows written

`recheck-13.jsonl`: 6 rows.

- Counted: 84:1, 84:2 (`correct`, partial flag, quote, method, where, journal field), 84:6 (`correct`, grade).
- Not counted: 84:3, 84:4, 84:5 (`correct`, metadata only). Authors, title subtitle, journal, volume, pages and DOI filled from the Pherobase literature record H/37681 (Chávez AE, Bozinovic F, Peichl L, Palacios AG; IOVS 44(5): 2290-2296; 10.1167/iovs.02-0670).

## Blocked pages

- The Lynx full-text PDF (publikace.nm.cz/en/file/.../185_205_Peichl.pdf), the Medwin PDF for the Amami rabbit paper, and link.springer.com/article/10.1186/s12917-026-05480-1 were refused at the permission step; the Springer paper was read through the link.springer.com/10.1186/... form.
- pmc.ncbi.nlm.nih.gov (PMC3877236) returned a reCAPTCHA page; doi.org/10.1167/iovs.02-0670 returned a fetch error. The avesis.iuc.edu.tr record was rejected for URL length.
- A first fetch of the PLoS URL with an unencoded slash returned a different article (e0136980); the encoded form returned the right one.

## Patterns (this run)

1. The audit-12 pattern recurs: a record filed from a repository abstract page (here U. Chile) missed that the same paper is open in full, so the flag was set and the value was quoted from a comparison sentence in the abstract when the Results state each species' value on its own.
2. Repository records from repositorio-az.uc.cl leave authors and DOI blank for the third time (82:7 to 82:9, 84:3 to 84:5). A literature index (Pherobase here, ANID last time) fills them in one fetch; the sweep agent could do it at filing.
3. Grade `g` was used to express doubt about a source's spelling. The grade rule is about pooled or unnamed taxa only; doubts about a source belong in the note.
4. Page metadata can disagree with the printed byline (86:2: the Medwin full-text page tags one author, the description page prints three). The byline wins.
