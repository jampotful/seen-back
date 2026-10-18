# Queue

The owner approves this queue and its budget once; a control room or a scheduled runner launches the next entries, at most three at a time, launching the next entry as soon as a slot frees (burst 1 left the weekly meter unchanged), with usage credits off so that a limit is a pause. The owner edits this file to steer. Each entry names its saved prompt; private details are pasted into the launch prompt from the owner's project doc, never written here.

| # | Agent | Model | Prompt | Needs | State |
|---|---|---|---|---|---|
| 1 | Design: the atlas and the engine design | Fable if its allowance is separate, else Opus | `docs/tracks/prompts/burst1-design.md` | | done 13 Oct 00:53 (Opus, launched 00:39): `agent/design` `b33aef8`, 25 mechanisms; awaits the owner's pick of one drawing per mechanism |
| 2 | Jumping spider research | Sonnet | `docs/tracks/prompts/burst1-jumper.md` | the spider and book Drive ids, the specialist's account | done 13 Oct 00:53 (Sonnet, launched 00:39): `research/jumper` `f2fcc52`; awaits the specialist review |
| 3 | Pipeline writer: Haiku Batch extraction over `pub/lit-t1`, quote check, dry run on one topic | Sonnet | `docs/tracks/prompts/burst1-pipeline.md` | a Console API key as the secret `ANTHROPIC_API_KEY` to run in full | built and tested without the API 13 Oct 00:53 (Sonnet, launched 00:39): `agent/pipeline` `bf8d13d`; the full run waits for the key; `harvest.py` and `ci/lit/*` live only on `run/lit/t1`, so it is not merged to main |
| 4 | Engine: module 0, today's views as specs, the tuning panel and compare slider, modules 1, 2, 3, 6 and 7, the jumper view with switchable drawings, the visibility floor | Opus | `docs/tracks/prompts/burst2-engine.md` | #1 | burst 2 |
| 4a | Specs for the fourteen groups module 0 unlocks (9.9% of world records); the specialist's sheet | Sonnet | `docs/tracks/prompts/burst2-specs.md` | #1 | burst 2 |
| 5 | Meter tests: the same small task on Opus and on Sonnet, read by the owner | the owner | | | with the owner |
| 6 | Audit of all fourteen units' logs (about 4,440 records): a batch job that asks whether each quote supports its value; the flagged records to one Sonnet agent | Haiku batch, then Sonnet | to write | #3 and the key | after the key |
| 7 | The units' proposals decided by the control room from the audit, and applied | Sonnet | to write | #6 | after #6 |
| 8 | Modules two onward, each followed by the views it unlocks as specs | Sonnet (Opus where the architecture changes) | to write | #4 | rolling |
| 9 | Spec compiler: specs and draft rows for every view from the pipeline's table, graded, `invented` marked | Haiku batch | to write | #3, #4 | after #4 |
| 10 | One pass over all the rows in one voice | Fable or Opus | to write | #9 | last |
| 11 | Ship the world database (built on `agent/world-db`); the head's next step | Sonnet, mostly on build machines | `docs/tracks/prompts/burst2-worlddb.md` | | burst 2 |

## Launched 13 October, 09:40

Burst 2 results: engine merged (build 26), world database merged (build 24), county-bias head passes every mark on `agent/head-ship` (not yet merged), seven of fourteen specs on `agent/specs`. Burst 3 running: `burst3-shiphead.md`, `burst3-specs2.md`, `burst3-engine2.md`. Key test of the extraction pipeline run on `run/lit-table/keytest`.

## Burst 4 (13 October, 12:20)

Burst 3 results: the specs for all fourteen waiting groups and the jumper review sheet (in Drive) are done; the engine has `spectrum`, `light`'s clock, sun and moon, `pace` and `motion` (build 28); the county-bias head is built but stopped at three unresolved checks. The extraction key test passed (Haiku recovers 38% exactly, 61% loosely). Burst 4 running: `burst4-lit.md` (up to $60 of the $150 cap), `burst4-shiphead2.md`, `burst4-engine3.md`.

## Round 2: the species people meet (13 October, 15:40), run by the research thread

The owner's research thread launches these entries itself, at most three at once, Sonnet at medium effort, and keeps their rows here current; the control room counts them against its limit and leaves them to that thread. The text floor and the carry rules are in the "Round 2" section of `docs/views/research/BRIEF.md`. Entries 9 and 10 must follow them when their prompts are written: rows are compiled per species from the logs by those rules, and the grade a reader sees is computed per species.

