# Queue

The owner approves this queue and its budget once; a control room or a scheduled runner launches the next entries, at most three at a time, one burst per five-hour window, with usage credits off so that a limit is a pause. The owner edits this file to steer. Each entry names its saved prompt; private details are pasted into the launch prompt from the owner's project doc, never written here.

| # | Agent | Model | Prompt | Needs | State |
|---|---|---|---|---|---|
| 1 | Design: the atlas and the engine design | Fable if its allowance is separate, else Opus | `docs/tracks/prompts/burst1-design.md` | | queued |
| 2 | Jumping spider research | Sonnet | `docs/tracks/prompts/burst1-jumper.md` | the spider and book Drive ids, the specialist's account | queued |
| 3 | Pipeline writer: Haiku Batch extraction over `pub/lit-t1`, quote check, dry run on one topic | Sonnet | `docs/tracks/prompts/burst1-pipeline.md` (to write) | a Console API key as the secret `ANTHROPIC_API_KEY` to run in full | queued |
| 4 | Engine: first modules from `docs/ENGINE-DESIGN.md`, the jumper view, the tuning panel, the compare slider, the visibility floor | Opus | `docs/tracks/prompts/burst1-engine.md`, read with the design | #1 | after #1 |
| 5 | Meter tests: the same small task on Opus and on Sonnet, read by the owner | the owner | | | with the owner |
| 6 | Audit of the three finished units: a batch job that asks whether each quote supports its value; the flagged records to one Sonnet agent | Haiku batch, then Sonnet | to write | #3 | after #3 |
| 7 | The owner's decisions on the three units' proposals applied | Sonnet | to write | the owner | after #6 |
| 8 | Modules two onward, each followed by the views it unlocks as specs | Sonnet (Opus where the architecture changes) | to write | #4 | rolling |
| 9 | Spec compiler: specs and draft rows for every view from the pipeline's table, graded, `invented` marked | Haiku batch | to write | #3, #4 | after #4 |
| 10 | One pass over all the rows in one voice | Fable or Opus | to write | #9 | last |
| 11 | The recognizer's group head (B/16) and the world database | Sonnet, mostly on build machines | `docs/tracks/head.md`, `docs/tracks/worlddb.md` | | overnight, any time |
