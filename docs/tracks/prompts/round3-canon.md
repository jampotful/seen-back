# Round 3: the canon (Sonnet, medium effort, run as a local agent because it needs the web)

Read `docs/views/research/THOROUGH.md`, then the Round 2 section of `docs/views/research/BRIEF.md`. Your branch is `research/canon`. Push at least every 15 minutes.

1. Take the traits that appear in `docs/views/gaps/queue.jsonl` (21 on 13 October). For each, find the cross-species compilations: reviews and papers with a table of values by species, data supplements, deposited datasets (Dryad, Figshare, Zenodo, Data in Brief) and, for the pigment traits, genome surveys of opsin genes. Look first for the orders that hold the most weight in the queue. Stop on a trait when two more searches add no compilation that covers a new order.
2. Confirm each DOI on its landing page or an index. A compilation whose DOI you cannot confirm gets `"doi": ""` and its full title.
3. Write one line per compilation to `docs/views/research/canon.jsonl`: `{"trait": "...", "doi": "...", "title": "...", "authors": "...", "year": 0, "covers": ["Order or family", ...], "species": 0, "in_hand": false, "open_access": ""}`. `species` is the approximate count its table or abstract gives. `in_hand` is true when its title is in `docs/views/sources/drive.jsonl` or it is marked `full` in `docs/views/papers-status.jsonl`.
4. For each compilation not in hand, add a wanted line to `docs/views/wanted/canon.jsonl` with `"priority": 1`, `"canon": true`, its `"covers"`, `"rows"` for its traits, `"why"` and `"get"`. Read any open-access compilation yourself and log its values as BRIEF describes, every species in its tables included.
5. Searches that found nothing new go to `docs/views/searched/canon.jsonl`.

Final message, at most 150 words: compilations per trait, how many in hand and how many wanted, and the last commit.
