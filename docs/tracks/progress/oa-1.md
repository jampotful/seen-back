# Open-access pass, batch 1

2026-10-14. Partial pass on `research/oa-1`, based on `de54993`. Resumed from the entry-13 handoff on 2026-10-14. Completed through entry 18 where full text was available. Next full verified copy is **entry 28, Lens and cornea limit UV vision of birds**. Entries 19–26 are now reviewed to the extent accessible; entry 25’s full supplement bundle is read. Entry 14 yielded four abstract-only records; entries 14–15 remain full-text retrieval-blocked and entry 16 has no retrieved abstract. No app setup, builds, servers, browser tests or self-tests ran.

## Counts

- **79 batch entries processed** in the discovery pass before reading papers. This does not mean all three providers successfully checked every entry.
- **35 candidate open-copy locations found**; **18 batch source copies retrieved and identified** by title on the PDF first page or XML article title. Eleven are read; seven are waiting. The newly retrieved copy is entry 25’s complete two-file supplement bundle, identified from its first-page dataset heading and the official Figshare record/file metadata.
- **11 batch entries read in full (10 articles and 1 supplement bundle)**, including available relevant tables and supplements; **4,531 full-text/supplement records**.
- **7 additional abstracts with logged measurements** from papers with no free full copy located; **50 partial records**. Abstracts do not count as full papers read.
- **4,581 evidence records total**, all quote-checked before append with `addlog.py`; no failed quotes retained. Source-registry counts agree with full-text evidence counts.
- **10 papers with no free copy located after completed permitted lookups**, recorded in `docs/views/sources/oa-none-1.jsonl`. Four of these yielded the abstract records above.
- **34 entries remain unresolved at discovery**, due to provider interruption or no verifiable title/author/year match. They are not declared unavailable.
- **17 further advertised candidate copies could not be retrieved**. They remain retrieval-blocked rather than counted as confirmed no-copy papers.

OpenAlex returned HTTP 429 during an additional title lookup for entry 2. Further OpenAlex calls stopped, as BRIEF requires. The main pass had saved responses through entry 37; remaining DOI entries were checked with Europe PMC and Semantic Scholar, with Semantic Scholar requests spaced by at least one second. Books/chapters received the permitted OpenAlex-only treatment. Title-only matches were accepted only when title, first author and year agreed; incomplete citations were not guessed. Provider errors, unresolved identity and no-copy results remain separate.

The temporary lookup script, provider responses, downloads and extracted text are under `/tmp/oa`. These are ephemeral and **not committed**. Only the four permitted batch-1 output files changed. No PDF, XML, full paper text, spreadsheet, source archive or app file is in this branch's changes.

## Completed full readings

