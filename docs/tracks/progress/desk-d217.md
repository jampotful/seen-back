# desk-d217 progress

Scope: animal sensory-trait records from open full text (PeerJ, PLOS ONE, MDPI Insects and Fishes). Records are in docs/views/evidence/desk-d217.jsonl; check.py reports 0 problems for the unit. Species and DOI were checked against origin/main (evidence, audit/ALL, audit/corrected, sheets, progress notes) before opening each paper. Every page was read through a page-summary tool that returns quotes only up to about 125 characters, so only whole short sentences were filed.

## Records (12)
- Blattella germanica, sense_chemical: mean EAG response 0.23 mV to DEET (PeerJ 4: e2150).
- Drosophila suzukii, sense_chemical: more summer-morph than winter-morph flies entered food-odour traps (PeerJ 10: e13825); morph comparison, not a threshold.
- Cyprinus carpio, sense_magnetic: spontaneous North-South body alignment in market tubs (PLoS ONE 7: e51100); field correlation, inflow tubs excluded.
- Larimichthys crocea, sense_chemical: EOG detection thresholds 10^-11 (cholic acid) and 10^-12 mol/L (chenodeoxycholic acid) (Fishes 8: 26).
- Hyphantria cunea, sense_chemical: female antennae more sensitive than male to beta-ocimene and cis-2-penten-1-ol (Insects 7: 19).
- Triatoma rubida, sense_chemical (nymph CO2 choice) and behaviour_vision (adults responded to all wavelengths) (Insects 8: 90).
- Cimex lectularius, sense_chemical: attraction to host-breath chemicals (Insects 2: 22).
- Lobesia botrana, sense_chemical: female EAG to pheromone lower than or equal to plant odorants (Insects 10: 281).
- Dastarcus helophoroides, sense_chemical: male-only dose-dependent EAG to (S)-(-)-alpha-pinene (PLoS ONE 12: e0190067).
- Eptesicus fuscus, sense_magnetic: magnetite-based detection of the Earth's field (PLoS ONE 3: e1676); quote joined from two consecutive fragments.
- Sclomina erinacea, sense_chemical: male Y-tube attraction to nonanal, beta-myrcene, trans-2-hexenal (Insects 12: 978).

## Held out
- Philaenus spumarius EAG (PLoS ONE pone.0190454), Aulacophora foveicollis (Agronomy 12: 2640), Phthonoloba viridifasciata (Insects 17: 554), Rhoptroceros cyatheae (IJMS 27: 4029), Bemisia tabaci phototaxis (Insects 17: 661): not opened or PLOS fetch rate limited; open for another unit.
- Jumping spider categorisation (pone.0097819): the fetch returned a different article; not read.
- Aromia bungii EAG (Insects 10: 274): only usable Abstract sentence is generic (olfactory system sensitive to concentration and structure); the numeric sentences exceed the quote limit.
- Sogatella furcifera (PeerJ 6576), rainbow trout sight or smell (PeerJ 1169), lumpfish magnetic coil (PeerJ 14745), Phyllostomus masking (PeerJ 10551), bullfrog rheotaxis (pone.0166989): no whole sentence under the limit that states the value.
- Mysis relicta lambda max (pone.0088107): values cited from earlier work, not new measurements.
- Already on main, skipped: Octopus vulgaris chemical vs visual, Siganus guttatus hearing, Leptophobia aripa, Chelonia mydas colour, Lycorma delicatula EAG, Spodoptera frugiperda blue light, Adoxophyes orana, Strongylocentrotus intermedius, Dasypus ABR, Trichopsis vittata, Arctocephalus forsteri, fur seal and odontocete audiograms, elasmobranch pulsed electric fields.
- Review articles skipped (African mole-rat bone conduction, Audiology Res 15: 64).

## Owner questions
- MDPI pages (Insects 7: 19, 8: 90, 10: 281, 12: 978; Fishes 8: 26) print a CC BY 3.0 metadata URL while Crossref lists CC BY 4.0; both are CC BY. Records are filed with the mismatch flagged in the note; remove if a version mismatch counts as a conflicting tag.
- Dastarcus (PLoS ONE 12: e0190067): the page read printed no licence line; CC BY 4.0 is from Crossref only.
- Larimichthys crocea order is given as Acanthuriformes (current GBIF/Fishbase); older sources say Perciformes.
- Larimichthys, Eptesicus and Cyprinus quotes were joined from consecutive tool fragments (flagged in each note); none was seen in one piece.
- Hyphantria cunea is filed from a sentence that the tool returned whole once; a second look would confirm it.
- Names were not checked against WoRMS or GBIF (refused to this unit).

## Desk disposition after audits 302 and 303

Audit 302 (lines 1 to 6): 4 of 6 in error (66.7%), 5 faults. Audit 303 (lines 7 to 12): 4 of 6 in error (66.7%), 4 faults. Combined for d217: 8 of 12 (66.7%), all fixable and corrected with the auditors' replacement text; no record dropped. Pooled audits 172 to 303: 313 of 713 (43.9%).

Errors: Drosophila suzukii (no unbaited control trap, dead flies in the denominator, trap-height bias); Larimichthys crocea (20 trials of five fish rather than 20 fish, no threshold criterion, Y-maze side not randomised); Hyphantria cunea (sex comparison is on values normalised to nonanal); Triatoma rubida CO2 (quote dropped "(Figure 2a)" unmarked); Triatoma rubida light (only 470 and 390 nm beat the no-light control, the value had said all wavelengths); Cimex lectularius (null results left out, breath source was one experimenter); Lobesia botrana (contrary Conclusions line and a 1,000-fold dose difference left out); Eptesicus fuscus (sham, release order and the axial result not stated). Blattella, Cyprinus, Dastarcus and Sclomina merged with uncounted fixes.

Owner questions: names for gbif-names.tsv (Triatoma rubida, Lobesia botrana, Sclomina erinacea Reduviidae, Drosophila suzukii, Blattella germanica, Cyprinus carpio, Larimichthys crocea, Hyphantria cunea; Cimex lectularius, Dastarcus helophoroides and Eptesicus fuscus already resolve); Larimichthys crocea order Acanthuriformes (Fishes of the World 5th ed. via taxobox); year of Fishes 8(1):26 set to the printed 2023 (Crossref issued 2022-12-30), so the convention is printed year; MDPI CC BY 3.0 page metadata against CC BY 4.0 on Crossref accepted as a version difference; Dastarcus page prints no licence line (Crossref CC BY 4.0, accepted); main's bat sheet carries Holland et al. 2006 (Nature, 10.1038/444702a) as an Eptesicus magnetic-compass row with no evidence row, so the Eptesicus pulse record is main's first evidence row for the species and the 2006 paper could be filed too (different claim); the Triatoma pair of records is kept as two (light and CO2).
