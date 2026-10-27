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

### Actaea — web screening finished; protocol partial

Ran harvest_get.py and screen_candidates.py: in no harvest run. Canon catalog/effective main evidence, prior wanted and owner statuses checked: no existing genus coverage/request for these leads. Exact queries, in execution order; returned titles/displayed passages screened, no page fetch:
- `web: Actaea seed germination light dark`
- `web: Actaea germination gibberellin OR smoke OR dormancy`
- `web: Actaea floral scent volatiles`
- `web: "Actaea" flower opening time anthesis`
- `web: "baneberry" flower opening time anthesis`
- `web: "Actaea" eye type epidermal lens cells`
- `web: "baneberry" eye type epidermal lens cells`
- `web: ("Actaea" OR "Cimicifuga") light perception phototropism germination`
- `web: "baneberry" light perception phototropism germination`
- `web: ("Actaea" OR "Cimicifuga") chemical signalling volatile response`
- `web: "baneberry" chemical signalling volatile response`
- `web: Ranunculaceae photoreceptor review`

Added four wanted lines: the Actaea racemosa light/dark germination and seedling-development experiment; the 1984 A. spicata fragrance/pollinator study; floral/vegetative volatiles comparison across Actaea species (sampling/species unresolved); and the A. erythrocarpa flower-opening study. For the last, expanded the already returned PMC search-result passage to read the observation protocol: flowers were observed at multiple daytime clock hours and hourly at anthesis. It is a genuine timing lead, not flowering-season text. No page was opened to expand this passage. Year 0 means not supplied; no missing metadata was guessed. The eye pair mainly returned the common name doll's eyes and berry pigmentation, not eyes; owner plant-none reading applies. Light pair also included older Cimicifuga spelling. Pharmaceutical effects of tissue extracts do not count as plant chemical responses. Family query returned general plant-photoreceptor reviews and other ranunculaceous genera; none was assigned to Actaea. OpenAlex skipped; all three plausible-measurement traits held and no null eye row written.

Cumulative counts: 7 genera web-screened, 0 full protocol complete, 0 searched rows, 10 wanted lines, 0 evidence rows. Remaining 33 unreviewed, next Lathyrus.

### Lathyrus — web screening finished; protocol partial

Ran harvest_get.py and screen_candidates.py. Adopted main light-response evidence, including GBIF accepted-name Lathyrus oleraceus rows formerly filed as Pisum sativum, and chemical receiver evidence canon-3:674 for L. japonicus. These already cover both light and chemical traits, so did not duplicate paired trait searches or add requests for germination/scent studies that bear only on those covered traits. No earlier wanted line found. Canon catalog/effective main evidence checked. Harvest query order, copied verbatim:
- `Lathyrus phytochrome photoreceptor`
- `Lathyrus light perception`
- `Lathyrus phototropism`
- `Lathyrus volatile signalling`
- citation harvest: works citing `10.3389/fpls.2015.00207` naming Lathyrus (1 result); `10.1111/ele.12205` (0); `10.1111/j.1744-7909.2007.00392.x` (0).
- family review harvest: `Fabaceae photoreceptor review`.

Exact web queries in order; returned titles/displayed passages screened, no page fetch:
- `web: Lathyrus seed germination light dark`
- `web: Lathyrus germination gibberellin OR smoke OR dormancy`
- `web: Lathyrus floral scent volatiles`
- `web: "Lathyrus" flower opening time anthesis`
- `web: "sweet pea" flower opening time anthesis`
- `web: "Lathyrus" eye type epidermal lens cells`
- `web: "sweet pea" eye type epidermal lens cells`

The germination-first search directly recovered light/dark studies in L. latifolius and L. aphaca, plus a smoke-solution study in L. sativus. Adopted the existing trait coverage rather than requesting more papers for it. Likewise the scent studies (10.1093/pcp/pcaa100; 10.3390/plants13233272) bear on existing chemical coverage; cut-flower ethylene work does not count under owner point 10(a). The remaining diel search returned flowering seasons, plant developmental dates and a Bruchus/L. latifolius interaction paper whose displayed passage describes insect day/night visits and flower age in days, not measured plant anthesis clock hours; the full source remains unresolved at https://horizon.documentation.ird.fr/exl-doc/pleins_textes/divers20-07/31763.pdf and was not screened as proof of absence. Main's photoperiod evidence was not relabelled as diel. The eye pair returned petal/leaf epidermal taxonomic microscopy, not image-forming organs; any focusing belongs under nonvisual light and the owner plant-none reading applies. Of the three harvest diel candidates, 10.1104/pp.84.2.318 measures Melilotus, 10.1093/aobpla/plac041 measures Swartzia, and 10.1111/j.1365-294x.2006.03051.x is a broad phytochrome review with no Lathyrus daily-timing measurement in the supplied abstract. Harvest eye candidate list was empty. OpenAlex supplements skipped; no null rows.

