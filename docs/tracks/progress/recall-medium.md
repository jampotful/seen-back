# Blind search-recall test — medium

Retrieved trait evidence for **9 of 10 cells**. `Onitis / interommatidial_deg` has `found: []`. This is a retrieval tally, not the research desk's scored recall.

Elapsed research time: **13.1 minutes**, from 2026-10-14 14:25:59 EDT to 14:39:05 EDT. Includes searching, screening, source retrieval, extraction and writing; excludes initial environment startup and locating the updated task instructions.

The JSONL has one record for every cell, with queries, sources, a citation/review step and quotes copied from retrieved sources (at most 40 words). Initial OpenAlex searches screened up to 25 titles and available abstracts per scientific-name and common-name query, or all results where fewer existed. Europe PMC supplied additional abstracts and open full texts. Crossref confirmed the reported source DOIs/titles. Source PDFs and intermediate results stayed outside the repository.

Qualifications for scoring:

- `Cupiennius`: the primary abstract reports **three visual opsins**. That is molecular repertoire evidence, not proof of three physiological receptor classes; the value explicitly preserves that distinction.
- `Phidippus audax`: the original paper reports ALE acute-zone interrhabdomal spacing of **0.46 ± 0.01 degrees**. The recorded **approximately 1.09 cycles/degree** is the explicitly labelled anatomical Nyquist calculation, 1/(2 × 0.46), not a directly measured behavioural threshold. The paper was read from the author's University of Cincinnati PDF.
- `Octopus`: the review's **72 Hz** is explicitly pooled across **O. vulgaris and O. briareus**; it must not be treated as a species-specific estimate.
- `Photuris`, `Chelostoma` and `Xiphydria`: spectral maxima come from Table 1 of the retrieved open review **10.1146/annurev-ento-061720-071644**. That review supplies the quoted values; none was inferred from a relative. Its `Photuris lucicrescens` row is under an unexpected family heading (Elateridae); the genus/species and numbers are transcribed as printed, without silently repairing the table.
- `Ovis`: the **60-degree** binocular field comes from Table 1 of **10.1007/s00429-021-02392-8**, which attributes it to Lindsay Johnson (1901); that older original was not read.
- `Phelsuma`: the review's Table 2 explicitly lists a temporal fovea in **P. laticauda**. The chosen row cites Griffing et al. (2020); the adjacent unpublished-data row was not used.
- `Onitis`: the accessible original abstracts report photoreceptor **acceptance angles**, which were excluded. Relevant original papers and later reviews were inspected, but an interommatidial-angle value could not be verified in a permitted, accessible source during this run. This is an access/retrieval miss, not a claim that the genus is unmeasured.

OpenAlex's shared daily budget ran out after the initial 20 searches; shorter follow-up and citation-list requests returned HTTP 429. Reviews or later citing papers supplied the citation steps instead. Several publisher or repository PDFs returned 403, and some Europe PMC fullTextXML requests returned 500. Supplemental web searches were used for source-location retrieval and the remaining Onitis search, in addition to the prescribed scholarly APIs. No values were accepted from search snippets, ResearchGate, Academia.edu or unverified mirrors. These access limits and the supplemental search are disclosed so this run is not mistaken for an unrestricted API-only comparison.

The test remained blind: no existing evidence logs, genus records, scoring script or other content under `docs/views/` was opened or searched; only the permitted `docs/views/research/THOROUGH.md` was read. No app setup, build, server or app tests ran. Only the two requested medium result files were written in the repository.
