# Audit 110: desk-d19 (5 evidence records; branch origin/research/desk-d19, head 0c6350e8)

## Lines judged

No sample was drawn. The launch prompt asks for the whole unit, so error lines can simply be dropped.
- Evidence records: all 5 lines of docs/views/evidence/desk-d19.jsonl.
- Search records: none (the unit has no searched file).
- Wanted lines: none (the unit has no wanted file).
- Leads the unit left alone: 6 spot-checked from its progress file (Senecio vulgaris, Bromus inermis, Quercus robur, Lonicera japonica, Euphorbia amygdaloides subsp. arbuscula, Persicaria maculosa).

## Gate

The unit has no searched or wanted file, so `screen_candidates.py --check` has nothing to check. All 5 evidence lines parse as JSON.

## Method

I judged against desk-audit.md, desk-screen.md points 1 to 10 (owner's readings 10(a) to 10(e) included), the counting rule of audit 39, the rulings of audits 84 and 86 to 90, and audits 100 to 108 (requotes listed, not counted; whole nulls filed as evidence, audit 107). For each record I ran a title WebSearch, fetched a URL that search returned, and compared authors, year, journal, DOI, quote, value, trait, grade and partial flag. Names were checked on POWO/WFO pages my searches returned. I checked origin/main (51d38503) docs/views/evidence and docs/views/searched for every genus, and origin/research/desk-d20 for its Ambrosia record.

Searches: 15 WebSearches (4 evidence titles, 2 taxonomy, 9 for left leads). I fetched only URLs my searches returned. The PMC page for Sanchez-Lucas et al. 2025 (PMC12050401) raised a permission request that went unanswered; I did not retry it. A biomedcentral-preview...saludcastillayleon.es result (a regional health-service mirror) was left alone. No ResearchGate, academia.edu, Sci-Hub, LibGen or proxy page was opened, and no paper text is committed.

## Evidence verdicts (5)

| Line | Record | Verdict |
|---|---|---|
| 1 | Epigaea gaultherioides sense_chemical (Pulatkan, Çimen, Kurt, Turna 2022, Baltic Forestry 28(1): 84-90, 10.46490/bf591) | **ok.** The Baltic Forestry OJS page (opened) confirms authors, volume, year and DOI; the KTU AVESIS page (opened) confirms pages 84-90, GA3 at 0, 100, 500 and 1000 ppm, and the quote word for word as one whole sentence (111 characters). Untreated seed did not germinate; GA3 on living seed is 10(d). The abstract's 80% sentence names no GA3 dose and says "cold storage at 25°C (24 h dark)", which clashes with its own +4 C storage; the record's value and note say as much. Abstract only, `partial` true, grade m. WFO wfo-0000383479 (opened, December 2023 snapshot) accepts Epigaea gaultherioides, with Orphanidesia gaultherioides as a synonym, so the genus is right. Main holds no Epigaea evidence; main's null search record sweep-28:38 (Epigaea sense_chemical) is contradicted, which is main's fault (audit 104), not counted. |
| 2 | Ambrosia artemisiifolia sense_chemical (Hall et al. 2023, Plants 12(18): 3298, 10.3390/plants12183298) | **ok.** PMC10534427 (opened) confirms the eight authors in order, volume, article number and DOI, and the quote word for word as one whole sentence (81 characters). Exposure was to living emitter plants in twin-chamber cages for 21 days against clean-air controls, with dry mass, allocation, SLA and chlorophyll measured: a living receiver's measured null response to airborne cues, 10(a). Main files whole nulls as evidence (audit 107: desk-c11, desk-d1, Ratibida), so a null belongs here. The value's other clauses (all species avoided ragweed root exudates; wheat and soybean lost dry mass after ragweed VOCs) match the abstract. Repeats and contradictions: main holds only A. artemisiifolia sense_light_nonvisual (sweep-6:33, recheck-quotes-3-fixed:169), so no repeat. desk-d20:2 (Šćepanović et al. 2022, ethephon and GA3 raised germination), on its branch and not on main, is the same species and trait with a different cue: a positive hormone response of seed and a null response of plants to volatiles do not contradict and do not repeat. Main's null search record sweep-6:31 (Ambrosia sense_chemical "none") is contradicted, main's fault, not counted. Abstract only (the full text was used only for method), `partial` true, grade m. |
| 3 | Geranium pratense diel (Abdusalam, Maimaitituerxun, Hashan, Abdukirim 2021, Plant Diversity 43(4): 308-316, 10.1016/j.pld.2021.04.001) | **ok.** The rhhz.net full text (opened) confirms authors, journal, pages and DOI, and the quote word for word in section 2.1 as one whole sentence (124 characters). The flowers are the authors' own study population (Wuqia County, 2017 and 2019), and the Introduction adds "These flowers close temporarily in the evening". Closing at dark and reopening in light is the timing of flower opening in a named species, which is the owner's plant diel reading; it is a field statement about the species, not a historical flower-clock table. The paper gives no clock hour (its 1-h interval records time the floral stages, not daily opening), and the value says "no clock hour given in the text", so the value claims no more than the source. Grade m; open full text, no `partial`, correct. POWO 322493-2 (opened) accepts Geranium pratense L. Main holds no Geranium diel evidence; main's null diel records desk-c8:30, harvest-15:7, harvest-1:42 and sweep-1:42 are contradicted, main's fault, not counted. Fork below. |
| 4 | Geranium pyrenaicum sense_chemical (Gommers et al. 2018, Plant Direct 2(8): e00066, 10.1002/pld3.66) | **ok, requote (not counted).** PMC6508794 (opened) gives the seven authors as the record has them (Jason P Banda = Banda JP). GA3 at 10, 50 or 100 µM, and 1-NAA at 0.1 to 500 µM, were sprayed on a leaf of intact living rosette plants against mock controls, and petiole elongation was measured: an applied-hormone response of a living plant, 10(d), so sense_chemical is the right trait. The quoted words open a longer Discussion sentence that cites Figure 6 and continues about endogenous GA synthesis, and start lower-case, so the quote is a clause; `where` says "results" but the sentence is in the Discussion. The value holds. POWO 322504-2 (opened) accepts Geranium pyrenaicum Burm.f. Main holds this paper under sense_light_nonvisual only (harvest-3:4, recheck-codex-b-fixed:19), so this is a different trait and no repeat. Main's harvest-15:7 sets the paper aside for sense_chemical as "logged under sense_light_nonvisual", a null this line contradicts; main's fault, not counted. |
| 5 | Geranium robertianum sense_chemical (same paper) | **ok, requote (not counted).** As line 4. The page says both species' petioles responded to GA3 and that G. robertianum's NAA response "at high concentrations was strongly reduced" against G. pyrenaicum; the value's "both species can respond to exogenous GA and auxin (NAA)" holds. Main holds G. robertianum sense_light_nonvisual only (harvest-15:3), so no repeat. Same quote and `where` fault as line 4. |

Fork on line 3. If the desk reads plant diel as needing a clock hour or a daily window, or files light-driven closure under sense_light_nonvisual, line 3 is an error and evidence is 1 of 5. I count it ok because audit 107 accepted "the anthesis is diurnal" with no hour (Tropaeolum majus) under the same reading, and the value states the absence of an hour.

## Leads left alone (6 spot-checked, not counted)

| Lead | Unit's reason | My check |
|---|---|---|
| Senecio vulgaris light (Tursun, Dayisoylu, Tursun 2015, KSU J Nat Sci 18(4): 48-54) | result sentence far over 125 | Confirmed. inonu.edu.tr AVESIS page (opened): the abstract has three sentences; the light result sits in a 399-character sentence. No quotable sentence. |
| Bromus inermis sense_chemical (Strand et al. 2025, J Insect Sci 25(2)) | sentence about 340 characters | Confirmed for the abstract (334 characters, scholarworks.montana.edu record opened). The open Montana thesis PDF breaks off in the chapter introduction, so no Results sentence could be read. |
| Quercus robur sense_chemical (Sanchez-Lucas et al. 2025, Plant Cell Environ 48(6): 4455-4474, 10.1111/pce.15419; UJI portal opened) | abstract sentence 135 characters | **Readable measurement left.** The open bioRxiv preprint (10.1101/2024.09.20.613659, full PDF opened) uses Q. robur seedlings, applies BABA as a 5 mM soil drench, SA as a 5 mM spray and JA as a 500 µM spray against water controls, and states in its Discussion "We have demonstrated that BABA and SA lead to enhanced resistance to PM in oak seedlings." (89 characters) and "Meanwhile, JA had no significant impact on resistance in both conditions (Fig. 1)." (82). Elicitor response of living plants, 10(d); main holds no Q. robur evidence. The published PMC12050401 text was refused, so the wording there is unchecked. |
| Lonicera japonica diel (Feng, Wang, Luo, Huang 2023, J Syst Evol 61(3): 530-537, 10.1111/jse.12916) | abstract sentences 139+ characters | Confirmed for the abstract (jse.ac.cn page opened: the night-scent sentences run 138 and 139 characters). Full text not checked. |
| Euphorbia amygdaloides subsp. arbuscula light (Cristaudo et al. 2019, Ecol Evol, 10.1002/ece3.5535) | only a group fragment, subspecies | Confirmed. The unict.it PDF (opened) has no whole sentence of 125 characters or fewer for this subspecies; its short dark-favoured sentence names E. characias and E. dendroides. |
| Persicaria maculosa light (Earley et al. 2023) | transcript counts only | **Unchecked.** My search did not return the paper. |

The Quercus robur lead is the one miss. A lead-reading unit makes no null claim, and a left lead stays on the wanted list, so I list it and do not count it. If the desk counts a readable lead left unread as an error, the unit is 1 of 6.

## Counts

- Search records: 0 of 0.
- Evidence: 0 of 5.
- Unit: 0 of 5, 0%.

Pooled with audits 83 to 90, from audit 90's figures (search records 48 in 1026; with evidence 52 in 1090):
- Search records: 48 in 1026, 4.7% (unchanged).
- With evidence included: 52 in 1095, 4.7%.

**Verdict: pass.** 0 of 5 evidence records are errors. Lines 4 and 5 should be requoted to the whole Discussion sentence and their `where` changed to "discussion", which changes no value.

**Error lines to drop:**
- docs/views/evidence/desk-d19.jsonl: none.

Follow-ups:
- Lines 4 and 5: requote to the whole sentence and correct `where`.
- Read the Quercus robur lead (Sanchez-Lucas et al. 2025) from the published PMC text and log SA and BABA priming under sense_chemical; quote the published wording, or cite the bioRxiv preprint if only it can be read.
- Main's null records now contradicted by this unit: sweep-28:38 (Epigaea), sweep-6:31 (Ambrosia), desk-c8:30, desk-c8:32, harvest-15:7, harvest-1:42, sweep-1:42 (Geranium). These should be re-opened when the lines land.
