# Audit 95: desk-d5 (7 plant genera; branch origin/research/desk-d5, head aa8b0bb3)

## Lines judged

No sample was drawn. The launch prompt asks for the whole unit, so that error lines can simply be dropped.
- Search records: all 9 lines of docs/views/searched/desk-d5.jsonl (1 to 9).
- Evidence records: all 14 lines of docs/views/evidence/desk-d5.jsonl (1 to 14).
- Wanted lines: both (listed, not counted).

The unit's progress file covers Plantago, Sassafras, Raphanus, Teucrium, Eryngium, Galium and Tilia; Rudbeckia and Ceratophyllum are named in its genus order but have no lines yet.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on copies of the searched file (9 lines) and wanted file (2 lines) prints "0 problems".

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e)), the counting rule of audit 39, and the rulings of audits 84, 86, 87, 89 and 90, with audits 90 and 94 as the format.

Queries. `harvest_get.py` ran without the network (it reads origin/ci). A script compared each record's unprefixed `queries` with the `query` and `family review` lines the harvest prints. All 9 match. Teucrium (5, 6) and Tilia (9) match word for word and in order, with the "web: " lines after them. Sassafras (1 to 4) and Eryngium (7, 8) are in no harvest run and list "web: " lines only. No harvest shows "gave up", and no line is unlabelled.

Chased.
- Lines 5, 6 and 9 name exactly the citation-step DOIs their harvest output prints.
- Lines 1 to 4 (Sassafras) name 10.1007/s44372-025-00446-3. My own "Lauraceae photoreceptor review" search returned link.springer.com for it on the first page, together with doc.rero.ch 309979 (10.1007/s00239-004-0294-2). I opened the Springer page: de Melo and Alves 2025, "Plant photoreceptors mediate multimodal environmental signaling", Discover Plants, a review, with no Sassafras or Lauraceae. Supported.
- Lines 7 and 8 (Eryngium) name 10.1007/s00239-004-0294-2. My own "Apiaceae photoreceptor review" search returned doc.rero.ch 309979. Supported, as in audits 86, 87 and 90.

Screened. Every screened DOI on lines 5, 6 and 9 is printed by the harvest output. The three OpenAlex ids (W844438413, W2970250993, W2410575972) are listed by `screen_candidates.py` for the trait. All screened titles are off-trait (contact lenses, extracts, other genera), and the reasons hold. The URL entries (USDA seed manual, SciELO, PMC9824129) are rightly screened.

Main. I checked origin/main (a64a3f88) docs/views/evidence and docs/views/searched for every genus in the unit.
- Main evidence: Plantago lanceolata and P. muelleri light (harvest-2:2, recheck-16-fixed:4, oa-9:59); Raphanus sativus thermal and R. raphanistrum light (oa-12:220, recheck-6-fixed:7, sweep-19:1); Eryngium maritimum light (oa-14:19); Galium odoratum light (oa-14:11, 13); Tilia cordata chemical (recheck-6-fixed:5, sweep-15:7). None for Sassafras or Teucrium.
- No unit search record names a trait with evidence on main. The harvest headers agree: Raphanus open diel and sense_chemical; Galium open sense_chemical; Teucrium and Tilia open all four; Plantago open none.
- No unit evidence line repeats a main source or contradicts a main value. Lines 3 (Plantago maxima light), 6 (Raphanus raphanistrum light), 12 (Galium tricornutum light) and 13 (Tilia cordata light) add species to cells main already holds, from other sources. Line 13 fills Tilia light, a cell main's harvest header still lists as open.
- Lines 1 and 2 (Plantago sense_chemical) meet main's null search record harvest-2:21. That record missed these measurements; the unit's evidence is not a repeat, and the old null record should be retired when the evidence lands.
- Main's older sweep records (sweep-2, -3, -12, -15, -19, -26) cover all these genera; the unit's records re-screen those cells, which is noted and not counted (audit 94).

