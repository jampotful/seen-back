# harvest-c16 progress

## 2026-10-27

Worker 4, issue 38. Read AGENTS.md, codex-round.md, round4-harvest.md, all ten desk-screen points, THOROUGH.md, BRIEF.md Round 2, round3-sweep.md and audits 53/54. Main was fetched and the shared round branch selected by the coordinator. No branch switching, push, startup, build, evidence logging or page fetch. Used the cloud-environment-runtime skill to inspect supported network policy; no credentials or network settings changed.

OpenAlex is skipped for the remainder of the round: coordinator's first probe received HTTP 429, free IP daily budget exhausted. Missing OpenAlex scientific/common-name supplements and citation steps were not run. Therefore null search records are held entirely, as instructed by the coordinator. A web-screened genus below is partial protocol work, not an exhausted or complete-protocol genus. No paper text is saved. No owner n/a paper was re-requested.

### Mycelis — web screening finished; protocol partial

Ran harvest_get.py and screen_candidates.py. Screened harvest run 2 and supplemental runs 12/14 plus the Asteraceae family review. The current harvest target listed only sense_chemical, but the queue also has diel, eye_type and sense_light_nonvisual with no main evidence; older thin sweeps do not stand in for this screening. No earlier wanted line for Mycelis was found. Canon list and effective main evidence were checked; no Mycelis evidence found. Canon entries were not fetched or re-requested.

Harvest queries, copied verbatim in order:
- `Mycelis phytochrome photoreceptor`
- `Mycelis light perception`
- `Mycelis phototropism`
- `Mycelis volatile signalling`
- family review: `Asteraceae photoreceptor review`

Web queries, in execution order (titles and supplied snippets screened; no pages opened):
- `web: Mycelis seed germination light dark`
- `web: Mycelis germination gibberellin OR smoke OR dormancy`
- `web: Mycelis floral scent volatiles`
- `web: Mycelis flower opening time anthesis`
- `web: wall lettuce flower opening time anthesis`
- `web: Mycelis eye type epidermal lens cells`
- `web: wall lettuce eye type epidermal lens cells`
- `web: Mycelis light perception phototropism`
- `web: wall lettuce light perception phototropism`
- `web: Mycelis chemical signalling volatile response`
- `web: wall lettuce chemical signalling volatile response`
- `web: Asteraceae photoreceptor review`

The germination search returned the 1999 Journal of Ecology Mycelis species account with an explicit light-versus-darkness/colour germination result. Added one wanted line for sense_light_nonvisual and held that trait. Search results about Lactuca sativa, celery, fungi or other genera do not establish a Mycelis measurement. Daily flower-opening results for Mycelis were floristic flowering-season descriptions, not measured hours. No direct Mycelis chemical-response lead appeared. Plant eye_type follows the owner's none reading; epidermal focusing would belong to sense_light_nonvisual.

Chemical harvest candidates: 10.3390/toxins15010077 concerns Pseudomonas/Aspergillus on stored Coix; 10.3390/jof8111162 concerns Pinus/Suillus; 10.31976/0104-038321v280007 reviews Trichoderma volatiles; 10.3390/crops5050072 is a general blue-light floral-development review with no Mycelis measurement in its supplied abstract. None supplies a Mycelis chemical measurement. The blue-light/floral review supplies no Mycelis anthesis hours either. The harvested irradiance experiment 10.3389/fpls.2014.00012 names no species in the supplied abstract; the precise Mycelis account is the confirmed light lead to read first.

Counts this round: 1 genus web-screened, 0 full protocol complete, 0 searched rows, 1 wanted line, 0 evidence rows. Remaining: 39 genera unreviewed, next Dryopteris. OpenAlex supplements remain outstanding for Mycelis; source reading remains with the oa job.

### Dryopteris — web screening finished; protocol partial

