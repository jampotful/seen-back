# Open-access pass, batch 1

2026-10-14. Resumed `research/oa-1` from commit `1553a5d`, after entry 11. This continuation completed entries 13, 17, 18, 25, 27 and 28 and read the full main article at entry 32. Stopped at that source boundary with entry 32’s raw supporting tables still inaccessible. The next untouched verified full copy is **entry 60, Slow or Fast Eyes**; first review the intervening entries’ access/abstract status in batch order. The unresolved discovery list remains below. No app setup, build, server, browser test or self-test ran.

## Counts

- **79 entries processed** in the original discovery script. This is not a claim that every provider successfully checked all entries.
- **35 entries with one or more advertised candidate-copy locations**; **18 source copies retrieved and identified**. This includes the newly recovered two-file supplement bundle at entry 25. Twelve entries are completed; entry 32 has only its main article completed; five retrieved copies are untouched.
- **12 batch entries completed**: 11 full articles and the standalone supplement bundle requested at entry 25. **5,069 records** reconcile with these twelve source-registry entries.
- **7 further abstracts with measurements logged**, contributing **50 abstract-only records** with `partial: true` and `access: abstract`.
- **38 main-article-only records** from entry 32 carry `partial: true` and `access: open`. The missing raw supporting tables prevent a completed source-registry entry; these records are separate from abstract evidence.
- **5,157 records total**, including **1,833 added in this continuation**. Six completed source entries and three evidence-bearing abstracts were added in this continuation, plus entry 32’s partial source coverage.
- **10 completed no-copy lookup verdicts**, unchanged in `docs/views/sources/oa-none-1.jsonl`. Four of these supplied abstract evidence. Advertised-but-blocked copies and interrupted searches were not converted to no-copy verdicts.
- **34 entries remain unresolved in discovery**. **17 other advertised candidate entries remain retrieval-blocked**, after recovering entry 25. Entry 32’s missing supplements are an additional limitation on an otherwise retrieved article.

## Discovery retry and access limits

The resumed retry script enforced at least **1.1 seconds between request start times** for OpenAlex and Semantic Scholar. The first OpenAlex retry, an exact-title search for entry 2, immediately returned HTTP 429. BRIEF requires stopping that provider after 429, so **no second OpenAlex request was sent in this session**; there is no observed spacing pair to report. All 34 unresolved entries remain unresolved. Previous lookup responses were preserved in the scratch audit trail; completed Europe PMC/Semantic Scholar results were reused. DOI-less records still require exact title, first author and year agreement; incomplete citations were not guessed.

The earlier session also encountered OpenAlex rate limiting and stopped further requests. Provider failures, unmatched identities, unavailable full copies and blocked advertised copies remain distinct.

Entry 25 was recovered through the public Figshare API and its returned ndownloader URLs. Both supplement PDFs were read, including the full data-source bibliography. The main mammal article itself remains unopened. Entry 30’s public Dryad metadata/file list was retrieved, but the first file-download endpoint returned 401; no login or credential workaround was attempted. Entry 19’s official PMC page returned HTTP 200 with only a recaptcha page; it was not treated as full text. Entry 32’s Birmingham repository holds the publisher PDF, while the publisher page returned 403; the repository lists no supporting-table files and a public Figshare resource-DOI search returned no entries.

## Completed sources

