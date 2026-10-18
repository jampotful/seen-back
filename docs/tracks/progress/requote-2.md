# Requote 2, 17 October 2026

Chunk: docs/views/repair/chunks/chunk-2.jsonl (97 lines). Output: docs/views/recheck/recheck-42.jsonl (unit "recheck-42").

Counts: fixed 21, retracted 0, unfixed 76.

Fixed (action "correct", whole sentence from the page): oa-10:290, 291, 301, 302, 312, 313, 323, 324, 334, 335, 345, 346, 356, 357, 368, 373, 374 (Streinzer et al. 2016, via the Springer full-text page); harvest-c1:4 (Maxapress page, citation marker shown as an ellipsis); harvest-c1:53 (Frontiers PDF); harvest-c2:15 (MDPI PDF); harvest-c4:25 (Frontiers XML). The fetch tool summarizes pages, so sentence ends were confirmed by asking for first and last words of each sentence.

Unfixed:
- oa-10:281-289, 292-300, 303-311, 314-322, 325-333, 336-344, 347-355, 358-366 (72 ids): quotes are Table 1 rows of Streinzer 2016 (10.1007/s00359-016-1118-8). The Springer page returns only the table caption ("Full size table" link), the PMC page shows a browser check, Europe PMC and the table URL were refused. The rows are also table cells, not sentences, so they need a table read.
- harvest-c4:36, harvest-c4:37 (10.5660/WTS.2020.9.4.345): KCI abstract page not returned by any search.
- harvest-c3:52 (10.3390/plants15162420): no search returned the article.
- oa-10:192 (10.1073/pnas.2534625123): searches returned no open page for the article.
