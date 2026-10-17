# Harvest c1 progress

## 2026-10-16

Checkpoint: Medicago is in progress; no genus has yet been declared complete and no null-search ledger has been written. Added 4 evidence records, 2 from full text and 2 marked partial, on Medicago sativa. The full-text records close its two current open cells (sense_light_nonvisual and sense_chemical). No wanted lines added at this checkpoint.

Opened the full text of Felle et al. 2000 (10.1104/pp.124.3.1373) at PMC, and Jiang et al. 2024 (10.3390/plants13050655) via Europe PMC. Read direct abstracts of Muschietti et al. 1993 (10.1042/bj2910383) and Lorenzo et al. 2019 (10.1111/tpj.14333). The G-protein source's scanned PDF did not open; its HTML has an abstract only. The latter two records are explicitly partial.

The harvest's Medicago results are cached locally in work/harvest-c1, along with eight missing-step queries run successfully on Europe PMC (20 records each), full XML of ten plausible papers and reviews, and the harvested works' direct Europe PMC abstracts. OpenAlex refused the first missing-step query with HTTP 429; it was stopped. Portland Press and Wiley OA PDFs returned HTTP 403 and were stopped. PMC later served a 200-status robot challenge for a PDF and a different article; challenge contents were not treated as paper text. The root coordinator was notified. No build, preparation, server, browser tests or self-test ran.

Next: finish screening Medicago's common-name and extra-trait results, add wanted records for relevant inaccessible sources not already marked full/partial/n/a, and write search records only for completed searches. Then continue Tussilago, Campanula and Daucus in batch order; the other assigned genera remain untouched.
