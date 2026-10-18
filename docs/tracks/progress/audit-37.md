# Precision audit 37, 18 October 2026

Scope: the latest version of each record in `docs/views/evidence/recheck-42-fixed.jsonl` to `recheck-52-fixed.jsonl`. A record retracted in `docs/views/audit/ALL.jsonl` is replaced by its correction in recheck-53-fixed (journal), recheck-54-fixed (grade), recheck-55-fixed (strict review) or recheck-56-fixed (journal names, issues, pages), and a retraction with no correction removes the record. The rebuilt population is 493 records, one per origin record in files 42 to 52, ordered by origin file and line. `docs/views/fixes/requote-partial.jsonl` was applied as a `partial: true` override (it lists origin ids). The worktree was cut from `research/repair-crossref` (af1e917c).

Draw: `random.seed(37)`, `random.sample(range(493), 493)` as the order. Skipped: Kott et al. 2010 and any record whose origin family appears in audits 33 to 36 (the files for 34 to 36 were read with `git show`; audit 33 names records as `recheck-N Lline`). The first 20 usable records fall in nine origin files (42, 43, 45, 46, 47, 49, 50, 51, 52). Because errors were found, the next 15 usable records were also checked (35 in all; the extension adds origin file 48). Records are named by latest id, with the origin id in brackets.

Method as in audit 16: WebSearch on the title, then WebFetch on a page the search or the record returned. The fetch tool returns about 125 characters per quote, so every quote was read back in consecutive pieces. No library login, proxy, Sci-Hub, LibGen, academia.edu or ResearchGate page was opened, and no paper text is committed. Open-access publisher, university-repository and journal pages only.

## First 20

| # | record | taxon / trait | grade | verdict | note |
|---|---|---|---|---|---|
| 1 | recheck-53-fixed:153 [50:12] | Cupiennius salei / receptor_classes | g | confirm | verbatim, p. R977 (author PDF). Magazine overview, `partial` true from the override. Current Biology 30(17): R975-R980 (first and last page checked on the PDF) |
| 2 | recheck-49-fixed:9 [49:9] | guinea pig / lambda_max_nm 420 | g | confirm | the full sentence runs 42 words; the record quotes the first clause with a marked ellipsis, verbatim (City accepted manuscript). Ten authors match; 33(10): 2483-2495 |
| 3 | recheck-43-fixed:26 [43:26] | Alligator sinensis / opsin_status | i | error (journal) | verbatim and complete, p. 668. Journal field "Molecular Biology and Evolution 34: 666-676" lacks the issue (34(3)) |
| 4 | recheck-52-fixed:39 [52:39] | Morpho peleides / diel | g | confirm | verbatim abstract sentence (Lund record); 211(6): 844-851; abstract, `partial` true |
| 5 | recheck-53-fixed:144 [50:3] | Araneae / eye_type | g | confirm | verbatim, p. R976, with the curly quotes round "camera"; override `partial` true |
| 6 | recheck-51-fixed:19 [51:19] | Thamnophis sirtalis / fovea | g | confirm | verbatim, section 1.2 of the IntechOpen chapter; a cited-study value (Wong), so `g`; chapter, `partial` true from the override; three authors; the chapter prints no pages |
| 7 | recheck-49-fixed:22 [49:22] | Otus asio / motion | i | confirm | verbatim, p. 66, Discussion; the sentence names no species and speaks for both owls, so `i` is safe; 18(2): 62-66 |
| 8 | recheck-55-fixed:1 [42:19] | Vaccinium myrtillus / sense_chemical | m | confirm | verbatim, Results, "Reproductive output" (Frontiers); the sentence is about bilberry only; two authors; 12: 1347837 |
| 9 | recheck-55-fixed:31 [47:19] | Apis mellifera / receptor_classes | g | confirm | verbatim, p. 486 (author PDF); cites (106), review, `partial` true |
| 10 | recheck-54-fixed:98 [47:65] | Anolis sagrei / fovea | g | confirm | verbatim, section 4.6, p. 12; the sentence names no species (all three anoles of the study), `g` is right; 2: 1410763 |
| 11 | recheck-53-fixed:208 [50:67] | Deinopis spinosa / sense_hearing | i | confirm | verbatim, Discussion p. 14 ("we expect"), so `i`; five authors; 30(24): 5033-5039.e3 |
| 12 | recheck-54-fixed:34 [43:35] | Alligator mississippiensis / opsin_status | g | error (journal) | verbatim and complete, p. 672, a group statement (four crocodylians) so `g`. Journal field lacks the issue (34(3)). Noted, not counted: "Both genes" points back to OPNPP and OPNPT in the sentence before, so the quote alone does not say which gene |
| 13 | recheck-52-fixed:54 [52:54] | Crotalus durissus / diel | g | confirm | verbatim with the two marked cuts (Figure 5 and Table 2 citation, closing citation); two species and cited activity patterns, `g`; three authors; Front Neuroanat 15: 770804 |
| 14 | recheck-53-fixed:109 [47:28] | Apis mellifera / opsin_genes | g | error (quote) | the Figure 6 caption on p. 488 reads "Several distinct opsin cDNAs or genes from the same organism have been isolated (e.g. three from Apis mellifera ...)"; the record's quote has "(10)" after "organism". Read twice; the caption holds no parenthesised number. A reference number was carried into the quote |
| 15 | recheck-49-fixed:5 [49:5] | Helicops angulatus / opsin_polymorphism | m | confirm | verbatim and complete; the paper's own finding for this species |
| 16 | recheck-54-fixed:119 [50:70] | Panthera leo / tapetum | g | confirm | verbatim and complete (Springer); the sentence covers clouded leopard and lions together, `g`; 22(1): 329. The page truncates the author list ("Show authors"); the six names shown match |
| 17 | recheck-45-fixed:47 [45:47] | Dermochelys coriacea / visual_field_area | m | confirm | verbatim and complete, p. 72 (journal PDF copy on a bycatch library); species-level area from n = 5 leatherbacks, so `m`; three authors; 41: 67-77 |
| 18 | recheck-46-fixed:22 [46:22] | Chamaeleonidae / lambda_max_nm | g | confirm | the abstract sentence as shown on an open abstract mirror (en dash printed as a hyphen); four species pooled; 191(10): 925-932; abstract, `partial` true. The Springer and PMC pages refused, so the sentence was read through a summary |
| 19 | recheck-53-fixed:180 [50:39] | Strombus / eye_role | g | confirm | verbatim and complete (Cambridge PDF); a Perspective, `partial` true from the override; 30(1-2): 5-20 |
| 20 | recheck-53-fixed:92 [47:11] | Photinus scintillans / filter_pigments | g | confirm | verbatim; the page is 479, matching the record; two firefly species, `g` |

