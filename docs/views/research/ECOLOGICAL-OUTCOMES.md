# Ecological intervention outcomes and sensory claims

Proposed 1 November 2026 after the owner's reassessment request for audit 350.
This extends [PR #49](https://github.com/jampotful/seen-back/pull/49)'s claim-scope
machinery; it does not replace its anatomical classification or acceptance rules.
Research-desk review and disposition precede accepted-main integration.

## Classification

`behaviour_vision` means a behaviour showing what is seen, as BRIEF specifies.
A measured outcome of equipment containing a light does not automatically satisfy
that definition. Grade, endpoint, modality, mechanism and source completeness are
separate questions. Statistical significance tests an endpoint comparison, not
all explanations of that comparison.

| Evidence | Appropriate scope | Limit |
|---|---|---|
| Directly measured approach, orientation, contact, choice or behavioural null in a specified stimulus comparison | `behavioural_response` under the appropriate existing trait | Claim only the tested response and controls. A device experiment need not identify a receptor to measure behaviour. |
| Behaviour demonstrating stimulus discrimination or detection with controls adequate for that particular claim | Existing sensory trait plus `behavioural_response` | Response to light alone does not establish colour discrimination, a receptor peak or a detection threshold. |
| Catch, camera-event rate, occupancy, survival or abundance under an intervention, without a resolved sensory response | `ecological_intervention_outcome`, `evidence_kind: ecological_outcome` | Preserve the endpoint; do not substitute avoidance, attraction, detection or a sensory absence. |
| An author's proposed sensory explanation for that outcome | Separately attributed `inferred_function` if worth recording | Does not gain measured status from the intervention's p-value. Do not label the measured outcome itself an inference. |

These are distinctions between claims, not ranks of scientific value. Behaviour
can be measured in a controlled group assay. Neither individual tracking nor
identification of the receptor is mandatory for every behavioural finding.
Conversely, tracking an individual does not by itself isolate a sensory modality.
Assess the exposure, measured endpoint and alternative pathways relevant to the
specific claim. No keyword classifier makes these scientific decisions.

A trap experiment may measure a controlled spatial choice, a field catch outcome,
or both. If a paper also contains a direct behavioural assay, split the claims:
that assay does not retroactively turn all field catches into measured behaviour.
Lamp peaks describe the apparatus; they are not animal sensitivity peaks. A null
intervention result is retained but cannot establish that a sense is absent.

## Filing and preservation

Use the new trait only when no established sensory trait describes the measured
endpoint without a mechanistic substitution. Required fields in addition to the
usual provenance are `measured_endpoint`, `experimental_unit`, `intervention`,
`comparator`, `mechanism_limit`, `method`, `conditions` and `units`.
The kind is `ecological_outcome`. Keep counts, effort denominators, effect estimates,
nulls and uncertainty in the existing value/conditions fields. Preserve the source
locator and quote. A correctly measured species endpoint can retain `m`; a genus
mixture does not become species evidence. `partial` retains its source-access role.

For historical corrections use the existing audit ledger and `apply_audit.py`;
the accompanying proposal is `docs/views/recheck/recheck-ecological-350.jsonl`.
It carries complete `corrected_record` objects, original field deltas, fingerprints,
the inspected main commit and historical audit links. Never append these as new
independent observations. The raw records and historical decisions remain intact.
The current proposal changes classification, not the numerical finding.

Before the desk applies the refile, the separate `ecological-use-limits.jsonl`
registry restricts the exact original scientific content through #49's loaders.
It changes no original field; the loaded record gains a reason and scope marker.
Changed content does not silently inherit a prior decision. Matching is by
scientific-content fingerprint, so identical raw/corrected copies are covered.
This branch's restriction is a conservative safeguard, not a claim that the desk
has already accepted the new classification.

## Evidence and representation eligibility

- An outcome cannot close a sensory trait cell, even if misfiled under another
  vision key or combined with unrelated evidence. An explicitly queried outcome
  cell can be `m` for its own measured species; it has no automatic genus/order
  carry and does not settle every possible intervention on that species.
- The row writer retains full methods, conditions, notes, source locator and
  outcome scope for both restricted legacy records and refiles. An outcome may
  support a row explicitly typed solely to `ecological_intervention_outcome`.
  The reviewer still verifies the endpoint and wording; metadata cannot prove
  arbitrary generated prose true.
- The spec compiler cannot turn an outcome number into a measured/calculated
  sensory parameter, including through a mixed citation list. Its generic rows
  lack endpoint typing, so outcome citations must use the explicit outcome-row
  route and review instead. Background evidence remains available.
- A representation inspired by an unresolved mechanism is an invention (`i`,
  `invented: true`), with the ecological finding and proposed sensory explanation
  stated separately. No catch reduction may become an avoidance probability,
  sensory gain, wavelength sensitivity or calibration constant.

Do not remove other valid behavioural records merely because they concern the
same species, apparatus category or sensory modality. The present inspection is
purposive and does not estimate the corpus-wide prevalence of misclassification.

## Choices considered

Retaining the old trait with prose alone leaves sensory eligibility unchanged.
Adding only `inferred_function` loses the distinction between measured outcome
and inferred mechanism. Deleting the record discards valid ecological evidence.
The proposed solution therefore combines a separately classified outcome with
enforced claim limits and reversible audit provenance.
