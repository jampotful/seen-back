# Spider eyes: what can enter an experience

Assessment of accepted main `db8dac28b7536a8b1aceb7c4a65b46f8fa3acb0e`, 2 November 2026. Scope: desk-d384 through desk-d386, the current spider and jumper JSON specifications, and their relevant renderer/input paths. This is a representational assessment, not a new scientific audit or an acceptance of new evidence. The proposed change belongs on an isolated branch for the existing desk and app thread to review.

Reconciled before submission with main `87029dcd805bcd89127449a0cc0e4418ee0aade1`: intervening changes add d419/d420 and update the desk queue; all assessed evidence, app source and view files are unchanged. The branch retains those newer research integrations.

## Decision

The 124 records establish eye dimensions in particular taxonomic descriptions. **None supplies a new numerical rendering parameter.** Keep all observations, classifications, contextual qualifications and audit dispositions. Do not convert eye diameter into acuity, angular field, colour, response speed, motion preference, sensory dominance or perceived brightness.

They do make a single web-centred account of non-jumping spiders less defensible as a general destination. Differentiate future experiments by measured sensory tasks and named taxa, not by a family-average eye size. The small implementation below improves an already-supported web metaphor, using existing web-vibration evidence rather than claiming that the new anatomy proves it.

## What was actually accumulated

Run `python3 -I tools/views/spider_eye_transfer.py` to reproduce the counts, ranges, source DOIs, description groups and SHA-256 fingerprints. Its output is an inventory, not another evidence log.

| Accepted batch | Records | Species | Source papers | Audit disposition |
|---|---:|---:|---:|---|
| [d384](desk-d384.md) | 48 | 6 | 3 | Audits 564–569; contextual replacements accepted |
| [d385](desk-d385.md) | 36 | 5 | 1 | Audits 570–574; contextual replacements accepted |
| [d386](desk-d386.md) | 40 | 5 | 1 | Audits 575–579; contextual replacements accepted |

Total: 16 species, eight genera, five families and five papers. All 124 records have `evidence_kind: anatomical_measurement` and grade `m`; 108 use `eye_diameter_mm`, 16 use `sensory_anatomy`. Grade `m` describes the measured anatomy, not a demonstrated sensory ability. There are 31 four-eye-type description groups, **not 124 independent animals or experiments**. Some descriptions cannot be tied to an individual catalogue number; do not reinterpret the groups as a confirmed sample size.

Accepted input SHA-256 fingerprints (files remain unchanged):

```text
desk-d384 e1fddd21e619db67089ae8f76e0a9f5970c5ac5c454c717f09048d49b899fc82
desk-d385 d02d2d9a15d8137c847195b04ac197de662e2ebf5dd87b25bc5a40711d81c2b5
desk-d386 50da1b418ff9d6baea21c8bcb8d8b80bc98f6f4a94635f079907946682b1b517
```

| Family and represented genera | Records | Reported range, mm | Meaning and limit |
|---|---:|---:|---|
| Tetragnathidae: Tetragnatha | 16 | 0.07–0.11 | Diameters at the widest point; four broadly similar eye dimensions in these descriptions |
| Cheiracanthiidae: Cheiracanthium | 16 | 0.13–0.19 | Reported eye sizes; the audited Methods do not define diameter, so retain `sensory_anatomy` |
| Pisauridae: Qianlingula | 16 | 0.31–0.85 | Maximum dorsal diameters; larger absolute dimensions do not establish better vision |
| Dictynidae: Sudesna | 36 | 0.04–0.09 | Maximum dorsal diameters; small size does not establish blindness or a motion-only world |
| Thomisidae: Camaricus, Monaeses, Sinothomisus, Spilosynema | 40 | 0.01–0.22 | Maximum dorsal diameters; lateral eyes exceed their corresponding median eyes in all ten descriptions |

These ranges pool eye types, sexes and species only to inventory the collection. They are not family distributions, matched comparisons, population estimates or confidence intervals. The measurements differ in definition and specimen context. Body size, preservation, sex and life stage would need controlling before comparing relative investment across families.

For example, the female Qianlingula turbinata PLE is 0.85 mm (d384:48); the male Sinothomisus dawai PME is 0.01 mm (d386:27). Those are different eye types in different species, not an 85-fold performance difference. In the same male S. dawai, ALE is 0.18 mm and PME 0.01 mm (d386:26–27): a reason to study eye-specific functions, not permission to draw the PME blind or enlarge the ALE's field.

The accepted notes remain essential: Qianlingula's contradictory type labels and unresolved specimen identities; Cheiracanthium's caption/type-list conflict and undefined size convention; Sudesna's corrected specimen/description associations; and the corrected Thomisidae headings, captions and source context. All three dispositions retained values, traits, taxa and quotes. This assessment rereads the accepted records and dispositions; it does not claim to have independently remeasured or re-audited all five original papers.

## Comparison with the current views

