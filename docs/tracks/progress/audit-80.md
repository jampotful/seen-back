# Audit 80: harvest-c23 (branch research/harvest-c23, head e842a979)

Gate: `screen_candidates.py --check` on the 38 search records and 13 wanted lines prints "0 problems".

## Sample (seed 80)

`random.seed(80)` and `random.sample(lines, 20)` over the 38 search record lines (1-based) give, in draw order, 18, 26, 35, 27, 24, 34, 37, 12, 1, 38, 25, 36, 13, 8, 20, 2, 32, 28, 6 and 17. The draw was made before any record was read. The same call on the numbers 1 to 38 gives the same positions.

The sample found errors, so the desk's 15-record extension ran: `random.seed(8015)` and `random.sample(<the 18 undrawn line numbers in ascending order>, 15)` draw 5, 31, 10, 22, 4, 7, 3, 11, 14, 9, 29, 33, 30, 19 and 23 (sorted: 3, 4, 5, 7, 9, 10, 11, 14, 19, 22, 23, 29, 30, 31, 33). Lines 15, 16 and 21 were in neither draw.

## Method

Judged against desk-audit.md and desk-screen.md, point 10 included, with the owner's readings of 25 October 2026: plant sense_chemical counts living responses (responses to hormones or elicitors included) and volatile signalling only, with no extracts, oils or cut-flower treatments; plant eye_type is "none" for every plant, and epidermal focusing is logged under sense_light_nonvisual. Where the readings leave a scope open I followed main's own evidence, as audit 78 did.

`harvest_get.py` and `screen_candidates.py` were run on main for the 14 genera drawn. A script compared each record's non-web `queries` with the harvest's `query` and `family review` lines: all 35 drawn records match word for word and in order, and each adds the two labelled web searches. Dittrichia, Sidalcea and Cochemiea are in no harvest run, and their records hold web searches only, as they say. No harvest shows a failed ("gave up") step. Every DOI named in `chased` (10.1016/j.tree.2009.09.010 for Hylodesmum and Calendula) is printed in the harvest's citation step; every other `chased` is a none-reason that the output supports (no citation step printed, or no harvest run). I read the screened entries against the harvest's titles and abstract starts (three per record, or all where fewer) and found none that reports a measurement of the trait. The harvest's screen lists candidates only for traits the harvest held open, so for the reopened diel and eye_type cells of Pulicaria, Hylodesmum, Cephalanthera, Nonea, Pelecyphora, Cota and Genista it lists none, and the records' empty or short `screened` fields are what the tool supports.

The WebSearch ration was 60, shared with another audit, so I could not run three searches for each of 35 records. I ran 38 WebSearches: one to three per genus and trait, aimed where a missed measurement was likeliest (synonyms, CAM gas exchange in the cacti, elicitor and germination responses, floral scent), and three pooled focusing searches for the eye_type records. I opened 17 pages my searches returned; four fetches were refused or went unanswered and were not retried (listed below). No ResearchGate, academia.edu, Sci-Hub, LibGen or library proxy page was opened (an MDPI result on 0-www-mdpi-com.brum.beds.ac.uk was left closed), and no paper text is committed.

## Verdicts (sample of 20)

