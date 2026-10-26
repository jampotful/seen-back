# harvest-c23 (desk screening, plant genera)

Batch: docs/tracks/batches/harvest-c23.json (28 plant genera). Rules: docs/tracks/prompts/desk-screen.md points 1 to 10 and the plant paragraph of round4-harvest.md; audits 77 and 78 read first.

OpenAlex refused this machine (proxy 403), so no OpenAlex step was run here. For genera in no harvest run the records hold the desk-screen web searches only and say so; for genera in a harvest run (Antennaria, Lagurus and Genista to Armoracia, Mentha) the records list the harvest's queries word for word, then the web searches, and name every screen candidate in `screened`. Every sense_chemical search carries hormone and elicitor words ("volatile emission jasmonate ethylene response"), after audit 78 found elicitor responses missed. A cell with a wanted lead (here or on main) or with evidence on main gets no record.

## Done

- Dittrichia: diel, eye_type; sense_chemical wanted (hairy-root elicitation); sense_light_nonvisual left to main's external-2 wanted line.
- Sidalcea: diel, eye_type, sense_chemical; sense_light_nonvisual wanted (MSU long-day perennials sheet).
- Cochemiea: diel, eye_type, sense_chemical.
- Antennaria: diel, eye_type, sense_chemical (harvest run 3, candidates screened); sense_light_nonvisual wanted (Minnesota photoperiod and irradiance study of herbaceous ornamentals).
- Lagurus (plant cells only; harvest run 3): eye_type, sense_chemical; diel wanted (bioRxiv 2026 night-time carbohydrate turnover in 41 pooid grasses; fork on whether a daily physiological rhythm counts as diel); sense_light_nonvisual wanted (grass epidermis and light environment).

Commit 4958ab46 went up with 32 check problems (Antennaria and Lagurus records written before I saw that both are in harvest run 3); the next commit replaces those records and the check prints 0 problems.
- Genista (harvest run 16): diel, eye_type, sense_light_nonvisual; sense_chemical wanted (Acta Physiologiae Plantarum 10.1007/s11738-011-0799-4 on G. tinctoria in vitro, title unseen).
