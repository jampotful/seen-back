# Burst 2: ship the full database for the world, and the head's next step (Sonnet)

Start with `burst2-common.md`. Your track is `worlddb`.

Read `docs/tracks/worlddb.md` and `docs/tracks/head.md`, then the work already done. The branch `agent/world-db` (12 October, to 23:08 US Eastern) holds the world rows, the place files at 2 degrees, the encounter rule, the world test and the page reading the world manifest. `tools/world/RESULTS.md` on `agent/world-head` says no head passes every mark. The briefs say the app's thread ships; the control room is that thread now and allows you to merge the world database to `main` under the rules below. Stop after 150 minutes.

1. **The world database.** Check `agent/world-db` against the brief's five steps, fill any gap, and run `test/rec/check_rec.js` (section large) and every other check. Merge `main` into the branch, run every check again, number the build as `docs/HANDOFF.md` describes, and merge to `main`. Ship only when every check passes and the page behaves as today for a person who has not consented to the download. The engine agent may merge to `main` at the same time.
2. **The world test table**: top-1 right with no prior, with the time zone's prior, with the time zone and three creatures met, and with the true 400 km prior. Use the runs already done, and run again only where results are missing.
3. **The head.** Read `RESULTS.md`'s account of why each candidate failed and take the next step it points to on build machines. One example is B/16 for the creature groups with TinyCLIP kept for people, pets and rooms, if two encoders keep the app fast; another is a threshold for each group. Report against every pass mark, and prepare `agent/head-ship` only for a head that passes every mark.

Final report, at most 350 words: what shipped, with its build number; the world test table; the head's table against the pass marks and your recommendation; and your branches and last commits.
