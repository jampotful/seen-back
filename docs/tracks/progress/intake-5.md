# Intake 5 progress note (round 2 Drive intake)

Branch: research/intake-5, cut from main. Launch prompt: docs/tracks/prompts/round2-intake.md.
Status: complete for this prompt (ten files read, 41 records logged, 3 held, drive.jsonl written). No wanted lines written: none of the ten is marked partial.

## Files (ten named in the launch prompt, keyed by sha1 of the Drive id)
All ten downloaded, decoded and run through pdftotext. None over 10 MB (largest 2.6 MB). None carries "(partial)" in its Drive name; all are full articles, a review or a thesis.

| sha1 key | file | DOI | wanted unit | records | status |
|---|---|---|---|---|---|
| f758cb063f91 | Geberl 2019 bat biosonar | 10.1016/j.cub.2019.04.046 | mammal-groups | 1 | read; degree-sign OCR issue, flagged |
| 073fd35890b9 | Ishengoma 2017 giraffe and okapi vision genes | 10.7717/peerj.3145 | web-mammals | 2 | read; predicted values only (grade i) |
| 6870c3673fe1 | Baker and Ma 2006 Solenopsis ommatidia | 10.1016/j.jcz.2006.06.001 | insect | 4 | read |
| a0c8b8d8469f | Ryan 2017 shark electrophysiology | 10.1007/s00359-017-1154-z | fish-shark | 8 | read |
| b05b5c515b65 | Coimbra 2013 giraffe RGC topography | 10.1002/cne.23271 | web-mammals | 3 | read |
| 0f70849b6e49 | Siebeck and Marshall 2001 reef fish ocular media | 10.1016/s0042-6989(00)00240-6 | fish-shark | 9 | read |
| a78766dceb78 | Timney and Keil 1992 horse acuity | 10.1016/0042-6989(92)90092-w | mammals-met | 2 | read |
| f84444fd2580 | Stuhlträger et al. 2025 review, light and vision in farmed ungulates | 10.3389/fanim.2024.1433181 | web-mammals | 10 | read; review, values as reported (primaries not opened) |
| 6a2c6562d9f8 | Wang 2013 alpaca thesis | 10.25675/3.021717 | web-mammals | 2 | read |
| 7951e29f1762 | Braekevelt 1993 great horned owl photoreceptors | none | web-birds | 0 (3 held) | read; no DOI or URL in source |

## Records
- evidence/intake-5.jsonl: 41 records, all pass quotecheck (verbatim or table) and tools/senses/check.py (0 problems).
- evidence/intake-5-failed.jsonl: 3 Braekevelt 1993 records. They quote correctly but fail the log check because the source has no DOI or URL. The owner needs to supply a locator (journal page or PubMed record) before they can be logged.
- Two new trait keys were used, each with "new trait" in the note: contrast_threshold_percent (Ryan 2017 group), rgc_peak_density_per_mm2 (Coimbra 2013), plus ommatidia facet count and photoreceptor ratio (Baker 2006, Braekevelt 1993). Four new traits in all; the owner may want them as keys.

## Issues for the owner
- Geberl 2019: the paper's azimuthal resolution "about 8" has its degree sign dropped in extraction (a symbol-font glyph). Read as 8 degrees, it is about 400 times the human value of 0.02 degrees, not the "three orders of magnitude" the paper states. Checked against the paper's own text; not resolved.
- Timney and Keil 1992: "23.3 c deg" has an OCR artefact in the unit; read as cycles per degree from the abstract wording. The best of three horses.
- Ryan 2017: per-species flicker fusion values sit in Table 1, which was not read as text. The H. portusjacksoni value is the range for three species, not an isolated figure.
- Ishengoma 2017: the giraffe lambda max of 560 nm and the okapi 553 nm are predictions from the five-sites rule, not measurements (grade i).
- Stuhlträger 2025: a review; cattle and goat values are as reported, citing Jacobs et al. 1998, Dimberton 1999, Blackshaw et al. 1983, Piggins and Phillips 1996, Walls 1942 and Hughes and Whitteridge 1973. None of these primaries was opened.
- Wang 2013: the thesis measures alpacas only; llama (Lama glama) rows still need a llama source.
- Siebeck and Marshall 2001: the T50 values are from Table 1, read in the layout text. The "class" letter is the paper's cut-off class, not a sensitivity class.

## Wanted lines
None added. The launch prompt asks for reference-list wanted lines only for partial files, and none of the ten is partial.

## Next
1. Owner supplies a locator for Braekevelt 1993, then the three held records are logged.
2. Owner checks the Geberl degree-sign reading against the printed PDF.
3. Ryan 2017 Table 1 per-species flicker values to be read as text.
