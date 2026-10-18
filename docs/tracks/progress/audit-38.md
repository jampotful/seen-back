# Precision audit 38, 18 October 2026

Scope: the latest version of each record in `docs/views/evidence/recheck-42-fixed.jsonl` to `recheck-52-fixed.jsonl`. A record retracted in `docs/views/audit/ALL.jsonl` is replaced by its correction in recheck-53-fixed (journal), recheck-54-fixed (grade), recheck-55-fixed (strict review), recheck-56-fixed (journal) or recheck-57-fixed (Emerling issue); a retraction with no correction removes the record. Six records were removed this way (recheck-54-fixed:52 and :117, recheck-46-fixed:34, recheck-49-fixed:26, recheck-53-fixed:213, recheck-52-fixed:43), which leaves 493 records. `docs/views/fixes/requote-partial.jsonl` was applied as an override that sets `partial` to true. Records that audits 33 to 37 checked (by id, and through the correction chain to the origin id), and Kott 2010, were skipped, which leaves a pool of 340.

Draw: `random.seed(38)`, `random.sample` of 35 from the pool (file order, then line order). The first 20 are the audit sample. They sit in recheck-53 to 57 files and trace back to origin files 42, 43, 45, 47, 49, 50, 51 and 52 (8 origin files). Because the first 20 held errors, the other 15 were checked as well.

Method as in audit 16: WebSearch on the title, then WebFetch on a URL the search returned. The fetch tool returns about 125 characters per quote, so every quote was read back in consecutive pieces. No library login, proxy, Sci-Hub, LibGen, academia.edu or ResearchGate page was opened, and no paper text is committed. Pages that showed a bot check or a permission block (PMC, PubMed, Springer for some tries, Annual Reviews) count as not opened. An error is any one fault: quote not verbatim or not one complete sentence (or marked cuts), a value or grade the quote does not support, a missing `partial: true`, an incomplete author list, or a journal field lacking name, volume, pages or issue. One fault per record counts once.

## First 20