| Entry | Paper | Records | Material read and important qualifications |
|---|---|---:|---|
| 3 | Katti et al., reptile photopigments | 89 | All 16 pages. Secondary measurements explicitly name the review; primary papers were not opened. Native A2 spectra and A1-reconstituted spectra differ. Pooled ranges stay with measured species groups; gene complement is not relabeled as measured color vision. |
| 4 | Kelber et al., animal color vision | 306 | Lund University Publications linked the publisher-formatted PDF. Read pp. 81–118, both tables and appendices. Table records checked against layout text; prose against the PDF. Visually confirmed 12+ and ≥3 glyphs. Suggestive tests, model estimates, taxon-label conflicts and contradictory cat/turtle entries are qualified. |
| 6 | Cantlay et al., Anatidae fields | 1,156 | Full XML and all three Figshare files: methods/tables DOCX plus both CSV datasets, 39 species. 195 field descriptors, 921 signed margin separations, 39 eye-movement observations and one secondary visual-streak report. Eight vertical extents have `bound: lower`; blank cells remain missing. Legacy source labels/subspecies retained; movement yes for mallards/Canada geese preserved. |
| 7 | Nityananda & Read, stereopsis | 34 | Full XML, figures/captions and references. Species remain unspecified when only common groups are given. Behavioral stereo, physiological responses and predictions are distinct. Owl distance range/optimum are inferred; dragonfly temporal resolution is not called behavioral CFF. |
| 9 | Sondhi et al., Lepidoptera opsins | 809 | Full XML and legal Europe PMC supplement archive; all 175 entries and reference sheet in Data 1, with Data 2–4/figure context. 699 recovered-sequence counts, 107 qualified diel assignments and three secondary repertoire summaries. Zeros mean non-recovery, not loss/color blindness. Crambus 2? retained; Eacles RH7 count 2 does not assert a validated duplication. Blank RH7/unknown diel cells remain missing. |
| 11 | Potier et al., owl fields | 898 | Full XML plus DOCX, Table S1 PDF and four-sheet workbook. 43 species' descriptors, 665 individual signed profile cells and 52 bill projections. Profile cells conservatively inferred because interpolation is unmarked. Ninox 54.5° in text versus 52° in tables, and Strix aluco 47° versus 48°, remain flagged. Posterior 180° is only an upper bound. |
| 13 | Mohun & Davies, amphibian photoreception | 99 | All 12 pages, Table 1 and figure captions/references. Review evidence: native/regenerated and A1/A2 peaks, life stages and mixture ratios stay separate. Split printed Xenopus 4/45 interpreted as 445 ±6 only with inference grade; Cynops green-rod table/text conflict retained. No supplement is cited in the PDF. |
| 17 | Kopania & Clark, mammalian retinal specializations | 290 | Full XML, six supplement tables and four supplement figures/references. 119 features from 82 retinal-species rows, 91 bony orbit angles, 78 estimated map coordinates, two secondary human cell densities. Measured-species columns override phylogeny/common-name labels; wolf, hyena, primates, marmot and camel distinctions preserved. Chinchilla retinal species ambiguous; blanks not absence. Published 2025 (batch says 2024). |
| 18 | Caves et al., avian acuity | 374 | Full XML, all 17 supplement pages, main tables and figure labels. 94 S1 bird rows (caption says 93); 29 S2 vertebrates (caption says 28), two duplicate RGC values omitted. RGC/behavior distinctions and uncertain method labels preserved; Dasyurus table/reference species conflict left unresolved at genus level. S1/S2 acuity disagreements retained. Main Table 1 image values and Fig.4 labels manually transcribed, visually verified, then quote-checked; Fig.4 magpie 38.3 versus S1 33 flagged inferred. |
| 25 | Veilleux & Kirk, mammal acuity supplements | 216 | Entire 14-page Table PDF (91 species, source bibliography) and 1-page Figure PDF; only the batch’s standalone supplement entry is marked read, not the main article. 91 acuities, 91 axial lengths, 34 activity classes. Blank method/AP cells stay unknown; cone-based estimates distinct from RGC. Taxon/citation conflicts (Eptesicus/Macrotus, primates, ground squirrel), source spellings and estimated wallaby axial length explicitly qualified. |
| 27 | Sharkey et al., beetle opsins | 260 | Full XML, all 11 supplement pages/seven tables, figure captions and Fig.4 grid. 231 recovery counts across 77 taxa, 26 categorical spectral bands, three prose measurements/classifications. Partial-copy asterisks retained; Xenos sequence/protein counts and Agrilus S2/S3 discrepancy qualified. Physiology stays with the right-hand measured taxa, not related left-column taxa. Dendroctonus blue report without UV stimuli remains inferred. |

None of the ten read article copies is an accepted manuscript: publisher-formatted papers or XML metadata explicitly mark manuscript/preprint as no. No full source is marked read until the reading and quote checks were complete.

The detailed CSV/XLSX evidence quotes exact cells (or consecutive cells), with filename, sheet, row/column or cell coordinates in `where`. Signed retinal-margin separation is distinct from total field of view. The genetic-recovery trait is distinct from physiological receptor classes. New traits have reasons in `note`; derived/inferred results retain their grades.

## Abstract-only evidence

