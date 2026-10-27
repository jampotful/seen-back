# Audit 84: harvest-c8, -c9, -c4 and -c6 as one unit (PR 37, Codex round 2026-10-27, ref origin/cx/round28, head 818d827b)

Gate: `screen_candidates.py --check` prints "0 problems" for each of the four batches (harvest-c8: 23 search records, 181 wanted lines; harvest-c9: 6 and 234; harvest-c4: 1 and 15; harvest-c6: 1 and 5).

## Sample (seed 84)

The 31 search record lines were listed as (file, line), 1-based, in the order harvest-c8, -c9, -c4, -c6. `random.seed(84)` and `random.sample(lines, 20)` give, in draw order: (c9, 1), (c8, 10), (c9, 2), (c8, 2), (c8, 16), (c8, 1), (c8, 17), (c8, 22), (c8, 11), (c8, 7), (c8, 15), (c9, 4), (c8, 18), (c8, 12), (c8, 5), (c8, 9), (c8, 20), (c8, 8), (c6, 1), (c8, 19). The draw was made before any record was read.

The first draw held exactly 1 error, so the extension ran. Only 11 lines were left undrawn, so all of them were judged: `random.seed(8415)` and `random.sample(<the 11 undrawn pairs in file order>, 11)` give (c9, 5), (c8, 23), (c8, 3), (c4, 1), (c9, 6), (c8, 13), (c8, 6), (c8, 4), (c8, 21), (c9, 3), (c8, 14). The two draws cover the whole unit.

## Method

Judged against desk-audit.md and desk-screen.md, point 10 (a) to (e) included: plant sense_chemical counts living responses, hormone and elicitor responses included, and volatile signalling, and excludes extracts, oils and cut-flower treatments; plant eye_type is "none" for every plant, with epidermal focusing logged under sense_light_nonvisual; growth or germination trials under set light intensities count under sense_light_nonvisual. For plant diel I used main's own standard: main logs descriptive anthesis rows such as "description of the study species" (Ipomopsis) and a field description of chicory heads opening around sunrise.

`harvest_get.py` was run for every genus in the unit, and a script compared each record's non-web `queries` with the harvest's `query` and `family review` lines. In all 31 records every harvest line appears word for word and in the harvest's relative order. Pilea (c4:1) puts its live OpenAlex queries between the twelfth harvest query and the harvest's family review, so its harvest lines form an ordered subsequence and lose their contiguity. Many records also carry queries the harvest never printed and that bear no "web: " label: Codex ran the OpenAlex API directly (for example nine such queries in Mikania, Ambrosia and Triodanis, five in Phoradendron) or repeated a run-17 family review that `harvest_get.py` does not print for a genus outside every run (Asteraceae for Baccharis, Sapindaceae for Aesculus). `where` declares both sources in every case. Audit 39 noted added queries without counting them, and I follow it; the fork is listed below.

Every DOI in `chased` is either printed in the genus's citation step (Ambrosia, Diospyros, Nephrolepis, Medicago, Cephalanthus, Calyptocarpus, Lorinseria, Pilea, Succisa) or is a work of a run-17 family review on the ci branch, which I read from the harvest data: 10.3390/plants7040111 in the Asteraceae review (Mikania, Baccharis), 10.1093/jxb/erag313 in the Fabaceae review (Albizia, Melilotus), 10.1093/jxb/eru327 in the Campanulaceae review (Triodanis), 10.1111/jbi.70113 in the Sapindaceae review (Aesculus). The none-reasons hold against the harvest output. No harvest shows a failed step.

I read the screened entries (three per record, all where fewer) and found none that reports a measurement of the record's trait in the genus. I ran 33 WebSearches: two to five per diel, sense_light_nonvisual and sense_chemical record, and five pooled focusing searches for the 22 eye_type records. I opened only pages my own searches returned.

## Verdicts, first draw (20)