| Entry | Source | Records | Coverage and qualifications |
|---|---|---:|---|
| 3 | Katti et al., reptile photopigments | 89 | All 16 pages. Review-derived measurements name the review; original studies not opened. Native A2 and reconstituted A1 peaks, pooled species ranges and gene-versus-vision distinctions retained. |
| 4 | Kelber et al., animal colour vision | 306 | Publisher PDF from Lund repository, pp.81–118, tables and appendices. Table quotes checked against layout text; 12+ and ≥3 visually verified. Suggestive tests, estimates, taxon conflicts and cat/turtle contradictions qualified. |
| 6 | Cantlay et al., Anatidae visual fields | 1,156 | Full XML and all three Figshare supplements; 39 species. 195 descriptors, 921 signed field-margin separations, 39 eye-movement observations and one secondary visual-streak report. Eight vertical extents are lower bounds; blanks remain missing. |
| 7 | Nityananda & Read, stereopsis | 34 | Full XML, figures/captions and references. Behavioral evidence, neural responses and predictions distinguished. Unspecified taxa stay unspecified; owl distance predictions inferred; dragonfly temporal resolution not relabeled CFF. |
| 9 | Sondhi et al., Lepidoptera opsins | 809 | Full XML and all supplements, including all 175 Data1 entries/reference sheet. 699 recovery counts, 107 qualified diel classes, three secondary inventories. Zero recovery is not gene loss or color blindness; Crambus 2? and Eacles RH7 discrepancy retained. |
| 11 | Potier et al., owl visual fields | 898 | Full XML plus DOCX, S1 PDF and four-sheet XLSX. 43 species, 665 individual profile cells and 52 bill projections. Unmarked interpolations inferred. Ninox 54.5°/52° and Strix aluco 47°/48° source conflicts preserved; 180° posterior limit only an upper bound. |
| 13 | Mohun & Davies, amphibian photoreception | 99 | All 12 pages, Table1 and figures/references; no supplement cited. Review peaks retain life stages, A1/A2 and native/regenerated distinctions. Split Xenopus 4/45 read as 445 only with inference grade. Cynops green-rod table/text conflict retained. |
| 17 | Kopania & Clark, mammalian retinal specializations | 290 | Full XML, six supplement tables and four figures/references. 119 retinal features from 82 rows, 91 bony orbit angles, 78 estimated map coordinates and two secondary human densities. Measured-species columns override phylogeny labels. Chinchilla ambiguity, hybrid ferret and camel/other relative substitutions qualified. Published 2025, despite batch’s 2024 citation. |
| 18 | Caves et al., avian acuity | 374 | Full XML, all 17 supplement pages, main tables/figures. 94 S1 bird rows (caption says 93), 29 S2 vertebrates (caption says 28); two duplicated RGC values omitted. S1/S2 and method/citation conflicts retained. Dasyurus maculatus/hallucatus conflict remains at genus level. Fig.4 magpie 38.3 versus S1 33 flagged inferred. Published 2024, despite batch’s 2023 citation. |
| 25 | Veilleux & Kirk, mammal acuity supplements | 216 | Entire 14-page Table PDF and one-page Figure PDF. Only the requested supplement entry marked complete. 91 acuities, 91 axial lengths and 34 activity classes. Missing method/AP remains unknown. Eptesicus/Macrotus, primate and squirrel citation conflicts qualified; cone density differs from RGC; wallaby eye length was estimated. |
| 27 | Sharkey et al., beetle opsins | 260 | Full XML and all 11 supplement pages/seven tables. 231 recovery counts across 77 taxa, 26 categorical spectral bands, three prose records. Fragment asterisks retained; Xenos sequence/protein distinction and Agrilus S2/S3 disagreement qualified. Physiology assigned to measured taxa, not related genetic taxa. Dendroctonus experiment lacked UV stimuli. |
| 28 | Olsson et al., bird ocular UV transmission | 538 | Full XML, main tables/figures, eight supplement analysis tables, Figshare XLSX and figure PDF. 180 half-max thresholds, 152 ocular dimensions, 71 SWS1 states, 135 source-calculated UVA integrals. Normalized transmittance is not a hard spectral cutoff or receptor peak. Borrowed/uncertain SWS1 states graded accordingly. Quail raw curve crosses ~381 nm versus stated 350 nm; red-kite lens 404.8 exceeds text’s 400-nm ceiling. |

All read article copies are publisher versions, not accepted manuscripts (PDF version statement/format or XML manuscript metadata checked). New evidence cites the fetched versions. The entry-25 files are publisher-hosted supplements, not a claim to have opened the main article.

## Partial source coverage: entry 32

Read all 11 article pages plus repository cover, including figures/captions and bibliography. Logged **38 partial full-text records** from the visible main article: species-level/pooled field descriptors, bill directions, observed eye movements and qualified geometric head-pitch interpretations, including secondary skimmer comparisons. Gulls’ eyes were spontaneously fully converged during measurement. Pooled means stay with the three-species group; vertical binocular extents are not total vertical fields. Exclusive monocular sectors are not entire single-eye fields. Figure values were visually checked. Supporting Tables S1–S3 contain individual signed profiles, but were not retrieved or logged; no completed source entry was added.

