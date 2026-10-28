# Audit 101: desk-d11 (13 plant genera; branch origin/research/desk-d11, head 0856e44f)

## Lines judged

No sample was drawn. The launch prompt asks for the whole unit, so that error lines can simply be dropped.
- Search records: all 14 lines of docs/views/searched/desk-d11.jsonl (1 to 14).
- Evidence records: all 11 lines of docs/views/evidence/desk-d11.jsonl (1 to 11).
- Wanted lines: all 3, listed and not counted.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on copies of the searched file (14 lines) and the wanted file (3 lines) prints "0 problems".

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e)), the counting rule of audit 39, and the rulings of audits 84, 86 to 90 and 99, with audit 99 as the format. I ran about 44 WebSearches:
- about 26 for the 14 null records;
- 4 for evidence sources (the rest were checked on pages my null-record searches had returned);
- 3 for synonymy (POWO);
- 2 for the web-only family reviews;
- 3 for wanted lines and 2 for the "held" leads.

I fetched only URLs my own searches returned. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened. An onlinelibrary-wiley-com-443.webvpn.zafu.edu.cn result (Porceddu et al. 2017) was left alone; its iris.unica.it record was used instead. No paper text is committed.

Queries. `harvest_get.py` ran without the network (it reads origin/ci). A script compared each record's unprefixed `queries` with every `query` and `family review` line the harvest prints. All 14 match word for word and in order, with the "web: " lines after them. No harvest shows "gave up". Zizia, Chenopodium, Aquilegia, Carya, Malvaviscus, Ricinus, Iris and Pyrus are in no harvest run, and their records list "web: " lines only.

Chased.
- Ptelea (9), Conopholis (10, 11), Tropaeolum (12), Chasmanthium (13) and Paulownia (14) name exactly citation-step DOIs their harvest prints.
- The eight web-only records (1 to 8) name 10.1007/s00239-004-0294-2 (Lariguet and Dunand, doc.rero.ch 309979). My "Malvaceae photoreceptor review" and "Ranunculaceae photoreceptor review" searches both returned doc.rero.ch/record/309979 on the first page, so it is supported for Malvaviscus and Aquilegia (audits 86, 87, 99). Apiaceae, Amaranthaceae and Juglandaceae were not searched separately; the same general review is accepted for them as in audit 99.

Screened. Every screened DOI is printed in its genus's harvest output. W2588437677 (line 14) is not printed by harvest_get but no screened reason is wrong for its trait.

Main (origin/main ea4577e0, docs/views/evidence, searched, wanted and gaps/cells.jsonl). No unit evidence line repeats or contradicts evidence on main. Paulownia tomentosa sense_light_nonvisual is on main (sweep-28) from the same Grubisic et al. 1988 paper that evidence line 9 logs under sense_chemical; that is a second trait, not a repeat. Every unit cell is open in cells.jsonl. Main holds a 27 October eye_type search record for all 13 genera, so skipping eye_type is right.

**Main's wanted list.** docs/views/wanted/harvest-c11.jsonl reached main at 09e53ab3 and a7b0ef6a (27 Oct, before the unit's base ea4577e0). It holds a pending lead for nine of the unit's 14 null cells (Aquilegia chemical and light, Malvaviscus diel, Ptelea light, Conopholis diel and light, Tropaeolum diel, Chasmanthium chemical, Paulownia diel). Under desk-screen point 3 a cell with such a lead stays out of the search record. I count the lines where the lead is a measurement I confirmed, or a title naming the trait's subject for a species of the genus; the weaker leads are noted and not counted.

