# Audit 115: desk-d25 (branch origin/research/desk-d25, head 0ea12d28)

## Lines judged

No sample was drawn. The launch prompt asks for the whole unit, so error lines can simply be dropped.
- Search records: all 6 lines of docs/views/searched/desk-d25.jsonl.
- Evidence records: all 4 lines of docs/views/evidence/desk-d25.jsonl.
- Wanted lines: all 5, listed and not counted.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on copies of the searched (6 lines) and wanted (5 lines) files prints "0 problems". All 4 evidence lines parse; quote lengths 114, 75, 105 and 45 characters.

## Method

Judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e)), audit 39's counting rule, the shared brief's rulings (audits 84, 86 to 90, 98 on `chased`), with audits 98 and 114 as format. About 44 WebSearches: 22 for the null records (germination light/dark, GA3/KNO3/smoke, jasmonate and herbivore volatiles, anthesis and flower-opening hours, shade and photoperiod trials), 1 labelled family search, 8 for evidence sources and names (POWO), 4 for wanted lines, the rest following leads. Only URLs my searches returned were fetched. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened (an ezproxyberklee.flo.org mirror in one result list was left alone), and no paper text is committed. origin/main at 6c41e6ba.

Queries. `harvest_get.py` ran offline. Chelidonium (harvest run 2) prints three queries ("Chelidonium phytochrome photoreceptor", "Chelidonium light perception", "Chelidonium phototropism") and the family review "Papaveraceae photoreceptor review"; line 1 lists all four word for word and in order, then its "web: " lines. Erodium, Tanacetum and Leucanthemum are in no harvest run, and lines 2 to 6 list "web: " lines only. No unlabelled line appears.

Chased.
- Line 1 names 10.1614/WS-D-15-00127.1, which the Chelidonium harvest prints as a citation step (0 hits). Supported.
- Lines 2 to 6 use the "none:" form with a reason, accepted as in audits 96 and 98. Fault, not counted: line 3 (Erodium sense_chemical) says "no Geraniaceae family review found by the web search above", but the Geraniaceae search is not among its own `queries` (it is in lines 2 and 4). My run of that search returned the Pakistan seed atlas (Ather et al. 2012, Pak J Bot 44(3): 1059-1064, seed morphology only) and Arabidopsis phytochrome work, no family review, so the reason holds in substance.

Bellis. Confirmed: its harvest prints "None hits (error gave up)" for all three queries and both citation steps, so point 6 holds it back.

Main. No evidence on main for any genus of the unit except Silene gallica (harvest-15:4, another species and trait). None of the four evidence DOIs is in any evidence or searched file on main. Kawano et al. 2020 is on main's wanted list (harvest-c13:38, which gives the year as 2019; AGRIS prints 2020), and line 4 now logs it. The nulls repeat older nulls on main (Chelidonium harvest-13:4 and sweep-7:8; Erodium sweep-6:28; Tanacetum sweep-6:32; Leucanthemum sweep-8:39), noted and not counted. No null contradicts a lead or evidence on main: the Chelidonium diel lead (harvest-c13:14, Denisow) is diel, not the trait of line 1, and the Tanacetum and Leucanthemum leads on main (harvest-c13:15 to 20 and 39, harvest-c18:19) are sense_chemical or sense_light_nonvisual, not diel.

## Search record verdicts (6)

