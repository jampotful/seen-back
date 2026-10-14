# Outside worker: a blind test of search recall (Codex cloud task, or any agent with a shell and internet access)

This task tests whether your searching finds measurements that are known to exist, before agents like you sweep hundreds of genera and declare many of them unmeasured. It is the search-recall test of `docs/views/research/THOROUGH.md` ("Three tests per burst"). Your task message gives a label, L, which is `medium` or `high`. Write only the two files named below with that label.

## Read first
1. `AGENTS.md`.
2. `docs/views/research/THOROUGH.md`, the section "The protocol that may declare a cell unknown".
3. `docs/tracks/prompts/external-sweep.md`, the section "How to search". Search exactly as it says, with the same APIs.

## The test
`docs/tracks/batches/recall-test.json` lists 10 cells. Each is a genus (with its family, order and English name when known) and one trait, with words for the trait. For each cell, run the protocol at genus level: two or more queries (the scientific name with the trait words, then the English name with the trait words), the first 25 results of each screened by title and abstract, anything that may hold a measurement opened, and one citation step (a review of the family, or later work citing the most relevant source you found). A cell ends when you have found a measurement of that trait in a species of that genus, or when the protocol is done.

The test is blind. Search only outside the repository. Do not open or search any file under `docs/views/` other than `THOROUGH.md`, and do not search the repository for these genera.

## Write
- `docs/tracks/tests/recall-L.jsonl`, one line per cell: `{"genus": "...", "trait": "...", "queries": ["..."], "where": ["..."], "chased": "<the DOI whose citations you checked, or what you checked>", "found": [{"species": "...", "value": "...", "units": "...", "doi": "...", "title": "...", "quote": "<copied exactly, at most 40 words>"}]}`, with `"found": []` when nothing turned up.
- `docs/tracks/progress/recall-L.md`: how many of the 10 cells you found a measurement for, and how long the task took.

Never write a value, DOI or quote from memory. Commit both files. The owner opens a pull request from your task, and the research desk scores it against the measurements already logged.
