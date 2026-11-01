# Reassessment of ecological intervention outcomes after audit 350

1 November 2026. Scientific inspection is pinned to main
`832884366160e258cbc7b3c30e61e807927b4e7d`; the implementation is stacked on
PR #49, `d5552710fb4cfca16dd02f85c9512d709168e67a`. This is a targeted reassessment
requested by the owner, not a random audit or a new estimate of historical error
rates. Historical audit reports and desk dispositions are unchanged.

## Decision and source reconciliation

`desk-d254:2` needs `correct` for trait/claim scope. File the measured finding as
`ecological_intervention_outcome` with `evidence_kind: ecological_outcome`; retain
`m` for the species-specific endpoint. A sensory explanation remains inferred.
The current note's assertion that this is an animal responding visually exceeds
the measurement. A prose caveat alone leaves the record eligible for sensory use.

The [publisher's Gautama et al. paper](https://www.frontiersin.org/journals/marine-science/articles/10.3389/fmars.2022.1036158/full)
was opened: abstract, Methods, Results, Tables 1–3 and Discussion. It reports
70 paired net deployments, green-turtle counts of 14 versus 6, and a 59.5% reduction
in mean CPUE with Wilcoxon p = 0.039. That percentage concerns effort-standardized
catch, not the raw-count percentage or the probability that an individual avoids
a light. The 500 nm peak describes the LEDs. Observers recorded catches, not
independent turtle visual responses. Illumination could act through pathways the
experiment did not distinguish. The Results text prints illuminated CPUE 0.07;
Table 3 prints 0.7. Both the numerical finding and the existing discrepancy
disclosure are retained. No raw-data reanalysis is claimed.

BRIEF defines `behaviour_vision` as behaviour showing what is seen. Audit 350's
explicit approval of a net comparison, despite its acknowledged mechanism limit,
does not meet that definition for a demonstrated visual response. Under
`oa-audit.md`'s scientific-context rule, this affects causal interpretation and
eligibility; count one corrected record, not one error per modified field.
Do not overwrite audit 350 or recalculate its historical pooled rate.

## Representative examination

Screened the 440 current-main evidence files and 20 corrected files for catch,
trap, deterrent, predation-risk and detection endpoints. The broad text search
returned 25 candidates, including incidental hits and historical copies; it is
triage, not a scientific census of accepted unique observations. The following
purposive comparisons separate source inspection from record-only findings.

| Accepted record(s) | Measurement and source access in this pass | Disposition |
|---|---|---|
| `desk-d254:2`, Chelonia | Publisher Methods, Results and catch tables read | Correct classification; preserve the ecological result. |
| `desk-d253:5–8`, fisher, wolf, moose, ground squirrel | [PLOS source](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0229055), Methods and Results read | Correct to ecological outcomes; retain the positive result and three nulls, all coefficients, uncertainty and qualifications. |
| `desk-d254:4`, white shark, Kempster 2016 (audit 350's pre-hold-out line 5) | [PLOS source](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0157717), deployment, video analysis, field calibration and Results read | Directly measured approaches/contacts under active/inactive equipment are behavioural evidence. Preserve the distinction between filmed distance and field strength estimated from a fitted calibration; no universal electrical threshold. No correction here. |
| `desk-d254:5`, Chaoborus (audit 350's original line 6) | [Nature abstract and opening Results](https://www.nature.com/articles/s41598-024-58406-y) read; subsequent Methods access failed | Another mechanism-limit concern: both larval distribution and fish attraction change. Queue targeted review of direct versus predator-mediated response; no new full-methods audit or mutation claimed. |
| `desk-d176:1`, Calanus | Accepted record read; publisher retrieval failed and PMC returned a challenge | Paired trap choice is not automatically invalid behavioural evidence; the record already discloses unequal intensity and cannot isolate polarization. Reopen the source before a new disposition. |
| `desk-d192:5–6`, Anoplophora | Accepted records read; MDPI returned 429 and PMC a challenge | Controlled chamber entry is a possible group behavioural endpoint. Do not apply a blanket field-catch rule. Preserve intensity/wavelength limits and nulls; no new source audit claimed. |
| `desk-d219:1`, Lymantria | Accepted record and publisher-deposited search/abstract information examined; full retrieval blocked | The record explicitly documents an owner precedent permitting lamp comparisons as behaviour. Reconcile field catches with the paper's separate laboratory assays before superseding it; no silent override. |
| `desk-d193:2`, Chelonia colour choice | Current accepted record inspected as an eligibility control, not independently re-audited | Remains eligible. Contact choice measures behaviour; its brightness and speed-null qualifications stay attached. This correction does not negate turtle vision. |

The camera-lure source models event counts over stations; equipment placement
uses fixed corners, and no matched empty-tube control is described. Counts combine
activity, local availability and detectability. They do not isolate olfactory
detection or its absence. The current notes already limit interpretation, but
`sense_chemical` still grants functional eligibility. The four proposed corrections
retain those findings under an endpoint-specific category. No mechanism is
declared false; the study simply does not resolve it. Audits 348 and 349 retain
their original decisions. Supplementary tables were not independently re-audited.

No blocked publisher was bypassed via a proxy, login or unauthorized copy. MDPI's
429 ended further direct requests there. A search excerpt was not treated as a
full source read. No article full text or PDF is committed.

## Implementation and demonstrated consequence

The [classification policy](../../views/research/ECOLOGICAL-OUTCOMES.md) distinguishes
behaviour, demonstrated stimulus response, ecological endpoint and inferred
mechanism. This extends #49's single `evidence_scope.py`; no parallel anatomical
ontology, new grade system or second scientific-review mechanism is introduced.

Five fingerprinted entries in `docs/views/ecological-use-limits.jsonl` restrict
the inspected original records in the gap, row and compiler loaders. Their
original numbers, source, quote, grade and method/conditions are unchanged.
`recheck-ecological-350.jsonl` supplies five complete corrections in the existing
`apply_audit.py` ledger format, with reversible field deltas, base commit and
prior-audit links. These are review proposals outside accepted evidence.
New outcome records require endpoint, experimental unit, treatment, comparator
and mechanism-limit fields. Neither the trait nor its kind can close a sensory
gap or carry automatically to relatives. A misfiled outcome cannot be relabelled
as `colour_vision`, `motion` or a receptor peak to regain eligibility.

An offline replay using the actual turtle record reproduced a concrete failure
on unmodified #49: its row validator accepted `You see green lights.`, and its
spec validator accepted a grade-`g` calculation taking 59.5/100 as `params.glow`
alongside that measured visual row. Both returned zero errors. With this patch,
the row and parameter are rejected for ecological scope. Mixed citation lists
cannot bypass the parameter safeguard. These are injected regression examples,
not claims about a generated or published turtle view.

| Replay | Before | After |
|---|---|---|
| Turtle record alone supporting `behaviour_vision` | `m` eligible | excluded; isolated sensory cell `i` |
| Refiled turtle outcome supporting its own endpoint | no separate category | `m`, with all original findings |
| Each of four camera-lure records alone supporting `sense_chemical` | `m` eligible | excluded; isolated sensory cell `i` |
| Outcome-only prose row with explicit outcome trait | no explicit scope route | retained, subject to ordinary voice/source review |
| Chelonia with its other accepted behavioural evidence | `m` support available | still `m`; `desk-d193:2` unchanged |
| Invented visual setting without a measured outcome claim | `i`, invented | remains permitted |

The combined raw-evidence replay checks current-main record identity and the
compiler loader. It does not recalculate published coverage: the complete
published gap cells and audit ledger were not fetched. No live view JSON, offered
flag, compiled draft, published gap output or build changed. Searching the current
view files found no direct Gautama DOI or desk-d254 citation; that is not a proof
against every indirect source path. No API generation or deployment was run.

## Validation

- 10 new offline regressions pass with `--corpus`: exact five-record identity,
  preserved findings/provenance, strict schema, original/refiled eligibility,
  raw/corrected loader paths, no carry, controlled behavioural/null retention,
  writer context, explicit outcome prose, compiler calculations/rows and existing
  audit application. The corpus mode fails if its current-main records are absent.
- #49's 15 scope tests pass; the existing test explicitly separates its original
  nine anatomy restrictions from the new ecological registry.
- Existing gap tests (5), compiler checks (0 failed), audit-application tests and
  quotation/append tests (4) pass. No full-corpus `test_rows.py` run is claimed;
  new tests directly exercise the changed row loader, input and draft checks.
- #50's eight actual-record compatibility tests also pass with
  `--require-classification` on its `ef1bac7` evidence/curve fixture. Those files
  were used only in the local integration snapshot; this PR does not include or
  scientifically admit them.
- Strict validation of the five proposed refiles: 5 records, 0 problems. Every
  quote, numerical value, method, condition and source object matches its original
  at the JSON level. The turtle note loses the unsupported visual-response filing
  assertion; new classification/provenance text is additive elsewhere.
- `oa_lint.py` reports four `partial` warnings both before and after. These are
  unchanged keyword matches in legacy provenance notes, not new numerical faults.
  Its broad pattern treats words such as citation/provenance references as evidence
  of secondary reporting. No linter or partial flag was weakened to hide them.
  Existing resource-close warnings were suppressed for concise test output.

## Research-desk handoff

1. Review this claim-scope extension with #49; the stacked PR should first target
   `codex/sensory-anatomy-292`, so it contains only this additional work. After #49
   integrates, rebase/retarget onto main. Retain its AEP/transduction compatibility
   with #50; this change neither edits nor admits those measurements.
2. Independently dispose of the five proposed corrections under the established
   scientific-context rules. Confirm the original fingerprints before applying;
   if a record changed since the pinned main, re-review it rather than matching a
   shifted line blindly. Review the listed unresolved comparators separately.
3. Use the existing command, once per unit, to materialize the correction for
   inspection, for example:

   ```sh
   python3 -I tools/views/apply_audit.py docs/views/evidence/desk-d254.jsonl \
     --all docs/views/recheck/recheck-ecological-350.jsonl \
     --out /tmp/desk-d254.ecological.jsonl
   ```

   Repeat for `desk-d253`. This produces `audit.was` and keeps all other records.
   Integrate the reviewed replacements through the desk's normal process, making
   sure both raw-log and corrected-log consumers see the refile or use restriction.
   A corrected copy alone is insufficient for `gaps.py`, which reads raw logs.
   Do not append the refiles as independent replications or retract valid outcomes.
4. Run `python3 -I -W ignore::ResourceWarning tools/senses/test_ecological_outcomes.py --corpus`
   on the combined integration tree. Update the desk-owned disposition/yield log
   after acceptance. Research acceptance and app-main integration are still pending;
   this submission does not impersonate either role or change the launch queue.
