# harvest-c8 progress

## 2026-10-27

Dispatch `regards-issue-28-20261027`, issue #28. Read AGENTS.md, the authoritative harvest-c8 line in work/queue-lines.txt, the batch JSON, round4-harvest.md, THOROUGH.md, BRIEF.md Round 2, round3-sweep.md, desk-screen.md points 1–10 and audit 53/54 context. Scope is the 40 genera in the batch; the entry after Nuttallanthus is Melilotus.

This round: 0 of 40 genera completed; 0 evidence records; 0 cells closed by measurement; 0 complete-protocol search records; 0 wanted lines so far. Albizia started, all 40 remain incomplete. No full-protocol negative record is licensed by the work below.

### Albizia partial work

The current queue lists only `Albizia julibrissin` / `eye_type` as open. Checked canon.jsonl: its eye_type compilations concern Metazoa (Animal eyes, in hand, plus the other animal compilations); the owner’s plant eye_type reading of 25 October applies. The required plant germination searches also returned leads for light and chemical response, but those traits are already covered for this genus and no duplicate wanted lines were added.

Connected web searches run, word for word, in order:

- `Albizia seed germination light dark`
- `Albizia germination gibberellin OR smoke OR dormancy`
- `Albizia floral scent volatiles`
- `Albizia eye type`
- `silk tree eye type`
- `Albizia epidermal lens cells eye type`
- `silk tree epidermal lens cells eye type`
- `Fabaceae photoreceptor review`

Read the returned titles/snippets only. The eye/lens results include epidermal anatomy and seed water-gap “lens” work, plus general plant-optics reviews; none supports an eye_type measurement under the owner’s reading. No source page was fetched and no evidence or negative record was written. Some paired searches yielded fewer than 20 results in the connected tool; no claim is made to have screened 20 where the tool did not expose 20. No unauthorized host was opened (the family-review results included a publisher mirror at legcat.gov.ns.ca, which was left unopened).

### Concrete access failures

- No local `refs/remotes/origin/ci` exists. `harvest_get.py` and `screen_candidates.py` call an automatic git fetch, so they were read rather than run while the parent’s no-fetch rule applies. Their actual current harvest candidate list has not been screened; a missing local ref is not a zero-hit result.
- The connected web tool refused all three explicit OpenAlex URLs as “not accessible via this tool”: `https://api.openalex.org/works?search=Albizia%20eye%20type&per-page=20`, `https://api.openalex.org/works?search=silk%20tree%20eye%20type&per-page=20`, and `https://api.openalex.org/works?search=Fabaceae%20photoreceptor%20review&per-page=20`. One repeated call confirmed the same failure, so this is an access block, not a completed OpenAlex step.
- Shell network proxy refusal/direct DNS failures were already established by the coordinating agent; no paid API or alternate unauthorized route used.

Next: obtain the ci harvest snapshot through the coordinator; finish Albizia’s scientific/common-name and family-review OpenAlex steps through an accessible route; then proceed to Ambrosia, preserving the mandatory first germination searches. Do not promote this note into a search record without completing those steps. Screening writes no evidence. No builds, servers, Playwright, self-tests, gates or #29/#30 files changed.
