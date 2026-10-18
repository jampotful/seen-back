# Requote chunk 7, 17 October 2026

Source list: `docs/views/repair/chunks/chunk-7.jsonl` (97 lines). Output: `docs/views/recheck/recheck-47.jsonl` (unit `recheck-47`, action `correct`, `supersedes` set on every row). No evidence file, src/, views/*.json or audit file was edited.

Counts: fixed 86, retracted 0, table rows 0, unfixed 11.

Method note: the fetch tool would not print long passages in one piece, so each sentence was read in short consecutive pieces and joined. Where a sentence runs past 40 words the quote is a clause-bounded excerpt with each cut marked by an ellipsis and described in `where`. Sentences copied with their in-text citations as the page prints them. Typographic symbols were taken from the page's text layer (for example "lmax" in the Anolis paper, "pm" for the micro sign in the owl paper, "mm2"), so a reader comparing against the typeset page should expect superscripts and Greek letters to differ.

Fixed (86): oa-1:9173, 9175-9179, 9182-9186, 9188, 9191, 9192, 9194, 9195, 9198, 9202-9208, 9210-9222, 9230; oa-2:8866-8869, 8871-8880, 8882-8887, 8889; oa-2:9733, 9739-9747, 9752, 9757; harvest-c4:20-23; oa-2:9128-9130, 9132; oa-1:8677, 8678; harvest-c1:22, 63; harvest-c3:9; harvest-c5:20; oa-9:2088.

Points for the desk:
- oa-1:9217 (human 557 nm): three reads of Briscoe and Chittka p. 490 gave the same wording ("exists in humans, which produces a red receptor maximally absorbing at 557 nm"), but the sentence reads oddly and is worth a glance at the typeset page.
- harvest-c1:63: the Frontiers page prints the sentence with a stray closing parenthesis and no opening one; the quote copies that.
- oa-1:8677/8678 (turtle): the abstract was read from a PubMed-derived mirror (busqueda.bvsalud.org), not the journal page; the record's own url is unchanged.
- oa-2:9745-9747: the chi-square statistics that end those sentences came out garbled, so the quotes stop before them with an ellipsis.
- harvest-c3:9: the quote keeps the record's curly single quotes around the cultivar names.

Retracted: none. Table rows: none.

Unfixed (11):
- oa-2:9773, 9774, 9775, 9776, 9777, 9778, 9779 (Biophysical Journal 2010, Acuity of a cryptochrome and vision-based magnetoreception system in birds): PMC shows a reCAPTCHA page and the Europe PMC render URL was refused by the fetch tool as not from a search result.
- oa-2:9721, 9722, 9723 (manatee visual pigments, Vision Research 2006): no open page carrying the abstract was returned by search (the Newman 2006 teaching page gives 556 and 411 nm in its own words and is not the abstract); PubMed and Europe PMC URLs were refused.
- harvest-c3:110 (Fragaria viridis, Annals of Botany): only the bioRxiv preprint opened; its sentence ("In F. viridis, shading of mothers increased carbon translocation from daughters to mothers.") matches the quote's words, but the published version at Europe PMC PMC11560365 would not open, so the printed sentence was not confirmed.