| File:line | Record | Verdict |
|---|---|---|
| c9:1 | Mikania eye_type | ok. Web and live-OpenAlex only (no harvest run). The Bras J Pharmacog epidermis paper is screened with the owner's wording. My pooled Asteraceae focusing search returned the FIU lens-cell paper, PMC8309337 and a Mikania morphoanatomy record; no focusing work on Mikania that eye_type could take. |
| c8:10 | Cephalanthus eye_type | ok. 15 harvest lines match; both citation DOIs printed. Screened pollen-wall and bird-lens works hold no eye. Pooled search found nothing. |
| c9:2 | Phoradendron diel | ok. My searches ("Phoradendron flower opening time anthesis"; a P. leucarpum anthesis and nectar search) returned floras, a Wikipedia page and a Mexican mistletoe on mesquite (PMC6108335, page unanswered); no daily anthesis time for Phoradendron. `chased` says no family review was found although the record ran the Viscaceae review live; noted, the harvest output prints none for the genus. |
| c8:2 | Ambrosia eye_type | ok. Six harvest lines match; chased DOI in the citation step. Pooled search found nothing. |
| c8:16 | Calyptocarpus sense_light_nonvisual | ok. My searches (C. vialis germination light against dark; horseherb shade and light intensity; straggler daisy germination and photoperiod) returned care pages, Flora of North America, and germination trials on Calotropis procera (magiran 881991, page opened) and wetland Carex; no Calyptocarpus trial. Main already holds a search record for this cell (harvest-18), so this record duplicates one. |
| c8:1 | Albizia eye_type | ok. Pooled Fabaceae focusing search returned PMC9824129 (plant ocelli) and the FIU paper; nothing on Albizia. |
| c8:17 | Lorinseria eye_type | ok. Pooled fern focusing search found nothing on Lorinseria. |
| c8:22 | Nuttallanthus diel | ok. My searches returned the UW-Eau Claire Putnam Park note on N. canadensis (page opened: bloom months only), the USGS plant ID page and Texas toadflax notes; no daily opening time. |
| c8:11 | Bignonia eye_type | ok. Pooled search returned a Bignoniaceae anatomy record; no focusing work. |
| c8:7 | Nephrolepis eye_type | ok. Pooled fern search found nothing. |
| c8:15 | Calyptocarpus eye_type | ok. Duplicates the main record of 16 October; nothing found. |
| c9:4 | Triodanis diel | **error**. Hilty, Illinois Wildflowers, "Venus' Looking Glass" (illinoiswildflowers.info/prairie/plantx/venusx.htm, page opened) says of Triodanis perfoliata: "When it is sunny, the flowers open up during the morning, and remain open for the rest of the day." A daily opening time for a species of the genus, of the descriptive kind main logs for chicory and Ipomopsis; my common-name search returned it on the first page. The record's three screened works and Patel 2014 (ECU thesis on delayed selfing, page opened: daily checks of opening, no hour) hold no such statement. |
| c8:18 | Lorinseria diel | ok. A fern has no flowers; my searches (spore release time of day; the anthesis pair) returned care and DNR pages; no daily rhythm. |
| c8:12 | Bignonia diel | ok. My searches returned anthesis hours for Bignoniaceae of other genera: Pyrostegia venusta 06:00 to 07:30 (Singh, Chauhan, Galetto 2009, CONICET record opened), Arrabidaea brachypoda and A. samydoides from 06:00 (Yanagizawa and Maimoni-Rodella 2007, SciELO page opened), which POWO places in Fridericia (pages opened), Anemopaegma chamberlaynii (Lundiana) and Tabebuia pulcherrima (Biotemas). None is Bignonia in the current sense. |
| c8:5 | Baccharis eye_type | ok. Pooled search returned an Embrapa Baccharis anatomy PDF; no focusing claim in its snippet. |
| c8:9 | Aesculus eye_type | ok. Pooled search found nothing. |
| c8:20 | Osmundastrum diel | ok. My searches returned Wikipedia, the Duke Osmunda phylogeny PDF and garden pages; no daily rhythm. |
| c8:8 | Medicago eye_type | ok. Duplicates the main record of 16 October; the 1989 and 1996 epidermal-optics works are screened with the owner's wording. |
| c6:1 | Succisa eye_type | ok. 11 harvest lines match; the tool lists no candidate. Pooled search found nothing. |
| c8:19 | Osmundastrum eye_type | ok. Spore phototropism works correctly sent to sense_light_nonvisual. |

## Verdicts, extension (11)