Cumulative counts: 8 genera web-screened (Mycelis, Dryopteris, Clintonia, Dicentra, Struthiopteris, Centranthus, Actaea, Lathyrus), 0 full protocol complete, 0 searched rows, 10 wanted lines, 0 evidence rows. Remaining 32 unreviewed; exact next genus Ornithogalum. Stopped between genera at the context checkpoint; all work committed. Required OpenAlex supplements/citation steps remain skipped, and wanted sources await oa reading.

### Worker 9 continuation — 2026-10-27

Adopted Worker 4's eight finished web screens and ten wanted lines without repeating their queries. Read required protocols and audits; supported network policy is enforced/unrestricted, VPN false, no credentials configured. Used cloud-environment-runtime skill; kept inherited proxy/TLS settings. OpenAlex remains skipped following the coordinator's HTTP 429 budget refusal. No page/paper fetching, evidence writing or null searched rows.

### Ornithogalum — web screening finished; protocol partial

Ran harvest_get.py and screen_candidates.py. Checked canon/evidence/wanted and owner-status files for new lead identifiers. Existing sweep-20:5–6 light/diel rows are Wikipedia-based; left untouched under the no-legacy-repair instruction and told coordinator. Current tool opens eye_type and sense_chemical. Plant eye_type follows owner none reading, with focusing assigned to nonvisual light.

Harvest queries in order: `Ornithogalum phytochrome photoreceptor`; `Ornithogalum light perception`; `Ornithogalum phototropism`; supplement `Ornithogalum volatile signalling`; `Ornithogalum epidermal lens cells`; `Ornithogalum epidermal focusing leaf optics`; family review `Asparagaceae photoreceptor review`. No citation harvest listed. Screened supplied harvest titles/abstract starts and the returned web titles/passages, up to twenty delivered per query; no claim of twenty where fewer were supplied.

Exact web queries in execution order:
- `web: Ornithogalum seed germination light dark`
- `web: Ornithogalum germination gibberellin OR smoke OR dormancy`
- `web: Ornithogalum floral scent volatiles`
- `web: "Ornithogalum" eye type epidermal lens cells`
- `web: "star of Bethlehem" eye type epidermal lens cells`
- `web: "Ornithogalum" chemical signalling volatile response`
- `web: "star of Bethlehem" chemical signalling volatile response`
- `web: Asparagaceae photoreceptor review`

Four wanted leads added: named O. arabicum dormancy/germination study, the living-cultivar vernalization/PGR trial, the Ornithogalum flowering/PGR title, and GA-linked O. umbellatum fruit epidermal growth. Species/culture details and absent metadata remain for source reading. The bulb NMR dormancy abstract uses storage temperature, not a demonstrated light/chemical manipulation; no chemical null is inferred. Cut-spike calcium/ethylene gravitropism and phenylalanine-induced fragrance of cut flowers are excluded by 10(a). Extract polysaccharides, OSW-1 cancer pharmacology and tissue metabolomics concern removed tissue/animal responses, not living plant sensing. Eye results concern ovary cuticles, lipotubuloids and taxonomic leaf anatomy, not image-forming organs; unrelated Gagea, Hippobroma, Episcia and astronomical Star-of-Bethlehem results do not cover this genus. Family web review results were broad plant/algal photoreceptor reviews rather than a direct Ornithogalum measurement. Harvest chemical candidates 10.21273/hortsci.35.3.406a (cut apples), the Origanum thesis and Eucomis LED cultures concern other taxa; aromatic-volatiles Viewpoint and nectar review did not identify a direct Ornithogalum measurement in the displayed passages. Held chemical for reading; OpenAlex supplement/citation protocol incomplete, so zero null rows.

Worker 9 counts: 1 new genus web-screened, 0 full-protocol complete, 0 searched, 4 wanted added, 0 evidence. Cumulative 9 web-screened, 14 wanted; remaining 31, exact next Phlox.

