# Mélotte 2018: species hearing evidence and representation handoff

Proposed evidence, pending independent scientific audit. The eight source-labelled audiograms are in [the evidence log](../evidence/melotte-2018.jsonl) and [structured supporting data](../sources/melotte-2018-audiograms.json). Read the [verification and integration report](../../tracks/progress/melotte-2018.md) before using them.

## What this adds

Use the existing `sense_hearing` trait. One record represents one species-labelled AEP audiogram: `value` stores its tabulated response endpoints in Hz; `method` identifies the neural measurement; `conditions` preserves the experiment; `note` contains every frequency/mean/SD/responding-N tuple and its limitations. The companion JSON transposes the same measurements into arrays for future use. It is supporting data, not a new runtime schema or a second set of evidence records.

Six records propose direct species evidence (`m`): Metynnis lippincottianus, Myloplus rubripinnis, Serrasalmus elongatus, Serrasalmus spilopleura, Pygocentrus nattereri and Pygocentrus piraya. Piaractus brachypomus and source-named Myleus schomburgkii are `g` because later species splits leave the 2018 aquarium-trade cohorts' modern identities unresolved. Those two curves are usable as qualified historical-cohort comparisons, not as grade-m measurements of modern species. Do not promote them by synonym replacement.

## Differences a representation could use

- Retain frequency-dependent threshold profiles. A binary 50–3600 Hz filter would erase large mid-frequency differences. The source-labelled Piaractus cohort required 120.0 ± 4.2 dB re 1 µPa at 1200 Hz; Pygocentrus nattereri required 92.4 ± 4.0 dB, both N=10. The 27.6 dB difference is arithmetic from the means, not a loudness ratio or a behavioural result. Keep the Piaractus identity qualification attached to any comparison.
- Preserve the high-threshold region around 2100/2400 Hz and the subsequent fall in thresholds. This is a region of **poorer** sensitivity. In Myloplus rubripinnis and Pygocentrus piraya, the particularly high means at 2100 Hz are 142.0 ± 6.0 (N=3) and 144.6 ± 10.0 (N=5) dB re 1 µPa. Do not smooth the curves into an assumed monotonic low-pass filter.
- Describe broadly stronger low-frequency sensitivity without presenting the lowest sampled mean as an exact tuning optimum. Seven of the tabulated curves reach their lowest sample mean at 600 or 300 Hz; Metynnis lippincottianus reaches it at 150 Hz. The paper's general best-hearing band is about 50–900 Hz.
- Preserve individual-response counts at the high-frequency edge. Piaractus has just one responder at 3600 Hz and Myloplus rubripinnis one at 3000 Hz. Neither endpoint justifies a hard perceptual cutoff for all individuals.

The paper finds broad overlap across species and across diet/vocal categories, despite some significant frequency-specific differences. These measurements do not establish that carnivorous fish have better hearing, that vocal species are more sensitive, or which natural sounds individuals attend to.

## Fit to the present app

At the inspected main revision, `views/fish.json` enables `tilt`; it has no hearing row or hearing effect. `docs/views/gaps/try-rows.json` maps fish's “Water moving” to `sense_airflow`, not `sense_hearing`. The fourteen offered-view mappings also contain no hearing trait. Therefore this submission adds evidence for future species-specific hearing representation; it does not claim that eight present gap-table cells have closed or that the live fish view has changed.

`views/PARAMS.md` describes microphone-driven `sound` effects and makes their drawing weights an app choice. The present hearing evidence cannot calibrate an airborne phone microphone to underwater pressure, supply particle-motion thresholds, or reproduce fish perception. Any future visual weighting, interpolation between sampled frequencies, normalization, gain or mapping to light/motion must be labelled invented and reviewed separately. A direct comparison display of the published AEP points with SD and N is supportable; a claim to simulate behavioural hearing is not.

## Species row proposal after audit

For a directly measured species, a restrained hearing row can say: “Your auditory pathways respond most sensitively to low-frequency sounds in laboratory tests. These measurements record neural responses; they do not establish what sounds you notice or act on.” Link the exact species record and show the tested protocol when expanded. Retain a separate omission/invention disclosure if the view does not render hearing or uses an artistic mapping.

Do not copy this row to relatives or the whole family. Do not publish the two identity-restricted records as direct statements addressed to modern Piaractus brachypomus, Myloplus schomburgkii, Myloplus sauron or Myloplus aylan.