| Line | Record | Verdict |
|---|---|---|
| 18 | Pulicaria eye_type | ok. Queries match (5 harvest, 2 web). The screened Tagetes lutein review concerns the human eye. My pooled Asteraceae focusing search returned general conical-petal-cell reviews; no Pulicaria focusing work. |
| 26 | Hylodesmum sense_chemical | ok. Queries match (5, 2); chased DOI in the citation step. The Swartzia stamen paper and the blister-beetle paper (Desmodium fodder species in push-pull plots) name no Hylodesmum. My search returned push-pull work on Desmodium intortum and D. uncinatum, which stay in Desmodium. |
| 35 | Cephalanthera eye_type | ok. Queries match (5, 2). The tool lists no candidate. My pooled focusing search returned the FIU lens-cell paper and grass epidermis work; nothing on Cephalanthera. |
| 27 | Hylodesmum sense_light_nonvisual | ok. Queries match; the six screened works are reviews or other legume genera. My search found Houx et al. 2009 (Native Plants Journal 10(3): 232-238, 10.3368/npj.10.3.232, page opened), a shade experiment on Desmodium canescens, D. canadense and D. illinoense; none is a Hylodesmum. |
| 24 | Hylodesmum diel | ok. Queries match; the Melilotus leaflet paper and two others are correctly screened. My search returned Desmodium setigerum and D. grahamii pollination studies (Desmodium s.s.); no Hylodesmum opening time. |
| 34 | Cephalanthera diel | ok. Queries match. My search found Dafni and Ivri 1981 (Plant Syst Evol 137(4): 229-240, 10.1007/BF00982788, Haifa portal opened), on bee pollination of C. longifolia; the abstract gives no daily timing. |
| 37 | Armoracia diel | ok. Queries match (13, 2). The progamic-phase paper (10.1111/j.1439-0523.2007.01439.x) treats anthesis as a stage with no clock time, as its abstract start shows. My searches (horseradish anthesis hour; horseradish circadian or day-night variation) returned seasonal glucosinolate studies and natural-history pages. |
| 12 | Lagurus eye_type | ok. Queries match (9, 2). My pooled search returned "Light environment and epidermal cell morphology in grasses" (Int J Plant Sci, 10.1086/683278), which the unit already holds as Lagurus sense_light_nonvisual wanted line 4, the home reading (b) gives it. |
| 1 | Dittrichia diel | ok. Web-only, as the record says. My search returned Dittrichia species pages and floras; no daily opening time. |
| 38 | Armoracia eye_type | ok. Queries match; the three screened animal-eye works are correctly screened. No horseradish focusing work found. |
| 25 | Hylodesmum eye_type | ok. Queries match; no candidate listed and none found. |
| 36 | Cephalanthera sense_chemical | **error**. D'Auria M, Lorenz R, Mecca M, Racioppi R, Romano VA, "Aroma components of Cephalanthera orchids", Natural Product Research 35(1): 174-177 (epub 2019), 10.1080/14786419.2019.1616724 (pherobase record opened): SPME-GC-MS of the scent of C. damasonium, C. rubra and C. longifolia, naming pentadecane, hexadecane, heptadecane, alpha-farnesene and cis-beta-farnesene. Main logs the same group's SPME-GC-MS floral scent of Platanthera bifolia under sense_chemical, grade m (recheck-1-fixed, sweep-21), so this is a measurement of the kind main holds. The record's own helleborine search returned pherobase records that it left unread. The work is not on main's wanted or evidence files; sweep-97:30 named it before the owner's reading and called it "not sensing". One fork stays open: the pherobase page does not say whether living plants were sampled. The group's 2021 Orchis paper (Compounds 1(2): 83-93, MDPI page opened) enclosed whole living plants under a bell jar, which suggests the same method; if the Cephalanthera samples were cut flowers, reading 10(a) would exclude them and this verdict becomes ok. |
| 13 | Lagurus sense_chemical | ok. Queries match (9, 2); the five screened works (potato tubers, hamsters, a hydroponics trial, Cannabis oil, centipede glands) hold no Lagurus response. Main logs germination responses to chemicals under sense_chemical, so I searched Lagurus germination under smoke, karrikin, gibberellin or ethylene: the hits are on Avena fatua (Kępczyński and Van Staden 2012, opened) and general karrikin work, and an Annales Botanici Fennici paper on three smoke-responsive species did not open (see Leads). |
| 8 | Cochemiea sense_chemical | ok. Web-only. My cactus germination search returned GA3 trials on Ferocactus wislizeni and F. histrix (both opened); the Mammillaria species named in the second (M. huitzilopochtli, M. oteroi, M. magnimamma) are outside Cochemiea. |
| 20 | Nonea diel | ok. Queries match; the Tibouchina colour-change paper is correctly screened. My search returned anthesis studies on other genera. |
| 2 | Dittrichia eye_type | ok. Web-only; my pooled Asteraceae focusing search found nothing on Dittrichia. |
| 32 | Cota eye_type | ok. Queries match; the horse-soring, speech-perception and lutein works are correctly screened. |
| 28 | Pelecyphora diel | **error**. Nobel PS 1981, "Influence of freezing temperatures on a cactus, Coryphantha vivipara", Oecologia 48(2): 194-198, 10.1007/BF00347964 (Springer page opened): in C. vivipara var. deserti the optimum temperature for CO2 uptake shifted from 10 °C to 6 °C, and plant death was scored as a lack of net CO2 uptake at night over two months, so the abstract reports measured night-time CO2 uptake, the CAM rhythm. POWO (page opened) gives Coryphantha vivipara as a synonym of Pelecyphora vivipara, the record's own queue species. Main logs the CAM day-night stomatal rhythm under diel (Opuntia ficus-indica from Lee 2010, the very review the record screened as "concerns stomata", and Tillandsia usneoides). Fork: if the owner reads a plant's diel cell as flower timing only, this verdict becomes ok. My searches also found a llifle album of P. sneedii subsp. leei whose photo captions say flowers open about 10 a.m. and are fully open at noon; a caption is no study and I count nothing on it. |
| 6 | Cochemiea diel | ok. Web-only. EPPO lists Cochemiea grahamii (the former Mammillaria grahamii). My CAM and opening-hour searches returned Mammillaria natural-history pages and a pollination study of Desmodium grahamii (Plant Syst Evol 305: 743-754, opened), a legume with the same epithet; no Cochemiea measurement. |
| 17 | Pulicaria diel | ok. Queries match (5, 2); the Daphnia pulicaria hits and the reviews are correctly screened. My search returned a BHL item "On the Diurnal Opening of Flowers" (Proc Acad Nat Sci Philadelphia, page opened, no Pulicaria named) and a BioStor PDF whose fetch went unanswered (see Leads). |

