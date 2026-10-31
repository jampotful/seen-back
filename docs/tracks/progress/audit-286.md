# audit-286: desk-d202 (1 evidence record, no search records, no wanted lines)

Audited 31 October 2026 from the desk-d202 files present untracked in the worktree (docs/tracks/progress/desk-d202.md and 1 evidence line in docs/views/evidence/desk-d202.jsonl; neither committed here, neither edited). HEAD 79db7ca9 equals origin/main. `tools/senses/check.py` on the evidence file: 1 record, 0 problems. Quote length (`len(q.split())`): 30, within 40. No searched or wanted file, so the one record was judged whole and there is no sample to draw. Rules applied: oa-audit.md "Scientific context and counting (29 October 2026)", oa-read.md and BRIEF (whole sentence, 40 words, grade, `partial`), desk-audit.md (no 125-character limit), the publisher-copy licence rule, and the Mammal Diversity Database (MDD) as mammal name authority as audit 256 used it for the same paper; the shared brief's plant-screening items are superseded for this animal unit. Duplicates checked with git grep on origin/main across docs/views (evidence, audit including corrected/ and ALL.jsonl, searched, wanted, gaps, sheets), views/ and docs/tracks for "Kogia breviceps", "K. breviceps", "pygmy sperm", the DOI suffix 984333, the title words "seldom-tested", "Delphinus capensis" and "Delphinus". 3 WebSearch and 8 WebFetch calls used.

Sources opened: api.crossref.org/works/10.3389/FMARS.2022.984333 (uppercase answered); the record URL frontiersin.org/journals/marine-science/articles/10.3389/fmars.2022.984333/full (two passes) and its /pdf (one pass); mammaldiversity.org/taxon/1006459 (Kogia breviceps), /taxon/1006411 (Delphinus delphis) and www.mammaldiversity.org/taxon/1006861 (Delphinus bairdii), all returned by my WebSearches. eunis.eea.europa.eu/species/16445 redirected off-host and was not followed. No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns model summaries, so the quote was checked as MATCH/MISMATCH; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification.

## Bibliographic and licence

- Houser et al. 2022, fresh Crossref: Dorian S. Houser, Lauren Noble, Erin Fougeres, Jason Mulsow, James J. Finneran, in the recorded order; title "Audiograms and click spectra of seven novel and seldom-tested odontocetes" as recorded; Frontiers in Marine Science 9, article number 984333, no issue; issued and published online 2022-12-21; licence https://creativecommons.org/licenses/by/4.0/ (vor, from 2022-12-21); relation empty; no update-to. PDF (publisher's copy): "© 2022 Houser, Noble, Fougeres, Mulsow and Finneran." and "This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY)." Licence on the exact copy read: met (the note says so correctly, as audit 256 asked).

Bibliographic faults 0; licence faults 0.

## Names

- Kogia breviceps: MDD 1006459, Kogia breviceps (de Blainville, 1838), Kogiidae (status field blank on the page, as for the d171 cetaceans in audit 256); docs/views/gaps/gbif-names.tsv "Kogia breviceps EXACT ACCEPTED ... 2440694". Accepted. Family Kogiidae right; order "Cetacea" against MDD's Artiodactyla is main's convention, uncounted.

Name faults 0.

## Duplicates

- Kogia breviceps on main: sense_echolocation click parameters (oa-7:774 to 779 and their recheck copies, a 2018 Current Biology compilation, retracted in audit/ALL 7284 to 7289) and tapetum (mammal-groups:160, with Tursiops). No sense_hearing row for the species and no row from this paper under the species.
- Same paper on main: desk-d171:1 to 5 (Kogia sima, Stenella frontalis, Peponocephala electra, Lissodelphis borealis, Feresa attenuata), other species. Their notes and conditions do not carry a Kogia breviceps or pygmy sperm whale finding (grep of notes for "breviceps", "pygmy sperm", "capensis": none).
- docs/tracks: audit-256.md line 113 (Kogia breviceps listed as a lead, with the pathology caveat), desk-d171.md:24 and desk-d198.md:11 (Delphinus capensis leads). Leads, not evidence.

