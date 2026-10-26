# harvest-c22b (desk screening, plant genera; 26 October 2026)

Branch research/harvest-c22b, cut from origin/main 823ea417. This unit takes the 26 genera that harvest-c22 left (docs/tracks/batches/harvest-c22.json, Nereocystis to Physocarpus), screened under docs/tracks/prompts/desk-screen.md points 1 to 10 and the plant paragraph of round4-harvest.md, after reading audits 79 and 80. Files: docs/views/searched/harvest-c22b.jsonl and docs/views/wanted/harvest-c22b.jsonl. No evidence records. Gate: `screen_candidates.py --check` prints 0 problems before every commit.

## Method

OpenAlex refused this machine (proxy 403 on api.openalex.org), so no OpenAlex step ran here. Genera in no harvest run hold web searches only and say so; genera in a harvest run list the harvest's queries word for word, then the web searches, and name every screen candidate in `screened`. Search words: diel "flower opening time anthesis" (scientific and common name; for the kelps and Huperzia, which have no flowers, the nearest timed event); eye_type "plant ocelli lens-like epidermal cells focusing light" (both names); sense_chemical "<Genus> jasmonate OR elicitor OR hormone response", plus "<Genus> floral scent volatiles" for insect-pollinated flowers; sense_light_nonvisual "<Genus> light intensity OR shade OR photoperiod growth" (point 10e). Results were judged by title (the search tool returned no snippets) and nothing was opened. A trait whose searches showed a work that may hold a measurement for a species of the genus stays out of the record and the work goes on the wanted list (point 3); hormone and elicitor responses (10d), light-intensity growth or germination trials (10d) and living volatile emission (10a) all count. A trait with evidence on main gets no record.

## Genera

| Genus | Records | Left out, and why |
|---|---|---|
| Nereocystis | diel, eye_type | sense_chemical: two lamoxirene sperm-release works (10.2307/1543327; 10.1515/znc-1984-0629) on the wanted list. sense_light_nonvisual: evidence on main (sweep-46:6). |
| Croton | eye_type | sense_chemical: University of Johannesburg record on volatiles of African Croton species (living or distilled not seen). sense_light_nonvisual: Revista Arvore 2003 shade study (SciELO). diel: evidence on main (sweep-46:7). |
| Scirpus | diel, eye_type, sense_chemical | sense_light_nonvisual: evidence on main (sweep-46:9). |
| Huperzia | eye_type, sense_chemical | sense_light_nonvisual: Bulletin of Botanical Research 2009 29(4): 411 and Jishou University journal 2016 (10.3969/j.cnki.jdxb.2016.01.015). diel: Frontiers in Plant Science 10.3389/fpls.2023.1226027, returned for both diel searches. |
