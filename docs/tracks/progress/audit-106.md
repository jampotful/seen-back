# Audit 106: desk-d17 (plant genera; branch origin/research/desk-d17, head 91f824a7)

## Lines judged

No sample was drawn. The launch prompt asks for the whole unit, so that error lines can simply be dropped.
- Search records: all 4 lines of docs/views/searched/desk-d17.jsonl (1 to 4).
- Evidence records: none (docs/views/evidence/desk-d17.jsonl is absent on the branch).
- Wanted lines: 1, listed and not counted.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on copies of the searched file (4 lines) and the wanted file (1 line) prints "0 problems".

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e)), the counting rule of audit 39, and the rulings of audits 84, 86 to 90 and 94, with audit 90 as the format.

Queries. `harvest_get.py` (origin/ci, no network) prints "in no harvest run yet" for Coccoloba, Olea and Hexastylis. Every record lists "web: " lines only, and no unlabelled line appears. `harvest_get.py Asarum` shows Asarum (Aristolochiaceae) in harvest run 2 with sense_chemical its only open trait.

Chased. All four records give the none-reason "no measured relative and no family review found", and name no DOI, so nothing needs a supporting search. My "Oleaceae photoreceptor review" search returned PMC12428501 first, as line 2's note says. Audit 90 accepted 10.1007/s00239-004-0294-2 as a family review for Coccoloba, so line 1's "no family review found" undersells what its own note reports (it calls the PDF not family-specific). That is a wording weakness and is not counted.

Form of the eye_type nulls. Main files plant eye_type as a genus search record with `found` "none", the focusing works named in `screened` with the owner's reason (for example desk-c12:7, 10 and 11, desk-d4:1 to 3 and 6). Main has no plant eye_type evidence record; the eye_type evidence on main is animal (canon-3 and others). Lines 1 to 3 use the same form, and screen PMC9824129 and the Bonn thesis with the owner's wording. The form is right.

Main (origin/main 1e4ecb4d), per genus:
- Coccoloba: desk-c12:14 (light) and :15 (chemical) nulls, and the older multi-trait sweep-36:4. No eye_type record of the 27 October form, so line 1 fills an open cell. Its re-screen of sweep-36:4 is noted, not counted (audit 90).
- Olea: evidence for diel (desk-c12:8), light and chemical (sweep-41:4, 5); the 27 October eye_type record (desk-c12 line 18) was dropped by audit 90 for an unsupported chased. Line 2 rewrites it with a none-reason, as audit 90 suggested. The re-screen of sweep-41:5 is noted, not counted. No contradiction.
- Hexastylis: only the older sweep-47:21. Under Asarum, main holds sense_light_nonvisual evidence (sweep-19:5, recheck-6-fixed:8, A. heterotropoides), the eye_type/diel/light null harvest-18:3 and the sense_chemical null harvest-18:4.
- Hypoxis: sense_light_nonvisual (sweep-46:8) and sense_chemical (desk-d4:2) evidence, eye_type null desk-d4:6; no diel evidence. The unit writes no Hypoxis record, as it should.

Names. POWO (taxon 121846-2, opened) says Hexastylis arifolia "is a synonym of Asarum arifolium", as audit 94 found. Audit 94 counted desk-d4's Hexastylis records (eye_type, light, diel) as filed under a synonym's genus, and main dropped them. Coccoloba and Olea are accepted genera.

Searches. I ran 14 WebSearches: 1 for POWO status, 7 for Hexastylis sense_chemical (germination and GA3, herbivore and jasmonate, scent, congener dormancy, auxin and cytokinin propagation, Asarum arifolium germination), 2 pooled focusing searches for the eye_type records, 1 family review, 2 for the wanted line and Hypoxis diel, plus 1 follow-up. I fetched only URLs my own searches returned. Two www-cambridge-org.ezproxyberklee.flo.org results and a 0-www-mdpi-com.brum.beds.ac.uk result were left alone, and a proquest.com result was not opened. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text is committed.

## Search record verdicts (4)

| Line | Record | Verdict |
|---|---|---|
| 1 | Coccoloba eye_type | ok. Web-only, none-reason chased, main's form. My pooled focusing searches returned only the general set (PMC9824129, FIU cas_bio/44, Nature 075535b0, AskNature, PMC8309337) and Oleaceae leaf micromorphology; nothing on Coccoloba. Plant eye_type is "none" in any case. |
| 2 | Olea eye_type | ok. Web-only; the Oleaceae family search returns what the note says (PMC12428501, a light-quality trial already logged under light). My olive leaf-optics search returned PMC8309337 and trichome optics papers, none a focusing work on Olea. Repairs audit 90's dropped desk-c12:18 without contradicting main. |
| 3 | Hexastylis eye_type | **error: filed under a synonym's genus, and repeats main.** POWO treats Hexastylis arifolia as Asarum arifolium, and Asarum eye_type is already covered on main (harvest-18:3). Audit 94 dropped the identical desk-d4 record on this ground. My focusing searches found nothing either way. |
| 4 | Hexastylis sense_chemical | **error: filed under a synonym's genus.** Asarum sense_chemical already has a null on main (harvest-18:4), so this re-files the same cell under the synonym. My searches also returned Davis, Frett and Kitto 2014, "Establishment of microcuttings of Hexastylis species", Native Plants J 15(3): 247-254 (npj.uwpress.org abstract opened): in vitro-rooted microcuttings of H. arifolia, H. minor and H. speciosa cultured four weeks with IBA at 0, 2.5, 5 or 10 µM "survived transplanting equally well". That is a living plant's response (no difference) to an applied auxin, which 10(d) lists. The record searched germination, elicitor and scent phrasings only. Fork below. Nothing else turned up: germination searches returned Heptacodium, Nyssa and orchid work, scent searches orchid and bromeliad papers, herbivory searches slug and beech papers, and the Auburn Harper's ginger page (opened) only says seedlings were started. |

