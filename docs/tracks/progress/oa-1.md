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

## 2026-10-16

This round is checking only entries 2, 8, 12, 14, 15, 19, 23, 24, 26, 30, 32, 33, 35–71, and 73–79 named by the round coordinator. Fresh discovery is in progress for the 56 assigned entries. Semantic Scholar returned HTTP 429 at entry 23 after three successful DOI requests; further requests to that provider stopped. Provider failures and title matches without verified author/year remain unresolved, rather than no-copy verdicts. No additional papers or records are claimed at this checkpoint. Scratch responses stay in `/tmp/oa/oa-1`, and scripts stay under `work/oa-1`.

Checkpoint: entry 19’s ten-page publisher article was recovered through Europe PMC’s public PDF rendering endpoint and read in full, including all main figures and bibliography. Added 303 partial records: 180 figure-6 inventory cells, 99 secondary figure-4 inventory cells, nine Ladona genome-complement values, three regional ERG peaks, two screening-pigment descriptions and ten tissue/stage expression observations. Figure cells were visually verified and transcribed into an external quote-check text. Seven preexisting group-level abstract records were corrected from `m` to `g`. The supporting PDF/workbook remain blocked (PMC download challenge; Europe PMC reports non-OA), so no completed source-registry line was added. Dryad’s public dataset page now opens, but file downloads return 403.

Checkpoint: six book/chapter entries (36, 37, 41, 49, 51, 55) received no-free-copy verdicts after successful OpenAlex closed-access responses, using the prompt’s single-provider allowance for books. Entry 39’s six-page publisher article plus funding correction was read from GEOMAR’s repository; 21 partial records cover seven recombinant phytochrome photocycles and their 14 photostate peaks. Values describe isolated proteins, not intact-algal vision; figure 2C’s 588-nm label versus the prose’s 584-nm pooled lower bound is retained. Supporting Tables S1–S2 could not be retrieved, so this source remains partial.

Checkpoint: entry57 is complete for its requested scope: chapters4/6 (printed pp.47–77 and107–137), all their figures/tables, and relevant Appendices2/3 (pp.168–176). The other thesis chapters are not claimed read. Added139 records, covering retinal-image dimensions, normalized scanning offsets, pounce rates/distances, individual retinal-angle changes, secondary field/movement reports, and explicitly inferred accommodation/model lengths. The published image-size percentages are not anatomical dimensions; angular acuity is not relabeled interreceptor spacing; a field without a stated axis stays unspecified. The chapter6 Figure6f bar counts disagree with prose counts in three eye-occlusion treatments; both versions are retained and labeled. The three-spider accommodation hypothesis is not established focusing behavior. Usable scanning N varies by stimulus despite six spiders being enrolled per species.

Checkpoint: entry59 is complete from the 59-page CITY accepted manuscript with its appended supporting material, now recovered in full. Added743 records: 237 qualified sequence-availability cells for79 taxa;259 S3–S5 predictions/empirical comparisons;140 ecological/retinal-morphology classifications;97 ocular-media cells for19 taxa; and10 prose/comparative observations. Every record identifies the accepted manuscript. Sequence predictions and reconstructed ancestors are inferred; earlier empirical comparisons, compiled sequences and relative-based anatomy are graded conservatively. SWS1 question marks, unknown combined shifts, uncertain species identifications, borrowed anatomy, and apparent row-value inconsistencies are retained. Normalized λ50 and integrated UVA transmission are distinct from receptor peaks and visibility cutoffs. The funding source correction in entry39 and this source’s accepted-version status were both checked.

Checkpoint: entry60 (Para thesis) is complete, including AppendicesA–D. Added105 records:54 explicitly approximate, inferred readings of the nine species’ CFF/ERG median lines; three exact group-level CFF spans; one illustrative Morpho ERG threshold;35 literature-appendix entries; and12 other secondary/qualitative observations. Raw individual data were not supplied, so plotted medians are never presented as exact author-tabulated values. The source’s voltage signs/units and100× amplifier gain are retained; population ERG latency/half-width are distinct from single-cell integration time. Earlier2024 protocol-error data were excluded by the author. The thesis’s87-Hz chicken average versus90–100-Hz stated individual range is flagged. Species identity, colour class, diel category and phylogeny remain confounded in the44-individual sample.

