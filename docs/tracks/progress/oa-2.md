# Open-access batch 2

Checkpoint: 2026-10-14, branch `research/oa-2`. Stopped between papers after rank 99 under the research brief’s context-limit rule. App setup, builds, servers and app checks were skipped.

- Entries checked: 79 (ranks 80–158), with all discovery completed before reading.
- Entries with legal free-copy candidates: 38; these are indexed locations, not verified successful downloads.
- Complete sources read: 6 (one dataset, five papers).
- Evidence records logged and quote-verified: 3,314.
- Negative index results: 39, in `docs/views/sources/oa-none-2.jsonl`; this does not prove that no legal copy exists.
- Identity lookups unresolved: 2 (87 and 120), excluded from the negative-copy log.
- Found candidates attempted but inaccessible: 4; other candidates awaiting reading: 28.

| Rank | Source | Records | Reading and limitations |
| --- | --- | ---: | --- |
| 80 | Amphibian pupil dataset | 2,240 | Complete 1,293-row CSV and documentation. Adult and larval pupils kept separate; NA excluded; larval `none` not interpreted as measured absence. Binary diurnal=no is not converted to nocturnal. Eye diameters explicitly identified as compiled from earlier measurements. |
| 83 | Toad low-light vision | 46 | All 12 scanned pages and tables. OCR numerical errors corrected against page images. Behavioural thresholds, neuronal thresholds, integration time, latency, gaze and snapping accuracy distinguished; secondary values labeled. |
| 84 | Pupil shapes | 447 | Main XML, complete supplementary PDF, 214-species table, original analysis matrices and both movies. Matrices cross-checked against Table S1; binary recodings and reconstructed ancestors excluded. |
| 93 | Five honeybee species | 115 | Complete XML, Table 1’s 15 sex/caste rows, figures and references. Morphology logged without converting counts or diameters into acuity or sensitivity. No supplements listed. |
| 94 | Bird UV sensitivity | 315 | Complete XML and 310-row Word supplement, labeled Additional file 1 in the publication (batch says Additional file 2). Blank Type excluded; question marks and paleognath exceptions retained. Genotype-based tuning assigned grade g, without claiming measured peaks or behavioural colour vision. |
| 99 | Tropical seabird fields | 151 | Complete XML and supplementary DOCX; every measured S1/S2 cell logged. Missing cells remain missing. Binocular overlap, blind gaps and vertical extent distinguished; discrepancies and ambiguous coordinate labels documented. |

Access limits: rank 81’s PMC manuscript is listed as free, but XML/PDF-render returned 500 and PMC HTML returned a bot challenge. NCBI BioC returned 429 and that host was not retried. Rank 86’s indexed journal PDF and rank 97’s Karger PDF returned 403. Rank 92’s Dryad page opened, but all three resource downloads returned 403 and its API query returned 404. None is marked read or labeled as lacking a legal copy.

Resume at rank 100 (negative index result), then rank 101 (next candidate). The full discovery responses and helper scripts are in `/tmp/oa`; regenerate lookups for unread entries if the machine is replaced. Skip DOI/title pairs already in `docs/views/sources/oa-2.jsonl`.

Rank 101’s preprint PDF, rank 102’s landing page, rank 103’s XML and rank 104’s landing page were retrieved but not read. Rank 101’s batch DOI is a Dryad dataset DOI: verify the document’s own DOI/version, and do not mark a dataset read from a preprint alone. Ranks 87 and 120 still need the required title/first-author/year match after corrected comma-containing queries; rank 87 lacks authors and has year 0.

Pending candidate ranks: 101, 102, 103, 104, 105, 109, 110, 113, 116, 117, 118, 119, 122, 123, 125, 126, 128, 130, 132, 135, 137, 141, 143, 146, 153, 154, 156, 158.

All records were appended with `addlog.py`; all quotes passed `quotecheck.py` against retrieved source text, visually verified scan transcripts, or extracted PDF table layout. Rank 84’s categorical rows fail the PDF prose-order path but all 283 pass against its `pdftotext -layout` text. Source counts reconcile exactly with the evidence log.

Only the four files authorized by `oa-pass.md` changed: this summary, `docs/views/evidence/oa-2.jsonl`, `docs/views/sources/oa-2.jsonl` and `docs/views/sources/oa-none-2.jsonl`. PDFs, full text, XML, metadata caches and scripts remain outside the repository. No pull request was opened.

## 2026-10-16

Assigned entries checked: 24 (2, 7, 13, 18, 22, 31, 37, 39, 41, 44, 46, 47, 49, 51, 53, 56, 58, 62, 64, 67, 74, 75, 77, 79). Discovery was completed before reading. OpenAlex and Europe PMC responses were saved outside the repository; Semantic Scholar refused the first request with HTTP 429 and was not retried. Later round-wide refusals also stopped OpenAlex, Crossref and the refusing publisher/repository domains. No app setup, builds or app checks ran.

