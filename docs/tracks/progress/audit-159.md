# audit-159: desk-d69 (3 evidence records, no search records, 2 wanted lines)

Audited 29 October 2026 from the desk-d69 files copied untracked into the worktree (progress note, 3 evidence lines, 2 wanted lines; none of the three is committed here). Sources checked on publisher, indexer and POWO pages reached through WebSearch results or the records' own URLs; 9 WebSearches used. Duplicates: git grep on origin/main finds neither DOI (10.17660/ActaHortic.2014.1042.37, 10.4141/p96-108) and no evidence for Galax urceolata or Poa alpina in docs/views, so nothing is repeated or contradicted. Lines 1 and 2 share one paper but file different traits (germination light response and GA3 response) from different abstract sentences, so they do not repeat each other.

| line | taxon | verdict | reason |
|---|---|---|---|
| 1 | Galax urceolata | OK | ishs.org article 1042_37 (opened; doi.org refused by robots): G. Yang, R. Jackson, Z. Lu in order, Acta Hortic 1042: 311-317, 2014, title verbatim, DOI as filed; quote verbatim as a whole sentence, 51 chars, own result with a direction. The abstract lists light intensity as a studied factor alongside medium pH, temperature stratification and seed maturity, and reports the light result on its own, so method and conditions hold. Germination light trial under sense_light_nonvisual. POWO urn:lsid:ipni.org:names:106783-2 (opened) "This species is accepted" for Galax urceolata (Poir.) Brummitt, no family printed |
| 2 | Galax urceolata | OK | Same ishs.org page: quote verbatim as a whole sentence, 118 chars, own result with a direction; the cold-stratification-first condition and the dark-coloured seeds are carried in value and conditions, and the abstract confirms that BA and IBA "at various ratios" inhibited germination. The abstract ties darker seed colour to greater maturity, so "(mature)" is supported. GA3 germination response under the desk extension of sense_chemical. Same POWO id, accepted |
| 3 | Poa alpina | OK (fault noted) | openpolar record (opened; doi.org returned a client error): Michelle Pahl, Barb Darroch, Can J Plant Sci 77(4): 615-622, 1997, title and DOI as filed; quote verbatim as a whole sentence, 120 chars, with "favoured", "and/or" and "12 °C" as printed. The abstract names "alpine bluegrass (Poa alpina L.)", gives 3, 9 and 12 C, dark, 8 h and 18 h, 6, 10 and 14 wk, says dark was not inductive and that lines differed significantly, line 907 needing less induction. It meets the floral-induction rule: one named species, and a stated direction for short days (favoured) and for darkness (not inductive). Grade m holds for three lines of one species. POWO 320036-2 (opened) "This species is accepted" for Poa alpina L. |

Errors: 0 of 3 (0%). Error lines: none.

Pooled with audits 156 to 158: 2 of 21 evidence records (9.5%; audit 156 1 of 13, audit 157 1 of 3, audit 158 0 of 5, audit 159 0 of 3).

Verdict: pass. All three lines can be merged.

Unconfirmed names: none. Every cited POWO id was opened by this audit and belongs to the accepted name itself.

Faults noted, not counted:
- Line 3: "temperature and photoperiod varied together" in conditions reads as confounded; the abstract describes every temperature under every photoperiod, so "crossed" is the accurate word. The value also leaves out the abstract's report that at 3 C all plants flowered after 10 wk under both long and short days, which shows the short-day effect is conditional on temperature; the quoted "and/or" carries that hedge, so it is noted, not counted.
- Lines 1 and 2: the note's remark that the NC A&T page prints 311-318 was not rechecked; the ishs page prints 311-317, as filed.

Wanted lines:
- 1 Teeri 1976: OK as a citation; FAULT in the name claim. bib-bvb record (opened) prints Teeri, J. A., Ecology 57(2): 374-379, March 1976, DOI 10.2307/1934827; scilit (opened) prints the title as filed and confirms the abstract names Saxifraga rivularis, "23 or more h/day" and 0.3 ly/min, and prints the 7 to 9 day sentence with a long dash. The unit's progress note says POWO lists Saxifraga rivularis (228623-2) as a synonym of S. hyperborea. That id (opened) is Saxifraga rivularis var. flexuosa (Sternb.) Engl. & Irmsch., which POWO sinks into S. hyperborea; POWO 30062111-2 (opened) is Saxifraga rivularis L. and states "This species is accepted". POWO and WFO therefore agree, and the hold for an owner ruling rests on a misread id. The wanted line should cite POWO 30062111-2. The WFO id in the line could not be opened here.
- 2 Wein and MacLean 1973: OK as far as it goes. openpolar (opened) prints Wein, Ross W.; MacLean, D. A., Canadian Journal of Botany, 1973, DOI 10.1139/b73-322, the title as filed with the spaced parentheses, and the 60-character sentence verbatim. Volume, issue and pages are not printed on openpolar or scilit and a search for them returned nothing new, so they remain unread, as the line says.

Blocked: doi.org/10.17660/ActaHortic.2014.1042.37 (robots refusal; ishs.org page read instead); doi.org/10.4141/p96-108 (client error; openpolar read instead); powo.science.kew.org/taxon/urn:lsid:ipni.org:names:320036-2 and worldfloraonline.org/taxon/wfo-0000494819-2024-12 (provenance refusals; the short POWO form 320036-2 was read instead). No library proxy, ResearchGate, academia.edu or Sci-Hub page opened; an elogim search result was left alone.

Stray files: none committed; the three desk-d69 copies stay untracked.
