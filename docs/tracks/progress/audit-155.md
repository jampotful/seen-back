# audit-155: desk-d65 (6 evidence records, no search records, no wanted lines)

Audited 29 October 2026 against origin/research/desk-d65 (merge-base diff: progress note and 6 evidence lines; no stray files). Sources checked on publisher, repository or indexer pages reached through WebSearch results; 14 WebSearches used. Duplicates: no DOI and no taxon of this unit on main (Aristida setifolia in desk-d52 is another paper and species; Tiarella polyphylla in desk-d47 is another genus). origin/research/desk-d66 does not exist on the remote, so no overlap could be checked there.

| line | taxon | verdict | reason |
|---|---|---|---|
| 1 | Aristida recurvata | OK (fault noted) | Ramos, Valls, Borghetti, Ooi 2019, title verbatim, DOI 10.1002/ajb2.1345 (UNESP page); 106(9): 1190-1201 confirmed on the Embrapa BDPA record (publisher page not reached; UOW repository shows a 1-12 preprint pagination); quote verbatim, 106 chars; sentence pools exactly the two Aristida species the abstract names among eight grasses; smoke water on living seeds. Accepted: WFO wfo-0000849099 accepted; POWO 389724-1 blocked, Kew-hosted colplanta 389724-1 "This species is accepted" |
| 2 | Aristida riparia | OK (fault noted) | as line 1; POWO 19334-2 "This species is accepted"; WFO wfo-0000849316 accepted |
| 3 | Senegalia polyphylla | OK (POWO unconfirmed) | Araujo Neto, Aguiar, Ferreira 2003, 26(2): 249-256, DOI as printed (UNESP page); quote verbatim on SciELO, 123 chars; light trials at 25 C confirmed ("conducted at that temperature", the optimum 25 C); WFO wfo-0000166132 is the accepted Senegalia polyphylla with Acacia polyphylla among its synonyms; POWO pages blocked or failed |
| 4 | Aethionema arabicum | OK | J Exp Bot 70(12): 3313-3328, twelve authors in printed order, DOI (OUP page); quote verbatim, 112 chars; POWO 1022841-2 "This species is accepted" (as (L.) Andrz. ex Rchb.); WFO wfo-0000407422 accepted; GBIF 3051150 accepted |
| 5 | Quercus mongolica | OK | Forests 15(3): 538, eleven authors in order (MDPI PDF page 1; Jinmao Wang 10th), DOI; quote verbatim, 62 chars; species-level, set shade S1 40%, S2 20%, S3 3% light against full light; POWO 50874074-1 "This species is accepted" |
| 6 | Croton urucurana | OK (fault noted) | Revista Arvore 27(1): 53-57, four authors in order, DOI (DOAJ; Redalyc PDF header); quote verbatim, 81 chars; set shade 30, 50, 70% against full sun; POWO 71032-2 "This species is accepted" |

Errors: 0 of 6 (0%).

Unconfirmed names: Senegalia polyphylla on POWO (WFO accepts, Acacia polyphylla its synonym); Aristida recurvata on POWO directly (WFO and Kew colplanta accept).

Faults noted, not counted:
- Lines 1 and 2: the abstract says smoke raised germination only in darkness (no effect in light); value and method omit the dark condition. The same paper's light/dark trial was not filed under sense_light_nonvisual.
- Line 6: the English abstract's preceding sentence says 70% shading gave higher leaf and root dry weight, contradicting the quoted sentence; the Redalyc full text (Portuguese resumo and results) supports the quoted sentence (roots heavier in full sun).
- Line 1/2 citation: volume, issue and pages taken from FAPESP; Embrapa agrees, publisher page not reached.

Blocked: POWO 389724-1 and 518289-1 (permission not answered), POWO 543-2 (client error), peeref (login). No library proxy, ResearchGate, academia.edu or Sci-Hub page opened.

Stray files: none (desk-d65.jsonl copy in the worktree root is untracked and not committed).
