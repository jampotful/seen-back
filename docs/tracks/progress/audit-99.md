# Audit 99: desk-d8 (12 plant genera; branch origin/research/desk-d8, head 2a3a044c)

## Lines judged

No sample was drawn. The launch prompt asks for the whole unit, so that error lines can simply be dropped.
- Search records: all 26 lines of docs/views/searched/desk-d8.jsonl (1 to 26). The progress note says 25, but the file holds 26.
- Evidence records: all 12 lines of docs/views/evidence/desk-d8.jsonl (1 to 12).
- Wanted lines: all 3, listed and not counted.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on copies of the searched file (26 lines) and the wanted file (3 lines) prints "0 problems".

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e)), the counting rule of audit 39, and the rulings of audits 84 and 86 to 90, with audit 90 as the format. I ran about 50 WebSearches:
- 22 for the 14 null records that are not eye_type;
- 2 pooled focusing searches for the 12 eye_type records;
- 3 for the web-only family reviews;
- 12 for evidence sources;
- 7 for synonymy;
- 2 for wanted lines.

I fetched only URLs my own searches returned. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened. An independent.academia.edu result and an onlinelibrary-wiley-com-443.webvpn.zafu.edu.cn result were left alone. No paper text is committed.

Queries. `harvest_get.py` ran without the network (it reads origin/ci). A script compared each record's unprefixed `queries` with every `query` and `family review` line the harvest prints. All 26 records match word for word and in order, with the "web: " lines after them. No harvest shows "gave up", and no record has an unlabelled line. Amorpha, Carica, Typha, Pueraria, Thunbergia and Morus are in no harvest run, and their records list "web: " lines only.

Chased.
- Leucaena, Fagus, Eleusine and Symphyotrichum (lines 1 and 19 to 22, 25, 26) name exactly the citation-step DOIs their harvest prints.
- Stellaria (23, 24) names 10.1093/jxb/eru327. The harvest has no citation step for Stellaria, but it prints that DOI ("Flower opening and closure: an update", 2014), so I accept it.
- Thelypteris (17, 18) gives "no family review found". The harvest's "Thelypteridaceae photoreceptor review" printed 2 hits: a leaf-beetle paper and an epiphytic-fern clonality paper. Neither is a photoreceptor review, so the reason holds in substance.
- Carica and Morus (8, 9, 16) give "no family review found" from web searches only. This is accepted.
- 10.1007/s00239-004-0294-2 (Lariguet and Dunand, doc.rero.ch 309979) is named for Amorpha and Pueraria (2 to 7) and Typha (10, 11). My "Fabaceae photoreceptor review" and "Typhaceae photoreceptor review" searches both returned doc.rero.ch 309979 on the first page, so the DOI is supported (audits 86 and 87).
- 10.1007/s44372-025-00446-3 is named for Thunbergia (12 to 15). My "Acanthaceae photoreceptor review" search returned link.springer.com/article/10.1007/s44372-025-00446-3, so it is supported.

Screened. Every screened DOI is printed in its genus's harvest output. The four OpenAlex ids are not printed (W140233209 on line 1, W1844947802 and W1521837500 on line 23, W7220607642 on line 26), but all four are in the harvest data (`harvest_get.load()`). No screened reason is wrong for its trait.

Main (origin/main a0136e11, docs/views/evidence, searched and gaps/queue). No unit evidence line repeats or contradicts evidence on main. Main holds the following for these genera:
- Leucaena: light only.
- Fagus: light only (harvest-13:1, 2).
- Thelypteris: chemical (oa-9) and light (sweep-97:4).
- Pueraria: diel (oa-13b:43) and light.
- Stellaria, Typha and Symphyotrichum: light only.
- Morus: animal (gannet) traits only.
- Amorpha, Carica, Eleusine and Thunbergia: no plant-trait evidence.

No null search record names a trait that main holds evidence for. Line 24 (Stellaria eye_type) repeats main's search record plant-1:4. As in audits 90 and 97, the repeat is noted and not counted. The queue still lists that cell.

Genus status (POWO pages returned by my searches). Symphyotrichum lanceolatum (981841-1), Thelypteris palustris (17226930-1) and Pueraria montana var. lobata (967441-1, with Pueraria lobata as a homotypic synonym) are each opened and "accepted". POWO entries for Fagus crenata Blume (295581-1) and Leucaena leucocephala (Lam.) de Wit (138955-2) were returned under their own names, not opened. Carica papaya, Fagus sylvatica, Eleusine coracana, Stellaria media, Typha latifolia and Morus nigra were not checked page by page; each is the type or a long-standing species of its own genus. No line is filed under a synonym's genus. The unit was right to hold Pueraria phaseoloides out as Neustanthus phaseoloides.

