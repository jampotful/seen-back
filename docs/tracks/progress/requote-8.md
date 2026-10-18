# Requote 8, 17 October 2026

Work list: `docs/views/repair/chunks/chunk-8.jsonl` (97 ids). Output: `docs/views/recheck/recheck-48.jsonl`. No evidence file, `src/`, `views/*.json` or `ALL.jsonl` was edited, and no paper text was committed.

Counts: fixed 11, retracted 0, table rows 27, unfixed 59.

Method note: the fetch tool would not return long passages verbatim, so each sentence was read in consecutive pieces under 100 characters and joined. Sentences were checked for first and last words. Page-read grades, values and flags are unchanged.

## Fixed (11)
oa-1:5164, oa-1:7376, oa-1:7382, oa-1:7383, oa-5:1176, oa-5:1177, oa-5:1178, oa-5:1181, harvest-c1:64, harvest-c5:24, oa-9:2089

## Table rows (27)
Appendix A Table A1 rows of the Carleton thesis: oa-1:6430, oa-1:6431, oa-1:6432, oa-1:6433, oa-1:6434, oa-1:6435, oa-1:6436, oa-1:6437, oa-1:6440, oa-1:6441, oa-1:6445, oa-1:6446, oa-1:6448, oa-1:6449, oa-1:6450, oa-1:6451, oa-1:6454, oa-1:6455, oa-1:6459, oa-1:6460, oa-1:6462.
Table 5 rows of Nagloo et al. 2019: oa-9:2060, oa-9:2061, oa-9:2062, oa-9:2072, oa-9:2073, oa-9:2074.

## Unfixed (59)
- the thesis (Carleton, 2026) is not returned by WebSearch and its DOI would not open: oa-1:6425, oa-1:6428, oa-1:6464, oa-1:6465, oa-1:6466, oa-1:6467, oa-1:6468, oa-1:6469, oa-1:6470, oa-1:6471, oa-1:6472, oa-1:6473, oa-1:6474, oa-1:6475
- the Wiley page is not in the search results and the ANU repository copy is embargoed to 2037; no open full text: oa-9:2046, oa-9:2047, oa-9:2052, oa-9:2053, oa-9:2058, oa-9:2059, oa-9:2064, oa-9:2065, oa-9:2070, oa-9:2071, oa-9:2076, oa-9:2077, oa-9:2078, oa-9:2079, oa-9:2080, oa-9:2081
- only PMC (PMC2781854) opens it in search and PMC answers with a reCAPTCHA page; the Royal Society page was refused: oa-2:9112, oa-2:9113, oa-2:9114, oa-2:9115, oa-2:9116, oa-2:9117, oa-2:9118, oa-2:9119, oa-2:9121, oa-2:9122, oa-2:9124, oa-2:9125
- PMC4798572 answers with a reCAPTCHA page, the Europe PMC render is blocked by robots rules, and the PLOS URL returned a different paper: oa-6:663, oa-6:664, oa-6:665, oa-6:669, oa-6:670, oa-6:671, oa-6:672, oa-6:673, oa-6:674
- no open page or abstract for the paper came back from search: oa-5:1263, oa-5:1264, oa-5:1265
- the journal abstract page has no body text and the PDF link opened the journal home page; PMC is blocked: oa-10:2, oa-10:3
- ScienceDirect refused the fetch and PubMed was not in the search results: harvest-c1:23
- the preprint did not appear in search: harvest-c3:12
- the paper did not appear in search: harvest-c3:112
