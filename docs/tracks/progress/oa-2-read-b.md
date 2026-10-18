# oa-2 reading pass, reader B (18 October 2026)

Prompt: `docs/tracks/prompts/oa-read.md`. Entries 38, 40, 44, 46, 49, 51, 62, 74 and 75 of `oa-2`, read in that order from the texts the `oa` job fetched again for this reader (run 6, `runs/oa/6-oa-2`). All nine decrypted with matching checksums, and each text's checksum equals run 1's, so the audit can use the control room's run-1 texts. This note is named `oa-2-read-b.md` because reader A logs other `oa-2` entries at the same time and a shared `oa-2-read.md` would collide at the merge.

## Counts

267 records in `docs/views/evidence/oa-2.jsonl`, 9 lines in `docs/views/sources/oa-2.jsonl`. Grades: 170 `m`, 93 `g`, 4 `i`. 140 records carry `partial: true`. Every record passes `quotecheck.py` (267 verbatim) and `oa_lint.py --text` against its paper, and `oa_lint.py --since-main HEAD` reports no faults.

| Entry | Paper | Records | m | g | i | partial |
|---|---|---|---|---|---|---|
| 38 | Thomas et al. 2020, frog eye size | 3 | 0 | 3 | 0 | 3 |
| 40 | Weller and Ortega 2015, legume flowering (review) | 23 | 13 | 10 | 0 | 23 |
| 44 | One Thousand Plant Transcriptomes Initiative 2019 | 0 | | | | |
| 46 | Li et al. 2015, phytochrome diversity | 49 | 19 | 30 | 0 | 16 |
| 49 | Hauzman, Bonci and Ventura 2018, snake retinal topography (book chapter) | 84 | 77 | 7 | 0 | 47 |
| 51 | Steck et al. 2024, salticid opsins (author manuscript) | 44 | 33 | 11 | 0 | 16 |
| 62 | Campbell and Loew 2024, anole oil droplets | 41 | 26 | 15 | 0 | 16 |
| 74 | Karban, Yang and Edwards 2014, volatile communication (meta-analysis) | 6 | 0 | 6 | 0 | 6 |
| 75 | Solov'yov, Mouritsen and Schulten 2010, cryptochrome compass model | 17 | 2 | 11 | 4 | 13 |

Paper with no measurement of a BRIEF trait: entry 44 (phylogenomics, genome duplications and gene-family sizes; its only light-related sentence is about chlorophyll b).

## Notes for the audit

- Entry 38: the species-by-species activity periods are in electronic supplementary table S1, which is not in the Europe PMC text; eye diameter is not a BRIEF trait. The three records cite the paper's refs 72, 73 and 76 by number, because the reference list did not come through in the XML text.
- Entry 40: the Crossref journal string lacked the article number and the XML text has no first page, so `journal` reads "Frontiers in Plant Science 6: 207", taken from the DOI suffix and the batch file. Vernalization responses are logged as `sense_thermal`, photoperiod classes and photoreceptor gene content as `sense_light_nonvisual`. Species-level values from this review are graded `m` with `partial: true`; group values are `g`.
- Entry 46: gene presence and absence come from the paper's own transcriptome and genome searches (`partial` false); genes reported from earlier cloning or genome projects are `partial`. The reference list is missing from the XML text, so some originals are named by reference number only. Group taxa are written as the paper prints them (hornworts, chlorophytes, ferns).
- Entry 49: `journal` reads "Sensory Nervous System (IntechOpen), chapter 5, pp. 101-126"; the chapter prints page numbers 102 to 126 and its first page (unnumbered) is headed "Provisional chapter". Table 1 activity patterns are from the literature (refs 77 to 79), so the 14 `diel` records are `partial`. Each Table 3 species has two acuity records (hexagonal and square array). Table 4 and the Results give a horizontal streak for Erythrolamprus poecilogyrus while the Discussion says area centralis; both are logged and cross-referenced. Table 1 prints "Spillotes pullatus", kept as printed.
- Entry 51: an NIH author manuscript (NIHMS1971931); every record's note says so. Opsin localization is logged under `receptor_classes` with a string value naming the opsins, and the method says it predicts spectral classes without measuring them.
- Entry 62: oil droplet proportions are the Results' right-eye means; the abstract's rounded percentages are not logged again.
- Entry 74: the eScholarship PDF is the journal's typeset version, not a preprint. Figure 1's per-study effect sizes are graphical only and are not logged.
- Entry 75: published version in PMC. Its own results are model predictions, logged as four `i` records with method "a prediction, not a measurement"; the measured facts it cites are `partial`.

## Deviations from the prompt

- The key pair lives in `/tmp/oa-b`, not `/tmp/oa`, so that a second reader on the same machine cannot overwrite it. It was never committed or printed.
- The oa-run branch is `run/oa/read-b`; reading was done on `agent/oa-read-b` from `main` as asked.

Nothing was left unread.