| Existing choice | Current implementation | What the new records permit |
|---|---|---|
| Spider sharpness | `cpd: 0.5`, grade `?`; row borrows a roughly 2-degree scale from Cupiennius | No numerical update. Eye diameter lacks retinal sampling and image-quality information. The donor is a wandering spider, not these species. |
| Spider field | `fov: 300`, grade `?` | No update. Diameter and inter-eye spacing do not give optical-axis directions, retinal extent or binocular overlap. |
| Spider motion and pace | `gate: 1`, `persist: 0.15`, both `?`; the sheet borrows Cupiennius behavioural flicker results | No validation from anatomy. Flicker cutoff is not automatically a frame rate or an exponential trail constant. The categorical cue that only moving things reach the spider remains an unresolved metaphor, not a result of these batches. |
| Spider web/air/contact | Jolt/microphone inputs, ripples, optional web/air drawing and haptics | No new mechanosensory claim. The physical-input translation may be improved using the existing web studies, with invented mapping retained. |
| Jumper surround and front lateral region | 350-degree field; 0.5 cpd surround, 1.1 cpd front region | No update: these batches contain no Salticidae. Those existing source/grade assignments require their own evidence. |
| Jumper principal-eye gaze | 3.6 cpd moving cross, 2.5 × 21 degrees; Portia override 12.5 cpd; gaze timing and genus-specific colour | No transfer from the eight non-salticid genera. Large eyes alone do not justify the cross, moving retina, red channel or attention controller. |

Both JSON files remain `offered: false`. The older spider research sheet includes an earlier jumper sketch with a single central sharp region and says several engine functions do not exist. The current JSON and source code already have zones, gaze, microphone/motion inputs and the web overlay. Do not implement that old to-do list again. No claim here revalidates every older jumper row.

Eye dimensions can legitimately support anatomical illustrations, eye-pair comparisons within the described individual, specimen provenance and prioritization of later functional work. They can constrain an optical model only after adding lens geometry, focal length, aperture, retinal dimensions/receptor spacing and relevant spectral/transmission data. Diameter alone is not even a complete sensitivity model: integration time, receptor dimensions, tapetum and adaptation also matter.

## Differentiation worth pursuing

The following are design/research directions, not accepted per-family rendering presets:

| Ecological strategy | Consequential experience to investigate | Where the present evidence stops |
|---|---|---|
| Capture-web builders: Tetragnatha; mesh-web Sudesna | Events arriving through a connected surface; distinguish visual movement from web contact and airborne vibration | The new records do not measure web transmission, leg comparisons or visual dependence. An orb-web spiral is not a measured model of a Sudesna mesh. |
| Ambush hunters: the Thomisidae genera in d386 | Waiting while different visual regions detect changes at different rates; determine what actually initiates a turn or strike | Larger lateral eyes are a hypothesis-generating pattern. Their angular fields, thresholds, receptor properties and behavioural roles were not measured in these species. |
| Hunters without capture webs: Cheiracanthium, and a separately verified hunting context for Qianlingula | Active or intermittent orientation to prey and surroundings, without automatically assigning a capture-web experience | A silk retreat or nursery web is not evidence of capture-web sensing. Confirm species behaviour before assigning active versus sit-and-wait hunting; anatomy does not decide it. |
| Jumping spiders | Peripheral events redirect a small region of detailed inspection | Already a distinct experiment backed by separate literature; the new batches add no salticid function. |

Even this division has exceptions. Stafstrom and Hebets' **Deinopis spinosa** eye-occlusion experiments found a deficit for walking-prey capture but no significant field effect on aerial-prey capture; laboratory successes while occluded occurred when prey contacted support threads. A web-using animal can combine visual and mechanical tasks. [Primary study](https://pmc.ncbi.nlm.nih.gov/articles/PMC4892245/), Methods and Results; full main text read for this assessment. This does not establish performance for Tetragnatha or Sudesna.

