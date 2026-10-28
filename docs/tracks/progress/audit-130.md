# Audit 130: desk-d40 (13 plant genera; branch origin/research/desk-d40, head c868f6fb)

## Lines judged

The whole unit, no sample: all 31 search records (docs/views/searched/desk-d40.jsonl lines 1 to 31), all 8 evidence records (docs/views/evidence/desk-d40.jsonl lines 1 to 8), and the 12 wanted lines (listed, not counted).

## Gate

`python3 -I tools/views/screen_candidates.py --check` on copies of the searched and wanted files prints "0 problems".

## Method

Judged against desk-audit.md, desk-screen.md points 1 to 10, audit 39's counting rule, audit 90's format, and the rulings in the launch prompt. `harvest_get.py` was run for all 13 genera (offline, origin/ci). A script compared each record's unprefixed `queries` with the harvest's `query` and `family review` lines, looked for each `chased` DOI and each screened DOI in the harvest output, and looked for "gave up". Main (origin/main 30e86878) was checked for evidence and search records for every genus.

I ran 44 WebSearches: 8 for evidence titles, 8 for POWO/WFO names, and 28 for null records (genus plus germination, hormone, smoke and flower-timing phrasings). WebFetch was used only on URLs my searches returned. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened (a brum.beds.ac.uk MDPI mirror was left alone). No paper text is committed.

## Mechanical findings

- Queries: all 31 records match the harvest word for word and in order, with "web: " lines after. Osteospermum, Fritillaria and Hippophae are in no harvest run and list web lines only. No "gave up".
- Chased:
  - Ballota, Coptis, Amaranthus: a DOI the harvest family-review step prints. Amaranthus leaves out the zero-hit citation-step DOI 10.3390/plants11233212, which is cosmetic.
  - Heliotropium, Ribes, Sanguisorba: citation-step DOIs the harvest prints.
  - Borago, Shepherdia, Zantedeschia: a none-reason that refers to the harvest's own family-review list. The output supports it. Borago says "10 works", but the harvest prints 15, which is cosmetic.
  - Dodonaea (lines 5 to 7): fails. The reason reads "the harvest ran no citation step or family review for Dodonaea" and cites a web search instead. The harvest prints `family review "Sapindaceae photoreceptor review": 38 hits` with its works, and the record's own `queries` list that line. Under the ruling for harvested genera, this is an error.
  - Osteospermum (16 to 19): a web-only DOI from a labelled "Asteraceae photoreceptor review" search, accepted under the ruling. I did not re-run that search.
- Screened: every screened DOI is printed by the harvest.
- Main: no unit record repeats evidence on main. Main's sweep-15, -31 and -32 search records left these cells open. Amaranthus light (A. retroflexus, A. caudatus), Ribes light (R. uva-crispa), Zantedeschia light (Garner 1999, g) and Sanguisorba light (Holloway and Matheke 2003) are on main, and the unit rightly writes no records for them.

## Search record verdicts (31)