| Line | Record | Verdict |
|---|---|---|
| 1 | Chelidonium sense_light_nonvisual | ok. Queries and chased match. My four searches returned Ji et al. 2022 (stratification and gibberellin only, no light arm), Tome and Colombo 1995 (Phytochemistry 40(1): 37-39, AGRIS: daily alkaloid variation put down "probably" to light and temperature together, with no light treatment), Krizhanovska et al. 2021 (wild against cultivated plants), a callus culture paper (light held constant) and seed-shop pages. No light/dark, shade or photoperiod trial. The three screened works I checked (nph.15229 Eschscholzia, plants9080927 Papaver, s40538-024-00698-3 Althaea) hold no Chelidonium measurement. |
| 2 | Erodium sense_light_nonvisual | **error: missed measurement.** My search "Erodium cicutarium photoperiod OR shading OR light intensity growth flowering experiment" returned the Dryad record 10.5061/dryad.gd3qh (Heger 2017, "Light availability experienced in the field affects ability of following generations to respond to shading in an annual grassland plant"; page opened). Its abstract describes maternal families of E. cicutarium grown in the glasshouse under no shade, homogeneous shade and heterogeneous shade (single and double light filters with gaps). Heterogeneous shade gave longer leaves, greater height, higher SLA, later first flowering and fewer fruits. That is a growth trial under set light levels on a named species, which 10(d) puts under sense_light_nonvisual. The record's own query "web: redstem filaree OR storksbill Erodium shade OR light intensity OR photoperiod trial growth" aimed at exactly this. The paper itself was not identified (mediatum.ub.tum.de 1354881 was bot-blocked); the Dryad page names no article. |
| 3 | Erodium sense_chemical | ok. My searches (GA3/KNO3/smoke; jasmonate and herbivore volatiles; ethylene/ABA/MeJA) returned Young et al. 1975 (sulfuric acid scarification only), Diyanat and Hosseini 2016 (Iranian Seed Research 3(1): 159-168, temperature only, the yujs page the record opened), the Çatav et al. 2024 smoke paper (Ann Bot Fenn 61: 31-40, abstract names no Erodium), and canola, tomato and potato hormone papers. Unchecked: 10.1007/s003440000026 (permission request not answered) and PMC9463459 (bot check), both from the jasmonate search with no Erodium in the title shown. Fault, not counted: the chased wording above. |
| 4 | Erodium diel | ok. My anthesis searches returned floras (wildflowersearch, PNW Flowers, Cretan flora, UCI pages), Fung and Thomson 2017 (flower longevity in unnamed subalpine species) and a Systematic Botany pollen-ovule paper on Erodium breeding systems (not flower timing). A Plant Ecology 2026 paper (s11258-026-01631-4) failed at its site and is unread. No opening hour. |
| 5 | Tanacetum diel | ok. My searches returned Eilers et al. 2021 (tansy scent with flower age, no time of day), Dobos et al. 1992 (Acta Hort 306: harvest timing by development phase), circadian scent papers on other genera and the sunflower circadian papers. No opening hour or diel scent measurement for a Tanacetum species. |
| 6 | Leucanthemum diel | ok. My searches returned flora and nursery pages (Wikipedia, RHS, NCSU, agroatlas), chrysanthemum plant patents, Stenc et al. 2025 (pollen presentation in Succisa, Centaurea, Trifolium) and "Rush hours in flower visitors over a day-night cycle" (visitor timing, not flower opening). A Hohenheim supplement came back as binary and is unread. No opening hour. |

## Evidence verdicts (4)

| Line | Record | Verdict |
|---|---|---|
| 1 | Chelidonium asiaticum sense_chemical (Ji et al. 2022, Korean J Plant Resour 35(6): 796-804, 10.7732/kjpr.2022.35.6.796) | **ok.** KoreaScience page (opened): ten authors in order, year, volume, issue, pages and DOI match; the quote is a whole abstract sentence word for word (GA subscripts in markup only). Applied gibberellin on living seed, 10(d). POWO 910403-1 (opened): "This species is accepted" for Chelidonium asiaticum (H.Hara) Krahulc.; the page listed no synonyms, so the identity with C. majus subsp. asiaticum rests on the record and the paper's title. Wording, not counted: "dormant seed germination improved ... after dormancy break" in `value` is self-contradictory; the paper says GA after dormancy break replaced cold stratification. |
| 2 | Silene latifolia diel (Dötterl, Wolfe and Jürgens 2005, Phytochemistry 66(2): 203-213, 10.1016/j.phytochem.2004.12.002) | **ok.** Bayreuth eref page (opened): citation matches; the quote is in the abstract; 98 plants of 15 European and 19 North American populations, dynamic headspace with Micro-SPE and GC-MS. Night-only scent emission is a scent-timing measurement under the diel reading. Main holds no Silene latifolia evidence; sweep-1:43 only names this paper in a search note. The POWO page for S. latifolia was not opened (Silene is an accepted genus; any synonymy stays inside it). |
| 3 | Maianthemum dilatatum sense_light_nonvisual (Shin et al. 2022, Horticulturae 8(11): 1057, 10.3390/horticulturae8111057) | **ok.** MDPI page (opened): five authors in order, citation and DOI match; quote verbatim and a whole sentence; seeds from the Nari Basin, Ulleungdo. Light against dark trial on living seed, 10(e). POWO 149429-2 (opened): "This species is accepted." Wording to fix, not counted: `value` says "the abstract adds that they germinated only in darkness, not under light", but the abstract's preceding sentence reads only "they germinated under dark conditions" with no "only"; the near-zero germination under light is in the article body. |
| 4 | Maianthemum dilatatum sense_light_nonvisual (Kawano et al. 2020, Plant Species Biol 35(1): 38-48, 10.1111/1442-1984.12258) | **ok.** AGRIS record (opened): authors, year, volume, pages and DOI match; "The seeds germinated well in dark conditions." is verbatim; montane to subalpine Japanese seed. The note rightly says no direct light comparison is in the abstract. A second source for the same cell as line 3, not a repeat of main. |