Errors in the sample: 2 of 20, 10.0% (lines 28 and 36).

## Verdicts (extension of 15, seed 8015)

| Line | Record | Verdict |
|---|---|---|
| 3 | Sidalcea diel | ok. Web-only. My search found Ashman and Stanton 1991, "Seasonal variation in pollination of sexually dimorphic Sidalcea oregana ssp. spicata", Ecology 72(3): 993-1003 (USU repository page opened); the abstract gives nectar over the 24 h after anthesis and no clock time (see Leads). |
| 4 | Sidalcea eye_type | ok. Web-only; my Malvaceae and Cactaceae focusing search returned the plant-ocelli review and Selaginella silica-body work. |
| 5 | Sidalcea sense_chemical | ok. Web-only; my search returned karrikin and smoke-germination work on other taxa. |
| 7 | Cochemiea eye_type | ok. Web-only; same search as line 4. |
| 9 | Antennaria diel | ok. Queries match (13, 2); the Eupatorium embryology paper and the blue-light review are correctly screened. My search returned extension and nursery pages only. |
| 10 | Antennaria eye_type | ok. Queries match; the 1920 wildflower guide and the lutein review are correctly screened. |
| 11 | Antennaria sense_chemical | ok. Queries match; all 18 candidates are screened, the A. dioica extract paper under 10(a). My search returned a conservancy blog on pussytoes allelopathy (the plant as donor, which audit 78 did not count) and floral-volatile work on other genera. |
| 14 | Genista diel | ok. Queries match; the three screened works are other legume genera or reviews. My search returned Desmodium pollination studies; no Genista opening time. |
| 19 | Pulicaria sense_chemical | ok. Queries match; the P. undulata chapter and the dried-herb profile are correctly screened under 10(a). My elicitor search returned methyl jasmonate trials on Calotropis procera and Echium rauwolfii hairy roots (both opened), no Pulicaria. |
| 22 | Nonea sense_chemical | ok. Queries match; the six screened works hold no Nonea response. My search returned allelopathy and hormone papers on other plants. |
| 23 | Nonea sense_light_nonvisual | ok. Queries match; the seven screened works are correctly screened. My search returned a photoperiod-sensitivity synthesis (PMC12391026, species list unseen) and germination papers on other genera. |
| 29 | Pelecyphora eye_type | ok. Queries match; no candidate listed and none found. |
| 30 | Pelecyphora sense_chemical | ok. Queries match; the Rebutia LED paper is correctly screened. My germination search found no Pelecyphora or Escobaria chemical treatment. |
| 31 | Cota diel | ok. Queries match; the circadian review, the oat flowering-date paper and the blue-light review are correctly screened. My search returned the sunflower floret-clock paper and a "sleeping daisies" blog; no Cota. |
| 33 | Calendula eye_type | ok. Queries match (13, 2); chased DOI in the citation step; the five screened human-eye and cosmetics works are correctly screened. |

