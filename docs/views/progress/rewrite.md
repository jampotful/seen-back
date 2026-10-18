# Progress: rewrite (18 October 2026)

Branch `agent/rewrite-1018`. The task: write a third version of each of the 31 rows the review on `agent/recommend-1018` (`docs/views/voice/recommend-1018.json`) marks "rewrite", stored in `rows_draft.rows` of each view with `"rewrite": "control room 18 Oct"` and the review's reason in `rewrite_reason`. Live `rows` stay untouched.

Done and pushed: all 31 rows in 13 views (jumper 9, spider 5, bee 3, dog 3, plant 3, and one each in alligator, cat, deer, frog, hawk, insect, squirrel and wader), each with cites into the audited evidence and a note. Each passes `voice_check.check_text` at its grade and the number check of `rows.py` (numbers above 10 in a cited record, cited records related to a species of the view, an m row citing an m record). The table is `docs/views/voice/rewrite-1018.md`. Rebased on `main` at `47351be`; `build.py` and `build.py --check` pass, and the built page is byte-identical to main's, since `rows_draft` stays out of it.

The `try` check must be served from this clone on a port of its own (`PORT=<free port>`, `SLOW=4`): port 8765 belongs to another agent's server, and a first run against it failed in jumper, reef, shark and spider with a 404.

The `try` check on port 8939 passed (exit 0; no view threw; every view shows all its rows). Merged to `main` with this track's row in `docs/STATUS.md`.

Next: the owner decides row by row between each live row and its rewrite.
