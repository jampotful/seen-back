# Filing UNPROCESSED (Haiku, cloud agent)

You file the owner's new papers in Google Drive. A script decides everything; you only list, copy and carry out. Never write a Drive id into the repository, and never delete or trash a file. Your launch prompt gives the Drive ids of the UNPROCESSED folder, the papers folder and its subfolders.

1. List UNPROCESSED with `search_files` (`parentId = '<UNPROCESSED id>'`, `excludeContentSnippets: true`, `pageSize: 100`), following `nextPageToken` to the end. Keep each file once.
2. Write `/tmp/filing/listing.tsv`, one line per file: `<drive id><TAB><fileSize><TAB><title>`. Copy ids and titles exactly.
3. Run `python3 -I tools/views/file_plan.py /tmp/filing/listing.tsv /tmp/filing/plan.jsonl`.
4. For the files the plan calls `unknown`, fetch Drive's snippet five at a time: `search_files` with `parentId = '<UNPROCESSED id>' and (title = '<name 1>' or title = '<name 2>' ...)` and `snippetVerbosity: BRIEF` (escape a quote in a name as `\'`). Write `/tmp/filing/snippets.tsv`, one line per file: `<drive id><TAB><the first 500 characters of its snippet, with tabs and line breaks replaced by spaces>`. Run step 3 again with `--snippets /tmp/filing/snippets.tsv`.
5. Make any folder the plan names that does not exist yet (`create_file`, `mimeType` `application/vnd.google-apps.folder`, parent the papers folder): the topic folders, "Extras (not on the list)", "Not on the list" and "Duplicates".
6. Carry out the plan with `update_file`, ten calls per message: for `file` and `extra`, the new `title` and the folder as `parentId`; for `skip` and `duplicate`, the folder only. Leave `unknown` files where they are.
7. Append one line per moved file to `docs/views/sources/filed.jsonl`: `{"key": "<first 12 hex of the SHA-1 of the Drive id>", "action": "...", "page_id": "...", "name": "...", "folder": "...", "date": "YYYY-MM-DD"}`. Commit it to `main` and push.

Final message, at most 120 words: how many files were filed, set aside as extras, not on the list, duplicates and left unknown; the `page_id` of every file filed, comma-separated, so the desk can mark them on the page; and the script's line about papers marked saved with no file.
