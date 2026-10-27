# Audit 82: harvest-c22b (branch research/harvest-c22b, head d5808544)

Gate: `screen_candidates.py --check` on the 35 search records and 25 wanted lines prints "0 problems".

## Sample (seed 82)

`random.seed(82)` and `random.sample(lines, 20)` over the 35 search record lines (1-based) give, in draw order, 10, 32, 33, 19, 27, 26, 6, 30, 29, 22, 9, 31, 2, 14, 16, 34, 4, 7, 35 and 5. The draw was made before any record was read; the same call on the numbers 1 to 35 gives the same positions.

The sample found errors, so the desk's 15-record extension ran: `random.seed(8215)` and `random.sample(<the 15 undrawn line numbers in ascending order>, 15)` draw 12, 28, 3, 25, 15, 18, 20, 13, 24, 23, 17, 21, 11, 8 and 1. The two draws cover the whole unit.

## Method

Judged against desk-audit.md and desk-screen.md, point 10 (a) to (e) included, with the readings the launch prompt gives: plant sense_chemical counts living responses, responses to applied hormones or elicitors included, and volatile signalling; extracts, oils, hairy-root cultures and cut-flower or excised-tissue chemistry do not count; plant diel means flower opening and scent timing, and CAM gas exchange does not count; growth or germination trials under set light intensities count under sense_light_nonvisual; plant eye_type is "none" for every plant, with epidermal focusing logged under sense_light_nonvisual. Nereocystis and Egregia, the two kelps, are judged by the same plant rules. Main logs light-for-germination responses under sense_light_nonvisual (Cochemiea grahamii seeds needing light, audit 79), so a light-against-dark germination trial counts there.

`harvest_get.py` was run on main for the 13 genera of the first draw. Reseda, Polygonum and Arctotheca are in harvest run 7, and Eurybia, Isocoma and Cystopteris in run 3; a script compared each record's non-web `queries` with the harvest's `query` and `family review` lines, and all eight drawn records of these six genera match word for word and in order (11 or 13 lines, supplement-run queries included), each followed by its labelled web searches. Anchusa, Sphaeralcea, Scirpus, Huperzia, Egregia, Nereocystis and Onopordum are in no harvest run, and their records hold web searches only, as they say. No harvest shows a failed ("gave up") step. Every DOI named in `chased` is printed in the harvest's citation step (10.1016/j.tree.2009.09.010 for Reseda and Arctotheca, 10.3390/plants11233212 for Polygonum); Eurybia, Isocoma and Cystopteris print no citation step, and the web-only genera have no harvest run, so their none-reasons hold. I read the screened entries against the harvest's titles and abstract starts (three per record, or all where fewer) and found none that reports a measurement of the trait. Three records hold a single web search (Scirpus sense_chemical, Sphaeralcea and Anchusa sense_light_nonvisual); point 10(e) names one search per plant trait plus the scent search, so I note the count and do not count it.

The WebSearch ration was 60, shared with another audit. I ran one to three searches per substantive record, aimed at hormone, elicitor and germination trials, light and shade trials, opening hours and spore release, and three pooled focusing searches for the eight eye_type records of each draw. Only pages my own searches returned were opened.

## Verdicts (sample of 20, seed 82)

