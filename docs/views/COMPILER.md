# The spec compiler: what it sends, what comes back, what it checks

Written 13 October 2026 (the engine track, burst 5). A batch script, `tools/views/compile_spec.py`, drafts one view's spec and rows from the literature table and the evidence logs, through the Batch API from a build machine, as the literature extraction does (`tools/lit/extract.py`, job `lit-table`). The output is a spec behind `?try=`, never offered, which a person then judges on a phone. This file is what an agent needs to build the script in one sitting.

## 1. One job per view

The script takes a job file, `tools/views/compile/<key>.json`, written by a person or the research thread:

```json
{ "key": "owl", "chip": "Owl", "who": "an owl", "applies_to": { "order": ["Strigiformes"] },
  "taxa": ["Strigiformes", "Tyto alba", "Strix aluco", "barn owl", "tawny owl"],
  "topics": ["birds"], "logs": ["docs/views/evidence/birds.jsonl"],
  "draft": "research/birds:docs/views/drafts/birds.md#2.2", "like": "bird" }
```

`taxa` are the strings matched against each record's `taxon`, `family` and `order` (case folded, whole words). `topics` name files on `pub/lit-table` (`<topic>.jsonl`, one record a line: `taxon`, `trait`, `value`, `units`, `eye`, `method`, `conditions`, `where`, `quote`, `grade`, `note`, `source`). `logs` are evidence logs in the same shape with `rank`, `family` and `order` added. `draft` is optional. `like` names the nearest existing view; without it the script takes the spec whose `applies_to` shares the highest rank with the job's, and failing that `jumper`.

## 2. What the script sends (one request a view)

The **system** part is the same for every view and is cached:

1. The format: section 3 of `docs/ENGINE-DESIGN.md` from "Rules of the format" to the end of the section, verbatim.
2. The schema, written by the script from the code so that it cannot drift: every name `paramsOf` in `src/cam.a.js` reads from a view (`fov`, `cpd`, `topoA`, `topoS`, `fall`, `pupil`, `dof`, `M`, `gain`, `sat`, `sheen`, `noGreen`, `gate`, `field`, `persist`, `hold`, `rate`, `glow`, `living`, `salience`, `ripple`, `shimmer`), each block the viewer resolves (the list in `viewOf`: `spectrum`, `clock`, `pace`, `motion`, `slow`, `tilt`, `magnet`, `remap`, `overlay`, `sound`, `haptic`) with its keys, and each `&draw=` category with its option names (the regular expressions beside `P.fieldMode`, `P.ovlMode`, `P.sndMode`, `P.hapMode` and the other modes). Each name carries one line of meaning and a range: the range in `docs/views/floor.json` where one was measured, and otherwise the widest range any existing spec gives it.
3. The grades: `m` measured in this animal, `g` measured in a relative or a wider group, `i` the app's guess; `invented` true when the app chose the number, the mapping or the drawing.
4. The writing rules: plain sentences that a curious adult understands, Canadian spelling, no em dashes, no "not X but Y" and none of its variants, no sentence fragments, no reference to the app's code.
5. The answer's shape (section 3) as a tool definition, so the reply is one JSON object.

The **user** part is particular to the view:

1. The job (section 1).
2. The nearest view's spec, whole, as the example of form.
3. The records, numbered `R1` to `Rn`: every record whose taxon matches the job's `taxa`, then, for traits with no match, records of the same order or class marked `wider`. Each record goes as one line with `id`, `taxon`, `trait`, `value`, `units`, `eye`, `conditions`, `grade`, `quote`, `note` and a short source (first author and year). At most 300, by trait in this order: `acuity_cpd`, `fov_h_deg`, `fov_v_deg`, `binocular_deg`, `lambda_max_nm`, `receptor_classes`, `pupil_shape`, `absolute_sensitivity`, `cff_hz`, `eye_movement`, then the `sense_*` traits, then the rest.
4. The draft's section, when the job names one, marked as a proposal whose values must still be found in the records.

## 3. What the model returns

```json
{ "spec": { "key": "owl", "version": 1, "chip": "…", "who": "…", "falls_back_to": "bird", "applies_to": {…}, "cue": "…",
            "modules": […], "params": {…}, "matrices": {…}, "draw": {…}, "rows": [[grade, title, text, ["R12", "param:cpd"]], …] },
  "claims": [ { "path": "params.cpd", "records": ["R12", "R40"], "how": "between R12 (2.6 to 4) and R40 (21.9)" } ],
  "quotes": [ { "record": "R12", "quote": "…the words of the record that state the value…" } ] }
```

Every parameter's `src` lists record ids, never free text. Every parameter graded `m` or `g` has a claim. `how` says whether the value is a record's value, a range's middle, or a calculation, and gives the calculation.

## 4. What the script checks

A failed check sends the request once more with the errors appended. A second failure writes `docs/views/compiled/<key>.refused.json` with the errors for a person, and the script goes on to the next view.