Genus status (POWO pages returned by my searches): Malvaviscus (30041958-2), Pyrus betulifolia Bunge (730718-1) and Carya illinoinensis (Wangenh.) K.Koch (442167-1) are returned under their own names. The other genera (Zizia, Ptelea, Iris, Ricinus, Conopholis, Tropaeolum, Chasmanthium, Paulownia, Chenopodium, Aquilegia) and species (Ricinus communis, Chenopodium album, Aquilegia vulgaris, Tropaeolum majus, Paulownia tomentosa, Iris pseudacorus) were not checked page by page; each is the type or a long-standing species of its own accepted genus. No line is filed under a synonym's genus. Iris on main also carries the mantid Iris oratoria, a cross-kingdom homonym, which does not touch the plant records.

## Search record verdicts (14)

| Line | Record | Verdict |
|---|---|---|
| 1 | Zizia sense_light_nonvisual | ok. My two germination searches returned nursery, seed-company and NANPS pages, a South Dakota native-plant note and a Holloway GA note that does not list Zizia. No light-against-dark trial. |
| 2 | Chenopodium diel | ok. My three searches returned Rodriguez de la Cruz et al. 2012 (Turk J Bot 36(4): 336-343, opened: an intradiurnal pattern for Chenopodiaceae-Amaranthaceae pollen type, no species named), the CATIE "Biologia floral de la quinua" record (opened: no hour), and a Setaria anther-timing paper. A family pollen type is not a named species, so nothing is missed. |
| 3 | Aquilegia sense_chemical | **error: missed measurement.** Porceddu, Mattana, Pritchard and Bacchetta 2017, "Dissecting seed dormancy and germination in Aquilegia barbaricina, through thermal kinetics of embryo growth", Plant Biol 19(6): 983-993, 10.1111/plb.12610 (iris.unica.it 11584/222396 opened): W+C stratification and GA3 "both promoted rapid embryo growth and radicle emergence", with thermal times four- to six-fold longer under GA3. That is an applied-hormone germination response (10(d), 10(e)). My first germination search also returned Holloway 2011 (Georgeson Botanical Note 43, UAF PDF opened), whose table lists Aquilegia canadensis, vulgaris, formosa and jonesii under "replaces or shortens afterripening" with GA. Main's harvest-c11 wanted list also holds 10.1002/ajb2.1846 (A. coerulea floral volatiles under water treatments) for this cell. |
| 4 | Aquilegia sense_light_nonvisual | **error: missed measurement.** My photoperiod search returned the AGRIS record (opened) of Zhang, White and Beattie 1991, "Regulation of flowering in Aquilegia", JASHS: plants given 18 h of supplemental HPS light flowered earlier and bore more flowers than plants under natural daylight. That is a growth trial under set light (10(d)). The same search returned Ballerini and Kramer 2011 (EvoDevo, 10.1186/2041-9139-2-4), which main's harvest-c11 wanted list holds for this cell as a measured photoperiod comparison in A. formosa. An MSU Aquilegia 'Winky' photoperiod PDF was bot-blocked. |
| 5 | Carya diel | ok. My two searches returned Zhang et al. 2015 (Acta Hortic 1070: 4, ISHS opened: stigma receptivity in days, no hour), Yates et al. 1991 (JASHS 116(3): 430, opened: catkins collected "between 12:00 PM and 3:00 PM", a protocol hour, not a measurement; audit 99 Carica), the USDA flowering note and aerobiology pages without Carya hours. |
| 6 | Malvaviscus diel | **error: lead on main left out.** My searches found no opening hour (Siquera et al. 2021 on M. penduliflorus, opened: "antese diurna" quoted from the ornithophily syndrome, observations 9h to 10h30 only; a Pachira paper). But main's harvest-c11 wanted holds "Hummingbird pollination of Malvaviscus arboreus in Costa Rica" (1984, 10.1080/0028825X.1984.10425293) for this cell, with a flower form and anthesis section. Point 3 keeps the trait out of the record while that lead is unread. Fork below. |
| 7 | Malvaviscus sense_chemical | ok. My two searches returned rooting-of-cuttings papers (excluded under the cut-branch rule, audit 87) and germination pages on other genera. |
| 8 | Malvaviscus sense_light_nonvisual | ok. Same two searches; no light trial for a Malvaviscus species. |
| 9 | Ptelea sense_light_nonvisual | ok. My two searches returned the ASHS 2018 abstract the record opened (cold only), Yale ELTI and extension pages, and the COSEWIC biology chapter (opened: "Seedlings develop in full sun to partial shade", "Increasing shade appears to suppress flowering", qualitative, no trial). Main's wanted 10.21273/hortsci14693-19 is the 2020 paper of the same cold-stratification study, not a light trial. |
| 10 | Conopholis diel | ok, weak. My two searches returned wildflower, FNA and USA-NPN pages with a flowering season only. The harvest prints Conopholis alpina floral-variation work (thesis 10.24275/uami.0p096709k; AJB 10.1002/ajb2.16001, 16405) that main's harvest-c11 wanted holds for diel as "plausible", with no hour shown; I do not count it. |
| 11 | Conopholis sense_light_nonvisual | ok. My germination-stimulant search returned only strigolactone chemistry on other parasites. Main's wanted 10.1007/s10722-016-0427-7 (204 Mexican species) is not shown to include Conopholis. |
| 12 | Tropaeolum diel | **error: missed measurement, and on main's wanted list.** Silva, Mussury, Vieira, Alves Junior, Pereira and Scalon 2011, "Floral biology of Tropaeolum majus L. ... Astylus variegatus", An Acad Bras Cienc 83(4): 1251-1258 (redalyc and SciELO opened): "the anthesis is diurnal and the flower duration is six days, on average." Main already logs that kind of value as diel (Centrosema pubescens: "anthesis is diurnal ... no hour given"). The work is printed twice in the Tropaeolum harvest output (10.1590/s0001-37652011005000046), was the first hit of my search, and is on main's harvest-c11 wanted list for this cell. |
| 13 | Chasmanthium sense_chemical | **error: missed measurement in the harvest output.** The Chasmanthium harvest prints "Hormonal Effects on the Germination Response of Chasmanthium latifolium" (1995, HortScience, 10.21273/hortsci.30.4.836d) four times. Main's harvest-c11 wanted describes it as nitrate, GA3 and kinetin applied to living caryopses with germination compared, an applied-chemical response (10(d), 10(e)). The record screens one Hedychium paper and names neither this work nor a wanted line. |
| 14 | Paulownia diel | **error: candidate in the harvest output left out.** The Paulownia harvest prints "Biology of Flowering Paulownia tomentosa in the conditions of the Sirdaryo Region" (2026, IJCMAS, 10.20546/ijcmas.2026.1504.025, diamond OA). That is a flowering-biology study of the species, which main's harvest-c11 wanted holds for this cell to check for anthesis timing. The record screens six other works and leaves this one out. My search for it returned only Vaidya, Bajaj and Joshee 2017 on P. elongata (opened: no timing), so the paper itself was not read. Fork below. |

