# Audit 131: desk-d41 (22 plant genera; branch origin/research/desk-d41, head d0e36819)

## Lines judged

No sample was drawn. The launch prompt asks for the whole unit, so error lines can simply be dropped.
- Search records: all 22 lines of docs/views/searched/desk-d41.jsonl (1 to 22).
- Evidence records: all 3 lines of docs/views/evidence/desk-d41.jsonl (1 to 3).
- Wanted lines: all 6, checked where a page opened, listed and not counted.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on a copy of the searched file (22 lines), with the wanted file (6 lines), prints "0 problems".

## Method

Judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e)), audit 39's counting rule, audit 90's format, and the launch prompt's rulings: unlabelled direct OpenAlex query lines are waived; a web-found `chased` family review is accepted only for genera in no harvest run; for harvested genera `chased` must be the harvest's own family review or citation step (an omitted zero-hit citation-step DOI is cosmetic).

- Queries. `harvest_get.py` ran offline (origin/ci) for all 22 genera and Sitobolium. A script compared each record's unprefixed `queries` with every `query` and `family review` line the harvest prints. All 20 harvested records match word for word and in order, with the "web: " lines after. Briza and Daphne print "in no harvest run yet" and list "web: " lines only. No harvest shows "gave up" for a unit genus.
- Screened. Every screened DOI or OpenAlex id is in the harvest data (`harvest_get.load()` genus and family records).
- Chased. 10.1007/s44372-025-00446-3 is printed by none of the unit's harvest outputs. It is named by 18 records. Briza (12) and Daphne (16) are no-run genera, so it is accepted there. Parnassia (1): its harvest family review "Parnassiaceae photoreceptor review" ran with 0 hits (fork, below). The other 15 (lines 2 to 11, 13, 15, 18, 19, 20) are harvested genera whose harvest family review ran with hits (7 to 581): Euphorbiaceae 98, Rosaceae 333, Poaceae 464, Myricaceae 7, Lamiaceae 284, Arecaceae 35, Orchidaceae 242, Ericaceae 107, Asteraceae 581, Cupressaceae 31, Plantaginaceae 63, Boraginaceae 76, Orobanchaceae 64. Their notes say "Family review searched by web", which misstates the harvest. Under the ruling each is an error. Paris (14), Microstegium (17), Cynoglossum (21) and Valeriana (22) name citation-step DOIs the harvest prints; Paris and Valeriana omit a zero-hit citation-step DOI (10.1016/j.cub.2026.03.002; 10.1002/ece3.71923), which is cosmetic.
- Main (origin/main a1f01864). No unit search record names a trait with evidence on main: Epigaea chemical (desk-d19:1), Sequoia, Paris, Comarum and Microstegium light, Phalaris light and chemical, Valeriana light and chemical are all left out, as they should be. No evidence record repeats main (no Parnassia, Comptonia or Eutrochium evidence on main). Several search records repeat earlier null search records on main (line 15 Comarum sense_chemical and rescreen-2:25; line 18 Pulmonaria sense_chemical and harvest-19:5; sweep-era records for most genera); noted, not counted.
- Taxonomy. POWO (opened): Eutrochium purpureum (L.) E.E.Lamont is accepted, and the record uses it, noting the source's Eupatorium purpureum. Parnassia grandiflora Raf. is "a synonym of Parnassia grandifolia", so P. grandifolia is the accepted name. Sitobolium Desv. is on POWO a synonym of Dennstaedtia (VASCAN accepts it after Triana-Moreno et al. 2023); the unit filed nothing under Sitobolium, which its progress note confirms. Comptonia peregrina: POWO page failed at its site; it is the genus's only species, not counted. No hybrid or synonym epithet appears in the unit. Betonica officinalis is the record's own POWO check, not re-checked.

Searches: about 55 WebSearches (3 evidence, 5 taxonomy, 4 wanted, the rest one or two per null record, using the germination light/dark, GA3/smoke/nitrate, jasmonate and anthesis phrasings of 10(e)). Fetches only of URLs my searches returned. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened (an ezproxyberklee.flo.org Cambridge result and a researchgate.net Pedicularis PDF result were left alone). No paper text is committed.

## Search record verdicts (22)

