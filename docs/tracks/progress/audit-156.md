# audit-156: desk-d66 (13 evidence records, no search records, 5 wanted lines)

Audited 29 October 2026 against origin/research/desk-d66 (merge-base diff: progress note, 13 evidence lines, 5 wanted lines; no stray files; desk-d66.jsonl copy in the worktree root is untracked and not committed). Sources checked on publisher, repository or indexer pages reached through WebSearch results; about 40 WebSearches used. Duplicates: no DOI of this unit on main; the only taxon overlap is Hibiscus sabdariffa sense_chemical (seed priming, another paper and trait).

| line | taxon | verdict | reason |
|---|---|---|---|
| 1 | Capsicum annuum | OK | Plant Ecology 155: 245-257, 2001, three authors in order, title verbatim (doi.org/Springer page; no issue printed); quote verbatim (page prints "inall"), 65 chars; GA3 and fluctuating temperature overcoming darkness is the next abstract sentence, value not overstated. WFO wfo-0001019982 accepted |
| 2 | Coffea arabica | ERROR | The quote is the abstract's opening background statement of a review of coffee areas (no measurement in the source); not the study's own result, so grade m is unsupported. Citation otherwise as printed (PAB 20(7): 831-839, 1985; DOI as given); visible abstract spells "defferentiation" (meta field "differentiation") |
| 3 | Theobroma cacao | OK | Plant Science 168(5): 1247-1258, 2005, five authors in order, DOI (Penn State Pure); quote verbatim, 102 chars; lab page confirms MeJA foliar spray on living seedlings. POWO 320783-2 "This species is accepted" |
| 4 | Aloe vera | OK | Env Exp Bot 44(2): 133-139, 2000, four authors in order, DOI (ORNL record); quote verbatim, 100 chars; 10%/30%/full sun; "After 1 year of growth" supports the method. WFO wfo-0000758976 accepted |
| 5 | Hibiscus sabdariffa | OK (fault noted) | IPTEK 25(1): 18-22, two authors, DOI; quote verbatim, 110 chars; 8-12 h black-cover day lengths. POWO 326388-2 accepted (Sabdariffa rubra a synonym) |
| 6 | Cucumis melo | OK (fault noted) | Acta Hortic 871: 283-290, 2010, four authors in order, DOI; quote verbatim, 95 chars; four set photoperiods; groups Flexuosus and Dudaim of C. melo, no cultivar or hybrid. POWO 292238-1 accepted |
| 7 | Passiflora edulis | OK (fault noted) | Rev Bras Frutic 31(1): 1-12, 2009, six authors in order, DOI, title as printed; quote verbatim, 53 chars; flower opening timing. POWO 321964-2 accepted |
| 8 | Ocimum gratissimum | OK | Acta Hortic 569: 33-39, 2002, four authors, DOI; quote verbatim, 121 chars; seven light treatments and fluence-response curve in abstract; no GA3/KNO3. POWO 452969-1 accepted |
| 9 | Tectona grandis | OK | Indian Forester 126(1): 57-61, 2000, four authors, title verbatim ("robust"), DOI; quote verbatim, 116 chars; pooled pair is exactly T. grandis and G. robusta (Ailanthus responded oppositely); 0% vs 75% shade. POWO 864923-1 accepted; Grevillea robusta 50798-3 is the accepted target of the synonym G. venusta |
| 10 | Coffea arabica | OK | Photosynthetica 48(2): 199-207, 2010, five authors in order, DOI; quote verbatim, 116 chars; species only, no cultivar; distinct from line 2 and from main. IPNI 747038-1 is Coffea arabica L. itself; GBIF 2895345 accepted (POWO page not reached) |
| 11 | Moringa oleifera | OK | UofK J Agric Sci 19(2), 2011, four authors in order, DOI, no pages printed; quote verbatim, 121 chars; three set shade levels. POWO 584736-1 accepted |
| 12 | Curcuma longa | OK | Plant Prod Sci 12(1): 29-36, 2009, six authors in order, DOI; quote verbatim, 115 chars; white nets set RLI levels; yield peak at 73% RLI in abstract. POWO 796451-1 accepted |
| 13 | Jatropha curcas | OK | J Biotechnol Biodivers 2(4): 43-47, 2011, five authors in order, DOI; Portuguese quote verbatim, 96 chars; set shade 0/50/90%; no English abstract. POWO 131462-2 accepted |

Errors: 1 of 13 (7.7%). Error line: 2.

Unconfirmed names: none unaccepted. POWO ids not opened by this audit: Capsicum annuum 316944-2, Aloe vera 530017-1, Coffea arabica 747038-1 (POWO page blocked; IPNI shows 747038-1 is Coffea arabica L., the accepted name, not a synonym); acceptance confirmed on WFO/GBIF.

Faults noted, not counted:
- Lines 2 and 10: the note says the POWO 747038-1 page was "opened", while the progress note says it was blocked and not surfaced.
- Line 5: the quoted sentence excepts plant height and leaf colour; the value states RGR highest at 8 h without that exception; the note repeats "Abstract only, so flagged partial."
- Line 6: value says short days "favoured" branch number and female flowers; the abstract says they "influenced" them more than long days.
- Line 7: value says flowers "closed from 6 pm to about 1 am"; the abstract says closing started at 6 pm and finished around 1 am.

Wanted lines (existence, DOI, authors, year, title, journal):
- 1 Aloe arborescens: DOI resolves to the titled paper (Taylor & Francis page); authors and journal blank in the line (page prints no byline). Fault: journal (Plant Biosystems per the progress note) left empty.
- 2 Jatropha curcas: PeerJ 4: e1819, 2016, DOI and title match; authors blank (page shows Rincon-Rabanales et al.).
- 3 Stevia rebaudiana: DOI redirects to ccsenet article 11244, title matches; authors (Abdullateef RA, Osman M), year 2011 and journal (International Journal of Biology 3(4): 83-91, IIUM repository) left blank.
- 4 Eucalyptus: title, five authors in order, Aust J Bot 66(8): 657-666, DOI match the CSIRO page; the page prints "Published: 14 February 2019", line gives 2018 (volume year).
- 5 Opuntia: title, J Plant Res 126(5): 643-649, 2013 match (NYBG); full author list and DOI page not reached.

Blocked: doi.org for 10.1023/A:1013234100003 (first try), 10.1080/11263504.2013.782901, 10.7717/peerj.1819, 10.1071/BT18115, 10.1007/s10265-013-0558-2, ccsenet article 11244; POWO 747038-1 (not surfaced); worldfloradb.net (Anubis). No library proxy, ResearchGate, academia.edu or Sci-Hub page opened.

Stray files: none.
