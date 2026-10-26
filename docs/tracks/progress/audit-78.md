# Audit 78: rescreen-2 (branch research/rescreen-2, head f38108ae)

Gate: `screen_candidates.py --check` on the 28 search records and 6 wanted lines prints "0 problems".

## Sample (seed 78)

The audit covers the whole unit, so the sample is all 28 search records. `random.seed(78)` over lines 1 to 28 gives the order 27, 7, 4, 10, 22, 9, 14, 2, 5, 13, 28, 16, 19, 23, 1, 26, 12, 3, 6, 18, 25, 8, 17, 21, 20, 15, 11, 24.

## Method

Judged against desk-screen.md, point 10 included, with the owner's readings of 25 October 2026: plant sense_chemical counts a living plant responding to a chemical or airborne cue and a living plant giving off volatiles as a signal, and excludes extracts, distilled oils and chemical treatments of cut flowers; plant eye_type is "none" for every plant, with epidermal focusing logged under sense_light_nonvisual; a lamp-spectrum activity comparison is behaviour and does not count under spectral_range_nm, while light-trap catch tables still do. For the scope of "a living plant responding to a chemical cue" I followed main's own evidence, which logs hormone and elicitor responses of living plants under sense_chemical: oa-13b:473 (methyl jasmonate on hydroponic Scutellaria baicalensis roots), oa-13b:474 (yeast extract and methyl jasmonate on aeroponic Valeriana jatamansi) and an ethylene treatment of Zanthoxylum bungeanum.

`harvest_get.py` and `screen_candidates.py` were run for all 22 genera. A script compared each record's non-web `queries` with the harvest's query and family-review lines: all 28 match word for word and in order, zero-hit queries and the two supplement-run-20 epidermal queries included (Iris has no harvest run and its records hold web searches only, as they say). Every candidate the tool lists for each record's trait is in `screened`. Every DOI named in `chased` (Tussilago, Lunaria, Parnassius) is printed in the harvest's citation step; the other `chased` fields are none-reasons the harvest output supports (no citation step printed for that trait, or no harvest run). I read the screened entries against the harvest abstract starts (three per record, or all where fewer) and found none that reports a measurement of the trait.

Duplicates on main: no record duplicates a desk-era record (harvest, desk, plant, replant, rescreen or oa units) for the same taxon and trait. Every cell except Parnassius cff_hz and corner_hz carries an older sweep record (sweep-6 to sweep-52), and the queue still lists those cells as open, so the new records add to them without doubling a desk-protocol record. No record's trait has evidence on main for its genus.

Point 10 checks. (a) The four plant-1 sense_chemical records and Chelone, Lunaria and Comarum sense_chemical put every extract, oil, food-aroma and cut-flower work in `screened` with the right reason; I found no living-response work wrongly screened out. (b) The twelve eye_type records screen every lens or epidermis candidate as no plant eye, and the Chelone record gives the Antirrhineae petal-cell work the owner's wording. (c) Colostygia names Briolat et al. 2026 as behaviour and canon-22 in `canon`. The reading was applied correctly in what the records hold; the three errors below are living-response measurements outside the harvest that the records missed.

I ran 43 WebSearches (of 60) and opened 16 pages my searches returned. Two fetches went unanswered or failed and were not retried (listed below). No ResearchGate, academia.edu, Sci-Hub, LibGen or library proxy page was opened (a proxy-mirror MDPI result, 0-www-mdpi-com.brum.beds.ac.uk, was left closed, as was a saludcastillayleon.es mirror of BMC Plant Biology), and no paper text is committed.

## Verdicts