## Abstract-only evidence

| Entry | Source | Records | Qualifications |
|---|---|---:|---|
| 5 | Tapetum comparative morphology | 17 | Selected-taxon categories; group reports not universal claims. |
| 10 | Honeybee temporal colour resolution | 8 | ~100Hz heterochromatic cutoff at optimal intensity ratios, not conventional achromatic CFF. Species unnamed in abstract. Inferred timing/channel ratios qualified. |
| 14 | Chick acuity and contrast | 4 | Age-dependent optokinetic acuity, peak contrast frequency and threshold. Species not named in abstract; advertised full copy remains blocked. |
| 19 | Dragonfly opsin diversity | 7 | Gene counts for unnamed Libellulidae species and other surveyed Odonata. Not receptor-class counts or demonstrated colour vision. |
| 21 | Walking-bird head bobbing | 1 | Thrust/hold pattern in unspecified walking birds. |
| 24 | Nocturnal bees and wasps | 7 | Focal bee eye design, nocturnality and learned landmarks; approximate pooled 30-fold relative optical sensitivity. Not an absolute threshold. |
| 31 | American-toad optics | 6 | Adult/juvenile activity, relative sensitivity and optical observations. Raw +8D not corrected resting focus; accommodation not proof of depth-cue use. |

Entry 15’s retrieved abstract gives genomic hypotheses but no additional usable species-specific measurement. Entry 16 returned no abstract. Entry 8’s abstract offered no usable species-specific value. No abstract reading enters the full-read registry.

## Validation and files

Every new record passed `quotecheck.py` and was appended through `addlog.py` schema validation. PDF table rows with corrected/qualified taxon labels were checked against their extracted layout text. Image-only table/figure cells were manually transcribed and visually verified against the downloaded image/PDF before quote-checking that transcription; quotecheck alone is not claimed to validate OCR. Spreadsheet/CSV records quote exact cells or consecutive cells with coordinates in `where`. All quotes are at most 40 words. Completed registry totals reconcile separately from the 88 partial records.

Only the four permitted batch-1 files changed. No source PDF, XML, full paper text, spreadsheet, archive or image was committed. Sources/provider responses are in `/tmp/oa`; continuation scripts are in `/workspace/work/oa-resume`. Both are ephemeral. Raw bird wavelength curves remain external data; the log retains reported thresholds/integrals, not a copy of the workbook. Supplement S5 of entry17 has BH p=0.08 for a 50%-diet test despite stronger main-text wording; no universal ecological carry inferred.

## Resume

1. Recover entry32’s raw Supporting Tables S1–S3 through an accessible lawful route. Do not repeat the blocked publisher request in this session. Its main records are already logged; do not duplicate them or mark the source completed until supporting-table coverage is resolved.
2. Review access/available abstracts for entries33–59 in order, reusing completed provider results and avoiding duplicate evidence. Discovery-pending entries require a fresh successful provider session before any absence verdict. Next untouched verified full copy: entry60, then66 and67.
3. Continue legal retrieval for the blocked candidates below. For OpenAlex retries, retain at least one second between request starts and stop on a new 429 as BRIEF requires. Exact title/first-author/year matching remains mandatory for DOI-less entries.

Discovery-pending entries: 2, 12, 35, 36, 37, 38, 41, 42, 43, 44, 45, 46, 47, 49, 51, 52, 53, 54, 55, 57, 58, 62, 63, 64, 65, 69, 72, 73, 74, 75, 76, 77, 78, 79.

Retrieved copies still awaiting completion (metadata links, not additional read claims):

