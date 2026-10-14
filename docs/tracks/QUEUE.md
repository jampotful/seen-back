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