Synonymy. POWO pages opened: Teucrium L. (30039259-2), Eryngium (30001853-2), Tilia L. (39532-1) and Raphanus L. (12986-1) each say "This genus is accepted". WFO (wfo-0000486578, opened) accepts Plantago maxima. The POWO page for Sassafras J.Presl (30028575-2), returned by my search, failed at its site; the search result list shows it as a genus page and the Sassafras species as its members, and I found no synonymy of the genus into another. Plantago and Galium were not opened separately; both are long-standing accepted genera, and no species in the unit is filed under another genus's synonym.

Searches. I ran about 47 WebSearches:
- 15 for the null records (Sassafras 7, including germination light and dark, GA3 and dormancy, herbivore and volatile, anthesis and a set-light seedling search; Eryngium 4; Teucrium 2; 1 pooled focusing search for the four eye_type records; 1 Sassafras tzumu follow-up);
- 2 for family reviews;
- 15 for evidence sources;
- 6 for synonymy;
- 2 for wanted lines.

I fetched only URLs my own searches returned. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened (a uniss.academia.edu result was left alone). No paper text is committed.

## Search record verdicts (9)

| Line | Record | Verdict |
|---|---|---|
| 1 | Sassafras sense_light_nonvisual | ok. Web-only, chased supported. My germination light/dark, GA3/dormancy and seedling-shade searches returned seed vendors, the FEIS species review (opened: cold stratification only, and a microsite association with less light that is no measurement), the USDA seed manual, a Sorbus alnifolia germination paper (MDPI Forests 10: 319, opened, no Sassafras) and a cloud-forest germination paper. No Sassafras light trial. A TUM PDF returned twice was blocked (Anubis), so it stays unread. |
| 2 | Sassafras sense_chemical | ok. Same germination searches; my herbivore, jasmonate and volatile search returned general jasmonate papers on other plants. No living Sassafras response to a hormone, nitrate, smoke or herbivore. |
| 3 | Sassafras diel | ok, with a lead. My anthesis search returned Yang et al. 2022, "Floral morphology and phenology of Sassafras tzumu (Lauraceae)", BMC Plant Biol 22, 10.1186/s12870-022-03714-6. The AGRIS record, figure 4 and figure 5 captions and a summary page (all opened) describe a female phase and a male phase by sequence only, with no clock time or time of day. The PMC full text (PMC9264512) asked for permission and was not retried, so whether the phases are timed by hour stays open. |
| 4 | Sassafras eye_type | ok. Pooled focusing search returned only the general set (AskNature, FIU cas_bio/44, Nature 075535b0, Martin et al. 1989 on Medicago, AGRIS opened); nothing on Sassafras. |
| 5 | Teucrium diel | ok. Queries match. My two searches returned Navarro and El Oualidi 1999, "Flower and life strategy diversity in Teucrium L." (Acta Bot Malac 24: 63-75, PDF opened: season and protandry, no hour), Giuliani et al. 2021 on T. chamaedrys trichomes and volatiles (Flora 282, AIR page opened, no timing), and floras. No Teucrium hour. |
| 6 | Teucrium eye_type | ok. Queries match; the pooled search found nothing on Teucrium. |
| 7 | Eryngium diel | ok, with a lead. Web-only, chased supported. My three searches returned plant-patent PDFs, the E. maritimum dune-network paper, a Nigella damascena nectar study (opened, no Eryngium), and Wróblewska's Lublin Umbelliferae series: Part II (Acta Agrobot 46(1): 51-65, DOAJ opened) gives insect visitation on E. planum and no hour, and a pbsociety abstract (opened) gives E. planum flower counts and no hour. Part I of the series, on flowering, may hold daily dynamics; not found. |
| 8 | Eryngium eye_type | ok. Web-only, chased supported; the pooled search found nothing. |
| 9 | Tilia eye_type | ok. Queries match; the screened works are contact-lens, corneal and leaf-micromorphology titles; the pooled search found nothing on Tilia. |

Search record errors: **0 of 9 (0%)**.

## Evidence record verdicts (14)

Each source page below was returned by my own search and opened.

