# Sensory anatomy classification after audit 292

31 October 2026. Implementation on `codex/sensory-anatomy-292`, based on main
`785f8504a8e78fb0e5caac6365ebc29e7dacb3bd`, for research-desk review and application.
This is a classification/implementation report, not an independent numbered audit.

## Decision and delivered change

Keep measured anatomy in `sensory_anatomy`, using `structure`, `measurement` and
`evidence_kind`. Taxonomic grade is independent of claim type. Anatomical presence,
counts, passive mechanical response and inferred function cannot establish a
sensory detection capability. Transduction, other physiological responses and
behaviour are distinguished, including nulls and method-specific limitations.
The alternatives and full policy are in
[SENSORY-ANATOMY.md](../../views/research/SENSORY-ANATOMY.md).

The code enforces the distinction in new-record validation and in gap, row and
spec compilation. New functional records need an evidence kind when appended;
the strict checker option also covers directly written logs. Nine legacy findings
receive conservative use restrictions, matched by a fingerprint of taxon, trait,
value, units, method, conditions, quote and DOI. Their scientific fields and
existing audit judgements are preserved. Untyped legacy evidence outside this
inspected set retains its existing behaviour pending migration.

## What was inspected

Read AGENTS, HANDOFF, CONTRACTS, STATUS, LOG, BRIEF, audit 292, desk-d208, the
scientific-context rules and dispatcher review procedure. Inspected the complete
corrected bee, insect, spider, fish-shark and ground-invertebrate logs for relevant
organ terms, and the evidence checker, gap loader/carry logic, row loader/writer,
spec compiler and checker, PARAMS glossary, engine documentation and representative
live/draft view specs. The local checkout is a connector-fetched snapshot of the
relevant files, not a full clone or a complete corpus audit.

Representative records below identify the corrected copy's filename and physical
line. Presence in those files does not mean every audit question is settled:
`unverifiable` and `flagged_unchecked` entries are identified explicitly. No
functional finding below was upgraded or newly source-validated by this pass.

| Corrected record | Finding and distinction | Treatment |
|---|---|---|
| `bee:151`, Apis mellifera | Johnston-organ axonal recordings under electric-field stimulation, alongside conditioning/vibrometry; neural response rather than organ presence | Retain; function is specific to the tested stimulus. Does not license a function for Megaphragma |
| `bee:221`, Apis mellifera | Hearing review under a hearing key; existing flagged/unchecked status | Preserve review and audit status; not a new confirmation of its range |
| `insect:510`, Danaus plexippus | Hair-sensillum anatomy combined with ablation; anatomy and causal behavioural claims need their own support | Preserve; a mixed-study method is not enough to classify the selected count as a hearing range |
| `spider:30`, Cupiennius salei | Trichobothrial count plus passive mechanical tuning | Restrict functional use; retain all original figures pending separation |
| `spider:31`, Cupiennius salei | Hair deflection follows oscillating flow; existing unverifiable flag | Restrict functional use; mechanics is not transduction |
| `spider:33`, several web spiders | Secondary trichobothrial counts; existing unverifiable flag | Restrict functional use without resolving the old flag |
| `spider:36`, Cupiennius salei | Slit/lyriform-organ anatomy; existing flagged/unchecked support | Restrict functional use; retain counts and audit |
| `spider:37`, Cupiennius salei | Intracellular receptor/action potentials; record distinguishes patellar strain organ from metatarsal vibration receptor | Transduction-type evidence, with unresolved organ/source audit caveats; preserve |
| `fish-shark:47`, Hemiscyllium ocellatum | Ampullary pore distribution | Restrict functional use; anatomy cannot establish electric sensitivity |
| `fish-shark:50`, Aulonocara stuartgranti | Prey detection under light/dark and lateral-line-block conditions | Behavioural/causal evidence; preserve the tested conditions |
| `fish-shark:53`, Elasmobranchii | Microscopy identifies free neuromasts | Restrict functional use; structural identification alone |
| `fish-shark:161`, Rhinoptera bonasus | Tail lateral-line anatomy supports an explicitly stated hydrodynamic-antenna hypothesis | Restrict functional use; hypothesis remains a hypothesis |
| `fish-shark:181`, two holocephalans | Paired species means for ampullary-pore counts | Restrict functional use; preserve paired values until source-verified splitting |
| `fish-shark:182`, Holocephali | Groove anatomy mixed with general water-movement claims | Restrict functional use pending splitting/source review |
| `ground-invertebrates:75`, Eremobates pallipes | Pressure response with an air-particle-motion null | Preserve both outcomes; no blanket airflow ability or inability |
| `ground-invertebrates:165`, Ixodes scapularis | Single-sensillum responses to named chemicals | Physiological/transduction evidence specific to the tested substances; preserve |

Only the nine records marked “restrict” enter `sensory-use-limits.jsonl`.
This is a conservative consumption restriction based on what the existing
records claim, not a retraction, a replacement primary-source audit, or a blanket
declaration that all the other records are correct.

## Megaphragma disposition

`docs/views/evidence/anatomy-d208.jsonl` contains four proposed records:
Johnston's organ scolopidia count 19, its reported cell count 95, central-organ
scolopidia count 5, and its reported cell count 20. Each has a numeric value,
units, named structure, measurement identity and explicit anatomical evidence
kind. All four are `m` for the measured anatomy of M. viggianii. None is a hearing,
airflow, vibration, electrical or graviception record; no function is inferred
from another species. These are four quantities from one study, not four
independent experiments. Cells are not equivalent to neurons.

