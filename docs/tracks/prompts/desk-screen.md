# Desk screening round (18 October 2026, after audits 40 to 42)

Audits 40, 41 and 42 failed the desk's screening batches harvest-26, -27 and -28 at 9 errors in 57 records pooled. Six of the nine errors were measurements the record called absent: three sat in the harvest output under a title the agent passed over (Digby and Firn 2002 on Tradescantia; Olsson et al. 2021 on Cuculus, on the record's own wanted list and already on main), and three were absent from the harvest output (Munir 2015, Desai 2018, Mann 1942). This round closes both gaps.

For each genus in your launch prompt:
1. `python3 -I tools/views/harvest_get.py <Genus>` prints the harvest's queries and works; `python3 -I tools/views/screen_candidates.py <Genus>` lists, per open trait, every harvest work whose title or abstract holds a word of that trait, and any evidence for the genus and trait already on main.
2. For each open trait, two web searches (THOROUGH.md step b): "<Genus> <trait words>" and "<common name> <trait words>". Read the first 20 result titles and snippets. List them in `queries` prefixed "web: ", after the harvest's queries copied word for word.
3. Fetch nothing (WebFetch of harvest URLs waits on a permission request nobody answers; the control room's `oa` job fetches free copies on build machines). A work that may hold a measurement of the trait for a species of the genus goes on the wanted list, and the trait stays out of the search record.
4. A search record for a trait names every candidate the tool listed for that trait in `"screened": {"<doi or OpenAlex id>": "<why it holds no measurement of the trait>"}`. A trait with evidence already on main gets no search record.
5. Before every commit: `python3 -I tools/views/screen_candidates.py --check docs/views/searched/<unit>.jsonl --wanted docs/views/wanted/<unit>.jsonl` must print "0 problems".
Write no evidence records in this round; readers log evidence from the oa job's texts with `quotecheck.py`.