| Line | Record | Verdict |
|---|---|---|
| 1 | Plantago lanceolata sense_chemical | ok. pakbs.org abstract page: Sarihan, Ipek, Khawar, Atak and Gurbuz 2005, Pak J Bot 37(4): 883-887. The quote is verbatim. Applied GA3 and KNO3 on living seed counts under 10(d) and 10(e). The record's `conditions` says the abstract gives no light regime, but the page gives incubation at 20 C under a 16 h photoperiod (cosmetic). |
| 2 | Plantago major sense_chemical | ok. NAU experts page: Dijkstra and Kuiper 1989, Physiol Plant 77(4): 512-518, 10.1111/j.1399-3054.1989.tb05385.x. The quote is verbatim. |
| 3 | Plantago maxima sense_light_nonvisual | ok. mtak.hu page: Kovács, Barabás and Höhn 2018, Bot Közlem 105(2): 243-252, 10.17716/BotKozlem.2018.105.2.243. "fényen 40%, fénytől elzárva 2,7% mag csírázott ki" is verbatim. |
| 4 | Raphanus sativus sense_chemical | **error: owner's reading.** natuurtijdschriften.nl page: Stulen, Koch-Bosma and Koster 1973, Acta Bot Neerl 22(5): 581-588; the summary gives high nitrate reductase activity after 24 h of induction. The value is accurate, but the measurement is the induction of a nitrate-assimilating enzyme by its substrate, a nutrient-ion response with no hormone, elicitor, herbivore or volatile. The owner's reading excludes nutrient-ion uptake and audit 89 counted a nutrient-ion response the same way. KNO3 counts under 10(e) as a germination cue, which this is not. Fork below. |
| 5 | Raphanus raphanistrum sense_chemical | ok, borderline. IRIS Unina page: Chan, Pellegrini, Zuellig, Guzzetti, Sala, Loreto, Scopece and Cozzolino 2026, J Chem Ecol 52(1), 10.1007/s10886-025-01677-0. The quote is verbatim. Floral volatiles of five natural populations, tested as signals of defence status, fit 10(a) (a living plant giving off volatiles as a signal). The abstract does not say how the volatiles were sampled, which the record's note flags. |
| 6 | Raphanus raphanistrum sense_light_nonvisual | ok. Cambridge page: Malik, Norsworthy, Riley and Bridges 2010, Weed Sci 58(2): 136-140, 10.1614/WS-09-109.1. The quote and the light/dark result are verbatim. |
| 7 | Teucrium marum sense_light_nonvisual | ok. ISHS page: Benvenuti, Ceccarini and Macchia 2006, Acta Hortic 723: 315-320. The quote is verbatim. The ISHS page gives DOI 10.17660/ActaHortic.2006.723.44, which the record's empty DOI field omits (cosmetic). |
| 8 | Teucrium santae sense_light_nonvisual | ok. reference-global page: Bentekhici, Mehdadi and Latreche 2023, Folia Oecol 50(2): 174-184. The sentence is "The seed's photosensitivity was tested afterward and found to be indifferent."; the quote is its last three words, so it is not a whole sentence (form only, value right). |
| 9 | Teucrium polium sense_chemical | ok. jcesc.um.ac.ir page: Koocheki and Azizi 2005, Iran J Field Crops Res 3(1): 81-88, 10.22067/gsc.v3i1.1294. The quote opens the abstract sentence verbatim, and the chilling result is in the same sentence. |
| 10 | Eryngium maritimum sense_chemical | ok. LU research page: Necajeva and Ievinsh 2013, Est J Ecol 62(2): 150-161, 10.3176/eco.2013.2.06. The quote is verbatim. |
| 11 | Galium tricornutum sense_chemical | ok. Adelaide repository page: Chauhan, Gill and Preston 2006, Weed Sci 54(3): 471-477, 10.1614/WS-05-176R1.1. The KNO3 figures (26 and 37% to 56 and 68%) and the GA3 darkness sentence are verbatim. |
| 12 | Galium tricornutum sense_light_nonvisual | ok. Same page: "In the absence of chilling, seeds germinated only in the darkness" and "Germination was inhibited by light". |
| 13 | Tilia cordata sense_light_nonvisual | ok. OUP page: Aasamaa and Aphalo 2017, Tree Physiol 37(2): 209-219, 10.1093/treephys/tpw091. Growth under set shade treatments and stomatal responses to coloured light; the blue-light and red/green results match the value. |
| 14 | Tilia diel | ok. KoreaScience page: Chung 1984, J Plant Biol 27(3): 107-127. The abstract gives anther and stigma opening "during the day-time in section(sect) Anastraea" and "the night-time in sect Astrophilyra", for six native and one introduced species, none named. Grade g for sections of the genus is right. |

