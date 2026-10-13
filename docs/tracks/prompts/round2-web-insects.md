# Round 2: web search for the insect and bee views (queue 16a, Sonnet, medium)

Run from the research thread, because cloud agents cannot reach the open web. Read the "Round 2" section of `docs/views/research/BRIEF.md` first. Work in your own git worktree (`git worktree add ../wt-webins origin/main`), never in the shared checkout. Stop after 60 minutes.

Goal: find the papers that would give species-level evidence for the insect and bee views, for the species people meet most.

1. Targets: the lines of `docs/views/gaps/queue.jsonl` with `view` of `insect` or `bee`, in rank order (records times rows), plus `docs/views/wanted/insects-met.jsonl` for what is already asked. Take the top 40 taxa by records, genus where species are many and alike.
2. For each taxon and each trait named in its gap lines, search with WebSearch and WebFetch by scientific and common name and by genus (PubMed, Europe PMC, PMC, bioRxiv, publisher abstracts, theses, repositories). Fetch each site at most once if it refuses; stop on HTTP 429.
3. Write a wanted line only for a paper whose title, authors, year, journal and DOI you saw on a page you opened. Never write a DOI from memory. Use the round-2 fields: `unit` "web-insects", `priority`, `authors`, `year`, `title`, `journal`, `doi`, `url`, `why`, `views`, `for`, `rows` ("<view>:<row title>"), `records`, `get`. Open-access papers go on the list too, with the address in `get`.
4. Record searches that found nothing in `docs/views/searched/web-insects.jsonl` (format in BRIEF Round 2).
5. Files you may write: `docs/views/wanted/web-insects.jsonl` and `docs/views/searched/web-insects.jsonl`. Commit as `git -c user.name=Claude -c user.email=noreply@anthropic.com commit`, push the branch `research/web-insects` within 10 minutes and every 15 after, then at the end push those two files to `main` (fetch and rebase first). Change nothing else.

Final message, at most 150 words: lines written, searches that found nothing, last commit.