Ran harvest_get.py and screen_candidates.py. Adopted main sense_light_nonvisual (harvest-18:1, recheck-17-fixed:6, recheck-25-fixed:1, sweep-5:16) and sense_chemical (oa-9:204–209, 289, 294, 298) coverage; did not repeat paired searches or request extra papers for those covered traits. No prior wanted lines found. Canon catalog/effective evidence checked. Harvest queries, verbatim:
- `Dryopteris phytochrome photoreceptor`
- `Dryopteris light perception`
- `Dryopteris phototropism`
- citation harvest: works citing `10.1007/BF00391162` that name Dryopteris (4 results screened).
- family review harvest: `Dryopteridaceae photoreceptor review` (13 results screened).

Web queries, in execution order:
- `web: Dryopteris seed germination light dark`
- `web: Dryopteris germination gibberellin OR smoke OR dormancy`
- `web: Dryopteris jasmonate herbivore`
- `web: "Dryopteris" flower opening time anthesis`
- `web: "wood fern" flower opening time anthesis`
- `web: "Dryopteris" eye type epidermal lens cells`
- `web: "wood fern" eye type epidermal lens cells`

Germination search returned multiple direct fern spore light studies and a Dryopteris fragrans methyl-jasmonate response study (10.1186/s12870-026-09723-z), but those traits already have main evidence and were adopted. The remaining diel pair returned nonflowering fern descriptions and seasonal growth, not a measured daily rhythm. The eye pair returned taxonomic epidermal anatomy (10.1016/j.micron.2018.05.008), not focusing; eye_type follows the owner's plant-none reading. Harvest diel candidate 10.1111/j.1365-294x.2006.03051.x is a general phytochrome review with no Dryopteris daily-timing measurement in the abstract; eye candidate 10.1038/s41598-022-22157-5 measures spider eyes, not fern eyes. Chemical candidates were not used to declare a null because main already holds measurements. No wanted line added. No pages fetched, including the proxy-host result returned for an unrelated Drosera paper. OpenAlex skipped; no null rows written.

Cumulative counts: 2 genera web-screened, 0 full protocol complete, 0 searched rows, 1 wanted line, 0 evidence rows. Remaining 38 unreviewed, next Clintonia.

### Clintonia — web screening finished; protocol partial

Ran harvest_get.py and screen_candidates.py: genus in no harvest run. Checked canon catalog/effective main evidence and prior wanted files: no genus evidence or prior wanted lines found. Screened returned titles and the displayed result passages; longer secondary-page text beyond the displayed passage was not reviewed. No page fetch. The scientific and common names were paired for all four open queue traits. Exact web queries, in order:
- `web: Clintonia seed germination light dark`
- `web: Clintonia germination gibberellin OR smoke OR dormancy`
- `web: Clintonia floral scent volatiles`
- `web: "Clintonia" flower opening time anthesis`
- `web: "bluebead lily" flower opening time anthesis`
- `web: "Clintonia" eye type epidermal lens cells`
- `web: "bluebead lily" eye type epidermal lens cells`
- `web: "Clintonia" light perception phototropism germination`
- `web: "bluebead lily" light perception phototropism germination`
- `web: "Clintonia" chemical signalling volatile response`
- `web: "bluebead lily" chemical signalling volatile response`
- `web: Liliaceae photoreceptor review`

Added the USDA species review (Meyer 2005) to wanted: its returned passage states a controlled sunlight/shade comparison and a day-length response of C. uniflora. The same result names the primary study Germination and growth of bird-dispersed plants: effects of seed size and light on seedling vigor and biomass allocation, attributed to Piper by the review; full bibliographic metadata remains to be read there. The germination searches also returned a C. udensis germination-time-course title on ResearchGate; that host was not opened or used to supply a DOI, author or year. Deno germination-book results named Clintonia but the supplied passage did not resolve its treatment/results. Those are remaining leads for the reader, not screened negatives. Fragrance/perfumery descriptions do not establish a measured living-plant signal; steroidal glycosides isolated from rhizomes and root extracts are tissue chemistry under owner point 10(a). Flower results give seasons, not anthesis hours; eye matches concern medicinal use or flora, not image-forming organs. Family-review results were broad plant-photoreceptor reviews (including the canon overview), not a Clintonia-specific measurement. OpenAlex required supplements/citation step skipped, so no null records.

