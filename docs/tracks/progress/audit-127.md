# Audit 127: desk-d37 (lead-reading unit, 2 evidence records; branch origin/research/desk-d37, head f8147d9d)

## Lines judged

No sample was drawn. The unit is judged whole, so that error lines can simply be dropped.
- Evidence records: both lines of docs/views/evidence/desk-d37.jsonl (1 and 2).
- Search records: none in the unit. Wanted lines: none.

## Gate

The unit has no searched or wanted file, so `screen_candidates.py --check` has nothing to run on. Measured by script, the quotes are 84 characters (line 1) and 116 characters (line 2). Each is one whole sentence.

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's reading: germination light/dark responses and growth under set light levels count under sense_light_nonvisual), the counting rule of audit 39, and the format of audit 123.
- I ran 7 WebSearches. I fetched only URLs those searches returned.
- Main. I grepped origin/main (9ed39ed8) docs/views/evidence/*.jsonl, searched/*.jsonl and wanted/*.jsonl for Sarracenia and Ampelopsis.
  - Main's only Sarracenia evidence is sweep-21 line 10 (S. purpurea sense_chemical, pitcher volatiles), a different trait. Main has no Ampelopsis evidence. Neither line repeats or contradicts evidence on main.
  - Main does hold null search records for both cells: sweep-21 line 29 (Sarracenia, sense_light_nonvisual among four traits, "none in the first 20 titles") and sweep-21 line 5 (Ampelopsis, the same four traits, "none"). These two records now count as misses on main. They are not errors of this unit.
- No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened. No paper text is committed.

## Source checks

Line 1, Sarracenia purpurea (Gotsch and Ellison 1998):
- Citation. The Harvard Forest page harvardforest.fas.harvard.edu/print/1073 (opened) gives S. G. Gotsch and A. M. Ellison, 1998, "Seed germination of the northern pitcher plant, Sarracenia purpurea", Northeastern Naturalist 5(2): 175-182. The page shows no DOI. All of this matches the record, and so does the record's URL.
- Quote. Asked for an exact match, the page confirms that "Fewer than 10% of seeds germinated when placed in darkness following stratification." appears word for word, in the section labelled Abstract. It is a result sentence of the study.
- Value. The same abstract gives 85% germination in ambient sunlight after 6 weeks of stratification and 53% after 4 weeks, as the value and note say. The trial is light against darkness, which falls under sense_light_nonvisual. Grade m is right for the one named species. `partial: true` is right because the record rests on the abstract only.
- Conditions. "laboratory germination trial" is not stated on the page read, since the abstract says "ambient sunlight". This is a wording point and is not counted.
- Name. POWO 30030166-2 (opened) shows Sarracenia purpurea L., "This species is accepted". Sarracenia is its own genus.

Line 2, Ampelopsis glandulosa var. brevipedunculata (Frampton et al. 2018):
- Citation. The PDF www.purchase.edu/live/files/2330-frampton-valencia-and-zimmerman-2018pdf (opened) is the college's own site, which is the record's URL. It gives Leo Frampton, Paola Valencia and Alivia Zimmerman, Purchase College Journal of Ecology vol. 2, Fall 2018, pp. 17-25, with no issue number and no DOI. All of this matches the record.
  - The paper's title spells the epithet "brevipedunculate". The record writes "brevipedunculata". This is a transcription point and is not counted.
- Quote. The sentence appears verbatim in Results, under "Stem Growth". It is the study's own result.
- Value and conditions. Methods: cuttings were grown in an incubator at 26.7 C under set PAR levels of 86.7 (high), 15.1 (medium) and 2.4 (low) umol/s-m2. Those levels were compared with a 10 m PAR transect at a field patch. That is growth under set light levels, so sense_light_nonvisual fits. Grade m is right. `partial: false` is right because the full text was read.
  - The record could have given the PAR values. The note's statement that the text gives no per-treatment numbers is true of the prose.
- Name.
  - POWO 892748-1 (opened): Ampelopsis glandulosa var. brevipedunculata (Maxim.) Momiy., "This variety is accepted". Its synonym lists rendered empty.
  - POWO 67552-1 (opened): Cissus brevipedunculata Maxim., the basionym, a synonym. Its listed synonym is Ampelopsis brevipedunculata.
  - POWO 992606-1 (opened): A. heterophylla var. brevipedunculata is a synonym of A. glandulosa var. brevipedunculata.
  - WFO wfo-0000421409 (opened): A. glandulosa var. brevipedunculata is accepted, and lists Ampelopsis brevipedunculata among its synonyms.
  - The paper's name is therefore a homotypic synonym of the accepted variety, and the record files the right taxon. Ampelopsis is accepted. The segregate genus Nekemias, which holds the former A. arborea, does not take this taxon.

## Evidence record verdicts (2)

| Line | Record | Verdict |
|---|---|---|
| 1 | Sarracenia purpurea sense_light_nonvisual | ok. Quote verbatim, whole and 84 characters, from the abstract's result. Citation, value, trait, grade and partial flag all match. POWO accepts the name. No repeat of main. |
| 2 | Ampelopsis glandulosa var. brevipedunculata sense_light_nonvisual | ok. Quote verbatim, whole and 116 characters, in Results. Citation matches the college's PDF. The trial is growth at set PAR levels. The paper's A. brevipedunculata is a synonym of the POWO-accepted variety filed. No repeat of main. |

**Evidence errors: 0 of 2 (0%).**

## Counts

- Search records: none in this unit.
- Evidence: 0 of 2, 0%.
- Unit: 0 of 2, 0%.

Pooled with audits 83 to 90, from audit 90's figures as written (48 in 1026 search records; 52 in 1090 with evidence), as audits 122 and 123 did:
- Search records: 48 in 1026, 4.7% (unchanged).
- With evidence included: 52 in 1092, 4.8%.

**Verdict: pass.** Both lines stand.

**Error lines:** none in docs/views/evidence/desk-d37.jsonl.

Uncounted points to fix:
- Line 1: the conditions say "laboratory", but the abstract says ambient sunlight.
- Line 2: the title epithet is "brevipedunculate" in the source.
- Main: sweep-21 lines 5 and 29 are null records for these cells and should be updated.

## Pages opened

- harvardforest.fas.harvard.edu/print/1073 (twice).
- www.purchase.edu/live/files/2330-frampton-valencia-and-zimmerman-2018pdf.
- POWO 30030166-2, 892748-1, 67552-1, 992606-1 and 2634471-4.
- WFO wfo-0000421409.
- None refused.
