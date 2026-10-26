# Audit 75: recheck-2 (branch research/recheck-2, commit 5f758184)

Gate: `screen_candidates.py --check` on the 9 search records and 2 wanted lines prints "0 problems".

## Sample (seed 75)

The unit holds 9 search records, fewer than 20, so the sample is the whole unit. `random.seed(75)` over lines 1 to 9 gives the order 8, 7, 4, 1, 5, 9, 3, 2, 6. Because the unit is its own sample, the "check 15 more after an error" rule is already met.

## Method

`harvest_get.py` was run for the six genera (Anthreptes, Eudyptula, Lama, Tympanuchus, Lepidochelys, Quelea). In all 9 records the entries not starting with "web: " equal, in order, the harvest's query lines and its family-review line (a first script compare flagged all nine only because the review line is not printed as a "query" line; read by eye they match), and no output shows "gave up". Every DOI named in `chased` and every `screened` id appears in the harvest output. The `canon` lists were compared with docs/views/research/canon.jsonl by trait and class: nothing for the trait and class is missing (Hauzman et al. 2018 covers snakes only, so its absence from the Lepidochelys fovea record is right). The queue shows `closest: none` for Anthreptes, Lepidochelys and Quelea, which supports "none applies" in `chased`. I ran 25 WebSearches (the two prescribed trait searches per genus and trait group, a third of my own for most) and 8 fetches of URLs my searches returned. No ResearchGate, academia.edu, Sci-Hub, LibGen or library proxy page was opened (an academia.edu result for Rutherford appeared and was not opened).

## Verdicts

| Line | Record | Verdict |
|---|---|---|
| 1 | Anthreptes lambda_max_nm | ok. Queries match; four screened works (galago natural history, hummingbird colour gamut, red-flower reflectance, feather transmission) hold no sunbird pigment. My searches returned the patent family, the eLife spectral-tuning paper (canon, named) and Hart-type MSP papers on other birds; no Anthreptes value. |
| 2 | Anthreptes spectral_range_nm | ok. Same as line 1. |
| 3 | Eudyptula lambda_max_nm | ok. Queries, three citation steps and screened works match. The Polar Biology paper (Hadden et al. 2023, s00300-023-03188-8) reports ocular media transmission only and cites the Humboldt penguin value, as the record says. No little penguin pigment peak found. |
| 4 | Lama depth_cue | ok. Queries and citation step match; `screened` is empty and the note says why. Two searches (stereopsis, visual cliff and motion parallax) returned human psychology pages and Nityananda and Read 2017 (canon); no camelid measurement. |
| 5 | Tympanuchus eye_movement | ok. The oculomotor-nucleus comparison is correctly screened. My search returned Moore et al. 2017 on retinal configuration and head/eye movement (PMC5228126; the page was blocked by a verification page and a redirect, so its species list is unread) and chicken head-bobbing pages; no prairie grouse measurement seen. Open lead: whether PMC5228126 includes a grouse. |
| 6 | Lepidochelys acuity_cpd | ok. Searches returned Copeia 2001 (juvenile loggerhead, Caretta), the FIT green turtle thesis (Chelonia), the sea snake paper (Hart et al. 2012) and a triplefin paper; no Lepidochelys retina. |
| 7 | Lepidochelys fovea | ok. Same as line 6. |
| 8 | Quelea acuity_cpd | ok. DTIC report ADA112802 (Wolbarsht and Ringo 1981) is cat and monkey; Long and Fisher 1983 is a ground squirrel. No Quelea measurement. |
| 9 | Quelea interreceptor_deg | ok. Same as line 8. |

Errors: 0 of 9, 0.0%. Pooled with audits 43 to 51 and 55 to 73 (8 errors in 664 records): 8 in 673, 1.2%. Under 5%, so recheck-2 passes. Lines to drop: none.

## The "already on main" claim

The launch prompt asked me to find rows for Tetrastes (four cells), Loxostege lambda_max_nm, Grylloprociphilus acuity_cpd and interommatidial_deg, and Tremex receptor_classes. The recheck-2 files make no claim about these cells: their genera (Anthreptes, Eudyptula, Lama, Tympanuchus, Lepidochelys, Quelea) are the unit's only genera, and the one claim the notes make about main (no row for Anthreptes, Lepidochelys, Quelea; sunbird SWS1 rows of Chalcomitra, Cinnyris and Aethopyga at oa-2:3128-3130; Eudyptula sws1_type at oa-2:2881; Lama pupil and diel rows at oa-2:2615-2618 and a tapetum row at recheck-8-fixed:4; Tympanuchus rows for other traits at canon-5:175 and oa-1:3748-3750) holds.

For the five named cells, no evidence row exists: docs/views/evidence and docs/views/audit/corrected hold no row whose taxon is Tetrastes, Loxostege, Grylloprociphilus, or any Tremex receptor_classes (the only "Tremex" hit in evidence is not a taxon). They are on main as search records, not evidence rows: Tetrastes acuity_cpd, interreceptor_deg, lambda_max_nm and spectral_range_nm at harvest-52:60-63, Loxostege lambda_max_nm at harvest-52:64, Grylloprociphilus acuity_cpd and interommatidial_deg at harvest-51:58-59, Tremex receptor_classes at harvest-51:60. If "on main" means an evidence row, the claim has no row for any of the five and is false for all of them; if it means a search record, it holds for all five. Since recheck-2 does not make the claim, I count no error against the unit.

## Wanted lines (faults listed, not counted)

1. Te Ara, "Reptiles and frogs (1966), page 2": the page title fetched is "Lizards"; year 1966 and the address check out; no author is shown; the fetched text (metadata only) does not mention pupil shape, so the line's relevance rests on its stated guess.
2. "NZ Skinks Wellington Region" (matiusomesisland.nz PDF): the page titles itself "Skinks of the Wellington region" and gives no year or authors (Romijn is credited for photographs, 2007 comes from the file name). The text I received lists iris colour and does not mention pupil shape, so the line is unlikely to serve Oligosoma pupil_shape.

## Leads

- PMC5228126 (head and eye movement and retinal configuration in foveate birds): species list unseen; may include a grouse for Tympanuchus eye_movement.
