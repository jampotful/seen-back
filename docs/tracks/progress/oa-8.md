# OA batch 8 (14 October 2026)

Branch: `research/oa-8`. The lookup and reading pass is finished for the copies accessible in this environment. No app setup, build, server, browser test, or app self-test was run. Only the four files allowed by `oa-pass.md` are changed.

## Counts

- Batch entries processed: 79, in the required lookup pass before reading.
- Candidate free-copy locations: 27 papers (24 from OpenAlex/PMC/Semantic Scholar candidate extraction, plus 3 from additional free URLs already returned by Europe PMC).
- Complete main texts read: 11, including one full bioRxiv preprint. Free supplementary Figures S1–S2 were also read for paper 33.
- Evidence: 307 records, comprising 209 from full texts and 98 from abstracts of 27 other papers. All 307 final quotes passed `quotecheck.py`; 304 were verbatim after normalization and 3 passed its table rule. `addlog.py` validated each record before appending it.
- Evidence grades: 254 m, 3 g, 50 i. The i records are sequence-based spectral predictions, explicitly distinguished from measurements.
- Remaining papers: 68. Free locations were found but not retrieved for 16; completed queries found no free location for 41; 11 had insufficient completed lookups to decide. The 41 negative entries retain their incomplete OpenAlex coverage explicitly; only the first two papers had successful checks with all three services.

## Sources read

Full main texts were read in batch order: 16 (rank 569), 20 (573), 33 (586), 35 (588), 42 (595), 65 (618), 66 (619), 67 (620), 69 (622), 72 (625), and 77 (630). The exact batch titles, free-copy URLs, per-paper record counts, version information and supplement limitations are in `docs/views/sources/oa-8.jsonl`. Abstract-only sources remain on the unresolved list in `docs/views/sources/oa-none-8.jsonl` and all their evidence carries `partial: true` and `source.access: abstract`.

All 38 species in the bird ocular-media table were logged, with their reported pigment peaks where given. The snake comparison logged all 17 species' reported activity classifications, the supported sequence predictions and the retinal anatomy of the 11 species examined anatomically. Measurements in species outside the wanted list are included. Mean/range/alternative-fit values are retained in the relevant records' notes where they describe the same measurement rather than an independent dataset.

The strongest evidence is the direct bumblebee intracellular spectral and temporal work, the stink bug ERG/chromatic adaptation experiments, and the bird ocular-media data. Bumblebee response half-width and peak time are recorded in milliseconds; they are not converted into flicker-fusion rates. The weakest evidence is the explicitly partial abstracts and sequence predictions. Opsin gene counts and anatomical cone shapes are distinguished from functional spectral classes and behavioural colour discrimination.

## Access limits

OpenAlex returned HTTP 429 on paper 3: the shared unauthenticated daily budget was exhausted, with reset at midnight UTC. BRIEF requires stopping a service after 429, so later entries were not retried there. DOI entries continued through Europe PMC and Semantic Scholar; title-only entries could not be resolved through OpenAlex. `checked` arrays include only services with an actual successful or not-found response, and `lookup_limits` lists missing coverage.

Publisher downloads returned HTTP 403 at Wiley, JEB/Biologists, OUP and doi.org, and those hosts were not retried. The eScholarship landing page returned HTTP 202 instead of content. Legacy PMC links for papers 31 and 54 led to robot challenges, and alternate Europe PMC XML requests returned HTTP 500. The lack of retrieval is not a claim that a free copy does not exist. Explicit free-copy and incomplete-lookup statuses are kept separate from negative lookup results.

Supplement limits: paper 35's primer supplement returned MDPI HTTP 403; paper 67's supplementary PDF download timed out; paper 66's separate primer/sequence supplements, and supplements to 69, 72 and 77 were not retrieved. Those limits are on their source lines. No values were inferred from unread supplements. Raw responses, PDFs, XML and extracted paper text remain outside Git in `/tmp/oa/8`; scripts remain in ignored `work/`. No paper text or PDF is committed.

## Items for the research desk

- Paper 66 was read as the 18 January 2017 bioRxiv preprint, DOI 10.1101/100792, with the batch's final-journal DOI retained only as the requested-work identity. Every evidence line marks the preprint version.
- Paper 67 predicts peaks from opsin sequences and does not measure them physiologically. The main text uses Dipsas indica in the LWS/RH1 prediction discussion despite sampling D. petersi. No such numerical peak was assigned to D. petersi without the unread supplement. Table spelling Spillotes pullatus is retained and flagged; the Echinanthera spelling is resolved from Methods.
- Paper 72's comparative table mixes garter-snake MSP values cited to Sillman 1997 with regeneration values cited to Schott 2016. The retrieved Sillman abstract identifies T. sirtalis, so its MSP values and the combined means were not assigned to T. proximus. Python and sunbeam-snake values are marked as secondary reports.
- Paper 65's Results and Discussion disagree about the direction of root-foraging precision. The record flags this and does not equate growth responses to a demonstrated sensory receptor or a chemical detection threshold. Five barnyardgrass taxa were pooled, so the pooled findings are not duplicated as species-level numbers.
- Stink bug receptor classes do not prove behavioural dichromacy. Likewise, gene expression and four morphological cone types in snakes do not demonstrate tetra- or trichromatic colour discrimination.
- Europe PMC gives paper 76 a 2015 year and revised title; the abstract evidence uses the retrieved citation rather than the batch's 2014 entry. The logger's bibliographic author lists use author groups, excluding editors.

Next three actions, when services permit: repeat only incomplete OpenAlex/title queries after its quota reset; retrieve the 16 known free locations and unread supplements through legal public routes; review the flagged species/citation discrepancies before merging. The owner opens the pull request and the desk samples records; this task opens no PR and does not push to main.