First 20: 0 unverifiable, 20 verifiable, 3 errors (2 journal-only).

## Extension, 15 more

| # | record | taxon / trait | grade | verdict | note |
|---|---|---|---|---|---|
| 21 | recheck-53-fixed:103 [47:22] | Papilio xuthus / filter_pigments | g | confirm | verbatim, p. 477; species named earlier in the paragraph |
| 22 | recheck-43-fixed:53 [43:53] | Crocodylus porosus / lambda_max_nm | i | error (journal) | verbatim and complete; the PDF prints the Greek letter as "k", so "kmax" matches the page; predicted value, `i`. Journal field lacks the issue (34(3)). The sentence is on p. 668 (record: 669) |
| 23 | recheck-50-fixed:72 [50:72] | Megalopta genalis / diel | g | confirm | verbatim and complete, p. 349 (Smithsonian PDF); three authors; 18(5): 349-353. The sentence is an opening description that gives the species its own value; `g` is the safe side of `m` |
| 24 | recheck-55-fixed:87 [52:23] | Deilephila elpenor / absolute_sensitivity | g | confirm | verbatim and complete (KOPS copy), on p. 824 (record: 823); three authors; 26(6): 821-826 |
| 25 | recheck-51-fixed:17 [51:17] | Loxodonta africana / fovea | g | confirm | the excerpt is verbatim with the sloth clause cut and marked; the full sentence ends after the fish clause. Noted, not counted: "This specialization" is the vertical streak of the sentence before, which the quote does not carry |
| 26 | recheck-54-fixed:15 [43:5] | Chrysemys picta / opsin_status | g | error (journal) | verbatim and complete, a two-species statement, `g`; journal field lacks the issue (34(3)); the sentence is on p. 666 (record: 667) |
| 27 | recheck-52-fixed:52 [52:52] | Crotalus durissus / lambda_max_nm | g | confirm | verbatim and complete; the 360-370 nm is predicted from Bittencourt et al., so `g` |
| 28 | recheck-53-fixed:87 [47:6] | Periplaneta americana / receptor_classes | g | confirm | verbatim from "there are a few cases" with the opening clause cut and marked; p. 478; three taxa listed, `g` |
| 29 | recheck-43-fixed:18 [43:18] | Apalone spinifera / opsin_status | g | error (journal) | verbatim and complete; "All four turtle species", `g`; journal field lacks the issue (34(3)); the sentence is on p. 666 (record: 667) |
| 30 | recheck-54-fixed:68 [45:50] | Caretta caretta / sense_chemical | g | confirm | verbatim and complete, p. 72; the subject is both hatchling species, `g` |
| 31 | recheck-53-fixed:164 [50:23] | Deinopis / f_number | g | confirm | verbatim and complete, p. R979; genus-level statement, `g` |
| 32 | recheck-51-fixed:11 [51:11] | Erythrolamprus poecilogyrus / fovea | m | confirm | verbatim with the trailing clause (O. guibei) cut and marked; the snake's own observation, `m`; section 3.2 |
| 33 | recheck-55-fixed:48 [48:9] | Vaccinium corymbosum / sense_chemical | g | confirm | verbatim abstract sentence; three authors; 35(2): 163-175; abstract, `partial` true |
| 34 | recheck-49-fixed:25 [49:25] | Strix aluco / retinal_composition | g | confirm | verbatim, Introduction p. 62; a finding of earlier studies (Martin), `g` |
| 35 | recheck-53-fixed:165 [50:24] | Deinopis / lens_diameter_mm | g | confirm | same sentence as 31 |

