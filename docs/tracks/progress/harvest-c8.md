# harvest-c8 progress

## 2026-10-27

**Current checkpoint:** 5/40 genera screened here (Albizia, Ambrosia, Diospyros, Rubus, Baccharis); 5 eye_type search records; 75 wanted lines; 0 evidence records; 0 cells closed by measurement. Morella is next. Pilea is complete in harvest-c4 and its provenance must be reused, leaving 34 genera requiring new work. Current service refusals remain OpenAlex429, MDPI429, UChicago403 and SANBI403; no further request made to these services. Worker16 stopped between Baccharis and Morella for fresh-context continuation.

The following dated subsections retain the actual attempts and earlier counts as history; the checkpoint above is current.

Dispatch `regards-issue-28-20261027`, issue #28. Read AGENTS.md, the authoritative harvest-c8 line in work/queue-lines.txt, the batch JSON, round4-harvest.md, THOROUGH.md, BRIEF.md Round 2, round3-sweep.md, desk-screen.md points 1–10 and audit 53/54 context. Scope is the 40 genera in the batch; the entry after Nuttallanthus is Melilotus.

Initial checkpoint: 0 of 40 genera completed; 0 evidence records; 0 cells closed by measurement; 0 complete-protocol search records; 0 wanted lines so far. Albizia started, all 40 remain incomplete. No full-protocol negative record is licensed by the work below.

### Initial Albizia work (subsequently completed)

The current queue lists only `Albizia julibrissin` / `eye_type` as open. Checked canon.jsonl: its eye_type compilations concern Metazoa (Animal eyes, in hand, plus the other animal compilations); the owner’s plant eye_type reading of 25 October applies. The required plant germination searches also returned leads for light and chemical response, but those traits are already covered for this genus and no duplicate wanted lines were added.

Connected web searches run, word for word, in order:

- `Albizia seed germination light dark`
- `Albizia germination gibberellin OR smoke OR dormancy`
- `Albizia floral scent volatiles`
- `Albizia eye type`
- `silk tree eye type`
- `Albizia epidermal lens cells eye type`
- `silk tree epidermal lens cells eye type`
- `Fabaceae photoreceptor review`

Read the returned titles/snippets only. The eye/lens results include epidermal anatomy and seed water-gap “lens” work, plus general plant-optics reviews; none supports an eye_type measurement under the owner’s reading. No source page was fetched and no evidence or negative record was written. Some paired searches yielded fewer than 20 results in the connected tool; no claim is made to have screened 20 where the tool did not expose 20. No unauthorized host was opened (the family-review results included a publisher mirror at legcat.gov.ns.ca, which was left unopened).

### Initial access failures (ci and OpenAlex subsequently resolved)

- No local `refs/remotes/origin/ci` exists. `harvest_get.py` and `screen_candidates.py` call an automatic git fetch, so they were read rather than run while the parent’s no-fetch rule applies. Their actual current harvest candidate list has not been screened; a missing local ref is not a zero-hit result.
- The connected web tool refused all three explicit OpenAlex URLs as “not accessible via this tool”: `https://api.openalex.org/works?search=Albizia%20eye%20type&per-page=20`, `https://api.openalex.org/works?search=silk%20tree%20eye%20type&per-page=20`, and `https://api.openalex.org/works?search=Fabaceae%20photoreceptor%20review&per-page=20`. One repeated call confirmed the same failure, so this is an access block, not a completed OpenAlex step.
- Shell network proxy refusal/direct DNS failures were already established by the coordinating agent; no paid API or alternate unauthorized route used.

Initial next steps (subsequently completed): obtain the ci harvest snapshot through the coordinator; finish Albizia’s scientific/common-name and family-review OpenAlex steps through an accessible route; then proceed to Ambrosia, preserving the mandatory first germination searches. Do not promote this note into a search record without completing those steps. Screening writes no evidence. No builds, servers, Playwright, self-tests, gates or #29/#30 files changed.

### Access recovery and Ambrosia leads (same date)

