# Audit 111: desk-d21 (3 evidence records; branch origin/research/desk-d21, head ce8f5fff)

## Lines judged

No sample was drawn. The launch prompt asks for the whole unit, so error lines can simply be dropped.
- Evidence records: all 3 lines of docs/views/evidence/desk-d21.jsonl.
- Search records: none (the unit has no searched file).
- Wanted lines: none (the unit has no wanted file).
- Leads the unit left alone: 4 spot-checked from its progress file (Platanus occidentalis, Medicago sativa, Rumex acetosella, Silybum marianum).

## Gate

The unit has no searched or wanted file, so `screen_candidates.py --check` has nothing to check. All 3 evidence lines parse as JSON. Quote lengths: 118, 61 and 90 characters.

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings included), the counting rule of audit 39, the rulings of audits 84 and 86 to 90, the taxon rulings of audits 86, 88 and 94, and audit 110 as format. For each record I ran a title WebSearch, fetched a URL that search returned, and compared authors, year, journal, DOI, quote, value, trait, grade and partial flag. Names were checked on POWO pages my searches returned. I checked origin/main (31ff0bf5) docs/views/evidence, docs/views/searched and docs/views/gaps/queue.jsonl for every genus.

Searches: 9 WebSearches. I fetched only URLs my searches returned. The WFO page for Ficaria verna (wfo-0000687184) failed at its site (robots), the Taylor and Francis abstract page and the Wiley Journal of Ecology page failed at their sites, and the Kew repository page gave a server error; none was retried. ResearchGate results (Prokop et al. 2025, the Ficaria nomenclature paper, a sheep sorrel germination paper) and an academia.edu result were left alone. No Sci-Hub, LibGen or proxy page was opened, and no paper text is committed.

## Evidence verdicts (3)

| Line | Record | Verdict |
|---|---|---|
| 1 | Ficaria verna diel (Prokop, Provazník, Tučník 2025, Plants 14(10): 1437, 10.3390/plants14101437) | **error (taxon).** The MDPI page (opened) confirms the three authors in order, volume, issue, article number and DOI, the quote word for word as one whole abstract sentence (118 characters), the Trnava site, 4 to 24 April 2021, daytime 4 to 17 C and night -2 to 6 C, and marked flowers on field plants with wire treatments; it gives no opening hour, as the note says. The value, method and conditions hold, and closure at night and in cloud is flower timing under the owner's diel reading (audit 110, Geranium pratense). But POWO (opened) says of Ficaria Guett. "This name is a synonym of Ranunculus", and its page for Ranunculus ficaria L. (urn:lsid:ipni.org:names:712703-1, opened) says "This species is accepted" with Ficaria verna Huds. as a homotypic synonym. The queue carries Ranunculus as its own genus (Ranunculus repens, R. acris, R. abortivus rows), so under the audit 86 (Ageratina), 88 (Mahonia aquifolium, an evidence record counted as an error although the queue lists Mahonia) and 94 (Hexastylis) rulings the record is filed under a synonym's genus. The note states the POWO synonymy itself. Repeats: main holds no Ficaria or Ranunculus diel evidence, so refiling as Ranunculus ficaria repeats nothing. Main's null records harvest-9:53 and sweep-5:25 (Ficaria diel) are contradicted by the measurement, main's fault, not counted. |
| 2 | Primula vulgaris sense_light_nonvisual (Marin, Blandino, Laverack, Toorop, Powell 2019, Plant Biology 21(3): 439-448, 10.1111/plb.12849) | **ok.** The Aberdeen research portal page (opened) confirms authors in order, journal, volume, issue, pages, year and DOI, and the quote word for word as one whole sentence (61 characters). Four maternal shading treatments over two seasons, seven light and five temperature treatments, and "maternal light conditions did not affect germination" support the value's "whatever the shade of the maternal plants". A germination light-quality trial on living seed is sense_light_nonvisual. Abstract only, `partial` true, grade m. Main holds Primula vulgaris diel only (oa-13b:136, 137, bioelectric rhythm) and P. veris sense_light_nonvisual, so no repeat; the queue still lists P. vulgaris sense_light_nonvisual as open (queue line 1833). |
| 3 | Comarum palustre sense_light_nonvisual (Heide, Sønsteby 2015, J Hortic Sci Biotechnol 90(3): 235-244, 10.1080/14620316.2015.11513177) | **ok.** The NIBIO Brage record (opened) confirms journal, volume, issue, pages, year and DOI, and the quote word for word as one whole abstract sentence (90 characters); it also gives two Norwegian populations, 10 h short days stopping growth with semi-dormancy at 9 to 21 C, and the 24 h long-day result, so the value holds. The page I read printed no author names; the title search returned the paper for "Heide Sønsteby", which I count as support but not as an opened byline. Trait: desk-screen.md 10(e) names photoperiod among germination and dormancy measurements of sense_light_nonvisual, and main files many set-photoperiod trials under that trait (audit 39 confirmed Veratrum californicum at 12, 14 and 16 h), so a controlled day-length trial on living plants belongs here and is inside the owner's reading. Name: Wikipedia (opened) gives Comarum palustre L. with Potentilla palustris (L.) Scop. as a synonym; the record cites POWO 63773-2 as accepting Comarum palustre, which I did not re-open, and the queue carries Comarum as the genus. Main holds no Comarum evidence; main's null sweep-29:25 (Comarum, four traits) is contradicted, main's fault, not counted. Abstract only, `partial` true, grade m. |

