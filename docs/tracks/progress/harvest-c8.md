# harvest-c8 progress

## 2026-10-27

**Current checkpoint:** 2/40 genera screened (Albizia, Ambrosia); 2 eye_type search records; 6 wanted lines; 0 evidence records; 0 cells closed by measurement. Thirty-eight genera remain, starting with Diospyros. Ambrosia’s diel, chemical and unmeasured-species light cells remain pending intake. Pilea is covered by the c4 worker under the coordinator; reuse its provenance when reached. The initial ci/OpenAlex access problems below were resolved. Current outside-service refusals are the desk-wide OpenAlex 429 (reported by coordinator), MDPI 429 and UChicago 403; skip those fetching routes. Next: Diospyros, Rubus, Baccharis, using current ci and available web/other sources. Stop here between genera for a fresh continuation.

The following dated subsections retain the actual attempts and earlier counts as history; the checkpoint above is current.

Dispatch `regards-issue-28-20261027`, issue #28. Read AGENTS.md, the authoritative harvest-c8 line in work/queue-lines.txt, the batch JSON, round4-harvest.md, THOROUGH.md, BRIEF.md Round 2, round3-sweep.md, desk-screen.md points 1–10 and audit 53/54 context. Scope is the 40 genera in the batch; the entry after Nuttallanthus is Melilotus.

Initial checkpoint: 0 of 40 genera completed; 0 evidence records; 0 cells closed by measurement; 0 complete-protocol search records; 0 wanted lines so far. Albizia started, all 40 remain incomplete. No full-protocol negative record is licensed by the work below.

### Initial Albizia work (subsequently completed)

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

### Initial access failures (ci and OpenAlex subsequently resolved)

- No local `refs/remotes/origin/ci` exists. `harvest_get.py` and `screen_candidates.py` call an automatic git fetch, so they were read rather than run while the parent’s no-fetch rule applies. Their actual current harvest candidate list has not been screened; a missing local ref is not a zero-hit result.
- The connected web tool refused all three explicit OpenAlex URLs as “not accessible via this tool”: `https://api.openalex.org/works?search=Albizia%20eye%20type&per-page=20`, `https://api.openalex.org/works?search=silk%20tree%20eye%20type&per-page=20`, and `https://api.openalex.org/works?search=Fabaceae%20photoreceptor%20review&per-page=20`. One repeated call confirmed the same failure, so this is an access block, not a completed OpenAlex step.
- Shell network proxy refusal/direct DNS failures were already established by the coordinating agent; no paid API or alternate unauthorized route used.

Initial next steps (subsequently completed): obtain the ci harvest snapshot through the coordinator; finish Albizia’s scientific/common-name and family-review OpenAlex steps through an accessible route; then proceed to Ambrosia, preserving the mandatory first germination searches. Do not promote this note into a search record without completing those steps. Screening writes no evidence. No builds, servers, Playwright, self-tests, gates or #29/#30 files changed.

### Access recovery and Ambrosia leads (same date)

The coordinator fetched `origin/ci` at `55a1f658a687c5d355ae11d9eec65def211f4033`. Explicit additional network permission restored `requests` access to OpenAlex. Re-ran `Albizia eye type`, `silk tree eye type`, and `Fabaceae photoreceptor review` against the required OpenAlex endpoint, each HTTP 200 with its first 20 results saved under work/harvest-c8/. Read all 60 titles and available abstracts. The common-name results are mostly silk biomaterials and silkworm history; the scientific results are medicinal chemistry and seed studies. No eye_type measurement is suggested. Opened the Fabaceae review Henriques and Benlloch 2026, DOI `10.1093/jxb/erag313`, through the connected web tool and checked for Albizia (no match); it reviews photoperiod signalling in crop legumes, not plant eyes. Shell fetching of the PMC page returned a reCAPTCHA despite HTTP 200; the connected tool exposed the review text. The initial access failures above are superseded for OpenAlex and ci availability, not for the initial failed calls themselves.

Started Ambrosia's mandatory first searches, word for word: `Ambrosia seed germination light dark`; `Ambrosia germination gibberellin OR smoke OR dormancy`; `Ambrosia jasmonate herbivore`. Read the available result titles/snippets. Added 2 wanted lines, checked absent from main's wanted/evidence/corrected stores and paper-status by DOI/title: Ruziev and colleagues 2020 on Ambrosia trifida light/dark germination (KCI abstract read, no evidence) and Šćepanović and colleagues 2022 on chemical germination treatments of A. artemisiifolia (PMC reCAPTCHA; MDPI HTTP 429). No further MDPI fetch after the 429. Author names for the latter verified via its exact DOI OpenAlex lookup, HTTP 200. A Frontiers article (`10.3389/fagro.2020.573860`) also opened at abstract/method context, but its A. artemisiifolia light-response trait is already on main; no duplicate or null record was added for it.