| Line | Record | Verdict |
|---|---|---|
| 1 | Ballota diel | ok. My flower-timing search returned only the Aquilegia paper (Denisow and Antoń 2012, Acta Agrobot 65(1): 37-44, opened, no Ballota). |
| 2 | Ballota eye_type | ok (eye_type is "none" under the owner's reading; queries and chased are sound) |
| 3 | Ballota sense_chemical | ok. My germination GA3 search returned no Ballota trial. |
| 4 | Ballota sense_light_nonvisual | ok. Same search, no Ballota light trial. |
| 5 | Dodonaea diel | **error: unsupported chased.** It misstates the harvest family review (above). My anthesis search returned a floral-development paper and flora pages, with no hour. |
| 6 | Dodonaea eye_type | **error: unsupported chased** (same reason as line 5) |
| 7 | Dodonaea sense_chemical | **error: missed measurement (and chased).** My search "Dodonaea viscosa germination smoke OR gibberellic OR GA3 OR potassium nitrate" returned jhs.um.ac.ir article 35305 (opened): Pourmombeini and Moalemi, "Effect of Hydro and Osmo-Priming in Combination with GA3 and KNO3 on Seed Germination of Dodonaea viscosa under Salinity Conditions". Priming with GA3 at 50 mg/L gave 68% germination and KNO3 at 1% gave 50%. A GA3 and KNO3 germination trial on a named species. |
| 8 | Heliotropium diel | **error: missed measurement.** My search "Heliotropium floral biology anthesis time flower opening morning hours" returned pakbs.org/pjbot/papers/1681376802.pdf (opened): Abid, Nayani, Riaz and Fatima 2023, "The pollination biology of Heliotropium curassavicum L. (Boraginaceae) from Pakistan", Pak J Bot 55(4): 1497-1501. It gives flowers "opened usually from 11:00 a.m.- 2:00 p.m." |
| 9 | Heliotropium eye_type | ok |
| 10 | Coptis diel | ok. My search returned only general pages and the Aquilegia paper. |
| 11 | Coptis eye_type | ok |
| 12 | Borago diel | ok. My search returned Gismondi et al. 2024, Plant Sci 345 (Tor Vergata page opened: a nectar peak at anthesis over days, no hour) and a Symphytum nectar paper (opened). |
| 13 | Borago eye_type | ok |
| 14 | Amaranthus diel | ok. My anthesis search returned no Amaranthus hour. |
| 15 | Amaranthus eye_type | ok |
| 16 | Osteospermum diel | ok. My search returned patents and garden pages. |
| 17 | Osteospermum eye_type | ok |
| 18 | Osteospermum sense_chemical | **error: missed measurement.** POWO (193267-1, opened) gives Chrysanthemoides monilifera (L.) Norl. as "a synonym of Osteospermum moniliferum", the species main's sweep-32 names. My boneseed search returned encyclopedia.pub entry 25723 (opened). It cites Reynolds, Long, Flematti, Cherry and Turner 2013, "Karrikins promote germination of physiologically dormant seeds of Chrysanthemoides monilifera ssp. monilifera (boneseed)", Weed Research 54: 48-57. That is a smoke-compound germination response stated in a title, so it closes the cell as a lead (10(e)). The record's searches used "Osteospermum" and "Cape daisy" only. |
| 19 | Osteospermum sense_light_nonvisual | ok, with a lead: my boneseed light search returned weed fact sheets only, no shown light trial. |
| 20 | Ribes eye_type | ok |
| 21 | Fritillaria diel | ok. Stpiczyńska, Nepi and Zych 2012, Plant Syst Evol 298: 997-1013 (Springer opened) on F. meleagris gives nectar by flowering stage, not hour. |
| 22 | Fritillaria eye_type | ok |
| 23 | Fritillaria sense_light_nonvisual | **error: missed measurement.** My search "Fritillaria seed germination light darkness effect" returned jipb.net abstract24581 (opened): Zhu, Hu and Yu 1980, on the annual growth cycle of Fritillaria pallidiflora Schrenk, J Integr Plant Biol 22(1). The abstract reports that regeneration bulbs form under short-day conditions and even in complete darkness, unlike onion, which needs long days. That is a photoperiod and darkness response of a named species. Fork below. |
| 24 | Hippophae diel | ok. Lu, Ma and Sun 2008, Acta Ecol Sin 28(6) (ecologica.cn opened) gives flower life in days only. |
| 25 | Hippophae eye_type | ok |
| 26 | Shepherdia diel | ok. My search returned sex-ratio and pollination-distance theses with no hour shown. |
| 27 | Shepherdia eye_type | ok |
| 28 | Zantedeschia diel | ok. My scent and spathe-opening search returned nursery pages and an Arum paper. |
| 29 | Zantedeschia eye_type | ok |
| 30 | Sanguisorba diel | ok. My search returned flora pages only. |
| 31 | Sanguisorba eye_type | ok |

Search record errors: **6 of 31 (19.4%)**, lines 5, 6, 7, 8, 18 and 23.

## Evidence record verdicts (8)

Every record was checked on a page my search returned. Species names were checked on POWO or WFO (opened):
- Accepted: Dodonaea viscosa, Heliotropium europaeum, Amaranthus viridis, Hippophae salicifolia, Fritillaria raddeana and Sanguisorba officinalis. POWO's Poterium officinale page is "a synonym of Sanguisorba officinalis".
- Coptis omeiensis is accepted in WFO.

| Line | Record | Verdict |
|---|---|---|
| 1 | Dodonaea viscosa sense_light_nonvisual | ok. UEA eprints 75426 opened: Al-Namazi, Al-Ammari, Davy and Al-Turki 2020, Saudi J Biol Sci 27(9): 2420-2424, 10.1016/j.sjbs.2020.05.036. The quote is a whole sentence. The abstract does state 12-h photoperiods against continuous darkness, so the record's note "does not state the light and dark treatments" is wrong (cosmetic). |
| 2 | Heliotropium europaeum sense_chemical | **error: quote not a whole sentence.** Uludag page opened. The words are verbatim, but they are preceded by "...incubation), and", so they are the second clause of a longer sentence that opens "Untreated seeds showed an extremely high dormancy...". Citation details match. |
| 3 | Amaranthus viridis sense_chemical | **error: quote not a whole sentence.** AGRIS page opened. The sentence goes on "...46.7% and autumn seeds with 68.5% increase was observed.", so the quote stops mid-sentence. The whole sentence is over 125 characters. |
| 4 | Coptis omeiensis sense_chemical | ok. tiprpress page opened. The sentence is verbatim, and the 5.0 and 7.5 mg/L doses match. |
| 5 | Hippophae salicifolia sense_chemical | ok. HEP page opened. The sentence is verbatim, and the citation matches. The abstract does give GA3 at 5, 10 and 20 mM, while the record says it gives no concentration (cosmetic; no dose is mis-copied). |
| 6 | Fritillaria raddeana sense_chemical | ok. DOAJ page opened. The sentence is verbatim. Authors, 8(1): 19-30, 2019, the DOI and GA 250 and 500 mg/L match. |
| 7 | Zantedeschia (genus, g) sense_chemical | ok. Springer page opened. The sentence is verbatim, and the abstract names no species or cultivar ("Black Magic" appears only in the references), so genus grade is right. |
| 8 | Sanguisorba officinalis sense_chemical | ok. CASB page opened. The sentence is verbatim, and the authors and 24(7): 318-322 match. |

Evidence errors: **2 of 8 (25%)**, lines 2 and 3. Both are quote-form faults. The values are right.

## Counts

- Search records: 6 of 31 (19.4%).
- Evidence: 2 of 8 (25%).
- Unit: 8 of 39 (20.5%).

Pooled with audits 83 to 90, from audit 90's figures (48 in 1026 search records, 52 in 1090 overall):
- Search records: 54 in 1057, 5.1%.
- With evidence: 60 in 1129, 5.3%.

Audits after 90 are not in this pool: I do not have their committed figures in this worktree.

Forks:
- Lines 5 and 6. If the desk reads a web-search none-reason as acceptable for a harvested genus, they stand. Search errors would then be 4 of 31 (12.9%), and line 7 stays an error on its missed trial.
- Line 23. If bulb formation under short days or darkness, reported in an abstract without a stated trial design, is not read as a photoperiod trial, line 23 stands. That gives 5 of 31.
- Line 18. It rests on POWO's synonymy (Chrysanthemoides monilifera into Osteospermum moniliferum) and a cited title. The desk's own sweep-32 already treats O. moniliferum as the genus's species.

**Verdict: fail.** The search records fail at 19.4% and the evidence at 25%. The whole unit was judged, so drop the error lines and the rest stands.

**Error lines to drop:**
- docs/views/searched/desk-d40.jsonl: 5, 6, 7, 8, 18 and 23.
- docs/views/evidence/desk-d40.jsonl: 2 and 3. Both could be requoted from other whole sentences, if any fit.

## Wanted lines (listed, not counted)

None of the 12 wanted lines was opened in this audit; the search budget went to null records.
- Line 9 (Tomar and Rattan 2013, Indian Forester 33520): an i-scholar mirror URL for article 33520 came back in a search, but I did not open it.
- Line 1 (bioRxiv 10.1101/2025.01.10.632421): authors and year are empty, as the rule allows.
- Lines 3, 7, 8 and 11 rest on harvest listings only, as the unit says.

## Leads

- Dodonaea viscosa sense_chemical: Pourmombeini and Moalemi (jhs.um.ac.ir article 35305), GA3 and KNO3 priming.
- Heliotropium curassavicum diel: Abid et al. 2023, Pak J Bot 55(4): 1497-1501.
- Osteospermum moniliferum sense_chemical: Reynolds et al. 2013, Weed Research 54: 48-57 (karrikins).
- Fritillaria pallidiflora sense_light_nonvisual: Zhu, Hu and Yu 1980, JIPB 22(1).
- Dodonaea: Evaluación de la propagación sexual de Hayuelo (repository.udistrital.edu.co), unread.

## Not checked

- No pooled epidermal-focusing search was run for the 13 eye_type records. They were judged on queries and chased, since eye_type is "none" for plants.
- The Osteospermum "Asteraceae photoreceptor review" web search was not re-run.
- Wanted lines were not checked (above).