| # | record | taxon / trait | grade | verdict | note |
|---|---|---|---|---|---|
| 1 | recheck-57-fixed:42 | Alligator sinensis / opsin_status | g | confirm | verbatim and complete (Whittier PDF). "Both genes" points back to OPNPP and OPNPT in the previous sentence; noted, not counted. 34(3): 666-676 |
| 2 | recheck-54-fixed:102 | Stellaria media / sense_light_nonvisual | g | unverifiable | PubMed redirect and the permission request went unanswered; no other page returned |
| 3 | recheck-54-fixed:111 | Otus asio / dark_adaptation_time_min | g | confirm | verbatim and complete (Results, Dark Adaptation; both owls, so `g`); 18(2): 62-66 |
| 4 | recheck-51-fixed:9 | Falco sparverius / acuity_cpd | g | error (journal) | verbatim with marked cuts (Silverchair page); Hirsch 1982 value, so `g`. Journal field "Journal of Experimental Biology219:2639-2649" lacks the issue (219(17)) and a space |
| 5 | recheck-47-fixed:70 | Anolis carolinensis / lambda_max_nm | g | confirm | opens as quoted on the Frontiers page ("lmax of 625nm" as printed); cited value (Provencio 1992), `g`; 2: 1410763 |
| 6 | recheck-54-fixed:4 | Paratrigona opaca / eye_topography | g | confirm | verbatim and complete (Springer full text); pooled result for all investigated species, so `g`; three authors |
| 7 | recheck-55-fixed:21 | Ophiocoma wendtii / behaviour_vision | m | error (quote) | the abstract on the Bristol page reads "We show that, although both species ..."; the quote drops the comma after "that". Species-level result, `m` is right; four authors; 30(2): 319-327.e4 |
| 8 | recheck-54-fixed:56 | Hasarius adansoni / opsin_localization | g | error (value) | sentence verbatim with a leading ellipsis (NSF copy). The quote gives RH1 proximal and RH3 distal in all three species; the value "RH3/RH4: distal tiers 3 and 4" adds RH4, which the quote does not state |
| 9 | recheck-47-fixed:48 | Pisum sativum / sense_light_nonvisual | g | confirm | verbatim and complete (Frontiers PDF, Pea, Induced Mutants); review, `partial` true. The authors field prints "Weller James L, Ortega Raúl" (surname first), a slip noted before and not counted |
| 10 | recheck-57-fixed:19 | Chrysemys picta / opsin_status | g | confirm | verbatim and complete; two-species statement, `g`; 34(3) |
| 11 | recheck-53-fixed:50 | Habrocestum africanum / opsin_localization | m | confirm | the sentence reads as quoted up to "suggesting a complex"; the closing "(Figs. 1, 4)" was not read back. Species-level, `m` |
| 12 | recheck-57-fixed:7 | Pelodiscus sinensis / opsin_status | i | error (value) | verbatim and complete. The quote supports pseudogenization or neofunctionalization only; "assembly error" in the value comes from a later sentence ("While this anomaly may be due to an assembly error") |
| 13 | recheck-53-fixed:220 | Deilephila elpenor / superposition_pupil_facets | m | confirm | verbatim, p. 821, 26(6): 821-826, three authors. `partial` is true on a full-text research sentence; over-flagged, not counted |
| 14 | recheck-53-fixed:190 | Sabellidae / eye_role | g | error (partial) | verbatim and complete (Nilsson 2013). The paper is a Perspective review and earlier records from it carry `partial` true; this record has none |
| 15 | recheck-53-fixed:140 | Streptophyta / lambda_max_nm | g | unverifiable | LSU, Duke and Cologne pages give the abstract only, PMC and Europe PMC did not open |
| 16 | recheck-53-fixed:191 | Polyplacophora / eye_type | g | error (partial) | verbatim and complete (Nilsson 2013, chitons named in the previous sentence); same review, no `partial` |
| 17 | recheck-57-fixed:29 | Alligator mississippiensis / opsin_status | g | confirm | verbatim and complete; four-species statement, `g`; 34(3) |
| 18 | recheck-53-fixed:170 | Drassodes cupreus / eye_role | g | error (partial) | verbatim and complete (R979; the species is named in the sentence before). A Current Biology magazine article ("Spider vision", R975-R980) with no `partial` |
| 19 | recheck-55-fixed:29 | Spodoptera exempta / lambda_max_nm | g | confirm | verbatim with "(127)"; review, `partial` true |
| 20 | recheck-57-fixed:2 | Pelodiscus sinensis / opsin_status | g | confirm | verbatim and complete; four-species statement, `g` |

First 20: 2 unverifiable, 18 verifiable, 7 errors (none journal-only except 4).

## Extension (15 more)