Fork on line 1. If the owner keeps Ficaria as a queue genus despite POWO (as main's Ficaria search records and queue rows do, and as audit 88 counted Mahonia search records ok), line 1 stands and evidence is 0 of 3. I count it an error because every evidence record filed under a POWO synonym's genus in audits 86, 88 and 94 was counted so, and the record's own note concedes the synonymy. The fix is to refile it as Ranunculus ficaria (genus Ranunculus), which changes no value.

## Leads left alone (4 spot-checked, not counted)

| Lead | Unit's reason | My check |
|---|---|---|
| Platanus occidentalis (Sperry, Chaney 1999, J Arboric 25(1): 43-47, lead 1384) | every sycamore sentence over 125 characters | **Confirmed.** The joa.isa-arbor.com PDF (opened): the abstract's sycamore sentence runs 134 characters and the two Results sentences 139 and 141. The only shorter sentences naming sycamore are the Figure 2 and 3 captions (102 and 79 characters), which say what was plotted and state no result. The reason is right. |
| Medicago sativa HIPV (Zakir et al. 2013, lead 1736) | abstract names no plant species | **Substance confirmed, wording loose.** The Journal of Ecology page failed; the journal's blog post (opened) names cotton, alfalfa and clover and says the measurement was Spodoptera littoralis egg-laying on undamaged plants near damaged cotton. That is moth behaviour, not a response of alfalfa, so leaving it is right, though alfalfa is named by its common name. |
| Rumex acetosella (leads 1749 to 1757) | papers are on Rumex confertus | **Confirmed.** The plant-1 wanted lines on main carry the Piesik et al. R. confertus volatile papers and Kołodziejek and Patykowski 2015 (R. confertus germination). Pointer, not counted: my search returned a title "Factors affecting seed germination and seedling emergence of sheep sorrel (Rumex acetosella)" only on ResearchGate (left alone); the R. acetosella sense_light_nonvisual cell is open on the queue (line 1231). |
| Silybum marianum (lead 1956) | cell already closed on main (sweep-21) | **Confirmed.** sweep-21 holds a Silybum marianum sense_light_nonvisual record ("seed germination is affected by light"). |

## Counts

- Search records: 0 of 0.
- Evidence: 1 of 3 (line 1, taxon).
- Unit: 1 of 3, 33.3%.

Pooled with audits 83 to 90, from audit 110's figures (search records 48 in 1026; with evidence 52 in 1095):
- Search records: 48 in 1026, 4.7% (unchanged).
- With evidence included: 53 in 1098, 4.8%.

**Verdict: fail as filed, pass once line 1 is dropped or refiled.** Lines 2 and 3 can merge as they are.

**Error lines to drop:**
- docs/views/evidence/desk-d21.jsonl: line 1 (Ficaria verna diel; refile as Ranunculus ficaria, genus Ranunculus, if the desk follows POWO).

Follow-ups:
- Line 3: the authors' names were not read on an opened page; check the byline on the Brage full record or the publisher page.
- Main's null records now contradicted: harvest-9:53 and sweep-5:25 (Ficaria diel), sweep-29:25 (Comarum). These should be re-opened when the lines land.
- If the desk follows POWO, the queue's Ficaria verna rows (lines 86, 446 to 448) and main's Ficaria search records (harvest-9:53, sweep-5:25, desk-c12:2) belong under Ranunculus.
- Rumex acetosella sense_light_nonvisual: find an open copy of the sheep sorrel germination paper (not via ResearchGate).
