# Audit 117: desk-d27 (branch origin/research/desk-d27, head 5f8c8962)

## Lines judged

No sample was drawn. The launch prompt asks for the whole unit, so error lines can simply be dropped.
- Search records: all 6 lines of docs/views/searched/desk-d27.jsonl.
- Evidence records: all 3 lines of docs/views/evidence/desk-d27.jsonl.
- Wanted lines: none in the unit.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on a copy of the searched file (6 lines), with an empty wanted file, prints "0 problems". All 3 evidence lines parse. Their quotes are whole sentences of 121, 110 and 105 characters.

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e)), audit 39's counting rule and the shared brief's rulings (audits 84, 86 to 90, and 98 on `chased`). Audits 90 and 115 served as the format. I ran 37 WebSearches:
- 26 for the null records (germination light/dark, GA3/KNO3/smoke, jasmonate and herbivore volatiles, flower opening and anthesis hours, shade and light-intensity trials, named species one at a time);
- 5 that re-ran the records' own labelled searches behind `chased`;
- 4 for evidence sources;
- 2 for POWO names.

I fetched only URLs my own searches returned. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened. An ezproxyberklee.flo.org mirror in one result list was left alone, and so were academia.edu hits in two lists. No paper text is committed. origin/main is at 386b9ecb.

### Queries

`harvest_get.py` ran offline. A script compared each record's unprefixed `queries` with every `query` and `family review` line the harvest prints:
- Claytonia (harvest run 2), Sorbus and Caltha (run 4) and Linaria (run 2) match word for word and in order, with the "web: " lines after them.
- Dactylis and Podophyllum are in no harvest run, and their records list "web: " lines only.
- No harvest shows "gave up", and no unlabelled line appears.
- The Linaria harvest is the bird genus's run (its bird-vision queries are copied as printed). That is the right copy, since harvest_get prints those queries for the name.

### Chased

