# Precision audit 34, 18 October 2026

Scope: the corrected records in `docs/views/evidence/recheck-42-fixed.jsonl` to `recheck-52-fixed.jsonl` (499 lines), in their latest versions. Records are named `recheck-N-fixed:LINE`, which is also the id that `docs/views/audit/ALL.jsonl` and `recheck-53-fixed.jsonl` use.

Population: ALL.jsonl holds 247 `retract` rows for ids in these files, and recheck-53-fixed.jsonl holds 247 journal-field corrections whose `rechecked` field names exactly those ids. Each retracted id was therefore replaced by its recheck-53 version, and no id was left without a later correction, so the population is 499 records. `docs/views/fixes/requote-partial.jsonl` was applied as an override that sets `partial` to true. The branch `origin/research/repair-crossref` does not exist on the remote; the worktree was cut from the local branch `research/repair-crossref` (d9acde5c), which is the tip of that work.

Draw: `random.seed(34)`, `random.sample` of 35 positions from the 499 records (file order, then line order). The first 20 are the audit sample; the last 15 were checked because the first 20 held errors. None of the 35 had been checked in audit 33. The draw falls in ten files (42, 43, 45, 46, 47, 48, 49, 50, 51, 52).

Method as in audits 16 and 33: WebSearch on the title, then WebFetch on a URL the search returned (or a page that returned page links). The fetch tool limits each quoted passage to about 125 characters, so every quote was read back in consecutive pieces. No library login, proxy, Sci-Hub, LibGen, academia.edu or ResearchGate page was opened, and no paper text is committed. A record whose paper would not open is `unverifiable`.

## First 20

| # | record | taxon / trait | grade | verdict | note |
|---|---|---|---|---|---|
| 1 | recheck-47-fixed:63 | Anolis cristatellus / fovea | m | error (grade) | verbatim and complete (Frontiers, section 4.6). The paragraph covers the anoles of the study as a group (A. carolinensis, A. cristatellus, A. sagrei) and names no species, so `m` for one species is wrong; it should be `g` |
| 2 | recheck-46-fixed:10 | Heliophobius argenteocinereus / behaviour_vision | m | unverifiable | PMC shows a browser check; Europe PMC and PLoS refused; the JCU repository holds only the thesis abstract |
| 3 | recheck-48-fixed:6 | Amphiprion akindynos / opsin_coexpression | g | confirm | verbatim and complete (JEB Silverchair, "this Review"); five authors, 223(8): jeb193334; `partial` true from the override |
| 4 | recheck-42-fixed:15 | Ptilotrigona occidentalis / eye_topography | m | error (grade) | verbatim and complete. The paragraph is about all eight species (the sentences around it use T. pipioli and P. occidentalis only as the ends of a range), so the value is a group statement and `m` is wrong |
| 5 | recheck-51-fixed:15 | Vicugna pacos / fovea | g | error | IntechOpen chapter, section 1.1.2; sentence verbatim and complete. The chapter carries no `partial` and the override does not list it. The journal field "IntechOpen, in Sensory Nervous System" gives no pages (the chapter prints none) |
| 6 | recheck-45-fixed:19 | Hasarius adansoni / opsin_localization | m | error (value) | the quote is verbatim and complete (section 3.3, lateral eyes): RH2 and RH3 were not localized in the ALE retina. The record's value says "RH3/RH4: not localized", but the paper reports RH3/RH4 as the label that did cover the whole PME retina. Value and quote disagree |
| 7 | recheck-52-fixed:16 | Deilephila elpenor / contrast_threshold_percent | m | confirm | verbatim and complete (KOPS copy); three authors; 26(6): 821-826 |
| 8 | recheck-42-fixed:16 | Apis dorsata / diel | g | confirm | verbatim and complete, Results; the sentence cites Somanathan et al. 2009b, so `g` is conservative |
| 9 | recheck-52-fixed:7 | Deilephila elpenor / optical_sensitivity_ratio | i | confirm | verbatim and complete (KOPS copy) |
| 10 | recheck-46-fixed:27 | Podiceps cristatus / diel | g | confirm | the core clause and the rest read verbatim in the open PDF; the "(…)" marks the omitted Newbrey et al. citation. Two authors, 31(2): 110-124. The journal field prints "Ornis Hungarica31(2)" with the space missing (typographic) |
| 11 | recheck-46-fixed:14 | Heliophobius argenteocinereus / behaviour_vision | m | unverifiable | same paper and blocks as #2 |
| 12 | recheck-52-fixed:44 | Crotalus durissus / fovea | m | confirm | verbatim and complete (Frontiers PDF, Results); the sentence is about C. durissus; three authors |
| 13 | recheck-52-fixed:41 | Bothrops jararaca / fovea | m | confirm | verbatim and complete; adults of B. jararaca |
| 14 | recheck-43-fixed:13 | Pelodiscus sinensis / opsin_status | g | error (journal) | quote verbatim and complete ("Turtle Visual Opsins", all four turtles, so `g` is right). Journal field "34: 666-676" lacks the issue (34(3)) |
| 15 | recheck-47-fixed:10 | Photinus scintillans / diel | g | confirm | the sentence opens "In one study ... fireflies, Cronin et al (45) found ..."; the leading ellipsis marks the cut, the rest is verbatim to the full stop. Two species pooled, `g`; annual review, `partial` true from the override; 46(1): 471-510 |
| 16 | recheck-52-fixed:45 | Crotalus durissus / fovea | m | confirm | same sentence as #12; the value "visual streak" rests on the cone clause |
| 17 | recheck-45-fixed:58 | Ranitomeya imitator / opsin_gene_recovery | m | error | the sentence is verbatim and complete (UCL PDF, Results) but speaks of "all four species of Dendrobatidae" in the dataset, and the next sentence gives the per-species evidence. A group statement is `g`, not `m`. The authors field also ends "et al., Bell RC" with six names; the paper prints 29 authors, so the list is incomplete |
| 18 | recheck-46-fixed:2 | Fukomys mechowii / behaviour_vision | m | unverifiable | same paper and blocks as #2 |
| 19 | recheck-43-fixed:28 | Alligator sinensis / opsin_status | m | error | quote verbatim and complete ("Light-Associated Gene Loss ..."). It states "shared among all four crocodylian species" and names none, so `m` is wrong (`g`). Journal field lacks the issue |
| 20 | recheck-47-fixed:54 | Glycine max / sense_light_nonvisual | g | confirm | verbatim and complete (Frontiers review, soybean subsection); `partial` true from the override. The authors field prints "Weller James L, Ortega Raúl" (given names after surnames), a formatting slip; both names are present |

