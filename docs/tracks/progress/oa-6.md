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

## 2026-10-17

User-facing research date: 16 October 2026; work and retrieval timestamps use UTC 17 October. Initial discovery checked all **60 assigned unresolved entries** with one Europe PMC DOI/title-search script. All 60 returned HTTP 200; OpenAlex, Semantic Scholar and Crossref were skipped because the shared round registry already recorded HTTP 429. General web searches were then used to recover legal repositories. No app, build or test checks were run.

Checkpoint through assigned entry **45**: **32 entries processed**, **1 legal full paper read**, **140 full-text records** and **11 new abstract-only records**, **26 actual limited-search no-copy outcomes**, and **5 indexed/free candidates technically inaccessible** (entries 8, 14, 26, 31, 41). Inaccessible entries are explicitly marked `skipped: free copy inaccessible`, carry actual candidate URLs/reasons, and remain unread/manual acquisition; they have no full-read marker. Abstract additions are from entries 36, 39 and 42 and all carry `partial: true`. One drone contrast estimate is grade `i`; the unnamed five-sciurid pigment summaries are grade `g`.

Entry **45**, *Retinal regionalization and heterogeneity of butterfly eyes*, was read in full from Groningen's publisher-version PDF. Tables 1 and 2 were checked visually. The 140 records contain 33 interommatidial angles, 33 facet diameters, 33 reported eye parameters, 11 frontal acute zones, 27 named-species tapetal-eyeshine observations, and 3 secondary/family statements (grade `g`, original sources named). Table 2's apparent spelling errors in rows 7, 9 and 10 are linked explicitly to the correct Table 1/figure species. Regional eyeshine colours are not treated as receptor sensitivity peaks. New anatomical trait keys distinguish facet diameter and the reported eye parameter from rhabdom diameter, angular sampling and f-number. All 140 quotes passed against a text assembled solely from the PDF's verbatim normal and layout extractions; all 11 partial quotes passed against the retrieved abstracts.

New refused hosts, reported to the coordinator: `connectsci.au` HTTP 403; `researchspace.auckland.ac.nz` JavaScript anti-bot challenge; `www.oceanfirstinstitute.org` and `www.bdbotsociety.org` HTTP 406; `stinchcombe.eeb.utoronto.ca` proxy CONNECT 403. No retry after refusal. UMass entry 51 and ANU entry 52 have actual download links but return login/request-copy pages; no access restriction was bypassed. Entry 63's Nebraska full-paper PDF was downloaded but is **not yet read**. Entry 73's actual Zenodo API record resolves to version 6360448 and supplies an 81-page review; it is **not yet read**. Downloading or finding a file is not a full-read claim.

At this checkpoint, continue with assigned entry **46**. Raw files, API responses and scripts are outside the public repository in `/tmp/oa/oa-6`. Commit for the entry-45 full read: `4e18f3a6`.