Errors in the extension: 0 of 15.

## Rate

Sample: 2 of 20, 10.0%. Sample and extension: 2 of 35, 5.7%. If the owner settles both forks against the records' finders (cut flowers for line 36, flower timing only for line 28), 0 of 35. On the counted reading the unit is above 5% on either base, so harvest-c23 fails. Pooled with the desk's earlier audits of desk-screen units (audits 43 to 51, 55 to 73 and 75 to 78, 13 errors in 724 records): 15 in 759, 2.0%.

**Error records: lines 28 (Pelecyphora diel) and 36 (Cephalanthera sense_chemical)** of docs/views/searched/harvest-c23.jsonl. The audit did not cover the whole unit, so the 3 undrawn lines (15, 16, 21) and the cells of the two error kinds elsewhere were not checked: the Cochemiea diel cell (line 6) shares line 28's CAM gap, though my searches found no Cochemiea gas-exchange study, and every reopened plant sense_chemical record that ran only the elicitor search words may share line 36's floral-scent gap.

## Wanted lines (listed, not counted)

All 13 lines leave `authors` empty, so none is counted.
- Line 7 (10.1007/s11816-014-0331-6, Cota sense_chemical): the Springer page (opened) is Jang G, Shim JS, Jung C, Song JT, Lee HY, Chung PJ, Kim J-K, Choi YD, "Volatile methyl jasmonate is a transmissible form of jasmonate and its biosynthesis is involved in systemic jasmonate response in wounding", Plant Biotechnology Reports 8(6): 409-419, 2014. The page names no species, and its mutant stock points to Arabidopsis. The paper holds no Cota measurement, so the line holds the Cota sense_chemical cell out of a record on a paper that cannot fill it.
- Line 5 (10.1007/s11738-011-0799-4, Genista sense_chemical): the harvest prints the title ("Elicitation and permeabilisation affect the accumulation and storage profile of phytoestrogens in high productive suspension cultures of Genista tinctoria", 2011), which the line leaves empty with year 0 while the progress note calls the title unseen.
- Line 13 (10.3390/biology14080935): the fetch went unanswered, so it is unchecked. The other lines were not checked against a page.

## Leads

- Pulicaria diel: BioStor 151411 (archive.org PDF) came back from a search on Pulicaria flower opening; its fetch went unanswered, so its subject is unknown.
- Lagurus sense_chemical: "Germination response of three smoke- and karrikinolide-responsive species", Annales Botanici Fennici 61(1), 10.5735/085.061.0106; the page was bot-protected and its species are unseen.
- Sidalcea diel: Ashman and Stanton 1991 may give hours of anthesis in the full text.

## Blocked pages

- pmc.ncbi.nlm.nih.gov PMC10818387 table (bot check).
- dn760003.eu.archive.org BioStor 151411 PDF (permission not answered; not retried).
- bioone.org Annales Botanici Fennici 61(1) article (bot protection).
- doi.org/10.3390/biology14080935 (permission not answered; not retried).

Desk ruling (27 Oct): both flagged records follow the rules in force. Plant diel means flower opening and scent timing (CAM night CO2 uptake is metabolism), and scent sampled from cut flowers is excised tissue under point 10(a). The 38 records merge whole; the CAM question goes to the owner as a fork.