First 20: 5 unverifiable, 15 verifiable, 7 errors (1 journal-only).

## Extension, 15 more

| # | record | taxon / trait | grade | verdict | note |
|---|---|---|---|---|---|
| 21 | recheck-51-fixed:5 | Parabuteo unicinctus / blind_area_above_head_deg | m | error (journal) | verbatim and complete (Silverchair), 75±5 deg is the Harris's hawk value. Journal field "219:2639-2649" lacks the issue (219(17)) |
| 22 | recheck-43-fixed:59 | Vicia faba / sense_light_nonvisual | g | confirm | verbatim and complete (RERO PDF); an original phylogenetic analysis, so no `partial` is needed; two species pooled, `g`; 61(4): 559-569 |
| 23 | recheck-43-fixed:29 | Crocodylus porosus / opsin_status | m | error | same sentence as #19; group statement graded `m`; journal lacks the issue |
| 24 | recheck-45-fixed:42 | Menemerus confusus / lambda_max_nm | g | error (quote) | the page sentence runs on after "Yamashita and Tateda, 1976)" with "and Plexippus validus (535 nm in PLEs; Hardie and Duelli, 1978), matching the molecular studies ... (Terakita and Nagata, 2014)." The quote stops there with no ellipsis. This is the same fault audit 33 found in recheck-45 L43 |
| 25 | recheck-46-fixed:5 | Fukomys mechowii / behaviour_vision | m | unverifiable | same paper and blocks as #2 |
| 26 | recheck-49-fixed:8 | Ancestor Serpentes / lambda_max_nm | i | confirm | verbatim and complete (City accepted manuscript, Results); a predicted value from ancestral reconstruction, so `i` is right; ten authors match; 33(10): 2483-2495. The page is the accepted manuscript, not the printed pages |
| 27 | recheck-42-fixed:1 | Trigonisca pipioli / eye_type | g | confirm | verbatim and complete (Introduction); cites Land 1997; 202(9-10): 643-655 |
| 28 | recheck-50-fixed:56 | Deinopis spinosa / sense_hearing | m | confirm | the UNL page prints the Summary sentence verbatim; the record has `partial` true for an abstract read. Five authors, 30(24): 5033-5039.e3 |
| 29 | recheck-50-fixed:44 | Copilia / eye_role | g | confirm | verbatim from "such as Pontella ..." to "(see Land & Nilsson, 2006)", leading ellipsis marks the cut; a Perspective article, `partial` true from the override; 30(1-2): 5-20 |
| 30 | recheck-47-fixed:61 | Anolis carolinensis / fovea | m | error (grade) | same sentence as #1; a group statement graded `m` |
| 31 | recheck-43-fixed:24 | Crocodylus porosus / opsin_status | m | error | "In all four sampled crocodylian species, I recovered ..." is verbatim and complete, but it is a group statement graded `m`; the journal field lacks the issue |
| 32 | recheck-50-fixed:69 | Neofelis nebulosa / tapetum | m | confirm | verbatim and complete (Springer). The sentence gives the clouded leopard its own value ("milky blue"), so `m` holds. The page truncates the author list ("Show authors"), so the record's six names could not be compared with the full list |
| 33 | recheck-43-fixed:11 | Chelonia mydas / opsin_status | m | error | the sentence names two species ("Chrysemys picta and Chelonia mydas, possess all five visual opsins"), so `m` for C. mydas alone is wrong (`g`). Journal field lacks the issue |
| 34 | recheck-46-fixed:17 | Spalax ehrenbergi / eye_type | g | unverifiable | same paper and blocks as #2 |
| 35 | recheck-45-fixed:32 | Menemerus bivittatus / opsin_localization | m | confirm | verbatim and complete (section 3.3, PMEs); seven authors; 217: 108367 |

