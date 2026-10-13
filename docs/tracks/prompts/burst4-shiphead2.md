# Burst 4: finish shipping the county-bias head (Sonnet)

Start with `burst2-common.md`. Your track is `shiphead`; continue from `docs/views/progress/shiphead.md` on `agent/head-ship` (last commit `3f4424b`, build 28 at the time). Stop after 90 minutes.

The earlier agent stopped with `check_rec.js` sections `service`, `away` and `zone` unresolved, and `lent` in `check4.js` failing on `main` itself under load (it passes with `SLOW=3` on a quiet machine). Use unusual ports (for example 18791 and 18782), run one check at a time, and never kill processes by name, since other agents share the machine.

1. Merge `main` into `agent/head-ship` again (it has moved), run `service`, `away` and `zone` alone, and read why `zone` fails. The branch adds a time-zone rule (the county list is used only in the Eastern time zone or with no zone) that `main` lacks, so the failure may be a check that still expects the older rule; decide from the code which is wrong, and fix the code or the check.
2. Run every check4 mode and every check_rec section once more on the final build, and `tools/fusion/parity.py`.
3. Confirm that the page for a person who has not consented to the database download behaves as before.
4. If everything passes, merge to `main`. If a check fails and you cannot say why, leave the branch unmerged and report exactly what failed.

Final report, at most 200 words: the build number, each check's result and your last commit.
