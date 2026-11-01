# desk-d192 progress

Animal sensory-trait records from open-access MDPI papers (the plant brief was superseded).

Records filed: 10 in docs/views/evidence/desk-d192.jsonl, from 5 papers (all CC BY, DOIs checked on Crossref).
- Asiophrida xanthospilota, Insects 15(7):532 (2 ERG records, including a sex-difference exception)
- Exolontha castanea, Agronomy 12(2):481 (2 phototaxis records, equal-lux confound noted)
- Anoplophora glabripennis, Insects 14(5):465 (1 peak record, 1 null result on intensity)
- Endebius florensis, Biomimetics 10(8):513 (phototaxis and ERG)
- Octopus vulgaris, Animals 10(3):457 (visual-only choice, chemical against visual)

Held out or skipped:
- Green turtle hatchlings (PeerJ 5572), Vespinae LED wavelengths (Animals 14:1543), Anoplophora opsins: already on main.
- Pholidobolus montium (Animals 11:3022): sentences came back only as fragments or mid-sentence cuts.
- zendy.io copy of a JEB paper: fetch denied by the permission classifier, not retried.
- JEB rattlesnake pit paper (jeb.065896): no open licence statement on the copy read.
- Hai 2013 Sensors silk moth/honeybee review: not filed (review; honeybee Johnston's-organ sentences not checked against main in detail).

Caveats: the fetch tool returns quotes in fragments; every filed quote was relayed as a complete sentence (joined from parts where noted in the record). GBIF was unreachable, so accepted status of Exolontha castanea, Asiophrida xanthospilota and Endebius florensis was not checked.

## Desk disposition after audit 276

Audit 276: 9 of 10 records in error (90%; lines 1, 2, 4 to 10). Line 10 (Octopus vulgaris chemical-cue choice) is a repeat of main's docs/views/audit/corrected/sea-invertebrates.jsonl:119 and was dropped. The other nine merged with the auditor's replacement text and uncounted fixes. Pooled audits 172 to 276: 236 of 568 (41.5%).

- Equal-lux stimuli are now stated on the ERG and phototaxis rows; Anoplophora line 5 no longer claims equal 180 lx; the Exolontha female quote is the full sentence; lines 3 and 4 carry family Scarabaeidae with the printed Melolonthidae in the note.
- Names unverified on a reachable authority: Asiophrida xanthospilota and Endebius florensis; Exolontha castanea has no status shown in the GBIF backbone mirror.

Owner questions: whether broad-colour ERG response ranks belong under spectral_range_nm rather than colour_vision (main is mixed); whether lux-matched stimuli must always be stated in conditions; whether main's sea-invertebrates:119 should be requoted (its quote is cut mid-parenthesis without a mark); whether the next unit should file the Asiophrida phototaxis result as a lead.
