# Audit 120: desk-d31 (lead-reading unit; branch origin/research/desk-d31, head 30e4ef58)

## Lines judged

No sample was drawn. The launch prompt asks for the whole unit, so that error lines can simply be dropped.
- Search records: docs/views/searched/desk-d31.jsonl is empty (0 lines).
- Evidence records: all 5 lines of docs/views/evidence/desk-d31.jsonl.
- Wanted lines: the 1 line of docs/views/wanted/desk-d31.jsonl, listed and not counted.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on copies of the searched file (empty) and the wanted file (1 line) prints "0 problems". All 5 evidence lines parse. The quotes are whole sentences of 58, 96, 72, 87 and 105 characters, all within 125.

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e)), the counting rule of audit 39 and the brief's rulings (audits 84 and 86 to 90). Audits 90 and 119 served as format. `harvest_get.py` prints "in no harvest run yet" for Argentina, Erodium, Passiflora, Erechtites, Carica and Convallaria, so no `queries` comparison arises.

I ran 21 WebSearches and fetched only URLs those searches returned. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened. A www-cambridge-org.ezproxyberklee.flo.org hit in the Convallaria results was left alone. No paper text is committed.

Main. I checked origin/main (58dfef7f) docs/views/evidence/*.jsonl for every taxon in the unit.
- Argentina, Potentilla anserina, Erodium and Erechtites have no evidence on main.
- Passiflora holds P. pohlii sense_chemical and diel and P. foetida diel only, with no sense_light_nonvisual.
- Carica holds C. papaya sense_chemical (10.4025/actasciagron.v36i4.18057) only. The unit's light record does not repeat it, and the unit rightly dropped its Carica GA3 record.
- Convallaria holds C. majalis sense_chemical only.

No unit evidence line repeats or contradicts evidence on main. Line 1 does contradict a main *search* record: sweep-13.jsonl line 19 (Argentina, sense_light_nonvisual among its traits) found "none". That fault belongs to the main record, not to this unit (see Notes).

## Evidence verdicts (5)

| Line | Record | Verdict |
|---|---|---|
| 1 | Argentina anserina sense_light_nonvisual | ok. Source checks: the PLOS ONE article page (opened) holds the quote word for word, under the Discussion heading "Ramet specialisation in physiological features". IDEAS/RePEc (opened) gives Zhengwen Wang, Yuanheng Li, Heinjo J During and Linghao Li, PLOS ONE 6(9), 2011, DOI 10.1371/journal.pone.0025401, on Potentilla anserina. The page also gives the yard of the Duolun station and sunlight "up to 2000 µmol·m−2·s−1", as the record says. Classification: shade cloth over one ramet is a set-light-intensity trial under sense_light_nonvisual. Grade: m. Weak quote, as reported: "This" refers back to the preceding sentence, a literature finding that shaded plants put more nitrogen into light harvesting. The Discussion says the shaded ramets "were stimulated to produce more chlorophyll". The value's "change chlorophyll content" is right but could say "higher". The Table 1 shade percentages are not on the page, as the record says. |
| 2 | Erodium cicutarium sense_light_nonvisual | ok. Quote: the Dryad record (opened) gives author Tina Heger, Erodium cicutarium, and the quote word for word. Citation: a WebSearch result on besjournals.onlinelibrary.wiley.com is titled "Light availability experienced in the field affects ability of following generations to respond to shading in an annual grassland plant - Heger - 2016 - Journal of Ecology", at /doi/10.1111/1365-2745.12607. That confirms the authors, year, journal and DOI the record marks as unconfirmed. The Wiley page itself failed at its site, so the quote is confirmed on Dryad only, and "partial": true is right. Classification: a shade trial under sense_light_nonvisual. Grade: m. The journal field lacks the volume and pages (cosmetic). |
| 3 | Passiflora incarnata sense_light_nonvisual | ok. Quote: word for word on the SciELO abstract page and the ABRATES page (both opened). Citation: the SciELO full-text page gives Zucareli, Henrique and Ono, J Seed Sci 37(2): 162-167, 2015, DOI 10.1590/2317-1545v37n2147082. Classification: germination in light against dark under sense_light_nonvisual. Grade: m. The light and dark percentages sit in Table 1, an image, so the categorical value is right. The page range is missing (cosmetic). |
| 4 | Erechtites valerianifolius sense_chemical | ok. Quote: word for word on the Embrapa PAB page (opened). Citation: the same page gives Zayat and Ranal, Pesq Agropec Bras 32(11): 1205-1213, 1997, DOI 10.1590/S1678-3921.pab1997.v32.4770, on Erechtites valerianaefolia DC. The page states no KNO3 concentration, so "concentration not read" is honest. Classification: KNO3 on living seed counts under sense_chemical (10(d) and 10(e); audit 88). Grade: m. Taxon: POWO 93323-2 (opened) says "This name is a synonym of Erechtites valerianifolius", so the name is accepted. |
| 5 | Carica papaya sense_light_nonvisual | ok. Quote: word for word in the RESUMO of the Redalyc PDF (opened). Irradiance: 60, 130, 580 and "1.200" mmol m⁻² s⁻¹, printed as mmol, so the units are copied exactly. Citation: DOAJ (opened) gives Mengarda, Lopes and Buffon, Pesq Agropec Trop 44(3): 325-333, 2014, DOI 10.1590/S1983-40632014000300012. The record writes "s1983" in lower case, which is the same DOI (case-insensitive). Classification: a set-irradiance trial under sense_light_nonvisual. Grade: m. Taxon: POWO 47494-2 (opened) says "This name is a synonym of Carica papaya". |

Genus status:
- POWO pages opened: Erodium cicutarium (L.) L'Hér. (372219-1) and Passiflora incarnata L. (675096-1) both read "This species is accepted".
- Argentina anserina is accepted per the launch prompt, which agrees with the record's note.
- No record is filed under a synonym's genus.

Evidence errors: **0 of 5 (0%)**.

## Wanted line (listed, not counted)

- Line 1 (Kondo et al. 2015). The UKY Scholars page (opened) gives:
  - title as in the line;
  - authors Tetsuya Kondo, Mizuki Narita, Shyam S. Phartyal, Siti N. Hidayati, Jeffrey L. Walck, Jerry M. Baskin and Carol C. Baskin;
  - Seed Science Research 25(2): 210-220, 2015;
  - DOI 10.1017/S0960258515000136.

  All of these match the line. POWO 77271793-1 (opened) gives Convallaria majalis var. keiskei as "a synonym of Convallaria keiskei", which supports the line's acceptance claim. No fault.

## Rates

Unit: search records 0 in 0; evidence 0 in 5; together 0 in 5.

Pooled with the running totals carried by audit 119 (search records 56 in 1084; with evidence 65 in 1181), a chain through audits 83 to 90 and on to 119:
- Search records: 56 in 1084, 5.17% (unchanged).
- With evidence included: 65 in 1186, 5.48%.

**Verdict: pass** (evidence 0 of 5; no search records). All five evidence lines and the wanted line can merge.

**Error lines to drop:** none.
- docs/views/searched/desk-d31.jsonl: none (file empty).
- docs/views/evidence/desk-d31.jsonl: none.

## Notes (not counted)

- Main search record sweep-13.jsonl line 19 (Argentina, "diel; eye_type; sense_chemical; sense_light_nonvisual") found "none" for sense_light_nonvisual. Wang et al. 2011 now measures a shade response in A. anserina. When line 1 merges, that search record's sense_light_nonvisual claim is superseded.
- Line 1's value could read "shaded ramets had higher chlorophyll content", as the Discussion says. Optional.
- Lines 2 and 3 could add the volume and pages: J Ecol (volume not read) and J Seed Sci 37(2): 162-167.

## Blocked pages

- pmc.ncbi.nlm.nih.gov PMC3184135: browser check, so I used journals.plos.org.
- mediatum.ub.tum.de 1354881: Anubis access denied.
- besjournals.onlinelibrary.wiley.com 10.1111/1365-2745.12607: failed at its site.
- POWO 47480-2: failed at its site.
- No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text was committed.
