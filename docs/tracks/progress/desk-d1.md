# desk-d1 (plant screening; stopped at the WebSearch limit)

Branch research/desk-d1. Genera screened in order: Marchantia, Vachellia, Poa, Parkinsonia, Panicum, Artemisia, Polystichum, Ailanthus (8 of 15).

Unfinished, no searches run (the shared 200-search limit per turn ran out at Hemerocallis): Hemerocallis, Chromolaena, Cyanthillium, Hexastylis, Hypoxis, Cichorium, Larrea. Nothing was written for them. Mahonia/Berberis synonymy was not needed for this unit's genera. Note for the rerun: Asteraceae genera can use the family review 10.1007/s44372-025-00446-3, returned by the web "Asteraceae photoreceptor review" and "Aristolochiaceae photoreceptor review" searches of this unit.

## Cells closed by a measurement (evidence/desk-d1.jsonl, all partial abstract reads)
- Marchantia polymorpha sense_chemical (JA-pathway defence against snail feeding, 10.1002/pei3.70052)
- Vachellia farnesiana sense_light_nonvisual (no light effect, 10.1017/wsc.2021.54)
- Poa annua sense_chemical (nitrogen nutrition, group statement), Poa pratensis sense_chemical (GA4, smoke, karrikin; no DOI listed)
- Parkinsonia aculeata sense_light_nonvisual (10.2307/3897928)
- Panicum virgatum sense_chemical x2 (10.3389/fpls.2019.01144 herbivory and MeJA volatiles; Sarath 2006 NO donor and ABA, no DOI on page) and sense_light_nonvisual (Aiken and Springer 1995)
- Ailanthus altissima sense_light_nonvisual x2 (10.13133/2239-3129/18231, 10.1111/1442-1984.12286)

## Search records (searched/desk-d1.jsonl, 13)
Marchantia diel, eye_type; Vachellia karroo sense_light_nonvisual (species level), Vachellia sense_chemical, eye_type; Poa eye_type; Parkinsonia diel, eye_type; Panicum eye_type; Artemisia diel, eye_type; Ailanthus diel, eye_type.

## Wanted lines (wanted/desk-d1.jsonl)
Stone et al. 2003 acacia pollination (Vachellia diel); Grana 1980 Poa annua anthesis; Saberi et al. 2021 Parkinsonia GA3/KNO3 germination; proso millet crossing paper and Johannesburg 1935 anthesis note (Panicum diel); Int J Plant Sci Polystichum acrostichoides antheridiogen paper (10.1086/297488); Torrey 2019 dormancy paper (Ailanthus).

## Notes
- Harvest URLs and doi.org links were not fetchable (permission unanswered); only URLs returned by my own searches were opened.
- Poa bulbosa and Panicum sense_chemical, Poa/Panicum/Artemisia sense_light: genus already has evidence on main, so --check forbids a search record; no record written.
- Vachellia karroo and V. farnesiana: light closed for farnesiana only.

## Desk disposition after audit 91 (28 October 2026)

Audit 91 judged the whole unit (13 search records, 10 evidence records). Search error: line 3 (Vachellia sense_chemical, which missed Mahmood 2022 on Acacia farnesiana, where GA3 raised germination from 48.37% to 78.67%). Evidence: 0 of 10 counted as errors, but line 8 (Panicum virgatum, sense_light_nonvisual) carries a url that points to a different paper than its DOI, so the desk dropped it rather than file a wrong source; the measurement stays a lead. Merged: 12 search records, 9 evidence records, 7 wanted lines (5 filled with registry authors from Crossref run desk-wanted-66, 2 already carried authors). The missed Vachellia result is a lead and its cell stays open. Not screened: Hemerocallis, Chromolaena, Cyanthillium, Hexastylis, Hypoxis, Cichorium, Larrea.
