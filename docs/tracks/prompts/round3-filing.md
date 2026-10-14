# Round 3: filing the UNPROCESSED folder (Sonnet, local)

Your launch prompt gives the Drive ids of the UNPROCESSED folder, the papers folder and its subfolders, the page's address and the scratch directory. Never write a Drive id into the repository or into any file under it. You write no repository files; your record is the manifest in the scratch directory.

For every file in UNPROCESSED (list with `search_files` and `parentId`, `pageSize` 100, following `nextPageToken` until it ends):
1. Identify it. Download with `download_file_content` (files up to 10 MB), decode the base64 into the scratch directory, run `pdftotext -f 1 -l 2 -layout`, and read the title, authors, year and DOI from the text, never from the file name. A file over 10 MB is identified by its file name and flagged "over 10 MB".
2. Match it to a line of `docs/views/wanted-merged.csv` by DOI, or by first author, year and title words. A match gives the page id: the first 10 hex characters of the SHA-1 of the lowercased DOI, or of "title:" plus the normalised title when there is no DOI (function `pid` in `tools/views/papers_page.py`).
3. Rename with `update_file` (title only) to "Surname Year Short title.pdf": first author's surname, the year, three to six words of title. A printed web page with an abstract and reference list only gets " (partial)" before ".pdf".
4. Move with `update_file` (`parentId`) to its folder: Spiders, Insects, Birds, General and methods, Books, or the top level of the papers folder for mammals, herps, fish and everything else. A file that matches nothing is still renamed from its own metadata and filed by topic.
5. Keep a manifest line in `MANIFEST.jsonl` in the scratch directory for each file: `{"drive_id": "...", "new_title": "...", "folder": "...", "doi": "...", "page_id": "..." or null, "wanted_unit": "..." or null, "partial": false, "text": "<path of the extracted text>"}`.
6. At the end, set the marks in one call: read `ticks/all` (ArtifactData get), then `update` with `{page_id: true}` for every matched id that is not already marked, or `"partial"` for a partial file. Never change an existing mark, never set `na`.

Rules: never delete or trash a file. A file that cannot be identified, is not a paper (an editorial board page, say), or is a duplicate of a paper already filed (same title and size as a file you filed, or a copy with " (1)" in its name) stays in UNPROCESSED and goes on the short list `LEFT.md` in the scratch directory. Final message, at most 120 words: filed, new folders made, left behind, and how many matched the wanted list.
