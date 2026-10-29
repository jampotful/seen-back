# Audit 151 of desk-d61 (29 October 2026)

Scope: all 18 evidence records of origin/research/desk-d61:docs/views/evidence/desk-d61.jsonl (no search records in the unit). Each source was found by my own WebSearch and checked on a page that search returned (publisher, journal host, SciELO, Silva Fennica, AGRIS, PMC); quotes were checked verbatim and their length counted (Python len); accepted names were opened on POWO where it answered, otherwise WFO or GBIF. Duplicates were checked by DOI, quote and taxon against docs/views/evidence/*.jsonl on main and against origin/research/desk-d62. No ResearchGate, academia.edu, proxy or mirror page was opened (several springerlink.bibliotecabuap.elogim.com results were left alone); no paper text is committed beyond the records' own quotes. About 44 WebSearches used.

| line | taxon | verdict | reason |
|---|---|---|---|
| 1 | Bletilla ochracea | OK | J-STAGE: Godo, Fujiwara, Guan, Miyoshi in that order, 2011, 28(4): 397-400, DOI; quote verbatim (66 chars); set LED colours and dark; POWO 617800-1 accepted |
| 2 | Paphiopedilum tigrinum | OK | MDPI: Yao, Huang, Zhang, 7(9): 298, DOI; quote verbatim in section 4.4 (92); 43.67% printed in 3.1 (as 43.67 ± 3.16%); dark/light germination trial |
| 3 | Pinus koraiensis | ERROR | Journal page (journal.hep.com.cn, Journal of Forestry Research) prints 2022, 33(4): 1135-1144; the record gives 32(4). Volume 32 is printed on no page opened (ouci prints 2021 and no volume). Authors, DOI and quote (109; printed with italic "G P"/"G V") otherwise agree; POWO 263037-1 accepted |
| 4 | Funaria hygrometrica | OK | Springer: Bauer L, Mohr H, Planta 54(1): 68-73, 1959, DOI; quote verbatim (45); Funaria hygrometrica named; WFO 2023-06 accepted; different paper from main's Funaria record |
| 5 | Bonatea polypodantha | OK | Pherobase and PMC: Balducci, van der Niet, Johnson, Ann Bot 126(7): 1155-1164, DOI; PMC prints the sentence with a final period (103), the record copies Pherobase's version without it (not counted). Floral phenophases (anthesis, scent) timed to dusk: diel in the owner's sense. WFO 2024-12 accepted; POWO fetch failed for me |
| 6 | Picea mariana | OK | Frontiers: Colombo SJ, Man R, 6: 1261112, 2023, DOI; quote verbatim (75); photoperiods 8 to 24 h set in glasshouse cubicles; POWO 195883-2 accepted |
| 7 | Pinus sylvestris | OK | Springer: Kasemir H, Mohr H, Planta 152: 369-373, 1981, DOI; quote verbatim (87, "15s" unspaced as printed); POWO 263353-1 accepted |
| 8 | Pinus sylvestris | OK | Springer: Elmlinger MW, Mohr H, Planta 183: 374-380, 1991, DOI; "(iii) Red light ... after sowing." starts with a capital and ends with a period, a whole sentence inside a numbered results list (100) |
| 9 | Pinus sylvestris | OK | AGRIS: Razzak, Ranade, Strand, Garcia-Gil in that order (diacritics dropped), PCE 40(8): 1332-1340, 2017, DOI; quote verbatim (124); set intensity and R:FR |
| 10 | Cyathea delgadii | ERROR | Duplicate of main: docs/views/evidence/desk-d54.jsonl already files Cyathea delgadii, sense_light_nonvisual, same DOI (10.1590/s0102-33062007000400015) and the same quote. Source itself checks (SciELO: Hiendlmeyer R, Randi AM, 21(4): 909-915; quote 84; the abstract names exactly the two measured ferns) |
| 11 | Blechnum brasiliense | OK | Same SciELO page; quote verbatim (102), pooled over the same two named species, grade g honest. Not on main (desk-d54 held it out). Name confirmed on POWO this time: 17058320-1 "This species is accepted"; Neoblechnum brasiliense 77158236-1 "This name is a synonym of Blechnum brasiliense". WFO (December 2023) wfo-0001113310 also accepts it. NZOR and PPG I (via Wikipedia's Neoblechnum page) sink it into Neoblechnum. Audit 144's fork is settled for POWO |
| 12 | Dicksonia sellowiana | OK | SciELO: Renner GDR, Randi AM, 18(2): 375-380, 2004, DOI; quote verbatim (98); 5, 20, 36 and 50% irradiance as printed; POWO 275823-2 accepted |
| 13 | Cyathea atrovirens | OK | Revista Ambiencia and core.ac.uk PDF: Marcon, Silveira, Bender, Droste in that order, 11(2): 409-422, 2015, DOI printed in the PDF; quote verbatim (37); 8, 12, 16, 24 h and dark. Fault, not counted: title drops "(Langsd. & Fisch.) Domin (Cyatheaceae)" from the printed English title. POWO fetch failed for me |
| 14 | Picea abies | OK | Springer: Mortensen LM, Sandvik M, New Forests 2(4): 281-287, 1988, DOI; quote verbatim (124); 18, 24 and 28 °C as printed; POWO 262609-1 accepted |
| 15 | Physcomitrium patens | OK | AGRIS: Uenaka H, Wada M, Planta 222(4): 623-631, 2005, DOI; quote verbatim (97). WFO wfo-0001151608 accepts Physcomitrium patens with Physcomitrella patens as its synonym; NZOR: Physcomitrella patens "Synonym of Physcomitrium patens (Hedw.) Mitt." Direction correct |
| 16 | Physcomitrium patens | OK | Same paper; quote verbatim (93); a different finding (R/FR branch position) from line 15 |
| 17 | Picea abies | OK | Silva Fennica: Höyhtyä R, Hänninen H, 25(3), 1991, DOI 10.14214/sf.a15610; quote verbatim (124); 300 μEm-2s-1 as printed |
| 18 | Pinus sylvestris | OK | Silva Fennica: Nygren M, 20(1), 1986, DOI 10.14214/sf.a15441; quote verbatim (107). Fault, not counted: the page prints "three photoperiods (0.8 and 24 hours)"; the record's method writes "0, 8 and 24 hours" |

Errors: 2 of 18 (lines 3 and 10), error rate 11.1%. Fail on those two lines; the other 16 can merge.

Repeats inside the unit: lines 7, 8, 9 and 18 are four different Pinus sylvestris papers (four DOIs, four findings); lines 14 and 17 are two different Picea abies papers; lines 15 and 16 are two findings of one paper. None of these repeats a paper on main. desk-d62 carries only a progress stub (no evidence file), so it has no overlap.

Unconfirmed names (my POWO fetch failed; other authority noted): Cyathea delgadii (GBIF 3598563 accepted; desk cites colplanta), Cyathea atrovirens (no authority page opened for me; desk reports POWO accepted), Bonatea polypodantha (WFO 2024-12 accepted), Paphiopedilum tigrinum (desk reports POWO accepted). Funaria hygrometrica and Physcomitrium patens are mosses confirmed on WFO only. Blechnum brasiliense is now confirmed on POWO.

Stray files: desk-d61.jsonl copied into the worktree root for this audit (untracked, not committed). The desk branch adds only its evidence and progress files (diff from merge base).

Procedure note: the Dicksonia SciELO page (line 12) was opened at the record's URL without a search returning it first.
