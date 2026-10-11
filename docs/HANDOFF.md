# Handoff

For whoever picks this work up next, person or assistant.

## Where things are

- **This repository** is the source of truth for the app. `python3 -I build.py` builds it. The address it is served at is the repository's GitHub Pages site.
- **Private working notes** are not in this repository. They hold the brief, the decisions, who is involved, and what has been promised. An assistant working for the owner will find them in the owner's Claude project, in the document `claude/seen-back-working-notes.md`. Read that first.
- `docs/PLAN.md` is the plan with its checkboxes. `docs/LOG.md` is the running log. `docs/SOURCES.md` backs every graded line in the app.

## How to work on it

```
python3 -I build.py                              # index.html, sw.js, dist/
python3 -m http.server 8771 --bind 127.0.0.1     # serve the repository root
sh tools/make_test_media.sh                      # once: the fake camera feed (needs ffmpeg)
PORT=8771 NODE_PATH=<playwright> node test/check4.js lex|record|viewer|edge|sweep|film
```

- Headless Chromium needs `--use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader --ignore-gpu-blocklist` where there is no graphics chip; the checks pass these already. Software graphics are slow, so the checks ask for a small picture with `?side=420`.
- The page has two wrappers. `index.html` is the standalone app. `dist/seen-back.artifact.html` is for Claude's artifact viewer, which allows fonts only from Google Fonts, allows no network calls except to itself, and refuses the camera.
- Inside that viewer the page can ask Claude to recognize a photo, and it keeps the record in the viewer's private store. Outside it, recognition has to come from the page itself. That is Phase 2 of the plan.

## Rules the work is held to

- A claim about an animal ships with a grade and a source, or it is marked as a guess.
- Nothing is called done that has only been run in software graphics. Say what was run and on what.
- Secrets never enter the repository. `hf-token.txt` is ignored by git.
- The repository is public. Private notes, names of collaborators, and plans for approaching other organizations stay out of it.

## Next steps, in order

1. Confirm the site is live at its https address and the camera opens on a phone.
2. Phase 2: read the licence of the candidate encoder, fetch it, compute label embeddings, run it in the page, measure.
3. Phase 3: build the local species list from GBIF with taxonomy and monthly counts; run BioCLIP 2 against held-out local photos; report numbers.
4. Keep `docs/LOG.md` current, and tick `docs/PLAN.md` only for what has been measured.