Search record errors: **6 of 14 (42.9%)**, lines 3, 4, 6, 12, 13 and 14. Four of them (3, 4, 12, 13) rest on a measurement I confirmed or that main's wanted line describes; two (6, 14) rest on unread leads of the flowering-biology kind.

## Evidence record verdicts (11)

| Line | Record | Verdict |
|---|---|---|
| 1 | Ricinus communis sense_chemical | ok. UNESP page opened: De Sibio and Rossi 2016, J Econ Entomol 109(4): 1612-1618, 10.1093/jee/tow115. The quote is verbatim and a whole sentence. Herbivore-induced response (10(a)). Partial. |
| 2 | Ricinus communis diel | ok, requote (not counted). NYSM page opened: Ogden and Hayes 1969, Am J Bot 56: 16-21. The Ricinus words are the final clause of a sentence that begins "Zea emits pollen fairly uniformly", as the unit flagged, so the quote is a clause. The value holds. Ricinus is monotypic, so "Ricinus pollen" is R. communis and grade m stands. Pollen emission hours count as flower timing (audit 99, Morus). Partial. |
| 3 | Chenopodium album sense_chemical | ok. Canberra research-profile page opened: Saini, Bassi and Spencer 1986, Weed Sci 34(4): 502-506, 10.1017/S004317450006731X. The quote is verbatim. The page says ethylene overcame "the dormancy of over 70% of the seed"; the record's "over 70% of dormant seed germinated" is a close paraphrase. Partial. |
| 4 | Aquilegia vulgaris diel | ok. Acta Agrobotanica PDF opened: Denisow and Anton, 65(1): 37-44, 2012. The quote is verbatim, and the Results give pollen release from about 5.00 with about 5% of anthers dehiscing per hour. The PDF prints no DOI, and my search for 10.5586/aa.2012.041 returned nothing, so the DOI is unchecked (listed, not counted). Open full text, so no partial flag is right. |
| 5 | Carya illinoinensis sense_chemical | ok, requote (not counted). BioOne page opened: Chen, Ni, Cottrell, Wood and Buntin 2009, J Econ Entomol 102(3). The quoted words are part of a longer sentence, as the unit flagged. Peroxidase rose only in susceptible genotypes and LOX3 was more often induced in resistant ones, as the value says. Partial. |
| 6 | Pyrus sense_chemical | ok. WUR page opened: Scutareanu, Drukker, Bruin, Posthumus and Sabelis 1997, J Chem Ecol 23(10): 2241-2260, 10.1023/b:joec.0000006671.53045.16. The quote is verbatim. The abstract says only "pear" and names no species or cultivar, so grade g at genus level is right, as the unit says. Herbivore-induced volatiles of living trees (10(a)). Partial. |
| 7 | Pyrus betulifolia diel | ok. ISHS page opened: Farkas and Orosz-Kovacs 2004, Acta Hortic 636: 317-324, 10.17660/ActaHortic.2004.636.38. The quote is verbatim, and P. betulifolia is the species. Nectar and anther-dehiscence hours count as flower timing (audit 99). Partial. |
| 8 | Tropaeolum majus sense_chemical | ok. AGRIS page opened: Bloem et al. 2014, Ind Crops Prod 60: 349-359, 10.1016/j.indcrop.2014.06.040. The quote is verbatim, on living greenhouse plants (10(d)). Partial. |
| 9 | Paulownia tomentosa sense_chemical | ok, requote (not counted). AGRIS page opened: Grubisic, Konjevic and Neskovic 1988, Physiol Plant 72(3): 525-528, 10.1111/j.1399-3054.1988.tb09160.x. The sentence continues past "(FC)" with ", which does not reverse the inhibition caused by FR or growth retardants", so the quote stops inside it. The value holds. Partial. |
| 10 | Iris pseudacorus sense_light_nonvisual | ok. idUS page opened: the quote is verbatim apart from the hyphen form. Gillard et al. 2022 (citation not printed by the fetch; unchecked). Germination light against dark (10(e)). Partial. |
| 11 | Tropaeolum majus sense_light_nonvisual | ok. DOAJ page opened: Munir, Alhajhoj, Khakwani and Baloch 2015, Songklanakarin J Sci Technol 37(3): 247-254. The quote is verbatim, and 57 days at 17 h and 83 days at 8 h are on the page. No DOI is shown. Partial. |

