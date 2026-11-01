# desk-d242

Evidence-only unit (vision, behaviour_vision). 4 records in docs/views/evidence/desk-d242.jsonl; `check.py` reports 0 problems. About 37 WebSearches. The niches assigned (hearing, electric, vibration, touch, thermal, ganglion cells, fovea, colour learning) are almost wholly worked by d143 to d241: nearly every PeerJ/PLOS/MDPI/Frontiers hit was already on main or in a progress note.

## Records
1. Thysanoessa inermis, erg_peak_nm: ERG spectral sensitivity curve peaked in the 470-490 nm region (Cohen et al. 2015, PLoS ONE 10(6) e0126247, 10.1371/journal.pone.0126247). Wild-caught Kongsfjorden krill, n = 5, 4.5 C, criterion response method; stimulus equal-quantum status, dark adaptation and wavelengths tested are not stated. Licence CC0 (page: free of all copyright; Crossref publicdomain/zero, vor). Whole sentence read in two abutting pieces on two passes.
2. Same paper, lambda_max_nm 492 nm: template best-fit rhodopsin to the ERG curve (modelled, not MSP); quote cut after the value (cut text carried in note).
3. Leucorrhinia intacta, behaviour_vision: mainly attacked 5 mm black bead rather than 12 mm (Duong, Gomez, Sherratt 2017, PLoS ONE 12(6) e0179483, 10.1371/journal.pone.0179483). Wild free-flying adults, field, 49 attacks from 131 presentations pooled over two species; individuals not marked; species x size interaction not significant (z = 1.539, P = 0.1238); community colour-pattern null carried as context. Quote is the 42-word sentence cut before its trailing figure reference.
4. Libellula pulchella, same paper and sentence: attacked both bead sizes; overall attack probability higher than L. intacta (z = -2.947, P = 0.0032). Each value confined to its own clause (audit 334).

## Held leads and why
- Papilio demoleus colour selection (insects 14(3) 249, MDPI): lab-reared from wild-collected eggs, percentages only with no test of the colour ranking; page tool declined the male and female sentences whole (longer than 125 characters). Held.
- Papilio xuthus colour choice (pone.0263709): breeding-population stock, inconsistent N across analyses, key sentence refused whole. Held.
- Thysanoessa inermis time-of-day ERG (pbio.3001413): Log K only in a figure, direction-only in text. Not filed.
- Lacerta agilis UV block (pone.0019360): reasons in desk-d232 unchanged (non-random assignment, effect fell short of significance); not retried.
- Odontocete retina (animals13213430): per-species table not readable; text unit conflict (per mm vs per mm2). Held.
- Not usable or off-niche: Sepia plangon courtship (fphys.2020.00845), cephalopod dynamic patterns (fphys.2017.00393), stomatopod central complex (fnbeh.2017.00012), box jellyfish opsin antibodies (lab culture, no measurement), Scylla light spectra (farm stock), ecotremology perspective, elephant geophone paper, Trachemys vocalisations (turtle-farm stock, no hearing measurement), Arctocephalus forsteri aerial audiograms (conservation6030099, already d193).
- Already on main or d22x/d23x/d24x: peerj 16602, 14230, 18491, 17962, 11248; pone 0147318, 0346423, 0057588, 0185353, 0192561, 0067049, 0037612, 0192865, 0037627, 0221659, 0146677, 0220652; fevo.2019.00352 not checked beyond search.

## Owner questions
1. Family/order for Thysanoessa inermis (Euphausiidae, Euphausiacea) come from main's other krill rows and a GBIF species page seen in search; WoRMS and OBIS could not be opened. Confirm.
2. Dragonfly sentence is 42 words; the cut drops only the trailing "(Fig 4)." and is marked with an ellipsis attached to the last word. Confirm that attachment counts as marking a cut.
3. erg_peak_nm for a range value ("470-490") with "new trait" in note: confirm a range string is acceptable for this key.

## Desk disposition after audit 337

Audit 337 checked all 4 lines: 4 of 4 needed correction (krill dark-holding and polar-night collection omitted; dragonfly sex effect credited to the wrong experiment, prey-size effect and sex x size null and temporal-block design omitted, "diameter" corrected to total length). Replacement text applied; 4 merged, 0 held out. Rulings: a 40-word cut quote with an attached ellipsis is allowed; a range value is written as a two-integer list [470, 490]; lambda_max_nm is acceptable for a template fit to an ERG curve.