Checkpoint: entry66 is complete for the requested Additionalfiles1–3. The main XML and136-row DOCX were read, as were both alternative phylogeny figures. Added 552 records: 408 tuning-site residues (171 from57 newly sequenced taxa and237 secondary),137 explicitly inferred VS/UVS predictions including a qualified alternative for a source conflict, five group-level review measurements and two amplification failures. Additionalfile1 prints Cyanistes caeruleus as VS despite its Cys90 sequence and the main article’s UVS description; both variants are retained. Acanthisitta Leu93 has an unknown tuning effect, and Caracara cheriway is not silently reassigned to C.plancus. No physiological peak or behavioral tetrachromacy is inferred from marker counts.

### Final counts for this round

- Discovery attempted for all **56 assigned entries**. OpenAlex and Europe PMC returned successful DOI responses for applicable entries. Three DOI-less entries were resolved by matching title, author and year (19, 52, 78). Other incomplete citations and unmatched searches remain unresolved. Semantic Scholar supplied three successful responses before HTTP 429; later requests stopped. This is not a claim that all three providers completed every lookup.
- **11 distinct papers have retrieved, title-identified legal full main copies** this round: 19, 32, 39, 57, 59, 60, 66, 67, 68, 70, 71. Multiple versions/supplements of the same paper count once.
- **4 requested sources completed**: 57, 59, 60, 66. Their new source-ledger records total **1,539**. Main articles at 19 and 39 were read and supplied **324 partial records**, with their supporting material still blocked. Entry 32's earlier main-only coverage remains unchanged.
- **1,863 records added**, bringing this batch log to **7,020**. Seven earlier group-level abstract grades were corrected. Of the new values, **54 are visually estimated plot medians**, all explicitly inferred with uncertainty and sample sizes. The other **1,809** come from explicit text/table/figure labels, including qualified author predictions and secondary reports.
- **6 new no-free-copy verdicts**, all books/chapters using the prompt's single-OpenAlex allowance: 36, 37, 41, 49, 51, 55. Batch no-copy ledger now has 16 entries. Blocked advertised copies and unavailable providers were not counted as no-copy verdicts.
- **10 assigned entries resolved**, leaving **46 unresolved**: 2, 8, 12, 14, 15, 19, 23, 24, 26, 30, 32, 33, 35, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 50, 52, 53, 54, 56, 58, 61, 62, 63, 64, 65, 67, 68, 69, 70, 71, 73, 74, 75, 76, 77, 78, 79.

All 1,863 new records passed final quote checking; the complete 7,020-record batch passed its evidence schema check. The source ledger has 16 completed entries totaling 6,608 records; 412 partial records reconcile the difference. No app setup, builds, servers or app tests ran. No paper text, PDF, XML, document or image was committed.

### Review manifest and continuation

External review manifest: `/tmp/oa/oa-1/review-manifest.json`. Record-to-quotecheck mappings, all under `/tmp/oa/oa-1/`:

| Records | Quotecheck text | Retrieved source |
|---|---|---|
| `19-records.jsonl` | `19-checked.txt` | `19-pdf.pdf`; visually verified figure-4 and figure-6 transcription appended to extracted text |
| `39-records.jsonl` | `39-checked.txt` | `39.pdf`; visually verified figure labels appended to extracted text |
| `57-records.jsonl` | `57-checked.txt` | `57.pdf`; figure-6f count labels appended after image review |
| `59-records.jsonl` | `59-checked.txt` | `59-city.pdf`; manuscript line-number gutter removed from main prose |
| `60-records.jsonl` | `60.txt` | `60.pdf`; caption quotes checked, median estimates visually checked in `60-figs/p-48.png` through `p-53.png` |
| `66-records.jsonl` | `66-checked.txt` | `66.xml` and `66-supp/1471-2148-11-313-S1.DOCX`; extracted table cells combined with XML text |

Stop at the source boundary before **entry 67**: the broad frog paper and its large species supplements need a fresh reading context. Main copies for **67, 68, 70 and 71** are downloaded and title-identified, but not claimed read. Continue them in batch order. Entry 77's Vienna repository page also opens; its thesis PDF has not been retrieved. The next worker should use the current discovery/provider responses rather than converting rate-limited or incomplete lookups into absence verdicts. All scratch files are ephemeral.