| Entry | Paper | Partial records | Qualifications |
|---|---|---:|---|
| 5 | Comparative morphology of the tapetum lucidum | 17 | Selected-taxon tapetum categories; broad group labels are not universal species claims. |
| 10 | Temporal resolution of colour vision in the honeybee | 8 | Approximately 100 Hz heterochromatic cutoff at optimal intensity ratio in each color pair; not conventional achromatic CFF. Bee species is not named in abstract. Inferred 10 ms and relative channel ratios retain inference grades. |
| 21 | Head-bobbing of walking birds | 1 | Thrust/hold pattern for unspecified walking birds, not every species. |
| 14 | Chick acuity | 4 | Abstract only: age-dependent optokinetic acuity ranges, peak contrast frequency and threshold. Chick species not specified in abstract. Advertised full copy remains retrieval-blocked; not added to no-copy registry. |
| 19 | Dragonfly opsin diversity | 7 | Abstract-only gene counts for unnamed Libellulidae species and wider sampled Odonata. Not physiological receptor-class count or demonstrated color vision. PMC HTML was a recaptcha response, not full text. |
| 24 | Nocturnal bees and wasps | 7 | Abstract-only focal bee eye design, nocturnality and learned landmarks, plus approximate pooled 30-fold relative optical sensitivity. Not a measured absolute threshold. |
| 31 | Visual optics in toads | 6 | Bufo americanus adult/juvenile activity, sensitivity comparison and optical observations. Raw +8 D retinoscopy is not corrected resting focus; binocular accommodation is not proof of a depth-cue strategy. |

All carry `partial: true`, `access: abstract`, `opened: true`, and the retrieved Europe PMC DOI-query URL. They do not enter the full-read registry. Entry 8's advertised Wiley free copy was not retrievable, and its abstract contained no species-specific value to log.

## Resume

1. Read entry 28 in full with supplements; continue down the batch in order. Keep source-registry entries confined to completed full readings.
2. Revisit discovery-pending entries in a fresh session with the rate-limit rule respected. Exact title/first-author/year agreement is still required for DOI-less records. Do not convert provider failures into no-copy results.
3. Investigate retrieval-blocked candidate copies through lawful publisher/repository routes. Read and quote-check any abstract-only measurements; do not mark a full paper read from an abstract.

Discovery-pending entry numbers: 2, 12, 35, 36, 37, 38, 41, 42, 43, 44, 45, 46, 47, 49, 51, 52, 53, 54, 55, 57, 58, 62, 63, 64, 65, 69, 72, 73, 74, 75, 76, 77, 78, 79.

Retrieved, title-verified copies awaiting full reading (the following are metadata links, not read claims):

- **28**: Lens and cornea limit UV vision of birds – a phylogenetic perspective. https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8601714/fullTextXML
- **32**: Visual fields, foraging and collision vulnerability in gulls (Laridae). https://pure-oai.bham.ac.uk/ws/files/239436691/ibi.13360.pdf
- **60**: Slow or Fast Eyes: Associations Between Critical Flicker Fusion Frequency and Anti-Predator Strategy in Lepidoptera. https://carleton.scholaris.ca/server/api/core/bitstreams/c439f395-f97d-4061-ae6d-ca7101030ee8/content
- **66**: Evolution of ultraviolet vision in the largest avian radiation - the passerines: Additional files 1 to 3 (species list with site-90 residue). https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3225180/fullTextXML
- **67**: Diversity and evolution of frog visual opsins: spectral tuning and adaptation to distinct light environments. https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10994157/fullTextXML
- **68**: Aspects of cranial adaptation in foot-propelled diving birds: foraging and visual fields of some piscivorous species. https://reference-global.com/download/article/10.2478/orhu-2023-0023.pdf
- **71**: Expression of UV-sensitive parapinopsin in the iguana parietal eyes and its implication in UV-sensitivity in vertebrate pineal-related organs. https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3375259/fullTextXML

Advertised candidate copies not yet retrievable (no absence verdict implied):

