# audit-163: desk-d73 (3 evidence records, no search records, no wanted lines)

Audited 29 October 2026 from the desk-d73 files copied untracked into the worktree (progress note and 3 evidence lines; neither is committed here). Sources checked on CSIRO Publishing, indexer, POWO and WFO pages reached through the records' own URLs or WebSearch results; 5 WebSearches used. Duplicates: git grep on origin/main (380f77dd) finds no "Pimelea ciliata", "pycnantha", "Trachyandra", "Withers", BT9940575, BT9790047 or BT9930321 in docs/views (the only "Slater" hits are a sea slater and Ctenophorus slateri). Nothing is repeated or contradicted. Quote lengths counted here: 104, 88 and 78 characters.

| line | taxon | verdict | reason |
|---|---|---|---|
| 1 | Pimelea ciliata | ERROR | The record's own URL, publish.csiro.au/bt/BT9940575 (opened), prints the citation line "Australian Journal of Botany 42(5) 575 - 585", and the acnpsearch index 42216625 (opened) also gives issue 5. The record files "42: 575-585" and its note says the publisher page prints no issue, so the issue is left out where the page prints one. Everything else holds: the quote is whole and verbatim at 104 characters with a magnitude; the abstract carries "for up to 8 weeks", the 8 h photo- and thermoperiod result, the low photon flux density result and "temperature had no apparent effect", all of which the record carries; ExportCitation (opened) prints Slater AT, Franz PR, Thompson WK; WFO wfo-0001282218 (opened) is Pimelea ciliata, species, accepted, and the id is the species' own. Photoperiod trial under sense_light_nonvisual; m and partial hold |
| 2 | Acacia pycnantha | ERROR | The cited id is a synonym's. list.worldfloraonline.org/wfo-0000201181 (opened) is the snapshot page whose table attaches wfo-0000201181 to Acacia westonii, listed under "Synonyms of Acacia pycnantha", and the page states that the accepted taxon's data "can be found on World Flora Online, id: wfo-0000210558". The note cites wfo-0000201181 as the species' own accepted id. The rest holds: publisher page (opened) prints 27(1): 47-66, 1979, title as filed; ExportCitation (opened) and CrossrefCites (opened) both give the sole author Withers JR; the quote is whole and verbatim at 88 characters with a direction; the abstract gives "Artificial shading experiments", 30% of full daylight for "9 months (autumn-spring)" raising A. pycnantha yield, and intense shading below 8% causing etiolation and lower yields in all species. Set shade levels in artificial experiments make a set-shade trial, not a field gradient |
| 3 | Trachyandra divaricata | OK (fault noted) | POWO urn:lsid:ipni.org:names:542385-1 (opened) is Trachyandra divaricata (Jacq.) Kunth, "This species is accepted", with no infraspecific taxa, so the id is the species itself. The publisher page (opened) prints 41(3): 321-326, 1993 and the title as filed; ExportCitation (opened) and zhenzhi 988988815 (opened) both give the sole author Bell DT. The quote is whole and verbatim at 78 characters ("dune inhabiting" unhyphenated as printed). The abstract describes "darkness and a range of monochromatic light conditions" and says nothing further about T. divaricata, so no later result qualifies the quote; the contrast with red-light-promoted species is carried. Germination light-quality trial under sense_light_nonvisual; m and partial hold |

Errors: 2 of 3 (66.7%). Error lines: 1, 2.

Pooled with audits 160 to 162: 3 of 11 evidence records (27.3%; audit 160 0 of 2, audit 161 0 of 4, audit 162 1 of 2, audit 163 2 of 3).

Verdict: fail on lines 1 and 2. Line 3 can be merged. Line 1 can be refiled with "42(5): 575-585" and the note's claim about the issue removed; line 2 can be refiled citing wfo-0000210558 once that page is opened.

On the line 1 ruling: audit 147 noted an omitted issue without counting it, while audit 152 counted missing volume and issue as an error. This audit's instruction is to copy the issue as printed and leave it out only where the page prints none; the publisher page prints 42(5), and the record states the opposite, so it is counted.

Unconfirmed names: Acacia pycnantha under its own id. wfo-0000210558 could not be opened (provenance refusal); the snapshot page reached through wfo-0000201181 places Acacia pycnantha as the accepted name, so the name is accepted and only the cited id is wrong. POWO and GBIF pages for Pimelea ciliata and Acacia pycnantha were not tried.

Faults noted, not counted:
- Line 1: author order rests on the CSIRO ExportCitation page; acnpsearch prints "At. Slater et al.", which agrees on the first author only. acnpsearch spells the title "PHOTON FLUX-DENSITY"; the record follows the publisher's unhyphenated title.
- Line 1: the conditions leave out the abstract's remark that a vernalisation response may be increasing the rate of flowering. It bears on temperature, not on the 12 h result, so it does not change the reading of the quote. The abstract does not say whether the plants were wild-collected.
- Line 2: the abstract says "Artificial shading experiments" without naming shade cloth or screens; the fixed daylight percentages are enough for a set-shade trial.
- Line 3: the abstract calls the eight species "native and naturalized" without assigning a status; T. divaricata is a named species with no cultivar, and the record does not mention its status.

Blocked: list.worldfloraonline.org/wfo-0000210558 (PROVENANCE_REQUIRED, not retried). worldfloradb.net and typeset.io results were left alone. No library proxy, ResearchGate, academia.edu or Sci-Hub page opened.

Stray files: none committed; the two desk-d73 copies stay untracked.
