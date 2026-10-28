# Audit 102: desk-d12 (9 plant genera; branch origin/research/desk-d12, head 0061877e)

## Lines judged

No sample was drawn. The launch prompt asks for the whole unit, so error lines can simply be dropped.
- Search records: all 8 lines of docs/views/searched/desk-d12.jsonl (1 to 8).
- Evidence records: all 10 lines of docs/views/evidence/desk-d12.jsonl (1 to 10).
- Wanted lines: the 1 line, listed and not counted.
- The unit's holds (Hypochaeris sense_chemical, Packera sense_light_nonvisual) and its skip (Foeniculum diel) are judged too. They write no line, so they are not counted.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on copies of the searched file (8 lines) and the wanted file (1 line) prints "0 problems".

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e)), the counting rule of audit 39, and the rulings of audits 84, 86 to 90 and 101. Audits 90 and 101 served as the format. I ran about 34 WebSearches:
- 17 for the 8 null records;
- 9 for evidence sources;
- 2 for the web-only family reviews;
- 1 for the wanted line;
- 4 for the holds.

I fetched only URLs my own searches returned. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened. Two results were left alone: an onlinelibrary-wiley-com-443.webvpn.zafu.edu.cn result and a springerlink.bibliotecabuap.elogim.com result. No paper text is committed.

Queries. `harvest_get.py` ran without the network (it reads origin/ci). Arundo (lines 1 and 2) is in harvest run 4. Its records list the 12 `query` lines and the `family review "Poaceae photoreceptor review"` line exactly as the harvest prints them, word for word and in order, with the "web: " lines after them. No step shows "gave up". Vinca, Lobelia and Packera are in no harvest run, and their records list "web: " lines only.

Chased.
- Lines 1 and 2 name 10.1016/j.tree.2009.09.010. That is the Arundo citation step the harvest prints ("works citing 10.1016/j.tree.2009.09.010 that name Arundo: 0").
- Lines 3 to 8 name 10.1007/s00239-004-0294-2 (Lariguet and Dunand, doc.rero.ch 309979). My searches "Apocynaceae photoreceptor review" and "Campanulaceae photoreceptor review" both returned doc.rero.ch/record/309979 on the first page. Asteraceae was accepted for the same review in audit 88. The DOI is therefore supported for Vinca, Lobelia and Packera (audits 86, 87, 99, 101).

Screened. Lines 1 and 2 are the only records with `screened` entries. Every DOI in them is printed in the Arundo harvest output, and every reason is right for its trait.

Main (origin/main e564311a: docs/views/evidence, searched and wanted; gaps/cells.jsonl).
- No evidence line repeats or contradicts evidence on main. Main holds no Helianthus sense_chemical, no Helianthus tuberosus row, no Sorghum halepense row, no Vinca row and no Dioscorea chemical row.
- Dioscorea alata diel (line 7) sits beside main's genus-level sweep-39:5 ("male flowers open about noon"), and the two agree.
- Rowe et al. 2012 (line 1) and Krenchinski et al. 2015 (line 5) are on main's harvest-c11 wanted list (lines 45 and 52). Logging them settles those wanted lines.
- Lines 5, 7 and 8 repeat 27 October search records already on main, for the same genus and trait: harvest-c11 Lobelia diel, and desk-c11 Packera diel and sense_chemical (audit 88 passed all three). These repeats are noted and not counted. A repeated search record is not a repeat of evidence. Still, the unit skipped Foeniculum diel for exactly this reason and did not skip these three.
- **Main's wanted list holds harvest-c11:51 for the cells of lines 1 and 2.** That line is Janni et al. 2021, "Real-time monitoring of Arundo donax response to saline stress through the application of in vivo sensing technology", Sci Rep 11, 10.1038/s41598-021-97872-6, filed for sense_chemical and diel. Its own `why` says no diel oscillation is established. The chemical side is salinity, which main does not log under sense_chemical (audit 88), and ion uptake is outside the owner's reading. So the lead is weak for both traits. Under audit 101's rule (count only a confirmed measurement or a title naming the trait's subject) I note it and do not count it (fork below). The unit held Hypochaeris for a lead on that same wanted file, so leaving Arundo unheld is inconsistent.

