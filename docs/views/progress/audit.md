# Progress: audit (burst 5)

Started 13 October 2026, about 16:20 US Eastern. Branch `agent/audit` (it already held an earlier, unrelated audit of the accuracy numbers; this work is on top of it, with `main` merged in).

## Done and pushed
- `tools/lit/audit.py`: first pass (Haiku 5.5, Message Batches API, cached system prompt, script check of the reply and of the numbers against the quote), `adjudicate` (flagged records settled from the source passage in `pub/lit-t1` by Sonnet 5.5), `decisions` (writes `docs/views/audit/<unit>.jsonl`), `test`. Checked against a local mock of the API.
- `.github/workflows/lit-audit.yml`, `ci/lit/audit.sh`, `ci/lit/audit.env`.

## Trial 2 (jumper and herps, 120 records): 85% flagged by the first prompt, too strict; prompt loosened, "unverifiable" verdict added, second pass sends worst flags first up to its cap.

## Full run (`run/lit-audit/full1`, ci run 3, finished 13 Oct about 22:15 UTC)
First pass: 4,166 records sent, 456 unseen (empty quote or book), $0.28; 3,223 flagged (77.4%), too many to be a useful list on its own because 1,831 of the flags are a grade suggestion (m to g) from a reviewer that sees only the quote. Second pass (Sonnet 5.5, $6.60): 3,223 flagged, 1,077 settled (310 confirm, 748 correct, 19 retract), 556 left out by the spend cap, 633 with no source text in the collection, and 935 lost to a script bug (the verdict "unverifiable" was rejected; fixed in the commit after this note, the 935 rows say "no usable verdict" in docs/views/audit/<unit>.jsonl).

Decisions are in `docs/views/audit/<unit>.jsonl`. Results: `ci` branch `runs/lit-audit/3/`, and `pub/lit-audit`.

## Next
1. Rerun the second pass on the 935 and the 556 (about $4 more; total spend so far about $7.3 of the $12), with `AUDIT_ADJ_MAX_USD` set to 4; needs an `--ids` option to select only rows whose verdict is "unchecked" for those two reasons.
2. A later step applies the 748 corrections (642 of them change the grade, 530 of those m to g, 249 of the settled records are lambda_max_nm).
