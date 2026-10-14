# Intake 8 progress

Branch research/intake-8, cut from main, 13 October 2026.

## Done
- Read all twelve Drive files in the intake list (none over 10 MB, none marked partial by name). Each matched to a wanted line by DOI or title.
- Scanned files with no text layer (Kim 1989, Seo 1996) read by tesseract OCR of the English abstract; quotecheck run on the OCR text.
- Rojas 1997 abstract and Tables 1 and 2 read from page images.
- Jenssen 1974 Table 2 values read from the page image.
- Logged 37 records in docs/views/evidence/intake-8.jsonl (quotecheck: all pass; check.py: 0 problems).
- 5 records failed quotecheck and sit in docs/views/evidence/intake-8-failed.jsonl: one Rojas 1997 skimmer density (garbled text layer) and four Jenssen 1974 Table 2 values (genus abbreviated in the table rows).
- Added 12 lines to docs/views/sources/drive.jsonl (keys are the first 12 hex digits of SHA-1 of the Drive id; no Drive id written).
- One wanted line added: Bowmaker and Martin 1978 (tawny owl microspectrophotometry), docs/views/wanted/intake-8.jsonl.

## Open
- Second reading of the five failed records (see the failed file).
- Hárosi 1982, cited by Schott 2022 for LWS 570 nm in Lithobates, is not in the paper's reference list as extracted; citation unchecked.
- Seo 1996 logged as partial: only the English abstract was read; Korean body unread.
- No partial files among the twelve, so no reference-list wanted lines were needed.

## Next three
1. Second reading of the failed records, with quotes that pass the table rule.
2. Check the Anolis Table 2 values against the full text layer once a readable copy is available.
3. Look for an open source for Bowmaker and Martin 1978 (tawny owl cones).