| Line | Record | Verdict |
|---|---|---|
| 10 | Reseda eye_type | ok. Queries match (11 harvest, 2 web); chased DOI in the citation step; the one candidate, a Gaziantep dye-plant survey, is correctly screened. My pooled focusing searches returned the FIU lens-cell paper (cas_bio/44), "Algal Optics" (arXiv 2506.15214), the AskNature page and a 1907 Nature item; nothing on Reseda. |
| 32 | Anchusa sense_chemical | ok. Web-only. My searches ("Anchusa officinalis methyl jasmonate OR salicylic acid"; "Anchusa flowers headspace volatiles bees") returned a Lithospermum officinale shikonin study (Sci Rep 2022, another genus), a Calendula methyl jasmonate study (Modares J Biotechnol 1(1), 2010, page opened), Lukas et al. 2019 on pear flowers (Chemoecology 29(5): 211-223, page opened) and Dekebo et al. 2022 on nine Korean bee plants (J Ecol Environ 46(1), AGRIS page opened); no Anchusa response or headspace study. |
| 33 | Anchusa sense_light_nonvisual | **error**. van Breemen AMM 1984, "Comparative germination ecology of three short-lived monocarpic Boraginaceae", Acta Botanica Neerlandica 33(3): 283-305 (natuurtijdschriften.nl page opened): germination of Cynoglossum officinale, Echium vulgare and Anchusa arvensis was studied under light in controlled environments, and the abstract states for A. arvensis that "the light response proved to be different for seeds from different populations". POWO (page opened) accepts Anchusa arvensis (L.) M.Bieb., with Lycopsis arvensis a synonym. A germination response to light in a species of the genus, the kind of row main logs; the record's one search returned garden pages. |
| 19 | Eurybia sense_chemical | ok. Queries match (13, 2 web); the 1892 perfume book and the two riodinid-butterfly papers are correctly screened. My searches (Eurybia macrophylla with allelopathy, herbivory, jasmonate or volatiles; big-leaved aster with gibberellin or induced defence) returned Solidago, Arabidopsis and Aster ericoides (Symphyotrichum) work; no Eurybia. |
| 27 | Cystopteris eye_type | ok. Queries match (13, 2 web); the 1922 nursery catalogue is correctly screened. My pooled focusing searches found nothing on Cystopteris. |
| 26 | Onopordum eye_type | ok. Web-only. My pooled searches found nothing on Onopordum. |
| 6 | Scirpus eye_type | ok. Web-only. My sedge focusing search returned a Turkish Cyperaceae anatomy PDF, Pakistani and Indonesian anatomy papers and the FIU lens-cell paper; no Scirpus focusing work. |
| 30 | Sphaeralcea sense_light_nonvisual | ok, with a lead. Web-only. My searches returned a vegetable-seedling shading study (Formisano et al. 2022, Front Plant Sci 13: 890830, page opened; no Sphaeralcea) and the Fire Effects Information System page on S. grossulariifolia (page opened), which says "Seeds germinate equally well in light and in darkness" and cites its references [2, 38] by number; the reference list did not load, so the primary work is unnamed. A review sentence with unnamed sources and no values is a lead (see Leads); I count nothing on it. |
| 29 | Sphaeralcea sense_chemical | **error**. Kildisheva OA, Dumroese RK, Davis AS 2011, "Overcoming dormancy and enhancing germination of Sphaeralcea munroana seeds", HortScience 46(12): 1672-1676 (USDA Forest Service RMRS PDF opened; DOI not shown): stored seeds were soaked in 100 ppm GA3 for 24 or 48 h, alone or after scarification, and germination was scored; GA3 alone gave about 15%, the same as the untreated control (15.9%), and the authors state that exogenous gibberellin failed to enhance germination. A living hormone response measured (a null response is still a measurement), of the kind audit 79 counted (Liatris gibberellin soak). The record's generic jasmonate search returned patents and reviews. A 2019 ASHS abstract on GA3 and excised S. coccinea embryos (ashs.confex.com Paper30854, page opened) reports no results and treats excised tissue. |
| 22 | Isocoma diel | ok. Queries match (13, 2 web); the blue-light review is correctly screened. My search returned extension and plant-guide pages on I. pluriflora and goldenbushes; no opening hour. |
| 9 | Reseda diel | ok. Queries match (11, 2 web); the wheat, maize and bindweed works are correctly screened. My search (Reseda odorata scent emission timing) returned the floral-scent circadian review (Front Plant Sci 2016, ETH record opened; Petunia and Nicotiana) and rose scent work; no Reseda timing. |
| 31 | Anchusa eye_type | ok. Web-only. My pooled search returned the A. officinalis floral-structure study (pbsociety aa/1641), which the unit already holds for diel; by title it is floral anatomy, and nothing on epidermal focusing. |
| 2 | Nereocystis eye_type | ok. Web-only. My kelp focusing search returned kelp natural-history pages and "Algal Optics"; nothing on Nereocystis. |
| 14 | Polygonum eye_type | ok. Queries match (11, 2 web); chased DOI in the citation step; the five screened animal and human eye works are correctly screened. Nothing on Polygonum focusing. |
| 16 | Arctotheca sense_chemical | ok. Queries match (11, 2 web); the Croton trichome paper and the blue-light review are correctly screened. My searches (capeweed germination with smoke, gibberellin, nitrate or karrikin; capeweed volatiles or hormone treatment) returned an apricot smoke study (DOAJ, opened), Nelson et al. 2009 on Arabidopsis (UTAS record, opened) and volatile-signalling reviews; no Arctotheca. |
| 34 | Egregia diel | ok. Web-only. My searches (Egregia spore release timing; feather boa kelp zoospore release periodicity) returned the fungal spore paper, the Friday Harbor Egregia life-cycle pages and a review of kelp zoospore release protocols (Dryad); no daily rhythm in Egregia. |
| 4 | Scirpus diel | ok. Web-only. My search returned anthesis papers on other plants and Desai et al. 2018 on Setaria (see Wanted lines); no Scirpus opening hour. |
| 7 | Huperzia sense_chemical | ok, with a fork. Web-only. My searches returned Yang et al. 2021, "In Vitro Propagation, Huperzine A Content and Antioxidant Activity of Three Genotypic Huperzia serrata", Plants 10(6): 1112, 10.3390/plants10061112 (MDPI page opened): stem explants, callus and thallus cultured on media with NAA, IAA, ZT and 2,4-D, with regeneration and a 164-fold biomass gain on 1.0 mg/L NAA. These are explant and callus cultures, tissue taken from the plant, which the readings in force exclude; if the owner reads explant regeneration under auxin as a living response, this verdict becomes an error. A Huperzia selago prothallus-culture paper (PMC7397083) did not open. |
| 35 | Egregia eye_type | ok. Web-only. Same kelp search as line 2; nothing on Egregia. |
| 5 | Scirpus sense_chemical | ok. Web-only. My searches returned hormone teaching pages, Larson 1997 on six wetland Cyperaceae (Field Station Bulletin 30(1): 1-9, MINDS page opened; S. atrovirens and S. cyperinus under storage and temperature, no chemical) and Thullen and Eberts 1995 on Scirpus acutus (Wetlands 15: 298-304, Conservation Evidence page opened; chilling and scarification, no chemical, and the species now sits in Schoenoplectus). |

