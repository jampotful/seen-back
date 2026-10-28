# Audit 123: desk-d34 (lead-reading unit, 2 evidence records; branch origin/research/desk-d34, head 02289b7e)

## Lines judged

No sample was drawn. The unit is judged whole, so that error lines can simply be dropped.
- Evidence records: both lines of docs/views/evidence/desk-d34.jsonl (1 and 2).
- Search records: none in the unit. Wanted lines: none.

## Gate

The unit has no searched or wanted file, so `screen_candidates.py --check` has nothing to run on. The quote (both lines) is 87 characters, measured by script, and is one whole sentence.

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's reading 10(d): germination light/dark trials count under sense_light_nonvisual, and a no-effect result is a measurement), the counting rule of audit 39, and the format of audit 122.
- 14 WebSearches; I fetched only URLs those searches (or a fetch's redirect) returned.
- Main. I checked origin/main (4a0c8102) docs/views/evidence/*.jsonl for Apocynum. Main holds desk-c11 line 5, Apocynum venetum sense_light_nonvisual, from the same paper (Jiang et al. 2021, 10.3389/fpls.2021.671157) with the same quote, filed abstract-only (partial: true). Main also holds A. cannabinum and A. androsaemifolium (desk-d13 lines 5 and 6), not A. pictum.
- No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened. No paper text is committed.

## Source check (both lines)

- Citation. The Frontiers endNote record (opened) gives Li Jiang, Chaowen She, Changyan Tian, Mohsin Tanveer, Lei Wang; Frontiers in Plant Science 12: 671157, 2021 (published 17 June 2021); DOI 10.3389/fpls.2021.671157. The record's authors, year, journal, volume, article number and DOI match.
- Quote. The PMC copy (www.ncbi.nlm.nih.gov/pmc/articles/PMC8248540/, opened) has "Light did not affect seed germination of A. venetum and A. pictum under any conditions." verbatim in the Abstract, as the record's `where` says. The Results sentence ("Light condition did not significantly affect seed germination for both Apocynum species under all test temperature regimes", longer than the quote) and the Discussion carry the same finding, so the abstract sentence states the study's own result.
- Value and conditions. Methods: freshly matured seeds and seeds stored 1 or 2 years, germinated in light (12 h darkness/12 h light) and in continuous darkness (dishes wrapped in two layers of aluminum foil), at 5/15, 5/20, 10/25, 15/30 and 20/35 C, checked daily for 15 days; light intensity and source not reported. All match. One wording point, not counted: the dark dishes were checked only at the end of the experiment, so "checked daily for 15 days" holds for the light dishes only (main's desk-c11 note says so; this record's `method` does not).
- Trait. A light against darkness germination trial, with a no-effect result, is sense_light_nonvisual under 10(d). Grade m is right (each species named and measured). Full text read, so partial: false stands.
- Names. POWO 77279-1 (opened): Apocynum venetum L., "This species is accepted". POWO 77225-1 (opened): Apocynum pictum Schrenk, "This species is accepted". The genus is not filed under a synonym.

## Evidence record verdicts (2)

| Line | Record | Verdict |
|---|---|---|
| 1 | Apocynum venetum sense_light_nonvisual | **error: repeats evidence on main.** Source, quote, taxon and trait are identical to docs/views/evidence/desk-c11.jsonl line 5 (merged after audit 88). The values agree, so nothing is contradicted, but the line adds a second record of one measurement. If the desk wants the full-text reading (Methods detail, partial false) it should replace desk-c11 line 5 rather than add this line. |
| 2 | Apocynum pictum sense_light_nonvisual | ok. Quote verbatim and whole in the Abstract, citation matches, value and conditions match the Methods and Results, trait and grade right, POWO accepts the name, and main has no A. pictum record. |

**Evidence errors: 1 of 2 (50%), line 1.**

## Open item: Lonicera insularis

- WFO (list.worldfloraonline.org/wfo-0000359595, opened) gives Lonicera morrowii as accepted and lists Lonicera insularis among its synonyms.
- POWO: not settled. POWO's Lonicera morrowii A.Gray page (urn:lsid:ipni.org:names:148944-1, opened) says "This species is accepted" but its homotypic and heterotypic synonym sections rendered empty, as the unit found. No POWO page for the name Lonicera insularis turned up in three searches; one unnamed POWO result (urn:lsid:ipni.org:names:149153-1) failed at its site, and the others I opened were other names (L. affinis, L. emphyllocalyx; Xylosteon morrowii, "This name is a synonym of Lonicera morrowii").
- So WFO treats L. insularis as a synonym of L. morrowii, and I could not read POWO's ruling. If a later unit confirms POWO agrees, the Lee et al. 2024 sentence would be filed under Lonicera morrowii with a note. No record filed.

## Counts

- Search records: none in this unit.
- Evidence: 1 of 2, 50%.
- Unit: 1 of 2, 50%.

Pooled with audits 83 to 90, from audit 90's figures as written (48 in 1026 search records; 52 in 1090 with evidence), as audit 122 did:
- Search records: 48 in 1026, 4.7% (unchanged).
- With evidence included: 53 in 1092, 4.9%.

**Verdict: fail (evidence 50%, on a repeat).** The unit was judged whole, so drop line 1 and line 2 stands.

**Error lines to drop:**
- docs/views/evidence/desk-d34.jsonl: line 1 (Apocynum venetum sense_light_nonvisual; repeats desk-c11 line 5).

## Pages opened

- www.ncbi.nlm.nih.gov/pmc/articles/PMC8248540/ (twice); www.frontiersin.org/articles/10.3389/fpls.2021.671157/endNote.
- POWO 77279-1, 77225-1, 148594-1, urn 148944-1, urn 269961-2, urn 148742-1; WFO wfo-0000359595; IPNI 895621-1, 148722-1.
- Refused or failed: pmc.ncbi.nlm.nih.gov/articles/PMC8248540 (browser check); public-pages-files-2025.frontiersin.org redirect of the Frontiers text page (permission not answered, not retried); POWO urn 149153-1 (failed at its site).
