# desk-d14 (plant genera: Parkinsonia, Panicum, Artemisia, Polystichum, Ailanthus, Equisetum, Cardamine, Rumex, Centaurea)

Searches run: 42 WebSearch calls. WebFetch worked for most hosts (mdpi.com, frontiersin.org, ebi.ac.uk and doi-less URLs not returned by a search were refused: permission unanswered, not retried).

## Skipped, with reason (checked on main at 7d27b44d)
- Parkinsonia: diel searched (desk-d1); sense_chemical held by main's wanted line (Saberi et al. 2021, GA3/KNO3 on P. aculeata seed).
- Panicum: diel held by main's wanted lead (Davidson 1935 anthesis); light and chemical already have evidence.
- Ailanthus: diel searched (desk-d1); sense_chemical held by wanted leads (Soler and Izquierdo 2024 review with GA3 table, Soler and Izquierdo 2026, Redwood et al. 2019). Soler 2024 sits on mdpi.com, which WebFetch refused here. Two web searches (GA3 germination; MeJA/herbivore) found nothing new.
- Polystichum, Equisetum: ferns; light/diel searched (harvest-6, harvest-c12, sweep-3); chemical evidence on main; open leads (Greer and McCarthy 1997; Pietrak et al. 2024 on mdpi.com; Guillon and Fievet 2003 concerns other Equisetum species).
- Artemisia, Cardamine: many species, chemical and light evidence already on main, many leads on wanted; not started (budget).
- eye_type: skipped for every genus (plants carry "none"; owner reading 10(b)).

## Evidence logged (6, docs/views/evidence/desk-d14.jsonl, all abstract-only, partial)
- Rumex obtusifolius sense_chemical x2: Moore et al. 2003 (Funct Ecol 17(4) and 17(1)), applied jasmonic acid and beetle feeding, systemic response. Closes that cell.
- Rumex crispus sense_chemical: Hemmat, Zeng and Khan 1985 (Weed Sci 33(5), 10.1017/S0043174500083041), GA4+7 on scarified seed. Closes that cell.
- Centaurea jacea diel: Štenc et al. 2023 (Am J Bot 110(6) e16179, 10.1002/ajb2.16179), pollen presentation peaks early afternoon. Diel is a genus-carry trait.
- Centaurea stoebe sense_chemical: Huang, Gfeller and Erb 2018 bioRxiv 441790 (preprint), root VOCs of a living plant act on a neighbour.
- Centaurea x moncktonii (hybrid of C. nigra and C. jacea, accepted by POWO) sense_light_nonvisual: DiTommaso et al. 2021 (Weed Sci 69(1), 10.1017/wsc.2020.86). Does not close the nigra or jacea cells.

## Search records: none written
Rumex sense_chemical (acetosella left) cannot take a null record: `screen_candidates.py --check` refuses a genus-trait with evidence already on main. Centaurea sense_chemical and sense_light_nonvisual are held by main's wanted leads (Lopez del Egido et al. 2018 genus lead; Greulach 1942 for C. cyanus; Nosratti 2017 for C. iberica).

## Leads found and not logged
- Kennett et al. (Montana RSIS item 635), spotted knapweed (C. maculosa = C. stoebe) under full, 2/3 and 1/2 light: abstract gives the design only; no DOI on the page.
- Celik 2006 (Pak J Bot 38(5): 1431-1437; C. spicata, fenzlii, kurdica), Uysal, Celik and Ozkan 2006 (Pak J Bot 38(4): 983-989; C. tomentella), a Tehran C. balsamita GA3/KNO3 paper (journal not shown), Biol Divers Conserv 8(3) (eight Phalolepis endemics, photoperiod): Centaurea germination papers on species outside the queue; page summaries only, no verbatim sentences.
- Štenc et al. 2025 (Perspect Plant Ecol Evol Syst 67, 10.1016/j.ppees.2025.125868): C. jacea gradual pollen presentation.
- Rumex: Schatral and Osborne 2006 (R. vesicarius), Voesenek et al. 1992 (R. acetosa, crispus, palustris light) not queue cells.

## Desk disposition after audit 104

Audit 104 judged the whole unit: 1 error in 6 evidence records (line 6, Centaurea x moncktonii, which POWO lists as a synonym of C. x gerstlaueri). That line is dropped and the other 5 records are merged. The bioRxiv preprint on line 5 (Centaurea stoebe) was later published in Plant Cell & Environment 42(6): 1964-1973; the record keeps the preprint citation and the published version is noted here only. The Centaurea x moncktonii light result can be re-filed under C. x gerstlaueri if a later unit wants it.