| # | record | taxon / trait | grade | verdict | note |
|---|---|---|---|---|---|
| 21 | recheck-54-fixed:71 | Dendrobates auratus / opsin_gene_recovery | g | error (authors, value) | sentence verbatim and complete (UCL PDF); four dart-frog species including D. auratus, `g`. The authors field reads "Schott RK, Fujita MK, Streicher JW, Gower DJ, Thomas KN, Loew ER, et al., Bell RC", which is not a complete list. The value adds "functional" and "potential gene loss supported", which "lacked SWS2" does not state |
| 22 | recheck-53-fixed:93 | Photuris versicolor / filter_pigments | g | error (partial) | verbatim with a closing marked cut (QMUL PDF); Annual Review with no `partial` |
| 23 | recheck-57-fixed:23 | Chelonia mydas / opsin_genes | g | confirm | verbatim and complete; two-species statement, `g` |
| 24 | recheck-49-fixed:27 | Ictidomys tridecemlineatus / filter_pigments | g | confirm | verbatim ("N-actetylated" as printed); diploma thesis, `partial` true; cited study, `g` |
| 25 | recheck-55-fixed:67 | Deinopis spinosa / sense_hearing | g | confirm | verbatim, the leading ellipsis marks the cut of "As with field trials,"; five authors; 30(24): 5033-5039.e3 |
| 26 | recheck-55-fixed:39 | Bubo virginianus / oil_droplets | g | confirm | verbatim ("3.0 pm" as the PDF prints it). The page shows no issue number for 8: 25-34; noted, not counted |
| 27 | recheck-53-fixed:3 | Scaura argyrea / eye_type | g | confirm | verbatim and complete (Introduction); group statement, `g` |
| 28 | recheck-54-fixed:116 | Trachemys scripta / behaviour_vision | g | error (journal) | abstract sentence verbatim, two species so `g`, `partial` true. Journal field "Journal of comparative psychology (Washington, D.C. : 1983)" has no volume or pages |
| 29 | recheck-55-fixed:66 | Deinopis spinosa / auditory_strike_responders | g | confirm | verbatim and complete (Results, Laboratory Behavioral Assays) |
| 30 | recheck-53-fixed:116 | Homo sapiens / receptor_classes | g | error (partial) | verbatim (Pingelap sentence, QMUL PDF); Annual Review with no `partial` |
| 31 | recheck-45-fixed:67 | Uta stansburiana / sense_light_nonvisual | g | confirm | verbatim; the lizard is named in the sentence before ("In the latter case"); noted, not counted. 7(6): e39003 |
| 32 | recheck-54-fixed:59 | Habrocestum africanum / opsin_localization | g | confirm | same sentence as #8, supports RH1 proximal for all three species |
| 33 | recheck-55-fixed:74 | Urtica dioica / sense_touch | m | confirm | Discussion sentence, read as "we have demonstrated for the first time that Urtica dioica exhibits changes in leaf geometry"; the opening "In our study," was not read back. Six authors; 260(2): 46 |
| 34 | recheck-57-fixed:24 | Chelonia mydas / opsin_status | g | confirm | same sentence as #10 and #23 |
| 35 | recheck-55-fixed:50 | vertebrate SWS1 / lambda_max_shift_nm | g | error (quote) | the page sentence continues past "respectively" (to the Malpolon monspessulanus and Pantherophis guttatus remark and a full stop); the quote stops there with no ellipsis. Ten authors match |

Extension: 0 unverifiable, 15 verifiable, 5 errors (1 journal-only: 28).

## Error rate

- Verifiable records: 33 (35 drawn, 2 unverifiable). Errors: 12 (7 in the first 20, 5 in the extension), or 36.4%.
- Excluding journal-only faults (records 4 and 28): **10 errors in 33, 30.3%**. Record 4 has only the journal fault; record 28 has only the journal fault.

## Distinct fault patterns

1. Missing `partial: true` on a review, Perspective or magazine source: recheck-53-fixed:190, :191 (Nilsson 2013), :170 (Morehouse 2020), :93, :116 (Briscoe and Chittka 2001). Five of the 12 errors. The overrides in `requote-partial.jsonl` cover other records from the same papers but not these.
2. Value wider than the quote: recheck-54-fixed:56 (RH4 added), recheck-57-fixed:7 ("assembly error" added), recheck-54-fixed:71 ("functional", "potential gene loss supported").
3. Journal field without issue, volume or pages: recheck-51-fixed:9 (no issue, JEB 219(17)); recheck-54-fixed:116 (no volume or pages).
4. Incomplete author list ("et al."): recheck-54-fixed:71.
5. Quote ends mid-sentence with no ellipsis: recheck-55-fixed:50.
6. Quote differs from the page in punctuation: recheck-55-fixed:21 (comma after "that").

Noted, not counted: "Both genes" and "the latter case" and "These receptors" quotes whose subject sits in the previous sentence (57-fixed:42, 45-fixed:67, 53-fixed:191); surname-first authors (47-fixed:48); `partial` true on a full-text research sentence (53-fixed:220); no issue shown for Histology and Histopathology 8 (55-fixed:39).

## The "(10)" marker in recheck-53-fixed:109

The Briscoe and Chittka PDF on the QMUL lab site, whose Figure 6 caption is on p. 488, reads "Several distinct opsin cDNAs or genes from the same organism have been isolated (e.g. three from Apis mellifera and Manduca sexta ...)". It has no "(10)" after "organism". The Annual Reviews page itself would not open, so the publisher's printed page is unchecked. On the evidence of the author-hosted copy, the marker is not on the printed page, and the record's quote is not verbatim.

## Unverifiable

recheck-54-fixed:102 (Hartmann 2005, PubMed blocked) and recheck-53-fixed:140 (Li 2015, only abstract pages opened).