Evidence errors: **0 of 11 (0%)**. Requotes, not counted: lines 2, 5 and 9 (the three clauses the unit itself flagged, Paulownia included). Every abstract-only record (1 to 3, 5 to 11) carries "partial": true. Line 4 read an open full text and rightly carries no flag.

## Counts

- Search records: 6 of 14, 42.9%.
- Evidence: 0 of 11, 0%.
- Unit: 6 of 25, 24.0%.

Pooled with the desk's audits 83 to 90 (audit 90's figures, as audits 91 to 99 used them: search records 48 in 1026; 52 in 1090 with evidence):
- Search records: 54 in 1040, 5.2%.
- With evidence included: 58 in 1115, 5.2%.

Forks that would change the count:
- Lines 6 (Malvaviscus diel) and 14 (Paulownia diel) rest on unread leads, one on main's wanted list and one in the unit's own harvest. If the desk counts only leads whose result is shown, search records are 4 of 14 (28.6%) and the unit 4 of 25 (16.0%). The verdict is unchanged.
- Line 12 (Tropaeolum diel). If a diel value must carry an hour, Silva et al. 2011 is a lead, not a measurement; the line still fails point 3, since main's wanted list holds it for the cell.
- Line 3 (Aquilegia chemical). Holloway 2011 is a compilation table; the count rests on Porceddu et al. 2017 alone.

