# Audit 113: desk-d22 (4 evidence records; branch origin/research/desk-d22, head f9816bd9)

## Lines judged

No sample was drawn. The launch prompt asks for the whole unit, so error lines can simply be dropped.
- Evidence records: all 4 lines of docs/views/evidence/desk-d22.jsonl.
- Search records: none. The unit's first commit (713005c1) wrote 3 eye_type nulls (Hemerocallis, Chromolaena, Cichorium) in docs/views/searched/desk-d22.jsonl; the head commit (f9816bd9) deletes all 3 lines, and the file is absent from the branch tree at f9816bd9. No eye_type line remains in any unit file. Main already holds eye_type search records for all three (desk-d4 plus sweep-42 or sweep-5), so the withdrawal was right.
- Wanted lines: none (the unit has no wanted file).
- Skips: Chamaenerion, Asparagus, and 4 of the lead-held genera (Cerastium, Lotus, Castilleja, Urtica).

## Gate

No searched or wanted file, so `screen_candidates.py --check` has nothing to check. All 4 evidence lines parse as JSON. Quote lengths: 121, 119, 102 and 123 characters, each within 125.

## Method

Judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e)), audit 39's counting rule, the rulings in the shared brief (owner's readings: plant sense_chemical counts living responses and volatile signalling only; no extracts, oils, processed tissue, or cut-flower or cut-branch sampling), and audits 109 and 112 as format. For each record I ran a title WebSearch, fetched URLs that search returned, and compared authors, year, journal, DOI, quote, value, method, grade and partial flag. I checked origin/main (2a88029c) docs/views/evidence and docs/views/searched for the three taxa and the four DOIs. 9 WebSearches. The PMC copy of Fatelnig et al. (PMC12764683) returned a bot check and was not retried; the Royal Holloway portal page was read instead. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text is committed.

## Evidence verdicts (4)

| Line | Record | Verdict |
|---|---|---|
| 1 | Pinus sylvestris sense_chemical (Hilker, Kobs, Varama and Schrank 2002, J Exp Biol 205(4): 455-461, 10.1242/jeb.205.4.455) | **error: outside the owner's reading (cut-branch sampling).** The Silverchair copy (opened) has the quote verbatim as the first sentence of Results, and 22 to 30 parasitoid females per treatment matches. But the Methods give detached twigs throughout: twigs from 30- to 40-year-old trees were cut several days beforehand and kept in tap water, sawflies laid eggs on those cut twigs in boxes for 72 h, and jasmonic acid was fed for 72 h through the cut stem. No living, rooted plant was treated or sampled. The brief's binding reading excludes cut-branch sampling, and the record's note itself concedes the twigs were cut. Authors and DOI were not shown on the page and rest on main's Crossref wanted line (harvest-c13:6); the title matches. The Pinus sylvestris sense_chemical cell is still filled by line 2. |
| 2 | Pinus sylvestris sense_chemical (Lundborg, Nordlander, Björklund, Nordenhem and Borg-Karlson 2016, 10.1007/s10886-016-0790-z) | ok. PMC5148791 (opened): J Chem Ecol 42(12): 1237-1246; authors and DOI match. The quote is verbatim, a whole Discussion sentence. One-year-old container seedlings sprayed with 5, 10 or 25 mM emulsified MeJA in 2.5% ethanol: matches. The page reports increased (-)-beta-pinene in phloem for both species (P = 0.002). A living seedling's response to an elicitor counts under 10(d). Not counted: the page states the journal, which the record says it does not and leaves out; "greenhouse" in `conditions` is not on the page I read. |
| 3 | Salix cinerea sense_chemical (Mrazova and Sam, Arthropod-Plant Interactions 12(1): 1-8, 10.1007/s11829-017-9558-9) | ok. Springer page (opened): authors, DOI, online 19 August 2017 and issue 12(1) 2018 match; the quote is verbatim in the abstract; treated shrubs emitted significantly more alpha-pinene, beta-pinene, 3-carene, limonene and beta-ocimene, and birds pecked artificial caterpillars on treated shrubs more often. Field MeJA spray on living shrubs counts under 10(d). Grade m and partial are right. Wording to fix, not counted: "shrubs ... were pecked more by birds" should say the caterpillars on them were pecked more. POWO 301107-2 (opened) accepts Salix cinerea L. |
| 4 | Daucus carota sense_chemical (Fatelnig et al. 2026, Planta 263: 35, 10.1007/s00425-025-04900-0) | ok. Royal Holloway portal (opened): the 12 authors as listed, Planta 263 article 35, online 12 December 2025, issue 3 January 2026, and the DOI match; the quote is verbatim in the abstract (123 characters); priming with gibberellins and ABA, and ABA priming raising the wet-ageing resilience of carrot and parsnip mericarps, match. Living seed responding to applied hormones counts under 10(d). The quote pools carrot and parsnip; the ABA-ageing sentence names carrot, so m stands; partial is right. |