**A functional lead for the desk:** Fischer, Scharff and Garm (2026), [Photoreceptor physiology of two species of crab spiders](https://doi.org/10.1007/s00359-026-01802-8), reports eye-specific ERG responses in Ozyptila praticola and Xysticus cristatus. Anterior lateral flicker cutoffs were about 19–20 versus 25 Hz; anterior median cutoffs were just above 10 Hz in both. The endpoint uses a 5% normalized ERG-response criterion after controlled light adaptation, not behavioural flicker fusion. Tested wavelengths were 430–680 nm, so this cannot exclude ultraviolet sensitivity or establish monochromacy. These are different genera from d386. Physiological eye-pair differences warrant follow-up; higher acuity, colour vision and specific hunting roles remain interpretations needing behavioural tests. Publisher Methods/Results/Discussion read; no evidence record admitted here. Repository search returned incomplete results, so the desk must deduplicate this lead against its current queue and accepted corpus before allocating work.

## What measurements would unlock the next change

Priority is the missing link to a perceptual task, not another batch of diameters.

1. **Does a stimulus trigger attention or action?** Within-individual prey/target trials separating visual-only movement, substrate contact, air movement and combined stimuli; sham-controlled, reversible eye-pair occlusion; report turn/strike probability, latency, misses and null outcomes under specified illumination. This could justify which events appear or call attention.
2. **Where can each eye see, and how much detail?** Optical-axis/visual-field maps, lens focal length and image quality, retinal area and receptor spacing; eye-specific behavioural grating or target-discrimination thresholds with contrast, orientation and light level controlled. This could justify region boundaries and blur. An anatomical sampling estimate must remain distinct from behavioural acuity; check whether degrees refer to a receptor separation, stripe width or full grating period before converting to cpd.
3. **How quickly and under how much light?** Eye-specific temporal contrast-response curves across adaptation and luminance, followed by behavioural detection measurements. ERG cutoff alone cannot justify film speed, reaction time or `persist = 1/cutoff`. Absolute sensitivity requires calibrated radiance/photon flux; camera auto-exposure is not a lux meter.
4. **What spectral distinctions matter?** UV-inclusive calibrated receptor recordings or absorption/opsin evidence, plus intensity-controlled wavelength-discrimination behaviour. Opsin presence, an ERG peak and behavioural colour vision are different claims. Phone RGB cannot recover a missing ultraviolet scene.
5. **What reaches the legs through a web?** Species-specific web geometry/tension, multi-point vibrometry at leg contacts, source-position/amplitude/frequency manipulation and behavioural localization. A single phone accelerometer cannot reproduce eight spatially separated leg signals or infer a prey direction from a jolt axis.

Keep taxon, eye pair, specimen/sex/stage, sample size, apparatus, stimulus, adaptation, tested range, uncertainty and nulls attached to any future parameter. Newly recovered functional records need the existing desk's independent audit and intake/preflight receipts, not admission through this PR.

## One small experimental improvement

**A web event can be seen and felt together.** Previously one `draw` URL choice selected either the web overlay or the haptic experiment. `?try=spider&draw=web&sense=motion` now selects the existing web overlay and the existing knock-triggered buzz together. The person still explicitly enables motion sensing. A browser that refuses, throws on, or lacks vibration gets the existing edge pulse. No new sensor, library, shader pass or biological number is added.

Implementation: a drawing option may name another direct option's `mode` in its own category. Only the spider's new haptic `web → buzz` alias uses it. Defaults, the separate `buzz` choice and all offered views remain unchanged. The spider's explanatory row and alias remain explicitly invented. The tactile output is an artistic translation of contact, not a reproduction of measured prey frequencies, eight-leg direction finding or spider sensation. It is a web study, not a hunting-spider preset or a validation of the generic spider optics.

The biological basis predates these batches: Landolfa and Barth (1996), DOI [10.1007/BF00192316](https://doi.org/10.1007/BF00192316), measured web vibrations and amplitude differences at the hub/legs in Nephila clavipes; the [author institution's abstract](https://ucrisportal.univie.ac.at/en/publications/vibrations-in-the-orb-web-of-the-spider-nephila-clavipes-cues-for/) was reopened. The app already represents this evidence in its web row. The existing 25 ms haptic pulse remains grade `i`; it is not a 5–30 Hz prey waveform. Physical haptic/accelerometer feedback, permissions, comfort and real-device timing still need phone testing.

## Verification and coordination

- The three accepted JSONL files pass the strict evidence checker: 124 records, zero problems. This is schema/classification validation, not a new source audit.
- `node tools/views/test_spider_web.js` tests the actual resolver and event handler: 225 option/category comparisons, experimental isolation, unchanged defaults, combined web/knock output, no repeat for one event timestamp, sound not causing a contact buzz, and vibration false/missing/throw fallbacks.
- All specifications pass `check_spec.py`; the checker rejects missing or chained alias targets. `build.py` and `node --check dist/app.js` pass. Build number remains 40; the app thread owns numbering and deployment.
- All 15 evidence-scope regression tests and the compiler checks pass. The two initially missing corrected-evidence fixtures were fetched at the accepted ref before the evidence-scope rerun; no fixture or evidence was modified.
- Browser integration, GPU/frame timing, the broad recognizer/browser suite and real-phone output are unverified. The local Playwright package has no browser executable. Logic tests do not replace those checks.
- No accepted evidence, historical audit, desk disposition, queue allocation, offered flag, recognition routing or dispatcher state is edited. No new research unit, continuation prompt or automation is launched. A pull request is the handoff; it does not imply that the private research launcher has read it or that the desk has accepted the scientific assessment.

**Desk/app-thread next steps:** review the transfer boundaries and the existing generic web cue; deduplicate the crab-spider functional lead and slot it into the existing workflow when appropriate; review the invented combined web/haptic experience and phone-test it before integration. Do not replace ongoing units or add a competing dispatcher. Only the app thread merges to main under `docs/HANDOFF.md`.