Genus status. Arundo, Vinca, Lobelia, Packera, Helianthus, Sorghum and Dioscorea are accepted genera. Sorghum halepense, Helianthus tuberosus, Dioscorea alata, D. esculenta and Vinca minor are long-standing species of their own genera. I did not read POWO pages for them in this audit. No line is filed under a synonym's genus.

## Search record verdicts (8)

| Line | Record | Verdict |
|---|---|---|
| 1 | Arundo diel | ok. Queries and chased match. My searches ("Arundo donax anthesis time of day flowering pollen release hour"; Arundo plinii/formosana/micrantha floral biology) returned flora pages and Spencer and Ksander 2006 (Aquat Bot 85(4): 282-288, marineinfo opened: ramet emergence only). They also returned Arundo taxonomy and polyploid-fertility papers. No hour for any Arundo species. Main's harvest-c11:51 (Janni et al. 2021) is a weak diel lead, noted, not counted. |
| 2 | Arundo sense_chemical | ok, with forks. Queries and chased match. My germination-chemical search returned only smoke papers on other genera. My herbivore search returned Moore, Watts and Goolsby 2010, "Ecophysiological Responses of Giant Reed (Arundo donax) to Herbivory", Invasive Plant Sci Manag 3(4): 521-529, 10.1614/IPSM-D-10-00007.1 (AGRIS opened). There, a scale insect and a galling wasp reduced leaf photosynthesis and transpiration. I read that as injury to the leaf, not an induced or signalling response, so it is not counted (fork below). Main's sweep-25:23 already names "the herbivory paper" for this cell. Spencer and Ksander 2006 found that nitrate level did not affect ramet emergence; that is nutrient supply, outside the owner's reading. Janni et al. 2021 (harvest-c11:51) is salinity, not counted. |
| 3 | Vinca sense_light_nonvisual | ok, with a fork. Web-only; chased supported. My searches returned the bedding-vinca germination paper (Catharanthus roseus, which the unit rightly set aside), seed-shop pages and grapevine light work (Bertamini and Nedunchezhian 2004, bp.ueb.cas.cz opened: Vitis only). They also returned Molchan and Yurin 2019, "Effect of LED-lighting with various spectral composition on the growth and alkaloids biosynthesis in Vinca minor callus cultures", Exp Biol Biotechnol (journals.bsu.by 2508 opened): green-dominant LED light most stimulated dry-matter gain. That is callus in vitro, not a plant, and the unit's own Arundo note sets tissue culture aside. Not counted (fork below). |
| 4 | Vinca diel | ok. Web-only; chased supported. My floral-biology search returned photomacrography forum threads and papers on other genera. No opening hour or scent timing for a Vinca species. |
| 5 | Lobelia diel | ok; repeats harvest-c11 on main (noted). Web-only; chased supported. My searches returned plant-patent pages, a squash nectar thesis (core.ac.uk opened: Cucurbita) and Eisen, Case, Caruso and Dudash 2017, "Variation in Pollen-Dispensing Schedules of Lobelia siphilitica", Int J Plant Sci 178(1): 79-84, 10.1086/688961 (LMU page opened: no abstract shown). It is a lead whose schedule is probably across the days of the male phase, not hours, so it is not counted. A PSU record on staminate and pistillate phase durations is likewise in days. |
| 6 | Lobelia sense_chemical | ok. Web-only; chased supported. My searches returned Holloway 2011 (UAF Note 43, opened: no Lobelia in its GA table) and Zhou, Teixeira da Silva and Ma 2014 on smoke water and karrikin in 13 Chinese species (Cent Eur J Biol 9: 1108-1116, Springer opened: no Lobelia named). They also returned GA3 germination papers on Leymus and Trollius (both opened) and jasmonate papers on Nicotiana. No Lobelia chemical response. |
| 7 | Packera diel | ok; repeats desk-c11 on main (noted). Web-only; chased supported. My search returned sunflower circadian anthesis papers only. |
| 8 | Packera sense_chemical | ok; repeats desk-c11 on main (noted). Web-only; chased supported. My search returned Çatav et al. 2024 (no Packera) and an ASHS 2025 session (Maurer and Tippins, sched page opened): GA3, smoke water and stratification were tested on 20 native perennials, but no species is named. |

Search record errors: **0 of 8 (0%)**.

## Evidence record verdicts (10)

