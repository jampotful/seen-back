# Harvest 12 progress (16 October 2026)

Branch research/harvest-12. Run per `docs/tracks/prompts/round4-harvest.md`, 20 genera: Euphorbia, Colaptes, Galium, Impatiens, Prunella, Pinus, Zonotrichia, Rhus, Toxicodendron, Dendrocopos, Gallinula, Cathartes, Melospiza, Actitis, Potentilla, Pandion, Alliaria, Quercus, Cyanocitta, Parus.

## Conditions on this machine

- `harvest_get.py` reported run 2 for 18 genera and run 1 for Pinus and Quercus (it merges every run on the ci branch and the newest wins per genus), so `where` names those runs.
- Web fetch worked for few hosts. OpenAlex's API, MDPI, Springer, Frontiers (one page), Oxford Academic and a PLOS page opened; Wiley, ScienceDirect, ASHS, Europe PMC, PubMed and the Biology Open PDF were refused, rate-limited or showed a bot check, and the PLOS page returned a different article from the one requested (the leafy spurge paper, 10.1371/journal.pone.0126030, was therefore not read). Most fetches were answered by a page summary, so records are partial.
- No paper was reached by any route other than a publisher or repository page.

## Result

- Genera screened: all 20. None was skipped, because no genus had full search records for all its open traits (Pinus, Quercus, Zonotrichia, Melospiza and Parus had records for some traits only; the new lines cover the rest).
- Search records: 48 in `docs/views/searched/harvest-12.jsonl`, one per trait group, with the harvest's queries word for word.
- Evidence: 1 record in `docs/views/evidence/harvest-12.jsonl` (Pinus pinaster, sense_light_nonvisual, grade m, partial). No open cell closed by a measurement.
- Wanted lines: 3 in `docs/views/wanted/harvest-12.jsonl` (Potentilla reptans, Pinus sylvestris, Quercus ithaburensis), authors confirmed from the OpenAlex record.
- Prunella is a homonym: the harvest lists Lamiaceae but ran bird-style queries. The records cover the traits those queries reached; sense_light_nonvisual was not searched for it and stays open.
- Plants: sense_chemical had no harvest query for any plant genus here and stays open.
- Unread candidates without confirmed authors, for a later round: 10.1371/journal.pone.0126030 (Euphorbia esula), 10.1016/j.semcdb.2020.05.004 (raptor vision review, for Cathartes and Pandion), 10.1002/ece3.74060 (moorhen visual field, not an open trait for the genus).