## Search record verdicts (26)

| Line | Record | Verdict |
|---|---|---|
| 1 | Leucaena eye_type | ok. Queries and chased match. My pooled focusing searches returned only the general set (AskNature, FIU cas_bio/44, Nature 075535b0, the Faraday Discussions 2020 paper, an arXiv algal-optics paper) and leaf-anatomy pages, nothing on focusing in any unit genus. |
| 2 | Amorpha sense_light_nonvisual | ok. My searches returned Sera et al. 2023 (the record's source), Wildflower Center notes, a Russian Far East fruiting paper and a Zagreb thesis, with no light-against-dark trial. |
| 3 | Amorpha diel | ok. My search returned only extension, arboretum and flora pages, with no hour. |
| 4 | Amorpha eye_type | ok. The pooled search found nothing. |
| 5 | Amorpha sense_chemical | ok. My herbivore, jasmonate and volatile search returned the Croatian leaf-extract allelopathy entries, which are tissue chemistry (10(a)), and papers on other plants. My germination search returned no Amorpha GA3 or nitrate trial. |
| 6 | Pueraria eye_type | ok. The pooled search found nothing. |
| 7 | Pueraria sense_chemical | **error: missed measurement.** My search "Pueraria lobata methyl jasmonate OR salicylic acid treatment plants isoflavone puerarin induction" returned Wang, Li, Zhou and Zhang 2019, "Identification of Three (Iso)flavonoid Glucosyltransferases From Pueraria lobata", Front Plant Sci 10: 28 (frontiersin.org PDF opened). Two-week-old P. lobata seedlings were given 100 µM MeJA for 7 days. Expression of PlUGT4, 15 and 57 "correlated with the accumulation of isoflavone glucosides in MeJA-treated P. lobata". That is a living plant's response to an applied elicitor (10(d)), and P. lobata is Pueraria montana var. lobata in POWO. The same search returned a 2016 Frontiers paper on P. lobata (10.3389/fpls.2016.00793; its epub came back as binary data, unread). |
| 8 | Carica sense_light_nonvisual | **error: missed measurement (10(e)).** My search "Carica papaya seed germination light darkness phytochrome" returned the IPB repository record (opened) for Suwarno 1990, "Pengaruh Cahaya Dan Perlakuan Benih Terhadap Perkecambahan Benih Pepaya (Carica papaya L.)", Buletin Agronomi XV(3). Papaya seeds were incubated in light and in darkness. The abstract gives no result, but a title naming light and germination for a species of the genus must go on the wanted list and cannot stay outside the record (10(e); audit 90, Szewczuk). The record neither names nor lists it. Main's sweep-43:20 knew of the same title. |
| 9 | Carica eye_type | ok. The pooled search found nothing. |
| 10 | Typha diel | ok. My three searches returned the ragweed diurnal-dispersal paper (Martin, Chamecki and Brush 2010, PSU page opened: Ambrosia only), the Typha hybrid pollen-dispersal dataset (distance, not hour), floras and FNA. No Typha hour. |
| 11 | Typha eye_type | ok. The pooled search found nothing. |
| 12 | Thunbergia sense_light_nonvisual | ok. My searches returned vendor and cultural pages and no light-against-dark germination trial. |
| 13 | Thunbergia diel | ok. My two searches returned Fiala et al. 1996 (Malayan Nature J 50: 1-14, AGRIS opened: ants and bud protection, no opening hour), a floral-development paper, and patent and NParks pages. |
| 14 | Thunbergia eye_type | ok. The pooled search found nothing. |
| 15 | Thunbergia sense_chemical | ok. My hormone search returned only rooting of T. mysorensis cuttings with IBA (UFRGS). Audit 87 excludes rooting of cuttings under the cut-branch rule, so it does not count. |
| 16 | Morus eye_type | ok. The pooled search returned only Moraceae leaf micromorphology (SEM identification), which is not focusing. |
| 17 | Thelypteris diel | ok. My search returned a fungal-spore timing paper and T. palustris spore-structure and germination-bank pages, with no clock time. |
| 18 | Thelypteris eye_type | ok. The pooled search found nothing. |
| 19 | Fagus diel | ok. My search returned Puc 2012 (AAEM 19(4): 660-665, icm.edu.pl PDF opened: hourly Betula and Fraxinus pollen only, no Fagus) and Fagus pollen-accumulation papers. No Fagus hour. |
| 20 | Fagus eye_type | ok. The pooled search found nothing. |
| 21 | Eleusine eye_type | ok. The pooled search found nothing. |
| 22 | Eleusine sense_chemical | **error: missed measurement.** My search "finger millet Eleusine coracana salicylic acid OR methyl jasmonate seedlings response" returned first Ye, Zhang, Tian, Yang, Zhu and Yin 2025, "Effects of Methyl Jasmonate on Flavonoid Accumulation and Physiological Metabolism in Finger Millet (Eleusine coracana L.) Sprouts", Plants 14(14): 2201, 10.3390/plants14142201 (MDPI page opened). MeJA "significantly suppressed sprout elongation", raised flavonoids and phenolics, and raised PAL and C4H activity in living sprouts. That is an applied-elicitor response (10(d)). The same page also returned a finger millet foliar growth-regulator paper (phytojournal 2018, unread). |
| 23 | Stellaria diel | ok. My two searches returned floras and extension pages (NC State, Naturblick, Cretan flora), a Heteracia floral paper (biodiversity-science.net, opened: not Stellaria) and a Stellaria apetaly paper. No hour. The screened ACC-oxidase papers are rightly screened as leaf rhythms. |
| 24 | Stellaria eye_type | ok, a repeat of main's plant-1:4 (noted, not counted). The pooled search found nothing. |
| 25 | Symphyotrichum diel | ok. My two searches returned the sunflower circadian floral-development paper, circadian scent reviews and the Heteracia paper. None is on Symphyotrichum. |
| 26 | Symphyotrichum eye_type | ok. The pooled search found nothing. |

Search record errors: **3 of 26 (11.5%)**, lines 7, 8 and 22.

## Evidence record verdicts (12)

| Line | Record | Verdict |
|---|---|---|
| 1 | Leucaena leucocephala sense_chemical | ok. DOAJ page opened. The authors are Xu et al. as recorded. The abstract gives JA-Ile as causing the most significant changes and JA, MeJA and CGM as causing few. The page does not show 10.3390/molecules23020188, Molecules 23(2): 188, which matched only by title (PMC6017012 was returned). Grade m, partial. |
| 2 | Carica papaya sense_chemical | ok. UEM page opened: Zanotti, Dias, Barros, DaMatta and Oliveira 2014, 36(4): 435-442, 10.4025/actasciagron.v36i4.18057. The abstract gives "KNO3 was the most effective" and CEPA lowering germination. Partial. The conditions field ("16 h dark, 8 h light") is not in the abstract and was not checked. |
| 3 | Carica papaya diel | **error: not a measurement of flower opening.** SciELO page opened. The quoted Methods sentence is verbatim, but 7:30 a.m. is the hour chosen to sample the "anthesis" stage for stigma-receptivity assays. The paper does not observe or report when papaya flowers open, and Results speak only of "24 hours after floral opening". Under the owner's reading, plant diel is flower-opening or scent timing measured in the source. A protocol hour is not that, any more than a flower-clock table is (audit brief). Grade m cannot stand. |
| 4 | Fagus sylvatica sense_chemical | ok. JFS page opened: Kolářová, Bezděčková and Procházková 2010, 56(9): 389-396, 10.17221/32/2010-JFS. The abstract gives better germination speed and dormancy release after 4 weeks of chilling plus GA3 or ethephon, and the cold requirement "reduced by three weeks". The value omits that both treatments lowered germination capacity in chilled seeds (significant for ethephon), though nothing in it contradicts the abstract. Partial. |
| 5 | Fagus crenata sense_chemical | ok, requote (not counted). DOAJ page opened: Hagiwara and Shiojiri 2020, J Plant Interact 15(1): 50-53, 10.1080/17429145.2020.1742393. The clipping and bagging design and the value hold. The page reads "These results suggested that SIR in beech trees required air contact.", and the record's "suggest ... depends on" is not verbatim. |
| 6 | Eleusine coracana diel | ok. ISGPB page opened: Dodake and Dhonukshe 1998, 58(1): 107-112. The quote is verbatim. 24 strains of one species, grade m, partial. |
| 7 | Stellaria media sense_chemical | ok, requote (not counted). Keele eprints page opened: Lyne, The effects of inorganic nitrate solutions on dormant seeds (file LynePhD1985). The abstract's extracted text prints "10 M to 10 M", exponents lost, for four ruderal species including S. media. The record says openly that its quote rebuilds the OCR order and exponents, so the quote is not verbatim. 10^-2 to 10^-3 M is the likely reading, and the value stands. |
| 8 | Typha latifolia sense_chemical | ok, requote (not counted). Moorwissen PDF opened: Jansen 2021, Stichting Bargerveen, §2.4.9. The review gives Morinaga 1926b on T. latifolia: 0.01 N KNO3 59%, distilled water 1.5%, in darkness at 27 C, with no effect on filter paper. The value holds. The quote stops at "(reduced oxygen pressure)" inside a longer sentence. Grade m rests on a review's report of a primary measurement (fork below). |
| 9 | Morus nigra sense_chemical | ok. Isparta avesis page opened: Koyuncu 2005, Acta Biol Cracov Ser Bot 47(2): 23-26. The quote is verbatim, and 250 mg/l GA3 with 100 days of stratification gave 96%. Grade m, partial. |
| 10 | Morus sense_light_nonvisual | ok. GOP page opened: Güneş and Çekiç 2004, Asian J Chem 16(3): 1842-1848. The darkness sentence is verbatim. The mulberries are named by common name only (white, red, pendulous and black), so grade g at genus level is right. |
| 11 | Morus diel | ok. ISGPB page opened: Roy Chowdhuri, Sau, Ghosh and Saratchandra 2004, 64(2): 130-131. The quote is verbatim for "Morus sp." germplasm, so grade g. Anther dehiscence hours count as flower timing, as with Carex in audit 90. |
| 12 | Symphyotrichum lanceolatum sense_chemical | ok. MDPI page opened: Nešić et al. 2022, Plants 11(7): 969, 10.3390/plants11070969. The quote is verbatim. Grade m, partial. |

Evidence errors: **1 of 12 (8.3%)**, line 3. Requotes, not counted: lines 5, 7 and 8. Every abstract-only record (1, 2, 4 to 7, 9 to 12) carries "partial": true. Lines 3 and 8 read open full texts, so they rightly carry no flag.

## Counts

- Search records: 3 of 26, 11.5%.
- Evidence: 1 of 12, 8.3%.
- Unit: 4 of 38, 10.5%.

Pooled with the desk's audits 83 to 90, from audit 90's figures (search records 48 in 1026; 52 in 1090 with evidence):
- Search records: 51 in 1052, 4.8%.
- With evidence included: 56 in 1128, 5.0%.

Forks that would change the count:
- Line 8 (Carica light). Suwarno 1990's abstract reports no result, and main's sweep-43 already saw it. If the desk counts only titles whose result is shown, line 8 stands and search records are 2 of 26 (7.7%). The verdict is unchanged.
- Evidence line 8 (Typha). If grade m requires the measurement in the source itself rather than a review's summary, the line needs grade or source changed, and evidence becomes 2 of 12.
- Line 7 (Pueraria). The MeJA work is a gene-expression study on seedlings. If the desk wants a whole-plant phenotype, the 2016 Frontiers paper should still have gone on the wanted list. I count the line once either way.

**Verdict: fail.** Search records fail at 11.5% and evidence at 8.3%. Both whole files were judged, so drop the error lines and the rest of the unit stands.

**Error lines to drop:**
- docs/views/searched/desk-d8.jsonl: lines 7, 8 and 22. They reopen Pueraria sense_chemical (Wang et al. 2019), Carica sense_light_nonvisual (Suwarno 1990 to the wanted list) and Eleusine sense_chemical (Ye et al. 2025).
- docs/views/evidence/desk-d8.jsonl: line 3 (Carica papaya diel), which leaves Carica diel open.

## Wanted lines (listed, not counted)

- Line 1 (10.1271/bbb.66.51, Leucaena leaf-closing substance, 2002). My title search did not return its page, so it is unchecked. The authors field is empty.
- Line 2 (Richardson-Calfee et al. 2001, 10.24266/0738-2898-19.4.171). Not checked. Main already holds Fagus sense_light_nonvisual evidence (harvest-13:1, 2), so this line serves a closed cell.
- Line 3 (10.1080/1343943x.2020.1758171). The title matches the tandf.figshare record my search returned, and the Kyoto repository page I opened showed no metadata, so authors and DOI are unchecked. Its `for` field says Eleusine indica, but the work is on finger millet, E. coracana.

## Leads

- Pueraria lobata sense_chemical: Wang et al. 2019 (Front Plant Sci 10: 28, MeJA on seedlings), and 10.3389/fpls.2016.00793 (unread).
- Eleusine coracana sense_chemical: Ye et al. 2025 (Plants 14: 2201, 10.3390/plants14142201).
- Carica papaya sense_light_nonvisual: Suwarno 1990 (Buletin Agronomi XV(3), light against dark; full PDF in the IPB repository).
- Neustanthus phaseoloides sense_chemical: de Morais et al. 2014 (GA3), as the unit says.

## Blocked pages

- frontiersin.org epub for 10.3389/fpls.2016.00793 returned binary data.
- repository.kulib.kyoto-u.ac.jp handle 2433/259441 showed only the repository's home metadata.
- No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text was committed.
