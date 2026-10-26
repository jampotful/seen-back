# Codex findings pass (report only; written 26 October 2026)

Used when `codex_queue.py` prints "Nothing to do", and added to the end of every round whose items finished with room to spare. You report problems; the research desk (a Claude session) checks each one against its source and makes the fix, because rounds whose own records were edited in place failed audit before. Change no file except the one below.

1. Work on the round's branch. Add or extend `docs/tracks/codex-findings/<YYYY-MM-DD>.jsonl`: one JSON line per problem.
   `{"n": 1, "file": "path", "where": "line number, record id or key", "kind": "value | source | grade | quote | duplicate | filing | taxonomy | link | format | tooling | docs | other", "problem": "what is wrong, in one or two sentences", "evidence": "the quote, link, rule (cite the doc and line) or the other record that shows it", "fix": "the right state, if you know it", "confidence": "high | medium | low"}`
2. Start with everything you have noticed or suggested in earlier chats about this repository, then sweep: `docs/views/evidence/*.jsonl` (values that do not match their quotes, wrong grades, wrong species or genus, duplicates, missing sources), `docs/views/wanted/*.jsonl` (wrong authors, years or titles; works that cannot serve the cell they name), `docs/views/searched/*.jsonl`, `docs/views/gaps/` (genera filed under the wrong family, kingdom or view; genus synonyms and splits), `docs/tracks/` (contradictory or stale instructions), `tools/` and `ci/` (bugs, broken assumptions, failing workflows). Skip a file a previous findings file already covers unless it changed.
3. Low confidence is fine; mark it. Never type a DOI, author or year from memory.
4. Finish with a line `{"n": "end", "covered": [...], "not covered": [...]}`.
