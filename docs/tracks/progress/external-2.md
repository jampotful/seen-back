# External batch 2

## 2026-10-14

This round: **7 of 50 genera completed in batch order**: Dittrichia, Sidalcea, Centrosema, Cochemiea, Stercorarius, Arge, Hemicordulia. Added **4 evidence records, 2 wanted lines, and 27 trait-specific null-search lines** (covering 71 species/trait entries in this batch). **43 genera remain**; the next full sweep begins with Antennaria. No cells are claimed exhausted before the canon gate and coverage calculation are satisfied. Local canon/evidence checking identified Hemicordulia tau acuity already in canon-4#202; it was not duplicated.

Evidence, all checked with quotecheck before addlog:

- Cochemiea grahamii: light-required seed germination stated directly in the primary abstract, published as Mammillaria grahamii. GBIF synonym lookup confirmed the identity. The record is partial/abstract evidence and identifies no specific photoreceptor.
- Centrosema molle: no significant inceptin-induced ethylene response at 1 μM In11 in accession PI 212980 01 SD (n=4, paired Wilcoxon p=0.38), from the opened primary paper and supplementary spreadsheets. This is an assay-specific negative result, **not absence of chemical sensing generally**, and no positive perception claim was inferred from sequence data.
- Arge similis: apposition compound-eye anatomy from the opened microscopy paper. Eight retinular cells were not called eight spectral receptor classes; facet counts/diameters were not converted into acuity.
- Hemicordulia tau: 0.90-degree interommatidial angle from the opened Feller et al. 2021 compilation (10.1016/j.asd.2020.101002), with the compilation named as the source and its original-reference number stated. The 2024 neural-adaptation paper uses a 0.7-degree model parameter from an older anatomical citation; that was not treated as a new measurement.

Wanted: Brownsey et al., Growth and phenology of Dittrichia graveolens (10.1007/s10530-013-0501-4), to separate light-dependent development from a photoperiod inference; Berry et al., Form vision in the insect dorsal ocelli (10.1016/j.visres.2007.01.019), for quantitative median-ocellus optics absent from its abstract. The latter is an extra-eye upgrade lead; compound-eye acuity already exists. Wanted counts use the actual deduplicated species/view RG count in cells.jsonl (7621 and 5367), not the batch weight.

Search scope and access limits: successful Europe PMC scientific/common-name queries were screened up to 25 titles and available abstracts; relevant public full texts and supplementary data were opened. Older names Inula viscosa and Mammillaria grahamii were searched. The Fabaceae flowering review (10.3389/fpls.2015.00207) was checked for Centrosema; the Arge citation step screened all 33 Europe PMC citing titles of 10.1242/jeb.204.3.559. The Dittrichia genus review (10.3390/molecules31142474) and primary stress papers were inspected. Emitted compounds, pharmacology, toxicity, culture photoperiod, seasonal flowering, neural tuning optima, adaptation rates and monitor refresh rates were not substituted for the requested sensory measurements.

OpenAlex returned shared-budget HTTP 429; its failed lookup contributes no null result. Europe PMC fullTextXML failed for some 2011/2019 dragonfly STMD papers, and PMC returned a challenge for two of them; their available abstracts were read, not claimed as full text. The distinct 2019 lobula motion-tuning paper was read through a reachable public PMC page. The publicly listed ScienceDirect ocellus PDF was denied by the session proxy (403); it remains wanted and no alternate access route was attempted.

Exploratory only, not counted as completed: queries for Antennaria, Clytus and Hylaeus are cached in /tmp/external-2. Antennaria lead 10.3390/genes11121449 concerns induced changes of reproductive mode and needs full screening before treating any treatment as a sensory cue. Hylaeus results 10.1016/j.ympev.2006.09.004 and 10.1016/j.ympev.2008.09.028 use opsin as a phylogenetic marker, not measured receptor spectra. These three genera and the rest of the batch remain unfinished. Scratch sources and scripts are outside the repository and are not durable deliverables.

Checkpoint commit: ac01848 (Dittrichia). The final batch commit is reported by the worker; the parent handles push and PR. No app build, prepare, server, browser, or self-test was run.
