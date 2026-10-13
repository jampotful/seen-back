# Progress: audit (burst 5)

Started 13 October 2026, about 16:20 US Eastern. Branch `agent/audit` (it already held an earlier, unrelated audit of the accuracy numbers; this work is on top of it, with `main` merged in).

## Done and pushed
- `tools/lit/audit.py`: first pass (Haiku 5.5, Message Batches API, cached system prompt, script check of the reply and of the numbers against the quote), `adjudicate` (flagged records settled from the source passage in `pub/lit-t1` by Sonnet 5.5), `decisions` (writes `docs/views/audit/<unit>.jsonl`), `test`. Checked against a local mock of the API.
- `.github/workflows/lit-audit.yml`, `ci/lit/audit.sh`, `ci/lit/audit.env`.

## Next
1. A trial run on two units (push to `run/lit-audit/trial1`), read the verdicts by eye.
2. The full run over all 18 logs.
3. Adjudicate the flags, then write the decisions to `docs/views/audit/<unit>.jsonl`.
