# Codex engineering task 1: the gap index reads the right records (26 October 2026)

You fix code, with tests. The research desk (a Claude session) reviews your pull request, then regenerates the gap files itself. Read `AGENTS.md` first. Work from the latest `origin/main`.

## What to fix (each item was checked by the desk against the code on 26 October)
Sources: `docs/tracks/codex-findings/2026-10-26.jsonl` findings 1 to 3, `docs/tracks/codex-findings/2026-10-26-fixes-needed-a.md` section C and A8, and `docs/tracks/progress/fix-a.md` (A8 and the closing side finding).

1. `tools/views/gaps.py` reads every fetched `origin/research/*` branch as if it were main (finding 1). Make main the default: evidence comes from the working tree only. Keep the branch reading behind an explicit flag (for example `--with-branches`) that no workflow passes.
2. `Tax` in `gaps.py` keys a genus by name alone, so homonyms across kingdoms or views collide (finding 2; C1 lists Arenaria, Linaria, Prunella, Morus, Aquarius, Orthosia, Iris, Colocasia, Scoparia, Amorpha, Dryas, Drymomantis, Parnassius). Key by genus plus view (or kingdom), and file each genus under the family of its own view.
3. C2 (synonyms the gap index does not apply) and C3 (empty family and order in `cells.jsonl` though `taxonomy-gbif.tsv` has them): implement both in code. For C2, read a new file `docs/views/gaps/synonyms.tsv` (columns: old_genus, current_genus, view, source_url) if it exists (a parallel Codex task, codex-data-1, writes that file; do not create it yourself). Do not edit `docs/views/gaps/taxonomy-extra.tsv`.
4. A8: `gaps.py` and `tools/views/rows.py` must skip `docs/views/evidence/*-failed.jsonl` (held intake records).
5. Retraction ids: `gaps.py` matches retractions by `"<unit>:<line>"` from each record's `unit` field, but every intake record carries `unit: "intake"`, and fix-a found six `oa-regraded` copies dropped through a key collision. Match retractions by file name and line (as `tools/views/apply_audit.py` does), so ALL.jsonl ids like `intake-7:16` work, and make the six oa-regraded copies count.
6. `ci/harvest/harvest.py` `targets()` treats thin sweep-era search records as fully searched, so a plant harvest run finds nothing to do (runs 23 and 24 on the `ci` branch). Make a genus count as harvested only when it has a real harvest entry (see how `tools/views/harvest_get.py` decides), and keep `PLANTTRAITS=1` working.

## How
- Add or extend tests (`tools/views/test_*.py` style, standard library only) for each item; run every existing `tools/views/test_*.py` and `python3 -I tools/senses/check.py`.
- Run `gaps.py` into a scratch folder before and after your change and put the cell-count deltas per view in the pull request description. Do not commit regenerated files under `docs/views/gaps/` or anything under `views/` or `src/`.
- Change no evidence, wanted, searched or audit file.
- One pull request titled "Codex engineering 1 YYYY-MM-DD", ready for review, branch `codex/eng-1`. Reply with its link and one line per item: done, partly, or not done and why.