At that checkpoint, running the official harvest_get and screen_candidates scripts through a work-only wrapper that suppresses automatic fetch while using the coordinator's exact ci snapshot. At that checkpoint, counts were 0/40 pending that inspection and protocol completion, with 2 wanted, 0 search and 0 evidence. All 40 were then incomplete; Ambrosia still needs paired trait searches and citation/review step.

### Albizia completed

Official harvest_get returned “in no harvest run yet” across runs 1–24; screen_candidates returned “not in the harvest”. The first 20 results of each successful OpenAlex query (60 total) and all exposed web titles/snippets were screened. The coordinator confirmed that genuinely fewer exposed web results may be recorded with their actual extent; no claim of 20 web titles per query is made. One eye_type search record now preserves every successful query above and the owner’s plant-eye reading. Family review `10.1093/jxb/erag313` is the chased step. No eye_type evidence exists on main for Albizia. Counts now: 1 of 40 genera complete, 1 search record, 2 wanted lines (Ambrosia partial), 0 evidence and 0 measured closures. Thirty-nine genera remain; Ambrosia is next and already has its initial germination searches/leads. Pilea is being covered by c4 under the coordinator; reuse that provenance when reached.

### Ambrosia completed screening; measurements await intake

The official harvest snapshot contains run 5, supplement 12 (photoperiod and circadian searches), a family review in run 17 and 21 works citing `10.1371/journal.pone.0166510`. Screened all 105 unique titles and stored abstracts (the harvest caps abstracts at 700 characters). Direct OpenAlex calls made before the desk-wide 429 refusal returned 152 results: 20 each for scientific/common diel, eye and chemical pairs and the Asteraceae review; 8 scientific-name and 4 common-name light results. All returned titles and available abstracts were screened. OpenAlex is now skipped globally after the coordinator reported an actual 429 from another worker; no further call made after that notice.

Completed the remaining web pairs: `Ambrosia flower opening time anthesis`; `ragweed flower opening time anthesis`; `Ambrosia eye type`; `ragweed eye type`; `Ambrosia chemical sense volatile response`; `ragweed chemical sense volatile response`; `Ambrosia light photoperiod phototropism`; `ragweed light photoperiod phototropism`. These and the initial three web queries are copied word for word after every successful harvest query and direct API query in the eye_type search record. Genuine fewer-results responses are stated without claiming 20. No truncated title/abstract output was treated as a complete screen; omitted stretches were recovered in subsequent reads.

Added four further wanted lines after checking main/status for DOI/title duplicates: Bianchi and colleagues 1959 (publisher abstract states anther opening at 06:30–08:00; full text requires access), Hall and colleagues 2023 (SLU institutional abstract directly reports living ragweed root responses to exudates; full text awaits intake), Effects of Photoperiod on Sex Expression in Ambrosia trifida 1942 (harvest abstract; own publisher fetch 403, authors not shown so blank), and Schutte 2007 (institutional thesis metadata/abstract read; germination/dormancy title is a required candidate, actual light/chemical methods need reading). The latter is explicitly a candidate rather than a claimed light/chemical measurement. No further UChicago fetch after its 403. No further MDPI fetch after its 429. No sense_light_nonvisual null: main already measures A. artemisiifolia; A. trifida remains pending the wanted papers. No chemical or diel null while their candidates await intake.

Round totals: **2 of 40 genera screened**, **2 eye_type search records**, **6 wanted lines**, **0 evidence records**, **0 cells closed by measurement**. Albizia and Ambrosia screening protocols are complete; all wanted-derived measurements remain unclosed. Remaining 38 genera start with Diospyros and Rubus; Pilea is being covered by c4 and the coordinator will account for that provenance. Stop here between genera for a fresh continuation rather than abbreviate the next genus’s protocol. Next: start Diospyros with its mandatory germination searches, use the saved ci snapshot and web/other sources while the OpenAlex and MDPI refusals stand, then Rubus and Baccharis. The scratch harvest cache is work/harvest-c8/harvest-cache.pkl (105 Ambrosia works in its full-genus/family data); it is not a deliverable and is never committed.
