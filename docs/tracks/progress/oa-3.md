# OA batch 3 progress

2026-10-14. Batch: 79 papers, ranks 159–237. Following `oa-pass.md`; app setup and app checks skipped. Branch: `research/oa-3`.

## Checkpoint

- Batch-wide lookup complete: 79 entries processed; 70 received at least one lookup response; 9 could not be searched after OpenAlex rate-limited. OpenAlex returned 200 for ranks 159–186, then 429 at rank 187. Subsequent OpenAlex requests stopped. Europe PMC and Semantic Scholar continued for DOI papers.
- 23 papers had candidate free-copy links. These are discovery results, not 23 confirmed readable papers. Publisher refusals, browser checks, and incomplete transfers are recorded separately below when work finishes.
- `oa-none-3.jsonl`: 47 no-copy-found entries; 27 explicitly flagged `lookup_incomplete` because OpenAlex was unavailable. The other 20 received the permitted lookup(s), including strict title matching and the book/chapter exception. These results describe the searches, not proof that no legal copy exists anywhere.
- 2 papers read in full: rank 166, *How fast can raptors see?* (publisher PDF deposited in HAL; publisher supplementary link returned 403), and rank 167, *Does retinal configuration make the head and eyes of foveate birds move?* (Europe PMC XML plus both PDF appendices; Appendix 2 phylogeny viewed).
- 66 quote-checked records logged: 29 from rank 166, 32 from rank 167, and 5 abstract-only records (`partial: true`) from rank 164. Rank 163's abstract was read but contains no extractable species-specific value. Neither abstract-only paper is marked fully read.

## Cautions for the research desk

Rank 167 calls its sampled birds single-foveate; the rank 164 abstract calls the specializations in five overlapping species areae centrales. Both claims are preserved with explicit disagreement notes. Rank 167 Appendix 1 calls *Poecile atricapilla* “Carolina Chickadee”; the phylogeny also says *P. atricapilla*. No species-level record is assigned to this ambiguous row. Its Pipilo spelling is resolved against the viewed Appendix 2 phylogeny. The actual rank 167 article year is 2017, unlike the batch's 2016 metadata.

Rank 166's true CFF was not reached in three birds; their highest tested FFF is logged as a lower bound in the note. Individual maxima are distinguished from species means and secondary Table 3 values. Quotes were checked against the PDF's reading-order and layout text extracted outside the repository. Originals behind secondary values were not claimed opened.

## Pending

1. Read rank 175's systematic review and its CFF data supplement (in progress), retaining review-level provenance, bounds, risk-of-bias flags and exclusions.
2. Continue down the available copies in batch order, beginning with rank 191 after earlier inaccessible candidates; quote-check each completed extraction.
3. Finish the access-failure and unsearched-paper lists, update counts, commit and push.

The nine unsearched entries are ranks 188, 195, 200, 204, 210, 214, 216, 228 and 234. They have no no-copy claim. Raw API responses, extracted text, PDFs and supplements stay outside the repository under `/tmp/oa`.
