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