- **8**: Insights into the adaptive significance of vertical pupil shape in snakes. Candidate: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/j.1420-9101.2010.02046.x
- **14**: Assessment of visual acuity and contrast sensitivity in the chick using an optokinetic nystagmus paradigm. Candidate: https://www.sciencedirect.com/science/article/pii/S004269899700446X/pdf
- **15**: Archelosaurian color vision, parietal eye loss, and the crocodylian nocturnal bottleneck. Candidate: https://academic.oup.com/mbe/article-pdf/34/3/666/10821775/msw265.pdf
- **19**: Extraordinary diversity of visual opsin genes in dragonflies. Candidate: https://www.pnas.org/content/pnas/112/11/E1247.full.pdf
- **23**: Evolution of vertebrate visual pigments. Candidate: https://www.sciencedirect.com/science/article/pii/S004269890800148X/pdf
- **24**: Seeing in the dark: vision and visual behaviour in nocturnal bees and wasps. Candidate: https://doi.org/10.1242/jeb.015396
- **26**: Head-bobs in birds: the eyes have it. Candidate: https://journals.biologists.com/jeb/article-pdf/217/11/1836/1882628/os1836-1838.pdf
- **30**: Ecological and morphological correlates of acuity in birds: data deposited with the paper (Bird_Acuity_Data.csv, 94 species from 38 families). Candidate: https://doi.org/10.5061/dryad.bzkh189g3
- **33**: Comparative study of the photopic spectral sensitivity of domestic ducks (Anas platyrhynchos domesticus), turkeys (Meleagris gallopavo gallopavo) and humans. Candidate: http://researchonline.rvc.ac.uk/id/eprint/268/
- **39**: Eukaryotic algal phytochromes span the visible spectrum. Candidate: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3956157/fullTextXML
- **40**: Extraocular Vision in a Brittle Star Is Mediated by Chromatophore Movement in Response to Ambient Light. Candidate: https://doi.org/10.1016/j.cub.2019.11.042
- **48**: Neural Summation in the Hawkmoth Visual System Extends the Limits of Vision in Dim Light. Candidate: http://www.cell.com/article/S0960982216000804/pdf
- **50**: Ogre-Faced, Net-Casting Spiders Use Auditory Cues to Detect Airborne Prey. Candidate: http://www.cell.com/article/S0960982220314184/pdf
- **56**: Understanding the cephalic eyes of pulmonate gastropods: a review. Candidate: https://www.biodiversitylibrary.org/part/411913
- **59**: Visual pigments, ocular filters and the evolution of snake vision. Candidate: https://academic.oup.com/mbe/article-pdf/33/10/2483/17473520/msw148.pdf
- **61**: A 'bright zone' in male hoverfly (Eristalis tenax) eyes and associated faster motion detection and increased contrast sensitivity. Candidate: https://journals.biologists.com/jeb/article-pdf/209/21/4339/1541731/4339.pdf
- **70**: Visual abilities in two raptors with different ecology. Candidate: https://jeb.biologists.org/content/jexbio/219/17/2639.full.pdf

## Resumed discovery attempt

On 2026-10-14 the unresolved-entry retry script enforced at least 1.1 seconds between OpenAlex request start times (and between Semantic Scholar request starts). The first OpenAlex request, for entry 2 by exact title, immediately returned HTTP 429. Per BRIEF, no further requests went to that provider in this session. No second OpenAlex request occurred, so there is no observed spacing pair to report. The 34 unresolved entries remain unresolved; provider failure is not an absence verdict. Saved previous lookup responses before retrying; no completed search was erased from the audit trail. Existing Europe PMC and Semantic Scholar successful/404 results were retained.

Entry 15's re-retrieved abstract reports genomic hypotheses but no species-specific numerical vision measurement to add; entry 16's DOI search returned no abstract. The chick abstract is a fifth evidence-bearing abstract, not a completed no-copy verdict. Supplement Table S5 for entry 17 gives BH p=0.08 for the 50%-diet horizontal-streak-only test, despite main-text wording implying this cutoff result held; no universal ecological carry is inferred. Raw map pixel sizes were not logged as physical retinal dimensions.

Entry 18's linked Dryad dataset metadata and file list were retrieved through the public API, but the first file download returned 401; no authentication attempted. Supplement PDFs provide the measurements above. Entry 30 is therefore still not fully retrieved/read. The Europe PMC advertised rendered main-PDF endpoint returned 404; the full XML, supplements and linked graphics were available.

Entry 25 was recovered legally via the public Figshare API and ndownloader URLs; the main 2014 article remains unopened. Added no no-copy verdict for retrieval-blocked entries. Entry 19’s official PMC page returned HTTP 200 but contained only “Checking your browser - reCAPTCHA”; it is not treated as a paper reading. Entries 20/22/23/26 offered no additional usable species measurements from the available material; entry 21 was already logged.
