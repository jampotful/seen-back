# OA batch 4

Checkpoint 2026-10-14. The initial lookup covered all 79 batch entries (ranks 238–316). OpenAlex exhausted the shared daily quota at rank 256 (HTTP 429), and further requests to that service stopped. Europe PMC exact-title/first-author/year matches recovered several missing DOIs. The unavailable-source log records the limitations rather than treating failed lookups as proof of absence.

All 13 confirmed, retrievable full sources have been read and logged, with 463 records. They are ranks 241 (requested thesis chapter 4), 247, 264, 267, 269, 274, 275, 276, 287, 288, 290, 300, and 309. Quotes passed the required checker before logging. Downloaded PDFs, XML, supplementary documents and extracted text remain outside the repository under `/tmp/oa/4`.

The viper accepted manuscript has unresolved conflicts between prose and figures, including the Bitis LWS peak and Agkistrodon brille transmission cutoff. Its caption identifies Crotalus atrox as the MSP specimen although a phylogenetic figure puts those values under C. durissus; no measured peak was carried to C. durissus. The two bird surveys conflict on the same fairywren voucher/accession. The larger survey also prints VS for the blue tit beside a UVS-type sequence and a main-text UVS caption. These conflicts are marked in individual records. Gene-class records do not claim measured color vision. Figure-derived numbers are marked approximate, and unit conversions include arithmetic.

Next: finish abstract-only records with `partial: true` and `access: abstract`; finish the 14 inaccessible candidate-copy statuses; inspect the direct repository/catalogue links supplied by three batch entries; then write the final counts and push. App setup and app checks are skipped.
