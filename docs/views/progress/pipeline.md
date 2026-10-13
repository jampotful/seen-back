# Progress: the extraction pipeline (agent/pipeline)

Started 13 October 2026, 04:40 UTC. Stops at 75 minutes (about 05:55 UTC).

## Done
- Read STATUS, QUEUE, the brief, check.py, and the harvest job (found on `run/lit/t1`, not on `main`).

- Prices read (13 Oct): Haiku 5.5, `claude-haiku-5-5`, batch $0.05 in / $0.25 out per million tokens; cache read $0.005 (derived), 1 hour write $0.10 (derived).
- tools/lit/extract.py written (plan, run, collect, check) with stdlib only; tools/lit/test_extract.py passes (7 tests, no key needed).
- Plan on spider-night: 650 passages, expected $0.09, ceiling $0.25.

- tools/lit/calibrate.py written. Offline calibration done (below).
- .github/workflows/lit-table.yml, ci/lit/table.sh and ci/lit/table.env written; table.sh run end to end in plan mode against a local checkout of pub/lit-t1 (estimates and offline calibration produced).
- extract.py `run` tested against a stand-in API server (8 tests pass): smoke request, batch submit, wait, results, check pass.

## Offline calibration (no API)
593 agent records (birds 218, cat-dog 178, ground-invertebrates 197). Sources cited: 207; in the collection: 188 (60 with full text, 120 abstract only). The agents' own quotes found in the collection's text or abstract and carrying the value: 334 of 593 (56%). That is the most the extractor can recover from the collection. The other 44%: source not in the collection (153), in it without text or abstract (78), or the agent's quote came from a text the collection does not hold.

## Cost (Haiku 5.5 through the Batch API, 13 October prices)
Inputs: $0.05 and outputs $0.25 per million tokens; the 1 hour cache write ($0.10) and read ($0.005) are derived from the page's standard prices and the stated 50% batch discount, so they are marked derived in the script. Estimates use 1.8 tokens a word, a system prompt of about 3,000 tokens (it may sit under the model's caching minimum, in which case the ceiling applies) and 250 output tokens a passage (ceiling 700). Passages per full text: 6.0 and 1,190 words, measured on the 101 full texts at hand.
- A topic costs about $0.20 to $0.70 expected (spider-night $0.09; the largest, mammals-other and methods, $0.69), $0.26 to $1.87 at the ceiling.
- All 34 topics, about 111,000 passages: about $17 expected, $44 ceiling, before the saving from works found under several topics (about 12% of works).
- The calibration run (505 passages) about $0.08 to $0.21.
- For the full run set LIT_MAX_USD to 50 in ci/lit/table.env.

## Next
1. When the key exists: set LIT_PLAN_ONLY=0 in ci/lit/table.env, push run/lit-table/<label>; read CALIBRATION.md on ci.
2. Review the first topic's table by hand (20 records) before the full run.
