# Instructions for outside agents (Codex and others)

A task that names `docs/tracks/prompts/external-sweep.md` or `docs/tracks/prompts/oa-pass.md` is a research task. For it, start nothing and run no checks: no build, no `prepare.py`, no servers, no Playwright, no browser tests and no self-test. It needs Python 3 with `requests` and `pypdf`, and internet access. Follow the named prompt, which says which files you may write.

For a task on the app itself, the environment's start instructions apply.

Never reach a paper through a library login, a university proxy, Sci-Hub, LibGen or any other unauthorized copy. Never commit a paper's PDF or full text, because this repository is public.