Evidence errors: **1 of 14 (7.1%)**, line 4.

## Counts

- Search records: 0 of 9, 0%.
- Evidence: 1 of 14, 7.1%.
- Unit: 1 of 23, 4.3%.

Pooled with the desk's audits 83 to 90, from audit 90's figures (search records 48 in 1026; 52 in 1090 with evidence):
- Search records: 48 in 1035, 4.6%.
- With evidence included: 53 in 1113, 4.8%.

With audits 91 to 94 as their reports give them (search 1 in 13, 3 in 12, 3 in 14, 6 in 14; unit 1 in 23, 4 in 23, 4 in 25, 6 in 20), the pool before this audit is 61 in 1079 search records and 67 in 1181 overall; with audit 95 it is 61 in 1088 (5.6%) and 68 in 1204 (5.6%).

Forks that would change the count:
- Line 4 (Raphanus sativus nitrate reductase). If the desk reads nitrate as a chemical cue whenever a living plant responds to it, as with KNO3 in germination, line 4 stands and the unit has no error. The record's author field note ("names garbled by the scan") is also stale: the natuurtijdschriften page prints Ineke Stulen, T. Koch-Bosma and A. Koster plainly.
- Line 5 (Raphanus raphanistrum volatiles). If the desk wants a receiver's response or sampling from intact flowers shown, line 5 would also fail, and evidence would be 2 of 14.

**Verdict: pass.** The search records pass at 0 of 9. The evidence has one error (line 4, 7.1% of 14), and the unit as a whole stands at 1 of 23 (4.3%). Both whole files were judged, so drop the error line and the rest of the unit stands.

**Error lines to drop:**
- docs/views/searched/desk-d5.jsonl: none.
- docs/views/evidence/desk-d5.jsonl: line 4 (Raphanus sativus sense_chemical). Raphanus sense_chemical stays closed by line 5 if the desk keeps it.

## Wanted lines (listed, not counted)

- Line 1 (Ashman, Galloway and Stanton 1993): authors, title, Oecologia 96: 102-107, year and DOI 10.1007/BF00318036 match the Springer page (opened). The abstract says "diurnal schedules of flower opening, stigma saturation with pollen, and pollen removal indicated that most effective matings occurred before noon". That is flower-opening timing in R. sativus stated in the abstract, so under 10(e) it could close Raphanus diel as a lead now.
- Line 2 (The pollination biology of Tilia, 1976, 10.1002/j.1537-2197.1976.tb13205.x): the NYBG IABL record (opened) gives Anderson, Gregory J., Am J Bot 63: 1203-1212, 1976. The line's author field is empty and could be filled from that page. The DOI page itself was not opened.

## Leads

- Sassafras tzumu diel: Yang et al. 2022, BMC Plant Biol 22 (10.1186/s12870-022-03714-6), full text on PMC9264512 unread here.
- Eryngium planum diel: Wróblewska's Lublin Umbelliferae series, Part I (flowering), not found.
- Raphanus sativus diel: Ashman et al. 1993 abstract (wanted line 1).
- Teucrium chamaedrys sense_chemical: "Effect of Different Treatments on Breaking Dormancy of Teucrium chamaedrys L. Seed" (jmpb.areeo.ac.ir article_108606), returned by my search; not needed, since line 9 closes the cell.

## Blocked pages

- pmc.ncbi.nlm.nih.gov PMC9264512: permission unanswered, not retried.
- mediatum.ub.tum.de 1182841 PDF: Anubis access denied.
- powo.science.kew.org urn:lsid:ipni.org:names:30028575-2 (Sassafras): failed at its site.
- No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text was committed.
