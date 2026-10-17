# Burst 11b: rerun the rows pipeline on the views whose evidence has settled (Sonnet, medium effort)

Start with `burst2-common.md`. Your track is `rows2`; work on `agent/rows2`. Stop after 120 minutes. API spend on build machines up to $6 (the job `views-rows`, plan-only as burst 10 left it). Read `docs/views/voice/REPORT.md`, `tools/views/rows.py` and the Burst 10 result in `docs/tracks/QUEUE.md`. You write only `views/*.json` (`rows_draft` blocks only, never live rows), `tools/views/`, `docs/views/voice/`.

1. Fetch `main`. For each view, compare the evidence that has landed since the drafts in `rows_draft` were made (audit decisions applied, canon partial flags now in the fixes file, the Crossref corrections if merged). Re-draft only views whose inputs changed; list them first.
2. Run `rows.py` for those views and for the views that have no draft yet. Every draft must pass `voice_check.py` and the number check. Refresh `docs/views/voice/REPORT.md` with pass rates and spend.
3. Also report, per view, which live rows now disagree with the evidence (grade or value), in a table in the report. Do not change any live row.
4. Run `python3 build.py --check` and `node test/check4.js try`; both must pass; `rows_draft` must stay out of the page.

Merge to `main` after fetching and rebasing. Final report, at most 150 words: views re-drafted, pass rates, live rows in disagreement, spend, last commit.
