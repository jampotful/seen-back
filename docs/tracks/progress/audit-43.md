# Precision audit 43, 18 October 2026

Unit: harvest-30 (branch research/harvest-30, commit 45b2a346), a desk screening unit written under desk-screen.md: 37 search records for 12 genera (Heliotropium, Cistothorus, Botrypus, Monobia, Nekemias, Cocculus, Vipera, Asparagus, Riparia, Masticophis, Lerema, Pyrgus) and 26 wanted lines. It has no evidence records. The two files were read with `git show 45b2a346:<path>` and saved to /tmp/au43/. The audit worktree /tmp/wsau43 was cut from origin/main (965e2f01). No evidence, searched or wanted file, no src/ file and no views/*.json file was edited. No ResearchGate, academia.edu, Sci-Hub or LibGen page, library login or proxy was used, and no paper text is committed (papers are paraphrased).

**Result: 1 error in 20 sampled records, 5.0%. The rule asks for under 5%, so harvest-30 does not pass. Pooled with audits 40 to 42 the desk's rate is 10 in 77, 13.0%.**

## Mechanical gate (step 1)

`python3 -I tools/views/screen_candidates.py --check harvest-30.searched.jsonl --wanted harvest-30.wanted.jsonl` on the saved copies printed "0 problems" (run at the start and again before this report was written), so the unit passes step 1.

## Sample (step 2)

All 37 lines of the searched file, `random.seed(43)`, `random.sample(lines, 20)`. The draw used the line count only, and the sample was committed (bb7b9dac) before the first web search. Line numbers in draw order: 3, 19, 10, 30, 24, 7, 15, 20, 16, 34, 1, 17, 14, 36, 12, 28, 18, 25, 13, 6. Sorted: 1, 3, 6, 7, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 24, 25, 28, 30, 34, 36.

The 20 fall in 10 of the 12 genera (Cocculus and Masticophis have no sampled line): Heliotropium 1, 3; Nekemias 17, 18, 19, 20; Botrypus 10; Riparia 28, 30; Vipera 24; Cistothorus 6, 7; Monobia 12, 13, 14, 15, 16; Lerema 34; Pyrgus 36; Asparagus 25. Eight of the 20 are plant lines (1, 3, 10, 17, 18, 19, 20, 25). The 17 lines outside the sample (2, 4, 5, 8, 9, 11, 21, 22, 23, 26, 27, 29, 31, 32, 33, 35, 37) were checked for queries and `chased` only.

## Verdict per record

"Confirm" means that the queries, `chased` and `screened` hold and that no measurement of the trait in a species of the genus surfaced in the harvest data, my searches or the pages I opened. It does not mean that no text anywhere holds one.

| line | genus / trait | verdict | reason |
|---|---|---|---|
| 1 | Heliotropium / diel | **error** | Abid, Nayani, Riaz and Fatima 2023 give the opening hours of H. curassavicum flowers (see "The one error"); the queries, `chased` and the empty `screened` map are right |
| 3 | Heliotropium / sense_chemical | confirm | The one screened work, a glossary of botanical epithets, holds nothing, and three searches found H. curassavicum only as a donor of allelopathic compounds |
| 6 | Cistothorus / cff_hz | confirm | `chased` names methods#994 (Boström et al. 2016, passerines), which is not among the printed citation steps; both screened works (a bird census, Cocos flycatcher song) hold no flicker data, and no wren flicker value surfaced |
| 7 | Cistothorus / fov_h_deg | confirm | `chased` names recheck-15-fixed#2 (Agelaius phoeniceus); the tool listed no candidate, and four opened visual-field sources name no wren (Martin's 2007 table has 32 species, the starling its only passerine) |
| 10 | Botrypus / eye_type | confirm | The tool listed no candidate, and three ocelli searches returned plant-vision reviews (the 2023 Plants review names Arabidopsis roots and Boquila only) and a protist eye paper |
| 12 | Monobia / acuity_cpd | confirm | `chased` is the printed citation-step DOI 10.1016/j.asd.2020.101002; the one screened work (mayfly eye development) is another order, and the thesis left unjudged in the note is about Vespula wasps |
| 13 | Monobia / cff_hz | confirm | `chased` names oa-5#10 (Oecophylla smaragdina); the screened work is a theory paper on dishonest infection signals, and the flicker searches found Lepidoptera and seven hymenopteran species without Monobia |
| 14 | Monobia / corner_hz | confirm | `chased` names bee#159 (Bombus terrestris); the screened work and the searches are those of line 13, so the result is the same |
| 15 | Monobia / interommatidial_deg | confirm | `chased` and the screened work are those of line 12, so the result is the same |
| 16 | Monobia / receptor_classes | confirm | `chased` is the printed DOI 10.1017/S1464793102005985; the tool listed no candidate, and the spectral searches found a jewel wasp (Nasonia) and general opsin papers, with no eumenine |
| 17 | Nekemias / diel | confirm | The screened flower-colour paper concerns Causonis japonica, another genus, and three searches found no time of day for any Nekemias species |
| 18 | Nekemias / eye_type | confirm | The screened resveratrol review concerns human eye disease, and the ocelli searches returned plant-vision reviews that name no Vitaceae genus |
| 19 | Nekemias / sense_chemical | confirm | Neither screened work (processing volatiles of vine tea, a plant-senses review on mangroves and carnivorous plants) measures sensing in a Nekemias species, and the searches found other taxa |
| 20 | Nekemias / sense_light_nonvisual | confirm | `chased` is the printed DOI 10.17660/ActaHortic.2005.689.66 (Vitis riparia photoperiod); the five screened works are grape, lighting, ultraviolet and gene-transfer reviews, and the searches found crapemyrtle, poinsettia and seed vendors |
| 24 | Vipera / fov_h_deg | confirm | The two screened works are a weever fish eye and a 1956 snakebite blindness report, and Gower et al. 2019 (opened) sectioned one Vipera berus retina and reports no visual field |
| 25 | Asparagus / eye_type | confirm | The tool listed no candidate, and the plant-ocelli literature the searches returned names no Asparagus |
| 28 | Riparia / cff_hz | confirm | `chased` names methods#994; the four screened works (farmland remote sensing, avian contact zones, Myrmecia ant eyes, roost radar) hold no flicker data, and no Riparia value surfaced |
| 30 | Riparia / interreceptor_deg | confirm | The three screened works (a plant, a scorpionfly eye, roost radar) hold no swallow data, and the swallow retina paper that surfaced concerns Tachycineta |
| 34 | Lerema / cff_hz | confirm | `chased` names intake#27 (Epargyreus clarus, Swihart 1969); the two screened works (a skipperling breeding paper, silk-moth gene expression) hold no flicker data, and no Lerema value surfaced |
| 36 | Pyrgus / cff_hz | confirm | `chased` and the searches are those of line 34, and the third screened work, a butterfly trait database, lists no flicker trait |

## How each check came out

### (a) Queries

All 37 records repeat the `query "..."` lines and the family review line of `harvest_get.py <Genus>` word for word and in printed order, then list only entries prefixed "web: " (140 entries, 105 distinct; 70 entries sit in the 20 sampled records). The `where` hit counts ("hits in order", and the family review's "N works; M listed") match the printed counts in all 37. Two of the 105 distinct web queries are shared across genera: Lerema and Pyrgus share a title search for Chatterjee et al. 2020 and a Hesperiidae flicker query, and each of the two carries its own scientific-name and common-name search, so I do not count it. Queries differ in 0 of the 20 sampled records (0 of 37).

### (b) `chased`

In the sample, 4 records name a DOI that the harvest prints as a citation-step line (12 and 15: 10.1016/j.asd.2020.101002; 16: 10.1017/S1464793102005985; 20: 10.17660/ActaHortic.2005.689.66). Nine say the queue names no measured relative (1, 3, 10, 17, 18, 19, 24, 25, 30), and the queue's `closest` is `none` for each. Seven say the citation step did not run on the nearest relative's source and give the queue's `closest_record`: methods#994 (lines 6 and 28; Boström et al. 2016, 10.1371/journal.pone.0151099), recheck-15-fixed#2 (line 7; Agelaius phoeniceus, Fernández-Juricic et al. 2019), oa-5#10 (line 13; Oecophylla smaragdina, Ogawa et al. 2023), bee#159 (line 14; Bombus terrestris, Skorupski and Chittka 2010) and intake#27 (lines 34 and 36; Epargyreus clarus, Swihart 1969, 10.1016/0022-1910(69)90196-6). I resolved each id to its source, and none of those sources is among the printed citation DOIs, so the reasons hold. Over all 37 records, 11 name a DOI, 16 give a queue-none reason, 10 give a nearest-relative reason and 0 are unsupported. No record says "no family review found". `chased` is unsupported in 0 of the 20 sampled records (0 of 37).

### (c) `screened`

15 of the 20 sampled records carry `screened` entries (30 entries, 25 distinct works), and the tool listed no candidate for the other 5 (lines 1, 7, 10, 16, 25). The prompt asks for three per record, and I read every entry. Ten of the 25 works print an abstract start in the harvest output. The other 15 are family-review lines, which `harvest_get.py` prints with the title only, so I read their abstracts from the harvest data itself (the works that `harvest_get.load()` returns, 700 characters each; all 15 carry one) and ran no title search. Every reason matches its abstract, and none of the 25 works reports the record's trait for a species of its genus. Six reasons (lines 17, 19 and 20) cite "the abstract start" of a family-review work whose abstract the printed output does not show; the abstracts exist in the data and agree with the reasons. No sampled record screened out a work that reports the measurement (0 of 20).

### (d) My own searches

Each trait group got the two prescribed searches and one of my choosing (18 groups, 54 searches; the full list is at the end). Only the Heliotropium diel group turned up a measurement; the other 17 groups turned up none, as follows.

- Heliotropium / sense_chemical (line 3): the searches returned general plant-volatile reviews, an eLife paper on herbivore-volatile transfer, and the allelopathy of H. curassavicum as a donor (essential oils and extracts tested on other plants). None reports a sensing measurement.
- Nekemias / sense_light_nonvisual (20): the searches returned crapemyrtle and poinsettia shading papers (both opened, neither Vitaceae) and garden and seed-vendor pages. A University of Tennessee thesis (voljournals.utk.edu/utk_gradthes/10646) came first for one query and was blocked, so its subject is unknown.
- Nekemias / diel (17): the searches returned the Illinois Wildflowers visitor page (opened; it gives no time of day), a Setaria anthesis paper already known from audit 41, and reviews of N. grossedentata flowering that give no hours.
- Nekemias / sense_chemical (19): the searches returned Heil and Karban 2009 (already on main) and papers on other taxa.
- eye_type for Nekemias (18), Botrypus (10) and Asparagus (25): each pair of searches returned the same plant-ocelli literature. I opened Yamashita and Baluška 2023 (Plants 12(1): 61), which gives ocelli to Arabidopsis roots and Boquila, mentions Monstera only for skototropism, and names none of the three genera, their families or Ophioglossaceae.
- Riparia / acuity group (30): no Riparia retina paper surfaced. The tree swallow paper (Tachycineta bicolor, American Naturalist, Dryad n7140) and a Purdue dissertation record did surface; the first belongs to another genus and the second names no species.
- Riparia / flicker (28): the searches returned general flicker reviews and news items on bird and animal flicker speed, among them the Trinity College Dublin item on Haarlem and Healy 2026 (237 species; the item gives no species list and does not mention swallows).
- Vipera / visual field (24): Gower et al. 2019 (opened, both the record and the accepted manuscript) sectioned one V. berus retina and reports no visual field, acuity or fovea. A degu binocular-vision preprint (opened) does not concern snakes, and the Viperidae retina paper that the harvest prints as its citation step (Frontiers in Neuroanatomy 2022, judged from its title) is a retina study.
- Cistothorus / flicker (6) and visual field (7): the flicker searches returned general reviews and a budgerigar paper, and the visual-field searches returned Fernández-Juricic, O'Rourke and Pitlik 2010 (American crow and Western scrub-jay; no wren), the Purdue visual-field page (starling, mallard, owl as examples), and, in the closing pass below, Martin 2007 and Cantlay et al. 2023.
- Monobia / acuity group (12, 15): the searches returned Currea et al. 2023 (Communications Biology; two flies, two moths, the honeybee and four ants; no wasp), Marshall and Land 1993 (stomatopods), and the Linköping thesis, which turned out to be Gutierrez Kemenes 2022 on Vespula germanica and V. vulgaris (interommatidial angles about 1.0 to 1.5 degrees), a different genus from Monobia. That resolves the lead that the notes of lines 12 and 16 left unjudged.
- Monobia / flicker (13, 14): the searches returned Chatterjee et al. 2020 (Lepidoptera) and de Souza and Ventura 1989 (seven hymenopteran species: Melipona, Trigona, Bombus, Polistes, Pseudomyrmex, Camponotus, Atta). Neither covers Monobia or another eumenine.
- Monobia / spectral (16): the searches returned Wang et al. 2023 on the jewel wasp Nasonia (UV, blue and green photoreceptors) and insect opsin-evolution papers, one of them (PMC4824169) blocked. The pages I could read hold no Monobia or other eumenine value.
- Lerema (34) and Pyrgus (36) / flicker: the searches returned Chatterjee et al. 2020 (the page names Hesperiidae but neither genus), Døving and Miller 1969 (Epargyreus clarus; spatial and intensity data, no flicker), Horridge, Giddings and Stange 1972 (seven Australian skipper genera; no flicker in the abstract), Dodt 1954 (vertebrates), Nakagawa and Eguchi 1994 (a swallowtail) and a box jellyfish paper. None gives a Lerema or Pyrgus value.

## The one error

**Line 1, Heliotropium / diel.** The record says `found: none` for the diel cell of Heliotropium curassavicum. Abid, Nayani, Riaz and Fatima, "The pollination biology of Heliotropium curassavicum L. (Boraginaceae) from Pakistan", Pakistan Journal of Botany 55(4): 1497-1501, 2023 (DOI 10.30848/PJB2023-4(23)), watched the species at five sites in and around Karachi and reported that its flowers open mostly between about 11:00 and 14:00 and close around noon to 14:00 after two to three days open. That is a flower-opening time for a species of the genus, the kind of evidence main holds for plant diel (sweep-20#5). The abstract states no time, which is how the paper passes a title-and-abstract screen. The record page (pakbs.org/pjbot/paper_details.php?id=7427) confirms authors, journal and DOI, and the open PDF (pakbs.org/pjbot/papers/1681376802.pdf) carries the hours, which I read in two fetches of the PDF.

The paper is new to the repository. The Heliotropium harvest output holds no pollination or anthesis work, a search of the repository for the DOI and the authors finds nothing, the queue lists diel for H. curassavicum as open (`closest: none`), and sweep-31 line 15 (14 October) also found none for the same cell with a single query.

How the record missed it (my inference from the queries): its first three web queries use the harvest's plant diel words, "flower opening time" and "nyctinasty", which retrieve movement papers, and five of its nine web queries then chased an unidentified PMC identifier (PMC5055817) and an Oxalis article (TIH-2023-0011), while a sixth restricted a topical query to PubMed Central domains. None used "anthesis", "pollination biology" or "floral biology". My two prescribed searches missed the paper in the same way, and my third, worded for floral biology, listed the PDF on its first page, so an auditor following the protocol to the letter could have missed it too.

## Closing pass and unread leads

After the prescribed searches I opened four more pages that those searches had returned and I had not read, because each could hold a Riparia or Cistothorus value. None does:

- Purdue news release on Tyrrell et al. 2019, "A novel cellular structure in the retina of insectivorous birds" (Scientific Reports): it names only the Empidonax flycatchers and gives no spacing or acuity value. The paper characterized other birds that the release does not name, so the paper stays unread.
- Martin 2007, "Visual fields and their functions in birds" (Journal of Ornithology): Appendix 2 lists 32 species, with the European starling the only passerine and no wren or swallow.
- Cantlay et al. 2023, "Binocular vision and foraging in ducks, geese and swans (Anatidae)" (Proceedings of the Royal Society B 290: 20231213) covers 39 anatid species only.
- Moore 2014, "Multidimensional approach to comparative avian visual systems", Purdue dissertation (repository record): the abstract names no species (29 North American species in 14 families), so a wren or swallow in its sample is unresolved.

These pages were blocked or left unread, and I retried none: voljournals.utk.edu/utk_gradthes/10646 (Anubis; Nekemias light thesis), pmc.ncbi.nlm.nih.gov PMC3886328 (reCAPTCHA; returned for a Cistothorus palustris query, title unseen), PMC4824169 (Feuda et al. 2016 opsin evolution; redirect not followed), archive.org biostor-148004 (redirect, then permission unanswered), bioone.org nvy171 and d.lib.msu.edu etd 7013 (bot protection; access limited). I did not open PMC5371358 (Tyrrell and Fernández-Juricic 2017, whose S1 Table lists 40 species; audit 42 met a bot check there), nature.com s41559-026-02994-7 (Haarlem and Healy 2026; species list unseen), the Healy et al. 2013 PDF on TARA (vertebrate flicker; species list unseen), or, in unsampled Riparia lines 27 and 29, the 2022 sight-line preprint 10.1101/2022.10.03.510686, whose note says it was left unopened and whose URL I saw only in the harvest print, since none of my searches returned it.

## Wanted lines (checked and listed outside the count)

I checked 6 of the 26 lines against a page I opened (lines 3, 12, 13, 14, 18 and 19). Two pages were blocked (lines 15 and 16), and no page surfaced for line 17. The other 17 lines (1, 2, 4 to 11, 20 to 26) were compared with the harvest listing they came from, and title, year and DOI (or OpenAlex id) agree in all 17.

| line | work | page opened | result |
|---|---|---|---|
| 3 | Phenology of Botrypus virginianus across 135 degrees of latitude | research-scotland.ac.uk record | Title agrees. The record is dated November 2025 and lists no authors, volume, issue, pages or DOI, so the blank year can be filled with 2025 while "115(4)" and the DOI 10.1640/0002-8444-115.4.296 stay unconfirmed. The abstract ties leaf timing to day length and temperature, so the lead is sound |
| 12 | Effects of daylength on dry matter partitioning in asparagus | ishs.org article 589_33 | Woolley, Karno and Nichols, Acta Horticulturae 589 (2002): 243-247, DOI 10.17660/ActaHortic.2002.589.33. The line leaves authors, year and DOI blank. The abstract reports a day-length response without naming a species or cultivar |
| 13 | Studies on flower bud formation of Asparagus officinalis L | Hokkaido University repository PDF | Mizonobe, Yamaguchi, Maeda, Harada and Yakuwa, Journal of the Faculty of Agriculture, Hokkaido University 64(4): 272-278 (1991); no DOI on the page. The line leaves authors, year, journal and DOI blank. The text reports nothing about light, photoperiod or day length, so the lead is dead for sense_light_nonvisual (the line's own `why` called it a long shot) |
| 14 | Effect of temperature and light on the texture of stored white asparagus spears | ishs.org article 368_18 | Siomos, Sfakiotakis and Dogras, Acta Horticulturae 368 (1994): 167-176, DOI 10.17660/ActaHortic.1994.368.18. The line leaves authors, year and DOI blank. The study is postharvest, as the line says |
| 18 | Floral aroma and pollinator relationships in two sympatric Mediterranean Asparagus species | UIB repository record | Llorens, Tomàs, Ferriol, García and Gil, Plants 12(18): 3219 (2023); year and DOI agree. The line leaves authors blank. The abstract gives no time of day for scent emission |
| 19 | Evolution of the eyes of vipers with and without infrared-sensing pit organs | City Research Online record and accepted manuscript | Thirteen authors (Gower, Sampaio, Peichl, Wagner, Loew, McLamb, Douglas, Orlov, Grace, Hart, Hunt, Partridge, Simões), Biological Journal of the Linnean Society 126(4): 796-823 (2019), DOI 10.1093/biolinnean/blz003. The line leaves authors, year and DOI blank. Main already holds this paper: evidence in oa-4 (Vipera berus lambda_max_nm and photoreceptor_tiers among others) and wanted lines in sweep-70, sweep-75 and web-herps. The accepted manuscript sectioned one V. berus retina, could not tell its rods from small single cones, and, in the text I could read (the fetch stops before the supplement), reports no acuity, fovea or pupil shape for Vipera, the three traits the line gives |
| 15, 16 | MSU asparagus-volatiles dissertation; Environmental Entomology 48(1) | d.lib.msu.edu etd 7013; bioone.org | Both pages were blocked, so I could not tell which dissertation etd 7013 is and could not verify either line (line 16 gives DOI 10.1093/ee/nvy171) |
| 17 | Allelopathic potential of asparagus | none | No page surfaced, so the line stays unverified |

Faults, listed outside the count: authors are blank on 26 of 26 lines; years are blank on 8 (3, 12, 13, 14, 15, 16, 17, 19); DOIs are blank on 8 (6, 8, 12, 13, 14, 15, 17, 19), two of those with an OpenAlex id that agrees with the harvest data. Of the 6 lines checked on an opened page, 0 are contradicted, and the table above fills most of their blanks (line 3 gains only its year, and line 13 has no DOI to give). Line 13 is a dead lead. Three lines duplicate entries already on main: line 2 (Li et al. 2015 on phytochrome diversity, in wanted/canon.jsonl with evidence in canon-3 and canon-13; Botrypus is not among the logged taxa), line 19 (above) and line 21 (the mock-viper pupil paper, in wanted/sweep-64.jsonl).

## Counts and rate

- I checked 20 of the 37 records.
- Queries differed in 0 records, `chased` was unsupported in 0, a `screened` work reported the measurement in 0, and a measurement was missed in 1 (line 1).
- **The unit has 1 error in 20 records, an error rate of 5.0%** (exact 95% interval 0.1% to 24.9%). The rate sits on the line and is not under it, and the interval is far too wide to place the unit's true rate on either side.

Pooled with the desk's other audits of units written for the desk-screen round:

| audit | unit | items | errors | rate |
|---|---|---|---|---|
| 40 | harvest-26 | 16 | 1 | 6.3% |
| 41 | harvest-27 | 25 | 4 | 16.0% |
| 42 | harvest-28 | 16 | 4 | 25.0% |
| 43 | harvest-30 | 20 | 1 | 5.0% |
| all four | | 77 | 10 | **13.0%** (6.4% to 22.6%) |

Audits 40 to 42 alone make 9 of 57, 15.8% (7.5% to 27.9%). Audits 41 and 42 counted evidence records and, in the totals above, quote-form failures, which harvest-30 does not have, so the search records alone are the closer comparison: 1 of 16 (audit 40), 2 of 16 (41), 3 of 13 (42) and 1 of 20 (43) make 7 of 65, 10.8% (4.4% to 20.9%). Harvest-30 is the best of the four on either count and still falls on the wrong side of the line.

## Fault kinds from audits 40 to 42

| kind | earlier audits | harvest-30 |
|---|---|---|
| Measurement in the harvest output but screened | Tradescantia (Digby and Firn 2002), Cuculus (Olsson et al. 2021), Ambrosia (Kralemann 2018 against a `where` sentence) | I did not find it. All 30 screened entries (25 works) were read against the harvest data, and none holds a measurement |
| Measurement absent from the harvest output, found by web search | Tropaeolum (Munir 2015), Setaria (Desai 2018), Photinus (Al Marshad), Ambrosia (Mann 1942) | **I found it once**, in Heliotropium diel (Abid et al. 2023). It has the shape of the Setaria miss: a flower-opening paper whose abstract gives no hours |
| `chased` holding a family-review query string, or a none-reason that contradicts `where` | Nymphaea, Lindera; Celastrus, Cuculus | I did not find it. 37 of 37 are supported |
| Queries that differ from `harvest_get.py` | Added web queries in every record of audit 39 | I did not find it. 37 of 37 are identical and in order |
| Web query shared across genera | Coccyzus and Cuculus; Graphium, Plutella and Euptychia | Two of the 105 distinct web queries are shared by Lerema and Pyrgus, each of which also has its own pair, so I did not count them |
| Unjudged or unopened leads | Pernis (Potier 2018), Nandina, Conopholis, Lespedeza | **I found three**: the Linköping thesis in lines 12 and 16 (judged here: Vespula), the sight-line preprint in lines 27 and 29 (unsampled, unopened) and the unidentified PMC5055817 in line 1 |
| Wanted lines with blank or contradicted authors, or duplicates of main | Authors blank on 4 of 6 (audit 41); 2 of 13 contradicted and 5 duplicates of main (audit 42) | **I found it**: authors are blank on 26 of 26 lines, years on 8 and DOIs on 8; 3 lines duplicate main; 0 of the 6 lines checked on a page are contradicted |
| Weak share | 100% (40), 74% to 80% (41), 100% (42) | **I found it** in 20 of 20 records (see below) |

## Weak share

All 37 records say in `where` that results were read by title and that no paper was opened. The 20 sampled records therefore rest on harvest titles and abstract starts and on title-level web search, with no full text read at the desk. That is the same limit as in audits 40 to 42, and it is why the Heliotropium paper passed: its abstract names no hours, and no query asked for anthesis. My "confirm" verdicts rest on the same kind of reading plus the pages I opened, with the limits stated in each line above.

## Verdict

**Does not pass.** One missed measurement in 20 records is 5.0%, which is not under 5%. On the counted faults harvest-30 is the cleanest of the four units audited: queries, `chased` and `screened` hold in every record I checked, and the one error is a miss of the kind that audits 40 to 42 also found. The miss follows from how the plant lines were searched. The harvest sent three light queries (phytochrome photoreceptor, light perception, phototropism) for each of the unit's five plant genera; Botrypus and Nekemias also list five plant-trait queries from run 12, each ending "error gave up", and Heliotropium, Asparagus and Cocculus list none (the run list shows plant-trait shards 0, 1, 3, 4 and 5 and no shard 2). The desk's own web pair for plant diel lines repeats the two words that run 12 would have used. For the plant diel and sense_chemical lines (1, 3, 9, 11, 17, 19, 21, 23) the only searches aimed at the trait are therefore the desk's web searches, and four of those eight lines were in my sample, with one error among them.

## For the desk

1. Open the Heliotropium curassavicum diel cell and send Abid et al. 2023 (DOI 10.30848/PJB2023-4(23); open PDF at pakbs.org/pjbot/papers/1681376802.pdf) to the oa queue.
2. Add "anthesis" and "pollination biology" to the plant diel words, both in `PLANT_TRAIT_QUERIES['diel']` (ci/harvest/harvest.py) and in the web pair of desk-screen.md. Both plant diel misses of audits 41 and 43 (Setaria, Heliotropium) are floral-biology papers, which is my inference from two cases. Line 21 (Cocculus diel), which I did not sample, used only "flower opening time" and "nyctinasty"; line 9 (Botrypus diel) used "nyctinasty" and movement words, and lines 11 and 23 (Botrypus and Cocculus sense_chemical) used "volatile signalling" alone. Line 17 (Nekemias diel) added "anthesis" to its third query.
3. Wanted lines: fill the blanks listed above for lines 3, 12, 14, 18 and 19; drop line 13 as a dead lead; mark line 19 as already read on main, with no acuity, fovea or pupil shape for Vipera in the text I could read; merge lines 2, 19 and 21 with the entries they duplicate. Lines 15 to 17 stay unverified.
4. Open leads, in the order I would take them: the Tyrrell et al. 2019 paper and the Moore 2014 dissertation (Riparia and Cistothorus retina and field values), the Haarlem and Healy 2026 species list (flicker for Riparia, Cistothorus, Monobia, Lerema and Pyrgus), the Tyrrell and Fernández-Juricic 2017 S1 Table (Cistothorus visual field), and the Tennessee thesis for Nekemias light.

## Searches and fetches used

62 WebSearch calls: the 54 prescribed (18 trait groups, two searches and one of my choosing each), one follow-up on the Haarlem and Healy 2026 lead, and 7 title searches (the Abid et al. page and the pages for wanted lines 3, 12, 13, 14, 16 and 18). No search was refused. 45 WebFetch calls, each on a URL that one of my searches returned; 7 were blocked or ended in an unanswered redirect and none was retried.

Searches by trait group (a group's third query is my own choice):

1. Heliotropium diel: "Heliotropium flowers open and close time of day diurnal rhythm"; "heliotrope plant flower opening time of day scent emission rhythm"; "Heliotropium anthesis time pollination biology floral biology flowers open morning".
2. Heliotropium sense_chemical: "Heliotropium volatile organic compounds plant-plant communication airborne signal response"; "heliotrope plant responds to volatiles from neighbouring plants or herbivores"; "Heliotropium curassavicum allelopathy volatiles neighbouring seedlings response chemical cue".
3. Nekemias sense_light_nonvisual: "Nekemias arborea light response photoperiod flowering growth shade"; "peppervine Ampelopsis arborea light shade photoperiod response"; "Ampelopsis arborea peppervine seed germination light requirement dormancy".
4. Nekemias diel: "Nekemias flowers open time of day anthesis flowering biology"; "peppervine Ampelopsis flowers open morning pollinators bees time of day"; "Ampelopsis grossedentata vine tea flowering biology blooming time pollination".
5. Nekemias sense_chemical: "Nekemias arborea herbivore-induced volatiles airborne signalling neighbouring plants"; "peppervine Ampelopsis arborea volatile emission plant defence communication"; "Nekemias arborea chemical ecology response to herbivory jasmonate volatiles experiment".
6. Nekemias eye_type: "Nekemias plant eye ocelli lens-like epidermal cells light focusing"; "peppervine plant ocelli vision lens cells leaf"; "Vitaceae Ampelopsis Cissus leaf epidermal lens cells iridoplasts light harvesting ocelli".
7. Botrypus eye_type: "Botrypus virginianus eye ocelli lens-like cells photoreceptor"; "rattlesnake fern grape fern eyes ocelli vision lens cells"; "Ophioglossaceae fern epidermal lens-like cells light sensing structure ocellus".
8. Riparia acuity group: "Riparia riparia visual acuity retina cone density photoreceptor spacing"; "bank swallow sand martin eye retina visual acuity ganglion cell topography"; "swallows Hirundinidae eye anatomy retina fovea cone density resolution comparative aerial insectivore".
9. Riparia flicker: "Riparia riparia flicker fusion frequency temporal resolution vision"; "bank swallow sand martin critical flicker fusion temporal resolution electroretinogram"; "aerial insectivore swallows swifts martins fast vision flicker fusion frequency measured Hz".
10. Vipera visual field: "Vipera visual field binocular overlap eye position head viper"; "adder viper snake visual field binocular vision eye orientation"; "Evolution of the eyes of vipers with and without infrared-sensing pit organs" (title).
11. Cistothorus flicker: "Cistothorus flicker fusion frequency temporal resolution vision wren"; "marsh wren sedge wren visual temporal resolution flicker vision"; "wren Troglodytidae retina photoreceptor electroretinogram flicker visual system study species Troglodytes Cistothorus".
12. Cistothorus visual field: "Cistothorus visual field binocular eye position wren"; "marsh wren visual field binocular overlap blind area"; "\"Cistothorus palustris\" visual field OR \"binocular\" OR \"eye\" vision physiology measured".
13. Monobia acuity group: "Monobia quadridens compound eye visual acuity interommatidial angle facets"; "mason wasp potter wasp Eumeninae compound eye visual acuity ommatidia"; "Daniel Gutierrez master thesis Linköping wasp compound eye vision".
14. Monobia flicker: "Monobia quadridens flicker fusion frequency photoreceptor temporal resolution"; "mason wasp potter wasp flicker fusion frequency photoreceptor corner frequency"; "Vespidae wasps Polistes Vespa temporal resolution flicker fusion electroretinogram photoreceptor speed comparative Hymenoptera".
15. Monobia spectral: "Monobia quadridens spectral sensitivity photoreceptor opsin UV blue green receptor classes"; "mason wasp potter wasp spectral sensitivity opsin photoreceptor colour vision Eumeninae"; "Hymenoptera opsin gene evolution wasps Vespidae UV blue long-wavelength opsins species sampled eumenine".
16. Lerema flicker: "Lerema accius flicker fusion frequency temporal resolution electroretinogram"; "clouded skipper butterfly temporal resolution flicker vision photoreceptor"; "Lerema accius clouded skipper eye photoreceptor electrophysiology compound eye structure".
17. Pyrgus flicker: "Pyrgus flicker fusion frequency temporal resolution electroretinogram skipper"; "grizzled skipper checkered skipper Pyrgus malvae oileus flicker temporal vision photoreceptor"; "Pyrgus skipper butterfly compound eye electrophysiology photoreceptors ERG temporal response".
18. Asparagus eye_type: "Asparagus plant eye ocelli lens-like epidermal cells photoreceptor vision"; "asparagus plant sees eyes ocelli vision cladodes lens cells"; "Asparagaceae plant ocelli light sensing structures epidermal lens cells shoot tip".
19. Lead on Haarlem and Healy 2026: "Haarlem Healy 2026 critical flicker fusion frequency 237 species phylogenetic analysis dataset temporal resolution animals Nature Ecology Evolution".
20. Title searches: the Abid et al. paper; "Phenology of Botrypus virginianus Across 135 Degrees of Latitude"; "Floral Aroma and Pollinator Relationships in Two Sympatric Late-Summer-Flowering Mediterranean Asparagus Species"; "Biological Control of Asparagus Pests Using Synthetic Herbivore-Induced Volatiles"; "Effects of Daylength on Dry Matter Partitioning in Asparagus"; "Effect of Temperature and Light on the Texture of Stored White Asparagus Spears"; "Studies on Flower Bud Formation of Asparagus officinalis L".
