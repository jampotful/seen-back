# Intake 4 progress note (round 2 Drive intake)

Branch: research/intake-4, cut from main. Launch prompt: docs/tracks/prompts/round2-intake.md.
Status: complete for this prompt (ten named files read, 34 records logged, 7 records in intake-4-failed.jsonl, drive.jsonl written).

## Files (ten named in the launch prompt, keyed by sha1 of the Drive id)
All ten downloaded, decoded and run through pdftotext -layout. None over 10 MB (largest 4.1 MB, Malkemper 2018).

| sha1 key | file | DOI | wanted unit | logged | status |
|---|---|---|---|---|---|
| c4df125ac039 | Cronin 2007 | 10.1007/s10336-007-0199-0 | web-birds | 6 | read in full |
| fe4e6e73a9e6 | Zurek 2012 | 10.1007/s00359-012-0719-0 | jumper | 3 | read in full (Servaea vestita, not Maevia) |
| 87bb4c3daf46 | Chung 2014 | 10.1242/jeb.092478 | fish-shark | 2 | read in full |
| 5764ff38fed3 | Riol 1989 | 10.1016/0168-1591(89)90110-X | web-mammals | 2 | read in full |
| 46abaca0f3ec | Peaslee 1989 | 10.1007/bf00612995 | jumper | 3 | read in full |
| 034d671e9f05 | Hanke 2009 | 10.1007/s00359-009-0439-2 | mammal-groups | 4 | read in full |
| 3ca9bf58ce01 | Malkemper 2018 | 10.1002/cne.24493 | cat-dog | 12 | read in full (plain text for prose, layout for the rest) |
| 34fcfd2b4de1 | Kelber 2002 | 10.1038/nature01065 | insect | 2 | read in full; the file starts with the tail of an unrelated Nature letter |
| 7eca21a431c5 | Heffner 1983 | 10.1121/1.2020376 | web-mammals | 0 (1 failed) | PARTIAL; abstract only, read from a page image |
| fa0fa374c3ab | Sillman 1991 | none printed | web-herps | 0 (6 failed) | read in full; no DOI or URL on the file |

drive.jsonl: ten lines appended, all keys new. Main already repeats ten keys (60 lines, 50 unique); left as found.

## Records
- evidence/intake-4.jsonl: 34 records, all pass quotecheck (verbatim against the PDF text layer) and tools/senses/check.py (0 problems).
- evidence/intake-4-failed.jsonl: 7 records.
  - Heffner 1983 (1): the abstract is in a page image, not the PDF text layer, so quotecheck cannot find it. Read by eye: "the degree of binocular overlap in mammals is positively correlated with sound-localization acuity for frontally placed sound sources (r = 0.83)". Species not named on the page.
  - Sillman 1991 (6): the printed file has no DOI or URL, which check.py requires. Values as read: Alligator mississippiensis single cones 535 and 444 nm, double cone 566 (principal) and 503 (accessory), rod 501 nm, four cone pigments. Owner to supply a locator, then these can be logged.
- Partial records carry "partial": true (Heffner, in the failed file).

## Notes for the owner
- Cronin 2007 names the sandhill crane as Grus canadensis; the wanted line says Antigone canadensis (synonym). One sandhill crane, one record.
- Zurek 2012 measured Servaea vestita, not the Maevia inclemens of the wanted line; the jumper view's Maevia figures come from Peaslee 1989.
- Malkemper 2018 acuity values are morphological estimates (peak RGC density and eye length). The corrected 7.0 and 7.4 cycles/degree use the cat's beta-cell fraction and are logged as grade i.
- Kelber 2002: the blue-trained tests were significant to 0.001 cd/m2 and not at 0.0001; yellow was significant at 0.0001 (P < 0.05). The abstract's dim-starlight claim rests on both.
- Chung 2014: 89.0 Hz is the control value at 29 °C; 78.6 Hz is the high-CO2 treatment.
- Heffner 1983 page has no reference list, so no wanted lines were added from it. docs/views/wanted/intake-4.jsonl was not created.
- Kelber 2002's journal pages were not confirmed (the file gives Nature 419, 31 October 2002 only).

## New trait
- pupil_shape (new trait, carry rule 3): used for Phoca vitulina (Hanke 2009) and Vulpes vulpes and V. lagopus (Malkemper 2018). Written with "new trait" in the note.

## Next
1. Owner supplies a locator for Sillman 1991, then the six records are logged.
2. Owner supplies the Heffner abstract text or the journal page to confirm the species list (cattle and goat).
3. Confirm whether Maevia inclemens eye-specific sensitivity exists in a later source.
