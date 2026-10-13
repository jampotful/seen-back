# Status

The plan is `docs/tracks/PLAN.md`; the order of work is `docs/tracks/QUEUE.md`. Updated 13 October 2026, 10:50 US Eastern. Whoever works on Regards updates this file at every checkpoint, and before and after any long step, so that the work can stop at any moment and pick up where it was.

## How the work is paced

- **In bursts sized to the owner's plan.** A burst runs at most three agents at once, each with a time limit set in its prompt. Nothing new starts until the owner says go or a time the owner agreed arrives. Usage beyond the plan has a ceiling the owner sets in the account's settings.
- **Build machines do the heavy computing between bursts.** GitHub's runners (fitting heads, computing rows, harvesting literature) cost the plan nothing.
- **Nothing is lost when work stops.** Every agent pushes its branch at least every 15 minutes and keeps a progress note (`docs/views/progress/<unit>.md` for research) saying what it has read, what it has logged and what comes next. A stop loses at most 15 minutes, and a fresh agent resumes from the note.

## Tracks

| Track | Brief | Branch | State | Next |
|---|---|---|---|---|
| The app | `docs/HANDOFF.md` | `main` | Build 25 is live: build 24 (the full database for the world) with four small copy and style changes (`docs/LOG.md`, 13 October). | A first message sent from a phone; fold in the research corrections the owner approves. |
| Research: birds | `docs/views/research/BRIEF.md` | `research/birds` | Done (`77aac6c`): 218 records, 30 papers wanted. Proposes `owl` and `duck` views and corrects `hawk`. | The owner's decisions; an audit. |
| Research: cats, dogs and people | same | `research/cat-dog` | Done (`3b18838`): 178 records (about 50 for people), 23 papers wanted. Proposes `bigcat` and `fox` views, and a person's field of 200 degrees in place of 180. | The owner's decisions; an audit. |
| Research: snails, worms, scorpions, ticks | same | `research/ground-invertebrates` | Done (`9c75995`): 197 records, 22 papers wanted. Proposes seven views, with new groups for millipedes, centipedes and harvestmen. | The owner's decisions; an audit. |
| Research: the other eleven units | same | `research/<unit>` | `jumper` done and merged to `main` (13 Oct). Ten more units hold logs on `research/<unit>` from 12 Oct, 21:00 to 23:12: methods 1,159, insect 523, spider 320, sea-invertebrates 307, bee 267, herps 220, mammal-groups 209, plant-fungus-slime 202, fish-shark 187, squirrel-deer-rabbit 171. None audited. | The batch audit of all fourteen units once the API key exists (queue 6). |
| The engine and new effects | `docs/tracks/engine.md` | `agent/engine` | The design is merged to `main`: `docs/views/ATLAS.md` (25 mechanisms) and `docs/ENGINE-DESIGN.md` (modules 0 to 13). `agent/engine` holds six earlier commits not on `main` (prototypes behind `?try=reef`, `shark`, `spider`). | Burst 2 (queue 4 and 4a). Drawing options are switchable with `&draw=` so the owner picks on the phone. |
| The pocket model's group head | `docs/tracks/head.md` | `agent/head-next`, `agent/head-ship` | `merge-county` on TinyCLIP passes every mark on the test photos (primate, whale and bat named; Alachua −0.80 points, interval to −1.42; `docs/tracks/head.md`). `agent/head-ship` (`251f719`, build 25) holds the slot and the page's second bias; not on `main`. | The app's thread merges `agent/head-ship` after `agent/world-db`. |
| The full database for the world | `docs/tracks/worlddb.md` | `agent/world-db` | Shipped to `main` as build 24 (13 Oct): 427,163 world rows, 2-degree place files, the encounter rule and the world test. 674,978,799 bytes in all, downloaded only with consent. The world test: 63.8% right with no prior, 76.1% with the time zone, 77.1% with three creatures met, 78.8% with the true 400 km circle. | Waiting on the owner's phone test of the download. |

## Burst 1 (launched 13 October 00:39, finished 00:53)

Meters at launch: session 0%, weekly 50%, Fable only 5%, credits $89.83 of $750 this month, usage credits switched on. Three agents ran at once: design (Opus), jumper research (Sonnet), pipeline writer (Sonnet). One shared checkout was switched between branches by agents; later prompts tell each agent to work in its own clone or worktree.

## The shape of the work (settled 13 October, 00:00)

Views are modules times specs. The engine gains about ten sensing mechanisms as general modules; a view is then one spec file (modules, parameters, rows), which is cheap to add once the modules exist. Three resources, each for what it does best: the plan's allowance for engine modules, view design and verification research, every five-hour window; the API from build machines for a one-time extraction pipeline over the literature collection (Haiku through the Batch API, every quote checked by script), whose table the research agents search instead of reading papers; and people, since the owner judges each view on a phone through `?try=<view>` with a tuning panel, and a specialist reviews the jumping spider view. Design comes before building: the atlas gives two or three ways to draw each mechanism and the owner picks.

The order of work is `docs/tracks/QUEUE.md`, which the owner approves once and edits to steer. Two rules decide where tokens go: an agent is used only for stateful, tool-using work, and any task that is many independent small judgments (extraction, quote checks, spec drafting, row drafting) goes to the Batch API as a script; and the expensive model writes the design that the cheaper models build from.

## Known limits

- PDFs from Drive now read in full through `download_file_content` and `pdftotext` (the brief says how), for files up to 10 MB; *Animal Eyes* gives all 291 pages. *Neurobiology of Arachnids* (18 MB) and *Spider Biology* (159 MB) are over the limit and wait for the owner to split them into parts.
- The papers the finished units want are in a sheet in the owner's Drive, beside the papers (71 from the first three units, 22 of them priority 1). Units add to it as they finish.
- From the cloud machines, PubMed, PubMed Central, Europe PMC, Crossref, doi.org, GBIF and iNaturalist mostly refuse or rate-limit. The research rests on the collection on `pub/lit-t1` and the owner's papers.
- The branch `probe/remote-push` holds one empty commit from a test; agents cannot delete branches, so it waits for the owner or a person with access.
