# Burst 1: the engine (Opus)

Read `docs/tracks/engine.md` for the code, the checks and the rules. This file narrows its scope for this burst. Stop after 75 minutes.

1. **The attention module**, as data-driven engine fields documented in `docs/ENGINE.md`:
   - a small motion-salience map from the frame ring, with the phone's own movement removed (the image's mean motion);
   - a cue for the motion of living things: local motion that is coherent over a small patch;
   - a gaze zone that jumps to the most salient place outside an inhibition-of-return mask, dwells, scans in small sweeps, and leaves the mask to fade over about five seconds.

   Read the map back asynchronously, so the frame never waits.
2. **The `jumper` view**, reached only with `?try=jumper`, following `docs/views/drafts/jumper.md` and `docs/views/evidence/jumper.jsonl`. The research agent working at the same time pushes better values to `research/jumper`; fetch it once near the end. Its rows are placeholders graded `i`.
3. **A tuning panel**, shown only with `?try=<view>&tune=1`: sliders for the view's parameters (the attention module's and the existing fields'), applied live, with a button that copies the current values as JSON. The owner tunes on a phone and sends the values back; most iteration then costs no agent time.
4. **Checks.** Every existing check still passes. Add a check that `?try=jumper` draws with no GL errors and that the gaze moves to a moving target in a test clip.
5. **Report** frame times from the About block for today's views and for `jumper` in headless Chromium. These numbers are only for comparing views with each other.

Not in this burst: the render gallery, new sensor inputs (microphone, motion sensors), other views.

Keep your context small. Print only the tails of test output, look at a few screenshots at most, push every 15 minutes, and if your context passes about 100,000 tokens, write `docs/views/progress/engine.md` and stop, so that a fresh agent can continue. Final report, at most 250 words: what works, the frame times, what needs the owner's phone to judge, and your last commit.