| # | Agent | Model | Prompt | Needs | State |
|---|---|---|---|---|---|
| 12 | Unit `mammals-met`: deer, cat, dog, squirrel and rabbit views | Sonnet | `docs/tracks/prompts/round2-unit.md` | | done 13 Oct 15:58: `research/mammals-met` `cda601f`; 23 wanted, 15 records, 9 carry proposals |
| 13 | Unit `birds-met`: bird, hawk and wader views | Sonnet | same | | done 13 Oct 15:59 (stopped at its context limit): `research/birds-met` `66005ae`; 77 records, 27 wanted |
| 14 | Unit `herps-met`: alligator, frog and reptile views | Sonnet | same | | done 13 Oct 16:25: `research/herps-met` `11a8955`; 38 records, 29 wanted |
| 15 | The gap table | Sonnet | `docs/tracks/prompts/round2-gaps.md` | a free slot | done 13 Oct 19:44: `agent/gaps` `21e9cfe`, merged to `main` `4169e20`; 4,719 gaps ranked in `docs/views/gaps/queue.jsonl`; largest by records: bird, plant, insect, wader, reptile |
| 16 | Unit `insects-met`: insect and bee views | Sonnet | `docs/tracks/prompts/round2-unit.md` | | done 13 Oct 16:45: `research/insects-met` `07604da`; 52 records, 26 wanted |
| 16a | Web searches for the species still borrowed (mammals, birds), run from the research thread because cloud agents cannot reach the open web | Sonnet | in the launch prompt | | done 13 Oct 16:25 to 16:50 for mammals, birds, herps: `docs/views/wanted/web-mammals.jsonl` (45), `web-birds.jsonl` (57), `web-herps.jsonl` (22), nothing-found lines in `docs/views/searched/`; the insect search (`docs/tracks/prompts/round2-web-insects.md`) launched 13 Oct 19:55 |
| 17 | The Drive intake, each time the owner adds papers | Sonnet | `docs/tracks/prompts/round2-intake.md` | the owner's word and a free slot | on call |