| Line | Record | Verdict |
|---|---|---|
| 1 | Tussilago sense_chemical | ok. Queries match (7 harvest, 2 web); chased DOI in the harvest. The screened extract thesis, deodorized-extract paper and Farfarae flos volatile profile are tissue chemistry, as their abstracts show. My searches (herbivore-induced volatiles, coltsfoot floral scent, methyl jasmonate or salicylic acid) returned general reviews and other species; no Tussilago response found. |
| 2 | Stellaria sense_chemical | **error**. Emery et al. 1994, "Phenotypic plasticity of stem elongation in 2 ecotypes of Stellaria longipes: the role of ethylene and response to wind", Plant, Cell and Environment 17(6): 691-700 (Bologna ACNP index page; DOI not shown): in alpine plants ethylene from ethephon or ambient exposure inhibited stem growth, low ethephon stimulated prairie plants, and silver thiosulphate restored growth under wind in alpine plants. A living congener responding to an airborne hormone, the kind of row main logs under sense_chemical. Kathiresan's 1997 Calgary thesis on ethylene and plasticity in S. longipes is a further lead. The donor-only allelopathy papers (Stellaria extracts on radish) do not count for Stellaria. |
| 3 | Dipsacus sense_chemical | **error**. Xu et al. 2022, "Transcriptome analysis reveals that jasmonic acid biosynthesis and signaling is associated with the biosynthesis of asperosaponin VI in Dipsacus asperoides", Frontiers in Plant Science 13: 1022075, 10.3389/fpls.2022.1022075 (Frontiers PDF opened): two-leaf seedlings grown in half-strength MS solution were treated with MeJA, and root asperosaponin VI rose significantly by day 5, with triterpenoid and JA genes up at 6 h. The same response as main's oa-13b:473. The harvest also prints a 2025 BMC Plant Biology paper on DaERF9 and JA signalling in D. asper (10.1186/s12870-025-06576-w), which the tool did not list for the trait. |
| 4 | Digitalis sense_chemical | **error**. Pérez-Alonso et al. 2014, "Estimulación de cardenólidos en brotes de Digitalis purpurea L. cultivados in vitro mediante elicitores", Revista Colombiana de Biotecnología 16(1): 51-61, 10.15446/rev.colomb.biote.v16n1.44225 (journal page opened): MeJA at 80 and 100 µM raised digoxin and digitoxin in in-vitro shoot cultures, chitosan and SilioPlant also raised cardenolides, and MeJA reduced biomass. A Kurdistan study of 3β-HSD expression under MeJA and salicylic acid in D. nervosa is a further lead (year and journal not shown). One fork stays open: if the owner reads an in-vitro shoot culture as tissue taken from the plant, this verdict becomes ok. The two cut-flower ethylene trials are correctly screened under 10(a). |
| 5 | Cynoglossum eye_type | ok. Queries match (13, 2 web). My focusing search returned the general leaf-optics review (PMC8309337), Bone et al. 1985 (FIU) and the asknature page; no Cynoglossum focusing work. |
| 6 | Lunaria eye_type | ok. Queries match. My search returned the same leaf-optics pages and a solar-cell biomimicry paper; no Lunaria focusing work. |
| 7 | Pastinaca eye_type | ok. Queries match. Same generic leaf-optics results. |
| 8 | Raphanus eye_type | ok. Queries match. Same generic results and a Merriam-Webster entry. |
| 9 | Scutellaria eye_type | ok. Queries match (13, 2 web); the onion-epidermis enzyme paper is correctly screened. My search returned generic leaf-optics pages. |
| 10 | Thlaspi eye_type | ok. Queries match. Same search as line 9; nothing on Thlaspi. |
| 11 | Valeriana eye_type | ok. Queries match. Generic results and the Selaginella silica-body paper. |
| 12 | Asparagus eye_type | ok. Queries match. Same search as line 11; nothing on Asparagus. |
| 13 | Botrypus eye_type | ok. Queries match. Generic results; no fern focusing work in the genus. |
| 14 | Heliotropium eye_type | ok. Queries match. Plant-ocelli review, Selaginella silica bodies, Bone et al.; nothing on Heliotropium. |
| 15 | Phalaris eye_type | ok. Queries match. Same search as line 14. |
| 16 | Chelone eye_type | ok. Queries match; Antirrhineae petal-cell item carries the owner's wording. Same search as line 14. |
| 17 | Chelone sense_chemical | ok, with a fork. Queries match. Bowers, Boockvar and Collinge 1993 (J Chem Ecol 19: 815-823, Springer page opened) is as the record says: leaf iridoids by GC and no difference between damaged and undamaged plants. Whether herbivore damage counts as a "chemical cue" under 10(a) is not settled by the reading; main's wanted lists hold herbivory-induction lines for Raphanus and Thlaspi under sense_chemical, which leans the other way. I count nothing on it. My other searches (turtlehead scent; induced defence with Euphydryas phaeton) found no Chelone response; the Muchoney et al. Dryad dataset measures caterpillars, and PubMed 35342612 was a bot check. |
| 18 | Colostygia spectral_range_nm | ok. Queries match (6, 2 web). My lamp search returned Infusino et al. 2017 (no Colostygia in the abstract; the record names it as the open lead) and Niermann and Brehm 2022 (10.14411/eje.2022.004), which main already read in oa-13c and logged pooled over 161 species, with no per-species table. My spectral search found no Colostygia measurement. |
| 19 | Iris acuity_cpd, interommatidial_deg | ok. Web-only queries, as the record explains. My search returned compound-eye mapping papers; none names Iris. |
| 20 | Iris cff_hz, corner_hz | ok. My search returned flicker papers on other taxa. |
| 21 | Iris lambda_max_nm, spectral_range_nm | ok. My search returned the mantis spectral-class paper already logged on main for other genera and a mantis-shrimp opsin preprint; a 2025 J Comp Physiol A page (10.1007/s00359-025-01776-z) failed to load and stays unread. |
| 22 | Scoparia acuity_cpd, interommatidial_deg | ok. Queries match (6, 3 web). My eye search returned the Paysandisia archon eye paper (no Scoparia). |
| 23 | Scoparia cff_hz, corner_hz | ok. My search returned the Lepidoptera flicker canon paper and a Ljubljana thesis on Triphosa dubitata (no Scoparia). |
| 24 | Scoparia lambda_max_nm | ok. Same searches; no Scoparia spectral measurement. |
| 25 | Parnassius cff_hz, corner_hz | ok. Queries match (5, 3 web), the "Parnasiinae vision review" now listed; both chased DOIs are in the citation step. My search found only general photoreceptor-speed papers. |
| 26 | Aquarius cff_hz, corner_hz | ok. Queries match (6, 3 web). My two searches found no water-strider flicker or photoreceptor-speed value. |
| 27 | Lunaria sense_chemical | ok. Queries match (11, 2 web); chased DOI in the harvest. Radish, collard, horseradish and caper chemistry correctly screened under 10(a). My searches (scent and herbivory; jasmonate or ethylene) found no Lunaria response. |
| 28 | Comarum sense_chemical | ok. Queries match (13, 2 web). My searches found no Comarum scent or elicitor work; a UCLouvain repository download on floral volatiles and pollinators was not opened and is an unread lead. |