### Phlox — web screening finished; protocol partial

Ran harvest_get.py and screen_candidates.py; checked canon catalog, effective main evidence, wanted lists and owner status. Adopted sweep-14:4 light-response evidence and existing sweep-14 primary-photoperiod request. Existing Andersson et al. 2002 butterfly-floral-scent request (sweep-20) is adopted for Phlox too; no duplicate request. Harvest queries in order: `Phlox phytochrome photoreceptor`; `Phlox light perception`; `Phlox phototropism`; supplement `Phlox photoperiod`; `Phlox circadian rhythm`; family `Polemoniaceae photoreceptor review`. No harvest citation step listed.

Exact web queries, executed in order; screened delivered titles and snippets/passages only, no pages fetched:
- `web: Phlox seed germination light dark`
- `web: Phlox germination gibberellin OR smoke OR dormancy`
- `web: Phlox floral scent volatiles`
- `web: "Phlox" flower opening time anthesis`
- `web: "garden phlox" flower opening time anthesis`
- `web: "Phlox" eye type epidermal lens cells`
- `web: "garden phlox" eye type epidermal lens cells`
- `web: "Phlox" chemical signalling volatile response`
- `web: "garden phlox" chemical signalling volatile response`
- `web: Polemoniaceae photoreceptor review`

Six wanted lines added: GA/light germination of P. pilosa, P. drummondii growth regulators, multispecies Phlox scent divergence, P. subulata volatile pathways, daily light-reversible petal colours, and in-vitro Phlox propagation (culture fork for desk). Existing genus light coverage avoids repeating paired light searches. The germination-first search additionally located The role of light during Phlox drummondii Hook. seed germination, a light-only study within adopted coverage. ResearchGate-only Timing is Everything: Temporal Variation in Floral Scent, and its Connections to Pollinator Behavior and Female Reproductive Success in Phlox divaricata remains an unresolved title lead; no DOI/year/authors obtained there and no host opened. The ant-repellence title surfaced via a secondary bibliography, not an opened primary source, so exact publisher metadata remains for oa readers.

Diel pair otherwise returned seasons and flower longevity in days, not daily anthesis hours. Eye matches are floral pigment eyes/cultivar names (including Red Eyes), taxonomic cytology and non-Phlox pollinator eyes; owner none reading applies. Harvest 10.1093/jxb/eru327 is a general opening review without a Phlox timing result in its supplied abstract; RHODOPSIN7 is Drosophila, linalool review centres on Clarkia, diurnal VOC result is Ficus, scent variation result is Lilium, and cut Narcissus is both another genus and harvested material. Cut Phlox NO/ethylene/1-MCP studies are excluded under 10(a); culture propagation remains explicitly uncertain rather than screened out. Web PhLOX/Phlox2 oxylipin results are red-algal enzymes, not genus Phlox. Family search returned general plant/algal photoreceptor reviews and Polemoniaceae phylogenetics; no direct new Phlox measurement. OpenAlex skipped and no null rows.

Worker 9 counts: 2 new genera web-screened, 0 full protocol complete, 0 searched, 10 wanted added, 0 evidence. Cumulative 10 web-screened, 20 wanted; remaining 30, exact next Solidago.

### Solidago — web screening finished; protocol partial

Ran harvest_get.py and screen_candidates.py. Checked canon catalog/effective main evidence, earlier wanted and owner status. Adopted existing chemical receiver evidence canon-3:668, recheck-17-fixed:4, recheck-quotes-3-fixed:166 and sweep-5:10 plus harvest-29 request for Insect Herbivory Selects for Volatile-Mediated Plant-Plant Communication; did not repeat paired chemical searches or request more chemical-only sources. Current light/diel/eye traits remain open.

Harvest query order: `Solidago phytochrome photoreceptor`; `Solidago light perception`; `Solidago phototropism`; citation works citing `10.1111/ele.12205` naming Solidago (five supplied results); supplement `Solidago volatile signalling`; family review `Asteraceae photoreceptor review`. Screened supplied titles/abstract starts; web returned titles/snippets/passages only; no pages fetched.