- **32**: Visual fields, foraging and collision vulnerability in gulls (Laridae). https://pure-oai.bham.ac.uk/ws/files/239436691/ibi.13360.pdf Main read; raw supplements pending.
- **60**: Slow or Fast Eyes: Associations Between Critical Flicker Fusion Frequency and Anti-Predator Strategy in Lepidoptera. https://carleton.scholaris.ca/server/api/core/bitstreams/c439f395-f97d-4061-ae6d-ca7101030ee8/content
- **66**: Evolution of ultraviolet vision in the largest avian radiation - the passerines: Additional files 1 to 3 (species list with site-90 residue). https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3225180/fullTextXML
- **67**: Diversity and evolution of frog visual opsins: spectral tuning and adaptation to distinct light environments. https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10994157/fullTextXML
- **68**: Aspects of cranial adaptation in foot-propelled diving birds: foraging and visual fields of some piscivorous species. https://reference-global.com/download/article/10.2478/orhu-2023-0023.pdf
- **71**: Expression of UV-sensitive parapinopsin in the iguana parietal eyes and its implication in UV-sensitivity in vertebrate pineal-related organs. https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3375259/fullTextXML

Other advertised entries still retrieval-blocked (not absence verdicts):

- **8**: Insights into the adaptive significance of vertical pupil shape in snakes. https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/j.1420-9101.2010.02046.x
- **14**: Assessment of visual acuity and contrast sensitivity in the chick using an optokinetic nystagmus paradigm. https://www.sciencedirect.com/science/article/pii/S004269899700446X/pdf
- **15**: Archelosaurian color vision, parietal eye loss, and the crocodylian nocturnal bottleneck. https://academic.oup.com/mbe/article-pdf/34/3/666/10821775/msw265.pdf
- **19**: Extraordinary diversity of visual opsin genes in dragonflies. https://www.pnas.org/content/pnas/112/11/E1247.full.pdf
- **23**: Evolution of vertebrate visual pigments. https://www.sciencedirect.com/science/article/pii/S004269890800148X/pdf
- **24**: Seeing in the dark: vision and visual behaviour in nocturnal bees and wasps. https://doi.org/10.1242/jeb.015396
- **26**: Head-bobs in birds: the eyes have it. https://journals.biologists.com/jeb/article-pdf/217/11/1836/1882628/os1836-1838.pdf
- **30**: Ecological and morphological correlates of acuity in birds: data deposited with the paper (Bird_Acuity_Data.csv, 94 species from 38 families). https://doi.org/10.5061/dryad.bzkh189g3
- **33**: Comparative study of the photopic spectral sensitivity of domestic ducks (Anas platyrhynchos domesticus), turkeys (Meleagris gallopavo gallopavo) and humans. http://researchonline.rvc.ac.uk/id/eprint/268/
- **39**: Eukaryotic algal phytochromes span the visible spectrum. https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3956157/fullTextXML
- **40**: Extraocular Vision in a Brittle Star Is Mediated by Chromatophore Movement in Response to Ambient Light. https://doi.org/10.1016/j.cub.2019.11.042
- **48**: Neural Summation in the Hawkmoth Visual System Extends the Limits of Vision in Dim Light. http://www.cell.com/article/S0960982216000804/pdf
- **50**: Ogre-Faced, Net-Casting Spiders Use Auditory Cues to Detect Airborne Prey. http://www.cell.com/article/S0960982220314184/pdf
- **56**: Understanding the cephalic eyes of pulmonate gastropods: a review. https://www.biodiversitylibrary.org/part/411913
- **59**: Visual pigments, ocular filters and the evolution of snake vision. https://academic.oup.com/mbe/article-pdf/33/10/2483/17473520/msw148.pdf
- **61**: A 'bright zone' in male hoverfly (Eristalis tenax) eyes and associated faster motion detection and increased contrast sensitivity. https://journals.biologists.com/jeb/article-pdf/209/21/4339/1541731/4339.pdf
- **70**: Visual abilities in two raptors with different ecology. https://jeb.biologists.org/content/jexbio/219/17/2639.full.pdf

## 2026-10-16 research round (continuation)

This round attempted discovery for the 46 assigned entries: 2, 8, 12, 14, 15, 19, 23, 24, 26, 30, 32, 33, 35, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 50, 52, 53, 54, 56, 58, 61, 62, 63, 64, 65, 67, 68, 69, 70, 71, 73, 74, 75, 76, 77, 78, 79. Only these entries were considered. This does not mean all three providers successfully checked every entry. The shared checkout was already updated to origin/main by the round coordinator.

