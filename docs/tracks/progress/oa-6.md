# Open-access batch 6

## 2026-10-14

This round settled **6 of 79 papers**, logged **659 records**, and leaves **73 papers remaining**. The settled entries are **1, 2, 18, 32, 34 and 35**. Entries 1 and 2 have no free copy after the required lookups; four papers have verified legal full copies and were read in full. No app checks were run.

| Outcome | This round |
|---|---:|
| Entries processed by the initial lookup script | 79 |
| Actual OpenAlex requests before its throttle | 3 |
| Europe PMC DOI searches | 54 |
| Semantic Scholar DOI searches | 54 |
| Entries with candidate URLs from that script | 27 |
| Verified free papers read in full | 4 |
| Papers settled as no free copy | 2 |
| Full-text evidence records | 624 |
| Abstract-only evidence records | 35 |
| Total evidence records | 659 |
| Papers still unresolved or unread | 73 |

The full reads and their record counts are:

- Entry 18: 325 records. The HAL publisher-version PDF and the S10 XLSX and S11 statistical supplements were read. The batch title is a French description; the linked record identifies the published English article, *A flashing light may not be that flashy*, DOI 10.1371/journal.pone.0279718. The source marker retains the exact batch title.
- Entry 32: 86 records. The Europe PMC XML, publisher PDF, spreadsheet supplement and figures were read. Figure 2's eye-type symbols were checked visually. The supplement reports gene-copy numbers, which were not converted to receptor spectral-class counts.
- Entry 34: 100 records. The complete public proceedings HTML and all seven table/figure images were read. Table 1's species rows were transcribed and checked visually. Retinal and optical fields, binocular width and vertical extent, monocular and cyclopean fields, and optic-axis divergence remain distinct. Differences between prose and table values are recorded explicitly.
- Entry 35: 113 records. The complete public proceedings HTML and all seven table/figure images were read. Table 1's pigment peaks were transcribed and checked visually, including the wrapped UV column. Pigment absorbance, effective filtered sensitivity, behavioural sensitivity and template/sequence labels are distinguished. Prose/table differences are retained with location notes; possible pigeon UV mechanisms are not claimed to establish pentachromatic colour vision.

The 35 partial records come from nine abstracts: entries **4, 13, 15, 17, 19, 25, 26, 30 and 31**. Every one carries `partial: true` and source access `abstract`. These papers remain unresolved and have no full-read marker.

OpenAlex returned HTTP 429 at entry 3, so subsequent requests to that host stopped. Entries lacking a DOI could not receive a title/first-author/year-verified OpenAlex match after that point. Missing candidates, skipped queries, failed downloads, robot pages and HTTP errors were **not** treated as evidence that no free copy exists. The coordinator subsequently reported the shared Semantic Scholar throttle; no further requests were made. Entry 33's linked PMC PDF returned an HTML robot page and its Europe PMC XML route failed, so it remains unresolved.

Entry 18's dataset contains 200 retained rows and 26 excluded rows. One excluded row gives no value; the other 225 rows have records with the review's risk-of-bias codes and original-study metadata. Ninety additional values in comment cells and ten group aggregates are separate records. Excluded results are explicitly identified. The beetle 300–500 Hz result is recorded as an infrared pit-organ response, not visual flicker fusion. A sheep result reported in frames/second retains that unit. Genus and aggregate records have grade `g`; the final log contains 588 `m` and 71 `g` records, with no higher-rank record graded `m`.

All 659 records passed `quotecheck.py` against the downloaded text/PDF or a faithful, visually checked table/figure transcription, followed by `addlog.py` validation. Downloaded papers, XML, spreadsheet files, image tables, extracted text, scripts and API responses remain outside the repository under `/tmp/oa/oa-6`.

Stopped at the requested clean boundary after entry 35. Resume with **entry 36**, keeping unresolved earlier entries **3–17, 19–31 and 33** pending. Entries **36–79** have initial lookup responses and some downloaded candidate files but have not been read in this round. Do not infer full-read status from a cached download.

Commits before this final checkpoint: `e9a2000`, `cca37f8`, `67f99a8`. The coordinator handles the shared branch's push and pull request.

## 2026-10-16

Round in progress. All 73 assigned entries are receiving initial OpenAlex, Europe PMC and Semantic Scholar lookups. Semantic Scholar returned HTTP 429 at entry 13 and was stopped for the round. Five earlier entries (4, 5, 7, 9 and 12) returned no free-copy candidate from the completed three-provider lookups and are settled as no free copy. No new evidence records or full-read markers yet. Remaining entries stay queued when discovery or downloads fail; errors are not no-free outcomes.

