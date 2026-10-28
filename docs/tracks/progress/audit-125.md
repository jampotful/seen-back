# Audit 125: desk-d35 (24 plant genera; branch origin/research/desk-d35, head ae1c531c)

## Lines judged

No sample was drawn. I judged every line in the unit, so error lines can simply be dropped:
- all 24 search records (docs/views/searched/desk-d35.jsonl, lines 1 to 24);
- all 4 evidence records (docs/views/evidence/desk-d35.jsonl, lines 1 to 4);
- the 8 wanted lines, which are listed and not counted.

Each record covers one genus and several traits. Where my own searches did not reach a trait, the table says so.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on copies of the searched file (24 lines) and the wanted file (8 lines) prints "0 problems".

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e) included), the counting rule of audit 39, and the rulings of audits 84, 86, 87 and 90. Audit 90 served as the format.

Queries. `harvest_get.py` ran without the network (it reads origin/ci). A script compared each record's unprefixed `queries` with every `query` and `family review` line the harvest prints.
- All 14 harvested genera match word for word and in order, with their "web: " lines after them: Phlox, Solidago, Gleditsia, Hylocomium, Phleum, Ferocactus, Galanthus, Angelica, Echinocystis, Silybum, Leonurus, Buddleja and Viscum.
- None shows "gave up".
- The 10 genera in no harvest run (Clinopodium, Holodiscus, Dasiphora, Ampelopsis, Spiraea, Sarracenia, Spinulum, Houstonia, Verbena, Hepatica, Medeola) list "web: " lines only, and no unlabelled line appears.

Chased.
- Lines 4, 6, 7, 8, 10, 13, 17, 18, 21, 22 and 23 name 10.1007/s10265-016-0785-4. My run of the pooled family search "Lamiaceae OR Rosaceae OR Vitaceae OR Rubiaceae OR Ranunculaceae OR Verbenaceae OR Sarraceniaceae OR Lycopodiaceae photoreceptor review" returned nutrition-evidence.com article 249643. I opened it: Li and Mathews 2016, J Plant Res 129(2): 115-22, with that DOI. These lines are supported, as in audits 86 and 87.
- Line 2 (Solidago) is a harvested genus. It names the same DOI and leaves out its printed citation step, 10.1111/ele.12205. My run of "Asteraceae photoreceptor review", the record's own labelled web search, also returned the nutrition-evidence page. So the DOI is supported by a labelled web search, and I note the line without counting it (compare Nyssa in audit 92).
- Every other harvested line uses the "none:" form with a reason, which is accepted.

Main. I checked origin/main (342fc7fe) evidence, searched and wanted files for every genus.
- No unit record names a trait for which main holds evidence. Main holds:
  - sense_light_nonvisual for Phlox, Hylocomium, Phleum, Ferocactus, Silybum and Leonurus;
  - sense_chemical for Solidago, Galanthus, Sarracenia and Buddleja.
- The unit's evidence duplicates nothing. Main's Phlox light value is P. paniculata photoperiod; the unit's is P. pilosa germination.
- Main's harvest-c16 wanted file already lists leads for four traits that the unit then filed as null: Gleditsia light (lines 11 and 18), Hylocomium chemical (line 25), Dasiphora diel (line 28) and Ampelopsis light (line 29). Main's leads have no `traits` field, so the unit's rule ("worked unless main held ... a wanted lead for that genus and trait") could not catch them. All four turn out to be measurements, below.

Taxonomy. On POWO pages I opened:
- Hepatica nobilis var. asiatica (2845812-4) "is a synonym of Hepatica asiatica", so H. asiatica is accepted.
- Hypopitys monotropa (582528-1) "is a synonym of Monotropa hypopitys", so skipping Hypopitys was right.
- Potentilla fruticosa (the name in the Dasiphora paper) is Dasiphora fruticosa under POWO's genus Dasiphora.

Title-only screening. The unit screened web results by title only. Every `screened` reason is the same boilerplate ("other taxon, general review or non-study page"). This practice hid at least two measurements that the unit's own first-page results held:
- Gotsch and Ellison 1998, returned by the unit's own Sarracenia query; the Harvard Forest page was dismissed in the note;
- the Phleum Moddus trial.

