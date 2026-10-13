# Progress: gaps (round 2)

Started 13 October 2026, 19:23 US Eastern; stops at 20:38.

Done: cloned the repository; found the data (`rows.tsv` on `pub/naturalist-world` has records a species worldwide; `regions/us-fl-alachua/species.json` on `pub/data-alachua` has the county's species with ranks).
Pushed: this note.
Next: fetch the evidence branches, write `docs/views/gaps/rows.json`, write `tools/views/gaps.py`, run it, push.

## Update, 13 October 23:50 UTC (second agent)

Done and pushed: `tools/views/gaps.py` runs cleanly (4 seconds); it wrote `docs/views/gaps/<view>.md` for the 14 offered views, `queue.jsonl` (4,719 gaps), `summary.json` and `README.md`. `taxonomy-extra.tsv` holds family and order for 202 genera the county list and the evidence lack (my own construction, unchecked against GBIF). Evidence read: 4,292 records from main and 17 research branches, 25 audit retractions dropped. The literature table only adds a `lit_hint`.
Limits: the agreement test for rule 5 is crude (README); Alachua has few species for some views (deer 3, cat 2, dog 3).
Next: merge the script and the outputs to main; then check a sample of cells by hand.