- Line 6 (Linaria) names 10.4161/psb.22704, a citation step the harvest prints (0 hits). Supported.
- Line 1 (Claytonia) gives a none-reason. The harvest's "Montiaceae photoreceptor review" printed 3 works: an Atacama flower-colour paper, a Cistanthe transcriptome and an Arabidopsis preprint. None is a Montiaceae review, so the reason holds.
- Lines 2 to 5 name 10.3389/fpls.2016.00462 (Fenske and Imaizumi 2016, the general review of circadian rhythms in floral scent emission). No harvest output prints it.
  - My re-runs of the labelled scent searches returned the Frontiers PDF on the first page. That holds for Caltha (the record's exact query), Podophyllum (exact query) and Sorbus (a close variant). Lines 2, 3 and 5 are supported.
  - None of Dactylis's three labelled searches returned it when I ran them word for word. Dactylis is in no harvest run, so line 4's chased has no support. Audit 90 (Olea) and audit 115 (Nasturtium, Cosmos) counted the same case as an error.

### Synonyms

- Caltha palustris var. membranacea: POWO 888903-1 (opened) says "This name is a synonym of Caltha palustris var. palustris", and so does 709325-1 for Caltha membranacea. The record is filed under the right genus and says so in `conditions`.
- Podophyllum hexandrum: POWO 327192-2 (opened) says "This species is accepted" (Sinopodophyllum is cited only as an alternative taxonomy). P. hexandrum results therefore count for Podophyllum.
- Nuttallanthus: main's Linaria canadensis lead (harvest-c8:84) is filed `for` Nuttallanthus canadensis, so it does not bear on the Linaria null.
- Echium and Eschscholzia are accepted genera.

### Main

- Main holds no evidence for Echium, Caltha, Claytonia, Sorbus, Podophyllum or Linaria.
- Eschscholzia californica has sweep-10:4 (Carter 1986, flowering photoperiod), a different measurement. Dactylis glomerata has sweep-9:1 (sense_light_nonvisual), and the unit's Dactylis record is diel.
- The three evidence DOIs or URLs appear on main only as wanted leads (harvest-c13:49, 54, 59), which these records log.
- No search record names a trait that main holds evidence for.

## Search record verdicts (6)

| Line | Record | Verdict |
|---|---|---|
| 1 | Claytonia sense_chemical | ok. Queries match, and the none-reason holds. My searches (GA3 or dormancy; jasmonate, herbivore or volatiles for C. virginica; C. perfoliata and Montia perfoliata nitrate, ethylene or allelopathy; C. virginica and C. lanceolata stratification or hormone) returned seed-shop pages and the Holloway Georgeson note. They also returned UW ESRM 412 protocols for C. lanceolata and C. cordifolia, both opened: cold-moist stratification only, 20% germination (Luna, Evans and Wick 2008), no chemical treatment. No Claytonia chemical response. |
| 2 | Sorbus diel | ok. Queries match, and chased is supported. My searches returned pladias and Trees and Shrubs Online pages, an Ecoscience mass-flowering phenology paper (dates), and the general scent-rhythm reviews (PMC4829607, Fenske 2016). No hour of opening or scent timing for a Sorbus species. Wording fault, not counted: the note says "The Rosaceae photoreceptor search lists no family review", but the harvest printed 333 hits, among them reviews of Rosaceae fruit anthocyanins and strawberry photobiology (none on flower timing). |
| 3 | Caltha diel | ok. Queries match, and chased is supported. My searches returned the Linnaeus flower-clock page (a historical table, not a measurement under the owner's reading) and a Tokyo thesis summary on circadian flower opening (repository.dl.itc.u-tokyo.ac.jp A31570, opened: Eustoma and tomato only). They also returned Denisow and Antoń 2012 (Acta Agrobot 65(1): 37-44, opened: Aquilegia only, opening 5.00 to 7.00) and heliotropism pages. No Caltha hour. |
| 4 | Dactylis diel | **error: unsupported chased.** Web-only, no harvest. I ran the record's three "web: " searches word for word, and none returned 10.3389/fpls.2016.00462 (results: the Worcester eprints, Aerobiologia s10453-020-09685-1, the JIRCAS JARQ PDF, a ragweed anthesis paper, the biostor 137766 PDF, the Tennessee thesis). No missed measurement shown. My other searches returned Calder 1964 (J Appl Ecol, 10.2307/2401315; BES page opened: heading dates only), a Czech BBCH phenology paper (cuni 315590, opened: dates only) and Jones and Newell 1946 (Nebraska AES Res Bull 148, UNL page opened). The UNL keywords do not name orchard grass, and the 30.8 MB PDF failed at its site. Leads below. |
| 5 | Podophyllum diel | ok. Web-only, and chased is supported. My searches returned mayapple extension pages and Xiong et al. 2013, AoB Plants, 10.1093/aobpla/plt037, on P. hexandrum (accepted in POWO). Its botany.one summary (opened) describes petal closure and stamen movement that give delayed selfing, with no time of day. The PMC full text was blocked, so that stays a lead. A Wisconsin Academy record and a "Reproductive biology of Podophyllum" record on search.library.wisc.edu returned "Browser not allowed" and a sign-in offer, so I left them. |
| 6 | Linaria sense_light_nonvisual | ok. Queries match, and chased is printed. I ran searches on Linaria light/dark and photoblastism, L. vulgaris and L. dalmatica light requirement, L. vulgaris shade or light intensity, L. maroccana, L. genistifolia and L. repens, and Iberian Linaria with light and photoperiod. They returned eFloraSys L. vulgaris (opened: 5 to 35 C optimum, no light trial) and a linseed paper (redalyc 445751259005, opened: Linum only). They also returned a clover light paper (uevora dspace, opened: Trifolium only) and seed-shop pages. Serrano-Bernardo, Rosúa and Díaz-Miguel 2007, Phyton 76: 27-38, "Light and temperature effects on seed germination of four native species of Mediterranean high mountains (Spain)" (UGR page opened) does not name its species, so it is an unread lead. |

Search record errors: **1 of 6 (16.7%)**, line 4.

## Evidence record verdicts (3)

| Line | Record | Verdict |
|---|---|---|
| 1 | Echium plantagineum sense_light_nonvisual (Florentine et al. 2018) | ok. CSIRO page (opened): seven authors in order, Crop Pasture Sci 69(3): 326-333, 10.1071/CP17308. The quote is a whole abstract sentence, verbatim. The value (light tested, temperature more influential) is what the abstract supports. Grade m and partial are right. |
| 2 | Caltha palustris sense_chemical (La and Jeong 2007) | ok. KoreaScholar 243873 (opened): authors, Flower Research Journal 15(2): 78-81, June 2007, no DOI. The quote is shown verbatim, and the abstract gives about 51% germination in light and 33% in dark after GA3. Applied GA3 on living seed counts under 10(d). Name status as above. |
| 3 | Eschscholzia californica sense_light_nonvisual (Castillo et al. 2013) | ok. busca.umc.cl record (opened): seven authors in order, Gayana Bot 70(2), 10.4067/S0717-66432013000200010. The page confirms the quoted sentence word for word. Germination was zero at the soil surface and rose when seeds were buried, which supports "light inhibits". Grade m and partial are right. |

Evidence errors: **0 of 3**.

## Counts

- Search records: 1 of 6, 16.7% (line 4).
- Evidence: 0 of 3.
- Unit: 1 of 9, 11.1%.

Pooled from audit 116's figures (search records 49 in 1032; with evidence 56 in 1120):
- Search records: 50 in 1038, 4.82%.
- With evidence included: 57 in 1129, 5.05%.

Fork that would change the count. Line 4's chased is supported only if the desk accepts the record's word that one of its Dactylis searches returned Fenske 2016. My three word-for-word runs did not. If the desk accepts it, the unit has 0 errors and passes.

**Verdict: fail** (search records 1 of 6, above 5%). Search lines 1, 2, 3, 5 and 6 and all three evidence lines stand and can merge.

**Error lines to drop:**
- docs/views/searched/desk-d27.jsonl: line 4 (Dactylis diel). It can be rewritten with a none-reason in `chased`. No missed measurement was shown.
- docs/views/evidence/desk-d27.jsonl: none.

## Leads (not counted)

- Dactylis diel: Jones and Newell 1946, "Pollination Cycles and Pollen Dispersal in Relation to Grass Improvement", Nebraska AES Res Bull 148 (digitalcommons.unl.edu/ardhistrb/206). It gives grass pollen-shedding hours, but whether orchard grass is among the species is unread. Also archive.org biostor-137766, which came back on every Dactylis anthesis-hour search (the fetch permission went unanswered, so it is unread).
- Podophyllum hexandrum diel: Xiong et al. 2013 (10.1093/aobpla/plt037), full text, for petal-closure timing.
- Linaria sense_light_nonvisual: Serrano-Bernardo et al. 2007, Phyton 76: 27-38 (species unread), and plantarum.izbis 386 (the record's own unread lead).
- Sorbus: the note in desk-d27.md rightly keeps Sorbus alnifolia (Micromeles alnifolia in POWO, as the note states) out.

## Blocked pages

- archive.org biostor-137766 PDF: redirect, then fetch permission unanswered.
- pmc.ncbi.nlm.nih.gov PMC4455658: permission unanswered, not retried.
- indianbotsoc.org (Wafai et al., P. hexandrum): failed at its site.
- digitalcommons.unl.edu viewcontent article 1207: failed at its site.
- search.library.wisc.edu records: "Browser not allowed" with a sign-in prompt, so left alone.