Exact web queries, in execution order:
- `web: Solidago seed germination light dark`
- `web: Solidago germination gibberellin OR smoke OR dormancy`
- `web: Solidago floral scent volatiles`
- `web: "Solidago" flower opening time anthesis`
- `web: "goldenrod" flower opening time anthesis`
- `web: "Solidago" eye type epidermal lens cells`
- `web: "goldenrod" eye type epidermal lens cells`
- `web: "Solidago" light perception phototropism germination`
- `web: "goldenrod" light perception phototropism germination`
- `web: Asteraceae photoreceptor review`

Seven wanted lines added for direct light/germination leads: S. chilensis germination behaviour, green-light sensitivity, comparative series parts 1 and 3, Brazilian arnica reproduction/photoblastism, growing-plant LED/shade-net experiment, and S. gigantea karrikin/dark germination. Adopted existing harvest-c18/c22b request for the Kansas shade thesis (10.58809/eiky9994), with no duplicate wanted line. Its related conference result at https://scholars.fhsu.edu/sacad/vol2018/iss2018/3/ names S. ulmifolia in controlled light fractions; full title and relationship to thesis remain unresolved for oa reading. Search results for S. gigantea hormone effects (10.1007/s11738-016-2179-6), floral emissions and gall-fly priming bear on adopted chemical coverage; no duplicate requests. The 1985 aspen-forest germination survey is an additional unresolved light lead at https://digitalcommons.usu.edu/aspen_bib/3847/; snippet names S. spathulata, but species-specific treatment contrasts require reading.

Anthesis pair returned flowering months, growing-degree phenology and flower-development dates, not clock hours. The anthochron harvest review concerns development/thermal time; no daily anthesis result was assigned to Solidago. Eye results describe taxonomic epidermis/oil glands or medicinal effects on animal eyes; owner plant-none rule applies. Broad family review gave general plant/algal photoreceptors and crop flowering reviews. Harvest light candidates in maize, spinach, Phaseolus, Halophila, white clover, Potamogeton, Cryptocoryne and Arabidopsis do not measure Solidago; they do not support a null while direct genus light leads wait. Extract antinociception and isolated diterpenoids are removed-tissue chemistry under 10(a). OpenAlex skipped; no null rows and no evidence.

Worker 9 counts: 3 new genera web-screened, 0 full protocol complete, 0 searched, 17 wanted added, 0 evidence. Cumulative 11 web-screened, 27 wanted; remaining 29, exact next Gleditsia.

### Gleditsia — web screening finished; protocol partial

Ran harvest_get.py and screen_candidates.py. Checked canon catalog/effective evidence, earlier wanted and owner status; no genus evidence/request found for these direct leads. Harvest uses GBIF Fabaceae with blank order; no taxonomy edits. Harvest query order: `Gleditsia phytochrome photoreceptor`; `Gleditsia light perception`; `Gleditsia phototropism`; supplements `Gleditsia flower opening time`; `Gleditsia nyctinasty`; `Gleditsia volatile signalling`; `Gleditsia photoperiod`; `Gleditsia circadian rhythm`; `Gleditsia anthesis`; `Gleditsia pollination biology`; `Gleditsia epidermal lens cells`; `Gleditsia epidermal focusing leaf optics`; family review `Fabaceae photoreceptor review`. No citation harvest listed. Screened supplied title/abstract starts and web titles/snippets/passages, no paper/page fetch.

Exact web queries, in execution order:
- `web: Gleditsia seed germination light dark`
- `web: Gleditsia germination gibberellin OR smoke OR dormancy`
- `web: Gleditsia floral scent volatiles`
- `web: "Gleditsia" flower opening time anthesis`
- `web: "honey locust" flower opening time anthesis`
- `web: "Gleditsia" eye type epidermal lens cells`
- `web: "honey locust" eye type epidermal lens cells`
- `web: "Gleditsia" light perception phototropism germination`
- `web: "honey locust" light perception phototropism germination`
- `web: "Gleditsia" chemical signalling volatile response`
- `web: "honey locust" chemical signalling volatile response`
- `web: Fabaceae photoreceptor review`

Eleven wanted lines added: seed local adaptation/light experiment; shade/nitrogen seedling experiment; observed flower opening/pollen study; nyctinastic Gleditsia/turgorines paper; circadian root flux study; nocturnal tree movement (species fork); GA/sugar dormancy study; living hormone-treatment/reference-gene paper; short-day bud dormancy study; seedling intensity study; and elevational-invasion germination/light experiment. Clock-time results, response comparisons and preparation/species forks remain for oa readers; no measurements invented. Root-flux preparation has severed shoots but living roots, explicitly held for desk. Extracted turgorines alone are not assigned to chemical sensing.

