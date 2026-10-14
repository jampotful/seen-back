# Intake 2 progress note (round 2 Drive intake)

Branch: research/intake-2. Launch prompt: docs/tracks/prompts/round2-intake.md.

## Files (10 named in the launch prompt, all full texts, none over 10 MB, none "(partial)")
Downloaded and decoded to the scratchpad; pdftotext -layout run on each.
Reading status: NOT YET STARTED on extraction (see below).

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

## Progress
- Log lines: 0
- Failed records: 0
- Next three things: extract and grep Veilleux; Laughlin; Potier. Then the remaining seven, quotecheck each, log.
