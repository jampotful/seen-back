# Burst 2 and later: the preamble every launch prompt starts with

You are working on Regards, a phone app, in the repository github.com/jampotful/seen-back. Clone it into your own directory, `/home/claude/wt-<your track>`, with `git clone --depth 1` (allow ten minutes), and fetch the branches you need with bounded fetches (`git fetch --depth 50 origin '+refs/heads/<branch>:refs/remotes/origin/<branch>'`). Never work in `/home/claude/seen-back`: another process uses it, and in burst 1 agents switched its branch under each other.

Read `docs/STATUS.md` first. Push within 10 minutes of starting and then every 15 minutes. Keep a progress note at `docs/views/progress/<your track>.md` saying what is done, what is pushed and what comes next. Change `docs/STATUS.md` only when you merge to `main`, and then only your track's row. If your context passes about 100,000 tokens, write the progress note, push and stop, so that a fresh agent can continue. You cannot launch agents of your own or delete branches. Commit as `git -c user.name=Claude -c user.email=noreply@anthropic.com commit` with your session's attribution lines.

`main` is the live page, served at https://jampotful.github.io/seen-back/ about a minute after every push. Merge to it only where your prompt allows, only when every check passes, and only after fetching `main` again and merging it in, since other agents may merge at the same time.

Writing, in every file: plain sentences, Canadian spelling, no em dashes, no "not X but Y", no sentence fragments.