| File:line | Record | Verdict |
|---|---|---|
| c9:5 | Triodanis eye_type | ok. Pooled searches found no focusing work. |
| c8:23 | Melilotus eye_type | ok. Chased DOI in the Fabaceae review; nothing found. |
| c8:3 | Diospyros eye_type | ok. Harvest lines match; both citation steps printed; a pooled search returned a Nigerian Diospyros leaf-epidermis survey (UNILAG record) with no optics. |
| c4:1 | Pilea eye_type | ok. Harvest lines present in order (the family review sits after the live queries); citation DOI printed. Nothing found. |
| c9:6 | Triodanis sense_chemical | ok. My searches (the gibberellin, smoke or dormancy search; a T. perfoliata dormancy and GA3 search; a jasmonate and volatile search) returned a Themeda thesis (UKZN, page opened), a Coreopsis after-ripening abstract (wildflower.org, page opened) and maize volatile work; no Triodanis response. An Annales Botanici Fennici smoke paper did not load. |
| c8:13 | Platanus eye_type | ok. Nothing found. |
| c8:6 | Morella diel; eye_type | ok. My searches returned PhytoKeys figure pages and corn pollen emission work; no Morella daily timing. |
| c8:4 | Rubus eye_type | ok. Nothing found. |
| c8:21 | Nuttallanthus eye_type | ok. Nothing found. |
| c9:3 | Phoradendron eye_type | ok. Nothing found. |
| c8:14 | Euonymus eye_type | ok. `chased` names the Celastraceae review it screened. Pooled search returned a Chinese Euonymus leaf-epidermis survey; no optics. |

## Errors and rate

Erroneous record, to be dropped: **harvest-c9 line 4** (Triodanis diel).

First draw: 1 of 20, 5.0%, undecided. First draw with the 11-record extension (the whole unit): 1 of 31, 3.2%. The unit is under 5% and passes. If the desk will not take a naturalist's web description as a diel row, the count falls to 0 of 31 and the verdict stands.

Pooled with the desk's earlier audits of desk-screen units (audits 43 to 51, 55 to 73 and 75 to 78, 13 in 724; audit 79, 7 in 35; audit 80 at its desk ruling, 0 in 35; audit 81, 9 in 35; audit 82, 3 in 35; audits 81 and 82 ran together and each pooled without the other): 33 in 895, 3.7%.

## Forks and notes, not counted

- Unlabelled queries. Most records hold OpenAlex API queries that Codex ran itself, mixed with the harvest's lines and carrying no "web: " prefix. Point 7 names only harvest queries and web searches. If the desk reads these as queries that differ, nearly every record of the unit fails on that ground alone; I followed audit 39, which noted additions without counting them. A label such as "openalex: " would settle it.
- Duplicates. Calyptocarpus eye_type and sense_light_nonvisual (c8:15, c8:16) and Medicago eye_type (c8:8) already have search records on main (harvest-18, sweep-19), which is why `harvest_get.py` no longer lists those traits as open.
- Triodanis sense_light_nonvisual is already on main (oa-7:459 to 460), as the c9 records say.

## Wanted lines checked against pages I opened

- harvest-c8:20, Rismona et al., HAYATI J Biosci 33(2): 278-287, 10.4308/hjb.33.2.278-287 (journal page opened): DOI and title right; year 2025 matches the online date, while the issue is labelled March 2026. The page names seven authors and the line leaves the field empty.
- harvest-c9:216, Koch and Kennedy 1980, Plant Physiol 65(2): 193-197, 10.1104/pp.65.2.193 (PMC440296 opened): DOI and year right; the page names the authors and the line leaves them empty. The line asks for diurnal acid and gas exchange, which audit 82's reading (CAM gas exchange does not count for diel) would keep from the diel cell.
- harvest-c8:146 (Euonymus fungus-gnat paper, 10.1093/aob/mcad081): the PMC page went unanswered, so it is unchecked.
- No other wanted line matched a page I opened. No wanted-line fault found.

## Blocked pages

- pmc.ncbi.nlm.nih.gov PMC6108335 and PMC10583214 (permission requests unanswered; not retried).
- bioone.org Annales Botanici Fennici 61(1) smoke paper (bot check).

No ResearchGate, academia.edu, Sci-Hub, LibGen or library proxy page was opened, and no paper text is committed.
