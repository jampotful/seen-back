# sweep-88 (Round 3 genus sweep, 15 October 2026)

Batch: 40 genera from sweep-1.json (frogs, rodents, galliforms, a kite, a quail-dove, a heron, two leporids, a felid and the addax).

Result: no measurement could be opened for any of the 40 genera, so no evidence records and no wanted lines were added. Each genus has one search record in `docs/views/searched/sweep-88.jsonl`.

Limits of this pass, for whoever sweeps these again:
- Search budget: about two searches per genus group rather than per genus, because the search tool returns titles only and most genera are obscure. The queries in each record are the combined queries for the group it was searched in, not a per-genus pair.
- `chased`: for frogs the DOI is the source of the nearest motion record (Satou and Shiraishi 1991), and for the felid and leporids Jacobs 2009. Reference lists of these were not opened; later work was looked for by title. Genera with no measured relative carry the "none" string.
- The NHM amphibian pupil dataset (10.5519/4q5uvvpa, already logged in oa-2) returned no rows for Oreophrynella, Atlantihyla, Niceforonia or Hildebrandtia through the fetch tool, which paraphrases large files; a direct look at the CSV would confirm.
- Hylodes asper: Haddad and Giaretta 1999 (Herpetologica 55:324-333) is a visual-signalling behaviour study with no vision measurement; not logged.
- Not valid sources and not logged: Wikipedia, Animal Diversity Web, birdforum pages.
