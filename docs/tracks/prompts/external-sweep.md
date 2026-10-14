# Outside worker: a genus sweep for the Regards research (any coding agent with web access)

You are helping research which animals, plants and fungi see what, for a phone app. The repository is github.com/jampotful/seen-back. Work only on a new branch named `external/sweep-1` and push to it at least every 20 minutes. Never push to `main`; the owner's research desk reviews and merges your branch.

## Read first
1. `docs/views/research/THOROUGH.md`, the sections "What done means" and "The protocol that may declare a cell unknown".
2. `docs/views/research/BRIEF.md`, the sections on the evidence log (record fields, grades `m`, `g`, `i`, the rule that `opened` means you read the source yourself) and "Round 2".
3. `docs/tracks/prompts/round3-sweep.md`. You do the same work as the sweeps it describes.

## Your batch
`docs/tracks/batches/external-1.json` lists 400 genera in order of importance. Each has its open traits, its species, its family and order, and the nearest measured relative for some traits (`closest`, an id in the evidence logs). Work down the list; it does not matter how far you get.

## For each genus
1. Search the web for measurements of each open trait in any species of the genus: the scientific name with the trait's words, then the common name with the trait's words (for example "Sphaeralcea flower photoreceptor", "Trichius compound eye spectral sensitivity"). Read the first 20 results' titles and open anything plausible.
2. Follow one citation trail: later work citing the nearest measured relative's source, or a review of the family.
3. Write what you find:
   - A measurement you could read (full text, or an abstract that states the value): one evidence record, appended with `python3 -I tools/senses/addlog.py external-1 < records.jsonl` (one JSON object a line, the fields of BRIEF's evidence log; the script checks each record and writes `docs/views/evidence/external-1.jsonl`). The quote must be copied exactly from the source, and the source must have a real DOI or URL that you opened in this task. Grade `m` only when the measurement is of that very species.
   - A measurement you could not read (paywalled): one line in `docs/views/wanted/external-1.jsonl` in the format of the other files in that folder, with `for`, `rows`, `records` and `get`.
   - A trait with nothing found: one line in `docs/views/searched/external-1.jsonl` with all of `taxon` (the genus), `level` ("genus"), `trait`, `queries` (at least two), `where`, `canon` (an empty list is fine), `chased` (the DOI you followed, or "none: ..." saying what you checked), `found` ("none"), `date`.

## Rules that matter more than speed
- Never write a citation, DOI, value or quote from memory. If you did not open it in this task, it does not go in.
- A number from a review counts only if the review states it; say which review in the record's `note`.
- Do not edit any other files.

When you stop, push the branch and write a short summary at the end of `docs/tracks/progress/external-1.md`: genera done, records logged, wanted lines, null searches.
