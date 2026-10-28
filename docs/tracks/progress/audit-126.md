# Audit 126: desk-d36 (18 plant genera; branch origin/research/desk-d36, head 24ab46d1)

## Lines judged

No sample was drawn: the shared brief asks for the whole unit, so error lines can simply be dropped.
- Search records: all 36 lines of docs/views/searched/desk-d36.jsonl. All were checked mechanically (queries, chased, main). The 19 null records on a diel, sense_chemical or sense_light_nonvisual cell (lines 1, 3, 5, 7, 8, 10, 12, 14, 15, 16, 18, 20, 22, 24, 26, 30, 32, 33, 36) each got searches of my own. The 17 eye_type records got one pooled focusing search.
- Evidence records: all 3 lines of docs/views/evidence/desk-d36.jsonl.
- Wanted lines: all 5, listed and not counted.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on copies of the searched file (36 lines) and the wanted file (5 lines) prints "0 problems".

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e) included), the counting rule of audit 39, and the rulings of audits 84, 86, 87, 88 and 90. Audit 90 served as the format.

Queries. `harvest_get.py` ran without the network. A script compared each record's unprefixed `queries` with every `query` and `family review` line the harvest prints for the genus. All 26 records of the 12 harvested genera match word for word and in order, with the "web: " lines after them. No harvest shows "gave up", and no record has an unlabelled extra line. Ulex, Scilla, Lysichiton, Allium, Orchis and Arctium are in no harvest run, and their records list "web: " lines only.

Chased.
- Lines 9 (Xanthium) and 35 (Rhododendron) name the one citation-step DOI their harvest prints.
- **Lines 18 and 19 (Marrubium) and 20 and 21 (Lycopus)**: the harvest prints two citation steps, 10.1111/een.12947 and 10.1016/j.isci.2022.104455. The records name only the first.
- **Line 34 (Opuntia)**: the harvest prints 10.1016/j.jaridenv.2016.11.003 and 10.3390/plants11233212. The record names only the first.
- Both harvests report 0 citing works for each DOI, so the omission hides no measurement. The launch prompt's rule is that every citation-step DOI the harvest ran is named, so I count these five lines. See the fork below.
- Lines 26 and 27 (Orchis) and 36 (Arctium) name 10.1007/s44372-025-00446-3. I ran "Orchidaceae photoreceptor review" and "Asteraceae photoreceptor review", and both returned link.springer.com s44372-025-00446-3 on the first page, so these are supported (audits 86 and 87). A springerlink.bibliotecabuap.elogim.com result in the same list was left alone.
- The remaining lines give "none" reasons. These name the family search (harvest or labelled web) as the protocol requires.

