# Scientific preflight: reconcile before drafting

For each newly launched desk evidence/lead-reading or OA-reading unit after integration, read this with BRIEF and the launch's reading prompt. Record their paths and the checkout commit in the usual progress note. Keep the existing branch, source, quote, trait, grade and independent-audit rules. The additional allowed output is `docs/views/progress/<unit>-scientific-review.jsonl`. Do not interrupt running units, edit accepted evidence, repeat completed dispositions, or change the desk queue.

## One reconciliation per paper, reused across its records

Do this while reading, before choosing a headline quote. Reuse the same open source; do not commission another agent, repeat a literature search or transcribe every cell. Read all relevant results for the record's taxon and trait, including the surrounding paragraph, Methods, tables and captions. Whole-paper reading remains required where the launch already requires it.

1. **Access.** Record the DOI (or source URL), the exact sections/tables actually inspected, and anything unavailable or unreadable with its reason. An open PDF URL or a summariser's assurance is not proof that its tables were inspected. Inspect a readable table with its headers and footnotes; if extraction loses columns, look at the source layout. Do not infer unread cells. Preserve inaccessible material as a limitation, never as a null finding.
2. **Design.** Identify taxon/form/cultivar, control, doses and units, treatment combinations, temperatures/light, pretreatment, duration, sampling endpoint and replication where given. Distinguish crossed factors from treatments confounded together; compare like endpoints against the corresponding control. Do not transfer a pooled result to one species/form without qualification.
3. **Metrics.** Define each claimed endpoint and which direction means what from the Methods/formula, not its name. Percentage, onset, mean time, T50, energy and uniformity are different outcomes. A variance-based uniformity index decreases as synchrony increases. Retain denominators/time windows and unit discrepancies; do not silently repair the paper.
4. **Results.** Record compact locator/finding pairs for the relevant comparisons. Check means against significance tests, the exact table column and letter-group footnote; overlapping letters do not establish a significant difference. Distinguish a numerical trend, a reported significant effect, a non-significant comparison, and no reported test. Preserve nulls, reductions, dose reversals and interactions that qualify a claim, including combined treatments and control comparisons. Do not infer a test or causal mechanism absent from the source.
5. **Reconciliation.** Compare the whole accessible abstract/conclusion with those results. Explicitly reconcile disagreements, translations, and pooled versus subgroup findings. Keep both locators when unresolved; narrow the claim or hold it rather than choosing the convenient statement. A statement of no effect on final percentage cannot cover speed or uniformity. Cover scientifically consequential qualifiers even when the chosen quote omits them. Unrelated outcomes need not be copied; explain borderline scope exclusions briefly.
6. **Final record check.** Reread `value`, `method`, `conditions` and `note` together against the reconciliation. Put necessary qualifiers in the evidence itself, not just this review. Retain the original provenance and quote rules; put extra result support/locators in conditions or note, or split records as the reading prompt requires. Do not lengthen or rewrite a quote to conceal an omission. Recheck after any edit.

## A small, inspectable receipt

After drafting, generate the skeleton (redirect to a new file; do not overwrite a completed review):

```sh
python3 -I tools/views/scientific_preflight.py candidates.jsonl --template > review.jsonl
```

One JSON object per paper, with these fields:

| Field | Required content |
|---|---|
| `source` | The candidate's DOI, or URL if it has no DOI (generated). |
| `access.kind` | `full_text`, `abstract_only`, or `incomplete` (e.g. text read but a relevant table unreadable). This describes what was inspected, not whether the journal is OA. |
| `access.inspected` | Nonempty list of exact sections/tables/captions and retrieval route actually inspected. |
| `access.unavailable` | List of missing material and reasons; empty only when no relevant access gap remains. |
| `design`, `metrics` | Concise paper-specific notes from steps 2–3, or what the accessible text does not report. |
| `results` | Nonempty list of `{"where": "Table/section", "finding": "comparison and statistical status"}`. Group comparisons when that preserves direction, conditions and exceptions. |
| `reconciliation` | Conflicts/qualifiers and how the final wording handles them, or a specific statement of which passages agree. |
| `records` | Generated physical `line` and canonical JSON `sha256`; add `decision`, `claim_check`, and (for `limited`) `limitation`. |

Decisions: `ready` means this author completed the reconciliation, not independently verified science. `limited` means a narrower claim is supported by the accessible material: explain exactly what remains unverified in `limitation` and copy that text into the record's `note` or `conditions`. Abstract-only records retain `source.access: abstract` and `partial: true`. For incomplete full text, retain the reading prompt's partial rules (including review/figure provenance); the `partial` flag is not a substitute for explaining a missing table. `hold` means the claim cannot safely be submitted; remove it from the submission set, retain the lead/reason in the usual progress note, and regenerate/check receipts for the actual set. Never downgrade access simply to avoid reconciling a known conflict.

Run on the final submission file (after addlog if addlog supplies fields):

```sh
python3 -I tools/senses/check.py candidates.jsonl
python3 -I tools/views/scientific_preflight.py candidates.jsonl --review review.jsonl
```

Keep running `quotecheck.py` against each paper's own source text and its record subset as required by the existing reading prompt. If source text needed for quote verification cannot be obtained, record that gap and hold the candidate; a summary/yes-no answer is not a successful `quotecheck.py` run. A restricted but directly inspected abstract can support a limited record when existing quote checks pass. Do not bypass retrieval restrictions.

The preflight fails missing/stale/duplicate receipts, held records, incomplete documentation and access-status inconsistencies. It does **not** read papers, interpret statistics, detect false assurances or certify that a claimed reconciliation is correct. Do not copy hashes onto stale reasoning: regenerate after changes and reread the changed claims. Keep the normal independent audit and its counting rules. Commit the review alongside the unit's progress/evidence and report all check outcomes separately.

## Keep the cost bounded

Use short notes once per paper, not a second manuscript or a second audit. Two traits from one paper share design, definitions and source inspection; each still gets a final claim check. Reuse source text and fetches. A difficult unresolved definition, translation or table goes to a narrow hold for normal independent judgment, not repeated speculative requests. In the first three fresh units, add review minutes (or `not measured`), extra source calls and resulting holds to the progress note. Compare with that unit's total reading cost; do not claim efficiency or prevention rates from checklist completion alone.