Searches. I ran about 50 WebSearches:
- 9 for evidence, taxonomy and chased;
- 2 for wanted lines;
- one to three for each null record, using germination/hormone, herbivore and anthesis phrasings under 10(e).

I fetched only URLs my own searches returned. Permission requests that went unanswered, and were not retried:
- archive.org biostor-62737 (Verbena);
- PMC10005799 (I resolved it through its MDPI page instead);
- bioone AMID-173-02-191-207.1 (Phlox, unresolved).

wicri-demo.istex.fr refused me through its robots file. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text is committed. I ran no eye_type focusing search, so the eye_type portion of every record is unchecked for missed measurements.

## Search record verdicts (24)

| Line | Record | Verdict |
|---|---|---|
| 1 | Phlox diel; eye_type | ok, with a lead. Queries match. My scent/opening search returned the general circadian-scent review (PMC4829607) and an Am Midl Nat article (10.1674/AMID-173-02-191-207.1). I could not open the latter (permission unanswered). Main's harvest-c16:8 (daily petal colour shift) is not flower opening under the owner's reading. |
| 2 | Solidago diel; eye_type | ok. Queries match; chased is supported by a web search (noted above). My search returned Su et al. 2025, Pak J Bot 57(2) (opened). It gives insect visits "mainly from 9:00 to 11:00" on S. canadensis, which is visitor timing, not flower opening. |
| 3 | Gleditsia diel; eye_type; sense_chemical; sense_light_nonvisual | **error: missed measurement (sense_light_nonvisual).** My search returned Tognetti, Mazía and Ibáñez 2019, "Seed local adaptation and seedling plasticity account for Gleditsia triacanthos tree invasion across biomes", Ann Bot 124(2): 307-318, 10.1093/aob/mcz077 (repositoriosdigitales.mincyt.gob.ar record opened). The abstract reports that germination of G. triacanthos responded to "light quantity (dark-light) and quality (red-far red) among origins". It is already a lead on main (harvest-c16:11), and so is short-day bud dormancy (harvest-c16:18). |
| 4 | Clinopodium (4 traits) | ok. Web-only; chased is supported. My searches returned Partzsch 2016, Hercynia N.F. 49: 27-45 (opened). It covers C. vulgare, but only under a 12 h light / 12 h dark regime (temperature optimum), with no light-against-dark comparison and no chemical treatment. Diel was not searched by me. |
| 5 | Hylocomium diel; eye_type; sense_chemical | **error: missed measurement (sense_chemical).** My search returned Bay et al. 2013, "Boreal feather mosses secrete chemical signals to gain nitrogen", New Phytol, 10.1111/nph.12403 (SLU earchive record opened). The abstract names Hylocomium splendens as one of the two feather mosses studied. A living moss giving off a chemical signal counts under 10(a), and the title states the result. It is already a lead on main (harvest-c16:25). The screened Vicherová et al. 2020 (Sci Rep 10: 7405; PMC opened) covers Hamatocaulis and Sphagnum only, so it was rightly screened. |
| 6 | Holodiscus (4 traits) | ok. Web-only; chased is supported. My search returned NRCS and propagation pages only. Diel was not searched by me. |
| 7 | Dasiphora (4 traits) | **error: missed measurement (diel).** My search returned Denisow, Antoń and Szymczak 2013, "The Flowering, Pollen Production, and Insect Visitors in the Ornamental Shrub Potentilla fruticosa L. (Rosaceae)", J Apic Sci 57(1): 95-106, 10.2478/jas-2013-0011 (reference-global.com abstract opened). It reports: "Flowers opened most intensively in the morning hours", most by 8.00 h GMT +2h. It is already a lead on main (harvest-c16:28). |
| 8 | Ampelopsis (4 traits) | **error: missed measurement (sense_light_nonvisual).** My search returned Frampton, Valencia and Zimmerman 2018, Purchase College Journal of Ecology vol. 2 (purchase.edu PDF opened). A. brevipedunculata saplings were grown for two weeks at high, medium and low light, and stem and leaf growth were measured. That is a set-light-intensity growth trial, which counts under 10(d). Main also holds a light-quality and quantity thesis lead (harvest-c16:29). |
| 9 | Phleum diel; eye_type; sense_chemical | **error: missed measurement (sense_chemical).** My search returned Bender 2021, "Effect of plant growth regulator and additional nitrogen fertilization in spring on the seed yield and seed quality of timothy (Phleum pratense L.)", Agraarteadus 32(1): 17-24 (DOAJ opened). Moddus 250 EC, applied at 0.4 + 0.4 l ha-1, "shortened the height of generative tillers", and "The germination energy of seed somewhat decreased under the influence of plant growth regulator." That is an applied growth regulator acting on a living plant, which counts under 10(d). |
| 10 | Spiraea (4 traits) | ok. Web-only; chased is supported. My search returned Brzyski and Culley 2013 on S. virginiana, Castanea 78(2) (opened): substrate and cold stratification only, with no light or chemical treatment. It also returned a Lonicera study. Diel was not searched by me. |
| 11 | Ferocactus diel; eye_type | ok. Queries match. My search returned McIntosh 2002, Plant Ecol 159: 1-13 (Springer abstract opened). It gives flowering months for F. cylindraceus and F. wislizeni, with no hour. |
| 12 | Galanthus diel; eye_type | ok, with a lead. Queries match. My search returned Engelmann 2013, "Galanthus nivalis Öffnen und Schließen der Blüten" (Tübingen record opened). It is a time-lapse film whose description gives no timing. It also returned a 1946-47 Belgian note on temperature and snowdrops (not opened). |
| 13 | Sarracenia diel; eye_type; sense_light_nonvisual | **error: missed measurement (sense_light_nonvisual).** My search returned first Gotsch and Ellison 1998, "Seed germination of the northern pitcher plant, Sarracenia purpurea", Northeastern Naturalist 5(2): 175-182 (harvardforest.fas.harvard.edu/print/1073 opened). It reports: "Fewer than 10% of seeds germinated when placed in darkness following stratification" (against ambient light). The unit's note dismisses "a Harvard Forest page" as "none read as a light or dark trial". |
| 14 | Angelica diel; eye_type; sense_light_nonvisual | ok. Queries match. My light/dark search returned only seed-merchant and grower pages. Diel was not searched by me. |
| 15 | Echinocystis diel; eye_type; sense_chemical | ok, with a lead. Queries match. My search returned Böszörményi 2023, Bot Közlem 110(2): 155-166 (opened). It covers fruit and seed size only, and cites Kazinczi et al. 1998 on germination, which I did not see. |
| 16 | Silybum diel; eye_type | ok. Queries match. My search returned Martinelli 2018, Acta Sci Pol Hortorum Cultus 17(3): 101-108 (opened). It advises morning pollen collection and gives no opening hour. |
| 17 | Spinulum (4 traits) | ok. Web-only; chased is supported. My search returned Lycopodium clavatum and Lycopodiella prostrata spore-light papers (valdosta.edu PDF opened). Both are other genera. |
| 18 | Houstonia (4 traits) | ok. Web-only; chased is supported. My two searches returned seed-merchant pages, an NPN protocol and an H. micrantha observation paper (Torrey 147(4), not opened). |
| 19 | Leonurus diel; eye_type; sense_chemical | ok. Queries match. My search returned Tomaz et al. 2004, Planta Daninha 22(3): 359-364 (AGRIS opened). It is on Leonotis, and names Leonurus cardiaca only as the source of a method. |
| 20 | Buddleja diel; eye_type; sense_light_nonvisual | ok. Queries match. My two searches returned Malek et al. 1989 (Kalmia; opened) and Bhatt et al. 2023, Plants 12: 1192 (MDPI opened). Buddleja is not among Bhatt's nine species. |
| 21 | Verbena (4 traits) | ok, partly unchecked. Web-only; chased is supported. My two searches returned the e-FloraSys V. officinalis page (opened: no experiment) and seed-merchant pages. biostor-62737 could not be opened. |
| 22 | Hepatica eye_type | unchecked for misses (no focusing search run by me). Web-only; chased is supported. |
| 23 | Medeola (4 traits) | ok. Web-only; chased is supported. My search returned grower blogs and other-genus stratification papers. |
| 24 | Viscum diel; eye_type; sense_chemical | ok. Queries match. My hormone search returned a seedling biomechanics paper (PMC12369475, not opened) and records I could not open. My scent-timing search returned nothing on Viscum. |