Search record errors: **2 of 4 (50%)**, lines 3 and 4.

## Evidence records

None in the unit. 0 of 0.

## Skipped genera (progress file claims)

Checked on origin/main:
- Cenchrus: eye_type null desk-c12:7; light evidence sweep-34:5; diel and sense_chemical leads in harvest-c12:139 to 149 and desk-c12:4 (wanted). Holds.
- Cerastium: diel, sense_chemical and eye_type nulls desk-c12:8 to 10; light leads desk-c12:5, 6 and harvest-c12:156 to 166 (wanted). Holds.
- Hemerocallis and Chromolaena: eye_type nulls desk-d4:1 and 2; their other traits carry evidence. Holds.
- Cyanthillium: diel, sense_chemical and eye_type nulls and light evidence on main. Holds.
- Carex: eye_type null desk-c12:11; diel, sense_chemical and light are closed by evidence (desk-c12:6, 7, oa-12:432, sweep-97:1, 2 and others), which is stronger than "carry leads". Holds.
- Coccoloba: light and chemical nulls desk-c12:14, 15; diel is held only by harvest-c12:138 (Trioecy in C. cereifera). Audit 90's Madriz and Ramírez 1996 lead (C. uvifera, opening 08:00 to 12:00) is not on main's wanted list. The skip is fair, but that lead should be logged.
- Hexastylis light and diel: held on main under Asarum (sweep-19:5 evidence; harvest-18:3 null), so no Hexastylis record was due. Holds.
- Hypoxis: as above. Holds.

## Counts

- Search records: 2 of 4, 50%.
- Evidence: 0 of 0.
- Unit: 2 of 4, 50%.

Pooled with audits 83 to 90, from audit 90's figures (search records 48 in 1026; with evidence 52 in 1090):
- Search records: 50 in 1030, 4.9%.
- With evidence included: 54 in 1094, 4.9%.

Forks that would change the count:
- If the desk accepts Hexastylis as a genus (GRIN and the Alabama checklist do; POWO does not), line 3 still repeats Asarum's closed eye_type cell in substance, and line 4 still misses Davis et al. 2014 if a no-difference auxin trial on microcuttings counts under 10(d). Audit 93 counted NAA on ivy cuttings, so I would still count line 4. Line 3 would then turn on the repeat alone.
- If the desk reads the IBA result as transplant survival rather than a hormone response, line 4 rests on the synonym ruling alone. Either way it is counted once.

**Verdict: fail.** 2 of the 4 search records are errors, both for the same reason audit 94 gave for desk-d4's Hexastylis lines. The whole unit was judged, so drop the error lines and the rest stands.

**Error lines to drop:**
- docs/views/searched/desk-d17.jsonl: lines 3 and 4. Asarum sense_chemical stays open under Asarum (harvest-18:4 is its null); Davis et al. 2014 is a candidate for it as Asarum arifolium.
- docs/views/evidence/desk-d17.jsonl: none (absent).

## Wanted lines (listed, not counted)

1. Ren, Bernhardt, Edens-Meier, Zweck, Arduser, Li and Wang 2019. The experts.umn.edu page (opened) confirms the title, all seven authors, Plant Syst Evol 305(2): 115-126 and DOI 10.1007/s00606-018-1556-6, and gives no hour of day in the abstract, as the line says. Fine.

## Leads

- Asarum arifolium (Hexastylis arifolia) sense_chemical: Davis, Frett and Kitto 2014, Native Plants J 15(3): 247-254 (IBA on microcuttings, no difference in survival).
- Hypoxis diel: audit 94's SANBI account of H. hemerocallidea ("The flowers are short-lived and close at midday", pza.sanbi.org/node/10428) still has no evidence line on main; it could close the cell ahead of the Ren et al. full text.
- Coccoloba uvifera diel: Madriz and Ramírez 1996, Rev Biol Trop 44(3A): 105-115 (audit 90), not yet on main's wanted list.

## Blocked pages

- None refused. Proxy results (ezproxyberklee.flo.org, brum.beds.ac.uk) and a proquest.com preview were left alone.
