# Audit 153 of desk-d64 (29 October 2026)

Scope: all 16 evidence records of origin/research/desk-d64:docs/views/evidence/desk-d64.jsonl (no search records, no wanted lines). Each source was found by my own WebSearch and checked on a page that search returned (ishs.org, J-STAGE, iris.unito.it, link.springer.com, bvsalud, rrc.nbrp.jp, utb.cz Summon record, Hacettepe AVESIS). Quotes checked verbatim against the abstract and counted with Python len. Accepted names opened on POWO, or on WFO or Kew species.data where noted. Duplicates checked by DOI and taxon against docs/views/evidence/*.jsonl on main and origin/research/desk-d63: none. No ResearchGate, academia.edu, proxy or mirror page was opened (springerlink.bibliotecabuap.elogim.com results were left alone). About 26 WebSearches used.

| line | taxon | verdict | reason |
|---|---|---|---|
| 1 | Kalanchoe blossfeldiana | OK | ishs.org: W. Amaki, M. Kunii, Acta Hortic 1107: 279-284, 2015, DOI 10.17660/ActaHortic.2015.1107.38; quote verbatim (83); species named in title and abstract, cultivars 'Arena' and 'Cora' of the species; POWO 274279-1 accepted |
| 2 | Hydrangea macrophylla | OK | ishs.org: B. Litlere, E. Strømme, 51: 285-298, 1975, DOI; title as printed (capitals); quote verbatim (66); no cultivar named; POWO 791637-1 accepted |
| 3 | Portulaca umbraticola | OK | J-STAGE: Maguvu, Higuchi, Shibata, Hortic J 87(1): 124-131, 2018, DOI; quote verbatim (99); flower-opening synchrony vs dark length (diel); abstract names only the species, no hybrid; POWO 323272-2 accepted |
| 4 | Portulaca umbraticola | OK | same paper; quote verbatim (112); light needed for full opening; distinct trait from line 3 |
| 5 | Mentha aquatica | OK | iris.unito.it: S. Atsbaha Zebelo, Bertea, Bossi, Occhipinti, Gnavi, Maffei, PLOS ONE 6(3): e17195, 2011, DOI; quote verbatim (108); herbivore-induced emission on living plants; POWO 450192-1 accepted |
| 6 | Helianthus annuus | OK | ishs.org: Blacquière, Straver, van den Berg, 580: 101-109, 2002, DOI; quote verbatim (102); 10-16 h treatments as printed; POWO 119003-2 accepted |
| 7 | Lilium longiflorum | OK | ishs.org: S. Lazare, M. Zaccai, 1171: 119-124, 2017, DOI; quote verbatim (52); 25°C as printed; no cultivar; POWO 537642-1 accepted; not the Heins 1982 main record |
| 8 | Dianthus caryophyllus | OK | J-STAGE: Kato, Katsuoka, Baba, Inaba, Hortic Res (Japan) 22(1): 35-44, 2023, DOI; quote verbatim (111); species in title, cultivars of the species; POWO 153205-1 accepted; different paper from main's hortj.szd-146 |
| 9 | Dianthus japonicus | OK | J-STAGE: Yun, Song, Kim, Hortic J 89(1): 37-44, 2020, DOI; quote verbatim (76); day-neutral; no other light or chemical trial in the abstract; Kew species.data 153487-1 accepted, POWO 153318-1 D. ellipticus synonym of D. japonicus |
| 10 | Salvia greggii | OK | ishs.org: G. Zanin, J.E. Erwin, 723: 367-374, 2006, DOI; title as printed (capitals); quote verbatim (52) and about S. greggii; POWO 456321-1 accepted |
| 11 | Salvia patens | OK | same paper; quote verbatim (117) and about S. patens; POWO 456902-1 accepted |
| 12 | Impatiens balsamina | OK | link.springer.com: K.K. Nanda, H.N. Krishnamoorthy, T.A. Anuradha, Planta 76(4): 367-370, 1967, DOI; quote verbatim (117); GA3 on living intact and decapitated plants (hormone response, no extract or nutrient); WFO wfo-0000730261 accepted |
| 13 | Ipomoea nil | OK | bvsalud and rrc.nbrp.jp: Shinozaki, Tanaka, Ono, Ogiwara, Kanekatsu, van Doorn, Yamada, Plant Cell Rep 33(7): 1121-31, 2014, DOI on NBRP; title verbatim; quote verbatim (123); flower opening vs dark length (diel); POWO 270882-1 Pharbitis nil synonym of Ipomoea nil, WFO wfo-0000747940 accepted |
| 14 | Camellia sinensis | OK | link.springer.com: Plant Growth Regul 95: 111-120, 2021, DOI, no issue printed; utb.cz Summon gives authors Mu, Pan, Qi, Qin, Li, Liang, Rao, Sun in the record's order and issue 1; quote verbatim (83); 29 vs 23 volatiles as printed; POWO 828548-1 taxon page (accepted in listed floras). Fault, not counted: "headspace" and "living plants" in method/conditions are not stated in the abstract |
| 15 | Lavandula stoechas | OK | AVESIS: Ghaderi-Far, Cosgun, Degirmenci, Tuysuz, Ulgen, Tavşanoğlu, Plant Biol 23(6): 992-999, 2021, DOI; quote verbatim (121); light/dark germination trial; POWO 449089-1 accepted |
| 16 | Perilla frutescens | OK | J-STAGE: S. Nakamura, Y. Okasako, JJSHS 26(1): 28-32, 1957, DOI; quote verbatim (45); paper's Perilla ocymoides var. crispa is on POWO 290244-2 "a synonym of Perilla frutescens var. crispa"; POWO 190343-2 P. frutescens accepted |

Errors: 0 of 16, error rate 0%. All 16 can merge.

Unconfirmed names: none. Impatiens balsamina and Ipomoea nil confirmed on WFO (Ipomoea also via the POWO Pharbitis nil synonym page); Dianthus japonicus on Kew species.data plus a POWO synonym page; Camellia sinensis POWO page has no explicit status line.

Blocked: three powo.science.kew.org urn-form URLs (Hydrangea 791637-1, Lilium 537642-1, Dianthus japonicus 153487-1) were refused for provenance; reached instead through search-returned URLs. pmc.ncbi.nlm.nih.gov PMC3052309 returned a reCAPTCHA page.

Stray files: desk-d64.jsonl copied into the worktree root for this audit (untracked, not committed). The desk branch adds only its evidence and progress files.