Errors in the sample: 2 of 20, 10.0% (lines 29 and 33).

## Verdicts (extension of 15, seed 8215)

All 15 drawn records' non-web `queries` match the harvest word for word and in order (Coreopsis 13, Eurybia 13, Isocoma 13, Honckenya 13, Polygonum 11, Reseda 11, Arctotheca 11 lines), or hold web searches only where the genus is in no harvest run (Croton, Onopordum, Sphaeralcea, Huperzia, Nereocystis). Coreopsis prints two citation steps and its record names the first DOI; Honckenya prints none.

| Line | Record | Verdict |
|---|---|---|
| 12 | Coreopsis eye_type | ok. Queries match (13, 2 web); chased DOI in the citation step. The retinopathy extract paper, the petal-patterning review (with the owner's wording) and the lutein review are correctly screened. My pooled petal-focusing search returned the conical-petal-cell reviews and the MIXTA origin paper (PMC9467652); nothing on Coreopsis. |
| 28 | Sphaeralcea eye_type | ok. Web-only; the same pooled search found nothing on Sphaeralcea. |
| 3 | Croton eye_type | ok. Web-only; nothing on Croton focusing in my pooled searches. |
| 25 | Onopordum diel | ok. Web-only. My search (Onopordum acanthium capitulum opening time) returned Wikipedia, the Cambridge Botanic Garden, RHS and New Zealand flora pages and two Gonzaga pollinator-repository records; no opening hour. |
| 15 | Arctotheca eye_type | ok. Queries match (11, 2 web); the stamen-collar anatomy, oak trichome, Croton trichome and lutein works are correctly screened. |
| 18 | Eurybia eye_type | ok. Queries match; the lutein review is correctly screened. |
| 20 | Honckenya diel | ok. Queries match (13, 2 web); the marula, phytochrome, flower-opening review and moth works are correctly screened by their abstract starts. My search returned the New Jersey heritage sheet on H. peploides var. robusta, Frier et al. 2016 on Haskap (J Pollination Ecol 19(11): 81-87, page opened; no Honckenya) and a Rhodora 114(958) paper on the seasonal growth of H. peploides, whose title is seasonal, not daily; no opening hour. |
| 13 | Polygonum diel | ok. Queries match (11, 2 web); chased DOI in the citation step; the eleven screened works (embryo-sac "Polygonum type", days-after-anthesis counts, other genera) are correctly screened. My search returned Pladias factsheets, flora pages and a UMBS working paper on Polygala paucifolia (Deep Blue page opened); no Polygonum opening hour. |
| 24 | Isocoma sense_chemical | ok. Queries match (13, 2 web); the gall-wasp, Stephanodoria, Andean-gradient and ice-core works are correctly screened. My search returned Friedjung et al. 2013 on desert allelochemicals (PLoS ONE 8(12): e81580, pherobase page opened; Origanum and Artemisia) and herbivory pages; no Isocoma. |
| 23 | Isocoma eye_type | ok. Queries match; the lutein review is correctly screened. |
| 17 | Eurybia diel | ok. Queries match (13, 2 web); the herbarium image, Byrsonima, hawk-moth and blue-light works are correctly screened. My search returned genus and garden pages and the COSEWIC report on E. divaricata (not opened); no opening hour. |
| 21 | Honckenya eye_type | ok. Queries match; the tool lists no candidate and none was found. |
| 11 | Reseda sense_chemical | ok. Queries match (11, 2 web); chased DOI in the citation step; all 13 candidates are screened, the constituents review and pollen chemistry under 10(a). My searches returned Antonova-Nedeltcheva et al. 2025, "Volatile Compounds Profiling of Fresh R. alba L. Blossom", Molecules 30: 3102, 10.3390/molecules30153102 (MDPI page opened), which is Rosa alba with picked blossoms, and Arabidopsis hormone cross-talk theses; no Reseda response or living-flower headspace. |
| 8 | Huperzia eye_type | ok. Web-only; nothing on Huperzia focusing in my pooled searches. |
| 1 | Nereocystis diel | **error**, with a fork. Amsler CD and Neushul M 1989, "Diel periodicity of spore release from the kelp Nereocystis luetkeana (Mertens) Postels et Ruprecht", J Exp Mar Biol Ecol 134: 117-127, as reference 2 of Deiman, Iken and Konar 2012 (ALGAE 27(2), KoreaScience page opened) gives it; Ulaski and Konar 2021 (ALGAE 36(2): 147-154, 10.4490/algae.2021.36.5.10, KoreaScience page opened) cites it too. The record chose spore release as the kelp's timed event and searched for exactly these words; its own results held the KoreaScience item JAKO202126758278416 (Ulaski and Konar), which it left unjudged. Fork: a kelp has no flowers, and the plant rule names flower opening and scent timing; if the owner reads a kelp's diel cell as closed to spore release, this verdict becomes ok. Spore release is a reproductive release event and differs from the CAM gas exchange that audit 80's desk ruling called metabolism, so I count it. |

Errors in the extension: 1 of 15 (line 1).

## Counts

Errors: 3 of 35, 8.6% (sample of 20: 2 errors, 10.0%; lines 29 and 33). If the owner settles the kelp fork of line 1 against the record's finder, 2 of 35, 5.7%; if he also reads Yang et al. 2021 (line 7) as a living auxin response, 3 of 35 again. On every reading the unit is above 5% and fails. Pooled with the desk's earlier audits of desk-screen units (audits 43 to 51, 55 to 73 and 75 to 80, 20 errors in 794 records once audit 80's two errors are withdrawn by the desk ruling of 27 October; audit 80 pooled without audit 79): 23 in 829, 2.8%. Counting audit 80's two as written, 25 in 829, 3.0%.

The two draws cover the whole unit, so the desk can drop the error records and merge the rest: **drop lines 1, 29 and 33** of docs/views/searched/harvest-c22b.jsonl (Nereocystis diel, Sphaeralcea sense_chemical, Anchusa sense_light_nonvisual). The 32 other records stand. The three cells then wait for the works above on a wanted list.

Pattern. Both counted plant errors are germination trials, a gibberellin soak and a light-against-dark test, and both were missed because the point 10(e) phrasing ("jasmonate OR elicitor OR hormone response"; "light intensity OR shade OR photoperiod growth") returns jasmonate reviews and garden pages for small genera; my searches with "seed germination" in them found both on the first page. Three of the unit's records ran a single web search for their trait. The kelp error is a result the record's own search returned and left unread, a cost of judging untitled results by title without opening them.

## Wanted lines (listed, not counted)

All 25 lines leave `authors` empty, so none is counted. Checked against pages my searches returned:
- Line 1 (10.2307/1543327): Maier I, Hertweck C, Boland W, The Biological Bulletin 201(2): 121-125, 2001 (University of Chicago Press page). The line carries year 0, which can be filled; the page names no kelp species.
- Line 2 (10.1515/znc-1984-0629): "Lamoxirene: Structural Proof of the Spermatozoid Releasing and Attracting Pheromone of Laminariales", Z Naturforsch 39c: 689-691, 1984 (De Gruyter PDF; the fetch renders the first author as "Mamer FJ", with Müller B and Jaenicke L). The paper reports the pheromone identical across "six different Laminariales" without naming them and describes no bioassay, so by itself it cannot fill a Nereocystis or Egregia cell.
- Line 13 (10.3389/fpls.2018.01585): Desai JS, Slabaugh E, Liebelt DJ and others, "Neural Net Classification Combined With Movement Analysis to Evaluate Setaria viridis as a Model System for Time of Day of Anther Appearance", Front Plant Sci 9: 1585, 2018 (Frontiers PDF). Only Setaria accessions are measured, so the line holds the Arctotheca diel cell on a paper that cannot fill it; the same holds for harvest-c22's lines on this DOI.
- Line 24 (BYU etd/8074): Jefferies JAM 1972, "A revision of the genus Sphaeralcea (Malvaceae) for the state of Utah", MS thesis (ScholarsArchive page). A taxonomic revision whose abstract gives no opening time; a weak hold on the Sphaeralcea diel cell.
- Line 25: Chwil M and Weryszko-Chmielewska E, Acta Agrobotanica 62(1): 37-47, 10.5586/aa.2009.005 (AGRIS record, which gives 2013; the DOI points to 2009). The line has year 0 and no DOI. The abstract treats floral micromorphology and gives no timing or scent.
- Lines 7 and 18: searches for the DOIs returned other Frontiers items, so both stay unconfirmed. The other lines were not checked against a page.

## Leads

- Sphaeralcea sense_light_nonvisual: the Fire Effects Information System page on S. grossulariifolia says seeds germinate equally well in light and in darkness, citing its references 2 and 38, whose entries did not load. The primary work behind it would be a measurement for the genus.
- Sphaeralcea sense_chemical: the 2019 ASHS abstract on GA3 and excised S. coccinea embryos (no results shown; excised tissue).
- Huperzia sense_chemical: Yang et al. 2021 (Plants 10(6): 1112), the fork under line 7; and the H. selago prothallus-culture paper PMC7397083, which did not open.

## Blocked pages

- pmc.ncbi.nlm.nih.gov PMC7397083 (permission not answered; not retried).
- journals.uair.arizona.edu JRM download 5401 (redirected to a publisher home page; not followed).

## Searches and pages

I ran 41 WebSearches (of 60) and opened 27 pages my own searches returned. No ResearchGate, academia.edu, Sci-Hub, LibGen or library proxy page was opened, and no paper text is committed.
