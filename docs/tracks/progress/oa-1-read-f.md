# oa-1 reading pass, reader F (18 October 2026)

Prompt: `docs/tracks/prompts/oa-read.md`, with the control room's two later instructions (run `tools/views/oa_lint.py` before each commit; the corrected grade rule). Entry 77 of `oa-1`, read from the text the `oa` job fetched again for this reader (branch `run/oa/read-f`, run 8, `runs/oa/8-oa-1` on `ci`). The text decrypted with a matching checksum, and the checksum equals the rescue run's (`runs/oa/2-oa-1`), so the audit can use that text. Reading branch: `agent/oa-read-f`. This note is named `oa-1-read-f.md` because reader C writes `oa-1-read.md` for other `oa-1` entries at the same time.

## Counts

| Entry | Paper | Copy | Records | m | g | i | partial |
|---|---|---|---|---|---|---|---|
| 77 | Abdel Keream 2013, Topographie und Verteilung retinaler Zellen bei Caniden (Diplomarbeit, Wien) | thesis PDF, University of Vienna repository | 72 | 70 | 2 | 0 | 8 |

One line added to `docs/views/sources/oa-1.jsonl`. Every record passes `quotecheck.py` (72 verbatim) and `oa_lint.py --text` against the thesis.

## Source record

Crossref has no record of the thesis, so `authors`, `year` and `journal` come from its title page: "Verfasser MOHAMED ABDEL KEREAM" (written `Abdel Keream M`), "Wien, 2013", a Diplomarbeit for the Mag. rer. nat. in Zoologie, prepared at the Abt. f. Neurophysiologie u. Neuropharmakologie, Ztr. f. Physiologie u. Pharmakologie, Medizinische Universität Wien. Title, DOI (10.25365/thesis.30387) and URL are as in `ci/oa/sources-r1.jsonl`. Every quote is the German exactly as the file holds it, and every `note` gives an English rendering.

## What was logged

- Tab. 1, one row per animal (red fox, black-backed jackal, and six dog breeds: Chihuahua, Dobermann, Border Collie, Chinese Crested Powderpuff, German Shepherd, Rottweiler): eye diameter, eye axial diameter, and the counted minimum and maximum density of labelled cones per mm2, all `m` (30 records).
- The Results' maps, one retina per animal (two for the German Shepherd): area centralis and visual streak for each animal under `fovea`, the map maxima and peripheral densities stated in the text under `cone_density_mm2`, and the red fox's S-cone maximum (2880 per mm2). Where the Results and the Discussion disagree (German Shepherd and Border Collie visual streaks), both statements are logged and each note names the other.
- Values that are not the thesis's own measurements, `m` with `partial: true`: the wolf's ganglion-cell topography from Peichl (1992), wolf and dog orbit angles from Hormann (2013), the dog eye-diameter range from McGreevy et al. (2004), and two uncited background statements on single species (vertical slit pupil of the red fox, skin-covered eyes of Spalax arenarius).
- Group records, `g`: a tapetal zone in an opened canid eye (the caption does not say which canid) and the fovea of diurnal primates.

The thesis counts L cones (antiserum JH 492) in every animal and S cones (JH 455) in one fox. The cone densities use the existing new-trait key `cone_density_mm2`; the orbit angle uses a new key, `orbit_angle_deg`, because the thesis does not define the angle.

## Not logged

- Tab. 1 lens diameters (LD, LAD) and Tab. 2's ellipse factors of the isodensity lines: no BRIEF trait.
- Retina areas and radii (800 and 8200 mm2, a 17 mm radius, an 11 mm diameter): no BRIEF trait, and the two areas disagree by a factor of ten.
- The sections on domestication, genealogy and breed groups: no measurement.

## Conventions and deviations

- Tab. 1 rows are quoted from the `=== LAYOUT ===` section (whitespace collapsed); the plain-text part holds the same rows value by value.
- Dogs are logged as Canis lupus familiaris, the form the thesis's text uses (Tab. 1 prints Canis familiaris), with the breed in `conditions`.
- The key pair lives in `/tmp/oa-f`, not `/tmp/oa`, because other readers share the machine. It was never committed or printed.
- Grades were first written under the prompt's narrower grade line and corrected in commit 07f33e1d after the control room's message.

Nothing in the thesis was left unread.