## Wanted lines (5, faults listed, not counted)

| Line | Work | Check |
|---|---|---|
| 1 | Hadi, Souri and Omidbeigi (jhs.um.ac.ir/article_29003) | Title and authors match the page (opened); the page gives no journal, year or DOI, as the line says. GA3 100 and 350 ppm giving 100% germination of C. majus confirmed. **Faults:** `for` names Tanacetum parthenium, but the paper's species is T. cinerariifolium (cinerariaefolium); and the `why` says GA3 trials on Tanacetum, but the abstract gives only cold stratification (control, 2, 3, 4 weeks) for Tanacetum. |
| 2 | Xiong et al. 2018 (10.1017/wet.2018.46) | Authors in order, Weed Technol 32(5): 564-569 and DOI match on BioOne (opened); GA3 and KNO3 "had no effect on breaking seed dormancy", scarification 92% to 98%. ok. |
| 3 | Özkil and Üremiş 2019 (10.16955/bitkorb.576677) | Authors, Bitki Koruma Bülteni 59(4): 3-10 and DOI match on openaccess.mku.edu.tr (opened); GA3 at 250 to 2000 ppm listed, result not stated. ok. |
| 4 | Stahler 1948 | AGRIS (opened): author, J Am Soc Agron 40(6): 490-502, no DOI; light named the prime competitive factor under ample moisture and nutrients. ok. |
| 5 | Shin et al. 2022 GA3 (10.3390/horticulturae8111057) | Citation as line 3 of the evidence; the abstract says GA3 treatments made no significant difference to germination rate, start date or mean germination time. ok. |

## Counts

- Search records: 1 of 6, 16.7% (line 2).
- Evidence: 0 of 4.
- Unit: 1 of 10, 10%.

Pooled with audits 83 to 90 onward, from audit 114's figures (search records 48 in 1026; with evidence 55 in 1108):
- Search records: 49 in 1032, 4.75%.
- With evidence included: 56 in 1118, 5.01%.

**Verdict: fail** (search records 1 of 6, above 5%). Search lines 1 and 3 to 6 and all four evidence lines stand and can merge.

**Error lines to drop:**
- docs/views/searched/desk-d25.jsonl: line 2 (Erodium sense_light_nonvisual; missed the E. cicutarium shade trial, Dryad 10.5061/dryad.gd3qh, Heger 2017).

Follow-ups:
- Erodium sense_light_nonvisual: find the article behind dryad.gd3qh (Heger, E. cicutarium shading; mediatum.ub.tum.de 1354881 was bot-blocked) and log it or put it on the wanted list.
- Wanted line 1: change `for` from Tanacetum parthenium to Tanacetum cinerariifolium and say the Tanacetum arm is stratification only.
- Evidence line 3: move "germinated only in darkness, not under light" from "the abstract adds" to the article body, or drop it.
- Search line 3: add the Geraniaceae family search to its `queries` or reword its `chased`.
- Main's harvest-c13:38 gives Kawano et al. the year 2019; AGRIS prints 2020.

## Blocked pages and unread leads

- link.springer.com 10.1007/s003440000026 (permission request not answered); PMC9463459 (reCAPTCHA); mediatum.ub.tum.de 1354881 (Anubis bot block); plantarum.izbis.bg.ac.rs 386, omorika 677 and enauka 169919 ("Seed germination of five weed species under different temperatures and light conditions", verification gates, species list unread); link.springer.com s11258-026-01631-4 (site error); d.lib.msu.edu etd 41956 (access limited); a Hohenheim supplement (binary).