Repeats of main: none. Main holds no sense_chemical evidence for Pinus sylvestris, Salix cinerea or Daucus carota (Pinus sylvestris has only the phytochrome-count lines canon-3:538 and oa-2:4119; Daucus carota only the sense_light_nonvisual day-length lines sweep-5:14 and recheck-17-fixed:5), and none of the four DOIs is in any evidence file on main. Desk-d20's Daucus carota MeJA line (Wang et al. 2024, 10.3389/fpls.2024.1467957), which audit 109 failed for the mM/μM dose fault, was dropped and is not on main; line 4 is a different paper and a different treatment, so it neither repeats nor contradicts it. Lines 1 and 2 share a cell but are different papers and treatments.

Names: Pinus sylvestris L., Salix cinerea L. and Daucus carota L. are accepted species of accepted genera (Salix cinerea on POWO 301107-2, opened; the other two are already filed under these names on main and my POWO search returned the Daucus carota pages; none is a synonym of another genus).

## Skips

| Genus | Unit's reason | Verdict |
|---|---|---|
| Chamaenerion | harvest failed | confirmed. harvest_get prints "error gave up" for all three queries and the citation step (run 2); point 6 bars a record. |
| Asparagus | no open trait | confirmed. harvest_get prints "open traits: " (empty), run 6. |
| Cerastium | open cell held by a lead | confirmed. Open trait sense_light_nonvisual; main's wanted holds desk-c12 lines for it (Cerastium regelii flowering and morphology), and searched records exist (desk-c12, sweep-23). |
| Lotus | held by a lead | confirmed. Lotus is in no harvest run; harvest-c13 wanted holds the L. japonicus LED cultivation and shoot-applied MeJA nodulation leads. |
| Castilleja | held by a lead | confirmed for sense_chemical (six harvest-c12 wanted lines naming sense_chemical, e.g. haustoria induction, alkaloid uptake). |
| Urtica | held by a lead | confirmed. Open trait sense_chemical; harvest-c12 wanted holds the herbivore-induced trichome density and IAA sulfonation leads. |

## Counts

- Search records: 0 of 0.
- Evidence: 1 of 4.
- Unit: 1 of 4, 25%.

Pooled with audits 83 to 90, from audit 112's figures (search records 48 in 1026; with evidence 53 in 1100):
- Search records: 48 in 1026, 4.7% (unchanged).
- With evidence included: 54 in 1104, 4.9%.

**Verdict: fail** (evidence 1 of 4, above 5%). Lines 2 to 4 stand and can merge.

**Error lines to drop:**
- docs/views/evidence/desk-d22.jsonl: line 1 (Hilker et al. 2002, cut twigs).

Follow-ups:
- Line 2: add "Journal of Chemical Ecology 42(12): 1237-1246" and drop "greenhouse" unless the Methods state it.
- Line 3: reword the bird result as pecking on artificial caterpillars on treated shrubs.
- The Hilker 2002 wanted lead (harvest-c13:6) should be closed as read and out of reading (cut twigs), so no later unit reopens it.