Main. I checked origin/main docs/views/evidence/*.jsonl, searched/*.jsonl and wanted/*.jsonl for every genus in the unit.
- No unit search record names a cell that has evidence on main, and no main search record duplicates one.
- No unit evidence record duplicates main. Main has Allium sense_light_nonvisual only and Rhododendron sense_light_nonvisual only, and holds no Scilla evidence.
- Every cell the progress file skips for "a wanted lead on main" has one in harvest-c17.jsonl (Goodyera, Calamagrostis, Marrubium, Lycopus, Orchis, Diplacus, Scilla).

Genus names. Every genus in the unit is accepted. POWO has pages for Anemonastrum Holub and Anemonastrum canadense (L.) Mosyakin. Diplacus is the record's own genus. Lines 30 to 33 screen the Anemone rivularis var. flore-minore light and dark hormone paper as "Anemone, not Anemonastrum". POWO (708608-1 and 60468400-2, opened) gives both names as synonyms of Eriocapitella rivularis, so the exclusion is right, though the record names the wrong genus as the reason.

Searches. I ran about 50 WebSearches:
- 6 for evidence sources;
- 3 for taxonomy;
- 2 for family reviews;
- about 31 for null records;
- 1 pooled eye_type focusing search;
- 6 for wanted lines.

I fetched only URLs my own searches returned. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened. An academia.edu result and a brum.beds.ac.uk mirror were left alone. No paper text is committed.

## Search record verdicts (36)

| Line | Record | Verdict |
|---|---|---|
| 1 | Ulex diel | ok. Web-only. My gorse anthesis and smoke searches returned no opening hour. |
| 2 | Ulex eye_type | ok. The pooled focusing search found nothing on Ulex. |
| 3 | Ulex sense_chemical | ok, with a lead. My searches "Ulex parviflorus smoke heat germination Mediterranean", "Ulex europaeus ... smoke OR nitrate OR gibberellic acid" and "gorse ... smoke water OR karrikin" returned Moreira, Tormo, Estrelles and Pausas 2010, "Disentangling the role of heat and smoke as germination cues in Mediterranean Basin flora", Ann Bot 105(4): 627-635, 10.1093/aob/mcq017 (UA repository opened). The Pausas page on Ulex parviflorus (opened) lists it, but neither page names Ulex among the species tried, and PMC2850801 returned a reCAPTCHA. No Ulex smoke result is shown, so the lead is not counted. |
| 4 | Scilla eye_type | ok. The pooled search found nothing. |
| 5 | Diphasiastrum diel | ok. Clubmosses have no flowers, and my spore-germination search returned only Lycopodium clavatum (Whittier 2008), another genus. |
| 6 | Diphasiastrum eye_type | ok. |
| 7 | Diphasiastrum sense_chemical | ok. My search returned no Diphasiastrum spore or chemical trial. |
| 8 | Diphasiastrum sense_light_nonvisual | ok. My search "Diphasiastrum OR Lycopodium complanatum spore germination light requirement darkness" returned only the red-light study of Lycopodium clavatum, another genus. |
| 9 | Xanthium eye_type | ok. Queries and chased match. |
| 10 | Goodyera diel | ok. Brzosko et al. 2023, IJMS 24(10): 8602, 10.3390/ijms24108602 (MDPI opened), studies G. repens flowers and nectar but measures no opening or scent timing. |
| 11 | Goodyera eye_type | ok. |
| 12 | Lysichiton diel | ok, with a lead. My searches returned an aroid-society page, an Arum concinnatum transcriptome paper (PMC5390080, opened: no Lysichiton), and "Plant-Pollinator Interactions in a Northwest Arum Related to Plant ..." (Northwest Science 89(3), 10.3955/046.089.0310). BioOne returned empty pages for the last, so its content is unknown. It is not counted. |
| 13 | Lysichiton eye_type | ok. |
| 14 | Lysichiton sense_chemical | ok. No germination, hormone or volatile trial on L. americanus or L. camtschatcensis surfaced. |
| 15 | Lysichiton sense_light_nonvisual | ok. Same searches. |
| 16 | Calamagrostis diel | ok. Two anthesis-hour searches returned flora and database pages only. |
| 17 | Calamagrostis eye_type | ok. |
| 18 | Marrubium diel | **error: chased omits the harvest citation step 10.1016/j.isci.2022.104455.** My anthesis search returned Lublin flowering-biology papers on Aquilegia (Denisow and Antoń 2012) and Melissa (Chwil 2009), both opened. Neither is Marrubium, so no measurement was missed. |
| 19 | Marrubium eye_type | **error: chased omits 10.1016/j.isci.2022.104455** (same as line 18). |
| 20 | Lycopus diel | **error: chased omits 10.1016/j.isci.2022.104455.** My search returned flora pages and the same Aquilegia paper, with no Lycopus hour. |
| 21 | Lycopus eye_type | **error: chased omits 10.1016/j.isci.2022.104455.** |
| 22 | Diplacus diel | ok. |
| 23 | Diplacus eye_type | ok. |
| 24 | Diplacus sense_chemical | ok. My smoke search returned Keeley and Fotheringham 1998 (USGS opened), whose abstract names no Diplacus. My herbivory searches returned Lincoln 1985 (J Chem Ecol 11: 1459-1467, Springer opened), which manipulates fertiliser, a nutrient cue, and does not induce resin. Johnson et al. 1984 (Oecologia 61: 398-402) measures Eriodictyon. Lincoln and Mooney 1984 (Oecologia 64: 173-176) is a sun and shade trial, which belongs to sense_light_nonvisual, a cell already on main's wanted list. |
| 25 | Allium eye_type | ok. |
| 26 | Orchis diel | ok. Chased is supported (above), and no Orchis opening hour turned up. |
| 27 | Orchis eye_type | ok. Chased is supported. |
| 28 | Amelanchier eye_type | ok. |
| 29 | Orthilia eye_type | ok. |
| 30 | Anemonastrum diel | ok. My opening-rhythm search returned nothing on the genus. |
| 31 | Anemonastrum eye_type | ok. |
| 32 | Anemonastrum sense_chemical | ok. My A. canadensis and A. narcissiflora germination searches returned the Holloway 2011 GA note (UAF, opened: no Anemone), seed-vendor and propagation pages, and the Eriocapitella paper (above). |
| 33 | Anemonastrum sense_light_nonvisual | ok. Same searches. The Ge et al. 2020 light and dark germination study (Chinese J Ecol 39(6): 1974, opened) is on Eriocapitella rivularis, not Anemonastrum. |
| 34 | Opuntia eye_type | **error: chased omits the harvest citation step 10.3390/plants11233212.** |
| 35 | Rhododendron eye_type | ok. |
| 36 | Arctium diel | ok. Chased is supported. My anthesis search returned crib and flora pages and a haskap paper, with no burdock hour. |

Search record errors: **5 of 36 (13.9%)**, lines 18, 19, 20, 21 and 34. All five are incomplete `chased` fields. No measurement was missed.

## Evidence record verdicts (3)

| Line | Record | Verdict |
|---|---|---|
| 1 | Scilla siberica diel | ok. The agro.icm.edu.pl PDF (opened) is Acta Agrobotanica 64(1): 11-18, 2011. The quoted sentence is in Results (Flowering), and the Results give the latest end of bud opening for S. sibirica at 5.00 pm, as the value says. The pbsociety page (opened) gives Beata Żuraw and 10.5586/aa.2011.002. This is a measured flower-opening hour and not a Methods sampling time. Grade m is right for the named species. |
| 2 | Allium fistulosum sense_chemical | ok. The iar.shirazu.ac.ir page (opened) holds the quote verbatim in the abstract, and gives doses of GA3 0, 100 and 200 ppm and IBA 0, 100 and 200 ppm, as the record copies them. The PDF (opened) gives Fazeli Kakhki and Beikzadeh, Iran Agric Res 41(1): 39-47, 2022, 10.22099/IAR.2022.40940.1453. An applied hormone acting on living seed counts under 10(d). |
| 3 | Rhododendron viscosum diel | ok. The sej.kgau.ru page (opened) gives Koksheeva, Tvorogov and Nekhaychenko, Bulletin of KSAU 5: 296-301, 2018, with no DOI. The quote (117 characters) is the abstract's result sentence ("are revealed"), which reports observed blooming rhythms. The circadian cause is the authors' hypothesis, and the record does not claim it. Opening at night is flower-opening timing. `partial` is set, and the categorical value fits an abstract with no hours. |

Taxa. Scilla siberica, Allium fistulosum and Rhododendron viscosum are each a name in their own genus, so the synonym-of-another-genus rule does not apply. The source spells the first "sibirica", which the record notes.

Evidence errors: **0 of 3 (0%)**.

## Counts

- Search records: 5 of 36, 13.9%.
- Evidence: 0 of 3, 0%.
- Unit: 5 of 39, 12.8%.

Pooled with audits 83 to 90 of desk-screen units, starting from audit 90's figures (48 in 1026 search records, 52 in 1090 overall):
- Search records: 53 in 1062, 5.0%.
- With evidence: 57 in 1129, 5.0%.

Fork that would change the count. The five errors are all `chased` fields that name one of two citation-step DOIs, where both returned 0 citing works. The launch prompt makes naming every one a rule, and audit 90 judged "name exactly the citation-step DOIs". If the desk treats an omitted zero-hit citation step as cosmetic, the unit has 0 errors in 39 and passes. The pool would then be 48 in 1062 search records (4.5%) and 52 in 1129 overall (4.6%).

**Verdict: fail** at 13.9% for search records under the launch prompt's rule. Every fault is a field repair, and no measurement was missed. The evidence passes at 0 of 3. The whole files were judged, so drop or repair the error lines and the rest stands.

**Error lines:**
- docs/views/searched/desk-d36.jsonl: lines 18, 19, 20 and 21 (add 10.1016/j.isci.2022.104455 to `chased`) and line 34 (add 10.3390/plants11233212).
- docs/views/evidence/desk-d36.jsonl: none.

## Wanted lines (listed, not counted)

- Line 1 (Atlan et al. 2015): the authors, year, PLoS ONE 10(9): e0137500 and title match the DOAJ record (opened). The DOI suffix pone.0137500 matches the PMC4575064 figure URLs my search returned.
- Line 2 (Gloser, Scheurwater and Lambers 1996): the authors, year, title and New Phytologist 134(3) match the muni.cz page (opened). The page shows no DOI, and the DOI field is empty as the line says.
- Line 3 (jpacd v17, 10.56890/jpacd.v17i.61): **flagged: DOI with empty authors.** My title search did not return its page, so it is unchecked.
- Line 4 (Plants 13(7): 963, 10.3390/plants13070963): **flagged: DOI with empty authors.** ScaleNet (opened) gives Rodríguez-Leyva, García-Pascual, González-Chávez, Méndez-Gallegos, Morales-Rueda, Posadas-Hurtado, Bravo-Vinaja and Franco-Vega, 2024, with this DOI, so the authors can be filled.
- Line 5 (Ma et al. 2015): the authors, year, J Syst Evol 53(1): 63-71 and 10.1111/jse.12114 match the jse.ac.cn page (opened).

## Leads (not counted)

- Ulex sense_chemical: Moreira et al. 2010, Ann Bot 105: 627-635 (10.1093/aob/mcq017), the heat and smoke trial of Mediterranean Basin flora. Check whether Ulex parviflorus is among its species.
- Lysichiton americanus: Northwest Science 89(3), 10.3955/046.089.0310, "Plant-Pollinator Interactions in a Northwest Arum Related to Plant ...". Unread.
- Diplacus aurantiacus sense_light_nonvisual: Lincoln and Mooney 1984, Oecologia 64: 173-176, a shrub growth trial in sun and shade. The cell already holds a main wanted lead.
- Arctium lappa sense_chemical: the unit's own note names two GA3 and KNO3 germination pages that show no bibliographic data.

## Blocked pages

- pmc.ncbi.nlm.nih.gov PMC2850801: reCAPTCHA, not retried.
- bioone.org 10.3955/046.089.0310 (.short and .full): empty pages.
- No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text was committed.
