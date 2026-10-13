# The plan (13 October 2026, 00:20)

The one document every agent on Regards reads first. `docs/STATUS.md` holds the current state and `docs/tracks/QUEUE.md` the order of work; the owner's project doc holds the private details. Read this, then those.

## The aim

The best, most informed, most interesting views that a phone can draw: accurate where the evidence exists, invented and marked as such where it runs out, beautiful, dynamic, and smooth on a phone. Every creature named; the full database for the world; the app still fast. The owner's budget is a Max plan's allowance plus a bounded spend on credits, and the owner can stop the work at any moment without losing it.

## Five principles

1. **Modules times specs.** The engine gains about twenty sensing mechanisms as general modules (`docs/views/ATLAS.md` names them; `docs/ENGINE-DESIGN.md` orders them). A view is a spec file: which modules, their parameters with grades and `invented` marks, and its rows. Once the modules exist, a view is data.
2. **Views are finer than the recognizer.** The pocket model names the group; the full database names the species; the spec chooses the view from the species, falling back to the group's view. So owl, duck, big cat, fox, millipede, centipede and harvestman views need no refit of the recognizer.
3. **Agents only for stateful, tool-using work.** Many small independent judgments (extracting measurements, checking that a quote supports a value, drafting specs, drafting rows) go to the Batch API as scripts, on build machines for the public collection and from agents' machines for nothing private. Haiku in batch costs about a hundredth of an Opus agent per token and reads no growing context.
4. **The expensive model designs; the cheaper models build.** One Fable or Opus agent writes the atlas and the engine design, with two or three structurally different ways to draw each mechanism, and the owner picks. Sonnet implements modules. Haiku compiles specs. Opus returns where the architecture changes. One Fable or Opus pass gives every row one voice at the end, after the owner approves five sample rows.
5. **Research stops at the visibility floor.** The engine measures, per parameter, the smallest change a phone render shows. Research precision stops there; agent research goes only to views whose record share and mechanism distinctness earn it; the long tail comes from the pipeline's table and the spec compiler. The jumping spider comes first regardless, for the owner and the specialist.

## Resources

- **The plan's allowance** (five-hour windows; a weekly meter; one free full reset that clears both): the design, the modules, verification research, the control room. Used every window, overnight included, so that the weekly meter reaches 100% early and the free reset buys most of a second week. After the reset, paced to Sunday.
- **Credits** (at most $750 a month; a few hundred if it changes the outcome): the batch jobs, estimated at tens of dollars in all, and daytime bursts while the owner reviews. Never overnight. Off between planned paid bursts, so that a limit is a pause.
- **Build machines** (free for a public repository): the pipeline, the renders, the recognizer fits, the world rows.
- **People** (free, and the best audit there is): the owner's phone through `?try=<view>&tune=1` with a tuning panel and a compare slider; the jumping spider specialist's review of a one-page parameter sheet; possibly the owner's course taking the parameter ledger as an assignment.

## How it runs

- One control room chat at a time, on Sonnet, started from the owner's project doc; strategy on Opus or Fable in a fresh chat. The control room launches the queue's next entries, at most three at once, one burst per window, and reports in a line. Once one scheduled task is shown to launch agents unattended, a runner works the queue at each reset.
- Every prompt is saved under `docs/tracks/prompts/` before launch. Every agent pushes within 10 minutes and then every 15, keeps a progress note, greps texts rather than reading whole books, and stops past about 100,000 tokens of context for a fresh agent to continue. `docs/STATUS.md` is updated at every checkpoint.
- Two tests the owner runs once decide allocation: whether the main weekly bar moves while using Fable, and the same small task on Opus and on Sonnet with the session meter read before and after each.
- The first visible result is the jumping spider view at `?try=jumper`, expected within two windows of the start.

## Risks, named once

- The tooling (pipeline, spec compiler, runner) could eat the first day with nothing to show. The queue interleaves it with the jumper view so that a view exists early.
- The pipeline's table can hold numbers out of context. It is for search; a value enters a spec only after a Sonnet agent verifies it against the source passage, and the calibration against the 593 hand-made records says how far to trust it.
- The meter's weighting of models is unknown until the owner's tests; allocation follows them.
- A scheduled runner may stall on approvals; the control room is the fallback.
