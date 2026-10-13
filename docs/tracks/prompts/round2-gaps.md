# Round 2: the gap table (Sonnet)

Start with `burst2-common.md`, then the "Round 2" section of `docs/views/research/BRIEF.md`. Your track is `gaps`; your branch is `agent/gaps`. Stop after 75 minutes.

Goal: for each offered view (`views/<key>.json` with `offered` set, except `person` and `other`), the species people meet most that borrow it, and for each of the view's rows, how close the best evidence comes to each of those species.

1. Counts: iNaturalist research-grade records per species, worldwide and for Alachua County. Look in `docs/tracks/worlddb.md`, `tools/world/prior.py` and the files it publishes on `pub/world-place`, `docs/views/world-orders.csv`, `docs/views/no-view-us-fl-alachua.csv` and `pub/data-world`. Use bounded fetches and never load a large file into your context.
2. The kind of eye of each species: `kind_of_eye` in `tools/species/eyes.py`.
3. The rows: map every row of every offered view to the trait keys it rests on (the brief's trait table) in `docs/views/gaps/rows.json`.
4. The evidence: every `docs/views/evidence/*.jsonl` on `main` and on each `research/*` branch, and the extraction table on the `ci` branch under `runs/lit-table/` if a run has finished (`git fetch --depth=1 origin +refs/heads/ci:refs/remotes/origin/ci`). Records carry `taxon`, `family` and `order`; take the genus from `taxon`.
5. Write `tools/views/gaps.py` (rerunnable, so the table can be remade as logs grow) and its outputs: `docs/views/gaps/<view>.md` with the 60 borrowing species most recorded worldwide and the 20 most recorded in Alachua County, and for each row the most specific level with evidence (species, genus, family, order or none), the record behind it and whether a carry rule allows it; `docs/views/gaps/queue.jsonl`, one line per gap (`taxon`, `trait`, `rows`, `records`), ranked by records times rows fixed; and `docs/views/gaps/README.md` with how to rerun and the share of each view's records its 60 species cover.
6. Push within 10 minutes and every 15 minutes. When the script runs cleanly you may merge `tools/views/gaps.py` and `docs/views/gaps/` to `main`, and nothing else.

Final message, at most 250 words: the five views with the largest gaps by records, the top ten gaps, and the last commit.
