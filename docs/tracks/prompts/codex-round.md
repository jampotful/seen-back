# A Codex round: all the open outside work, from one chat (Codex cloud chat, GPT-6.1 Sol, High)

The owner starts a round by sending one line to one new Codex chat. Do the whole round from here, in parallel where you can, and never ask the owner anything.

1. Make sure you are on the latest main from GitHub (`git fetch origin main`, then check out `origin/main`): the environment's saved copy of the repository can be hours old. Read `AGENTS.md`. Start nothing from the start skill.
2. Run `python3 -I tools/views/codex_queue.py`. It prints this round's items, one line each: the prompt to follow, the batch, and the entries or genera still to do. If it prints "Nothing to do", reply with that line and stop.
3. Spawn one subagent per item, as many at once as you are allowed, up to eight. Give each its line from step 2, word for word, and add: "Read AGENTS.md first. Do only the entries or genera named. Add this round's counts to your batch's progress note under a heading with today's date. Commit as you go, and stop between entries if you run out of room." Each item writes only files that carry its own batch name, so the subagents never touch the same file. If you cannot spawn subagents, do the items yourself, one after another, in the order printed.
4. When every subagent has finished or stopped, check the round: run `python3 -I tools/senses/check.py` on each evidence file the round changed, and confirm that no PDF, XML or other paper text is among the changes.
5. Commit everything, open one pull request into main titled "Codex round YYYY-MM-DD", ready for review, and reply with its link and one line per item: entries or genera done, records logged, and how many are left.

Never write a value, DOI or quote from memory. Work left over is not lost: the next round's `codex_queue.py` lists it again once this round's pull request is merged, so nobody continues a chat by hand.
