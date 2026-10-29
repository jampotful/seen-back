# Audit 152 of desk-d62 (29 October 2026)

Scope: all 13 evidence records of origin/research/desk-d62:docs/views/evidence/desk-d62.jsonl (no search records). Each source was found by my own WebSearch and checked on a page that search returned or the record's own URL (SciELO, biotaneotropica.org.br, NTU Scholars, DergiPark, CSIRO, PeerJ, DOAJ, butbn.cas.cz, ishs.org, impact.ornl.gov, J-STAGE, bvsalud, libmast DOAJ record, HUSCAP). Quotes were checked verbatim and counted (Python len). Accepted names opened on POWO where it answered, else WFO. Duplicates checked by DOI and taxon against docs/views/evidence/*.jsonl on main: none. origin/research/desk-d63 does not exist on the remote (ls-remote), so no overlap could be checked there. No ResearchGate, academia.edu, proxy or mirror page was opened (a webvpn.zafu.edu.cn Wiley result was left alone). About 21 WebSearches used.

| line | taxon | verdict | reason |
|---|---|---|---|
| 1 | Pleroma mutabile | OK | SciELO: Simão E, Takaki M, Biota Neotrop. 8(2): 63-68, 2008, DOI; quote verbatim (108); POWO 574841-1 accepted, Tibouchina mutabilis listed as its homotypic synonym (direction correct) |
| 2 | Streptocarpus rexii | OK | NTU Scholars: Nishii, Nagata, Wang, Möller, SAJB 81: 50-60, 2012, DOI; quote verbatim (97); WFO wfo-0001064746 accepted (POWO page not surfaced) |
| 3 | Cotoneaster horizontalis | OK | DergiPark PDF: Çelik H, Kalaycı Karasakal Ö, 42(1): 73-79, 2025, DOI; quote verbatim (120); GA3 on seeds; no light trial in the paper; POWO 722522-1 accepted |
| 4 | Anigozanthos flavidus | OK | CSIRO: Downes, Light, Pošta, Kohout, van Staden, 62(4): 347-358, 2014, DOI; quote verbatim (64); nitrate tested as a post-fire germination cue, not nutrient uptake; POWO 429575-1 accepted |
| 5 | Primula florindae | OK | DOAJ: Qin, Geng, Yang, Peng, PeerJ 11: e15234, 2023, DOI; quote verbatim (70); light/dark germination trial, light requirement reduced; POWO 701941-1 accepted |
| 6 | Cyperus difformis | ERROR | SciELO page prints Planta Daninha vol. 31, no. 4, Dec. 2013, pp. 823-832; the record gives no volume or issue and its note says they are not printed. Authors, DOI and quote (99) agree; POWO 304311-1 accepted |
| 7 | Utricularia vulgaris | OK | PDF: Prausová, Holzbauerová, Springrová, Jara, Šafářová, Cross, Adamec, Aquat Bot 182: 103545, 2022, DOI; quote verbatim (97); ethylene on seeds. Fault, not counted: the paper also has a light/dark trial (photophilous), which the note says the abstract lacks. POWO 527199-1 accepted |
| 8 | Vaccinium arctostaphylos | OK | ishs.org: Sedaghathoor S, Acta Hortic 771: 27-31, DOI; quote verbatim (61); no germination in darkness, positive photoblastic; WFO wfo-0000422273 accepted |
| 9 | Zingiber mioga | ERROR | ishs.org prints the title "The importance of photoperiod in cultivar and site selection for production of myoga (Zingiber mioga Roscoe): determination of critical daylength"; the record files a paraphrased title. Authors (Stirling KJ, Clark RJ), 620: 53-61, 2003, DOI and quote (124) agree; POWO 798364-1 accepted |
| 10 | Curcuma alismatifolia | OK | ORNL page: Hagiladi, Umiel, Yang, Acta Hortic 430: 755-761, 1997, DOI; quote verbatim (122); set LD/SD trial; POWO 796420-1 accepted |
| 11 | Eustoma russellianum | OK | J-STAGE: Bai J, Kawabata S, Hortic J 84(2): 148-155, 2015, DOI; quote verbatim (102); flower opening and closure timing; POWO 102343-2 E. grandiflorum is a synonym of E. russellianum, 367445-1 accepted |
| 12 | Gentianopsis paludosa | OK | libmast DOAJ record: Hou, Zhao, Pang, Duan, Ehmet, Shao, Sun in that order, DOI; bvsalud prints 12(1): e8490 and the quote verbatim (60); flower-closure rhythm |
| 13 | Gaultheria pyroloides | OK | HUSCAP: Tsuyuzaki S, Bot Lett 167(4): 424-429, 2020, DOI; quote verbatim (120); only G. miqueliana named; WFO wfo-0000695268 and POWO 330610-1 both treat G. miqueliana as a synonym of G. pyroloides |

Errors: 2 of 13 (lines 6 and 9), error rate 15.4%. Fail on those two lines; the other 11 can merge.

No null records, so no missed-trial check applied. No record repeats main.

Unconfirmed names: Gentianopsis paludosa (POWO fetch failed for me; WFO accepts the genus, floraoftheworld accepts var. paludosa; species page not opened). Streptocarpus rexii and Vaccinium arctostaphylos confirmed on WFO only.

Stray files: desk-d62.jsonl copied into the worktree root for this audit (untracked, not committed). The desk branch adds only its evidence and progress files.
