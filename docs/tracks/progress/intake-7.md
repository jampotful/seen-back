# Intake 7 progress note (round 2 Drive intake)

Branch: research/intake-7, cut from main. Launch prompt: docs/tracks/prompts/round2-intake.md (ten named Drive files).
Status: complete for this prompt. Ten files downloaded, decoded and run through pdftotext; 27 records logged; 0 failed; 3 wanted lines added.

## Files (keyed by the first 12 hex digits of SHA-1 of the Drive id; none existed on main or on the branch before this run)
| key | file | DOI | wanted unit | records | status |
|---|---|---|---|---|---|
| 0715978ec23a | Calderone 1995 mouse UV retina | 10.1017/S0952523800008361 | web-mammals | 3 | PARTIAL: printed web page, abstract and references only; partial true on all 3 |
| 9dc42ee254b0 | McComb 2009 hammerhead visual fields | 10.1242/jeb.032615 | fish-shark | 5 | read; binocular values from the abstract, cross-checked to Table 1 |
| 49bb21e8c7ec | Fleissner 1977 scorpion eye sensitivity | 10.1007/bf00612341 | ground-invertebrates | 4 | read; table exponents OCR-garbled, text figures used |
| 27a9a73ccb39 | Rahmoun 2020 dromedary eye histology | 10.32819/2020.82018 | web-mammals | 1 | read |
| e0188d1215a8 | Prusky 2000 mouse and rat acuity | 10.1016/s0042-6989(00)00081-x | web-mammals | 2 | read |
| 3960ef9fd0bc | Bakken 2007 pitviper facial pits | 10.1242/jeb.006965 | herps | 3 | read |
| 9802b03b7369 | Phillips and Lomas 2001 cattle colour | none (matched by title) | web-mammals | 1 | read (primary experiment, full text) |
| 1c520da6f796 | Brown 1969 turtle linear area centralis | 10.1016/0042-6989(69)90047-9 | herps | 3 | read; species name OCR-garbled, read as Pseudemys scripta elegans |
| e902e80b965a | New and Bull 2011 sleepy lizard | 10.1007/s00359-011-0635-8 | herps | 3 | read |
| d530a91eb854 | Abedellaah 2017 camel eye gross | 10.21608/avmj.2017.170671 | web-mammals | 2 | read |

## Records
- evidence/intake-7.jsonl: 27 records. quotecheck: 27 verbatim, 0 failed. tools/senses/check.py: 0 problems.
- evidence/intake-7-failed.jsonl: not written (no failures).
- Degree signs in the McComb and Brown PDFs are a symbol-font space (U+F020) before "deg."; quotes keep it so they match the text.
- Two new trait keys, each with "new trait" in the note: receptor_density_per_441um2 (Brown 1969), pupil_shape (Abedellaah 2017). rgc_peak_density_per_mm2 (New and Bull 2011) reuses the key already added in intake 5.

## Issues for the owner
- Calderone 1995 is partial. The two mouse cone classes (360 and 511 nm) are the earlier study's values, as the abstract cites them; this paper confirms the regional segregation. Its records are abstract-level.
- Fleissner 1977: the lateral night threshold (1.5 x 10^-8 uW cm-2 sr-1) is taken from the text; Table 1 exponents are OCR-garbled. The lateral and median night thresholds differ by about 1 log unit, as the paper says. Median and lateral daytime values are not logged separately.
- McComb 2009: the abstract mixes physiological and morphological binocular values across species. Table 1 gives both; the rows are logged as abstract values with the table values in the note. The cyclopean and monocular fields in Table 1 (e.g. 308 deg for the lemon shark, 338.3 deg for the scalloped hammerhead) are not logged: the table line does not name the species, so the quote check cannot pass it. These bear on the shark view's invented 300-degree field and need a table-aware record.
- Bakken 2007: the pit-membrane sensitivity (0.001 degC) is an inference from behaviour as the paper states it, graded i. The measured thresholds (0.003 to 0.001 degC) are from Bullock and Diecke 1956 and are not opened.
- Rahmoun 2020 does not say the tapetum is absent; its choroid is described as dark and pigmented. Abedellaah 2017 states absence. Both are logged.
- Abedellaah 2017 gives camel axial length (3.1 to 3.16 cm) and the lens and cornea dimensions; no trait key fits, so they are not logged.
- Phillips and Lomas 2001: the cattle result is behavioural (two-choice after isoluminance). It does not give a receptor count, so no receptor_classes record is logged.
- Prusky 2000: the abstract rounds the rat acuity to about 1.0 cpd; the Results give 0.95 cpd. The mouse abstract reads "C57BU6" (OCR of C57BL/6).
- Brown 1969: the species and the receptor counts are logged. Brown's "oil droplets per 441 sq micron" counts are a proxy for receptor density, and the note says so.

## Wanted lines
- docs/views/wanted/intake-7.jsonl: three reference-list papers from the Calderone partial file (Szel 1992, Szel 1994, Jacobs 1993). None has a DOI in the printed reference list, so doi and url are empty; get is "journal via library".
- Jacobs, Neitz and Deegan 1991 (Nature) is on the reference list too, but docs/views/wanted/squirrel-deer-rabbit.jsonl already asks for it, so no line was added.
- Other reference-list papers were not added: the Calderone list is mostly 1990s retinal work on mouse and rat, and most of it does not bear on a view row.

## Next
1. The owner can fetch Szel 1992 and Szel 1994 and Jacobs 1993 through the library for the mouse colour row.
2. A table-aware record for McComb 2009 Table 1 (monocular and cyclopean fields) for the shark view.