| Line | Record | Verdict |
|---|---|---|
| 1 | Parnassia diel, eye_type, sense_chemical | ok (chased fork). Ren and Bu 2014, PLoS ONE 10.1371/journal.pone.0086581 (PMC opened) on P. palustris gives stamen movement about 5 h after full opening, with no clock hour of opening. Holloway 2011 Note 43 (uaf.edu opened) lists P. palustris as GA-responsive with no stated trial or source, as the record says. |
| 2 | Mercurialis eye_type, sense_chemical | **error: missed measurement (and chased).** Villamil, Sommervogel and Pannell 2022, "Disentangling the effects of jasmonate and tissue loss on the sex allocation of an annual plant", Front Plant Sci 13, 10.3389/fpls.2022.812558 (Frontiers opened): methyl jasmonate sprayed on living M. annua restored male investment in damaged plants. The harvest prints it ([92] of the Mercurialis output) and the record did not name it. Applied elicitor on a living plant, 10(d). |
| 3 | Oemleria (4 traits) | **error: chased.** Harvest Rosaceae review ran (333 hits). My searches returned the Woody Plant Seed Manual, the UW protocol and a sex-ratio paper; no missed measurement. |
| 4 | Anthoxanthum (4 traits) | **error: chased.** Poaceae review ran (464). My germination and anthesis searches returned a lettuce smoke paper (van Staden et al. 1995, Springer opened, no Anthoxanthum) and a ragweed paper (PSU page opened); no missed measurement. |
| 5 | Comptonia diel, eye_type | **error: chased.** Myricaceae review ran (7). My catkin search returned flora pages; no hour. |
| 6 | Betonica (4 traits) | **error: chased.** Lamiaceae review ran (284). Lead, unresolved: my search returned "Effect of light, gibberellic acid and nitrogen source on germination of eight taxa from dissapearing European temperate forest, Potentillo albae-Quercetum" (PMC5654834, bot check twice). Betonica officinalis is a character species of that forest type, but I could not see the taxa list, so it is not counted. A Stachys annua GA3 paper (sze.hu page opened) is Stachys, not Betonica. |
| 7 | Cocos diel, eye_type | **error: chased.** Arecaceae review ran (35). Singh et al. 2020 (ispgr.in opened) gives flowering phases in days only; no hour found. |
| 8 | Calypso (4 traits) | **error: chased.** Orchidaceae review ran (242). My germination/fragrance search returned other orchids only. |
| 9 | Epigaea diel, eye_type, light | **error: chased.** Ericaceae review ran (107). My light search returned the Seed Manual and general pages; no missed measurement. |
| 10 | Eutrochium diel, eye_type, chemical | **error: chased.** Asteraceae review ran (581). My hormone/herbivore search returned Solidago and Ageratina (E. adenophorum) papers only. |
| 11 | Sequoia diel, eye_type, chemical | **error: chased.** Cupressaceae review ran (31). Kępczyński 2018 (Springer opened) and a Nicotiana smoke record (frames.gov opened) name no Sequoia; pollen searches gave no hour. |
| 12 | Briza (4 traits) | ok. No-run genus; web chased accepted. My germination search returned seed-seller and flora pages. |
| 13 | Chelone sense_light_nonvisual | **error: chased.** Plantaginaceae review ran (63). My germination search returned nursery and extension pages. |
| 14 | Paris diel, eye_type, sense_chemical | **error: missed measurement.** Zheng et al. 2023, "Multiomics strategies for decoding seed dormancy breakdown in Paris polyphylla", BMC Plant Biol 23: 247, 10.1186/s12870-023-04262-3 (BMC page opened): seeds of P. polyphylla var. yunnanensis treated with GA4 reached 52% germination after 3 months against 30% untreated, and GA3 gave 15%. A gibberellin trial on another species of the genus. Not in the harvest output. A second result, Frontiers 10.3389/fpls.2024.1389357, redirected and stays unread. |
| 15 | Comarum diel, sense_chemical | **error: chased.** Rosaceae review ran (333). My search returned no Comarum trial. |
| 16 | Daphne (4 traits) | **error: missed measurement.** No-run genus, so chased is accepted, but my search "Daphne mezereum OR Daphne laureola seed germination dormancy gibberellic acid OR light" returned Fang et al. 2016, "Germination and dormancy-breaking of Daphne giraldii Nitsche (Thymelaeaceae) seeds from northwestern China", Rev Chapingo Ser Cienc For Ambient 22(1): 99-113 (revistas.chapingo.mx opened): GA3 at 100 mg/L for 16 h gave 17.3% where untreated fresh seed did not germinate. The same search returned Folia Geobot 10.1007/s12224-021-09389-5 (Springer opened) with a 250 mg/L GA3 trial on D. arbuscula and D. cneorum. Both are GA3 trials the sense_chemical null missed. |
| 17 | Microstegium diel, eye_type, chemical | ok. Citation-step chased printed. My search returned an allelopathy (extract) paper, which does not count, and general smoke papers. |
| 18 | Pulmonaria sense_chemical | **error: chased.** Boraginaceae review ran (76). My search returned no Pulmonaria trial. |
| 19 | Phalaris diel | **error: chased.** Poaceae review ran (464). My anthesis search returned flora pages and PMC6220418 (bot check, unread). |
| 20 | Melampyrum sense_chemical | **error: chased.** Orobanchaceae review ran (64). My search returned no Melampyrum trial. |
| 21 | Cynoglossum sense_light_nonvisual | **error: missed measurement.** van Breemen 1984, "Comparative germination ecology of three short-lived monocarpic Boraginaceae", Acta Bot Neerl 33(3): 283-305 (natuurtijdschriften.nl opened): light was tested on C. officinale seeds, and the abstract reports that the light response differed between populations. A germination light trial on a named species. Not in the harvest output. The PDF permission went unanswered and was not retried. |
| 22 | Valeriana diel | ok. Citation-step chased printed (zero-hit second DOI omitted, cosmetic). My search returned carnation and general scent-rhythm papers. |

