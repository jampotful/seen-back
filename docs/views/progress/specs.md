# Progress: specs track (burst 2)

Started 13 October 2026. Branch `agent/specs`, from `main`.

## Done and pushed

- `tools/views/check_spec.py`: the spec checker, written from `docs/ENGINE-DESIGN.md` section 3 (no checker existed on `main` or `agent/engine` at 13 Oct). A row links to a parameter by listing `param:<name>` among its sources, or by sharing a source string with it.
- `tools/views/make_specs_a.py`: writes the first batch. Run `python3 tools/views/make_specs_a.py` then `python3 tools/views/check_spec.py` from the root.
- Specs written and passing the checker: fungus, slime, fish (with `by` for sunfish, damselfish, catfish and a `reef` variant carrying the engine agent's `TRY.reef` values), shark (ray as a variant, `TRY.shark` values), spider (other spiders), snail, sealife (starfish and sea urchin as a variant).

## Still to do

- Specs: crab, mammal, salamander, worm, bat, tick, flying fox. Sheets are in `docs/views/sheets/` (crab, mammal, salamander, bat, tick); worm and tick also in `docs/views/drafts/ground-invertebrates.md` on `research/ground-invertebrates` (section 2.4 worm, 2.2 millipede, 2.3 centipede, 2.7 tick); salamander in `drafts/herps.md` on `research/herps`; mammal in `drafts/mammal-groups.md` on `research/mammal-groups`; flying fox in `bat.md`.
- Re-check fish against the final audits (`fish.audit.md`) and the research draft; the checked sheet gave the base values, the draft gave the settings.
- Step 3: if the engine's module 0 loader exists on `agent/engine`, render each spec with `?try=<key>` in headless Chromium. At 13 Oct (`de1fd5c`) no loader exists, so none of this is done.
- Step 4: `docs/views/review/jumper.md` and its PDF in the owner's Drive folder.

## Conventions used

- Only today's fields (`fov cpd fovea fall topoA topoS pupil dof M uvBlue sheen gain sat noGreen gate field persist hold thrust rate`). `M` is the name of a 3 by 3 matrix in `matrices`, row by row as the engine reads it. Mechanisms the engine lacks are listed under `notes` with the module that would draw them; `zones` is empty in every spec.
- Each spec carries `"draft": true`, since row wording is rewritten later in one pass.

## Burst 3 (13 October)

- Merged `main` into `agent/specs`; the engine track's shark, spider and checker were kept.
- `tools/views/make_specs_b.py` writes crab (with woodlouse and horseshoe crab as variants), mammal (raccoon and mole as variants), salamander, worm, bat, flyingfox and tick. Rows come from the sheets' own row lines; the worm rows from the ground-invertebrates draft, section 2.4. All pass the build's checker.
- Next: render each with `?try=<key>`, merge to `main`, then the jumper review sheet and its PDF.
- Rendered `?try=` for all seven in headless Chromium (the page's self-test with `&try=`): no GL error and a non-blank picture for each. The worm drew a flat picture at cpd .014 (spread 0), so it takes `field: 1`. The self-test's "zone programs compiled" check fails for every view without zones (fungus, snail and these seven alike); it is the test, not the views.
- Jumper review sheet: `docs/views/review/jumper.md` and `.html` from `tools/views/make_review_jumper.py`; the PDF (two pages, landscape) is printed by `tools/views/make_review_pdf.py` with reportlab, since a Chromium print embeds fonts as outlines and was too large to pass through the Drive tool. Uploaded to the owner's Drive. Next: the owner sends it to a specialist, and the answers go into `jumper.json`.