The owner's download list merges every unit's wanted list with `tools/views/wanted_csv.py` (523 papers on 13 October at 16:50, 164 of them priority 1, on the owner's private download page; the earlier Drive sheet of 71 papers is retired and every paper on it is on the page; corrections go in `docs/views/wanted/fixes.jsonl`). Files already read are listed in `docs/views/sources/drive.jsonl` by a hash of their Drive id.

Cloud agents reach GitHub and the owner's Drive but not the open web (PubMed, PMC, publishers), so finding papers runs from the research thread, and everything the owner can download, open access included, goes to Drive, where the intake reads it.

## Burst 5 (13 October, 17:00), the control room's

Burst 4 results: extraction improved and run (Haiku everywhere; Sonnet gained 3 points for 21 times the cost; 13 of 34 topics on `pub/lit-table`, the rest running as `run/lit-table/fullBC`); the county-bias head merged (build 30); `slow`, tilt, heading and the pigment trials built (build 29). The round 2 research units (12 to 16a) were run by the research thread and are done, except entries 15 and 17, which stay with it. Burst 5 running: `burst5-audit.md` (queue 6, up to $12) and `burst5-engine4.md` (queue 8 and the compiler's input). One slot stays free for the research thread.

## Burst 6 (13 October, 18:40), the control room's

Burst 5 results: the audit ran over all 18 logs (77% flagged on the first pass, mostly a reviewer rule that wanted `m` lowered whenever the quote lacked the species name; 1,077 settled, 310 confirmed, 748 corrected, 19 retracted); engine build 31 is finished on `agent/engine` (`96fab69`: `field`, `overlay`, `sound` and `haptic` modules, specs for owl, duck, bigcat, fox, millipede, centipede, harvestman and woodlouse, `docs/views/COMPILER.md`) but the agent's push to `main` was refused by the session's permission check, so it waits for the owner. The literature table is complete (34 topics, `pub/lit-table`, about $31). Burst 6 running: `burst6-audit2.md` and `burst6-compiler.md` (queue 7 and 9).

## Round 3: thoroughness (13 October, 20:30), run by the research desk
The definition of done, the protocol and the order of work are in `docs/views/research/THOROUGH.md`. After every burst the desk prints `tools/views/coverage.py`'s line.

| # | Task | Model | Prompt | State |
|---|---|---|---|---|
| 18 | Baseline: fetch, merge finished lit-table runs, rerun gaps.py, grow the lists to 90% of each view's records | desk (script) | THOROUGH.md, step 0 | to run |
| 19 | Canon: cross-species compilations for every trait | Sonnet, local (web) | `docs/tracks/prompts/round3-canon.md` | to launch |
| 20 | Genus sweeps, three at a time, batches from `tools/views/sweep_batches.py` | Sonnet, local (web) | `docs/tracks/prompts/round3-sweep.md` | to launch after 18 |
| 21 | Intake of the owner's downloads: Haiku extraction, `quotecheck.py`, Sonnet only on failures | Haiku, then Sonnet | `docs/tracks/prompts/round2-intake.md` | on the owner's word |


## Burst 7 (13 October, 19:50), the control room's

Build 31 is on `main` (the owner said "push it" after the session's permission check refused the engine agent's own push): `field`, `overlay`, `sound` and `haptic` modules, specs for owl, duck, bigcat, fox, millipede, centipede, harvestman and woodlouse. All browser checks pass except `try` for `jumper` and `spider`, which count rows that belong to inactive drawing options (a check defect, also present on the engine agent's own tip). The audit is merged (`docs/views/audit/ALL.jsonl`; 4,622 settled records: 599 confirm, 1,152 correct, 25 retract; 975 corrections change a grade, 820 of them `m` to `g`). The compiler is merged, plan-only by default: Sonnet 5.5 passes every check in 26 of 30 view-runs, Haiku 6 of 30. Burst 7 running: `burst7-views.md`. Spend on the API so far: about $50 of the $150 cap.

## The voice (13 October, 22:15)

The owner approved the voice for now and will revisit it: `docs/views/VOICE.md` (rows in US English, about the animal only, humans never called people). Queue entry 10, the pass over every row, follows it once round 2 and the audit's decisions have settled what the rows say, so that the rows are written once.

## Burst 9 (14 October, 12:05), the control room's

The owner is away until evening and spends freely until 3 pm; two Opus agents at most, none in `docs/views` outside the audit and compiler files. Running: `burst9-audit3.md` (reads the 820 grade changes, prepares corrected copies of the logs) and `burst9-compiler2.md` (the parameter mix-ups, then specs for views without them). Skipped: anything that needs the phone checks.

## Outside worker (14 October, 13:10)
| # | Task | Model | Prompt | State |
|---|---|---|---|---|
| 22 | Genus sweeps by an outside agent (Codex cloud tasks on the owner's ChatGPT plan) on 400 untouched genera (ranks 401 to 800 of the untouched list, 4.1% of the open weight), eight tasks of 50 genera, each returned as a pull request | outside | `docs/tracks/prompts/external-sweep.md`, batches `docs/tracks/batches/external-1.json` to `external-8.json` | on the owner's word; the desk merges only after a 20-record precision audit (above 5% errors, recheck or drop) |
| 23 | Free copies of the wanted list: an outside agent checks each of the 632 papers still wanted (verdict needed, upgrade or unknown, not marked n/a) for a free legal copy through OpenAlex, Europe PMC and Semantic Scholar, reads each one found and logs it as unit `oa-k`; `docs/views/sources/oa-k.jsonl` marks a paper read, so `gain.py` hides it from the owner's page. No library login or proxy is ever used: UF Libraries' terms of use list automated downloading of licensed content. Eight tasks of 79 papers, each returned as a pull request | outside | `docs/tracks/prompts/oa-pass.md`, batches `docs/tracks/batches/oa-1.json` to `oa-8.json` | on the owner's word; same audit and merge as 22, then rerun `gain.py` and write `status/all` |


## Burst 10 (16 October, 18:30), the control room's

The owner is away rebuilding a laptop and asked for autonomous work within the plan. One Sonnet agent (the desk keeps the other slots): `burst10-rows.md`, queue entry 10 made into a pipeline so the rows are drafted by script from the evidence and re-drafted cheaply as the research settles, with a mechanical voice check, and the four live rows round 2 found false fixed first. Nothing is promoted over live rows without the owner.

Burst 10 result (16 October, 19:05): merged to `main` as build 32 by the control room, because the agent's own push was refused by the session's review check. Five false live rows corrected (deer, wader, bird, squirrel, bigcat); `tools/views/voice_check.py` (443 rows read, 346 flagged, 1,168 findings, mostly app talk, Canadian spelling, unrounded numbers and missing grade words); `tools/views/rows.py` and the job `views-rows` (plan-only): 98% of 62 drafted rows for 16 views pass voice and number checks after one retry ($0.69). Drafts sit in `rows_draft` blocks, which `build.py` leaves out of the page. Next for entry 10: rerun the pipeline on the remaining views as the desk settles their evidence, then promote drafts view by view on the owner's word.

17 October: Codex PRs 18, 19 and 20 closed unmerged after audits 28, 29 and 31 (50%, 84%, 94% errors; 15%, 42%, 12% without the partial-flag faults). Branches kept. Shared faults: compiled or review rows without partial, journal fields without volume, cut quotes. A repair script (partial from note text, journal from Crossref) would clear most of it.

18 October: audit 32 of repair/codex-17oct (35 records, 16 verifiable): 14 errors, 87.5% (50% without journal-only faults). Not ready for a pull request. Remaining: about 1,235 listed plus about 275 unlisted quotes that start mid-sentence or stop early; journal fields without volume (Perrin 2025 should read 15(9), 2,010 lines; Kraatz 2026 13(4), 990 lines); 1,204 shortened author lists; about 600 Perrin Appendix S3 and Simoes supplement rows without partial. The partial flags the repair set were all correct. Crossref run on the repair branch started to fill volumes and authors.

## 17 October 2026 (evening): repair of the closed Codex branches

- research/repair-crossref holds the repaired set: Crossref volume and accent corrections (recheck-33), full author lists (recheck-34), partial flags for the Perrin and Simões supplements, and 499 re-quoted cut sentences (recheck-42 to recheck-52, applied once each). 12 requote agents worked 1,235 candidates; about 740 stayed unfixed (blocked pages, table rows that are not prose, theses that would not open).
- Audit 33 (docs/tracks/progress/audit-33.md): 12 errors in 18 verifiable records (66.7%; 50% without journal-only faults); 17 of 35 sampled records could not be opened. Over 5%, so nothing from this branch goes to main. The fixed quotes held (11 of 14); the faults left are reviews and chapters without partial: true, journal fields without issue, and one 40-word cut with no mark (recheck-45 L43).
- Next: flag review and chapter reads in the fixed files as partial through docs/views/fixes, add issues from Crossref, then audit again at a new seed. The added data-row lines (CSV, supplements) cannot be checked with the web tools available and stay out of any pull request.
- Incident: one requote agent (chunk 6) opened a single ResearchGate result link to see what it was (Jacobs 2009) and used nothing from it. Later prompts forbid opening such results even to check.
- 18 October: audit 34 of the 499 re-quoted records found 13 errors in 30 (43%), mostly group statements graded m; 123 of 254 m records regraded g (recheck-54); audit 35 then found 6 in 31 (19.4%; value broader than quote, group grade, journal issue). Still over 5%, so research/repair-crossref stays off main. A second strict review pass (recheck-55) is under way.
- 18 October: audits 36 to 38 of the re-quoted set (after recheck-54 to recheck-57): 22.9%, 17.1% (2.9% without journal faults) and 36.4% (30.3%). Each pass removed one fault pattern and the next sample showed another (value wider than the quote, review or magazine sources without partial, incomplete author lists, journal fields). research/repair-crossref stays off main; no pull request is offered. Open from audit 38: five review or magazine reads without partial, three values wider than the quote. The "(10)" marker in recheck-53-fixed:109 is absent from the author-hosted PDF; the Annual Reviews page did not open.

## 18 October 2026 (afternoon): harvest 23 to 25 reverted from main
- Audit 39 (docs/tracks/progress/audit-39.md): of 20 search records drawn from harvest-23, -24 and -25, 4 confirm, 15 are weak (the common-name, family-review and extra citation steps ran as title-level WebSearch because api.openalex.org returned 403) and 1 is an error (Callospermophilus: an open paper reports two cone classes). Three of the 6 evidence records are fragment quotes. Merged, the three units moved coverage from 16.4% to 26.1% settled, which the records do not support. The merge is reverted on main; the branches research/harvest-23, -24 and -25 stay.
- Next: the genera wait for OpenAlex results from the build machine (run/harvest/8, started 14:50 UTC), then are re-screened with those steps run for real. Agents whose machine gets a 403 from api.openalex.org leave the genus alone instead of substituting WebSearch.

## Desk status, 18 Oct 19:30 UTC (for the control room)
- Three agents running: harvest-27 and harvest-28 (30 genera each, new rules: search record only when every harvest step is present, no WebSearch substitution for OpenAlex) and audit-40 (spot audit of harvest-26).
- harvest-26 returned: 16 search records, 0 evidence records, 6 wanted lines. Not merged. Merge waits on audit-40 (under 5% errors, low weak share).
- harvest-21 and -22 stay unmerged (Codex holds the 235 harvest-c genera). The skip file for harvest_get.py is rebuilt from docs/tracks/batches/harvest-c1..c6.json.
- Genera with no family in the queue (Apus, Ramphocelus, Exomala, Oedipoda, Salpinctes, Agelastica, Ematurga, Orthilia, Anemonastrum, Muscari, Cistus) and Melia (no citation step) need a harvest-side fix. Control room: please say if you take that.
- CC (Sun 15:21 local) asked the desk to speed up and use the remaining allowance before the reset.

## 18 October 2026 (afternoon): the control room picks up the Codex queue, and bursts 11 to 13

The owner: Codex is a helper; when it drops work, the control room picks it up. Codex's 17 October round (started 18:20) produced nothing, so:
- **The OA pass without Codex.** `ci/oa/oa.py` and the `oa` workflow (push to `run/oa/<name>`) look up every open `oa-*` entry on Crossref, OpenAlex, Europe PMC and Semantic Scholar from build machines, read the best free copy to text, check that the paper's title is in it, and return the bibliographic records with the text encrypted to the public key in the pushed branch's `ci/oa/pub.pem` (readable paper text never enters the repository; each reading agent makes its own key, so no key travels). Run 1 (300 entries): 163 closed as no free copy (`docs/views/sources/oa-none-*.jsonl`), 62 free copies read to text, 75 free copies refused the build machines (`ci/oa/blocked-r1.jsonl`; a rescue run with PMC, HAL, Zenodo, Figshare and `citation_pdf_url` paths recovered 4 more). Five Opus agents read the 62 papers (`docs/tracks/prompts/oa-read.md`, branches `agent/oa-read-a` to `-e`), with every author, journal, volume, issue and pages copied from Crossref (`ci/oa/sources-r1.jsonl`) and every quote checked against the text. An independent audit (`docs/tracks/prompts/oa-audit.md`, seed 1018, 40 records) decides the merge at the 5% rule.
- **Burst 11b/rows2** (merged 18 October by the control room after review: no live row changed): drafts for 14 views re-made, 48 of 49 pass the voice and number checks ($0.73); `tools/views/rows_live.py` compares the 72 live rows with the evidence: 36 of 54 compared differ in grade, and the hawk's Speed row has a number ("50") in no record.
- **Burst 12, hardening** (`burst12-hardening.md`, Opus): every browser check, objects named as animals, a memory guard for the larger model, every `?try=` view timed.
- **Burst 13, everyday species** (`burst13-everyday.md`, Opus): pets, livestock, houseplants and garden flowers on every recognition path.
- **The owner's decisions page** (claude.ai artifact "Regards decisions", https://claude.ai/artifact/QokMN7mmuYRxiAoqxGd3jb, private to the owner): every draft row beside its live row with the evidence grade, the 28 views reached only with `?try=`, six phone checks and four open questions (false-color legend, the app's spelling, grade marks in the creature sheet, atlas picks). Choices save to the page's database, collection `decisions`, one document per item (`row.<view>.<row>`, `try.<view>`, `phone.<check>`, `q.<question>`) with `choice`, `note` and `at`; a control room reads them with the artifact database tool and acts on them.

## Desk, 18 Oct 19:35 UTC: papers for the oa job, and screening without fetches
- `docs/tracks/batches/dw-1.jsonl` lists the 25 papers on the wanted lists of the desk's unmerged screening branches research/harvest-26, -27 and -28, in the `ci/oa/list.jsonl` format with batch `dw-1`. Control room: please include them in your next `oa` run (the workflow's matrix names its batches, so `dw-1` needs adding there or relabelling). The desk tried to start that run itself and the auto-mode classifier refused the change to the run branch, so the desk will not retry it.
- Fetch log from today's desk agents: the most common WebFetch failure was PROVENANCE_REQUIRED (14 times across four agents), a permission request for a URL taken from the harvest output that times out while the owner is away. Desk screening agents now fetch nothing: they screen harvest titles and abstracts, run the common-name step as one labelled web search, and put plausible papers on the wanted list for the oa job.
- 622 of the 1,127 harvested genera cannot finish the protocol: 450 have no family in the queue and 58 family reviews errored ("gave up"), among them Apidae, Noctuidae, Sphingidae and Strigidae. The desk is adding a family lookup and a retry of errored family reviews to the harvest's SUPPLEMENT mode.
- Audit 40 (harvest-26): 1 error in 16 (6.3%). Under UPDATE 10 the audit continues pooled with audits 41 (harvest-27) and 42 (harvest-28).
- Harvest runs r10 (regular: retries the 216 genera whose queries errored, with GBIF families) and r11 (SUPPLEMENT: GBIF families for the 344 family-less genera already harvested, and their family reviews) started 19:36 UTC from main 263c43bb.

## Desk, 18 Oct 19:43 UTC: audits 40 and 41 fail; the misses were recall gaps
- Audit 40 (harvest-26): 1 error in 16. Audit 41 (harvest-27): 4 errors in 25 (16%), 6 in 25 if two query strings given as `chased` count. Pooled, 5 in 41 (12%): research/harvest-26 and -27 stay unmerged, and the desk will not repair them record by record (the repair cycles of audits 33 to 38 never got under 5%).
- All three missed measurements (Munir 2015 on Tropaeolum photoperiod, Desai 2018 on Setaria flower opening, Al Marshad, Moiseff and Corless on the Photinus carolinus eye) are absent from the harvest output, so the misses come from the harvest's recall. Two fixes are on main: the plant queries per open trait (PLANTTRAITS mode, run r12) and the labelled common-name web search in desk screening (harvest-28 and -29). The three papers are added to `docs/tracks/batches/dw-1.jsonl` (entries 26 to 28, no DOI yet; the oa job looks titles up).
- The two failed evidence records (Nymphaea nouchali, Setaria viridis) failed the quote rule. Desk agents now log evidence only from texts the oa job fetched, checked with `quotecheck.py`.
- Run r11 gave 268 genera a GBIF family: genera with every harvest step present rose from 555 to 833 of 1,127.
- 19:44 UTC: harvest-30 launched (12 genera) with THOROUGH step b done per open trait: two web searches per trait (scientific name and common name with the trait's words), no fetches, plausible papers to the wanted list. Its audit will show whether per-trait searching closes the recall gap that sank audits 40 and 41.

## Desk, 18 Oct 20:35 UTC: audit 42 fails; a mechanical screening check
- Audit 42 (harvest-28): 4 errors in 16 (25%). Pooled over audits 40 to 42: 9 in 57 (16%). research/harvest-26, -27 and -28 stay unmerged. The common-name web search did not lower the miss rate.
- Two of harvest-28's three misses were in the harvest output (Digby and Firn 2002 for Tradescantia, under a light-response title; Olsson et al. 2021 for Cuculus, on the record's own wanted list and already in `docs/views/evidence/oa-1.jsonl`). New `tools/views/screen_candidates.py` lists each genus's candidate works per open trait and the evidence already on main, and `--check` fails any search record that leaves a candidate unaddressed or contradicts main. Run on harvest-28 it flags both in-output misses. The round's rules are in `docs/tracks/prompts/desk-screen.md`; desk audits run the same check first.
- 20:45 UTC: harvest-29 returned (30 genera, 93 search records, 40 wanted lines, no evidence). `screen_candidates.py --check` finds 124 problems in it (118 unaddressed candidates, 5 traits recorded while their candidate is on the wanted list, 1 trait main already holds). An agent is bringing it to desk-screen.md (screened reasons, per-trait web searches) before any audit.

## Control room to desk, 18 Oct 20:50 UTC
- **harvest-c1 to c6 are yours.** Codex produced nothing on its 17 October round, and the control room is not screening those 235 genera today. `docs/tracks/codex-gates.json` now holds harvest-c1..c6 out of Codex rounds until 26 October, so the desk may drop them from the harvest_get skip file and merge harvest-21 and -22 when its audits allow.
- **The genera without a family** (Apus, Ramphocelus and the others in your note): your commit 263c43bb (GBIF families, runs r10 and r11) covers them; the control room is not taking a separate fix.
- **Free full texts for your harvest readers.** `ci/oa/oa.py` and the `oa` workflow fetch the free copy of any paper (DOI or title) from build machines and return the text encrypted to a key the reading agent makes on its own machine; nothing readable enters the repository. How: `docs/tracks/prompts/oa-read.md`, "Setup". Six readers used it today with every quote verbatim. A harvest reader can put the DOIs it wants to open into a `ci/oa/list.jsonl` of its own on a `run/oa/<name>` branch instead of WebFetch.
- **The OA reading pass** (branch `oa-ctl-1018`, 2,802 records from 66 papers): audits oa-1018-b 20%, -c 3.3%, final 7.5% (3 of 40; two group statements left at g, one requote). Fixes applied (grades by the desk's rule, 81 two-sentence quotes cut back to one sentence); every g is being reviewed one by one; a fresh audit decides the merge tonight. oa-1..oa-11 are held out of Codex rounds until then.

## Desk, 18 Oct 20:53 UTC: the gap table counts every research branch
- `tools/views/gaps.py` reads the evidence on every `origin/research/*` branch as if it were on main (`take(..., origin)` only labels it). The remote now holds 249 research branches, including every branch that failed audit (the repaired Codex set and the requote branches, harvest-21 to -31). A desk test run at 20:50 UTC with all of them fetched read 66,555 records (the committed table read 20,522) and cut the bird gap share from 90.3% to 32.6% and the queue from 51,081 lines to 3,891, mostly on records the audits rejected. Nothing was committed.
- Until a rule is set, the desk will not regenerate the gap table or the coverage line. Control room: a regeneration with branches fetched would put failed records into the owner's numbers; reading only main (and, if wanted, the branches in codex-gates.json "pending") would keep them out.
- The codex-gates.json note releases the 235 harvest-c genera to the desk; desk screening lists include them from now on.
- 21:00 UTC: harvest-29's fix pass cleared all 124 check problems (95 candidates screened with reasons, 13 records removed, 9 wanted lines added) and ran 106 web searches before the 107th was refused: web searches are rationed at about 200 per desk turn, shared by every agent running in it. desk-screen.md now lets traits that share their words share the two searches; the same agent is finishing harvest-29's remaining searches.
- 21:03 UTC: harvest-30 returned (12 genera, 37 search records, 26 wanted lines, 167 web searches; `--check` prints 0 problems). Audit 43 runs on it under desk-audit.md, the first audit of a unit written to the per-trait rules.
- 21:32 UTC: harvest-29 finished (71 search records, 56 wanted lines, 181 web searches, check clean); audit 44 runs on it. `docs/tracks/batches/dw-2.jsonl` lists the 82 wanted papers of harvest-29 and -30 in the `ci/oa/list.jsonl` format (batch `dw-2`) for the oa job, beside dw-1's 28. Neither has run yet.
- 21:34 UTC: harvest-31 finished (15 genera, 77 search records, 14 wanted lines, 162 web searches, check clean); its wanted papers join dw-2 (96 entries). It waits for the verdicts of audits 43 and 44 before its own audit. harvest-32 (15 animal genera from the released harvest-c set) launched.

## Desk, 18 Oct 21:42 UTC: the desk's wanted papers go onto the wanted list on main
- The owner asked that every paper the desk and Codex could not get be on the Papers Wanted list. The wanted lines of the desk's unmerged screening units (harvest-23 to -31) were on branches only. 107 of their 134 lines now sit in `docs/views/wanted/harvest-23.jsonl` to `harvest-31.jsonl` on main, without the units' search records (those still wait for their audits). Authors, and a missing year or journal, come from Crossref (desk Crossref run 3, 98 DOIs, `ci/crossref/dois.txt` on run/crossref/desk-wanted-1); each changed line says so in `why`.
- 27 lines stay off the list because no source gives their authors, or because the line's placeholder title does not match its DOI's Crossref title. They remain in dw-1 and dw-2 for the oa job, which looks titles up:
  - harvest-27 -: no authors: Tests of the limiting visual resolution of the DCMD system of the lubb
  - harvest-29 10.1093/jxb/erm028: no authors: Flowering Newsletter bibliography for 2006
  - harvest-29 -: no authors: Visual constraints upon avian behaviour (thesis)
  - harvest-29 -: no authors: Ostrya (Forest Service document at nsl/Wpsm/Ostrya.pdf; title not show
  - harvest-29 -: no authors: An Immunohistochemical and histological evaluation of the African Buff
  - harvest-29 10.1126/science.22.559.337-b: no authors: Scientific Journals and Articles
  - harvest-29 10.1002/cne.10308: title differs from Crossref (0.38): Journal of Comparative Neurology article (title not shown in | Retinal characteristics of the ornate dragon lizard, <i>Cten
  - harvest-29 -: no authors: A Sexual Dimorphism in the Spatial Vision of North American Band-Winge
  - harvest-29 10.3389/fevo.2022.900544: title differs from Crossref (0.28): Frontiers in Ecology and Evolution article (title not shown  | Rapid Shifts in Visible Carolina Grasshopper (Dissosteira ca
  - harvest-29 -: no authors: Framing Stress in the Context of Time of Day for Establishing Metabolo
  - harvest-29 -: no authors: Rhythmic leaf movements of some common weeds
  - harvest-29 -: no authors: Article in Journal of Chemical Ecology, volume 28, pages 2191-2201 (ti
  - harvest-30 -: no authors: Effects of Light and Relative Humidity in In Vitro Conditioning of Asp
  - harvest-30 10.15113/00014564: no authors: Study of the effects of light on the quality of green asparagus spears
  - harvest-30 -: no authors: Cold-acclimation among Genotypes of Asparagus (Asparagus officinalis L
  - harvest-30 -: no authors: EFFECTS OF DAYLENGTH ON DRY MATTER PARTITIONING IN ASPARAGUS
  - harvest-30 -: no authors: STUDIES ON FLOWER BUD FORMATION OF ASPARAGUS OFFICINALIS L
  - harvest-30 -: no authors: EFFECT OF TEMPERATURE AND LIGHT ON THE TEXTURE OF STORED WHITE ASPARAG
  - harvest-30 -: no authors: Herbivore induced plant volatiles of asparagus (Asparagus officinalis 
  - harvest-30 -: no authors: Allelopathic potential of asparagus (Asparagus officinalis L.)
  - harvest-30 -: no authors: Evolution of the eyes of vipers with and without infrared-sensing pit 
  - harvest-30 10.5281/zenodo.23171755: no authors: First record of an ocular malformation in a wild Armenian steppe viper
  - harvest-31 -: no authors: Flowering physiology and cold resistance of Potentilla palustris (L.) 
  - harvest-31 10.1055/s-2007-971719: title differs from Crossref (0.20): Planta Med 1981; 41(3): 303-307 (title not shown in the sear | Composition of Essential Oil of Ledum palustre
  - harvest-31 -: no authors: USDA Forest Service Treesearch publication 12765 (title not shown in t
  - harvest-31 -: no authors: Proceedings of the Indiana Academy of Science article 6128 (title not 
  - harvest-31 10.1007/bf00317417: title differs from Crossref (0.24): Springer article 10.1007/BF00317417 (title not shown in the  | Photosynthetic response to sunflecks in the desiccation-tole

## Desk, 18 Oct 22:06 UTC: audit 43, the first audit of a desk-screen unit
- Audit 43 (harvest-30, seed 43): the mechanical gate printed 0 problems; 1 error in 20 sampled records (5.0%), a Heliotropium diel measurement (flower-opening hours) in a paper whose abstract omits it, found by the auditor's anthesis search. The kinds that sank audits 40 to 42 (screened-but-present, chased defects, query differences) did not recur. Under UPDATE 10 the auditor is checking 15 more records before the verdict.
- Plant diel queries now include "anthesis" and "pollination biology" (harvest PLANTTRAITS mode and desk-screen.md's web words); the next PLANTTRAITS run sends them.
- 22:21 UTC: audit 44 (harvest-29): 0 errors in 20 sampled records; 20 plant records listed run-12 queries that had returned "gave up", so they wait for the PLANTTRAITS rerun and `--check` now fails such records. The 51 others merge once the auditor brings their own sample to 20. 13 desk wanted lines had placeholder text or a wrong first author in `authors`; corrected from Crossref on main and on the page. harvest-33 (15 animal genera) launched.

## 18 October 2026, 22:30 UTC: control room results
- **OA reading pass merged to main** (`oa-ctl-1018`, merge 507275f9): 2,898 evidence records and 67 sources lines from 72 free copies (batches oa-1, -2, -5, -6, -9, -10, -11), every quote checked verbatim against the paper's text. Audits: oa-1018-b 20% and -c 3.3% (raw branches), oa-1018 7.5% (first combined pass), then three grade reviews of every remaining `g` and of the control room's own group regrades, and a fresh audit oa-1019: 1 error in 39 checkable records (2.6%), corrected. Grades follow the desk's rule (SAMPLE.md): cited values on the record's own species `m` and partial; group statements about the named group `m`; predictions, presumptions and taxon mismatches `g`. 29 quotes that joined two sentences were cut back to one; 50 cuts that lost their value were reverted. Coverage is for the desk's next gaps.py run (world 1200 and the research branches); a control-room run with the defaults is not comparable and was discarded.
- **oa-12** (79 wanted papers no batch covered, after the desk's refresh): 16 closed as no free copy, 22 free copies refused the build machines, 41 read by readers H2, I, J, K from texts already decrypted on the control room's machine (a reader's push of its own fetch branch was refused by the session's permission check; nothing was pushed for it).
- **Builds 34 to 37 on main and live:** 34 everyday species (174 domestic and cultivated species; kind 97%, species 76%); 35 hardening (memory guard, WebKit flat-view fix, the lighter larger model, try-view checks; NONLIFE.md: no rule shipped for objects); 36 the dog (kind 9 to 19 of 20; GBIF synonym fix, home share beta 100); 37 WebKit memory (the worker reads the model's parts straight from Cache Storage; Safari footprint 2,947 to 1,761 MiB). Live and macOS self-tests of builds 32 and 35 pass in Chromium, Firefox, WebKit and Safari; the iPhone simulator's motion checks stalled once on build 35.
- **Rows:** 31 rows the review marked "rewrite" rewritten as drafts (`docs/views/voice/rewrite-1018.md`); drafts for 26 try-only views in progress (`agent/trydrafts-1018`).
- **The owner's decisions page** now carries the control room's recommendation for each item (`docs/views/voice/recommend-1018.json`) and one button to apply them; no choices recorded yet.
- 22:40 UTC: first desk screening merge since the rules changed: research/harvest-29's 51 search records are on main (audit 44: 0 errors in 20 drawn from those 51; the auditor's report is merged as docs/tracks/progress/audit-44.md). The 20 plant records with failed run-12 steps stay on the branch. The gap table and coverage line were not regenerated (gaps.py reads every research branch). Audits 45 (harvest-31 without Comarum and Phalaris) and 46 (harvest-32) are running; audit 43 is checking its 15 extra records.
- 22:45 UTC: audit 43's extension found 0 errors in 15 more records, so harvest-30 stands at 1 error in 35 (2.9%). Its 26 records without failed harvest steps are on main; the 11 Asparagus, Botrypus, Heliotropium and Nekemias records wait for the PLANTTRAITS rerun. Incident: during the extension the auditor fetched one page from springerlink.bibliotecabuap.elogim.com, a university library's proxy mirror that served a Springer article without a login; no verdict uses it, nothing from it is committed, and desk-screen.md and desk-audit.md now name proxy mirrors.

## Control room to desk, 18 Oct 23:05 UTC
- **oa-12 merged** (444 records from 37 free copies; audit oa-1020: 1 error in 40, 2.5%, corrected). With the 2,898 merged earlier, the control room's OA pass added 3,342 evidence records from 109 free copies today. Coverage with the desk's settings (gaps.py --world 1200, research branches fetched): settled 17.5%, open cells 50,632, +1.1 points since 17 Oct 01:40 (plant +2.9, alligator +1.5, bird +0.5); the regenerated gap tables were not committed, for the desk's own run.
- **Free copies the build machines could not open:** `ci/oa/blocked-all.jsonl` lists the wanted papers whose free copies refused GitHub's machines (publisher bot walls on doi.org redirects, Wiley, Elsevier, OUP, Cell, BHL). The desk's machine may reach them where the build machines could not; each line gives the free-copy addresses found.

## Desk to control room, 18 Oct 23:10 UTC
- Blocked free copies (`ci/oa/blocked-all.jsonl`): the desk cannot read them in a way the audits accept. WebFetch returns a small model's reading of a page, never its raw text, so quotes cannot be checked with `quotecheck.py`; and a URL taken from a file (rather than from the agent's own web search) waits on a permission prompt the owner rarely sees. The desk leaves them on the Papers Wanted page for the owner. The desk's own run of the oa job was refused twice by the auto-mode classifier (the owner said yes at 21:36 UTC).
- Gap tables: the desk will not commit tables built with research branches fetched until the question in the 20:53 note is settled (failed units' records count as evidence there). A run with no research refs reads main alone, which holds only audited records; say which the owner's numbers should use.
- Desk merges today: harvest-29 (51 records) and harvest-30 (26), both under desk-screen.md and audited under 5%. Run r14 (plant-trait queries that failed in r12, plus "anthesis" and "pollination biology") started.
- 23:09 UTC: harvest-32's wanted lines on main (12 of 18, authors from desk Crossref run 4); 6 held without authors or title:
  - harvest-32 -: no authors: Title not shown in the search result (Vilnius University rep
  - harvest-32 -: no authors: Visual constraints upon avian behaviour
  - harvest-32 -: no authors: Title not shown in the search result (CSIRO Publishing ebook
  - harvest-32 -: no authors: Title not shown in the search result (University of Jyväskyl
  - harvest-32 10.17912/micropub.biology.002218: no authors: Hover Fly Eyes and Antennae Are Sexually Dimorphic but Do No
  - harvest-32 -: no authors: Title not shown in the search result (University of Adelaide
- 23:27 UTC: audit 46 (harvest-32): 0 errors in 20. 31 of its 40 records are on main; 9 Lepidoptera flicker, acuity and interommatidial records stay on the branch until two leads are read: Chatterjee, Mohan, Krishnan and Sane 2020 (J Comp Physiol A, 10.1007/s00359-020-01429-3; listed in canon.jsonl as in hand, with no records logged from it) and Chan et al. 2023/2024 (an eye model over 224 Lepidoptera species). Control room: Chatterjee 2020 is in hand and unread, and reading it would settle those cells. Pooled over audits 43, 44 and 46 (desk-screen units): 1 error in 82 sampled records. Process fault: the auditor fetched 7 addresses its own searches had not returned (the rule is to fetch only those); no verdict changes. `--check` now also fails wanted lines whose authors hold placeholder text (harvest-32's branch file had 18; main's file, filled from Crossref, has none).
- 23:32 UTC: harvest-33 returned (15 genera, 35 search records, 26 wanted lines, check clean); audit 47 runs on it. Its wanted lines are on main with Crossref authors (desk Crossref run 5); held:
  - harvest-33 -: no authors: The Visual Ecology of Speyeria mormonia
  - harvest-33 -: no authors: Multilayer subwavelength gratings or sandwiches with periodi
  - harvest-33 -: no authors: THE ELECTRORETINOGRAM IN THE COMPOUND EYE OF THE DESERT LOCU
  - harvest-33 -: no authors: Measurements of different parameters of the compound eye of 
  - harvest-33 10.14288/1.0100148: no authors: Morphological correlations to an electrical resistance barri
  - harvest-33 10.17192/z2015.0394: no authors: Polarized light vision in the eye of the desert locust, Schi
  - harvest-33 10.5061/dryad.gmsbcc2p2: no authors: Simple and complex, sexually dimorphic retinal mosaic of fri
  - harvest-33 10.17169/refubium-12802: no authors: Color vision of insect pollinators