- Free-copy candidates located: 23, including index/author candidates whose files remain inaccessible; this is not 23 successful downloads. Twelve usable main texts were downloaded and read. Rank 132 has conflicting index availability labels; its indexed free Karger candidate remains unverified behind HTTP 403.
- Complete sources read this round: 10; cumulative complete sources: 16.
- New evidence records logged and quote-verified: 770; cumulative evidence records: 4,084. Of the new records, 700 belong to the ten completed sources, 62 are from a main text with an unread supplement, and eight are explicitly partial abstract records.
- Terminal access outcomes: 13 `free copy inaccessible`, one `lookup unresolved`; these do not assert absence of a lawful free copy. No new `no free copy` verdicts. All 24 assigned entries have a completed-source or explicit terminal-outcome line; inaccessible wanted papers remain active because skipped lines are not counted as complete readings.

| Entry / rank | Completed source | New records | Reading and limitations |
| --- | --- | ---: | --- |
| 2 / 81 | Spectacled caiman retina | 4 | Complete accepted manuscript via PMC HTML. Anatomical acuity estimate, guanine tapetum, absent cone oil droplets and acute zones; hypothesized tetrachromacy excluded. |
| 31 / 110 | Mammalian colour-vision review | 111 | Full 11-page review and Table 1. Genus-level cone complements and spectral bands remain group evidence; no genus number promoted to species. |
| 39 / 118 | Great horned owl photoreceptors | 7 | Complete university-repository PDF. Oil-droplet morphology, size, photoreceptor proportions and descriptive activity; presumed colourlessness not treated as a measured spectrum. |
| 44 / 123 | One thousand plant transcriptomes | 0 | Main paper, methods, figures and 13 free supplements inspected. Phylogenomics without a sensory-trait measurement. |
| 46 / 125 | Phytochrome diversity | 382 | Complete main paper and supplementary PDF. 380 taxon/phylogenetic-clade sequence-presence records and two broad-group photoconversion bands; gene homology stays grade g and does not prove a functional sensory response. |
| 47 / 126 | Plant photoreceptor overview | 43 | Complete published repository version, visually checked Fig. 3 gene-count matrix and publisher supplementary figures 8–9. Putative receptors and Pinus figure/prose discrepancy retained; no supplementary table link exposed. |
| 49 / 128 | Retinal topographic maps chapter | 95 | Full publisher chapter, four tables and figures. Twelve original snake species distinguished from review/group figures; alternative hexagonal/square acuities retained separately. Eye-size and PND assumptions explicit. |
| 62 / 141 | Anole oil droplets | 34 | Complete article and figures. Exact reported proportions/densities, ratios and distribution/topography; excluded foveal tissue and pooled droplet classes do not imply spectral receptor counts. Earlier pigment spectra remain secondary. |
| 64 / 143 | Light-environment primer | 15 | Complete primer and both figures from author PDF. All secondary/group records grade g; giant-squid group maximum not assigned to individual species. Adjacent unrelated articles excluded. |
| 75 / 154 | Cryptochrome compass model | 9 | Full main paper and 17-page author-hosted supplement, all five supplementary figures. Seven secondary observations grade g; two explicit model predictions grade i. Computed protein disorder and hypothetical visual modulation are not measured avian spatial acuity or observed magnetic appearance. |

Incomplete readings: entry 37/rank 116 main paper read, but free species-table supplement blocked; no completed-source row. Entry 51/rank 130 accepted-manuscript main paper read and 62 records logged, but free supplementary PDF remains behind a download challenge, so no completed-source row. Entries 56/rank 135 and 58/rank 137 contributed five and three abstract-only records respectively (`partial:true`, `access:abstract`); their full papers remain unread.

Other terminal outcomes are entries 7, 13, 18, 22, 41, 53, 67, 74, 77 and 79. Dryad files were not replaced by related article/preprint content. Entry 41's exact-title/year Crossref DOI candidate lacks author metadata to finish identity verification; no free-copy absence inferred. Entry 77's JSTOR PDF returned HTTP 420 and later citations disagree on the author; verify the actual first page. Terminal rows list actual checked sources and retrieved candidate/file URLs, the response or availability problem, unread scope and manual-acquisition need. No challenges were bypassed.

All 770 new quotes passed `quotecheck.py` against the actual downloaded PDF, extracted full text or visually checked figure transcription before their evidence commits. All evidence was appended with `addlog.py`; completed-source record counts reconcile with the corresponding evidence and exclude the 70 incomplete-text records. Papers, metadata caches, source text, figure images and helper scripts remain under `/tmp/oa/oa2-round`, outside the repository. Only this batch's four authorized files were changed.