Extension: 2 unverifiable, 13 verifiable, 6 errors (1 journal-only).

## Error rate

- First 20: 7 errors in 15 verifiable records (46.7%).
- Both draws: **13 errors in 30 verifiable records, 43.3%** (5 of 35 unverifiable, all from one paper, Kott et al. 2010).
- Excluding journal-only faults (records 14 and 21): **11 errors in 30, 36.7%**.
- The 5% threshold is not met on any counting.

## Distinct fault patterns

1. **Group statement graded `m`** (records 1, 4, 17, 19, 23, 30, 31, 33). The quote speaks of several species, a genus or "all four species" and the record gives one of them the `m` grade. This is the largest pattern, 8 of the 13 errors.
2. **Journal field lacks the issue** (14, 21, plus 19, 23, 31 and 33 as a second fault). The Emerling records print "34: 666-676" (issue 3) and the Potier record "219:2639-2649" (issue 17). Recheck-53 added volume and issue to 247 records but did not reach these.
3. **Unmarked cut at the 40-word limit** (24). The quote ends mid-sentence with no ellipsis, as in audit 33 for recheck-45 L43.
4. **Missing `partial` on a book chapter** (5). The IntechOpen chapter is neither flagged in the record nor listed in `requote-partial.jsonl`; its journal field has no pages.
5. **Value contradicts the quote** (6). The record names RH3/RH4 as not localized where the paper reports RH2 and RH3 not localized in the lateral eyes and RH3/RH4 present in the PMEs.
6. **Truncated author list** (17). "et al." stands in for 23 of 29 printed authors.
7. Noted, not counted: author names written surname-first in a given-name slot (20); a missing space in the journal string (10); `partial: true` on records whose full text was read (7, 9); an author list that the page truncated (32).

## Blocked pages

- pmc.ncbi.nlm.nih.gov (browser check) for Kott et al. 2010 and for Carleton et al. 2020 (the Silverchair page opened instead); Europe PMC REST and doi.org/10.1371 (permission step not answered); the JCU repository returned only the thesis abstract.
- hal.umontpellier.fr (bot protection) for Potier et al.; the Silverchair page opened instead.
- The Springer page for the Klećkowska-Nawrot paper hides part of the author list.

No evidence file was edited and no correction rows were written.
