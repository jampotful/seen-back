# Round 2: the Drive intake (Sonnet)

Start with `burst2-common.md`, then `docs/views/research/BRIEF.md` (the evidence log, the rules and "Round 2"). Your branch is `research/intake`. Your launch prompt gives the papers folder's Drive id; never write a Drive id into the repository. Stop after 75 minutes or when every new file is read.

1. List every file under the papers folder, subfolders included. A file is new when `docs/views/sources/drive.jsonl` on `main` and on your branch has no line whose `key` is the first 12 hexadecimal digits of the SHA-1 of its Drive id.
2. For each new file up to 10 MB: download it with `download_file_content`, decode it, run `pdftotext -layout`, find its DOI or title on the first pages and match it to the wanted lists (`docs/views/wanted/*.jsonl` on `main` and the `research/*` branches). Grep the text for the species in the matched line's `for` field and the traits behind its `rows` (or, for an unmatched file, the species and traits of the views it concerns), read only around the matches, and log records as the brief says, every quote checked against the text, in `docs/views/evidence/intake.jsonl` with `"unit": "intake"` and the wanted line's unit in `note`.
3. Add a line for each file to `docs/views/sources/drive.jsonl`: `{"key": "...", "title": "...", "doi": "...", "wanted_unit": "...", "records": 0, "read": "<date>"}`, or `"skipped": "over 10 MB; the owner can split it"`.
4. Push after every five files.

Final message, at most 200 words: files read, records logged, files skipped and why, and the last commit.

**Partial files.** A file whose name ends in "(partial)" is a printed web page with the abstract and reference list only. Read both. Log abstract-level evidence with the grade "abstract only", list the reference-list papers that bear on the views as new wanted lines (skipping any marked `n/a` in `docs/views/papers-status.jsonl`), and never ask for that paper again.