The coordinator fetched `origin/ci` at `55a1f658a687c5d355ae11d9eec65def211f4033`. Explicit additional network permission restored `requests` access to OpenAlex. Re-ran `Albizia eye type`, `silk tree eye type`, and `Fabaceae photoreceptor review` against the required OpenAlex endpoint, each HTTP 200 with its first 20 results saved under work/harvest-c8/. Read all 60 titles and available abstracts. The common-name results are mostly silk biomaterials and silkworm history; the scientific results are medicinal chemistry and seed studies. No eye_type measurement is suggested. Opened the Fabaceae review Henriques and Benlloch 2026, DOI `10.1093/jxb/erag313`, through the connected web tool and checked for Albizia (no match); it reviews photoperiod signalling in crop legumes, not plant eyes. Shell fetching of the PMC page returned a reCAPTCHA despite HTTP 200; the connected tool exposed the review text. The initial access failures above are superseded for OpenAlex and ci availability, not for the initial failed calls themselves.

Started Ambrosia's mandatory first searches, word for word: `Ambrosia seed germination light dark`; `Ambrosia germination gibberellin OR smoke OR dormancy`; `Ambrosia jasmonate herbivore`. Read the available result titles/snippets. Added 2 wanted lines, checked absent from main's wanted/evidence/corrected stores and paper-status by DOI/title: Ruziev and colleagues 2020 on Ambrosia trifida light/dark germination (KCI abstract read, no evidence) and Šćepanović and colleagues 2022 on chemical germination treatments of A. artemisiifolia (PMC reCAPTCHA; MDPI HTTP 429). No further MDPI fetch after the 429. Author names for the latter verified via its exact DOI OpenAlex lookup, HTTP 200. A Frontiers article (`10.3389/fagro.2020.573860`) also opened at abstract/method context, but its A. artemisiifolia light-response trait is already on main; no duplicate or null record was added for it.

At that checkpoint, running the official harvest_get and screen_candidates scripts through a work-only wrapper that suppresses automatic fetch while using the coordinator's exact ci snapshot. At that checkpoint, counts were 0/40 pending that inspection and protocol completion, with 2 wanted, 0 search and 0 evidence. All 40 were then incomplete; Ambrosia still needs paired trait searches and citation/review step.

### Albizia completed

Official harvest_get returned “in no harvest run yet” across runs 1–24; screen_candidates returned “not in the harvest”. The first 20 results of each successful OpenAlex query (60 total) and all exposed web titles/snippets were screened. The coordinator confirmed that genuinely fewer exposed web results may be recorded with their actual extent; no claim of 20 web titles per query is made. One eye_type search record now preserves every successful query above and the owner’s plant-eye reading. Family review `10.1093/jxb/erag313` is the chased step. No eye_type evidence exists on main for Albizia. Counts now: 1 of 40 genera complete, 1 search record, 2 wanted lines (Ambrosia partial), 0 evidence and 0 measured closures. Thirty-nine genera remain; Ambrosia is next and already has its initial germination searches/leads. Pilea is being covered by c4 under the coordinator; reuse that provenance when reached.

### Ambrosia completed screening; measurements await intake

The official harvest snapshot contains run 5, supplement 12 (photoperiod and circadian searches), a family review in run 17 and 21 works citing `10.1371/journal.pone.0166510`. Screened all 105 unique titles and stored abstracts (the harvest caps abstracts at 700 characters). Direct OpenAlex calls made before the desk-wide 429 refusal returned 152 results: 20 each for scientific/common diel, eye and chemical pairs and the Asteraceae review; 8 scientific-name and 4 common-name light results. All returned titles and available abstracts were screened. OpenAlex is now skipped globally after the coordinator reported an actual 429 from another worker; no further call made after that notice.

Completed the remaining web pairs: `Ambrosia flower opening time anthesis`; `ragweed flower opening time anthesis`; `Ambrosia eye type`; `ragweed eye type`; `Ambrosia chemical sense volatile response`; `ragweed chemical sense volatile response`; `Ambrosia light photoperiod phototropism`; `ragweed light photoperiod phototropism`. These and the initial three web queries are copied word for word after every successful harvest query and direct API query in the eye_type search record. Genuine fewer-results responses are stated without claiming 20. No truncated title/abstract output was treated as a complete screen; omitted stretches were recovered in subsequent reads.

