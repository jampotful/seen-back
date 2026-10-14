# Progress: views (burst 7)

Started 13 October 2026, about 20:35 UTC. Branch `agent/views`.

## Done
- Task 1: `test/check4.js try` counts the rows the sheet shows and compares them with the spec's rows exactly. It did not fail on `main` for `jumper` (14 of 14) or `spider` (8 of 8): the sheet shows every row of a spec whatever drawing option is on, so the described miscount does not occur in this build. The check now also loads each view once with every option its `draw` block names past the first of each category.
- Task 2: `views/PARAMS.md` (the glossary) and its use in `tools/views/compile.py` (`read_glossary`, `glossary_text`, a section of each request), with tests in `tools/views/test_compile.py`.

## Next
- Rerun the compiler on the jumper and the bee with the glossary; promote primate, whale, scorpion, cephalopod; merge.