Search record errors: **18 of 22 (81.8%)**: lines 2 to 11, 13 to 16 and 18 to 21. Of these, 15 are chased errors under the ruling (line 2 is also a missed measurement), and 3 are missed measurements alone (14, 16, 21).

## Evidence record verdicts (3)

| Line | Record | Verdict |
|---|---|---|
| 1 | Parnassia grandifolia sense_light_nonvisual | ok. WUSTL profile opened: Albrecht and Long, Seed Sci Res 24(3): 239-245 (2014), 10.1017/S0960258514000166. The quote is verbatim and one sentence of 116 characters, reporting the study's result. Germination light/dark response, grade m, partial. |
| 2 | Comptonia peregrina sense_chemical | ok. Harvard Forest PDF opened: del Tredici and Torrey, Bot Gaz 137(3): 262-268 (1976). The quote is verbatim from the abstract. The value (500 ppm GA3 up to 24 h, 20%; embryos best at 1-10 ppm) matches, units as printed. |
| 3 | Eutrochium purpureum sense_light_nonvisual | ok. FHSU repository page opened: Aline Rodrigues de Queiroz 2018, darkness and about 10, 50 and 100% of natural light. The quote is verbatim. The record uses the accepted name and notes the source's Eupatorium purpureum. |

Evidence errors: **0 of 3**.

## Counts

- Search records: 18 of 22, 81.8%.
- Evidence: 0 of 3.
- Unit: 18 of 25, 72.0%.

Pooled with audits 83 to 90, from audit 90's figures (48 in 1026 search records; 52 in 1090 overall):
- Search records: 66 in 1048, 6.3%.
- With evidence: 70 in 1115, 6.3%.
Audits after 90 are not added, as in audits 129 and 130.

Forks:
- Line 1 (Parnassia chased). The harvest family review ran with 0 hits, so the harvest has no review to name. I do not count it. Under a strict reading it is an error too, making 19 of 22.
- Chased lines 3 to 11, 13, 15, 18 to 20. If the desk accepted a web-found family review for harvested genera, these 14 stand and the search errors fall to 4 of 22 (18.2%: lines 2, 14, 16, 21). The verdict is a fail either way.
- Line 21. The abstract does not give the C. officinale light/dark percentages; if the desk wants a stated direction, the work still belonged on the wanted list under 10(e).

**Verdict: fail.** Drop the error lines; the rest of the unit stands.

**Error lines to drop:**
- docs/views/searched/desk-d41.jsonl: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 18, 19, 20, 21.
- docs/views/evidence/desk-d41.jsonl: none.

## Wanted lines (listed, not counted)

1. Vandelook, Van de Vyver, Carta 2019, 10.1007/s12224-019-09346-3: Springer page opened; authors, year and DOI match (Folia Geobot 54: 73-84). The abstract states no photoinhibition in M. perennis.
2. Mercurialis annua 1994, 10.1006/anbo.1994.1102: my search did not return its page; not checked.
3. Magdalita, Damasco, Adkins 2010 (UPLB repository): not checked.
4. Runyon and Birdsall 2016: treesearch page opened; authors, year, Arthropod-Plant Interact 10: 383-391 match; no DOI shown, as the line says. The FS PDF (rmrs_2016_runyon_j001) also came back.
5. Richardson and Irwin 2015: journal page and DOAJ (Nov 2015) returned by my search; title and year match.
6. del Tredici and Torrey 1976, 10.1086/336868: PDF opened; the total-dark sentence is in the paper, as the line says.

## Leads

- Mercurialis annua sense_chemical: Villamil et al. 2022 (10.3389/fpls.2022.812558).
- Paris polyphylla sense_chemical: Zheng et al. 2023 (10.1186/s12870-023-04262-3); also Frontiers 10.3389/fpls.2024.1389357, unread.
- Daphne giraldii sense_chemical: Fang et al. 2016 (Rev Chapingo 22(1): 99-113); D. arbuscula and D. cneorum GA3 trial (10.1007/s12224-021-09389-5).
- Cynoglossum officinale sense_light_nonvisual: van Breemen 1984 (Acta Bot Neerl 33(3): 283-305).
- Betonica: PMC5654834 (light, GA3 and nitrogen on eight Potentillo albae-Quercetum taxa), taxa unseen.

## Blocked pages

- pmc.ncbi.nlm.nih.gov PMC5654834 and PMC6220418: bot check.
- natuurtijdschriften.nl ABN1984033003004.pdf: permission unanswered, not retried.
- POWO 281115-2 (Comptonia peregrina), core.ac.uk 65488562: failed at site.
- horizon.documentation.ird.fr: redirect to a maintenance page.
