# Seen Back

*Working title.* A camera that takes on another creature's way of seeing.

You photograph something alive. The app works out what kind of living thing it is, and your camera view changes toward what is known of how that kind sees: its field of view, where its sight is sharp, the shape of its pupil, its colours, and the pace at which it takes in movement. Where the camera has to guess, the app says so, line by line.

Every meeting is kept in a record, and eyes you have met can be looked through again.

## Status

A working prototype. It runs in a browser on a phone or a computer, and can be added to the home screen.

| Part | State |
|---|---|
| Camera engine (WebGL 2: field, sharpness, pupil-shaped defocus, colour, motion) | working |
| Sixteen kinds of eye, each line graded as measured, measured in a relative, guessed, or left out | working, awaiting review by a vision scientist |
| Record of meetings, and looking again | working |
| Recognition on the device | not yet built; the page asks you what it was |
| Species-level recognition | not yet built |

## Run it

```
python3 -I build.py                                   # builds index.html, sw.js and dist/
python3 -m http.server 8765 --bind 127.0.0.1          # then open http://127.0.0.1:8765/
```

A page may use a live camera only at an `https` address or on `localhost`. Opened as a file on a phone, it falls back to a photo of who you met and a clip of your own view.

## Layout

- `src/` holds the parts of the page: the markup and styles, the eye models, the engine, the app logic, the record.
- `build.py` joins them into `index.html` (the standalone app) and `dist/seen-back.artifact.html`.
- `test/` holds the browser checks (Playwright) and their media. `tools/make_test_media.sh` makes the fake camera feed.
- `docs/PLAN.md` is the plan, `docs/LOG.md` the running log, `docs/SOURCES.md` the sources behind every graded line.

## What is measured and what is invented

Each line the app shows about an animal's sight carries a grade. `docs/SOURCES.md` lists the source for every measured line and names every convention that is this project's own invention, among them: sharpness drawn against the viewer's own eye, a faster eye suggested by slowing the picture, depth guessed from height in the frame, and ultraviolet drawn as violet.

## Data and licences

- Typeface: Instrument Serif, SIL Open Font License 1.1 (`fonts/OFL-Instrument-Serif.txt`).
- The Gainesville list in `src/cam.g60.js` counts iNaturalist research-grade records gathered by GBIF for one town in October and November.
- No licence has been chosen for this code yet.