Cumulative counts: 3 genera web-screened, 0 full protocol complete, 0 searched rows, 2 wanted lines, 0 evidence rows. Remaining 37 unreviewed, next Dicentra.

### Dicentra — web screening finished; protocol partial

Ran harvest_get.py and screen_candidates.py: in no harvest run. Checked canon catalog/effective main evidence and prior wanted: no genus evidence or prior wanted line. Exact queries, in order; only returned titles and displayed result passages screened, with no page fetch:
- `web: Dicentra seed germination light dark`
- `web: Dicentra germination gibberellin OR smoke OR dormancy`
- `web: Dicentra floral scent volatiles`
- `web: "Dicentra" flower opening time anthesis`
- `web: "Dutchman's breeches" flower opening time anthesis`
- `web: "Dicentra" eye type epidermal lens cells`
- `web: "Dutchman's breeches" eye type epidermal lens cells`
- `web: "Dicentra" light perception phototropism`
- `web: "Dutchman's breeches" light perception phototropism`
- `web: "Dicentra" chemical signalling volatile response`
- `web: "Dutchman's breeches" chemical signalling volatile response`
- `web: Papaveraceae photoreceptor review`

Added the publisher-title lead on supplemental irradiance and STS in potted Dicentra species. Its reader must resolve species identity; the title alone does not establish which current Dicentra species was measured. Year is 0 (unset), authors/journal/DOI empty because search did not supply them. The D. spectabilis GA3 and photoperiod leads concern a former Dicentra now named Lamprocapnos spectabilis (confirmed by University of Wisconsin/Vermont extension search snippets); they do not establish a measurement for current Dicentra. The Dicentra chrysantha smoke title appeared only at ResearchGate; that host was not opened or used to supply metadata. Germination-book snippets name Dicentra but do not identify a measured species or the experiment; retained as unresolved leads, not screened negatives. Dutchman's breeches also names Thamnosma texana in a Texas source, so its scent/toxicity results were excluded from Dicentra. Extract pharmacology/animal analgesic responses do not satisfy living-plant sense_chemical. Anthesis results were seasonal flowering descriptions. Papaveraceae review search returned Papaver colour/reflectance work and broad photoreceptor reviews, not a Dicentra measurement. Owner plant-eye-none reading applies. OpenAlex steps skipped; no null rows.

Cumulative counts: 4 genera web-screened, 0 full protocol complete, 0 searched rows, 3 wanted lines, 0 evidence rows. Remaining 36 unreviewed, next Struthiopteris.

### Struthiopteris — web screening finished; protocol partial

Ran harvest_get.py and screen_candidates.py: in no harvest run. Canon catalog, effective main evidence, earlier wanted and owner status checked, including Blechnum spicant spelling; no existing coverage/request located for the two leads. Exact web queries in order; returned titles/displayed passages screened, no page fetch:
- `web: Struthiopteris seed germination light dark`
- `web: Struthiopteris germination gibberellin OR smoke OR dormancy`
- `web: Struthiopteris jasmonate herbivore`
- `web: "Struthiopteris" flower opening time anthesis`
- `web: "deer fern" flower opening time anthesis`
- `web: "Struthiopteris" eye type epidermal lens cells`
- `web: "deer fern" eye type epidermal lens cells`
- `web: ("Struthiopteris" OR "Blechnum spicant") light perception phototropism`
- `web: "deer fern" light perception phototropism`
- `web: ("Struthiopteris" OR "Blechnum spicant") chemical signalling volatile response`
- `web: "deer fern" chemical signalling volatile response`
- `web: Blechnaceae photoreceptor review`

