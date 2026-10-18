# Audit 46, 18 October 2026: harvest-32 (desk-screen unit)

The unit is branch research/harvest-32 at commit a7178fde: 40 search records (docs/views/searched/harvest-32.jsonl) and 18 wanted lines (docs/views/wanted/harvest-32.jsonl). I read the files with `git show a7178fde:<path>` and saved copies to /tmp/au46/ (byte-identical to the committed files). The audit worktree /tmp/wsau46 was cut from origin/main and edits only this report. No ResearchGate, academia.edu, Sci-Hub or LibGen page, library login or proxy was used, and no paper text is committed.

## Gate

`python3 -I tools/views/screen_candidates.py --check /tmp/au46/harvest-32.jsonl --wanted /tmp/au46/harvest-32-wanted.jsonl` printed "0 problems". The unit goes on to the sample.

## Sample

All 40 search record lines (1-based line numbers), `random.seed(46)`, `random.sample(lines, 20)`. The draw used the line count only, and it was written here before any record was read.

Draw order: 5, 26, 3, 15, 34, 10, 38, 2, 40, 39, 11, 21, 27, 33, 1, 32, 18, 35, 17, 30

Sorted: 1, 2, 3, 5, 10, 11, 15, 17, 18, 21, 26, 27, 30, 32, 33, 34, 35, 38, 39, 40

The 20 lines left out are 4, 6, 7, 8, 9, 12, 13, 14, 16, 19, 20, 22, 23, 24, 25, 28, 29, 31, 36 and 37. They are the pool for a seed-4601 extension of 15 if an error turns up in the first 20.

Verdicts follow in the next commits.
