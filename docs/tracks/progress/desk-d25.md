# desk-d25 (plant genera Chelidonium to Echium; 15 given, 8 worked, 7 not reached)

About 37 WebSearches and 30 WebFetches used. Many publisher and PMC pages returned a permission request (PROVENANCE_REQUIRED) and were not retried; URLs not returned by a search were refused outright.

## Evidence (docs/views/evidence/desk-d25.jsonl, 4 lines)
- Chelidonium asiaticum sense_chemical, Ji et al. 2022 (10.7732/kjpr.2022.35.6.796): GA3 and GA4+7 at 500 mg/L after dormancy break; abstract only. The paper calls it C. majus subsp. asiaticum; POWO accepts C. asiaticum as a species, so the C. majus cell stays open.
- Silene latifolia diel, Dotterl, Wolfe and Jurgens 2005 (10.1016/j.phytochem.2004.12.002): scent emitted only at night; abstract only. Main had a search note for it but no evidence line.
- Maianthemum dilatatum sense_light_nonvisual, Shin et al. 2022 (10.3390/horticulturae8111057) and Kawano et al. 2020 (10.1111/1442-1984.12258, closes the harvest-c13 lead); abstracts only. POWO accepts the species.

## Search records (docs/views/searched/desk-d25.jsonl, 6 lines)
Chelidonium sense_light_nonvisual; Erodium sense_light_nonvisual, sense_chemical, diel; Tanacetum diel; Leucanthemum diel. All `chased` entries except Chelidonium are "none: ..." because the web search for a family review found none.

## Wanted lines (docs/views/wanted/desk-d25.jsonl, 5 lines)
Hadi et al. (C. majus and Tanacetum cinerariifolium GA3 and stratification; no DOI), Xiong et al. 2018 (Convolvulus arvensis, GA3 and KNO3 no effect), Ozkil and Uremis 2019 (Convolvulus GA3), Stahler 1948 (Convolvulus shade), Shin et al. 2022 (Maianthemum dilatatum GA3).

## Skipped or held
- Bellis: harvest shows "error gave up" on its first queries (skipped, point 6).
- Eye_type: already filed on main for Chelidonium, Tanacetum, Erodium, Leucanthemum, so no new line.
- Chelidonium diel (harvest-c13 lead), Tanacetum, Convolvulus, Impatiens, Silene, Maianthemum, Leucanthemum sense_chemical and sense_light_nonvisual cells: held by leads on main or by my wanted lines, so no null.
- Not reached: Impatiens (diel null incomplete), Linaria, Onoclea, Podophyllum, Rosa, Dactylis, Echium (diel searches for Dactylis and Echium found only the Eberle et al. 2014 nectar-hours statement, a nectar window and not flower opening, already noted on main).
- Leads tried and not logged: Xiong 2018 (abstract GA3/KNO3 sentence is over 125 characters).
