# audit-167: desk-d77 (2 evidence records, no search records, no wanted lines)

Audited 29 October 2026 from the desk-d77 files copied untracked into the worktree (progress note and 2 evidence lines; neither is committed here). Mechanical gate: `screen_candidates.py --check` with empty searched and wanted files prints "0 problems". Duplicates: git grep on origin/main (765e4050) finds no evidence for any Lagerstroemia or Spathodea taxon and no copy of either source, so neither line repeats or contradicts main. Quote lengths counted here: 66 and 65 characters; each is one whole sentence, verbatim, reporting the study's own result. 8 WebSearches used.

| line | taxon / trait | verdict | reason |
|---|---|---|---|
| 1 | Lagerstroemia speciosa / diel | OK | SJST article page (opened) prints Vinod Prasad Khanduri as sole author, 36(4): 389-396, 2014, title as filed, no DOI. Quote is abstract sentence 4, verbatim; "2.5 to 3.0 hours for complete opening" (sentence 5), anther dehiscence half an hour after anthesis (6) and the three-month flowering period (3) are carried; the remaining sentences (pollinators, visitation rates, alternate-year pollen, fruit set) bear on no diel reading, and nothing in value or conditions goes beyond the abstract. Time of anthesis and flower opening is the owner's plant diel reading (flower opening), not a leaf or other rhythm. POWO 553618-1 (opened): Lagerstroemia speciosa (L.) Martyn, species, "This species is accepted"; the accepted name's own id. m and partial hold |
| 2 | Spathodea campanulata / sense_light_nonvisual | OK (fault noted) | Lincoln research archive record (opened) gives the abstract; quote is sentence 8 of 9, verbatim. Compensation point below 10 umol, positive carbon gain at 50 umol in shade, light for maximum photosynthesis averaging 260 umol (below 13% of full sun) are in sentences 5 and 7 and carried; the last sentence is an inference about persistence, not a result. Shade against sun growth comparison counts as a set-light trial under the owner's readings. POWO urn:lsid:ipni.org:names:110661-1 (opened): Spathodea campanulata P.Beauv., species, "This species is accepted"; the accepted name's own id. m and partial hold |

Faults noted, not counted:
- Line 2: the publisher page could not be read. Both bioone URLs my search returned (bioone.org and complete.bioone.org, 10.2984/68.3.4) gave only page metadata, zendy returned nothing and HAL hal-01122865 returned an Anubis block. The sciencegate page (opened) prints Sébastien Larrue, Curtis Daehler, Franck Vautier, Jennifer L Bufford in that order, volume 68, issue 3, pages 345-358, 2014, matching the record's authors, order, volume and issue. The DOI 10.2984/68.3.4 appears in the bioone URL path. The omitted page range is not an error (the rule counts a missing range only when the publisher prints it otherwise), but authors, issue and pages remain unconfirmed against the publisher itself.
- Line 2: "very low light" in value paraphrases "positive carbon gain at 50 umol photons" (about 2.5% of full sun by sentence 6); the conditions give the numbers, so this is wording, not an overstated result.

Evidence errors: 0 of 2 (0%). Error lines: none.
Search records: none in the unit (0 of 0). Wanted lines: none.

Pooled with audits 162 to 166: 5 of 20 evidence records (25.0%; audit 162 1 of 2, audit 163 2 of 3, audit 164 2 of 5, audit 165 0 of 4, audit 166 0 of 4, audit 167 0 of 2).

Verdict: pass. Both lines can be merged.

Blocked or left alone: bioone (metadata only), HAL (Anubis), zendy (empty). Scribd results and the Frankfurt repository were left alone. No library proxy, ResearchGate, academia.edu or Sci-Hub page opened; no paper text committed.

Stray files: none committed; the desk-d77 copies stay untracked.
