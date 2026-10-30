# Audit 150 of desk-d60 (29 October 2026)

Scope: all 19 evidence records of origin/research/desk-d60:docs/views/evidence/desk-d60.jsonl (no search records in the unit). Each source was found by my own WebSearch and checked on a page that search returned (publisher, DOAJ, repository or index page); each quote was checked verbatim and its length counted; accepted names were opened on POWO (GBIF for Ochroma, WFO for Marchantia). Duplicates were checked by DOI, quote and taxon against docs/views/evidence/*.jsonl on main: none. No ResearchGate, academia.edu, proxy or mirror page was opened; no paper text is committed beyond quotes already in the record. About 30 WebSearches used.

| line | taxon | verdict | reason |
|---|---|---|---|
| 1 | Ceratopteris richardii | OK | DOAJ: authors, Front Plant Sci 14, DOI; quote verbatim (101 chars); POWO accepted |
| 2 | Colocasia esculenta | ERROR | Author order wrong: DOAJ and the Redalyc PDF print Gondim ARO, Puiatti M, Finger FL, Cecon PR; the record lists Puiatti first and Gondim third. Quote verbatim (112), DOI, 48(2): 83-89 and POWO accepted confirmed |
| 3 | Pinus strobus | OK | Springer: authors, New Forests 32: 33-49, DOI; quote verbatim (77); 47 and 13% full sunlight as printed; POWO accepted |
| 4 | Eulophia bicallosa | OK | DOAJ: authors, Plants 14(14): 2212, DOI; quote verbatim (111); dark, white, green, red, blue treatments; POWO accepted |
| 5 | Zostera marina | OK | Springer: citation, quote verbatim (114), 4.0-17.2% and 8.2/23.2 C as printed; POWO accepted |
| 6 | Marchantia polymorpha | OK | zhenzhi: authors, DOI, quote verbatim (105), red most effective; fh-zwickau: PCP 40(10): 1014-1020, 1999; WFO 2022 snapshot accepted (newer WFO snapshot blocked) |
| 7 | Dipterocarpus retusus | OK | Indian Forester page: Beniwal 1990, 116(9): 694-698, DOI; quote verbatim incl. "overbead" (86); 25 treatments, aim height growth. POWO 320711-1: D. macrocarpus "is a synonym of Dipterocarpus retusus" (direction confirmed); D. retusus accepted |
| 8 | Cucumis anguria | OK | Springer: authors, Biol Plant 20: 281-286; quote verbatim (106); white/B/FR inhibit, dark and R promote; POWO accepted. Issue (4) not printed on the page (not counted) |
| 9 | Araucaria angustifolia | OK | CSIRO page: authors, 59(1): 32-37, DOI; quote verbatim (83); 139 days, shade cloth; low-light reserve use longer is printed; POWO accepted |
| 10 | Juniperus procera | OK | SLU page: authors, New Forests 33(2): 155-169, DOI; quote verbatim (60); POWO accepted |
| 11 | Juniperus procera | OK | Same page; quote verbatim (101). Aqueous smoke on living seeds, a living-response trial. Other trials in the paper: light (filed as line 10), cold stratification (thermal) and NIR sorting; no GA3/KNO3/karrikin/photoperiod trial missed |
| 12 | Oryza sativa | OK | Banglajol: authors, 13(1-2): 56-62, DOI; quote verbatim (99); dark control, 6 h light/18 h dark, 24/18 C; POWO accepted. Note: abstract says "red and green" LEDs in methods, record says red and blue (abstract inconsistent; not counted) |
| 13 | Picea abies | OK | Silva Fennica page: authors, 29(2), DOI 10.14214/sf.a9200; quote verbatim (89). POWO page fetch blocked for me |
| 14 | Ochroma pyramidale | OK | Smithsonian PDF and zhenzhi: authors, J Trop Ecol 15: 827-839, 1999, DOI; quote verbatim (98); both species named in abstract; six gaps 25-800 m2 (Methods); R:FR film. Accepted: GBIF 3152240 "Species Accepted"; POWO page shows only an "Accepted by" section |
| 15 | Luehea seemannii | OK | As line 14; POWO "This species is accepted". Grade g pooled pair, both members named and accepted |
| 16 | Pinus banksiana | OK | Springer: title printed "depinus", authors, Biol Plant 14: 260-268, 1972; quote verbatim (120); 660 and 730 nm as printed. POWO page fetch blocked for me |
| 17 | Calopogon tuberosus | OK | Springer: authors, PCTOC 85: 91-102; quote verbatim (121); five dark/16-h regimes; POWO accepted |
| 18 | Ophrys sphegodes | OK | DOAJ: quote verbatim (123); agris: six authors in record order, 67, 196-201, DOI; POWO accepted. Agris prints issue 3, record 3-4 (not counted) |
| 19 | Cypripedium cordigerum | OK | EJES page: Kaur 2023, 13(2): 90-95, DOI; quote verbatim (113); 24-h dark vs 12-h light; POWO 625683-1 accepted |

Errors: 1 of 19 (line 2), error rate 5.3%.

Unconfirmed names (my POWO fetch was blocked; desk reports POWO accepted): Pinus banksiana (line 16), Picea abies (line 13). Marchantia polymorpha confirmed only on an older WFO snapshot.

Stray files: desk-d60.jsonl copied into the worktree root for the audit (untracked, not committed). The desk branch itself carries only its evidence and progress files as read.