Additional unresolved light leads returned: Effects of shading on growth and biochemical characteristics of Gleditsia sinensis seedlings (https://www.sciopen.com/article/10.14067/j.cnki.1673-923x.2024.08.008) and the G. sinensis light-quality/intensity thesis (https://www.globethesis.com/?t=2543306815465164); the latter is only a third-party thesis listing, so original institution/author/year need verification. Seed coat colour, water-entry and dormancy/scarification results need physical-versus-physiological mechanism assessment; no chemical measurement is inferred from acid/coat disruption. Harvest salt-stress (10.1038/s41598-026-68202-5) and low-P tolerance (10.1038/s41598-024-82071-w) are additional living chemical-response leads; existing direct hormone/nitrogen candidates already hold that trait for reading.

Anthesis pair mostly returned flowering months or hours since opening, but the direct G. sinensis flower-observation study was retained. Other harvest diel candidates measure Chrysanthemum, Aeschynanthus, apple, bean, muskmelon, raspberry, lily, peach, Macadamia, Melilotus and Swartzia, not Gleditsia. Eye searches describe the seed-coat lens/strophiole and cotyledon areoles, not optical focusing/image-forming organs; owner none reading applies. Dry-eye drug inserts concern animal eyes. Volatile oil administered to rats, steamed-seed flavour profiles, methanol-extracted insect phagostimulants and saponin pharmacology are tissue chemistry/animal responses under 10(a). Gall-midge sex pheromone measures an insect, not its host tree. Family review returned legume photoperiodic regulation/phylogenetics without a Gleditsia experiment in the displayed passages. The 0-academic-oup-com.legcat.gov.ns.ca proxy result was left unopened. OpenAlex skipped; no null search records or evidence.

Worker 9 counts: 4 new genera web-screened (Ornithogalum, Phlox, Solidago, Gleditsia), 0 full protocol complete, 0 searched rows, 28 wanted added, 0 evidence. Cumulative 12 web-screened and 38 wanted lines. Remaining 28 genuinely unreviewed genera; exact next Cakile. Stopped between entries at context checkpoint; existing first eight screens and ten wanted preserved. OpenAlex supplements/citation work remains skipped for the round and source reading remains with the oa job.

## 2026-10-27 — issue38 worker 48 continuation

### Cakile — web screening finished; protocol partial

Checked canon catalog, global evidence/wanted/searched, owner status and actual queue species/traits. Harvest currently calls only chemical open, but the actual queue also has C. maritima light/diel/eye; no congener physiological carry was adopted. C. edentula kin evidence oa-10:130–131 and harvest-19:2 leaves chemical-cue mechanism unresolved; existing Bhatt request 10.1111/j.1469-8137.2010.03548.x adopted without duplication. Ran harvest_get.py and screen_candidates.py; read supplied 54 title/abstract starts. Harvest successful query order: `Cakile phytochrome photoreceptor`; `Cakile light perception`; `Cakile phototropism`; supplement `Cakile volatile signalling`. No citation/family step supplied.

Exact web queries in execution order:
- `web: Cakile seed germination light dark`
- `web: Cakile germination gibberellin OR smoke OR dormancy`
- `web: Cakile floral scent volatiles`
- `web: "Cakile" chemical signalling volatile response`
- `web: "sea rocket" chemical signalling volatile response`
- `web: Brassicaceae photoreceptor review`
- `web: "Cakile" flower opening time anthesis`
- `web: "sea rocket" flower opening time anthesis`
- `web: "Cakile" eye type epidermal lens cells`
- `web: "sea rocket" eye type epidermal lens cells`
- `web: "Cakile" light perception phototropism germination`
- `web: "sea rocket" light perception phototropism germination`

Screened returned titles/snippets/passages as delivered, fewer than 20 per individual query; no paper/page opened. One combined tool display was truncated, so no claim that every underlying returned passage was visible. Nine wanted leads added: Mediterranean germination light/salinity, British biological flora GA/light, halopriming, maritime photoinhibition, C. edentula provenance/light, systemic wounding signalling (cue-mechanism fork), hormone-treated calli (culture fork), nutrient/kin thesis, and after-ripening/stratification germination (fixed-darkness/physical-dormancy fork). Germination and salt studies directly cover C. maritima; congener leads retain their own species. An additional heterotrophic-to-autotrophic C. maritima seedling-transition study appeared in the light pair, but title/complete primary metadata were not retained in the truncated display and it remains unresolved rather than a fabricated wanted record.

Anthesis results chiefly give seasons, weeks from emergence and morphology, not daily opening hours. Eye hits describe epidermal anatomy/cutin or seed tissues; owner plant-none reading applies, with optical focusing reserved for light. Extract pharmacology/molecular docking, antibacterial extracts and rat/cancer-cell assays are removed-tissue/animal effects excluded under 10(a). Harvest light experiments in Arabidopsis, Beta, Cymodocea, Portulaca, Erysimum and Glechoma are other genera; review titles do not prove Cakile-specific measurements. Family search returned Brassicaceae floral phytochrome plasticity and general phytochrome reviews without a displayed Cakile experiment. No physiological carry from family/congener. OpenAlex skipped following round-wide 429; no null searched rows or evidence.

Worker 48 running counts: 1 new genus web-screened, 0 full protocol complete, 0 searched, 9 wanted, 0 evidence. Cumulative batch 13 web-screened and 47 wanted; 27 remain, exact next Clinopodium.

### Clinopodium — web screening finished; protocol partial

Ran harvest_get.py and screen_candidates.py: not in any harvest run, hence no successful harvest queries/candidates to copy. Checked global canon/evidence/wanted/searched, owner status, and queue C. vulgare separately across all four traits; no same-species evidence found. Adopted harvest-c18 request for Influence of Some Physicochemical Treatments to Stimulate Seed Germination of Agrimonia eupatoria L. and Clinopodium vulgare L.; its displayed result explicitly compares C. vulgare potassium nitrate and GA3 responses, though the earlier request lists Agrimonia as beneficiary. No duplicate request; oa reader should retain both species.

Exact web queries in execution order:
- `web: Clinopodium seed germination light dark`
- `web: Clinopodium germination gibberellin OR smoke OR dormancy`
- `web: Clinopodium floral scent volatiles`
- `web: "Clinopodium" flower opening time anthesis`
- `web: "wild basil" flower opening time anthesis`
- `web: "Clinopodium" eye type epidermal lens cells`
- `web: "wild basil" eye type epidermal lens cells`
- `web: "Clinopodium" light perception phototropism germination`
- `web: "wild basil" light perception phototropism germination`
- `web: "Clinopodium" chemical signalling volatile response`
- `web: "wild basil" chemical signalling volatile response`
- `web: Lamiaceae photoreceptor review`

Screened returned titles/snippets/passages as delivered (not an asserted 20 per query). Six wanted lines added for C. odorum GA3, C. sandalioticum germination, C. mexicanum germination, C. rouyanum biogenic defence emissions (living-versus-oil fork), C. pulegium carbon-source effects (culture fork), and C. macrostemum stress-explant effects (culture/treatment fork). Congener physiology is not carried to C. vulgare. Additional unresolved lead: Volatile Organic Constituents of Clinopodium gilliesii (Benth.) Kuntze: Analysis by HS-SPME and classic hydrodistillation, https://revistas.sena.edu.co/index.php/recia/article/view/351 ; the displayed title alone does not establish living-plant emission or a response.

Diel hits give flowering months or bud counts, not opening clock hours. Eye hits describe taxonomic epidermis/stomata/trichomes and naked-eye microscopy; none displayed optical focusing, and owner none rule applies. Wild basil also returned Ocimum gratissimum, O. basilicum and O. campechianum; these are other genera and do not provide Clinopodium trait coverage. Cheminopodium/Chenopodium germination and Conopodium scent are likewise spelling/taxon mismatches. Essential oils, alcoholates, extract effects on neutrophils and pharmacology review are removed-tissue/animal work excluded under 10(a). Family review search returned general photoreceptor and medicinal-light reviews, with displayed measurements in Salvia, Scutellaria and other genera; no Clinopodium-specific result adopted. OpenAlex skipped; no null rows, evidence or fetched pages.

Worker 48 running counts: 2 new genera web-screened, 0 full protocol complete, 0 searched, 15 wanted added, 0 evidence. Cumulative batch 14 web-screened and 53 wanted; 26 remain, exact next Hylocomium.
