# desk-d53 progress (lead reading, plant leads)

Started 29 October 2026. Branch research/desk-d53.

Lead pool: plant lines in docs/views/wanted/*.jsonl with a DOI, a species-level trait cell still open on main, minus /tmp/desk/d47_leads.json, DOIs in the desk-d47 to desk-d52 notes and DOIs already in any evidence file (877 leads). Focus: ferns, bryophytes, aquatic plants, volatile signalling, night light, UV. When pool leads ran dry, a few papers were found by topic search (SciELO fern, moss and macrophyte abstracts) and checked against main before filing.

## Filed (8 records, docs/views/evidence/desk-d53.jsonl, all partial)
- Solanum tuberosum sense_chemical (Vazquez-Gonzalez et al. 2023, Planta, 10.1007/s00425-023-04075-6; measured null on VOC composition under herbivore load; POWO treats the varieties as synonyms of the species)
- Oenothera biennis and Lotus pedunculatus sense_light_nonvisual (Anic Thomas 2021, Exeter doctoral thesis on night lighting, abstract on ORE, no DOI; POWO accepts both)
- Dicksonia sellowiana sense_light_nonvisual (Filippini, Duz and Randi 1999, Rev Bras Bot 22(1); daily light hours spore trial; WFO accepts)
- Pleopeltis pleopeltifolia sense_light_nonvisual and sense_chemical (Felippe et al. 1992, Acta Bot Bras 6(1); the paper's Polypodium pleopeltifolium is a WFO synonym; red light, IAA, GA3, CEPA, ABA on spores)
- Elodea naias sense_light_nonvisual (Tavechio and Thomaz 2003, Braz Arch Biol Technol, 10.1590/S1516-89132003000200011; the paper's Egeria najas is a POWO and WFO synonym)
- Spirodela polyrhiza sense_light_nonvisual (Appenroth 2003, J Plant Physiol 160(11); photoperiod and turion formation; POWO accepts)

## Held, not filed
- Bryum argenteum (Silva, Porto, Simabukuro 2010, Braz Arch Biol Technol 53(4): 763-769; "The spores germinated when exposed to light, independent of both medium used.") and Dolichomitriopsis diversiformis (Liu et al. 2016, 10.1590/1678-4324-2016160061; "In contrast, in darkness at 20 C from one to 30 days, spores did not germinate."): quotes verified, but neither POWO nor WFO species page could be reached to confirm the accepted name (WFO returned only the genus Bryum and a variety; the Dolichomitriopsis epithet appears as diversiforme on other sites).
- Cheilanthes concolor (Colli and Perez 1999, 10.1590/S1516-89131999000200006; "Germination of the spores in the dark was not observed."): the paper's name is now Doryopteris concolor; POWO page refused (permission unanswered), WFO not found.
- Cyathea delgadii and Blechnum brasiliense (Hiendlmeyer and Randi 2007, 10.1590/S0102-33062007000400015; "Higher percentages of germination were observed at 5 and 22% light for both species."): Cyathea delgadii is accepted on the Colombian POWO mirror, but Blechnum brasiliense is probably a synonym of Neoblechnum brasiliense and a pooled record needs every member accepted.
- Carex brevior and C. stipata dark germination (Kettenring et al. 2006, 10.1093/aob/mcl170): already on main.

## Leads read, nothing filed
- Volatile emissions of six New Zealand ferns (NZ J Ecol 44): no species named for the herbivory result and the damage sentence runs past 125 characters.
- Phartyal et al. 2022 ethylene (Plant Biol): every sentence naming Sagittaria sagittifolia or the other five species exceeds 125 characters.
- Artificial night light grassland (Ecol Evol 12; Bennie et al. 2018): species sentences exceed 125 characters or are cut, and the Bennie abstract names no species. The thesis supplied the three short sentences above; its Lapsana, Leontodon, Ranunculus acris, Agrostis and Holcus sentences are 133 to 194 characters.
- Fern spore review (Front Biol 2015), Amphicarpaea (Am J Bot 2015: dormancy classes only), Ipomoea purpurea optics (Plants 2025: no epidermal focusing in the abstract), Polystichum Pb and light (Agronomy 2024: sentences over 125), Salvia sclarea zinc (the short sentence concerns zinc), mulberry LED (Plants 2022: result sentences over 125), Solanaceae light/dark cycles (eggplant not named), Thunbergia alata (preprint: fragments only), Panicum miliaceum photoperiod (gene counts), Magnolia sinica (record is a Manglietia paper), Euphorbia of Ile-Ife (AJOL page empty), Pontederia sagittata (no opening time), Pistia stratiotes (temperature and photoperiod varied together), Eichhornia crassipes and Salvinia auriculata photoperiod (pooled nutrient uptake), Gleichenella pectinata (lowercase sentence fragment), Phragmites australis light and depth (Chinese abstract only), Typha and Phragmites (Ecol Eng 2016: no light result), Duckweed vertical farm (Plants 2022: species sentence over 125), Seed dormancy of 15 peatland species (no species-specific light or GA sentence), Chasmanthium (listing was a different paper).
- Blocked: PMC, link.springer.com and BMC (permission unanswered), Europe PMC API, doi.org, oasisbr, mdpi 12/10/1928 (permission unanswered), wfoplantlist search pages, POWO pages for Cheilanthes/Doryopteris and Cyathea delgadii (the colplanta mirror served the last).

No wanted lines written. WebSearch used: about 75.

## Desk disposition after audit 143
Audit 143 checked all 8 evidence records and found 1 error (line 7, Elodea naias: dose unit mis-copied, the paper prints a different unit). The line is dropped and the other 7 are merged.