Entry 33 has now been read in full (eight-page publisher PDF via Europe PMC). Its primary measurements concern eye and skull dimensions and allometric scaling, with no measured value of the listed sensory traits: 0 evidence records. The paper does not supply species-level acuity from eye diameter, and none was inferred.

Entry 40 read in full with all three figures, the stimulus-spectrum supplement and all 75 rows of S1 Table: 90 records. Individual light-level thresholds remain separate from maxima and species means. Results-section means (130.3, 128.1, 138.2 Hz) differ from the abstract and are retained with that discrepancy noted. Five previously published animal thresholds and a human range are explicitly secondary reports; pigeon ERG is distinct from behavioural thresholds. Quote checks passed for all 90 records.

Entry 53 read in full (46-page thesis and tables/figure captions): 17 records. Marmota marmota has a horizontal oval pupil, yellow lens, peripheral corneal pigment, no tapetum and a cone-dominated retina with a sparse rod population. Retinal thickness and the blind optic disc are kept distinct from a sharp visual streak; no acuity, field width or spectral-class count was inferred. Comparative natural-history and lens-chemistry reports are marked secondary. All 17 quotes passed against the PDF.

Entry 56 read in full with the supplementary figures and materials table: 51 records for all 48 experimentally tested species. Flowering classifications stay distinct from day-neutrality, low-power comparisons and complete failure to flower. Dactylis glomerata NGB7723 is long-day responsive after vernalization; Bromus catharticus and B. hordeaceus were not measured. Ehrharta calycina’s follow-up failure contrasts with its initial short-day classification and is logged separately. Main-text taxon misspellings were checked against Supplementary Table S1. All 51 quotes passed.

Entry 31 was retrieved late from the HAL file link and its complete main text was read: 155 partial records from all 52 rows of Table 1, comprising 32 primary species rows and 20 explicitly secondary study rows. Peak contrast sensitivity, its spatial-frequency position, and high-frequency CSF cutoff use distinct keys; the cutoff is not treated as static-pattern acuity and may be extrapolated. Original publisher title says “many phylogenetic orders”; the source marker preserves the exact batch title (“most”). HAL supplied the publisher PDF. Publisher supplements and Harvard Dataverse raw data were inaccessible (403). Table S3 bandwidths, Table S1 conditions/nonresponders and Dataverse trial thresholds remain unread, so the full-read marker was withheld and all 155 records carry partial:true (source access remains open). Entry 31 stays queueable; no values were invented from its supports. All 155 quotes passed the PDF table check.

Entry 58 read in full, with Table 1, all figure captions, Figure 3 and the linked Figshare dataset/readme: 15 records. Theopropus elegans and Popa spurca support three candidate ERG pigment components, Hymenopus coronatus two; these are physiological/model inferences, not demonstrated behavioural color vision. Eight fixed template peaks remain distinct from the observed adaptation-dependent peaks. The two aggregate ranges are grade g with all three species named. Mantis religiosa was not measured. Testing range, assumed photoreceptor length and normalized amplitudes were not converted to visual thresholds. All 15 quotes passed.

Entry 59 read in full (20-page publisher PDF): 17 records. Compound-eye and median-ocellus ERG peaks remain separate, including dorsal versus ventral compound-eye recordings. The ocellus supports at least two inferred components; compound-eye monochromacy is not declared because rare extra receptor classes were explicitly not excluded. Secondary Mantis religiosa results are labelled as such, and the coarse-filter localization caveat is retained. All 17 quotes passed.

Entry 60 read in full (five-page paper): 4 records of new-bud opening and pollen-release rhythms in Hepatica nobilis. First opening of buds is distinguished from repeated daily flower movement; no isolated light-response mechanism is claimed. The conclusion’s 09:00 pollen-release start conflicts with 10:00 in the results and abstract; both statements are labelled. H. acutiloba and H. americana were not measured. All 4 quotes passed.

Entry 62 read in full, including all nine appendix tables: 35 secondary records, all grade g. Table 1 supplies 34 CFF values with ERG/behavioural and optimum/suboptimum codes preserved. The high/low light labels describe normal habitat/foraging environments, not measured stimulus luminance; the 25 °C correction applies to metabolic rates, not CFF temperature. Cat 55 Hz is labelled ERG while its cited primary title says Behavioral methods, and harp-seal 32.7 Hz points to the cat reference rather than the separately listed seal study. These source discrepancies remain explicit and unresolved. One tiger-beetle motion-behaviour record is also secondary. All 35 quotes passed. This round’s other explicitly secondary reports were conservatively set to g; direct species measurements remain m. Earlier-round records were unchanged.

### Final checkpoint for 2026-10-16

Stopped cleanly between entries after entry 62, before starting extraction from the 81-page entry 73 review, to preserve room for a complete source-by-source extraction in a fresh context. All 73 assigned entries received initial discovery checks; checked does not mean resolved.

