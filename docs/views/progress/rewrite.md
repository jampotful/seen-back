# Progress: rewrite (18 October 2026)

Branch `agent/rewrite-1018`. The task: write a third version of each of the 31 rows the review on `agent/recommend-1018` (`docs/views/voice/recommend-1018.json`) marks "rewrite", stored in `rows_draft.rows` of each view with `"rewrite": "control room 18 Oct"` and the review's reason in `rewrite_reason`. Live `rows` stay untouched.

Done: 12 of 31 stored (jumper 9, bee 3), each passing `voice_check.check_text` and the number check of `rows.py` against the audited evidence. A jumper row with no draft entry is appended under the live title, or under the approved VOICE.md title with `live_title` naming the live row.

Next: alligator, cat, deer, dog (3), frog, hawk, insect, plant (3), spider (5), squirrel, wader; then `docs/views/voice/rewrite-1018.md`, the build checks and the merge.
