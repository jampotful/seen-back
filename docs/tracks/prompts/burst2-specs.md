# Burst 2: specs for the fourteen waiting groups, and the specialist's sheet (Sonnet)

Start with `burst2-common.md`. Your track is `specs`.

Read `docs/ENGINE-DESIGN.md`, sections 2 (module 0's row) and 3 (the spec), and `docs/views/sheets/README.md`. For each of the fourteen groups module 0 unlocks (fungus, fish, spider, snail, sealife, crab, mammal, salamander, worm, shark, slime, bat, tick, flying fox), read its sheet and audit in `docs/views/sheets/`, and grep the matching research log where one exists (`research/plant-fungus-slime`, `fish-shark`, `spider`, `sea-invertebrates`, `mammal-groups`, `herps`, `ground-invertebrates`, `methods`; grep, never read a log whole). `src/cam.a.js` on `agent/engine` has prototypes for reef, shark and spider; carry their values over. Stop after 120 minutes.

1. On `agent/specs`, from `main`, write `views/<key>.json` for each group, following section 3 exactly. Use only fields today's engine already has, since these groups were chosen because their sheets fit today's settings. Give each parameter its value, grade, source (the sheet or log line), range and `invented` flag. Draft rows plainly from the sheets' graded statements; their final wording comes later, in one pass over every view. Where a group needs a new mechanism to be drawn faithfully, say so in a note and draw it with today's fields.
2. Fetch `agent/engine` and `main` for the engine agent's spec checker and use it if it exists; otherwise write `tools/views/check_spec.py` from section 3. Run the checker on every spec.
3. Near the end, fetch `agent/engine` again. If module 0's loader exists, render each spec with `?try=<key>` in headless Chromium and confirm it draws with no GL errors.
4. **The specialist's sheet for the jumper view**: `docs/views/review/jumper.md`, one page and two at most. Give every parameter of the jumper table (value, units, grade, short source), two blank columns for the reviewer's value and comment, then the six questions from the end of `docs/views/drafts/jumper.md`. Name no person except cited authors. Print it to PDF with headless Chromium and upload the PDF to the owner's Drive folder named in your launch prompt, with the Drive tool's `create_file`.

Final report, at most 250 words: the specs written and checked, the groups that need a new mechanism, where the PDF is, and your last commit.