1. **The spec checker.** `tools/views/check_spec.py` passes on the spec as returned.
2. **Records exist.** Every id in `src`, in a row's sources and in `claims` was among those sent.
3. **Quotes are found.** Each returned quote occurs in its record's `quote` after folding whitespace, quote marks and dashes; the record's own quote was already checked against the paper by the extraction pipeline.
4. **Grades are honest.** The script recomputes each grade and refuses a higher one. `m` needs a cited record of a taxon inside `applies_to`, for the trait the parameter stands for (a table in the script maps `cpd` to `acuity_cpd`, `fov` to `fov_h_deg`, `M` to `lambda_max_nm` and `receptor_classes`, and so on), whose value equals the parameter's or brackets it with another such record. `g` needs the same from a wider group. A value reached by a calculation is at most `g` and is `invented`. A matrix `from_pigments` needs each peak to equal a cited `lambda_max_nm`, within 2 nm.
5. **Invented is marked.** A parameter with no claim is `i` and `invented: true`, and some row graded `i` or `g` names it (`param:<path>`). Every `draw` option is `invented: true`.
6. **Inside the floor's range.** Each value lies inside its range. Where `floor.json` gives a floor for the parameter, a value that differs from the nearest view's by less than the floor at that value is reported as a change nobody will see, which is a warning and does not refuse.
7. **Rows read plainly.** No em dash, no "not … but" or "…, not …" in one sentence, the spellings in a short list (colour, grey, centre, metre, behaviour) and no code names (a word with an underscore, a dot inside a word or `@`). A row graded `m` cites at least one record that grades `m`.
8. **Only known options.** Every block, key, category and option is in the schema of section 2.

The script then rewrites each `R` id into the record's file and source (`birds.jsonl:Harmening 2009`), sets `"draft": true` and leaves out `offered`, and writes `views/<key>.json` with a report beside it (`docs/views/compiled/<key>.md`: each parameter, its grade, its records and its warnings). The build machine pushes the lot to `run/compile/<key>`; a person merges what they want.

## 5. Calibration and cost

Before the full run, the script compiles five views that already have hand-made specs (`jumper`, `owl`, `duck`, `fox`, `bigcat`) with their own specs removed from the example pool, and reports, parameter by parameter, how many values and grades match. The model is the cheapest that matches as well as the next one up on those five, as the extraction's calibration chose Haiku. A request is about 35,000 tokens in (6,000 of system, cached; 8,000 of example; up to 20,000 of records) and 5,000 out.

## 7. As built (the compiler track, 13 October 2026)

`tools/views/compile.py` (commands `plan`, `run`, `check`, `compare`), `tools/views/test_compile.py`, job files in `tools/views/compile/`, and the job `views-compile` (`.github/workflows/views-compile.yml`, `ci/views/compile.sh`, `ci/views/compile.env`). Where the build differs from the sections above:

- **Records.** The job's `taxa` match a record's taxon, family or order as whole words; `wider` taxa are used only for traits that have no record inside `taxa`. At most 16 records a trait and 300 in all, graded `m` and hand-log records first, with a spread of taxa. Audit verdicts (`docs/views/audit/<unit>.jsonl`, line number as id) drop retracted records and swap in corrected ones; a table record whose quote was not found in its source is dropped.
- **The reply** is a tool call with `spec`, `claims` and `quotes`. Haiku 5.5 sometimes returns `spec` as a string that runs on into the claims; the script reads it back. Sonnet 5.5 refuses a forced `tool_choice` and takes `auto`.
- **Checks** are those of section 4, with these additions: every numeric `m` or `g` value must be a cited record's value or lie between two of them (a calculation is at most `g`); the schema's widest range replaces the reply's range; a spec's `modules` are derived from the blocks it carries; a parameter graded `i` that no row names is named by one plain row, "Settings the app chose", which the report lists as added by the script; a row's parameter names written among its record ids are moved to the fifth element.
- **Retry.** One more request with the first reply and the errors appended; a second failure writes `<key>.<model>.refused.json`, and `compare` still reads that reply as returned.
- **Output.** `pub/views-draft/<label>/<key>.<model>.json` (the spec, `"draft": true`, record ids rewritten to `file:Author year`), `.md` (the report) and `COMPARISON.md`. Nothing goes to `views/`.

## 8. The second pass (the compiler2 track, 14 October 2026)

### The parameter mix-ups, and how each is handled now

The failed runs on `ci` (runs 1 to 19) were read against the records each run sent, rebuilt from `pub/lit-table` with `plan`. Most refusals of a sharpness value came from five mix-ups, and two more were in the compiler's own text.

