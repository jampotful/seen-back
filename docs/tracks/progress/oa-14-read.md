# OA reading pass, batch oa-14 (26 October 2026)

Prompt: `docs/tracks/prompts/oa-read.md` and `oa-pass.md`, with the desk's launch prompt for oa-14. Branch `research/oa-14`, cut from `main` at 7ee4d07f.

## Batch

`docs/tracks/batches/oa-14.json` holds 76 papers: every line of `docs/views/wanted/*.jsonl` on main with a DOI or a full title, less the papers an earlier oa batch covers (oa-1 to oa-12 on main, oa-13 on `origin/research/oa-13`, matched by DOI or normalised title; 1,529 lines), less the papers with evidence on main by DOI (85 lines), with 3 duplicate wanted lines kept once. Ten of the 76 have no DOI and are looked up by title. The order is their rank in `docs/views/wanted-merged.csv`. `ci/oa/list.jsonl` gains the 76 oa-14 lines.

## Fetch

Run branch `run/oa/read-r14` (from main): own public key, the 76 oa-14 lines, the batch file, matrix `[oa-14]`, and library proxy hosts (ezproxy, libproxy, elogim, idm.oclc.org, proxy.) added to the banned list in `ci/oa/oa.py` so that the job never opens one. Waiting for the job.
