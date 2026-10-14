# Outside worker: a genus sweep for the Regards research (Codex cloud task, or any agent with a shell and internet access)

You are helping research which animals, plants and fungi see what, for a phone app. The repository is github.com/jampotful/seen-back. Your task message names a batch number, k (1 to 8). Work only on that batch and write only the files named below with that k, so that eight tasks can run at once without touching each other's files.

## Read first
1. `docs/views/research/THOROUGH.md`, the sections "What done means" and "The protocol that may declare a cell unknown".
2. `docs/views/research/BRIEF.md`, the sections on the evidence log (record fields, the grades `m`, `g`, `i`, and the rule that `opened` means you read the source yourself in this task) and "Round 2".
3. `docs/tracks/prompts/round3-sweep.md`. You do the same work as the sweeps it describes.

## Your batch
`docs/tracks/batches/external-k.json` lists 50 genera in order of importance. Each has its open traits, its species, its family and order, and, for some traits, the nearest measured relative (`closest`, an id in the evidence logs). Work down the list; finish as many genera as you can, completely, before stopping. When your instructions name genera, do only those: earlier rounds settled the rest.

## How to search (use the scholarly APIs from the shell; they are faster and more complete than web search)
- OpenAlex, titles and abstracts of about 250 million works: `https://api.openalex.org/works?search=<genus> <trait words>&per-page=25&select=id,doi,display_name,publication_year,abstract_inverted_index,primary_location,open_access`. Search the scientific name with the trait's words, then the common name with the trait's words.
- Citation trail: find the nearest relative's source in OpenAlex (by DOI: `https://api.openalex.org/works/doi:<doi>`), then list later work that cites it: `https://api.openalex.org/works?filter=cites:<openalex id>,title_and_abstract.search:<genus>`.
- Europe PMC for abstracts and open full texts: `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=<terms>&resultType=core&format=json`, and full text for open-access papers at `https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/fullTextXML`.
- Crossref to confirm a DOI and its title: `https://api.crossref.org/works/<doi>`.
- Semantic Scholar for a free PDF that OpenAlex missed: `https://api.semanticscholar.org/graph/v1/paper/DOI:<doi>?fields=title,openAccessPdf`, at about one request a second.
- An open-access PDF (OpenAlex `open_access.oa_url`) may be downloaded and read with `pypdf` or `pdftotext`. Keep it outside the repository. Never reach a paper through a library login, a university proxy, Sci-Hub, LibGen, ResearchGate or Academia.edu.
Screen the first 25 results of each query by title and abstract; read anything that may hold a measurement. Send each genus's queries from one short script and read its saved results, so the API responses stay out of your context until you screen them.

## Write what you find
- A measurement you read (full text, or an abstract that states the value): one evidence record per value, appended with `python3 -I tools/senses/addlog.py external-k < records.jsonl` (one JSON object a line, with the fields of BRIEF's evidence log; the script checks each record and writes `docs/views/evidence/external-k.jsonl`). The quote is copied exactly from the source you read, and the source carries its DOI. The record's taxon is the species that was measured, graded `m`. Write no records for unmeasured species of the genus: the carry to them is computed later from the carry rules.
- Before you commit records, check their quotes against the file you read: `python3 -I tools/views/quotecheck.py <file.pdf or file.txt> records.jsonl`. Correct or drop each record that fails.
- A measurement you could not read (no open full text and the abstract does not give the value): one line in `docs/views/wanted/external-k.jsonl` in the format of the other files in that folder, with `for`, `rows`, `records` and `get`.
- A trait with nothing found: one line in `docs/views/searched/external-k.jsonl` with all of `taxon` (the genus), `level` ("genus"), `trait`, `queries` (two or more, as sent), `where` (the APIs and pages used), `canon` (an empty list is fine), `chased` (the DOI whose citations you checked, or "none: no measured relative; checked <review or query>"), `found` ("none"), `date`.

## Rules that matter more than speed
- Never write a citation, DOI, value or quote from memory. If you did not retrieve it in this task, it does not go in.
- A number from a review counts only if the review states it; name the review in the record's `note`.
- Do not edit any other file.
- Commit your work as you go. At the end, write a short summary to `docs/tracks/progress/external-k.md` (genera done, records logged, wanted lines, null searches) and commit it. The owner opens a pull request from your task; the research desk checks a sample of your records before merging.
