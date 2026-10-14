# Precision audit 6, 14 October 2026

Two parts. (a) A random sample of 20 records from the newest sweeps (sweep-44 to sweep-48), each opened at its source and checked for value, grade and a verbatim quote. (b) The batch recheck that audit 5 left in progress, resumed at insects-met:24, then sweep-15, sweep-19, sweep-7 and sweep-17, skipping ids already corrected in `recheck-2.jsonl`, `recheck-4.jsonl` and `recheck-5.jsonl`.

Method as in audit 5: each source URL opened with WebFetch and asked first whether the exact quote string appears, then for the page's own sentence in consecutive pieces of at most about 125 characters (the summariser's cap), with split points recorded in `where`; corrected quotes are kept to 40 words or fewer. A page blocked by a bot wall, a proxy refusal (429) or a paywall hiding the passage is `unverifiable`, never guessed; repository copies are tried where PMC, Elsevier or Wiley block, and link.springer.com where doi.org is refused. Verdicts: `confirm`, `requote` (value right, quote not on the page), `correct` (value, grade, partial flag or source metadata changed), `retract` (the page does not support the value). Opsin-inferred and family-level claims are held to `g` at most; a sampling time is not a diel rhythm. Typographic differences (spacing artefacts, curly quotes, dashes, degree signs) and verbatim table-column readings count as `confirm`, as in audits 2 to 5. A quote that is an unpunctuated verbatim substring of a longer sentence is `confirm`; a quote that adds a full stop where the page's sentence continues is a `requote`. Corrections go to `docs/views/recheck/recheck-6.jsonl` in the recheck-5 schema; no evidence file is edited.

## Part (a): random sample of sweep-44 to sweep-48

sweep-45 has no records (its run stopped on 429s before writing any), so four records were drawn from each of sweep-44, sweep-46, sweep-47 and sweep-48, and four more from the remainder of those files (Python `random`, seed 20261014). Fifteen of the twenty are abstract-level partial records.

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
| sweep-44:6 | Triteleia laxa / sense_light_nonvisual | m | confirm | quote verbatim in the abstract; 18 degrees C in short photoperiods confirmed |
| sweep-44:5 | Bouteloua curtipendula / sense_light_nonvisual | m | confirm | quote verbatim (point 2 of the abstract); critical photoperiod "between 14 and 141/2 hours" confirmed |
| sweep-44:2 | Syringa vulgaris / sense_chemical | m | confirm | sentence verbatim but for the page's spacing artefacts ("S. o blata" as returned against "S. o b lata" in the quote); more than 70 % and 'Bright Centennial' confirmed |
| sweep-44:7 | Scolopax minor / absolute_sensitivity | m | requote | value confirmed; the quote is the middle clause of a sentence that opens "Although they have low rod density compared to that of stilts and plovers," and continues "but rank midway between plovers and dowitchers for the b-wave amplitude." |
| sweep-46:13 | Arctotheca calendula / sense_light_nonvisual | m | confirm | clause verbatim in the abstract |
| sweep-46:8 | Hypoxis hemerocallidea / sense_light_nonvisual | m | confirm | sentence verbatim in the abstract |
| sweep-46:10 | Serenoa repens / sense_chemical | m | confirm | sentence verbatim in the introduction |
| sweep-46:9 | Scirpus lacustris / sense_light_nonvisual | m | confirm | sentence verbatim in the abstract (repository page) |
| sweep-47:6 | Circaetus gallicus / fov_h_deg | m | confirm | verbatim opening of the sentence, which continues ", and the blind area above and behind the head reaches maximum width of 100°" |
| sweep-47:9 | Hylotelephium spectabile / sense_light_nonvisual | m | confirm | first sentence verbatim; 0 to 1 d, 2 to 10 d, after 11 d under 20 h confirmed |
| sweep-47:3 | Caladenia crebra / sense_chemical | m | confirm | sentence verbatim in the abstract |
| sweep-47:5 | Polybia occidentalis / colour_vision | m | confirm | last sentence verbatim; CB card discriminated from cards of similar brightness confirmed |
| sweep-48:3 | Mus musculus / fov_h_deg | m | confirm | verbatim in the Figure 6 caption (panel B) |
| sweep-48:2 | Mus musculus / binocular_deg | m | confirm | verbatim in Results, Transformation to visuotopic coordinates; sentence continues "slightly larger than the 30–40° of Dräger and Hubel" |
| sweep-48:4 | Spheniscus humboldti / spectral_range_nm | m | confirm | verbatim in section 3.1.9 (Retina) of a review, cited to ref. 83 (Bowmaker and Martin); already `partial: true` |
| sweep-48:5 | Puffinus puffinus / fov_h_deg | m | confirm | sentence verbatim in the abstract |
| sweep-47:2 | Bothrops atrox / receptor_classes | g | confirm | sentence verbatim; RH1, LWS full length and most of SWS1 confirmed; opsin-inferred, held at `g` already |
| sweep-47:1 | Bothrops jararaca / fovea | m | confirm | sentence verbatim; juvenile ventral-retina sentence confirmed |
| sweep-46:6 | Nereocystis luetkeana / sense_light_nonvisual | m | confirm | clause verbatim; Fv/Fm fell 40% after 60 min and recovered within 8% after a 300-min dim period confirmed |
| sweep-46:5 | Fulmarus glacialis / acuity_cpd | m | confirm | verbatim in Results, Retinal ganglion cell density and spatial resolving power |

**Part (a) rate: 1 error in 20 verifiable records, 5%** (0 unverifiable). The one error is the clause-cut shape audit 5 named (pattern 2), not the summariser rebuild. The newest sweeps, which asked the fetch tool for the sentence verbatim in pieces, run far cleaner than the old batches (34% to 74% in audit 5).

## Part (b): batch recheck

### Batch table

| batch | due | records checked | errors | error rate | unverifiable | status |
|---|---|---|---|---|---|---|
| insects-met (24 on) | 28 | 0 | 0 | n/a | 0 | in progress |
| sweep-15 | 13 | 0 | 0 | n/a | 0 | not started |
| sweep-19 | 19 | 0 | 0 | n/a | 0 | not started |
| sweep-7 | 16 | 0 | 0 | n/a | 0 | not started |
| sweep-17 | 12 | 0 | 0 | n/a | 0 | not started |

Error rate is errors over verifiable records (checked minus unverifiable).

### Records

| id | taxon / trait | grade | verdict | note |
|---|---|---|---|---|