The first germination searches mostly matched the epithet in Matteuccia struthiopteris, which is a different genus and does not cover Struthiopteris. Added Blechnum spicant to the required scientific-name trait pair after the deer-fern results supplied that older spelling. This located the direct light-intensity productivity experiment (10.1186/s12870-024-04782-6) and antheridiogen response experiment (10.1002/pmic.201300166); both are wanted, and both traits are held. The light paper's explicit publication year was not displayed, so year 0 is an unset sentinel, not a date estimate. A fern-volatiles composition study (10.1177/1934578X1000501028) did not expose whether it sampled living emissions or tissue extracts; the direct antheridiogen receiver test is the confirmed chemical lead. A field-gametophyte thesis snippet says B. spicant spores are photoblastic; retained as another unresolved light lead at https://era.ed.ac.uk/server/api/core/bitstreams/f655297b-360f-4ea3-8be1-3e03b5a0caa9/content without inventing author/year. Diel results show nonflowering ferns/seasonal growth; eye results provide no image-forming organ, with plant eye_type none under owner rule. Family query returned broad reviews and other Blechnum species, not an additional direct current-genus source. OpenAlex skipped; no null rows.

Cumulative counts: 5 genera web-screened, 0 full protocol complete, 0 searched rows, 5 wanted lines, 0 evidence rows. Remaining 35 unreviewed, next Centranthus.

### Centranthus — web screening finished; protocol partial

Ran harvest_get.py and screen_candidates.py: in no harvest run. Checked canon catalog/effective main evidence. Adopted existing sweep-20 wanted request for Andersson et al. 2002 Floral scents in butterfly-pollinated plants: possible convergence in chemical composition, which already requests Centranthus ruber signal/scent timing. Did not duplicate it or repeat paired chemical searches. Exact web queries in order; returned titles/displayed passages screened, no page fetch:
- `web: Centranthus seed germination light dark`
- `web: Centranthus germination gibberellin OR smoke OR dormancy`
- `web: Centranthus floral scent volatiles`
- `web: "Centranthus" flower opening time anthesis`
- `web: "red valerian" flower opening time anthesis`
- `web: "Centranthus" eye type epidermal lens cells`
- `web: "red valerian" eye type epidermal lens cells`
- `web: "Centranthus" light perception phototropism germination`
- `web: "red valerian" light perception phototropism germination`
- `web: Caprifoliaceae photoreceptor review`

Added Mattana 2010 comparative Centranthus germination study (10.1111/j.1442-1984.2010.00280.x) under point 10(e); its light/dormancy methods remain for the reader. Germination-book search snippets concatenate neighboring entries, including C. occidentalis next to Centranthus: no result for that epithet was assigned to Centranthus. A later Deno snippet explicitly names C. ruber but exposes only germination timing, not its treatment comparison. A repository result names C. ruber in Germination ecology of wild living walls for sustainable vertical garden in urban… (https://arpi.unipi.it/retrieve/e0d6c92f-86aa-fcf8-e053-d805fe0aa794/Benvenuti%20et%20al%20Scientia%20Hortic%202016%20living%20walls%20postprint.pdf); exact full title and species-specific treatment results remain unresolved. A phototropism review result illustrates C. ruber inflorescences oriented toward the sun in Environmental and Experimental Botany 147 (2018) 75–85; retained as an additional unresolved lead at https://ri.conicet.gov.ar/bitstream/handle/11336/69645/CONICET_Digital_Nro.c2590fd0-0f92-4327-9691-2909c00bad31_A.pdf?isAllowed=n&sequence=2. These were not screened negatives. Essential-oil composition of harvested roots/aerial parts is tissue chemistry under owner point 10(a). Diel results provide seasonal flowering or developmental stages, not hours; existing scent paper remains wanted for timing. Epidermal spur anatomy does not describe a plant eye; owner none reading applies. Family review returned broad photoreceptor literature, not a direct new genus source. OpenAlex skipped; no null rows.

Cumulative counts: 6 genera web-screened, 0 full protocol complete, 0 searched rows, 6 wanted lines, 0 evidence rows. Remaining 34 unreviewed, next Actaea.