Duplicates 0. Contradictions 0.

## Per-paper findings

### Houser et al. 2022, Kogia breviceps (line 1)

Design (tool summary with verbatim fragments). Animal: "A neonate, female pygmy sperm whale (SWCKb1701b) stranded on La Jolla Shores Beach in San Diego, CA on 28 July 2017." (verbatim, as recorded); taken to SeaWorld San Diego; "Audiometric tests were performed the following day." Health: "Due to the animal's poor health status upon admission to the facility" the veterinarian gave ceftiofur, amikacin and enrofloxacin IM; "Amikacin has known ototoxicity (Griffin, 1988; Tange, 1998)", though the authors judge it "unlikely that the drug would have had sufficient time to affect cochlear function"; the animal died on 23 August 2017. No sedative is mentioned for this animal (tool summary). Testing: floating at the surface, transducer posterior to the mouth gape, electrode about 8 cm behind the blowhole; click-evoked ABRs and SAM-tone ASSRs; Table 1 test frequencies 40, 56, 80, 113 and 160 kHz (so the 153 kHz estimate is interpolated between 113 and 160 kHz, inside the tested range). Definitions confirmed: "The threshold was defined as the SPL of the lowest detected ASSR"; UFL "the highest frequency corresponding to an interpolated threshold of 120 dB re 1 µPa". Results 3.2: "A full audiogram was not obtained for the pygmy sperm whale."; best sensitivity at 80 and 113 kHz, thresholds higher than in the dwarf sperm whale. Discussion: the thresholds "were higher than expected based on experience with similar sized delphinids" and it "cannot be ruled out that the pygmy sperm whale might have had some underlying pathology affecting hearing." Caveats: received levels for "the smaller kogiids and delphinid neonates and adolescents are likely to be underestimated" given the 15 cm calibration distance.

Quote. MATCH: "The estimated UFL was 153 kHz, although this was possibly an underestimate given that the thresholds appeared to be higher than expected for an animal of this age and size." whole, the last sentence of Results 3.2, as `where` says. One sentence, one section, 30 words, no cuts, no mid-sentence start; contains 153 kHz and the qualifier; the value says no more than the quote. Quote-form 0.

Line 1. Counted (scientific context; animal health and pathology caveat omitted; fixable). The record's `conditions` says "sedation and testing details for this animal were not read", but the paper's Methods for this animal give a poor health status on admission, treatment with amikacin, which the authors cite as ototoxic, testing the day after stranding, and death 26 days later; the Discussion says underlying pathology affecting hearing "cannot be ruled out". The authors' own reason for calling 153 kHz a possible underestimate is that the thresholds were higher than expected, and the paper's candidate explanations for that are the animal's health, so a row that reads as the species' upper hearing limit without them misstates what the one measurement can carry. Audit 256 named this caveat in advance ("if logged, the authors' pathology caveat belongs in its conditions"). The fix belongs in `conditions` and `note`.

Uncounted, suggested:
- `method` names only SAM-tone ASSR; click-evoked ABRs were also recorded for this animal. Add.
- `conditions` "thresholds were higher than in the dwarf sperm whale" is right; the test frequencies (40 to 160 kHz, so 153 kHz is interpolated and below the highest tested) and the calibration-distance caveat for neonates belong there too.

Grade m right (one named species measured in the source); access open; `partial` false right (full text read). `eye` "inner ear (hearing)" and units "Hz" follow desk-d171's convention.

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Kogia breviceps, estimated UFL 153 kHz, possibly an underestimate | correct | conditions, note, method | Quote MATCH, citation, licence and name right; omits the animal's poor health on admission, ototoxic amikacin, death on 23 August 2017 and the authors' "underlying pathology affecting hearing" caveat, and says the testing details were not read |

