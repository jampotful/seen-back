# Classifying nonvisual light evidence

30 October 2026. Prospective research and audit rule, motivated by audit 224. Apply to fresh units after integration. Historical audits and dispositions remain unchanged. This specifies trait fit and supplements existing source, quotation, taxon, provenance and scientific-context rules.

## Decision

File a plant finding under `sense_light_nonvisual` when the source reports an organismal endpoint compared across an explicit light exposure contrast, or a directly measured light-related function already within the owner's scope, such as epidermal focusing. Classify the **individual finding**, not the paper, its title, the organism's reputation or the authors' preferred explanation.

Photoperiod, irradiance, light/dark, spectrum, UV, shading and night interruption remain in scope. Growth, germination, development, physiology and metabolism remain eligible under the owner's 25 October scope; molecular identification of a receptor is not required. A lighting treatment can establish an endpoint response without establishing a sensory pathway, day-length timer, adaptive purpose or subjective perception. Longer lighting also changes daily photon dose unless the design separates them. Do not call an energy-dependent growth response proof of photoperiodic time measurement.

Natural light is eligible. A greenhouse is not automatically controlled, and a field study is not automatically observational. Blackout, night-break and shade-net experiments can manipulate sunlight. Inspect what was actually varied and compared.

## Evidence basis and permitted claim

Use the following literal basis in `method` for new light records, followed by the actual design. These are descriptive evidence categories within existing fields, not new traits or replacements for `grade`/`partial`.

| Basis | Required evidence | Permitted claim and limits |
|---|---|---|
| `experimental light contrast` | A defined lighting intervention and comparator, with the endpoint measured in the record's taxon. Identify assignment, replication, other treatments and relevant co-varying conditions as reported. | Describe the observed treatment comparison. Attribute a light effect only to the extent the design separates light from alternatives. If shade changes microclimate or treatment is confounded with chamber/site, identify the treatment bundle and limits; do not claim an isolated light effect. Crossed factors and within-factor contrasts are eligible. |
| `observational light association` | The source documents different actual light exposures (measured, calculated, or explicitly characterized, such as sun/shade), links them to measured endpoints through an explicit comparison or analysis, and supplies enough design information to describe the association. | Say **associated with**, **covaried with**, or **differed between the stated light environments** in `value`. Name major co-varying factors and limits in `conditions`. Adjusted regression supports conditional association; it is not automatically a causal experiment. A quasi-experimental causal claim needs an identification argument and assumptions assessed in audit. |
| `direct light-related function` | A measured function such as epidermal light focusing, within existing owner-approved scope. | Describe the measured function. Focusing alone does not establish a downstream physiological response or receptor mechanism. |

All three require a source-supported endpoint, contrast/function and applicability. With inaccessible methods, use a limited claim only if accessible material establishes those essentials; otherwise hold it. Do not invent a missing comparator or assignment. Keep null results: “no detected difference in germination between the tested photoperiods” is eligible and differs from both “light has no effect” and “no light comparison was made.” Preserve tested ranges, endpoints and important interactions; a null for one endpoint cannot erase an effect on another.

### Cases that do not supply a measured light response

- **Population origin in a common environment:** provenance differences under one shared lighting regime measure provenance-associated phenology, not response to a light contrast. Latitude of origin is not exposure at the experimental site. A common garden can support population differentiation without identifying the cue or excluding maternal/epigenetic carryover. A shared seasonal trajectory does not turn different event dates into tested critical photoperiods.
- **Multiple gardens or planting dates:** these create environmental contrasts but do not alone isolate light. They qualify as observational light associations only when the paper explicitly relates documented exposure variation to the endpoint. Site, date, latitude or season used only as a proxy is insufficient. Retain relevant coupled temperature, moisture, irradiance and age/cohort factors. Do not calculate day length at flowering and relabel it a tested threshold.
- **Mechanistic interpretation:** author attribution to photoperiod, candidate clock-gene expression, a pathway annotation, seasonal flowering or an adaptive explanation is not an additional measured light response. A measured genotype difference under constant light remains a genotype difference. If the paper separately tests a light contrast, assess that result separately.
- **Cited established response:** secondary evidence from an earlier experiment remains possible under existing rules, with the original study identified and `partial: true`. The accessible source must actually report that result; a general explanatory citation does not establish it for the current population or endpoint. Never borrow an earlier study's intervention to upgrade current common-garden measurements.

