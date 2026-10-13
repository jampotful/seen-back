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
