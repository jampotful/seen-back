# harvest-c23 (desk screening, plant genera)

Batch: docs/tracks/batches/harvest-c23.json (28 plant genera). Rules: docs/tracks/prompts/desk-screen.md points 1 to 10 and the plant paragraph of round4-harvest.md; audits 77 and 78 read first.

OpenAlex refused this machine (proxy 403), so no OpenAlex step was run here. For genera in no harvest run the records hold the desk-screen web searches only and say so; for genera in a harvest run (Antennaria, Lagurus and Genista to Armoracia, Mentha) the records list the harvest's queries word for word, then the web searches, and name every screen candidate in `screened`. Every sense_chemical search carries hormone and elicitor words ("volatile emission jasmonate ethylene response"), after audit 78 found elicitor responses missed. A cell with a wanted lead (here or on main) or with evidence on main gets no record.

## Done

- Dittrichia: diel, eye_type; sense_chemical wanted (hairy-root elicitation); sense_light_nonvisual left to main's external-2 wanted line.
- Sidalcea: diel, eye_type, sense_chemical; sense_light_nonvisual wanted (MSU long-day perennials sheet).
- Cochemiea: diel, eye_type, sense_chemical.
- Antennaria: diel, eye_type, sense_chemical (harvest run 3, candidates screened); sense_light_nonvisual wanted (Minnesota photoperiod and irradiance study of herbaceous ornamentals).
- Lagurus (plant cells only; harvest run 3): eye_type, sense_chemical; sense_light_nonvisual wanted (grass epidermis and light environment); diel left without a record because the harvest lists the bioRxiv 2026 preprint on night-time carbohydrate turnover in 41 pooid grasses (10.64898/2026.06.02.729567), already on main (replant-1 wanted, oa-13b:477 Pooideae row); whether Lagurus ovatus is among its species is unchecked.

Commit 4958ab46 went up with 32 check problems (Antennaria and Lagurus records written before I saw that both are in harvest run 3); the next commit replaces those records and the check prints 0 problems.
- Genista (harvest run 16): diel, eye_type, sense_light_nonvisual; sense_chemical wanted (Acta Physiologiae Plantarum 10.1007/s11738-011-0799-4 on G. tinctoria in vitro, title unseen).
- Pulicaria (harvest run 10): diel, eye_type, sense_chemical; sense_light_nonvisual wanted (Ben-Gurion University photoperiod and red/far-red work, title cut short).
- Nonea (harvest run 16): diel, eye_type, sense_chemical, sense_light_nonvisual.
- Hylodesmum (harvest run 10): diel, eye_type, sense_chemical, sense_light_nonvisual.
- Pelecyphora (harvest run 16): diel, eye_type, sense_chemical; sense_light_nonvisual has evidence on main.
- Cota (harvest run 10): diel, eye_type; sense_chemical wanted (Plant Biotechnology Reports 10.1007/s11816-014-0331-6, title unseen); sense_light_nonvisual wanted (PanAmerican Seed grower guide).
- Calendula (harvest run 3): eye_type; diel, sense_chemical and sense_light_nonvisual wait on five harvest works put on the wanted list (phenology study, inflorescence-scent study, service-plant volatile thesis from the citation step, 1978 photoperiod study, end-of-day red/far-red study), so no web searches were spent on those three cells.
- Cephalanthera (harvest run 16): diel, eye_type, sense_chemical; sense_light_nonvisual has evidence on main.
- Armoracia (harvest run 3): diel, eye_type; sense_chemical and sense_light_nonvisual not done (ration spent). The harvest lists a horseradish hairy-root phytochrome A study (10.5511/plantbiotechnology.20.13) that the next unit should weigh for sense_light_nonvisual, with the hairy-root fork.

## Stopped

WebSearch ration: 99 of 100 used (two per open trait, plus five follow-ups named in the records and wanted lines). Stopped between genera with everything committed.

Genera left for a later unit: Armoracia (sense_chemical, sense_light_nonvisual), Bellardia, Eriophorum, Desmanthus, Sapindus, Helleborus, Dermatophyllum, Himantoglossum, Sesuvium, Themeda, Mentha, Oncosiphon, Stylophorum, Cyclamen, Delphinium. Of these only Armoracia and Mentha are in a harvest run; Mentha's sense_light_nonvisual cell has evidence on main (sweep-100:1).

Totals: 38 search records, 13 wanted lines (authors empty throughout), check 0 problems. No page was opened (WebFetch not used), no proxy or ResearchGate result was followed, and no evidence was written.