| Outcome | This round |
|---|---:|
| Assigned entries checked | 73 |
| Verified legal free full copies retrieved | 10 |
| Papers completely read and settled | 8 |
| Additional main texts read with missing supports | 1 |
| Evidence records logged | 384 |
| Records from complete reads | 229 |
| Partial-main-text records | 155 |
| Abstract-only records added | 0 |
| Papers settled as no free copy | 5 |
| Newly settled queue entries | 13 |
| Papers still queueable | 60 |
| Cumulative oa-6 evidence records | 1043 |

Full reads settled this round: **33, 40, 53, 56, 58, 59, 60, 62** (respectively **0, 90, 17, 51, 15, 17, 4, 35** records). No-free entries: **4, 5, 7, 9, 12**. The 384 records comprise **272 m** direct species measurements/descriptions and **112 g** secondary or aggregate reports. All 155 entry-31 records have `partial:true`; its full-read marker was removed, so entry 31 remains queued. Earlier-round records and outcomes were preserved.

Remaining entries, exactly: **3, 6, 8, 10, 11, 13, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 36, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 54, 55, 57, 61, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79**.

Discovery limits: Semantic Scholar returned HTTP 429 at entry 13 and was not called again. OpenAlex title queries were corrected and title/first-author/year matches verified before accepting recovered DOI identities. Entries without an accepted match, incomplete provider coverage, failed publisher downloads, inaccessible repositories, and bot pages remain unresolved. Five no-free markers are backed by completed provider responses before the throttle. ANU entry 52 explicitly requires a copy request; no request was sent. No library login, proxy library, unauthorized host, ResearchGate or Academia.edu copy was used.

Readable material pending: entry **73**, verified publisher PDF from `https://zenodo.org/records/6360448/files/source.pdf`, is saved as `/tmp/oa/oa-6/2026-10-16/73/more-0.pdf`; first-page title/author/date match. Its 81 pages have not been read or logged. Entry **31** still needs its publisher supplementary methods/tables and Dataverse trial data; the complete main text and all Table 1 rows were read. Entry **72** returned errors from Europe PMC full-text/PDF routes; its Nature page opened only the abstract, references and figure thumbnails, with access options for the main text. It remains queued and received no full-read marker or new record.

Source discrepancies retained for review: entry 40’s abstract means differ from its results; entry 60’s conclusion starts pollen release at 09:00 while the results/abstract say 10:00; entry 62 labels cat 55 Hz ERG despite citing a primary title saying Behavioral methods, and maps the harp-seal value to that cat reference although a seal reference is separately listed. These were not silently corrected. The primary cat paper remains unopened.

Verification: every new quote passed `quotecheck.py` (229 verbatim and 155 faithful table-row matches; 0 failed). `addlog.py` accepted every record and the batch-only evidence validator reported **1043 records, 0 problems**. No app build, server, browser or app tests were run. Only the four permitted oa-6 evidence/source/progress files were changed. Downloads, XML, PDFs, spreadsheets and extracted text remain outside the repository; scratch scripts remain under ignored `work/`.

Temporary quote-check map (record file → source file; all under `/tmp/oa/oa-6/2026-10-16/`):

- `40/records-main.jsonl` → `40/copy-0.txt` (15 verbatim, 0 table rows, 0 failed).
- `40/records-table.jsonl` → `40/s003.txt` (75 verbatim, 0 table rows, 0 failed).
- `53/records.jsonl` → `53/more-0.pdf` (17 verbatim, 0 table rows, 0 failed).
- `56/records.jsonl` → `56/more-0.txt` (51 verbatim, 0 table rows, 0 failed).
- `31/records.jsonl` → `31/last.pdf` (0 verbatim, 155 table rows, 0 failed).
- `58/records.jsonl` → `58/copy-0.txt` (15 verbatim, 0 table rows, 0 failed).
- `59/records.jsonl` → `59/more-0.pdf` (17 verbatim, 0 table rows, 0 failed).
- `60/records.jsonl` → `60/more-0.pdf` (4 verbatim, 0 table rows, 0 failed).
- `62/records.jsonl` → `62/copy-0.txt` (35 verbatim, 0 table rows, 0 failed).

Resume in batch order among accessible pending sources: finish entry 31’s supports, obtain a readable full copy of entry 72, then read entry 73; retain every other unresolved entry above for a fresh discovery round after provider access recovers.

Commits before this final progress checkpoint: `0b6a2cc`, `abdc5b6`, `61f000e`, `82d5b62`, `9632db9`, `8d7f6fd`, `dee5446`, `ed4c7da`, `3b2dbf3`, `a1187dc`. The coordinator handles the shared branch’s push and pull request.
