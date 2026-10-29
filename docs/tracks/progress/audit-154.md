# audit-154: desk-d63 (23 evidence records, 3 wanted lines)

Audited 29 October 2026 against origin/research/desk-d63 (merge-base diff: progress note, 23 evidence lines, 3 wanted lines; no stray files). Every source checked on a publisher, repository or indexer page reached through a WebSearch result; about 45 WebSearches used. Duplicates grepped against docs/views/evidence/*.jsonl on main and origin/research/desk-d64 (16 lines): no DOI shared, no taxon shared with d64; Zostera marina (desk-d60, other DOI) and Cereus jamacaru (desk-d56, oa-10) are different papers or species, so no repeat.

| line | taxon | verdict | reason |
|---|---|---|---|
| 1 | Cuscuta pentagona | OK | Science 313(5795): 1964-1967, DOI and authors as printed (Penn State page); quote verbatim, 105 chars; abstract names C. pentagona; POWO 72922-2 "This species is accepted" (lists C. campestris only as an alternative-taxonomy name) |
| 2 | Vallisneria americana | OK | CSIRO page matches 55(8): 749-758; quote verbatim, 122 chars; 70%/9% in value from the next abstract sentence |
| 3 | Orobanche aegyptiaca | OK | Plant Growth Regul 81(2): 221-230 as printed; quote verbatim, 83 chars; abstract writes Phelipanche aegyptiaca (syn. O. aegyptiaca); POWO 662086-1 and WFO wfo-0000388672 both accept Orobanche aegyptiaca Pers. |
| 4 | Santalum album | OK | Cent Eur J Biol 9(11): 1108-1116 (De Gruyter PDF header); quote verbatim, 124 chars; GA3 on living seeds |
| 5 | Cereus repandus | OK | Seed Sci Res 32(3): 166-174, authors X-Y. Yang, Hugh W. Pritchard; quote verbatim, 56 chars; POWO 130627-1 accepted (C. jamacaru not among its synonyms; POWO accepts C. jamacaru separately) |
| 6 | Cereus repandus | OK | same paper; distinct finding (light dose saturating germination, 5 min per day for 4 d), not a repeat of line 5; quote verbatim, 100 chars |
| 7 | Posidonia oceanica | OK | MEPS 215: 107-120 as printed; quote verbatim, 106 chars; imposed in situ light reduction in replicated plots (SS and MS treatments), not a natural gradient; 70 to 80% survival matches |
| 8 | Halodule wrightii | OK (issue unconfirmed) | Estuaries 15: 214-217 and DOI match Springer page; the page prints no issue, so "15(2)" could not be confirmed; quote verbatim, 118 chars; neutral density screens |
| 9 | Thalassia testudinum | OK (flag) | GoMS 23(2), start page 7, DOI and authors match; polyethylene mesh to about 40% of ambient; quote verbatim, 124 chars; note the quoted effect is not significant |
| 10 | Elodea canadensis | OK | Front Plant Sci 10, DOI and six authors in order; five set light intensities; source measured exactly E. canadensis and E. nuttallii; quote verbatim, 87 chars |
| 11 | Elodea nuttallii | OK | as line 10 |
| 12 | Pedicularis olympica | OK | Turk J Bot 34(3): 225-232; quote verbatim, 31 chars; 250 ppm, 64% dark and 75% photoperiod match; POWO 807420-1 accepted |
| 13 | Zostera marina | OK | PLoS ONE 8(11): e81058, five authors in order; in situ PVC mesh screens at 24, 40, 75% attenuation; pooled over exactly the two species measured; quote verbatim, 75 chars |
| 14 | Cymodocea nodosa | OK | as line 13 |
| 15 | Halocnemum strobilaceum | OK | Ann Bot 101(2): 293-299, authors as printed; quote verbatim, 102 chars; POWO 165766-1 accepted |
| 16 | Elodea nuttallii | OK | Hydrobiologia 734: 159-170, sole author; quote verbatim, 92 chars; E. nuttallii branching finding, distinct from line 17 and from line 11 |
| 17 | Myriophyllum spicatum | OK | same paper; pooled growth-rate sentence over the two species studied, distinct claim from line 16; quote verbatim, 98 chars |
| 18 | Myriophyllum spicatum | OK | Aquatic Ecology 56(1): 89-98 (online 2021, issue 2022), ten authors in order, DOI on OUCI; red, blue, white LEDs against a control; quote verbatim, 93 chars |
| 19 | Orobanche ramosa | OK | J Cent Eur Agric 15(4): 72-82, authors and DOI as printed; quote verbatim (page has a double space), 65 chars; sentence pools exactly P. ramosa and P. purpurea of 11 species tested; accepted name: see below |
| 20 | Orobanche purpurea | OK | as line 19 |
| 21 | Orobanche foetida | OK (POWO unconfirmed) | Weed Research 48: 163-168, authors and DOI as printed (IRIS Unina); quote verbatim, 77 chars, "It" is the fenugreek crude root exudate; WFO wfo-0000387823 accepted (Dec 2023 snapshot); POWO page not found by search |
| 22 | Cuscuta campestris | OK | Plant Growth Regul 105: 1157-1167; quote verbatim, 122 chars; the authors' own plate trials with 1 uM GA3 and MeJA; POWO synonym page 72759-2 says "synonym of Cuscuta campestris" (accepted) |
| 23 | Viscum coloratum | OK (fault noted) | J Plant Biotechnol 35(1): 47-53, DOI and authors as printed; quote verbatim, 121 chars; WFO accepts Viscum coloratum with V. album var. and subsp. coloratum as synonyms; GBIF backbone accepts it; POWO 552303-1 blocked. Fault: the WFO ID cited (wfo-0000424975) is Viscum alni-formosanae, a synonym whose page points to V. coloratum |

Errors: 0 of 23 (0%). Pooled with audits 150 to 153 not recomputed here.

Names: Orobanche aegyptiaca accepted on POWO and WFO. Orobanche ramosa: WFO wfo-0000387703 accepted; POWO 662640-1 blocked, but POWO's Phelypaea ramosa page says "synonym of Orobanche ramosa". Orobanche purpurea: POWO 662628-1 "This species is accepted" and POWO's Phelipanche purpurea page says "synonym of Orobanche purpurea"; WFO wfo-0000387561 accepted. Both names are accepted on POWO, the authority the unit used.

Unconfirmed names: Orobanche foetida on POWO (WFO accepts); Viscum coloratum on POWO (WFO and GBIF accept).

Wanted lines (3): all OK. Jamil et al. 2022 Plants 11(8): 1045, 10.3390/plants11081045, ten authors in printed order (KAUST page); Magnani and Cardoso 2023 Plants 12(24): 4127, 10.3390/plants12244127; Hu et al. 2022 Plants 11(13): 1777, 10.3390/plants11131777.

Blocked: WebFetch permission not answered for degruyterbrill html, frontiersin /full, POWO 662640-1 and 552303-1; worldfloradb.net and biolib.cz behind bot checks. No library proxy, ResearchGate, academia.edu or Sci-Hub page opened.

Stray files: none (desk-d63.jsonl copy in the worktree root is untracked and not committed).