Added four further wanted lines after checking main/status for DOI/title duplicates: Bianchi and colleagues 1959 (publisher abstract states anther opening at 06:30–08:00; full text requires access), Hall and colleagues 2023 (SLU institutional abstract directly reports living ragweed root responses to exudates; full text awaits intake), Effects of Photoperiod on Sex Expression in Ambrosia trifida 1942 (harvest abstract; own publisher fetch 403, authors not shown so blank), and Schutte 2007 (institutional thesis metadata/abstract read; germination/dormancy title is a required candidate, actual light/chemical methods need reading). The latter is explicitly a candidate rather than a claimed light/chemical measurement. No further UChicago fetch after its 403. No further MDPI fetch after its 429. No sense_light_nonvisual null: main already measures A. artemisiifolia; A. trifida remains pending the wanted papers. No chemical or diel null while their candidates await intake.

Round totals: **2 of 40 genera screened**, **2 eye_type search records**, **6 wanted lines**, **0 evidence records**, **0 cells closed by measurement**. Albizia and Ambrosia screening protocols are complete; all wanted-derived measurements remain unclosed. Remaining 38 genera start with Diospyros and Rubus; Pilea is being covered by c4 and the coordinator will account for that provenance. Stop here between genera for a fresh continuation rather than abbreviate the next genus’s protocol. Next: start Diospyros with its mandatory germination searches, use the saved ci snapshot and web/other sources while the OpenAlex and MDPI refusals stand, then Rubus and Baccharis. The scratch harvest cache is work/harvest-c8/harvest-cache.pkl (105 Ambrosia works in its full-genus/family data); it is not a deliverable and is never committed.


## 2026-10-27 — worker11 continuation

Completed Diospyros screening only in this continuation. **This worker: 1 genus, 1 eye_type search record, 30 wanted lines, 0 evidence records, 0 measured closures. Cumulative harvest-c8: 3 genera, 3 search records, 36 wanted lines, 0 evidence and 0 measured closures.** Pilea's completed harvest-c4 protocol is preserved and is not repeated. Rubus is next, then Baccharis and Morella; 36 genera require new work after reusing Pilea.

Read AGENTS.md, the worker guide and exact fresh assignment, batch/queue order, THOROUGH.md, BRIEF.md, round3-sweep.md and desk-screen.md including plant 10(a–e), with audit 53/54 context. Used worker05's legitimate serialized hg.load data from the coordinator-fetched ci commit 55a1f658a687c5d355ae11d9eec65def211f4033. Official harvest_get.show and screen_candidates functions ran on that snapshot. Diospyros has no failed harvest step: run 4, supplements 12/14/20, family review (10 returned works), and two zero-hit citation steps on 10.1111/ele.12205 and 10.25066/agrotec.v35i1.10254. Read all 157 unique titles and the complete stored abstracts (up to 700 characters each), including the entire family result set. Recovered omitted stretches from shell output in subsequent reads; no truncated stretch was treated as a complete screen. Checked main's global searched, wanted, accepted evidence/corrected stores and papers-status by genus and candidate DOI/title, plus canon metadata. No accepted Diospyros evidence exists in those stores. Its old sweep-15 line is a thin search, not a completed protocol.

Successful cached harvest queries, word for word, in order:
- `Diospyros phytochrome photoreceptor`
- `Diospyros light perception`
- `Diospyros phototropism`
- `Diospyros flower opening time`
- `Diospyros nyctinasty`
- `Diospyros volatile signalling`
- `Diospyros photoperiod`
- `Diospyros circadian rhythm`
- `Diospyros anthesis`
- `Diospyros pollination biology`
- `Diospyros epidermal lens cells`
- `Diospyros epidermal focusing leaf optics`
- `Ebenaceae photoreceptor review`

Connected web searches, word for word, in actual execution order:
- `Diospyros seed germination light dark`
- `Diospyros germination gibberellin OR smoke OR dormancy`
- `Diospyros floral scent volatiles`
- `Diospyros flower opening time anthesis`
- `persimmon flower opening time anthesis`
- `Diospyros eye type`
- `persimmon eye type`
- `Diospyros chemical sense volatile response`
- `persimmon chemical sense volatile response`
- `Diospyros light photoperiod phototropism`
- `persimmon light photoperiod phototropism`
- `Ebenaceae photoreceptor review`
- `Diospyros seed germination light dark`
- `Diospyros germination gibberellin OR smoke OR dormancy`
- `Diospyros floral scent volatiles`

