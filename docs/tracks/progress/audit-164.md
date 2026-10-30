# audit-164: desk-d74 (5 evidence records, no search records, 1 wanted line)

Audited 29 October 2026 from the desk-d74 files copied untracked into the worktree (progress note, 5 evidence lines, 1 wanted line; none is committed here). Mechanical gate: `screen_candidates.py --check` with an empty searched file and the unit's wanted file prints "0 problems". Sources checked on Cambridge Core, DOAJ, the Serbian Biological Society abstract page, doi.org and POWO, reached through WebSearch results or the records' own URLs; 9 WebSearches used. Duplicates: git grep on origin/main (fbf5094f) finds none of the three DOIs, no Avena fatua record, no Balanites, and no Centaurium evidence. Main holds one Thlaspi arvense record (sweep-18#8, sense_light_nonvisual, vernalization and day length for flowering); line 2 is a germination light/dark trial from another paper, so it neither repeats nor contradicts it. The Centaurium null search records on main (sweep-47:10, harvest-c22) are search records, not evidence. Quote lengths counted here: 51, 96, 111, 75 and 99 characters; each is one whole sentence, verbatim in the abstract (checked sentence by sentence on the publisher or DOAJ page).

| line | taxon / trait | verdict | reason |
|---|---|---|---|
| 1 | Thlaspi arvense / sense_chemical | ERROR | Citation holds: Cambridge Core page (opened) prints Saini, Bassi, Goudey, Spencer in order, Weed Science 35(6): 802-806, 1987, DOI 10.1017/S0043174500079376, title as filed; quote verbatim, the article's own abstract. The fault is an omitted conditional hormone result: the abstract's GA3 sentence ("Gibberellic acid3 (GA3) was promotive under isothermal conditions, but its effectiveness was enhanced..." by a temperature shift) is carried in neither value nor conditions. The value lists GA4+7, ethephon plus GA3, water, KNO3, kinetin and ethephon alone, and the quote is the ethephon-plus-GA3 sentence, so the record reads as if GA3 needed ethephon, while the study reports GA3 alone promotive with a temperature dependence (audit 162 rule) |
| 2 | Thlaspi arvense / sense_light_nonvisual | OK (fault noted) | Same citation, confirmed. Quote and the KNO3-light-shift sentence verbatim. Water gave no germination under any condition, so light alone is covered by "no germination in water". Germination light/dark trial, owner reading 10(d)/(e); m and partial hold |
| 3 | Avena fatua / sense_chemical | OK | Cambridge Core (opened) prints Saini, Bassi, Spencer, Weed Science 34(1): 43-47, 1986, DOI 10.1017/S0043174500026424, title as filed. Quote and the "Both chemicals ... additive" sentence verbatim. The abstract's decline in response with temperature and after-ripening, the continued responsiveness of seed kept dormant, and the above-90% combinations are all carried. POWO 391443-1 (opened) is Avena fatua L., species, accepted |
| 4 | Centaurium erythraea / sense_light_nonvisual | OK | DOAJ (opened) prints Mijajlović, Grubišić, Giba, Konjević, Archives of Biological Sciences 57(1): 25-28, 2005, DOI 10.2298/ABS0501025M; the Serbian Biological Society page (opened) gives the same four in order. Quote and "Seeds did not germinate in darkness." verbatim; the abstract prints no temperature, as the conditions say. POWO urn:lsid:ipni.org:names:326619-2 (opened) is Centaurium erythraea Rafn, species, accepted, the species' own id |
| 5 | Centaurium erythraea / sense_chemical | ERROR | Citation and quote hold (verbatim, 99 characters). The value misstates the rescue: it says abscisic acid and growth retardants inhibited light-induced germination "and the inhibition was overcome by adding gibberellic acid", but the abstract (Serbian Biological Society page, opened) says "Growth retardant-caused inhibition can be overcome by the addition of gibberellic acid." and reports no reversal of the abscisic acid inhibition. The value extends a result to a treatment the study does not report it for |

Evidence errors: 2 of 5 (40%). Error lines: 1, 5.
Search records: none in the unit (0 of 0).

Pooled with audits 160 to 163: 5 of 16 evidence records (31.3%; audit 160 0 of 2, audit 161 0 of 4, audit 162 1 of 2, audit 163 2 of 3, audit 164 2 of 5).

Verdict: fail on lines 1 and 5. Lines 2, 3 and 4 can be merged. Line 1 can be refiled with the GA3-alone result (promotive under constant temperature, enhanced by the temperature shift) in value; line 5 with the gibberellic-acid reversal limited to the growth retardants.

Wanted line 1 (Balanites aegyptiaca, 10.15258/SST.2003.31.3.10): doi.org page (opened) prints the title as filed, publication date 1 October 2003, and the quoted null sentence verbatim; it prints no authors, volume, issue or pages, so the empty author field is correct. Faults noted, not counted: the journal and issue "Seed Science and Technology 31(3)" rest on the DOI string, not on a page that prints them; the page names Seed Science and Technology only in a general description.

Faults noted, not counted:
- Line 2: conditions leave out that the 12 C sensitivity held through 15 days and was lost within 3 days at 22 C; these bear on temperature, not on the light result.
- Line 2: GA4+7 gave 100% germination in the dark (the light requirement is bypassed by gibberellin); this is carried in line 1, not here.
- Line 3: the abstract's decline sentence is garbled in the source ("reponse", incomplete); the record's paraphrase follows its sense.

Blocked or left alone: PMC10761227 (redirect, not followed; the desk reported reCAPTCHA). typeset.io, peeref, bohrium and worldfloradb results were left alone. No library proxy, ResearchGate, academia.edu or Sci-Hub page opened. The bib-bvb catalogue result was not opened.

Stray files: none committed; the desk-d74 copies stay untracked.