Source: Diakova AV, Makarova AA, Pang S, Xu CS, Hess H, Polilov AA (2022),
Scientific Reports 12(1):20172, [doi:10.1038/s41598-022-24390-4](https://www.nature.com/articles/s41598-022-24390-4).
The publisher article initially returned Results and figure captions, including
the separate organ arrangements and female measurements. Subsequent publisher
retrieval hit an identity redirect; PMC returned a browser check and Europe PMC
was inaccessible. The [primary PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/36424494/)
was opened successfully and supplies all four counts in one complete sentence.
The paper's licence is CC BY 4.0 as recorded in audit 292 and the initial publisher
copy. No paper full text or PDF is committed.

The record quotes use the exact primary-abstract sentence, one count per record.
The complete Methods and supplements were not recovered in this pass. The
single complete reconstruction and partly damaged comparison specimen context
is retained with explicit attribution to audit 292, whose FIB-SEM-method account
also agrees with the publisher's indexed passage. `access: abstract` and
`partial: true` deliberately preserve the current verification limit. These are
not newly asserted population averages or replicated estimates of a species-wide
constant. No extra sizes, allometric ratios or cell-type counts are refiled.

Original audit 292 and the desk-d208 disposition are byte-for-byte unchanged.
The old held line is not silently restored under hearing; the new file links
back to `desk-d208:5` and both historical documents. Independent desk review
remains the acceptance step.

## Presentation consequences

The engine has no model that converts scolopidium count to sensitivity. Its
sound, haptic and overlay choices are proxies and often intentionally invented.
An anatomy-only factual row is possible; a sensory depiction derived from it
must separately disclose the invented mapping and untested modality, at `i`.
The compiler now prevents anatomical numbers from supporting otherwise unmapped
measured/calculated engine parameters merely by matching their digits.

No live rows, view specs, builds, offered flags or published gap tables are
regenerated. The wasp's hearing/airflow/vibration gaps remain open in regression
tests. Source review still governs free-form wording: a mechanical checker
cannot verify every arbitrary sentence a model might write.

## Validation

- `python3 -I tools/senses/check.py --require-evidence-kind docs/views/evidence/anatomy-d208.jsonl`: four records, zero problems.
- `quotecheck.py` against the short scratch excerpt transcribed from the opened primary abstract: four verbatim matches, zero failed. This checks transcription, not an independent full-text audit.
- `oa_lint.py docs/views/evidence/anatomy-d208.jsonl`: four records, zero with faults.
- `test_evidence_scope.py`: 13 offline tests covering counts, identity, schema, genus/order exclusion, functional positive controls, legacy limits, both loaders, row citations and compiler settings.
- Existing `test_gaps.py`, `test_compile.py` and `test_quote_limit.py` pass. The quote-limit fixture now supplies its physiological evidence kind and copies the new helper; it also tests that addlog refuses an untyped new functional record without appending it.
- The full-corpus `test_rows.py` is not claimed: it requires the complete evidence/taxonomy corpus, absent from this scoped snapshot. New offline tests exercise the changed row loader and draft check directly. No API-funded generation, app build or browser test was needed for these evidence-pipeline changes.
- `git diff --check` passes. Historical records/audits and view JSON are unchanged.

## Open decisions and handoff

The classification rule and proposed treatment of the wasp counts are concrete
on this branch. Review and apply through the research desk; HANDOFF says only
the app thread merges main. Continue typing and separating legacy mixed records
as sources become available. Do not treat this first migration set as completion
of the whole evidence audit. Taxonomic-name maintenance from audit 292 is a
separate outstanding task; no name registry was invented or changed here.

The owner still decides whether anatomy-only evidence should have visible rows,
which explicitly speculative sensory views to offer, and how their visual or
haptic language should work. The scientific question of how these wasp organs
actually respond remains open to direct experiments.
## PR #50 compatibility follow-up (31 October 2026)

The eight candidate Mélotte 2018 audiograms in
[PR #50](https://github.com/jampotful/seen-back/pull/50) initially lacked
`evidence_kind`. Its follow-up adds `transduction` after checking the primary
Methods' neural AEP protocol against this ontology. The 107 thresholds, source
quotations, conditions, six proposed `m` grades and two identity-restricted `g`
grades remain unchanged. This is classification work, not independent audit.

Testing those records exposed lost scientific context in the writer inputs:
`rows.record_line` omitted conditions and notes and truncated methods/quotes;
`compile.record_line` truncated notes at 200 characters. The two modern-species
restrictions occur later in the notes. This branch now preserves full typed
sensory context (including source locator, curve and restrictions) and makes the
neural-versus-behavioural rule explicit. Untyped legacy serialization retains its
previous compact format. No eligibility, carry, audit disposition or app setting
is changed by this follow-up.

Two new scope regressions fail before and pass after the change (15 total).
The companion `test_melotte_2018.py --require-classification` in PR #50 passes all
eight actual-record checks on the combined tree: strict validation, exact
scientific-payload preservation, atomic append rejection, raw/corrected loading,
no identity upgrade or hearing carry, full writer context and retained
`not audited` status. Existing gap (5), quote/append (4), and compiler tests pass;
strict validation and numerical lint report eight records and zero problems.
Full-corpus row tests and API generation were not run in the scoped snapshot.

Merge/admission coordination: review the two compatibility commits together;
the research desk must still independently dispose of PR #50's eight records,
including both identity restrictions, before accepted-main integration. Raw-log
loaders are not an acceptance gate, and the compiler's `not audited` label does
not exclude a record. No historic audit, legacy aggregate, accepted evidence,
published gap output or representation was updated. Full context still needs
source review before generating any behavioural or species-specific claim.
