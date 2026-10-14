# Open-access pass, batch 1

2026-10-14. Partial pass on `research/oa-1`, based on `de54993`. Resumed from the entry-13 handoff on 2026-10-14. Completed entry 13; next full verified copy is **entry 17, Mammalian retinal specializations for high acuity vision**. Entries 14–16 require retrieval or abstract review before moving onward. No app setup, builds, servers, browser tests or self-tests ran.

## Counts

- **79 batch entries processed** in the discovery pass before reading papers. This does not mean all three providers successfully checked every entry.
- **35 candidate open-copy locations found**; **17 full documents retrieved and identified** by title on the PDF first page or XML article title. Seven are read; ten are waiting.
- **7 full papers read**, including available relevant tables and supplements; **3,391 full-text records**.
- **4 additional abstracts read** from papers with no free full copy located; **32 partial records**. Abstracts do not count as full papers read.
- **3,423 evidence records total**, all quote-checked before append with `addlog.py`; no failed quotes retained. Source-registry counts agree with full-text evidence counts.
- **10 papers with no free copy located after completed permitted lookups**, recorded in `docs/views/sources/oa-none-1.jsonl`. Four of these yielded the abstract records above.
- **34 entries remain unresolved at discovery**, due to provider interruption or no verifiable title/author/year match. They are not declared unavailable.
- **18 further advertised candidate copies could not be retrieved**. They remain retrieval-blocked rather than counted as confirmed no-copy papers.

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

None of the seven read copies is an accepted manuscript: publisher-formatted papers or XML metadata explicitly mark manuscript/preprint as no. No full source is marked read until the reading and quote checks were complete.

The detailed CSV/XLSX evidence quotes exact cells (or consecutive cells), with filename, sheet, row/column or cell coordinates in `where`. Signed retinal-margin separation is distinct from total field of view. The genetic-recovery trait is distinct from physiological receptor classes. New traits have reasons in `note`; derived/inferred results retain their grades.

## Abstract-only evidence

| Entry | Paper | Partial records | Qualifications |
|---|---|---:|---|
| 5 | Comparative morphology of the tapetum lucidum | 17 | Selected-taxon tapetum categories; broad group labels are not universal species claims. |
| 10 | Temporal resolution of colour vision in the honeybee | 8 | Approximately 100 Hz heterochromatic cutoff at optimal intensity ratio in each color pair; not conventional achromatic CFF. Bee species is not named in abstract. Inferred 10 ms and relative channel ratios retain inference grades. |
| 21 | Head-bobbing of walking birds | 1 | Thrust/hold pattern for unspecified walking birds, not every species. |
| 31 | Visual optics in toads | 6 | Bufo americanus adult/juvenile activity, sensitivity comparison and optical observations. Raw +8 D retinoscopy is not corrected resting focus; binocular accommodation is not proof of a depth-cue strategy. |

All carry `partial: true`, `access: abstract`, `opened: true`, and the retrieved Europe PMC DOI-query URL. They do not enter the full-read registry. Entry 8's advertised Wiley free copy was not retrievable, and its abstract contained no species-specific value to log.

## Resume

1. Investigate entries 14–16, then read entry 17 in full, including free tables/supplements; continue down the batch in order. Keep source-registry entries confined to completed full readings.
2. Revisit discovery-pending entries in a fresh session with the rate-limit rule respected. Exact title/first-author/year agreement is still required for DOI-less records. Do not convert provider failures into no-copy results.
3. Investigate retrieval-blocked candidate copies through lawful publisher/repository routes. Read and quote-check any abstract-only measurements; do not mark a full paper read from an abstract.

Discovery-pending entry numbers: 2, 12, 35, 36, 37, 38, 41, 42, 43, 44, 45, 46, 47, 49, 51, 52, 53, 54, 55, 57, 58, 62, 63, 64, 65, 69, 72, 73, 74, 75, 76, 77, 78, 79.

Retrieved, title-verified copies awaiting full reading (the following are metadata links, not read claims):

- **17**: Mammalian retinal specializations for high acuity vision evolve in response to both foraging strategies and morphological constraints (Supplementary Table S1). https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11968189/fullTextXML
- **18**: Ecological and morphological correlates of visual acuity in birds: supplementary Tables S1 and S2 (acuity, eye size and body mass for 94 species). https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10906485/fullTextXML
- **27**: Overcoming the loss of blue sensitivity through opsin duplication in the largest animal group, beetles. https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5428366/fullTextXML
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
- **25**: Supplementary Material for: Visual Acuity in Mammals: Effects of Eye Size and Ecology. Candidate: https://figshare.com/articles/dataset/Supplementary_Material_for_Visual_Acuity_in_Mammals_Effects_of_Eye_Size_and_Ecology/5126077
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