The final three queries repeat the initial three solely to recover tool-output truncation; their full saved result was read in two parts, without claiming extra protocol coverage. The family web result also had a truncated middle; its visible general-photoreceptor results add no claim of an Ebenaceae review, and the completely screened cached family review and citation steps supply the required citation/review step. Every scientific/common trait pair was fully read at the extent actually exposed by the web tool; genuinely fewer results were not counted as 20. Common name was persimmon because harvest english is empty. OpenAlex API calls were skipped after the desk-wide 429; no unrun API query is represented as executed. MDPI and UChicago fetches were skipped.

Before the coordinator reiterated desk-screen point 3, an initial recovery call opened returned metadata/reference pages at Eurekamag, AGRIS, TFRI and the Korean flower journal, a PROSEA page and a general dormancy review. It also encountered SANBI https://pza.sanbi.org/diospyros-natalensis as actual `(403) Forbidden`; reported this to the coordinator and made no further SANBI fetch. Several guessed recovery reference IDs returned only Internal Error; none was treated as a source. No further page opening after the coordinator's point-3 reminder. No paper text is committed, and no evidence is logged. No library/proxy mirror, ResearchGate or other unauthorized source was opened.

The 30 wanted leads retain exact source URLs/DOIs from the cached metadata or returned web snippets, with unknown fields empty and no invented dates/DOIs/authors. Strong examples are 10.1603/022.038.0512 (living D. kaki tree emissions after wax-scale attack or methyl jasmonate), Oh/Kim/Ahn 1988 at AGRIS 6471cc19f762bd4124ec594d (light/dark and GA seed germination), Everitt 1984 (D. texana light/dark seeds), 10.4308/hjb.33.2.278-287 (light color/intensity at night in D. discolor seedlings), LED scion production and the long-day Saijo experiment. Applied hormone and regeneration experiments are retained under owner reading 10(d), including nodal/leaf explants; no response magnitude is logged. Mandatory germination/dormancy candidates whose abstracts show only temperature, maturity or moisture were retained under 10(e), explicitly saying that a light/chemical experiment is unconfirmed. The Uniben project PDF has no exposed complete title or author/year, so those fields remain empty. The repeat search exposed the original journal source for the D. hispida germination work; its ResearchGate result was never opened. Floral biology 10.3390/plants11192535 and D. dumetorum sap flow 10.3390/f16030387 remain diel leads; no anthesis hour is claimed.

Dispositions outside those leads: 10.1139/b85-258 uses geological clay lenses, while the other three tool-listed eye candidates concern human/animal eye treatment; all four are individually screened in the eye_type record under the owner's plant-eye reading. Optical-coherence-tomography disease imaging uses human instruments and measures no plant eye. Persimmon vinegar, dried-fruit sensory tests, essential oils and volatile profiles of collected/extracted fruit/flower material measure product/tissue chemistry, excluded under 10(a). The Korean flower/calix VOC paper (https://www.ksbec.org/articles/article/RaGo/) compares dissected organs for fragrance use, so no living-signal measurement is claimed. The bee-attractive-flower VOC study remains wanted because its snippet does not establish whether flowers were attached or collected. The 109-species living-VOC survey 10.1038/s41598-017-10975-x is already wanted in plant-screen-1; no duplicate line added, and its Diospyros species list still needs intake. Phytochrome-marker phylogenetics and genetic pathway enrichment alone are not a light/clock response measurement. Seasonal flowering dates, fruit-development days after anthesis, embryo-sac development and pollination elapsed hours are not flower-opening hours. Broad reviews whose stored abstracts do not identify a Diospyros measurement were not used to claim one.

No null is written for diel, sense_chemical or sense_light_nonvisual while these plausible sources await intake. Only eye_type has a completed negative search record under owner reading 10(b). The actual screen_candidates.check implementation, using legitimate hg.load data via the scratch cache wrapper, printed **0 problems** on this unit's searched/wanted files before commit. This is research screening validation; no app check/build/server, gate change, #29 or #30 change was made.