Errors: 3 of 28, 10.7%. If the owner reads the in-vitro shoots of line 4 as tissue taken from the plant, 2 of 28, 7.1%. Either way the unit is above 5%. Pooled with audits 43 to 51, 55 to 73 and 75 to 77 (10 errors in 696 records): 13 in 724, 1.8%.

Because the audit covers the whole unit, the desk can drop the error records and merge the rest: **drop lines 2, 3 and 4** of docs/views/searched/rescreen-2.jsonl (Stellaria, Dipsacus and Digitalis sense_chemical); the 25 other records stand. The three cells then wait for the papers above on a wanted list.

## Wanted lines (listed, not counted)

All 6 lines leave `authors` empty, so none is counted. None duplicates a DOI on main's wanted, evidence or sources files.
- Line 1 (10.1021/jf00048a054, Medicago 1994): a title search returned other alfalfa-weevil papers (Doss and Johnson 1991, J Chem Ecol 17(3): 535-542, a different work), so the DOI and year stay unconfirmed.
- Line 6 (10.1111/eea.13334, Cynoglossum): a title search did not return the article itself. It did return Park's 2017 Idaho dissertation on olfactory and visual cues in host finding by Mogulones borraginis, which identifies electrophysiologically active volatiles, two sesquiterpenes found only in Cynoglossum officinale, and shows weevils telling the host by scent. That is a measurement of volatiles a living Cynoglossum gives off as a signal, a stronger lead for the reopened Cynoglossum sense_chemical cell than line 6.
- Lines 2 to 5 were not checked against a page.

## Notes for the desk

- Main's replant-1 wanted lines 3 (Lunaria seed glucosinolates) and 59 (Comarum ultrasound extraction) still sit on main as sense_chemical lines; records 27 and 28 say the reading frees those cells. They should be dropped from main or re-tagged when rescreen-2 merges.
- Hormone and elicitor responses: main logs them under sense_chemical, and the screen's word list does not catch "jasmonate", "ethylene" or "elicitor" in titles like these. The three errors all came from that gap, so the other reopened plant sense_chemical cells may need one more search aimed at elicitor or hormone treatments.

## Blocked pages

- pmc.ncbi.nlm.nih.gov PMC8654843 (permission not answered; not retried). Mann et al. 2021, Sci Rep 11: 23698, 10.1038/s41598-021-02801-2 (pherobase record), compares volatiles of 14 cultivated plants; the species were not seen.
- link.springer.com 10.1007/s00359-025-01776-z (client error).
- pmc.ncbi.nlm.nih.gov PMC9928152 and pubmed 35342612 (bot checks); the Frontiers PDF served Xu et al. 2022.
