# Thoroughness: when the research is done, and the cheapest way there (13 October 2026)

The owner asked for research that is thorough without skimping, at the least cost and in the least time. This file says what "done" means, which number tracks it, which search may declare a fact unknown, in what order the work runs, which model does what, and three small tests that keep the claim honest. It extends the Round 2 section of `BRIEF.md`. For how a record is written, BRIEF governs; for what to do next and when to stop, this file governs.

## What done means

A cell is one trait (a trait key of `docs/views/gaps/rows.json`) of one species on a view's list. The open cells are the lines of `docs/views/gaps/queue.jsonl`, which `tools/views/gaps.py` rebuilds. A cell closes in one of three ways:

1. It is measured in that species (`m`).
2. It is carried from a measured relative under a carry rule, and the row names the relative (`g`).
3. It is exhausted: the protocol below ran at the level its trait allows and found nothing. Only an exhausted cell licenses the looser wording of "Wording by certainty".

The research is done when no open cell is untouched or half-searched, and when each view's list holds the species that make up at least 90% of that view's research-grade records. On 13 October the lists of 60 species covered 10% of plant records, 15% of insect records and 33% of bird records, so the lists grow before the sweeps reach their tails.

"Every relevant paper has been read" has no end, so it cannot serve as the target. A target made of cells ends.

## The number

`python3 -I tools/views/coverage.py` prints one line after every burst and appends it to `docs/views/gaps/coverage-history.jsonl`. On 13 October, before any of this ran, it read:

`Coverage: settled 8.7% of record-rows; open cells 4,719 (exhausted 0.0%, half-searched 11.4%, untouched 88.6% of their weight).`

- Settled is the share of record-rows (records times rows) whose traits are all `m` or `g`.
- Exhausted, half-searched and untouched divide the open cells by their weight. Half-searched means a search record exists without the full protocol; every record written before this file is half-searched.
- `--views` adds a line per view. `--tests "..."` appends the three test results below.

Untouched and half-searched should fall to zero. Settled rises as far as the literature allows, and some cells will stay exhausted.

## The protocol that may declare a cell unknown

Run it at the widest level that cannot miss a measurement, and record it once for every cell it covers.

- For the optics traits (the `genus` class of `rows.json`: acuity, fields, flicker, tapetum, pupil and the rest), search the genus. A search on the genus name finds papers on any of its species, so one record covers every species of the genus, and a congener's measurement closes the cell as `g`.
- For pigments and receptor classes (the `order` class), search the genus and then the family, because rule 2 can carry from any measured family of the order.
- A family whose members are absent from every canon compilation may be searched at family level alone (`"level": "family"`). The search-recall test decides whether that is safe.

The steps, all in one line of `docs/views/searched/<unit>.jsonl`:

a. Canon. Check the trait's compilations in `docs/views/research/canon.jsonl` that are in hand and list their DOIs in `"canon"`. The script decides when this step is done, so nobody can skip it: `coverage.py` counts a trait's canon step complete when `canon.jsonl` exists and each of the trait's compilations is logged in the evidence or marked n/a by the owner. A sweep may therefore run before the compilations arrive; its records turn from half-searched to exhausted when they are logged.
b. Two searches. Search the scientific name with the trait's words, then the common name with the trait's words. Read the first 20 titles of each and open anything plausible. List the queries in `"queries"` and the places in `"where"`.
c. One citation step. Take the source of the nearest measured relative (the queue's `closest_record`) and look for later work that cites it and names the taxon, or for a review of the family. Put its DOI in `"chased"`.

Example: `{"taxon": "Sciurus", "level": "genus", "trait": "cff_hz; acuity_cpd", "queries": ["Sciurus flicker fusion", "tree squirrel visual acuity"], "where": ["WebSearch"], "canon": ["<DOI of each compilation checked>"], "chased": "10.1016/0376-6357(82)90008-0", "found": "none", "date": "2026-10-14"}`. A record older than a year is redone.

## Order of work

0. Baseline. Fetch the branches `gaps.py` reads (its README lists them), merge any finished `run/lit-table/*` results, rerun `gaps.py`, and print the coverage line. Then raise `gaps.py --world` until each view's list holds 90% of its records, and print the line again. If a view needs more than 300 genera to reach 90%, report the genus count to the owner before sweeping that view's tail.
1. Canon, one agent with web access, one burst. For each of the 21 traits, find the cross-species compilations: reviews with species tables, data supplements and deposited datasets, and genome surveys of opsin genes for the pigment traits. Confirm each DOI and write `canon.jsonl` lines: `{"trait": "...", "doi": "...", "title": "...", "covers": ["Order or family", ...], "species": 214, "in_hand": false}`. Put each one not in hand on the wanted list with priority 1, `"canon": true` and its `"covers"`.
2. The owner downloads in the page's order. `tools/views/gain.py` ranks each paper by the weight of the open cells it could close, so compilations rise to the top.
3. The intake reads each compilation whole and logs every species in its tables, on the queue or not. A paper is read once and everything in it is kept.
4. Genus sweeps, three agents at a time. Take open cells in order of weight, grouped by genus; each agent takes about 40 genera and runs the protocol on all open traits of each genus with combined queries. On 13 October the queue held 4,719 cells in 482 genera and 191 families, and 527 cells carried half the weight.
5. The intake runs on each batch of about ten new files in UNPROCESSED.
6. Steps 4 and 5 repeat until untouched and half-searched reach zero. Then the one-voice wording pass runs.

## Who does what

- The research desk runs on Sonnet at medium effort. It launches agents, merges results and runs scripts.
- Extraction from the owner's PDFs goes to Haiku subagents. Burst 4 measured Haiku within 3 points of Sonnet on extraction at a twenty-first of the cost (`docs/tracks/QUEUE.md`, burst 4 results). `tools/views/quotecheck.py` then checks every record against the PDF at no cost, and only the records that fail go to Sonnet. On two papers already logged it passed 15 of 16 and 44 of 47 records (verbatim or as a table row).
- `tools/views/windows.py` cuts a text to the passages near trait words and numbers. On two focused vision papers it kept 89% and 98% of the text, so it saves nothing there. Use it only for books and broad reviews.
- Searching needs judgment and the web, so it runs on Sonnet at medium effort, unless Haiku passes the search-recall test, in which case it runs on Haiku.
- Carry exceptions, rule 5 conflicts and the precision audit go to Opus, in small batches.
- Many small independent judgments on open text run as a Batch job (STATUS, "Two rules decide where tokens go").

## Three tests per burst

- Search recall. Take 10 cells already closed by a measurement, hide the record, and run the protocol blind. It must find at least 9. When it finds fewer, add a query type and test again. The same test decides whether family-level searching is safe.
- Extraction recall. Run the Haiku path on 3 papers a round-1 unit read in full. It must recover at least 95% of their records. When it recovers fewer, send that kind of paper to Sonnet.
- Precision. An Opus agent checks 20 random new records against their sources and reports the error rate. Above 5%, the batch they came from is checked again. Burst 5's audit corrected 748 of 1,077 settled records, mostly their grades, so this test pays for itself.

The coverage line carries the three results, for example `--tests "search 9/10; extraction 96%; precision 1/20"`.

## Papers that are no longer needed

At every check-in, and after every intake or sweep is merged, the desk saves the page's `ticks/all` (ArtifactData `get`) and its `extra` collection (`list`, limit 1000) into one folder, runs `python3 -I tools/views/papers_refresh.py FOLDER OUT --gaps` (gaps.py with the 1,200-species lists, the owner's marks, wanted_csv.py, gain.py, papers_extra.py), then writes OUT/status.json to `status/all` (ArtifactData `set`, pinned to the version it last read), sends each OUT/extra/batch-N.json (`batch`), and applies OUT/ticks-patch.json to `ticks/all` (`update`) when it exists. The page files every paper by itself, with no republish: To get (unmarked papers), Try again (marked partial or can't get, ranked by priority and then by what the paper would still fill) and Done (saved, in Drive, given up, or verdict done or read). A paper missing from `status/all` leaves the page, so `status/all` must always be written from the same run as the extras. Each paper gets a verdict:

- needed: at least one cell it bears on is open. It is ranked by the weight of its open cells.
- upgrade: none is open, but some are filled only by borrowing from a relative or only by an abstract. It stays on the list below the needed papers of its priority, because it would give the species' own measurement. `--retire-upgrades` retires these too, if the owner prefers.
- done: every cell it bears on is measured in the species itself from a full text. The page hides it.
- read: the intake has already read it in full from Drive. The page hides it.
- unknown: it names no listed species and no view, so nothing can judge it. It is never hidden.
- A reference work of `canon.jsonl` that the owner marked can't get or partial keeps priority 1 and ranks by the open cells of its traits, so it heads Try again.

Duplicates fold: a paper without a DOI whose title equals, extends or is extended by another paper's title, same first author and year, joins that paper (`wanted_csv.py`; supplements and data packages never fold). A mark on the folded copy carries over through OUT/ticks-patch.json.

The owner can bring any hidden paper back with its Still want it button (document `keep/all`), and the desk never overrides that. Records logged from a partial file carry `"partial": true`, so a cell that rests only on an abstract never counts as measured from a full text.