## 2026-10-27 — worker16 continuation

Completed Rubus screening. **This worker so far: 1 genus, 1 eye_type search record, 24 wanted lines, 0 evidence and 0 measured closures. Cumulative harvest-c8: 4 genera, 4 search records, 60 wanted lines, 0 evidence and 0 measured closures.** Pilea's completed harvest-c4 coverage is preserved; 35 genera still require new work, starting Baccharis, Morella, Nephrolepis.

Read AGENTS.md first, exact worker16 fresh queue line, current worker guide, batch and original queue order, round4-harvest.md, THOROUGH.md, BRIEF.md Round 2, round3-sweep.md and desk-screen.md points 1–10 including plant 10(e), and audit53/54 context. Consulted the cloud-runtime skill and enforced unrestricted network status. Official harvest_get.show and screen_candidates.show using the legitimate cached hg.load data for coordinator-fetched ci 55a1f658a687c5d355ae11d9eec65def211f4033 report Rubus in no harvest run across runs1–24. No failed or zero-hit API query is invented. The old sweep-1 two-query combined record lacks a completed web protocol and does not settle the original four traits. Global queue/searched/wanted/accepted evidence/corrected and papers-status checked by genus, then prospective wanted items checked by exact DOI, normalized title and URL: none duplicated. Canon metadata checked; eye_type compilations concern animal eyes.

Connected web searches, word for word in execution order:
- `Rubus seed germination light dark`
- `Rubus germination gibberellin OR smoke OR dormancy`
- `Rubus floral scent volatiles`
- `Rubus flower opening time anthesis`
- `blackberry flower opening time anthesis`
- `Rubus eye type`
- `blackberry eye type`
- `Rubus chemical sense volatile response`
- `blackberry chemical sense volatile response`
- `Rubus light photoperiod phototropism`
- `blackberry light photoperiod phototropism`
- `Rosaceae photoreceptor review`

Read all exposed original-source titles/snippets and available returned abstracts; fewer than20 results were exposed for individual queries where applicable. Saved complete outputs under work/harvest-c8/Rubus-web0.txt through Rubus-web3.txt and recovered omitted output sections; no truncated stretch was treated as reviewed. No source/fullpaper page fetched. OpenAlex API remains skipped after desk-wide429; no MDPI/UChicago/SANBI fetch, paid API, unauthorized copy or proxy used. Returned results on ResearchGate, Wikipedia and unattributed third-party full-text hosts were not opened or used as source records.

Added24 wanted candidates:10 germination/dormancy sources (including the USDA seed-handbook chapter as a route to its original trials);3 living floral/herbivore volatile candidates;2 daily anthesis/nectar timing candidates; and9 light/photoperiod experiments or plausible studies. Empty authors/years/titles remain empty where original-source snippets do not expose them. In particular, the 2019 International Journal of Chemical Studies PDF explicitly shows Table4, Time of anthesis in Rubus macilentus C., but its exact article title was not exposed by the original-source result; the journal title/volume/pages are available in that result. The Chinese journal figure snippet explicitly names Rubus setchuenensis nectar secretion rhythms; exact article title and daily values await intake. Spontaneous floral aroma leads require original methods to establish living attached emission and signalling; removed-tissue chemistry alone is excluded. The Rubus seed anatomy title describes low germination generally and was not promoted to a light/chemical experiment. Postharvest/juice/fruit-extract chemistry, human eye cosmetics and developmental days-to-anthesis studies were not mistaken for plant chemical sensing, plant eyes or daily opening time.

The family query returned Rosaceae anthocyanin-review metadata/abstract (10.1002/fsn3.72269), alongside general photoreceptor and animal-eye reviews; all returned material was screened, without fetching. Its environmental signalling is a light trait, and its returned material reports no plant-eye measurement. One eye_type search record holds all12 exact queries and the owner's none reading; no null for diel, chemical or light while their candidates await intake. No measurement cell closes in desk screening.

### Baccharis completed; worker16 checkpoint