| Line | Record | Verdict |
|---|---|---|
| 1 | Helianthus annuus sense_chemical | ok. PMC3356381 opened: Rowe, Ro and Rieseberg 2012, 10.1371/journal.pone.0037191. The quote is verbatim. Whole potted plants were sprayed with 100 µM MeJA against an ethanol control, and trichome density did not change significantly at that dose, as the value says. Grade m; full text, so no partial flag is right. |
| 2 | Helianthus tuberosus sense_chemical | ok, requote (not counted). tci-thaijo page opened: Singphan 2022, Health Sci Sci Technol Rev 15(2): 111-117, no DOI. The quote is verbatim, but it is the total-soluble-solids sentence, which pools MeJA with yeast extract. The value's fructan result is in the next abstract sentence ("100 µM of Methyl jasmonate gave the highest Fructans ... content", p<0.05), as the record's note says. That sentence is the better quote. Partial. |
| 3 | Helianthus tuberosus sense_light_nonvisual | ok, with a fork. gau.ac.ir page opened: Ruttanaprasert et al. 2013, Int J Plant Prod 7(3): 393-416, 10.22069/ijpp.2013.1111. The quote is verbatim. Photoperiod varies through 13 planting dates and is confounded with growing degree days, which the record states. Partial. |
| 4 | Sorghum halepense diel | ok. tehqeeqat.org 8879 opened: Husain, Ahmed, Hussain and Nazim 2012, vol. 2(2), no journal name shown. The quote is verbatim. The page gives the start half an hour earlier in March to May and the end at 7:00 AM. Partial. |
| 5 | Sorghum halepense sense_light_nonvisual | ok. SciELO page opened: the quote is verbatim, as are the optima of 31.98 and 29.75 C and the "neutral photoblastic" conclusion. Authors, volume and DOI are not shown on that page; the UNESP and USP records my search returned carry the title. Partial. |
| 6 | Sorghum halepense sense_chemical | ok. ojs.srce.hr 4648 opened: Baličević, Ravlić and Balić 2016, J Cent Eur Agric 17(3), 10.5513/jcea.v17i3.4648. The quote is verbatim and control germination is 2.8%. KNO3 is confounded with acid scarification, as the record says. Partial. |
| 7 | Dioscorea alata diel | ok. Springer page opened (doi.org/10.1007/BF00028959): Abraham and Nair 1990, Euphytica 48: 45-51. The quote, the 4 to 5 hour and 9 to 11 day longevities and the 12.00 to 15.00 h pollination window are verbatim. Partial. |
| 8 | Dioscorea esculenta sense_light_nonvisual | ok. smujo.id 3840 opened: Lestari, Utami and Wawo 2019, Pros Sem Nas Masy Biodiv Indones 5(2): 374-382, 10.13057/psnmbi/m050241. The quote is verbatim, and the 0/25/55/75% shade levels and the "up to 50%" yield result are as recorded. Set-shade trial (10(d)). Partial. |
| 9 | Dioscorea sense_chemical | ok. Springer page opened (10.1023/A:1005816324097): Okagami, Tanno, Kawai et al. 1997, Plant Growth Regul 22: 137-140. The page prints "GA3 ... 1 micro;M" where the record has "GA(3) ... mu M", a typographic difference. Seed germination was not inhibited. No species is named, so grade g is right. The record's DOI field is empty, and this DOI can fill it. Partial. |
| 10 | Vinca minor sense_chemical | ok, with a fork. The Elsevier Pure page (Abouzeid et al. 2017, J Nat Prod 80(11): 2905-2909, 10.1021/acs.jnatprod.7b00424) and the TU Braunschweig dissertation record were both opened. The quote is verbatim. The dissertation abstract says "mature Vinca minor plants of defined physiological status" were treated and that the regulators were applied over nine days, which supports a living-plant response. Neither page says outright that the leaves stayed attached, as the record itself notes. Partial. |

Evidence errors: **0 of 10 (0%)**. Requote, not counted: line 2.

## Holds and skip