Evidence errors: 1 of 1 (100%): scientific-context faults 1 (line 1); quote-form 0; name 0; duplicates 0; licence 0; bibliographic 0; abstract-access grading 0. Unfixable records: none.

Pooled with audits 172 to 285: 264 of 614 evidence records (43.0%; audit 285's 263 of 613, and 1 of 1 here). No search records, so nothing to pool with audits 83 to 90.

## Replacement text

Counted (line 1):
- `conditions`: "one neonate female pygmy sperm whale (SWCKb1701b, n=1) stranded on La Jolla Shores Beach, San Diego, California, on 28 July 2017 and tested at SeaWorld San Diego the following day, floating at the surface (no sedative stated); in poor health on admission and given ceftiofur, amikacin (cited by the authors as ototoxic, though judged unlikely to have affected the cochlea by test time) and enrofloxacin IM; died 23 August 2017; test frequencies 40, 56, 80, 113 and 160 kHz, so 153 kHz is interpolated below the highest tested; a full audiogram was not obtained; best sensitivity at 80 and 113 kHz, thresholds higher than in the dwarf sperm whale and higher than expected for similar-sized delphinids, and the authors cannot rule out underlying pathology affecting hearing; received levels for neonates likely underestimated (15 cm calibration distance); not a behavioural audiogram"
- `method`: "auditory evoked potentials (click-evoked ABR and SAM-tone auditory steady-state response); threshold defined as the SPL of the lowest detected ASSR; upper frequency limit defined as the highest frequency corresponding to an interpolated threshold of 120 dB re 1 µPa"
- `note`: append "Methods give poor health on admission, amikacin and death on 23 August 2017; the Discussion says underlying pathology affecting hearing cannot be ruled out, so the 153 kHz limit is one possibly impaired neonate's estimate, not a species limit."

## Held-out Delphinus capensis (owner question)

The decision not to file under Delphinus capensis is right; the stated reason and the owner question's proposed fix are not. The animals are Dc1304b, "stranded on a beach in San Diego, CA on 14 May 2013", and Dc1601b, which "stranded on a beach in Oceanside, CA" (verbatim, Methods). MDD 1006411 (Delphinus delphis) says "includes capensis and previously included D. bairdii", and MDD 1006861 recognises Delphinus bairdii Dall, 1873, "split from capensis (now a synonym of D. delphis)", distributed in the eastern Pacific from the Monterey and San Francisco Bay areas south through Baja California and the Gulf of California (type locality Seal Beach, Orange County, California). Southern California long-beaked common dolphins therefore fall under Delphinus bairdii on the mammal name authority audits use, not under D. delphis. Filing the Results 3.5 finding under D. delphis "with the long-beaked form noted" would put an eastern Pacific long-beaked result on a species MDD now limits to the other common dolphins. If the lead is filed: taxon Delphinus bairdii, a note that the paper uses D. capensis and that MDD 1006861 places California animals in D. bairdii, and the animal behind the sentence confirmed (my fetch gives "The UFL exceeded 160 kHz, which was the highest frequency tested." for the older animal, Dc1601b, about 3 years, tested on 19 June 2016 after a small dose of diazepam and dead three days later on 22 June, and "No UFL was identified in this animal either" for the younger Dc1304b; tool summary, the 116 dB figure the progress note gives was not checked). docs/views/gaps/gbif-names.tsv holds no Delphinus row, so the name needs adding through the owner before any record. The progress note's "the SMM taxonomy list (iucn-csg.org summary) lumps D. capensis into D. delphis" was not re-read here.

## Progress note

Accurate on the DOI, licence, n, date and name of the filed record and on the 153 kHz qualifier. It does not mention the animal's health, amikacin or the pathology caveat. The Delphinus capensis entry is corrected above. The other held-out leads were not re-checked (they are not filed records).

Verdict: 1 error in 1 (100%), above the 5% bar; pooled 43.0%. Error line: 1. No unfixable records; line 1 can merge with the counted text. Delphinus capensis: keep held out; if filed, file under Delphinus bairdii, not D. delphis.

This report is model output and carries no authority.
