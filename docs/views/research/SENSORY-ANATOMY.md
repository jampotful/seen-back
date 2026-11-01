# Sensory anatomy and demonstrated function

Classification rule proposed and implemented on `codex/sensory-anatomy-292`,
31 October 2026, in response to the owner's instruction after audit 292.
Code and instructions integrate separately from candidate evidence. The four
proposed anatomy records remain subject to independent research-desk disposition;
their copies under `tools/senses/fixtures/` are regression inputs only.

## Decision

Retain experimentally observed sensory anatomy. Use `sensory_anatomy` when no
existing anatomical trait fits. Name the structure and the particular measurement;
do not create a hearing or airflow record merely because that structure serves
that function in another species. Existing precise anatomical keys such as
`eyes_count`, `eye_type` and `rhabdom_um` remain appropriate.

Trait, evidence kind, taxonomic grade and source completeness answer different
questions. `m` can describe a directly counted structure without establishing any
particular sensory function. `g` and `i` do not turn an anatomical count into a
measured sensitivity. `partial` still reports limitations of source access or
secondary reporting. Neither small sample size nor an untested function makes a
correctly measured anatomical count an invented number.

| `evidence_kind` | What the observation establishes | What it does not establish by itself |
|---|---|---|
| `anatomical_presence` | A named structure is observed in the sampled animal, stage and body location | Response to any specified stimulus; absence in unexamined tissues |
| `anatomical_measurement` | A count, dimension, arrangement or other structural measurement | Threshold, tuning, acuity or relative sensory performance |
| `mechanical_response` | Physical displacement or deformation under a specified stimulus | Neural transduction, stimulus detection or behaviour |
| `transduction` | A measured receptor potential, neural response or other experimentally demonstrated conversion of the stimulus into a biological signal | Behavioural detection, ecological use or subjective experience |
| `physiological_response` | A measured physiological or developmental response to the specified stimulus | A particular receptor or molecular transduction mechanism; behavioural detection |
| `behavioural_response` | The tested organism's response, discrimination or null under stated controls | The receptor responsible without causal evidence; unrestricted ability or inability |
| `inferred_function` | An explicitly attributed functional hypothesis or model | Experimentally demonstrated detection |
| `ecological_outcome` | A measured ecological or survey endpoint under an intervention | A particular sensory response or mechanism; see [ECOLOGICAL-OUTCOMES.md](ECOLOGICAL-OUTCOMES.md) |

These are claim types, not a ladder of quality. A behavioural experiment can
establish detection without identifying the receptor; anatomy can be measured
precisely without a functional experiment. Mere mechanical motion is kept separate
from biological transduction. Passive hair resonance is not a hearing audiogram.
An organ ablation plus a controlled response can support a causal role, subject to
the experiment's confounds; morphology alone cannot.

## Filing rules

- A `sensory_anatomy` record requires `evidence_kind` (`anatomical_presence` or
  `anatomical_measurement`), `structure`, `measurement`, `method` and `conditions`.
  Quantities require `units`. Use the existing scalar/string value format and one
  measurement per record. Keep stage, sex, organ location, sample limitations and
  which cells or units were counted explicit where available.
- Use functional `sense_*` keys for stimulus-specific physiological or behavioural
  findings. For legacy compatibility, `sense_airflow` includes water flow; identify
  the medium explicitly. Distinguish acoustic particle motion, pressure, steady
  air flow, substrate vibration and water displacement in conditions. A structure
  name cannot decide the modality.
- New functional records require `evidence_kind`; validate new logs with
  `check.py --require-evidence-kind`. `addlog.py` enforces it. Existing untyped
  records remain readable pending migration. Being untyped is not a positive
  scientific assertion that function was tested.
- A mechanical response may remain under its stimulus key with
  `evidence_kind: mechanical_response`, but it cannot settle a detection claim.
  An attributed prediction may use `inferred_function`, graded by the existing
  author-prediction (`g`) versus project-derivation (`i`) rule; it cannot settle a
  functional gap. Do not invent a prediction the source does not make.
