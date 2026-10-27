# Audit 86: desk-c7 (12 plant genera; branch origin/research/desk-c7, head 79855def)

## Samples (seed 86), drawn before any record was read

Search records: the unit has 13, fewer than 20, so all are judged. `random.seed(86)` and `random.sample(range(1, 14), 13)` give the order 13, 1, 9, 6, 12, 2, 10, 5, 3, 4, 11, 7, 8.

Evidence records (18 lines in docs/views/evidence/desk-c7.jsonl): a second sample of 10, `random.seed(86)` and `random.sample(range(1, 19), 10)`: 1, 11, 18, 13, 2, 12, 9, 17, 5, 7.

## Gate

`python3 -I tools/views/screen_candidates.py --check` on the searched and wanted files (copied to /tmp) prints "0 problems".

## Method

Judged against desk-audit.md, desk-screen.md points 1 to 10 (the owner's readings in 10(a) to 10(e) included) and the rulings of audits 83 to 85, with the launch prompt's two rulings: an unlabelled direct OpenAlex query line in `queries` is waived (audit 84), and a `chased` DOI that no harvest output prints is an error unless otherwise supported.

`harvest_get.py` ran without the network (it reads origin/ci), so `queries` were judged against its output. A script compared each record's unprefixed `queries` with the `query` and `family review` lines the harvest prints for the genus. Serenoa, Nekemias and Mitchella (lines 3, 7, 10, 11) match word for word and in order, with "web: " lines after them. Gaillardia, Acer, Monarda, Taxodium and Eupatorium are in no harvest run; their records hold "web: " lines only. No harvest shows a failed step.

Chased. Lines 3, 7, 10 and 11 name the citation-step DOI the output prints (Serenoa's step returned 1 work, Nekemias's and Mitchella's 0, as the records say). The nine records for no-run genera (lines 1, 2, 4, 5, 6, 8, 9, 12, 13) name 10.1007/s44372-025-00446-3. I grepped every harvest file on origin/ci: that DOI occurs only in the Balsaminaceae family review (runs 9-2, 11-2, 13-2, 17-1) and in the Impatiens genus record (run 2-0). No harvest family-review step for Asteraceae, Lamiaceae, Sapindaceae or Cupressaceae prints it. It is otherwise supported: my own WebSearch "Asteraceae photoreceptor review" returned it second on the first page (link.springer.com/article/10.1007/s44372-025-00446-3), so it is what the records' labelled web family step returned, and audits 83 and 85 accepted a web-found family review in `chased` for genera in no harvest run. I accept it and count none of the nine. The fork is set out under Counts.

Screened. I read up to three entries per record against the record's reasons, the harvest titles and abstract starts, and the result lists of my own searches (patents, extension pages, the general photoreceptor review, a human-eye pharmacology review and similar). None reports a measurement of the record's trait in a species of the genus.

Searches. I ran 32 WebSearches: three per diel record (two for Taxodium) (scientific name and common name with "flower opening time anthesis", plus one of my own), three for Nekemias sense_chemical, four pooled focusing searches for the seven eye_type genera, and the rest for evidence and taxonomy checks. I fetched only URLs my searches returned. Two result lists held springerlink.bibliotecabuap.elogim.com proxy links, which I left alone.

## Search record verdicts (13)

| Line | Record | Verdict |
|---|---|---|
| 13 | Eupatorium eye_type | ok. Web-only; chased accepted (above). My pooled search returned the general focusing set (FIU lens-cell paper, PMC8309337, conical-petal work); nothing on Eupatorium. |
| 1 | Gaillardia diel | ok. Web-only. My two paired searches returned the same cultivar patents, the phytojournal volume and dictionary pages the record screens; my third (G. pulchella florets opening hours) returned patents only. |
| 9 | Taxodium eye_type | ok. Web-only. The leaf-epidermis anatomy paper is rightly screened; my pooled search returned general focusing works and Selaginella silica bodies, nothing on Taxodium. |
| 6 | Monarda eye_type | ok. Web-only. My pooled search returned Martin et al. 1989 on Medicago sativa (AGRIS record opened) and Lamiaceae leaf micromorphology; no Monarda focusing. |
| 12 | Eupatorium diel | ok. Web-only. My searches returned patents, nursery pages and floral-biology work on other genera; no Eupatorium opening hour. Its note's claim that sense_chemical and sense_light_nonvisual are closed by evidence falls with evidence lines 16 to 18 (below). |
| 2 | Gaillardia eye_type | ok. Web-only. Patents and the taxonomy file hold no optics. |
| 10 | Mitchella diel | ok. Queries match (12 harvest, 6 web); citation step named. My three searches (including distyly and bumblebee visits) returned Wikipedia, native-plant society and extension pages; no daily opening time. |
| 5 | Monarda diel | ok. Web-only. The Plovdiv M. didyma page (months only) is rightly screened; my third search (M. fistulosa time of day, nectar, protandry) returned flora and garden pages. |
| 3 | Serenoa eye_type | ok. Queries match (12, 4); citation step named. The ghost-orchid and human-eye works hold no Serenoa eye; nothing on palm focusing came back. |
| 4 | Acer eye_type | ok. Web-only. Monitor-brand, clinical and wood-grain pages rightly screened; my search returned the general leaf-optics set. |
| 11 | Mitchella eye_type | ok. Queries match (12, 6); the intumescence, butterfly-eye and green-flower works are rightly screened with the owner's wording. |
| 7 | Nekemias sense_chemical | ok. Queries match (13, 4). The vine-tea aroma paper is processed tissue (10(a)). My searches returned the A. grossedentata genome paper (Frontiers 10.3389/fpls.2025.1580779, PDF opened: garden tissue sampling, no hormone or elicitor treatment) and a Lichuan leaf-flavonoid extract study (journal.ccnu.edu.cn, abstract opened: extract and antibacterial assay only). No living response missed. |
| 8 | Taxodium diel | ok. Web-only. My searches returned Wikipedia, the NJ heritage sheet and Toth et al. 2011 (Collegium Antropologicum 35 suppl. 2, hrcak.srce.hr 72222, opened), whose diurnal pollen counts are for Cupressaceae and other taxa, with no Taxodium row. |

Search record errors: 0 of 13.

## Evidence record verdicts (10)

| Line | Record | Verdict |
|---|---|---|
| 1 | Salvia officinalis sense_chemical (GA priming) | ok. Tropentag page opened: authors and quote match; a living seed's response to gibberellin counts under 10(d); grade m. The ppm/mM inconsistency is in the abstract, as the note says. |
| 11 | Monarda fistulosa sense_chemical (herbivore volatiles) | ok. Springer page: Keefover-Ring 2013, Chemoecology 23: 1-11; quote verbatim. Herbivore-induced emission counts under 10(a); grade m. |
| 18 | Eupatorium riparium sense_light_nonvisual (Rai 1987) | **error (taxon).** The abstract (Springer page opened) holds the photoblastic and red/far-red result. But Eupatorium riparium Regel is a synonym of Ageratina riparia (Wikipedia infobox opened; WFO and POWO pages came back for it), and docs/views/gaps/queue.jsonl carries Ageratina as its own genus (Ageratina altissima rows). The record closes a Eupatorium cell with a measurement of another genus. |
| 13 | Monarda didyma sense_light_nonvisual | ok, weak. AGRIS page (Gavrilova and Zapryanova 2023, Bulgarian J Crop Sci 60(2): 63-68) holds the quoted sentence; light raised uniformity of germination in both species. No dark treatment is described, and the value says only that light influences germination, as the note states. |
| 2 | Salvia assurgens sense_chemical (floral volatiles) | ok, with a fork. Abstract and authors match (Botanical Sciences 102(4): 1080-1092, 10.17129/botsci.3489). The SciELO PDF's methods say inflorescence branches were cut, placed in water and sampled in the lab about an hour later, which the note left open. That is emission by freshly cut living flowers, correlated with field visitation of living plants; it is neither an extract, an oil nor a chemical treatment of cut flowers, so I let it stand. If the desk reads 10(a)'s "tissue taken from the plant" to cover it, this line fails too. |
| 12 | Monarda fistulosa sense_light_nonvisual | ok, weak. As line 13 (same abstract). |
| 9 | Acer mono sense_light_nonvisual | ok. cjae.net page: Zhang, Zhu and Yan 2012, CJAE 23(10): 2625-2631; the abstract gives A. mono's highest germination under R-FR-R. The record's quote is the general sentence on large seeds, as its note says. |
| 17 | Eupatorium adenophorum sense_light_nonvisual (Rai 1987) | **error (taxon).** Value holds against the abstract (effect "more marked in Eupatorium adenophorum"), but the POWO page for Eupatorium adenophorum Spreng. (urn:lsid:ipni.org:names:205345-1, opened) lists it as a synonym of Ageratina adenophora. |
| 5 | Gaillardia aristata sense_light_nonvisual | ok. rngr.net protocol 2203 opened: Skinner 2006; 84% under light/dark cycles and 80% in darkness at 20/30 C, verbatim. The protocol attributes the result to Maguire and Overland (1959), which the record does not say (noted, not counted). |
| 7 | Serenoa repens diel | ok. PALMS PDF opened: Carrington, Gottfried and Mullahey 2003, PALMS 47(2): 95-103; "Over half of the buds opened from 02:00 to 04:00." verbatim; flower opening time is the plant diel reading; grade m. |

Evidence errors in the sample: 2 of 10 (lines 17 and 18). Outside the sample, line 16 (Ren et al. 2010, Weed Science 58(3): 252-257, "Eupatorium adenophorum" aphid and MeJA volatiles) names the same species and fails on the same ground; I list it for dropping but do not count it.

## Counts

Search records: 0 of 13, 0%. Evidence sample: 2 of 10, 20%. The unit as drawn: 2 of 23, 8.7%, above 5%, so the unit fails on its evidence records; its search records pass.

Pooled search-record rate with the desk's other audits of desk-screen units, as written: audit 83's figure (30 in 860), audit 84 (1 in 31) and audit 85 (8 in 41) give 39 in 932; with this unit, 39 in 945, 4.1%. Audit 84's waiver of unlabelled OpenAlex lines would remove audit 83's five query errors and audit 85's two Ulmus errors (and, if the cached family-review lines count as such, audit 85's other six), giving 32 in 945 (3.4%) or 26 in 945 (2.8%). Adding this unit's evidence sample to the pool: 41 in 955, 4.3%.

Fork on `chased`. If the desk reads 10.1007/s44372-025-00446-3 as unsupported for the nine no-run records (the harvest family reviews for Asteraceae, Lamiaceae and Cupressaceae exist and do not print it; it is a general review that names no genus of these families, and no citations were chased from it), search lines 1, 2, 4, 5, 6, 8, 9, 12 and 13 become errors: 9 of 13, and the search records fail as well. I hold to audits 83 and 85, which accepted a web-found family review for genera in no harvest run, since my own family search returned this DOI.

**Verdict: fail (evidence records).** Drop the error lines and the rest of the unit stands.

**Error lines to drop:**
- docs/views/searched/desk-c7.jsonl: none.
- docs/views/evidence/desk-c7.jsonl: lines 17 and 18 (sample errors) and line 16 (same fault, found outside the sample). All three can be re-logged under Ageratina (A. adenophora, A. riparia) if those cells are open; the Eupatorium sense_chemical and sense_light_nonvisual cells then reopen.

Proposed audit lines (docs/views/audit format; not written to that directory):

```
{"unit": "desk-c7", "id": "desk-c7:16", "line": 16, "taxon": "Eupatorium adenophorum", "trait": "sense_chemical", "grade": "m", "verdict": "retract", "flags": ["taxon"], "reason": "Eupatorium adenophorum Spreng. is a synonym of Ageratina adenophora (POWO urn:lsid:ipni.org:names:205345-1); Ageratina is a separate genus in queue.jsonl. Audit 86."}
{"unit": "desk-c7", "id": "desk-c7:17", "line": 17, "taxon": "Eupatorium adenophorum", "trait": "sense_light_nonvisual", "grade": "m", "verdict": "retract", "flags": ["taxon"], "reason": "As desk-c7:16; the value holds for Ageratina adenophora. Audit 86."}
{"unit": "desk-c7", "id": "desk-c7:18", "line": 18, "taxon": "Eupatorium riparium", "trait": "sense_light_nonvisual", "grade": "m", "verdict": "retract", "flags": ["taxon"], "reason": "Eupatorium riparium Regel is a synonym of Ageratina riparia; the value holds for that species. Audit 86."}
```

## Wanted lines (listed, not counted)

- desk-c7 line 8 (Acer pycnanthum, 10.1007/s10310-014-0451-4): the `why` says the abstract was read on an "informahealthcare mirror of the Springer record". That host is a publisher's legacy domain and not a library proxy by the launch rule's tests, but a mirror is not the record; the authors and title stay unread.
- desk-c7 line 10 (Liu et al. 2009, bald cypress germination): not checked against a page.
- No other wanted line was checked against a page.

## Leads

- Eupatorium sense_light_nonvisual, once lines 17 and 18 go: the E. cannabinum achene paper the record opened (Seed Science Research, cambridge.org abstract, opened) covers temperature, stratification and burial only, and gives no light result.

## Blocked pages

None. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened (two elogim proxy links in one result list were left alone), and no paper text was committed.
