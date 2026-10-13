# Status

Updated 12 October 2026, 23:30 US Eastern. Whoever works on Regards updates this file at every checkpoint, and before and after any long step, so that the work can stop at any moment and pick up where it was.

## How the work is paced

- **In bursts sized to the owner's plan.** A burst runs at most three agents at once, each with a time limit set in its prompt. Nothing new starts until the owner says go or a time the owner agreed arrives. Usage beyond the plan has a ceiling the owner sets in the account's settings.
- **Build machines do the heavy computing between bursts.** GitHub's runners (fitting heads, computing rows, harvesting literature) cost the plan nothing.
- **Nothing is lost when work stops.** Every agent pushes its branch at least every 15 minutes and keeps a progress note (`docs/views/progress/<unit>.md` for research) saying what it has read, what it has logged and what comes next. A stop loses at most 15 minutes, and a fresh agent resumes from the note.

## Tracks

| Track | Brief | Branch | State | Next |
|---|---|---|---|---|
| The app | `docs/HANDOFF.md` | `main` | Build 23 is live: build 22 with the contact form switched on. | A first message sent from a phone; fold in the research corrections the owner approves. |
| Research: birds | `docs/views/research/BRIEF.md` | `research/birds` | Done (`77aac6c`): 218 records, 30 papers wanted. Proposes `owl` and `duck` views and corrects `hawk`. | The owner's decisions; an audit. |
| Research: cats, dogs and people | same | `research/cat-dog` | Done (`3b18838`): 178 records (about 50 for people), 23 papers wanted. Proposes `bigcat` and `fox` views, and a person's field of 200 degrees in place of 180. | The owner's decisions; an audit. |
| Research: snails, worms, scorpions, ticks | same | `research/ground-invertebrates` | Done (`9c75995`): 197 records, 22 papers wanted. Proposes seven views, with new groups for millipedes, centipedes and harvestmen. | The owner's decisions; an audit. |
| Research: the other eleven units | same | `research/<unit>` | Not started. `jumper` has 20 records and a draft on `main`. | Bursts 1 to 4 below. |
| The engine and new effects | `docs/tracks/engine.md` | `agent/engine` | Not started. | After the jumping spider research. |
| The pocket model's group head | `docs/tracks/head.md` | `agent/world-head` | The trials so far are in `tools/world/EXPERIMENTS.md`. | A burst of its own, mostly on build machines. |
| The full database for the world | `docs/tracks/worlddb.md` | none yet | Not started. | A burst of its own, mostly on build machines. |

## Bursts proposed (revised 12 October, 23:40)

Spend first where the outcome is decided, push mechanical work onto build machines, keep every context small, and use a model fitted to each job (Haiku for extraction and quote checks, Sonnet for research, Opus for design, engine and audits).

1. 00:31, 13 October: the senses atlas (Opus); the engine's render gallery and attention module, starting the jumping spider view from the draft and log on `main` (Opus); and the build-machine jobs (Sonnet): a measurement index over `pub/lit-t1` (every sentence with a value and a unit, with its source), the published cross-species compilations, and record shares from `pub/data-world`.
2. The jumping spider and other spider research, searching the measurement index first; more engine modules.
3. Onward, one burst at each five-hour reset: research filled in just in time for each engine module, then audits by agents that did not write the work, a gallery review by the owner, one pass over all the rows, and builds.

## Known limits

- PDFs from Drive now read in full through `download_file_content` and `pdftotext` (the brief says how), for files up to 10 MB; *Animal Eyes* gives all 291 pages. *Neurobiology of Arachnids* (18 MB) and *Spider Biology* (159 MB) are over the limit and wait for the owner to split them into parts.
- The papers the finished units want are in a sheet in the owner's Drive, beside the papers (71 from the first three units, 22 of them priority 1). Units add to it as they finish.
- From the cloud machines, PubMed, PubMed Central, Europe PMC, Crossref, doi.org, GBIF and iNaturalist mostly refuse or rate-limit. The research rests on the collection on `pub/lit-t1` and the owner's papers.
- The branch `probe/remote-push` holds one empty commit from a test; agents cannot delete branches, so it waits for the owner or a person with access.
