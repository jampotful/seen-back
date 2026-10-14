# Intake 2 progress note (round 2 Drive intake)

Branch: research/intake-2. Launch prompt: docs/tracks/prompts/round2-intake.md.

## Files (10 named in the launch prompt, all full texts, none over 10 MB, none "(partial)")
Downloaded and decoded to the scratchpad; pdftotext -layout run on each.
Reading status: all ten read in full (pdftotext -layout), none skipped.

| sha1 key | file | wanted line (DOI) | status |
|---|---|---|---|
| 23e3241163d2 | Veilleux 2014 | cat-dog, mammal-groups (10.1159/000357830) | downloaded |
| b8b0128d02d8 | Laughlin & Weckstrom 1993 | insect, methods (10.1007/bf00213682) | downloaded |
| 497c042219f5 | Potier 2020 | birds, birds-met (10.1016/j.semcdb.2020.05.004) | downloaded |
| 824a6aa1fe47 | Jander & Jander 2002 | bee, insects-met (10.1016/s1467-8039(01)00035-4) | downloaded |
| 2e50f7f85357 | Kraatz 2026 | rabbit (10.1098/rsos.252149; wanted line has no DOI) | downloaded |
| 8b103d8d424d | Swihart 1969 | insects-met (10.1016/0022-1910(69)90196-6) | downloaded |
| 623a898d1b42 | Peitsch 1992 | bee, insects-met (10.1007/bf00190398) | downloaded |
| 5ef6247ecba8 | Jacobs 1982 | squirrel-deer-rabbit, mammals-met (10.1016/0376-6357(82)90008-0) | downloaded |
| 81f9b751d5e4 | Ault 1984 | web-birds (no DOI) | downloaded |
| cc585c58fbb8 | Lisney 2013 | birds-met, birds (10.1002/ar.22815) | downloaded |

Note: three of these (Jacobs, Lisney, Ault) already have lines in sources/drive.jsonl from intake-1. They are re-read here as the launch prompt asks.
Note: the rank numbers in the launch prompt match wanted-merged.csv only for Kraatz (72). The rest are matched by DOI.

## Progress (complete for this prompt)
- Logged: 43 records to docs/views/evidence/intake-2.jsonl (all pass quotecheck, verbatim or table).
- Failed: 12 records to docs/views/evidence/intake-2-failed.jsonl. Causes: table species names that wrap onto a second line (Laughlin Table 1, 4 rows), OCR-merged or garbled names (Peitsch: Paravespulayermanica, 9allicus, 6 rows), a row whose species is not printed (Potier Hirsch 40), and a spaceless PDF line (Ault, Bubo).
- drive.jsonl: 10 lines appended. Jacobs, Lisney and Ault keys already had intake-1 lines; these are now duplicated with different counts (Lisney intake-1 6, intake-2 2; Ault intake-1 0, intake-2 1).
- Wanted lines: none added (all ten files are full texts).
- Prompt ranks: only Kraatz (72) matches wanted-merged.csv. The rest are matched by DOI.
- Not logged: Veilleux per-species values (in supplementary table, not in PDF); Jander per-species values (Figure 7 only).
