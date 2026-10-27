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

### Cnidoscolus checkpoint

Added Cnidoscolus: 1 eye_type search record and 4 wanted lines (three germination/seed studies retained under point 10(e), and a publisher snippet reporting within-night anthesis in C. urens). This round now has 4 genera screened, 5 search records covering 8 queued cells, 28 wanted lines, and 0 measurements. Nine OpenAlex queries and eleven web searches completed. Family-review alternative: 10.3389/fpls.2022.1015114. Required gate printed `0 problems`. Remaining: 36 genera beginning Magnolia.

### Magnolia and final context checkpoint

Added Magnolia: 1 eye_type search record and 12 wanted lines, bringing this context chunk to **5 genera screened, 6 search records covering 9 queued cells, 40 wanted lines, and 0 cells closed by measurement**. Its main sense_chemical evidence (sweep-33:4) is preserved. The light and diel cells stay out of the null record because germination/light trials and named anthesis observations need reading. Ten distinct web queries completed; the first three were repeated once to recover output truncated by the tool display. All executed query wordings are in the eye_type record. The family-review alternative was The floral biology of the Magnoliaceae, at the USDA author-paper address in the record. No paper was fetched or logged.

The desk reported an actual OpenAlex HTTP 429 from another unit while this unit was finishing Cnidoscolus; under codex-round step 3/service-refusal guidance, Magnolia and all subsequent work must skip OpenAlex for the rest of this dispatch. No OpenAlex request was made for Magnolia, and no unrun API query is represented as completed. The first four genera completed their direct OpenAlex queries before this notice.

Stopping between genera for a fresh context after Magnolia. **35 genera remain**, beginning Sabal, Smilax, Erythrina, Ruellia, Salvia, Stachys, Rhus, Pontederia, Phytolacca, Sambucus, Oxalis, Phyla, Toxicodendron, Youngia, Trifolium, Broussonetia, Passiflora, Urena, Campsis, Verbesina, Triadica, Quercus, Saururus, Cirsium, Ilex, Gaillardia, Serenoa, Acer, Monarda, Nekemias, Taxodium, Mitchella, Euphorbia, Eupatorium, Juniperus. Preserve globally covered traits: Nekemias already has replant-1 diel/eye_type/sense_light_nonvisual screening; multiple later genera have corrected-first main evidence (the evidence scan is available in work-session output and can be rerun without networking). The direct Sabal palmetto volatile lead 10.3390/plants12112164 appeared incidentally during the Callicarpa OpenAlex chemical search; Sabal main already has sense_chemical and diel evidence, so inspect current open traits before spending searches. Required final gate printed `0 problems` before the final context checkpoint commit.

## 2026-10-27 worker10 continuation

Sabal completed: this worker 1 genus, 1 eye_type search record, 6 wanted lines, 0 measurements; cumulative 6 genera, 7 search records, 46 wanted lines, 0 measurements. Existing Sabal diel/chemical evidence preserved. Germination studies (including a Sabal hians light lead) and a canopy-light leaf study keep sense_light_nonvisual out of a null record. No source pages fetched or evidence logged.

Ran harvest_get.py and screen_candidates.py: Sabal absent from runs 1–17,20,23,24. Checked canon catalog, accepted-name-aware corrected-first evidence, global wanted/search records and papers-status. All eight distinct executed web queries are copied in the eye_type record; family review alternative is Pollination systems of palms (Arecaceae), journal URL in record. The family-review and light/eye searches were repeated once after truncated display; returned titles/snippets screened, with no claims of full-text access. OpenAlex skipped for the whole continuation under shared HTTP429 notice; MDPI fetching skipped too. 34 genera remain, beginning Smilax.
