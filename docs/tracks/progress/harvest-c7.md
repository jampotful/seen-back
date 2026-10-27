# harvest-c7

## 2026-10-27

Dispatch `regards-issue-28-20261027`, issue #28, branch `codex/round-2026-10-27-issue-28`, starting main `96225855ff44ad1bdb15cc365314b3b4e06cb284` (parent fetched and created the shared branch).

Screened under round4-harvest and desk-screen points 1–10, including the owner's plant cue, applied hormone, germination and epidermal focusing readings. No evidence written and no source pages fetched. Wanted leads await the oa reader.

Progress this round: 2 genera screened (Bidens, Callicarpa), 3 search records, 19 wanted lines, 0 cells closed by measurement. Bidens eye_type and Callicarpa eye_type/diel have search records; the light and chemical traits for both genera, and Bidens diel, stay out because candidates need reading. Five queued species/trait cells are covered by these genus search records. Callicarpa has four germination/culture leads; Bidens has fifteen leads, including the queue's B. alba and B. cernua light/GA work, floral emission, and within-day anthesis.

Both genera are absent from harvest runs 1–17,20,23,24. Ran the full scientific/common-name OpenAlex pairs (20 works requested per query), the appropriate family photoreceptor review, desk-screen's paired trait web searches, and its three first germination/scent searches. Bidens also had two preliminary eye-type wordings before the focused epidermal-cell pair. Exact successful queries are in each search record. Canon catalog and corrected-first evidence stores were checked; neither genus has existing evidence. Family review titles/abstracts used as the review alternative: 10.3390/plants7040111 (Asteraceae), 10.3389/fpls.2024.1370810 (Lamiaceae).

Initial default-sandbox harvest and OpenAlex attempts failed; direct requests with explicit network access then succeeded after the parent fetched origin/ci `55a1f658a687c5d355ae11d9eec65def211f4033`. Those failures are not counted as completed searches. OpenAlex snapshots and scripts are scratch in work/harvest-c7, not public full texts. Search results were screened from their titles and available abstracts/snippets; no source was treated as read in full.

Remaining: 38 genera, beginning Parthenocissus, in batch order. Required screening gate: `screen_candidates.py --check docs/views/searched/harvest-c7.jsonl --wanted docs/views/wanted/harvest-c7.jsonl` printed `0 problems` before this checkpoint commit.

### Parthenocissus checkpoint

Added Parthenocissus: 1 eye_type search record and 5 wanted lines, bringing this round to 3 genera screened, 4 search records, 24 wanted lines, and 0 measurements. Its light, chemical and diel traits await candidates, including a direct phototropism experiment and a Virginia-creeper volatile table. Parthenocissus is absent from the same harvest runs and has no accepted-name-aware main evidence. Nine OpenAlex queries and eleven web searches completed; the Vitaceae family-review alternative was 10.3390/horticulturae5020041. Required gate printed `0 problems`. Seven queued cells are covered by search records. Remaining: 37 genera beginning Cnidoscolus. Global coverage scan preserves the existing replant-1 diel, eye_type and sense_light_nonvisual records for Nekemias and existing evidence for later genera.
