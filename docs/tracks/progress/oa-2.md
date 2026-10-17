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

## 2026-10-17

Discovery checkpoint for the 26 entries assigned this round: positions 2, 7, 13, 18, 22, 30, 31, 37, 39, 41, 43, 44, 46, 47, 49, 51, 53, 56, 58, 62, 64, 67, 74, 75, 77 and 79. OpenAlex and Europe PMC lookups completed before reading. Semantic Scholar returned HTTP 429 at position 13; further requests to that host stopped. Unresolved lookups and blocked free-copy candidates are kept pending, rather than newly declared unavailable. Downloaded papers and scripts are outside the repository in `/tmp/oa2-20261017`. Reading and record counts follow at the final checkpoint below.

Final checkpoint for this round:

- Assigned entries checked: 26. OpenAlex indexed an OA location for 21; position 39 additionally supplied a repository link, giving 22 legal-copy candidates to attempt. Four entries had no indexed OA location; incomplete Semantic Scholar coverage prevents a definitive new no-copy finding.
- Full texts successfully retrieved: 9, at positions 22, 30, 43, 44, 46, 47, 49, 62 and 74. A retrieved paper is not counted as read merely because it downloaded.
- Complete papers read and retired: 2 (positions 30 and 43; ranks 109 and 122).
- Records added: 122, all appended with `addlog.py` and all quotes verified with `quotecheck.py`. The evidence log now contains 3,436 records. Both sources are secondary compilations; every added record is conservatively graded `g`.
- New definitive no-free-copy lines: 0. The existing negative-copy log was unchanged.
- Assigned entries remaining: 24, positions 2, 7, 13, 18, 22, 31, 37, 39, 41, 44, 46, 47, 49, 51, 53, 56, 58, 62, 64, 67, 74, 75, 77 and 79. Access failures and unread downloads remain pending.

| Position (rank) | Source read this round | Added records | Reading and caveats |
| --- | --- | ---: | --- |
| 30 (109) | Hunt et al. 2009, visual-pigment evolution | 88 | Complete PMC HTML, tables, figures/captions and references. Secondary pigment measurements, cone classes and oil droplets. Original citations are named in notes and not claimed opened. Table 1 jointly attributes several studies without mapping each row to one study; this limitation is explicit. Genus/group rows remain group evidence; allelic variants do not imply every individual has all listed peaks. In vitro expression is identified where the passage states it. |
| 43 (122) | Healy et al. 2013, temporal perception | 34 | Complete XML, Table 1, figures/captions and complete in-article appendix. Every Table 1 CFF value logged, with ERG/behavioral method and optimum/suboptimum protocol flags. H/L habitat coding is not experimental illumination or a diel classification. Tupaia glis versus the cited T. belangeri title and the harp-seal citation-number mismatch are explicitly unresolved in notes. |

Access detail: Semantic Scholar returned 429 on the third request, position 13, and was not queried again. NCBI BioC returned 503 on one supported-endpoint attempt and was not retried. PMC manuscript requests mostly served bot pages; Europe PMC XML returned 500 for those manuscripts. Both Dryad datasets opened as landing pages, but all listed data-file downloads returned 403. Journal/repository candidates also produced 403, 404, proxy errors or challenges; none was mislabeled as a completed read or definitive no-copy result.

Resume information: the downloaded paper associated with position 22 is the ant article (DOI 10.1371/journal.pone.0257779), not proof that the requested Dryad dataset was read. Positions 44 and 46 had their main texts inspected, but supplements remain unread and no completion lines were added. Their supplement ZIP files did download before the round closed. Other downloaded papers have not been read. All raw responses, PDFs, extracted text and helper scripts are in `/tmp/oa2-20261017`; regenerate when that temporary directory is unavailable. Stop was between completed source records after the research round's rate-limit close instruction. No app setup, builds, servers or app tests ran.