- Hypochaeris sense_chemical, held. The hold is right under point 3: main's harvest-c11:65 (Maruta et al. 1995, CuCl2-elicited stress compounds) is a pending lead for the cell, and no record was written. However, audit 88 (desk-c11 line 4) had already found Wala, Kołodziejek and Patykowski 2021, PLOS ONE 16(1): e0244737, which reports a nitrogen-compound germination response of H. radicata that is ready to log. It is still not on main's evidence. The unit could have closed the cell instead of holding it. My own search (Hypochaeris radicata germination GA/nitrate/jasmonate) returned only a Sonchus paper (redalyc opened).
- Packera sense_light_nonvisual, held. The hold is right: main's sweep-22:3 holds the Kansas light-level germination paper (10.1660/062.122.0311, Trans Kans Acad Sci 122(3-4)). My search also returned the matching FHSU thesis, de Queiroz 2019, "Influence of Shaded Conditions on Development of Asteraceae Species Native to Kansas" (scholars.fhsu.edu/theses/3132 opened). It tested germination of six native Asteraceae at 10%, 50% and 100% light, and shade reduced germination in every species, but the page does not name them. If Packera is among them, that settles the cell.
- Foeniculum diel, skipped. The skip is right: main holds desk-c11 line 1 (Foeniculum diel, 27 October), which audit 88 passed.

## Counts

- Search records: 0 of 8, 0%.
- Evidence: 0 of 10, 0%.
- Unit: 0 of 18, 0%.

Pooled with the desk's audits 83 to 90, using audit 90's figures as audit 101 did (search records 48 in 1026; 52 in 1090 with evidence):
- Search records: 48 in 1034, 4.6%.
- With evidence included: 52 in 1108, 4.7%.

Forks that would change the count:
- Line 2 (Arundo sense_chemical). If the desk reads herbivore-caused loss of photosynthesis (Moore et al. 2010) as a herbivore-induced response under 10(a), the line is a missed measurement. Search records would then be 1 of 8 (12.5%), the unit 1 of 18 (5.6%), and the search records would fail.
- Lines 1 and 2 (Arundo). If any lead on main's wanted list must keep a cell out of the record, as audit 101 counted for Malvaviscus, harvest-c11:51 makes both lines errors: 2 of 8 (25%).
- Line 3 (Vinca light). If an in vitro callus light response counts under sense_light_nonvisual, Molchan and Yurin 2019 is a missed measurement: 1 of 8.
- Line 3 of the evidence (H. tuberosus light). If natural photoperiod across planting dates is not a light trial, the line is an error: 1 of 10.

**Verdict: pass** on the reading used here: 0 errors in 18 records. Each of the three search-record forks would fail the search records, so the desk should rule on them, the Moore et al. 2010 fork first, before the Arundo cells are taken as settled.

**Error lines to drop:**
- docs/views/searched/desk-d12.jsonl: none. Lines 5, 7 and 8 repeat search records already on main and can be dropped as redundant.
- docs/views/evidence/desk-d12.jsonl: none. Line 2 should be requoted to the fructan sentence. Line 9 can take the DOI 10.1023/A:1005816324097.

## Wanted line (listed, not counted)

- Line 1 ("Response of Giant Reed (Arundo donax) to Intermittent Shading", 10.1614/IPSM-D-11-00087.1). The BioOne URL my search returned carries this DOI with volume 5, issue 3 of Invasive Plant Science and Management, and the title matches. The Cambridge abstract page redirected and then was refused (permission unanswered), so authors and year are unchecked. The authors field is empty, as the rule allows.

## Leads

- Arundo donax sense_chemical: Moore, Watts and Goolsby 2010 (10.1614/IPSM-D-10-00007.1), herbivory and photosynthesis; this lead depends on the desk's ruling.
- Vinca minor sense_light_nonvisual: Molchan and Yurin 2019, LED spectra on callus (journals.bsu.by 2508).
- Lobelia siphilitica diel: Eisen et al. 2017 (10.1086/688961), pollen-dispensing schedules, unread.
- Hypochaeris radicata sense_chemical: Wala et al. 2021 (PLOS ONE e0244737), ready to log since audit 88.
- Packera sense_light_nonvisual: the de Queiroz 2019 FHSU thesis behind the Kansas paper; the species list is unread.

## Blocked pages

- www.cambridge.org abstract for 10.1614/IPSM-D-11-00087.1: permission unanswered, not retried.
- doaj.org 7f202880fffe4c0ab9c35b2a02346e3d: title only, so the Springer page was used instead.
- No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text was committed.