Keep unresolved light interpretations and useful phenological observations without a qualifying light comparison in the unit's progress note with source and reason. They do not close a light-response evidence gap. Use another existing trait only if the measured endpoint fits it; seasonal bud set is not automatically `diel`. Do not create a new biological sense to house an evidential weakness. A future phenology catalogue needs an explicit design.

## Measurement, interpretation and explanation

1. **Measured result:** put the endpoint and actual contrast in `value`. An association qualification must remain visible there even if methods/notes are hidden. Retain material nulls, reversals and limits.
2. **Supported interpretation:** put an explicitly attributed interpretation and its basis in `note`, distinguished from what was tested. A light-treatment effect can support photoperiodic regulation while the receptor remains untested. Wording or grading cannot promote an interpretation into a measurement.
3. **Speculative causal explanation:** identify it as untested in the progress note or, only when needed for an otherwise eligible result, in `note`. It cannot qualify a record or strengthen its measured claim.

`m` is not a causal-certainty grade: an association measured in the named taxon can be `m` **as an association**. Keep existing grade rules for taxonomic transfer and predictions. `partial` describes source provenance/access as required by the reading prompt; it does not repair trait fit or causal overstatement. Neither changing `m` to `g` nor setting `partial: true` supplies an absent light comparison. If a renderer or summary drops the qualification, hold that use until it is preserved. A covered cell means evidence exists, not that a universal positive effect or molecular mechanism has been demonstrated.

## Research and audit procedure

During ordinary source reading, answer: **What light variable/function was compared or measured? What endpoint? What other factors varied? What inference does the design support?** Use the answers to select the basis and wording. Source reconciliation, faithful quotation and independent audit remain necessary; this is not another verification workflow.

- Screeners retain plausible experiments and explicit natural exposure-response studies as leads. If accessible evidence cannot distinguish origin from exposure, hold for reading; uncertainty is not a negative search finding. Inspect Methods before rejecting a study because its title says natural, field or common garden.
- Readers state the basis in `method`, limits in `conditions`, and distinct author interpretations in `note`. Where the launch uses PR #45's scientific preflight, reuse `design`, `reconciliation` and per-record `claim_check` for these answers. Create no duplicate receipt, second review or required JSON field.
- Auditors check whether `value` stays within the comparison's inferential limits. No qualifying comparison/function means hold or reject this trait claim, not declare the species insensitive to light. An inaccurate basis label with accurate meaning can be harmless documentation; absent contrasts, causal overstatement and lost consequential qualifiers are scientific-meaning errors under `oa-audit.md`. Count each affected record once. Use `correct` when a narrower eligible claim is supported and `retract` from this trait when none is; keep access gaps explicit.

## Calibration and rollout

- **Populus balsamifera, audit 224:** the two 2007 population means remain a provenance contrast under shared natural light. Author attribution does not admit them as measured light responses. The unsupported “range” claim remains a separate fault. Audit 224 and its rejection stand.
- **Larix laricina, sweep-28:3:** the 6-, 10-, 14- and 18-hour treatments establish a light contrast across provenances. Eligible on trait fit, subject to ordinary quotation/provenance rules; this is not certification of every field.
- **Natural observations:** documented exposure–endpoint associations may remain with observational wording. Bare provenance or seasonal-timing observations cannot.

See [the assessment](../../tracks/progress/light-response-classification-224.md) for the representative replay, affected records, source-access limits and PR #45 coordination. Reassess legacy records through a new targeted audit/correction submission; never rewrite historical decisions or silently reinstate rejected evidence. No automatic migration, coverage/renderer change or validator enforcement is introduced. After integration, the next new unit should name this prompt and show a classified record or explain why none was relevant; document integration alone does not establish launcher adoption.
