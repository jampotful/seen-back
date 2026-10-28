# Outside worker: free copies of the papers on the owner's list (Codex cloud task, or any agent with a shell and internet access)

You are helping research which animals, plants and fungi see what, for a phone app. The repository is github.com/jampotful/seen-back. The owner downloads the papers on the research's wanted list by hand. Your job is to find each paper in your batch that has a free, legal copy online, read it, and log what it measures, so the owner never has to fetch it. Your task message names a batch number, k (1 to 8). Work only on that batch and write only the files named below with that k, so that eight tasks can run at once without touching each other's files.

## Read first
1. `docs/views/research/BRIEF.md`, the sections on the evidence log: the record fields, the trait keys, the grades `m`, `g`, `i`, and the rule that `opened` means you read the source yourself in this task.
2. `docs/tracks/prompts/round2-intake.md`, which says how a paper is read. You read papers the same way, from a free copy instead of the owner's folder.

## Your batch
`docs/tracks/batches/oa-k.json` lists about 80 papers in the order of the owner's page, most useful first. When your instructions name entries (positions in its list, counting from 1), do only those: earlier rounds settled the rest. Each entry gives what is known of the paper: title, authors, year, journal, DOI or link, why it was wanted, and the species and views it bears on.

## Finding a free copy
Do the lookups with one script before you read anything: write a short Python script that checks every paper in your batch against the three sources below, saves what each returns under `/tmp/oa`, and prints one line per paper (found or not, and where). Then read only the papers it found, in batch order. Work down the list; if you have to stop before the end, stop between papers, with everything so far committed and the summary written.

The sources, by paper:
- OpenAlex, by DOI: `https://api.openalex.org/works/doi:<doi>?select=id,doi,display_name,publication_year,open_access,best_oa_location,locations`. Use `best_oa_location`, or any location with `is_oa` true, and its `pdf_url` (or its `landing_page_url` when that page carries the full text).
- Europe PMC: `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:"<doi>"&resultType=core&format=json`. A result with a `pmcid` and `isOpenAccess` "Y" (or `inPMC` "Y") has its full text at `https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/fullTextXML`.
- Semantic Scholar: `https://api.semanticscholar.org/graph/v1/paper/DOI:<doi>?fields=title,openAccessPdf,externalIds`, at about one request a second.
- A paper without a DOI: search OpenAlex by title (`https://api.openalex.org/works?filter=title.search:<words of the title>&select=id,doi,display_name,publication_year,authorships,open_access,best_oa_location`) and accept a match only when its title, first author and year agree with the batch entry. Then check it as above.

A free copy is the publisher's own free version, an open-access journal, PubMed Central or Europe PMC, a university or subject repository (often the author's accepted manuscript), or a preprint server. Never use a library login, a university proxy, Sci-Hub, LibGen, or uploads to ResearchGate or Academia.edu. A book or a book chapter almost never has a free copy, so one OpenAlex check is enough for it.

Keep downloaded files outside the repository, for example in `/tmp/oa`. Confirm that each file is the paper by finding its title on the first page. An accepted manuscript counts as the paper; say "accepted manuscript" in the `note` of each record taken from one.

## Writing what you find
- Read the whole paper, with its tables, and its supplements when they are free too. Log every measurement of a trait in BRIEF's list for every species in the paper, on the owner's lists or not, one record a value, with `python3 -I tools/senses/addlog.py oa-k < records.jsonl`. The record's `source` carries the DOI and, in `url`, the free copy you read, with `"access": "open"`. `opened` is true, and `quote` is copied exactly from that copy. Grade as `oa-read.md` does (BRIEF lines 66 and 174, `docs/views/audit/SAMPLE.md`, "The rule decided", adopted 18 October): `m` for a value on the record's own taxon, its own or cited from another study (a cited value is also `partial`), whether that taxon is one species or the group the record names, when the statement is about that group as a whole. `g` for a taxon mismatch (a wider or narrower group, one species or a few standing for a group, a relative) and for a value the paper predicts or presumes rather than measures. `i` only for a value you derive yourself; the measured value goes in as its own record.
- Check every record's quote against the file before you commit: `python3 -I tools/views/quotecheck.py <file.pdf or file.txt> records.jsonl`. For an XML full text, save its text as a .txt file first. Correct or drop each record that fails.
- For each paper you read in full, write one line in `docs/views/sources/oa-k.jsonl`: `{"doi": "...", "title": "<the title exactly as your batch gives it>", "url": "<the free copy>", "records": 3, "read": "oa-k 2026-10-14"}`. Write the line even when the paper holds no measurement (`"records": 0`), because it tells the owner's page to stop asking for that paper.
- For each paper with no free copy, write one line in `docs/views/sources/oa-none-k.jsonl`: `{"doi": "...", "title": "...", "skipped": "no free copy", "checked": ["openalex", "europepmc", "semanticscholar"], "date": "2026-10-14"}`.
- When the only free text is an abstract that states a value, log that value with `"partial": true` and `"access": "abstract"`, and count the paper as having no free copy.

## Rules that matter more than speed
- Never write a value, DOI, quote or URL from memory. If you did not retrieve it in this task, it does not go in.
- Never commit a PDF, an XML file or any paper's text. The repository is public and the papers are under copyright.
- Do not edit any other file.
- Commit as you go. At the end, write a short summary to `docs/tracks/progress/oa-k.md` (papers checked, free copies found, papers read, records logged, papers with no free copy) and commit it. The owner opens a pull request from your task, and the research desk checks a sample of your records before merging.