Extension: 0 unverifiable, 15 verifiable, 3 errors (all journal-only).

## Error rate

- First 20: 3 errors in 20 verifiable records (15.0%).
- Both draws: **6 errors in 35 verifiable records, 17.1%** (0 unverifiable; every paper opened, the Chamaeleonidae abstract through a mirror).
- Excluding journal-only faults (records 3, 12, 22, 26, 29): **1 error in 35, 2.9%**.
- The 5% threshold is met only when the Emerling journal faults are set aside.

## Distinct fault patterns

1. **Journal field lacks the issue** (recheck-43-fixed:26, 54-fixed:34, 43-fixed:53, 54-fixed:15, 43-fixed:18). All five are Emerling 2017, printed "Molecular Biology and Evolution 34: 666-676"; the paper is 34(3). Audit 34 found the same string on other Emerling records; recheck-53, 54 and 56 did not reach them. One correction (add "(3)") would clear every record of this paper.
2. **Reference number carried into the quote** (recheck-53-fixed:109). "(10)" is inserted after "organism" in a figure-caption sentence; the caption has no such number.
3. Noted, not counted:
   - Page numbers in `where` are off by one on four records (43-fixed:53 says 669 for 668; 43-fixed:18 and 54-fixed:15 say 667 for 666; 55-fixed:87 says 823 for 824).
   - `partial: true` stands on the Emerling research article, which was read in full (five records).
   - The quote leaves the antecedent outside it for 54-fixed:34 ("Both genes") and 51-fixed:17 ("This specialization").
   - 50-fixed:72 (Megalopta) could carry `m`; `g` is the cautious grade.

No group-statement-graded-`m` fault, unmarked cut, missing `partial`, truncated author list or value mismatch appeared in this draw. The audit 34 patterns that did not recur were already repaired by recheck-54 and recheck-55.

## Blocked pages

- pmc.ncbi.nlm.nih.gov (PMC8825375, PMC1810110): browser check or permission step not answered; the Frontiers PDF served Tashiro et al. instead.
- Europe PMC REST for Frederiksen and Warrant 2008: permission step not answered; the Lund record served the abstract.
- int-res.com PDF, Springer pages for Bowmaker et al. 2005 and the Frontiers HTML for Hegland (the HTML mirror loaded abstract only; the PDF route served the full text); doi.org links: not answered or fetch errors.
- The Bowmaker et al. sentence was confirmed only through an open abstract mirror (altmetric page), which summarises; volume and pages come from a second open listing.

No evidence file was edited and no correction rows were written.