Search record errors: **6 of 24 (25.0%)**, lines 3, 5, 7, 8, 9 and 13. All six are missed measurements. Four of them were already leads on main's harvest-c16 wanted file.

## Evidence record verdicts (4)

| Line | Record | Verdict |
|---|---|---|
| 1 | Phlox pilosa sense_light_nonvisual | ok. AGRIS record opened: Madeiras, Boyle and Autio 2007, HortScience 42(5): 1263-1267. The quote "Light was found to be necessary for germination." is a verbatim abstract result sentence. Grade m and partial are right. The note's "Seeds kept in total darkness germinated less" is a paraphrase I could not see in the abstract (cosmetic). |
| 2 | Phlox longifolia sense_chemical | ok. npj.uwpress.org abstract opened: Ridout and Tripepi 2009, Native Plants J 10(2): 80-90, 10.2979/NPJ.2009.10.2.80. The quote is verbatim. The doses "10 or 20 ml/l liquid smoke" and "100 or 500 ppm GA3", and germination "in the dark", match. A null response of living seed to smoke and KNO3 is a measurement under 10(e). |
| 3 | Echinocystis lobata sense_light_nonvisual | ok. ruj.uj.edu.pl record opened: Filar 2023 (bachelor's thesis, supervisor Stachurska-Swakoń). The quote is verbatim from the English abstract, and the abstract states that light conditions and stratification were tested. |
| 4 | Hepatica asiatica sense_light_nonvisual | ok. AGRIS record opened: Jeong, Jeon, Chon and Yun 2015, Korean J Hortic Sci Technol 33(1): 24-30. The quote is verbatim, and the 52% shading / 65% survival sentence matches the note. A survival trial at set shade levels counts under 10(d). POWO confirms the name is accepted. |

Evidence errors: **0 of 4**.

## Wanted lines (faults listed, not counted)

1. Walck, Baskin and Baskin 1997, Seed Sci Res 7(3): 293-301, 10.1017/s0960258500003640. Confirmed on the UKY page.
2. Ferocactus (Chihuahuan cacti): no DOI, authors or year. Flagged.
3. Galanthus and Narcissus: the title comes from a file name, the authors are empty, and the year is 2015. Flagged; not checked.
4. Angelica archangelica GA3: no DOI, authors or year. Flagged.
5. Moradi et al. 2024: not checked.
6. Chon et al. 2015: not checked.
7. Hepatica nobilis flower ecology (10.5281/zenodo.161177): DOI only, authors empty. Flagged. It also repeats main's wanted sweep-9:9, the same DOI.
8. Viscum album Biological Flora. The Keele repository record (opened) gives J Ecol 111(3): 701-739, published online November 2022, but no authors. The line's authors come from a blog and may be incomplete. Not confirmed.

## Rates and verdict

- This unit: search records 6 in 24 (25.0%); evidence 0 in 4; overall 6 in 28 (21.4%).
- Pooled with audits 83 to 90, starting from audit 90's figures as written (48 in 1026 search records; 52 in 1090 with evidence):
  - search records 54 in 1050, 5.1%;
  - with evidence 58 in 1118, 5.2%.

Verdict: **fail**. The unit is far above 5%. Drop search-record lines 3, 5, 7, 8, 9 and 13 (or reopen the named traits as leads), and keep evidence lines 1 to 4.

Unchecked: the eye_type portion of every record, line 22 as a whole, and the diel portion of lines 4, 6, 10 and 14.