**Verdict: fail.** Search records fail at 42.9% (28.6% on the narrow reading). The evidence file passes. Both whole files were judged, so drop the error lines and the rest of the unit stands.

**Error lines to drop:**
- docs/views/searched/desk-d11.jsonl: lines 3, 4, 6, 12, 13 and 14. They reopen Aquilegia sense_chemical (Porceddu et al. 2017, GA3), Aquilegia sense_light_nonvisual (Zhang, White and Beattie 1991; Ballerini and Kramer 2011), Malvaviscus diel (1984 Costa Rica pollination paper), Tropaeolum diel (Silva et al. 2011), Chasmanthium sense_chemical (HortScience 1995 hormonal germination) and Paulownia diel (IJCMAS 2026 flowering biology).
- docs/views/evidence/desk-d11.jsonl: none. Lines 2, 5 and 9 should be requoted to whole sentences, which changes no value.

## Wanted lines (listed, not counted)

- Line 1 (10.21273/jashs05119-21, "Floral Aromatics of Ptelea", 2021). DOAJ page opened: JASHS, December 2021, title matches; the page shows no authors or DOI, so the DOI is unchecked. The authors field is empty, as the rule allows. The abstract does not say whether the flowers were on living trees.
- Line 2 (10.1093/aesa/saac012, "Insect Floral Visitors of Ptelea trifoliata (Rutaceae) in Iowa", 2022). The BioOne URL my search returned carries the DOI and volume 115, issue 5; the PMC copy (PMC9467031) was not answered. Authors unchecked.
- Line 3 (10.3897/phytokeys.275.192014). Pensoft page opened: Piwowarczyk et al. 2026, PhytoKeys 275: 209-297, DOI confirmed. It names Conopholis only for its visitors (Hymenoptera 41.4%, and others) and reports no scent or chemical cue for it, so the line is unlikely to settle Conopholis sense_chemical.

## Held leads (no record written)

- Ptelea diel and chemical: real; wanted lines 1 and 2 exist.
- Conopholis chemical: the only named lead (wanted 3) holds nothing on Conopholis chemistry. Holding the cell costs nothing, but the lead is empty.
- Ricinus light: real. Bulletin of the Faculty of Science, University of Alexandria 1993, 33[A]: 56-70 (BVS record). My search also returned a Torrey Bot Soc paper on Ricinus germination after autochorous dispersal (10.3159/08-RA-092R.1).
- Carya light: real. Lombardini et al. 2009 press releases ("Sun or shade: pecan leaves' photosynthetic light response evaluated") and an AGRIS record were returned.
- Iris chemical: real. Holloway 2011 (Note 43) lists Iris setosa as germinating more completely with GA after scarification or stratification.
- Eye_type: main holds a 27 October search record for all 13 genera, so skipping it is right.

## Blocked pages

- canr.msu.edu Aquilegia 'Winky' PDF: bot check.
- link.springer.com redirect for 10.1186/s12870-023-04357-x: not in provenance, not retried.
- pmc.ncbi.nlm.nih.gov PMC9467031: permission not answered, not retried.
- sora.unm.edu Auk 97(4): 790 PDF: redirect to digitalcommons, not followed.
- No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text was committed.
