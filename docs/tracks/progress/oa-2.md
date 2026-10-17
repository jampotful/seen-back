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

Discovery completed for all 34 assigned entries before reading. OpenAlex and Europe PMC returned 29 entries with indexed free-copy candidates; five entries have no candidate or unresolved identity. Semantic Scholar returned HTTP 429 on entry 7 and was not retried. Missing candidates therefore remain queued, with no new no-free-copy declarations.

Checkpoint: one complete paper read (entry 8, rank 87), 37 records appended and quote-verified. Title and supplied PMC identifier resolve the batch’s missing author/year to Gutiérrez et al. 2024. All ten figure captions and full body read; no supplementary files listed. Anatomical spacing is kept distinct from behavioral acuity, pooled acceptance angles are grade g, and cited comparisons are labeled secondary. Entry 2’s XML returned 500 and PMC HTML was a browser challenge; it remains queued. Downloads are in `/tmp/oa/oa-2`, scripts untracked in `work/`.

Entry 23 (rank 102), Gilbert’s 1985 cattle thesis: 84 records. Read the thesis and seven tables; all 62 nonmissing Table 1 response cells, eight Table 2 response means, and eight Table 6 trial means logged. Three scanned numerical tables were checked visually; quotes pass against the extracted text plus a visually checked table transcript. Green is 535 nm in the abstract/methods and 531 nm in tables/results, retained in every relevant note. Inconsistent prose/abstract values are not substituted for table cells. The study does not establish cone dimensionality or a brightness-independent discrimination test. Dryad datasets at entries 13 and 22 opened, but their resource downloads returned 403; neither dataset is marked read.

Round checkpoint: 34 checked; 29 indexed candidates; 2 complete sources read; 121 new records; 0 new no-free declarations; 32 assigned entries remain queued.

Entry 24 (rank 103), Toomey et al. 2016: complete main XML, all figure-supplement captions, three supplementary DOCX tables and three source-data XLS workbooks retrieved. Logged 417 records: 45 whole-retina composition ratios, 45 tuning classes, 144 compiled optical/pigment parameters, 119 individual-droplet spectral-fit contributions, 57 developmental pigment concentrations, four droplet descriptions and three group-level statements/model optima. Sequence classes, secondary model inputs, and pooled model predictions are grade g; fit proportions are labeled fitted spectral contributions. The table’s ratio denominator conflicts with the figure/method wording, so both labels are retained without recalculation. Ocular-media approximations in three species remain explicit. The worksheets’ analyte codes are preserved without guessed chemical assignments. Continuous absorbance traces, enzyme qPCR values and hypothetical spectral sweeps were inspected as supporting data and are not converted to measured animal-vision traits.

Round checkpoint: 34 checked; 29 indexed candidates; 3 complete sources read; 538 new records; 0 new no-free declarations; 31 assigned entries remain queued. Wasp source metadata now includes the retrieved journal and volume.

Entry 25 (rank 104), phytochrome Dryad dataset: retrieved its legal Zenodo mirror, complete alignment/tree archive and probe FASTA. README and all alignment/tree/probe file structures inspected. These are sequence alignments (423 global protein sequences, 97 bryophyte, 113 fern/lycophyte and 111 neochrome nucleotide sequences), phylogenetic trees and 7,502 bait sequences. They contain no direct sensitivity, spectral maximum, behavioral threshold or sensory-organ measurement to log. Gene-tree membership is not converted into measured light sensing: zero records. Dataset is marked read independently of the linked research article at entry 46.

Entry 26 (rank 105), comparative felid morphology: full main XML and all ten tables read, 110 records logged. All 100 ocular dimension/histology cells from Tables 4 and 5 logged; pupil outlines, cellular tapeta, post-mortem tapetal colors and lion iridic granules kept distinct. These are four cadavers, not species reference populations. Every relevant note preserves n=1 per sex/taxon and distinguishes six technical repeats from biological replication. Round/ovoid pupil observations are post-mortem at rest and do not establish a live constricted aperture. Supplementary literature-summary DOCX could not be retrieved because its publisher CDN returned a proxy 403; it is not claimed read.

Round checkpoint: 34 checked; 29 indexed candidates; 5 complete main sources/datasets read; 648 new records; 0 new no-free declarations; 29 assigned entries remain queued.

Abstract-only evidence: 19 records from entries 2 (3), 7 (5), 51 (4), 56 (5), and 58 (2), all partial=true, access=abstract, and quote-verified against the retrieved Europe PMC core abstract. These five sources remain queued for full reading and have no full-read marker. They include two reconstituted manatee pigment peaks (555/410 nm), intensity-matched cattle discrimination, caiman tapetum/retinal specialization, and salticid opsin expression without asserting behavioral color vision. No-free-copy declarations are withheld because discovery or download restrictions leave the full-copy question unresolved.

Round checkpoint: 34 checked; 29 indexed candidates; 5 complete main sources/datasets read, 5 additional abstracts read; 667 new evidence records; 0 new no-free declarations; 29 assigned full-source entries remain queued.

Entry 34 (rank 113), Nilsson’s eye-evolution review: full main text, figures and its theoretical parameter table read. Logged 28 explicitly secondary descriptions of eyes, nonvisual receptors, eye roles, and two counts. No model assumptions (integration times, detection angles or hypothetical intensities) are logged as measured species traits. Broad taxa remain grade g, larval and adult box-jellyfish organs are separated, and proposed scallop retinal roles retain the author’s uncertainty. No supplements listed. Entries 30 and 31 remain queued after Europe PMC XML errors and publisher/PMC challenges.

Round checkpoint: 34 checked; 29 indexed candidates; 6 complete main sources/datasets read, 5 additional abstracts read; 695 new records; 0 new no-free declarations; 28 assigned full-source entries remain queued.