| Mix-up | Seen in | Now |
|---|---|---|
| **Units.** 182 of the table's 1,363 `acuity_cpd` records are not plainly in cycles per degree: 83 are in minutes of arc, degrees, cycles per radian, Snellen fractions, decimal acuity or logMAR, and 99 are percentages, ratios to a human, words or numbers with no units. The checker took any number a record held, so 42 minutes of arc could stand as 42 cycles per degree, and a bracket could span two units. | cephalopod (Haiku), primate (Haiku) | Each sharpness record goes with `as_cpd`, its figure in cycles per degree, and `as_cpd_how` when the script converted it (`as_cpd()` in `compile.py`); a percentage or a ratio goes as unreadable. The checker judges a sharpness value only against these figures. A value that needs a conversion must be a calculation, at most `g` and invented. `interommatidial_deg` and `interreceptor_deg` count as sharpness through 1 / (2 x angle). |
| **Direction.** An angle runs the other way: a smaller angle is sharper sight. | primate (Haiku: 1.4 minutes of arc) | A value equal to a cited angle's raw figure is refused with the converted figure in the message; so is 1 / angle without the factor 2. |
| **Which eye.** The acuity of a separate small pair of eyes (the principal eyes of a jumping spider) was copied into `params.cpd`. | jumper (Haiku, four runs) | A `params.cpd` citing a record whose `eye` names principal eyes, AME or ocelli is refused, and the message says to put the figure in a zone. |
| **Fovea read as a separate eye.** `views/PARAMS.md` told the model never to take `cpd` from a fovea, which contradicts the engine (the blur is `cpd` at the middle, raised toward the edge by `topoA` or `topoS` with `fall`) and every hand-made vertebrate spec (hawk 60, bird 25, cat 8). | the glossary | `PARAMS.md` and the prompt now say: one kind of eye, best acuity including the fovea, edges blurred by `topoA`/`topoS` and `fall`; eyes with different jobs, the small pair in a zone. |
| **Field of view.** One eye's field or the binocular overlap taken as the whole field. | whale (hand fix in burst 7), bee | A `params.fov` citing a `binocular_deg` record, or equal to a record whose `eye` or `conditions` say one eye, is refused with the calculation to do. |
| **The compiler's own text.** `MEANING` said a human is 30 cycles per degree (the engine draws 60), that `topoA` and `topoS` ran along and across the long axis (they are a round middle and a horizontal band), and that `fall` was about light (it is the steepness of the edge blur); `TRAIT_MAP` sent `fall` to `absolute_sensitivity` and `topoA` to `fov_v_deg`. | every request | Rewritten from the shader (`src/cam.b.js`: the blur radius is blur x (1 + fall x topo squared)). |
| **Mixed-unit vectors.** A gaze value such as [degrees, ms, ms] graded `m` when a record gave one element. | jumper (Sonnet, 13 of 19 runs) | The prompt says how to grade a part-measured vector (`g`, invented, a calculation that names its parts). |

Two other changes: the rows follow `docs/views/VOICE.md` in the prompt, and the checker now refuses British spellings (it refused American ones before) and "people" or "a person" in a row or the cue; a reply's `gaze` block with no zone that follows the gaze is refused, since nothing would move. The tests are in `tools/views/test_compile.py` (23 new). `compile.py check --write <tag>` writes a reply that passes on rechecking.

### Which views now have specs

The fourteen offered views whose specs held only ungraded (`?`) parameters were compiled with Sonnet 5.5 (run 20 on `ci`, drafts on `pub/views-draft/c2a`, $2.45): cat, dog, squirrel, deer, rabbit, hawk, wader, bird, alligator, reptile, frog, bee, insect and plant. Each job's `taxa` are the genera the view stands for, so the compiler's `m`, `g` and `i` follow the carry rules of `docs/views/research/BRIEF.md` (Round 2), which the prompt now states. Thirteen passed every check, seven on the first request and six on the second. The rabbit's second reply was refused by a new field-of-view check that read a record's note too broadly ("monocular" in passing); the check now reads `eye` and `conditions` only, and the same reply passes and was written with `check --write`.

Each draft is offered only behind `?try=<view>`, through the view's `trial` block (`tools/views/promote_trial.py`): the offered view is unchanged; a hand-made trial setting (most are pigment matrices) is kept where it exists; the trial's rows are the draft's rows followed by the hand-made trial rows whose titles the draft does not repeat. The reports are `docs/views/compile/<view>.md`. Hand corrections: the wader's `cpd` and `rate` come from the pigeon, another order, so they are `i` (the carry rules let acuity and flicker travel only within a genus); the cat's and hawk's `gaze` blocks were left out (timings with no zone to move); two British spellings were corrected. Every trial passes the spec checker and `node test/check4.js try` with no error.

Not compiled: `person` and `other` (no animal to measure), `jumper` (hand-made and graded), and `reef`, `shark` and `spider`, which are not offered, so a draft could only replace the engine track's hand-made file.

### What a hand-made spec still does better

- **Mechanisms.** No draft added a zone, a gaze that moves or a drawing option; the hand-made jumper, owl and fox carry them. The drafts set the whole-picture numbers and the color matrix and stop there.
- **Carry beyond the taxa.** The checker knows inside and wider, not order and genus, so it cannot tell a pigeon's acuity carried to a heron (another order, should be `i`) from a red-tailed hawk's carried to a Harris's hawk. A person caught the wader's two.
- **Rows.** The drafts repeat a "Settings the app chose" row next to their own "What nobody has measured" row, and some verbs break the voice ("cones that answer to"). The one-voice pass should take them.
- **Units the extraction mislabeled.** The conversion trusts a record's `units`; a cycles-per-degree figure filed under degrees would be converted wrongly, and only a reader of the quote catches it.