- Discovery: 46 entries attempted; 15 returned advertised candidate locations. OpenAlex returned 23 HTTP-200 responses, one HTTP-400 response (the long chapter title at entry35), then HTTP429 at entry52; 21 later requests were skipped. Semantic Scholar returned HTTP429 on its first DOI lookup (entry8), then was stopped. Europe PMC returned 37 successful search responses; nine DOI-less/book entries could not be queried there. Exact-title matching did not accept entry12 because its batch lacks the matching first author and year. Entry2's search found no exact matching title. No incomplete/blocked lookup was converted into a no-copy verdict.
- Retrieved main copies: publisher PDFs for entries19 and39 through Europe PMC `?pdf=render`; the entry39 publisher PDF also from GEOMAR; entry32's already-read main PDF from Birmingham; full XML for entries67 and71. Five distinct entries have verified full main texts; entry32 was already read in the earlier round. Copies67 and71 remain unread at this checkpoint.
- Read this round so far: entry19's entire ten-page main article, all eight main figures and captions, methods and bibliography. **323 new partial full-text records** were logged. They cover thirteen named odonate species, eleven comparative insect genome inventories, and secondary Daphnia counts. **0 newly completed source-registry entries, 0 new no-copy verdicts.** Supplements still prevent a completion claim. No new abstract-only evidence was duplicated.
- Entry19's gene inventories are `opsin_genes_detected`, never receptor-class counts or demonstrated colour dimensionality. Its three ERG peaks are `spectral_sensitivity_peak_nm`, explicitly aggregate regional responses, never individual pigment lambda_max. Gene zeros are inventory results, not independently demonstrated gene loss. Figure4 comparative genome values have grade g and identify the secondary compilation. Figure6 counts and Figure4 cells were manually transcribed, visually checked against downloaded figures, then quote-checked against that labelled transcription. Other quotes were checked against the fetched article text. All 323 records passed quotecheck and addlog validation.

Access limits this round: Wiley, doi.org, OUP, PNAS, Journal of Experimental Biology, RVC and Cell returned HTTP403 and were stopped; ScienceDirect returned a proxy-tunnel403 and was also stopped. The round coordinator maintains the shared service stop list. Europe PMC fullTextXML for19 and39 returned500, but PMC HTML and Europe PMC publisher PDFs opened. PMC supplement downloads delivered a preparation/recaptcha page; Europe PMC supplement routes returned520, while its supplementaryFiles API explicitly says these entries are outside its open-access subset. No challenge was solved, login attempted or protected route bypassed. Those supplements remain unaccessed. Entry32's supporting tables remain missing; its prior partial records were not duplicated.

Next: finish entry39's available main-text measurements and resolve its supporting tables if a lawful accessible copy exists. Then review entries40–65 in order before starting the already-retrieved entry67. Do not repeat provider/site refusals in this round. Research scripts, metadata, papers and figure transcriptions are outside the repository under `/tmp/oa/oa-1` and `/workspace/work/oa-1`; none are committed.

### Entry39 checkpoint

Read the entire six-page main article, all six main figures/captions and bibliography, from the identified Europe PMC publisher PDF and the GEOMAR publisher version (the latter prepends the funding correction). Added **23 partial full-text records**: fourteen recombinant phytochrome-state absorption peaks in seven named algal species, their seven photocycle categories, and two explicitly secondary phytochrome-absence statements. These are nonvisual photosensors expressed as truncated proteins in E. coli with predicted native bilin precursors, not demonstrations of organismal colour vision or whole-organism spectral limits. Figure2C explicitly labels Prasinoderma coloniale at586nm although the prose's pooled range starts at584nm; that discrepancy is retained in the note. Main figure labels were visually checked before their marked transcription passed quotecheck. Supporting methods and TablesS1–S2 still fail retrieval; no source-registry completion was added. Round totals now: **346 new records, two main articles read, zero completed sources, zero no-copy verdicts.** Existing log now has 5,503 records. Entries67 and71 are retrieved but still unread. Entry32's old partial coverage was not duplicated.
