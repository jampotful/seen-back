# desk-d519 progress

evidence_intake: evidence-kind-v2
intake_base: 7b43aedc64c70645d8c5be9827c6b01d42ac5e28

Angle used: the later ANGLE in the brief (Jung et al. 2014 remaining molossids, then Pontoporia), sense_echolocation, physiological_response, one record per parameter. The earlier reptile/fish ANGLE paragraph got three searches only (no fileable reptile found, see below). About 21 WebSearches. 64 records in docs/views/evidence/desk-d519.jsonl; check.py plain and --require-evidence-kind: 0 problems for this file.

## Filed
- Jung K, Molinari J, Kalko EKV 2014, PLoS ONE 9(1): e85279, 10.1371/journal.pone.0085279 (PMC PDF, CC BY printed): start frequency, end frequency and call duration (mean +- 1 SD, NC/NS in conditions), 20 call-type rows x 3 = 60 records: Molossops temminckii (Low, High, High II), Molossops neglectus (Low, High), Molossus molossus (Low, Middle, High), Molossus sinaloae (Low, Middle, High), Molossus rufus (Low, High), Cynomops planirostris (Low, High), Promops nasutus (Low), Eumops glaucinus (Low, High), Eumops auripendulus (Low, High). MDD pages 1005193, 1005192, 1005202, 1005206, 1005205, 1005172, 1005258, 1005182, 1005174, opened from own search results. Reached by the unfiltered search: Neotropical bat echolocation call parameters species table Phyllostomidae OR Emballonuridae OR Molossidae open access Scientific Reports OR PeerJ OR PLOS ONE call duration peak frequency mean (result: rcastoragev2.blob.core.windows.net .../PMC3891751.pdf, PMC's PDF storage; the pmc.ncbi.nlm.nih.gov/articles/PMC3891751 page is the one cited in source.url, as d518 did).
- Bittencourt L, Carvalho RR, Pereira K, Santos-Neto EB, Lailson-Brito J Jr, Bisi TL, Azevedo AF 2025, Front Mar Sci 12: 1641888, 10.3389/fmars.2025.1641888 (CC BY printed), Pontoporia blainvillei, MDD 1006457: Table 2 peak frequency and click duration for click trains (n = 55 clicks) and click packets (n = 34 clicks), 4 records. The n question for the text sentence "mean peak frequency of 132.4 +- 6.8 kHz" is NOT resolved by the paper (no n printed; the weighted mean of the two Table 2 PeakF means with n = 55 and 34 gives 132.4, which is an inference); that sentence is not filed. The Table 2 column headers print n = 55 and n = 34, so the Table 2 rows are filed with those n. Reached by: Bittencourt 2025 Pontoporia blainvillei franciscana echolocation clicks peak frequency 132.4 kHz Frontiers in Marine Science (result: public-pages-files-2025.frontiersin.org .../pdf).

## Weak spots
- The reader extracts the PMC PDF with the plus-minus sign as "6" (32.661.7 = 32.6 +- 1.7). Decoding confirmed by the Table 3 footnote ("mean 61 standard deviation") and start/end/bandwidth arithmetic in every filed row; the quote keeps the extracted form. The PLoS/PMC HTML page was not reached, so the symbol itself was not seen.
- Number of individuals is not stated in Jung et al.; SD is across calls; calls within a sequence are not independent. Frontiers pages came through the reader as quoted fragments.
- MDD pages for Molossops temminckii, Molossus rufus and Cynomops planirostris print no explicit Living/valid line in the reader text (status blank, IUCN printed); noted per record.

## Not filed and why
- Molossus currentium (3 rows): start minus end frequency does not match printed bandwidth in any row (e.g. 29.7 - 24.4 = 5.3 vs 4.3); possible print or extraction error, held back.
- Nyctinomops laticaudatus: Low row mismatch (26.7 - 23.6 = 3.1 vs 2.4); Middle row consistent but the species is held back as a whole; High row has NC 9 below NS 10.
- Promops centralis: NC 12 vs NS 13 (Low) and 7 vs 9 (High II); unresolved from the paper, skipped. Promops nasutus High II (2 calls, SD 0.0) and Molossops neglectus High II (3 calls) skipped as too thin.
- Eublepharis jhuma (Herpetozoa 39: 161-176, 10.3897/herpetozoa.39.e183441, CC BY 4.0; Reptile Database page reached): the Methods define OD as "greatest diameter of orbit" (orbital diameter), not eye diameter; Table 4 OD 9.1 / 8.7 / 7.7 mm for holotype ZSI-R-29431 and two female paratypes. Lead if a later unit accepts orbit diameter as sensory_anatomy; not filed here.
- A ZooKeys frog table (zookeys.pensoft.net article 146533 CSV) has no species name in the CSV and holotype ED 1.0 against male mean 2.0; not filed. Zootaxa venues (Hebius ngoclinhensis, Dibamus irregularis) dead.
- Fish: not searched.