- Split mixed claims before upgrading their use: anatomy, passive mechanics,
  neural response, other physiological response, behaviour and inference can be separate records from one
  paper. Do not carry an organ count into a tuning range, or one sensory modality
  into another, even for homologous organs. Counts do not automatically travel to
  congeners or higher taxa. A future anatomical row must name its structure and
  measurement; generic anatomy coverage does not settle every organ's anatomy.
- Preserve null results with the tested stimulus and protocol. No response under
  one protocol is not proof that a species lacks a sense. Anatomy with function
  untested is not evidence of functional absence.

## Fit to the presentation system

The current engine renders camera imagery and uses microphone/motion inputs,
sound-driven overlays and haptic patterns. `views/PARAMS.md` describes the bands,
weights and invented visual choices. There is no physical chordotonal-organ model
or parameter translating a scolopidium count into hearing or sensitivity.

An anatomical description can be a factual row at its own grade. A diagram or
effect may draw inspiration from receptor distribution or structure, but a
mapping from organ number to intensity, resolution, timing or stimulus modality
is a separate invention. Its parameter is `i`, `invented: true`; state the
anatomical basis and the untested functional assumption separately. This branch
does not invent or publish a wasp sensory effect. More scolopidia must not be
shown as better hearing without evidence for that relationship.

Implementation:

- `tools/senses/evidence_scope.py` centralizes evidence kinds, validation,
  functional eligibility and conservative legacy use restrictions.
- `gaps.py` excludes restricted records from species, genus and order functional
  support. It retains them in the evidence collection. Anatomy has no automatic
  carry even if a caller mistakenly assigns it a carry class.
- `rows.py` applies the same restrictions, passes evidence scope to the writer,
  and rejects restricted citations for functional rows.
- `compile.py` passes structure, measurement, method and scope to the writer and
  excludes these records from measured/calculated engine-parameter support.
  This closes the previous fallback that accepted any record for an unmapped
  parameter. Anatomy remains available as background and for factual rows.
- `sensory-use-limits.jsonl` restricts nine inspected legacy records by an exact
  scientific-content fingerprint. It changes no raw measurement, grade, quote,
  taxon or audit. It works across identical raw/corrected copies and does not
  silently follow a shifted line number. A changed finding needs renewed review.

The checks do not prove arbitrary generated prose true. Source review still has
to confirm that a row makes only the claim its cited record supports. No live
view, offered flag, compiled draft, published gap table or build is regenerated.

Typed sensory records also retain their full method, conditions, note and source
locator in writer inputs. A note can contain a complete response curve followed
by a taxonomic restriction; shortening it to an arbitrary character boundary
can remove the qualification. The row writer retains the complete normalized
quotation too. This preserves claim context, not scientific acceptance. Neural
thresholds must not be narrated as behavioural detection. These fields can make
requests longer; review request size when planning generation.

## Alternatives considered

| Alternative | Evaluation |
|---|---|
| Exclude anatomy entirely | Loses independently valuable measurements and possible grounds for an explicitly invented representation; inconsistent with existing anatomical vision traits |
| Add only `chordotonal_organs` | Accommodates this wasp but repeats the problem for sensilla, neuromasts and ampullary pores; a structure field is more general |
| Keep anatomy under `sense_hearing`/`sense_airflow` with a note | Taxonomic `m` can still close a functional gap or justify a numeric effect; notes alone are insufficient |
| Add only evidence-kind metadata to the old keys | Useful but leaves organ-only records implicitly associated with an untested modality |
| General anatomy trait plus evidence kind and consumer guards | Preserves the measurements, separates the claims, and fits the existing grade/invention system without asserting detection |

## Remaining decisions

Scientific work: review and split the remaining legacy mixed records, retain
their original audit flags, and type direct functional records with stimulus and
method specificity. The nine use limits are a conservative first set, not a
claim that every legacy record has been audited. A later migration may require
typed functional evidence everywhere; this change does not silently invalidate
all older functional records. It does not decide a numerical count-to-performance
law, cross-species anatomy transfer, or a blanket interpretation of nulls.

Artistic decisions: whether to display anatomy-only rows; whether an untested
modality should be available as an explicitly labelled speculative view; and
what visual or haptic language would express structure without implying sensory
performance. These can be decided without discarding the anatomical evidence.