**This worker total: 2 genera (Rubus, Baccharis), 2 eye_type search records, 39 wanted lines, 0 evidence and 0 measured closures. Cumulative harvest-c8: 5 genera, 5 search records, 75 wanted lines, 0 evidence and 0 measured closures.** Pilea's completed c4 coverage stays preserved and is not redone; 34 genera require new work, starting Morella, Nephrolepis, Medicago.

Official harvest_get.show and screen_candidates.show on the same legitimate cached ci snapshot report Baccharis in no genus harvest. The Asteraceae family-review record exists separately in run17: Asteraceae photoreceptor review returned15 works (out of581 hits); read all15 titles and complete stored abstracts, capped at700 characters each. The review Translating Flowering Time from Arabidopsis thaliana to Brassicaceae and Asteraceae Crop Species (10.3390/plants7040111) supplies the family review step at the metadata/stored-abstract level, without fetching MDPI. General animal/retinal-cell results were not plant-eye measurements. Global stores have only the thin old sweep-9 two-query compound absence, with no accepted Baccharis evidence/wanted candidates. Original queue has all4 traits for B. pilularis, B. halimifolia and B. salicifolia; they were all researched. Canon metadata checked as for Rubus.

Connected web searches, word for word in execution order:
- `Baccharis seed germination light dark`
- `Baccharis germination gibberellin OR smoke OR dormancy`
- `Baccharis floral scent volatiles`
- `Baccharis flower opening time anthesis`
- `eastern baccharis flower opening time anthesis`
- `Baccharis eye type`
- `eastern baccharis eye type`
- `Baccharis chemical sense volatile response`
- `eastern baccharis chemical sense volatile response`
- `Baccharis light photoperiod phototropism`
- `eastern baccharis light photoperiod phototropism`
- `Asteraceae photoreceptor review`

Read all exposed original-source titles/snippets and returned abstracts. Output files Baccharis-web0.txt through Baccharis-web3.txt under work/harvest-c8 retain complete raw results; long outputs were read in sections. Fewer than20 results were exposed per individual query where applicable; no claim of20 unseen titles. Only searches were sent: no source or fullpaper-page fetch. Asteraceae web review results were general plant/algal photoreceptor articles; the complete cached family review separately supplied the family step. No OpenAlex API/MDPI/UChicago/SANBI request, paid API, library proxy or unauthorized copy used.

Added15 wanted lines after DOI/title/URL duplicate/status checks:9 seed/germination sources, 4 volatile/communication candidates, 1 capitulum/floret phenology candidate and the existing opened-source shading lead. Germination candidates include B. dracunculifolia, B. retusa, B. dracunculifolia subsp. tandilensis and B. milleflora/tridentata. B. salicifolia plant-plant experiments are direct living volatile emission/receiver leads (10.1002/ecy.2534 and10.1111/nph.14164); the Macrodactylus interaction and psyllid-induced volatile-profile title remain candidates whose intact-plant versus removed-tissue methods need intake. The latter title is a reference exposed in the original Wiley result for10.1002/cbdv.201800017: that is the citing article DOI, so the candidate DOI remains empty and its get field explicitly identifies the reference. Plain distilled essential-oil and collected-tissue volatile surveys were excluded under10(a), not treated as living chemical responses.

The old sweep-9 record explicitly names Panetta1979,10.1071/AR9791053 and an opened abstract describing living B. halimifolia shaded to about14% of open-sky radiation. It excluded that experiment as not a light sense; owner reading10(d) now makes it a required light-response lead. Added a wanted line with the actual DOI and local provenance, without inventing the original title. The separate Panetta germination/seed-survival title is supported by current returned metadata and Canadian government review snippets. Baccharis aliena capitulum/floret phenology is a plausible daily-anthesis candidate; no diel null while it waits. Seasonal months of flowering in floras were not treated as time of day.

One eye_type search record includes the real cached family query then all12 actual web queries and the owner's none reading. No null for chemical, light or diel. Unknown authors/years/titles remain empty. Validation used the actual current screen_candidates.check on the legitimate serialized hg.load snapshot, not a substitute checker; it returned0 problems before the Rubus commit and0 before the Baccharis commit. No gate code changed. Stop here between genera for fresh-context takeover; Morella is unstarted.
