# rescreen-2 (26 October 2026)

Branch research/rescreen-2, cut from origin/main a5213610. Files: docs/views/searched/rescreen-2.jsonl (28 search records) and docs/views/wanted/rescreen-2.jsonl (6 lines). No evidence records: none of the held branches carries an evidence file, so `addlog.py` was not run. Gate: `screen_candidates.py --check` prints 0 problems. WebSearch calls: 32 of the 60 allowed; no WebFetch, no proxy, ResearchGate or academia.edu page opened (an academia.edu result for the Aquarius and Iris searches was left closed).

## Part 1: records held for the owner's readings (desk-screen.md point 10)

Held records were found by comparing each branch file with main by genus and trait (search records) and by DOI or title (wanted lines).

### plant-1 (4 held search records, 50 held wanted lines)

- Kept and fixed, 4: Tussilago, Stellaria, Dipsacus and Digitalis sense_chemical. All four stood on reading A in audit 54. Under point 10(a) the tissue-chemistry and cut-flower works that audit 54 named from the harvest output now sit in `screened` with that reason (Tussilago extract paper 10.5530/fra.2018.1.7; Dipsacus asper root oil 10.4314/tjpr.v16i1.24; the two Digitalis ethylene-blocker trials on excised flowers), and so do the candidates today's tool lists (its chemical words now include "scent"). No other field changed; the note says what was added.
- Wanted lines kept, 5: lines 31 (Medicago volatiles as weevil signals), 32 (herbivore-induced changes in alfalfa and Spodoptera reproduction; no DOI or authors), 37, 38 and 39 (Campanula floral scent and bee responses). Reading 10(a) counts volatiles a living plant gives off as a signal, and each work treats a species of the genus.
- Wanted lines dropped, 3: line 33 (SPME profile of alfalfa trichomes, stems and leaves taken from the plant: tissue chemistry), line 144 (Hypericum extract tested on moth larvae: extract chemistry), line 150 (Mediterranean odorscapes thesis: Hypericum among its species is unconfirmed).
- Left held, 42: the light and daily-rhythm lines that audit 54 held for hedged reasons, weak or doubled claims, or missing registry authors. The readings do not touch them, so this unit did not re-judge them.

### replant-1 (13 held search records, 13 held wanted lines)

- Kept and fixed, 13: the twelve eye_type records (Cynoglossum, Lunaria, Pastinaca, Raphanus, Scutellaria, Thlaspi, Valeriana, Asparagus, Botrypus, Heliotropium, Phalaris, Chelone) and Chelone sense_chemical. Under point 10(b) every candidate today's tool lists (pavement-cell surveys, lentil "Lens" papers, zinc in Thlaspi epidermis, sorghum silica cells) went into `screened`; none is a focusing work on its genus. The Antirrhineae petal-cell item in the Chelone record carries the owner's wording ("focusing belongs under sense_light_nonvisual"). Each record also regained the two supplement-run-20 harvest queries ("<Genus> epidermal lens cells", "<Genus> epidermal focusing leaf optics"), which the harvest added after the records were written (point 7). Chelone sense_chemical now names Bowers, Boockvar and Collinge 1993 (10.1007/BF00985011, the DOI printed by my search and by audit 53) in `screened`: leaf iridoid chemistry with a damage comparison, and no chemical or airborne cue.
- Wanted lines dropped, 5: lines 2, 7, 9, 10 and 11 (essential oils of Cynoglossum and Pastinaca, Pastinaca hirsuta headspace of harvested tissue) under point 10(a).
- Left held, 8: lines 22, 23, 62, 69, 78, 84 (no authors) and 81 (placeholder title) for reasons outside the readings; line 33 (metals and glucosinolates as defences in Thlaspi caerulescens, no authors) also stays held, since whether a defence response to soil metals counts as a chemical cue is a fork the readings do not settle.

### harvest-46 (3 held search records)

- Kept and fixed, 1: Colostygia spectral_range_nm. Under point 10(c) the Briolat et al. 2026 activity test is a behaviour finding. Canon-22 (Nowinszky et al. 2022) was added to `canon`; audit 63 read its Table 1 and found no Colostygia. The note names Infusino et al. 2017 (10.14411/eje.2017.004, on the audit-63 list): a catch table listing C. pectinataria would overturn the record under point 9.
- Dropped, 1: Conistra spectral_range_nm. Main now holds Conistra rows from the light-trap table (oa-13a:469 to 472).
- Left held, 1: Dysgonia spectral_range_nm waits for Infusino et al. 2017 under point 9, which the readings do not change.

## Part 2: leftover cells

| Cell | Result |
|---|---|
| Iris (Mediterranean mantis) acuity_cpd, interommatidial_deg | 1 record (web searches only; Iris is in no harvest run) |
| Iris cff_hz, corner_hz | 1 record |
| Iris lambda_max_nm, spectral_range_nm | 1 record. Qian, Theobald and Frank 2026, the mantis spectral paper the search returned, is already logged on main for its three species (Popa, Theopropus, Hymenopus), none an Iris. |
| Scoparia acuity_cpd, interommatidial_deg | 1 record |
| Scoparia cff_hz, corner_hz | 1 record |
| Scoparia lambda_max_nm | 1 record |
| Scoparia spectral_range_nm | no record. My lamp search found no catch table, but Table 1 of canon-22 (Hungarian light-trap catches) is unread here and may list a Scoparia species; under point 9 the desk should read it before this cell gets a record. |
| Parnassius cff_hz, corner_hz | 1 record. "Parnasiinae vision review" is now listed in `queries` (audit 76's fault), and "web: Papilionidae vision review" is the family step. |
| Parnassius acuity_cpd, interommatidial_deg | no record: Awata et al. 2010 and Matsushita et al. 2012 on P. glacialis are on main's wanted lists (harvest-51, desk-76), so point 3 keeps the trait out. My two searches found nothing new. |
| Aquarius cff_hz, corner_hz | 1 record, with "web: Gerridae vision review" in `queries` (audit 76's fault) |
| Sphenomorphus acuity_cpd and fovea (audit 62) | already on main as harvest-50 search records (dated 19 Oct), so no new record |

For the wrong-kingdom family reviews (Plantaginaceae for Scoparia, Alismataceae for Aquarius), the review ran without error, so it stays in `queries` under point 7 and the note explains it; the right family went in as a web search.

### Plant sense_chemical cells reopened by point 10(a)

Audit 53 found that four replant-1 genera (Cynoglossum, Lunaria, Pastinaca, Comarum) had only tissue-chemistry wanted lines for sense_chemical. I ran the protocol for them (8 searches):
- Lunaria and Comarum: 1 record each.
- Cynoglossum: no record. The harvest candidate 10.1111/eea.13334 (host finding by a weed biocontrol candidate, returned by a Cynoglossum query) went on the wanted list, since it may test responses to odours of living Cynoglossum plants.
- Pastinaca: no record and no wanted line. Both searches returned a pestinfo page for Journal of Chemical Ecology 28: 2191-2201 (2002) whose title was not shown, and I could not judge it. The desk should look it up before this cell gets a record.

## Counts

- Held search records judged: 20 (plant-1 4, replant-1 13, harvest-46 3). Kept with fixes 18, dropped 1 (Conistra), left held 1 (Dysgonia).
- Held wanted lines judged on the readings: 14 (plant-1 8, replant-1 6). Kept 5, dropped 8, left held 1 (replant-1 line 33); the other 49 (plant-1 42, replant-1 7) are held for reasons outside the readings.
- New search records from leftover cells: 8, plus 2 for the reopened plant cells. New wanted line: 1.
