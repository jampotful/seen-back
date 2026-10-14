# External 8 progress

## 2026-10-14

- Completed genera this round: 5 of 50, in order: Cosmopepla, Vermivora, Pholisora, Biorhiza, Omocestus.
- Evidence records added: 0. Cells closed by a new measurement: 0.
- Wanted lines added: 0.
- Null-search lines added: 29 (4 + 5 + 6 + 8 + 6 traits), covering 34 species-trait cells. These are complete search-protocol records; final exhausted status remains subject to canon-intake coverage rules.
- Remaining genera: 45; next Tiaris, Illeis, Pseudovadonia. Stopped between entries.
- Sources read: Europe PMC titles/abstracts; nearest-relative abstracts and indexed citation trails for Land 1997 and three bird sources; Hesperiidae passages and references in the open full texts of Lu and Kronforst (10.1007/s00359-025-01751-8) and Lienard et al. (10.1098/rstb.2021.0279). No Pholisora measurement. Swihart 1969 is already full in owner status and logged for Epargyreus, so no duplicate request.
- OpenAlex, Crossref and Semantic Scholar had returned HTTP 429 elsewhere in this shared session and were not retried. Successful Europe PMC queries and full-text retrievals support these results; failed lookups were not treated as null results.
- Raw search responses/full texts remain outside the repository in /tmp/external-8. No app checks were run.

- Additional sources read for Biorhiza and Omocestus: open Biorhiza gall-induction genomic paper (10.1371/journal.pgen.1008398); Cynipidae section of the annotated brain-study translation (10.1101/lm.053894.123); Brown et al. 1998 publisher abstract/reference list (10.1017/S0007485300025864); Peitsch 1992 abstract (10.1007/bf00190398) and its zero-result Biorhiza citing-work query; open locust sky-compass review (10.3389/fnbeh.2015.00346); Schmeling 2014 abstract (10.1242/jeb.108514) and zero-result Omocestus citing-work query. No direct requested measurement in either genus.
- Taxonomy caveat: Pholisora, Biorhiza and Omocestus have blank family/order in the batch. Explicit family searches used Hesperiidae/Lepidoptera, Cynipidae/Hymenoptera and Acrididae/Orthoptera. The retrieved Peitsch abstract reports four hymenopterans with an additional red receptor, so no universal three-receptor carry was invented.
- Checkpoint commit: f3a4b23 (first three genera). Final commit adds Biorhiza and Omocestus. Parent handles push and PR on the shared branch.
