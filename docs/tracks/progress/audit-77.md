# Audit 77: plant-screen-1 (branch research/plant-screen-1, head 4e07f0c5)

Gate: `screen_candidates.py --check` on the 5 search records and 24 wanted lines prints "0 problems".

## Sample (seed 77)

The unit holds 5 search records, fewer than 20, so the sample is the whole unit. `random.seed(77)` over lines 1 to 5 gives the order 3, 5, 1, 4, 2.

## Method

Judged against desk-screen.md, point 10 included, with the owner's readings of 25 October 2026: plant sense_chemical counts living responses and volatile signalling only (no extracts, oils or cut-flower treatments); plant eye_type is "none" for every plant, and epidermal focusing is logged under sense_light_nonvisual; an activity comparison under lamps of different spectra is a behaviour finding and does not count under spectral_range_nm (no moth genus is in this unit). Under reading (b) an eye_type record cannot miss a measurement of eye_type itself, so for the four eye_type records step (d) looked for epidermal-focusing work in the genus, which would have to sit in `screened` with the owner's note if the harvest had listed it.

`harvest_get.py` was run for Tillandsia, Ardisia, Pleopeltis and Tradescantia. In every record the `queries` repeat the harvest's query lines and family review word for word and in order (zero-hit queries included), followed by the two labelled web searches. Each `chased` is a none-reason ("closest none"), and the harvest prints a citation step that returned 0 works naming the genus in all four genera, which supports it. Every candidate `screen_candidates.py` lists for the record's trait is in `screened`. I read the harvest abstract starts of the screened entries (three per record, or all where fewer). I ran 27 WebSearches in all (three per record, plus 12 for the lead and the wanted lines) and opened 6 pages my searches returned; one fetch went unanswered and was not retried. No ResearchGate, academia.edu, Sci-Hub, LibGen or library proxy page was opened, and no paper text is committed.

## Verdicts

| Line | Record | Verdict |
|---|---|---|
| 3 | Pleopeltis diel | ok. Queries match (13 harvest lines, 2 web). The one screened work, a 2006 Molecular Ecology review of phytochrome sensing, has no abstract in the harvest, and its title holds no daily timing in a Pleopeltis. My searches ("Pleopeltis flower opening time anthesis", "resurrection fern flower opening time anthesis") returned the same anthesis, Capsicum and fern natural-history pages the record lists. My third search (Pleopeltis polypodioides diurnal gas exchange) found a fern gas-exchange paper whose species list I could not open (see Leads); no Pleopeltis daily rhythm was found. |
| 5 | Tradescantia eye_type | ok. Queries match (9 harvest lines, 2 web). The screened turgor paper (Tradescantia virginiana water relations), the HortScience growth-regulator paper (the 'Angel Eyes' cultivar) and the pavement-cell survey hold no lens-like cells, as their abstracts show. My searches returned Bone, Lee and Norman 1985 (Applied Optics 24(10), FIU repository page opened), whose page names no genus, a leaf-optics review and the plant-ocelli review; no Tradescantia focusing work. |
| 1 | Tillandsia eye_type | ok. Queries match (9 harvest lines, 2 web). The Croton trichome paper, the 1916 freshwater textbook and the beech foliar-uptake paper hold no focusing, as their abstract starts show. My searches returned the plant-ocelli review, foliar anatomy of Tillandsia aeranthos (title only) and bromeliad trichome pages (Pierce et al. 2001 on the STRI site, title only); trichome reflectance is a different subject from epidermal focusing, and none is a Tillandsia focusing measurement. |
| 4 | Pleopeltis eye_type | ok. Queries match. The one screened work is the ogre-faced spider eye paper. My searches returned the plant-ocelli review, the camera-type eye paper on warnowiids, fern natural-history pages and a Selaginella micromorphology paper; no Pleopeltis focusing work. |
| 2 | Ardisia eye_type | ok. Queries match (13 harvest lines, 2 web). The food-packaging film (match inside "nanocellulose"), the foetal mouse melanopsin paper and the Selaginella blue-leaf paper hold no focusing in Ardisia, as their abstracts show. My searches returned Wikipedia and rainforest-plant pages, the plant-ocelli review and Bone et al. 1985 again; no Ardisia focusing work. |

Errors: 0 of 5, 0.0%. Pooled with audits 43 to 51, 55 to 73, 75 and 76 (10 errors in 691 records): 10 in 696, 1.4%. Under 5%, so plant-screen-1 passes. Lines to drop: none.

## Wanted lines (listed, not counted)

All 24 lines leave `authors` empty; the desk fills them from the registry. The pages I opened supply these, for the registry to match:

- Line 1 (10.3390/metabo11090594): Lo M-M, Benfodda Z, Bénimélis D, Fontaine J-X, Molinié R, Meffre P; Metabolites 11(9): 594, 2021 (MDPI page). Year and DOI agree. The page says the flowers were harvested from nursery plants and sealed in vials before headspace sampling, so they were excised. Under reading 10(a) the emission of tissue taken from the plant does not count, and the line's sense_chemical "why" overstates the work; line 2, from the same series, likely shares the method (its page was not opened).
- Line 3 (10.32854/agrop.v16i1.2442): García-Granados Brian I, Valdez-Hernández EF, Rodríguez-De la O JL, Juárez-Hernández MJ, Flores-Cruz M; 2023, vol. 16(1) by the DOI (Agro Productividad page). One factor is light against dark, as the line says.
- Line 11 (10.1038/s41598-017-10975-x): Vivaldo G, Masi E, Taiti C, Caldarelli G, Mancuso S; Scientific Reports 7, 2017 (University of Florence repository page). The page does not list the 109 species, so whether Liquidambar is among them is unchecked.
- Line 12 (10.3390/agronomy13071747): Midzi J, Jeffery DW, Baumann U, Capone DL, Rogiers SY, Pagay V; Agronomy 13(7): 1747, 2023 (MDPI page).
- Line 20 (New Phytologist 1971): two title searches returned no page for the paper, so year, DOI and authors are unconfirmed.
- Lines 8 and 9 carry year 0 and no DOI; lines 4, 5, 8 and 9 have no DOI.

No line duplicates a DOI or title in docs/views/wanted or docs/views/evidence on main.

## Leads

- "Light, rather than circadian rhythm, regulates gas exchange in ferns and lycophytes", Plant Physiology, 10.1093/plphys/kiad036, first author Daniela Aros Mualin (Plantae author profile dated 15 February 2023, opened). Its species list did not open (PMC10022864 fetch went unanswered). If it holds a Pleopeltis, it bears on a fern's diel cell only under one sense of diel: the desk's plant diel words are flower opening, and a fern has no flowers. The owner has not read whether a daily gas-exchange rhythm closes a fern's diel cell; I leave that fork open and count nothing on it.

## Blocked pages

- pmc.ncbi.nlm.nih.gov PMC10022864 (permission not answered; not retried).
