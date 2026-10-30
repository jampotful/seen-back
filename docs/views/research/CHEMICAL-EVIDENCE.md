# Chemical evidence: detection, response, emission and signalling

Prepared 30 October 2026 under the owner's OA-14 investigation request. Apply after desk integration to new submissions and explicitly reopened records. This clarifies desk-screen 10(a) and 10(d); it does not rewrite historical audits, change other traits' eligibility rules, or authorize mass reinstatement. The [OA-14 investigation](../../tracks/progress/oa-14-classification.md) supplies the source checks and calibration cases.

## Classify the experiment before choosing the trait

An instrument detecting a chemical released by a plant is not evidence that the plant detected that chemical. Chemical production, release, reception and a receiver's response are different endpoints. A receptor need not be identified for a controlled response to qualify, but an outcome measurement must not be described as a demonstrated receptor or transduction mechanism.

| Evidence demonstrated | Classification and admission |
|---|---|
| Biological chemical detection: a measured receptor, antennal, cellular or physiological response to controlled chemical exposure | `sense_chemical`, with the measured level and the existing tissue/organism eligibility limits stated. Instrumental GC/MS detection alone is excluded from this meaning of detection. |
| Living plant responds to an applied chemical, airborne blend, hormone, regulator or elicitor relative to a suitable control | `sense_chemical` under 10(a)/(d). Name the treatment, route, endpoint, duration and comparison. No implication of consciousness, olfaction, ecological communication or an identified receptor follows automatically. |
| Chemical present in tissue, or emitted without a tested cause or receiver | Physiology. An emission assay supports release under its sampling conditions, not biosynthetic rate, chemical reception or signalling. Baseline sampling alone does not establish that emission is constitutive in all environments. |
| Emission changes after an intervention | Induced emission describes the output. If the intervention isolates an applied chemical, the same experiment may support `sense_chemical` as a chemical-response endpoint. Herbivory, wounding, heat and light must not be relabelled chemical stimuli merely because the output is chemical; do not infer their sensory mechanisms from injury or metabolic change. |
| A living emitter's volatiles have an experimentally supported effect on a defined receiver | The owner's 10(a) signalling allowance can apply, with emitter and receiver explicitly identified. Demonstrate the chemical connection with an appropriate exposure, exclusion, airflow, odor-only choice, synthetic blend or comparable causal test. Distinguish receiver attraction/avoidance/priming from emission alone. |
| A controlled chemical-exposure trial reports no detected response | An eligible, condition-specific `sense_chemical` null, never proof that the species has no chemical sensing. Preserve power/detection limitations when reported. |
| No isoprene/monoterpene emission detected in a sampling assay | A condition-specific physiology null. It is neither a sensory null nor proof that the species cannot make the compounds or emit other volatiles. |

For signalling, record the direction. An emitting plant does not thereby become a measured receiver. A receiver using incidental odor is evidence of cue use; an evolved signal additionally requires evidence for that functional claim. Attraction of a herbivore can be exploitation of a plant's cue, not a plant adaptation to attract that herbivore. When evolutionary function is untested, use precise wording such as volatile-mediated interaction, receiver response or odor attraction. General introduction/discussion claims that VOCs defend plants or attract pollinators do not establish the function of each species' measured emissions. Constitutive emissions can have demonstrated signalling functions; induction is neither necessary nor sufficient for signalling.

## Preserve physiological measurements separately

Use `physiology_volatile_emission` for independently verified emission findings that do not support a sensory or signalling claim. BRIEF permits a new key when no existing one fits: include `new trait` and the reason in `note`. This is a research evidence category, not an automatic app feature or sensory-coverage credit. Do not alias it to `sense_chemical` in coverage, inheritance or rendering.

The record must identify the source taxon or sample label, tissue and whether attached, collection/analytical methods, compounds or compound classes actually assayed, relevant conditions and controls, and whether induction was tested. Preserve detection limits as the source states them; do not convert instrumental limits to a biological threshold without the required sampling information. An assay of tissue content needs its own appropriate category, not this emission key.

For the Danum table, the positive wording is: emission detected in the isoprene/monoterpene assay under the study's conditions. The table does not identify which of those classes each positive row emitted. The negative wording is: neither assayed class detected under those conditions; production capability and other VOC emissions were not determined. Do not use a bare emitter/non-emitter species binary. Do not infer lifetime constitutive production from absence of an experimental induction treatment.

All ordinary source-access, faithful-quotation, taxon, grade, partial/provenance and independent-audit requirements still apply. `m` identifies the taxonomic relation of a measurement; it does not certify a sensory mechanism. `partial: true` does not repair an unverified taxon or missing causal experiment. A familiar binomial or an accepted-name database match does not validate the specimen identification.

## Identification and provenance gate

1. Preserve the source's label, authority, row and original record identifier. Keep any accepted-name mapping separate, with its authority and date. Never silently replace a suspicious species with a plausible local relative.
2. Check geographic plausibility against native **and introduced/cultivated** ranges, site description, vouchers or sample identifiers and the paper's actual sampling design. Absence from a checklist is a flag, not proof of impossibility. Malaysian occurrence does not by itself establish occurrence at Danum Valley.
3. Where many table identities conflict with the site, hold taxon-specific admission until sample-to-row provenance is resolved. An unflagged name is not independently cleared by omission from the original flag list.
4. An unidentified `Genus sp. 1` or family-level morphotaxon remains that particular source sample. Do not turn it into a family/genus-wide yes/no phenotype, identify it to species, or let an arbitrary `g` grade settle sensory cells. Keep distinct morphotaxa distinct.
5. Resolve compilation versus original measurement from the source, not from a conjecture about suspicious names. If later documentation establishes imported measurements, cite their actual origins and use the applicable partial flags. Until then, retain the discrepancy and hold.

## Review and app interpretation

In the existing scientific review, state stimulus, receiver/emitter role, endpoint and causal support. Reuse the paper's reconciliation; no second form or extra agent is required. Follow scientific-preflight when that separate workflow is integrated. Keep 40-word quotations, consequential qualifications and the current audit counting rules.

For app explanations, keep chemistry received separate from chemistry released. Incoming chemical responses can support a response depiction at the demonstrated scale and timescale. Emission evidence can inform a clearly identified depiction of outgoing chemistry, with its function unknown where untested. A phone-camera plume or color effect remains a representation/fabulation, not a measurement of airborne chemicals or a demonstrated plant perceptual field. A negative assay must not produce an absent-sense badge.

The existing 10(a) emitter allowance is retained. A future split of demonstrated sender interactions into a dedicated `chemical_signalling` trait, with migration of accepted records and revised UI/coverage mappings, is a separate owner/schema decision. No such migration is made here.
