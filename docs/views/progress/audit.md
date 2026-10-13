# Progress: audit (burst 5)

Started 13 October 2026, about 16:20 US Eastern. Branch `agent/audit` (it already held an earlier, unrelated audit of the accuracy numbers; this work is on top of it, with `main` merged in).

## Done and pushed
- `tools/lit/audit.py`: first pass (Haiku 5.5, Message Batches API, cached system prompt, script check of the reply and of the numbers against the quote), `adjudicate` (flagged records settled from the source passage in `pub/lit-t1` by Sonnet 5.5), `decisions` (writes `docs/views/audit/<unit>.jsonl`), `test`. Checked against a local mock of the API.
- `.github/workflows/lit-audit.yml`, `ci/lit/audit.sh`, `ci/lit/audit.env`.

## Trial 2 (jumper and herps, 120 records): 85% flagged by the first prompt, too strict; prompt loosened, "unverifiable" verdict added, second pass sends worst flags first up to its cap.

## Full run (started 13 Oct 21:44 UTC)
Push `run/lit-audit/full1` (settings in `ci/lit/audit.env`: all units, first pass cap $2, second pass cap $8, wait 150 min). The first-pass batch of trial 2 (120 requests) took 36 minutes to finish, the second pass 6 minutes, so the full run was still waiting at the time limit. When the job finishes, the results are on `ci` under `runs/lit-audit/<run number>/` (SUMMARY-first.md, SUMMARY-second.md, verdicts.jsonl, flagged.jsonl, adjudicated.jsonl, unseen.jsonl) and on `pub/lit-audit`.

## Next
1. Read SUMMARY-first.md from the finished run; check the share flagged (trial 2 flagged 85% with the first prompt, which was too strict; the full run uses the looser prompt).
2. `python3 -I tools/lit/audit.py decisions --out <dir with adjudicated.jsonl> --dest docs/views/audit` writes `docs/views/audit/<unit>.jsonl`; commit it on `agent/audit`.
3. If the first prompt's trial-2 pattern repeats (grade 'g' that should be 'm' on original studies, composite values the quote supports only in part), the decisions file carries the corrections.

Trial 2 spend $0.39 ($0.02 first pass, $0.37 second pass).
