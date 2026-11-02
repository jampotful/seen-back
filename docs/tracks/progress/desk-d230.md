# desk-d230

Sonnet 5.5 desk unit. Four records filed in docs/views/evidence/desk-d230.jsonl, all checked (0 problems). DOIs and species were grepped against the whole docs/ tree and against the other units' evidence files before each filing. About 36 WebSearches used. The page tool returns only quotes of up to about 125 characters, which ruled out most candidates; each filed quote was returned whole.

## Records

1. Macropus eugenii, colour_vision, "dichromat" (Ebeling and Hemmi 2014, PLoS ONE 9(1) e86531, 10.1371/journal.pone.0086531). Quote is the Conclusions sentence (67 characters). Conditions carry: three wallabies in the study but one animal (Miller) in Experiment 3, intensity matching to a 540 nm pigment, brightness series, chance performance 480-487 nm (P>0.29), relative-before-absolute training, neutral point 484-487 relative and 480-483 absolute. Main had only lambda_max_nm and receptor_classes for this species.
2. Oophaga pumilio, behaviour_vision, males left perches when an approaching UV-A light was 26.8 cm away (Kats et al. 2012, PLoS ONE 7(12) e51364, 10.1371/journal.pone.0051364). Quote is one 126-character Results sentence. Conditions carry the light-off (16.7 cm) and visible-light (8.7 cm) comparators (from the page tool's summary of the next sentence, labelled as such), ANOVA F = 6.0, post-hoc P values (UV-A vs off P = 0.05), unmeasured UV-A at the perch, unknown visible leakage of the UV-A mode, no blinding stated.
3. Amalosia lesueurii, sense_thermal, preferred body temperature depends on feeding status (Abayarathna and Webb 2021, Front. Ecol. Evol. 9 727602, 10.3389/fevo.2021.727602). Qualitative value only because every numeric sentence exceeds 125 characters. Conditions carry the incubation-temperature null, F values, counterbalanced fed/fasted design, proxy body temperature, and two internal inconsistencies in the paper. Family/order from ALA/AFD.
4. Phymaturus tenebrosus, sense_thermal, mean Tpref 35.36 +/- 0.38 C, set-point 34.09-36.59 C (Cabezas-Cartes et al. 2019, PeerJ 7 e7437, 10.7717/peerj.7437). Quote is the whole Results sentence including "(Figs. 2 and 3)". N for Tpref not printed. Family from the Reptile Database entry.

Preferred-temperature gradient choice is filed under sense_thermal on the precedent of Callosobruchus maculatus on main.

## Held leads and why

- Delphinus capensis (Houser 2022, fmars.2022.984333): already held by d198 and audit 286 over the taxon name; not touched.
- Walleye scotopic ERG (peerj.21156): page would not open (client_error) in this unit too.
- NZ crab megalopae (pone.0028572): thresholds only in sentences over 125 characters; the paper also disagrees with itself on the H. sexdentatus threshold (126 vs 125 dB) and on which species was the Pakiri non-responder. Held.
- Dikerogammarus villosus / D. haemobaphes thermal preference (peerj.4871): page shows no author list or licence line and Crossref says "unspecified"; infection and sex confounds. Held.
- Iberolacerta galani and Podarcis bocagei Tpref (peerj.2085), Timon lepidus, Lacerta schreiberi, Psammodromus algirus, Podarcis guadarramae Tp (peerj.2107): all four are absent from main for sense_thermal, but the value sentences exceed 125 characters or are table rows. Table-row quoting has no recent precedent, so held. Both pages print the CC BY licence line.
- Nanorana pleskei Tpref (fevo.2021.763191): only clause fragments returned; no licence line on the page.
- Cnemaspis mysoriensis Tset (famrs.2024.1522805): the Tset sentence is 137 characters; held.
- Zdenek et al. 2023 snakes sound (pone.0281285): genus-level results, species not named in text. Held.
- Leatherback hatchling acoustic cues (pone.0253770): the Abstract says hatchlings may be unable to localise sound; only a small time-to-orient difference. No clean hearing value. Held.
- Greenland shark SMART hook (peerj.4751): deterrent field test, no response to a combined magnet and electropositive metal hook; ambiguous between sense_electric and sense_magnetic and similar to the held-out Carcharodon electric deterrent. Held.
- Newt UV (pone.0030391): journals.plos.org rate-limited every fetch; not read.
- Murre (Mooney 2019, JEB): Crossref licence is the Company of Biologists user licence, not open. Fratercula arctica from the same paper is already on main.
- Vespa velutina (Sci Rep hornet defence paper): no nature.com page found in search; PMC refused.
- Peafowl crest vibration (pone.0207247): measures resonance of detached crests, not a sensory response.
- Podarcis muralis acuity, Gelasimus dampieri, Sepia infrasound, Liolaemus, Paracentrotus: searches returned no open journal page I could read.

## Owner questions

1. Should preferred-temperature gradient trials be a standing sense_thermal source? Candidates above (peerj.2085, peerj.2107) would add six Iberian lizard species if table-row or longer-sentence quotes are allowed.
2. A qualitative value with a numeric-free quote (record 3) is thin. Say if such records should be dropped.

## Desk disposition after audit 323

Audit 323 judged all four records in error, all fixable. Applied for lines 1, 2 and 4 (Macropus eugenii colour_vision, Oophaga pumilio behaviour_vision, Phymaturus tenebrosus sense_thermal); 3 records merged, check.py 0 problems. Line 3 (Amalosia lesueurii sense_thermal) was held out: the audit's replacement quote is a 34-word Results sentence assembled from page-tool fragments with the dash and degree characters unconfirmed, and the filed direction-only value is not a measurement. Retry lead: re-read the Amalosia Results sentence whole from the Frontiers page and file with its numeric values (means 30.6 vs 25.8 C) and the feeding x hour interaction. Thermal ruling from audit 323: preferred body temperature in a gradient measures thermoregulatory preference, not thermosensation proper; main's convention (audits 280, 282) still files whole-animal gradient choice under sense_thermal with a preference label. Owner question: keep that convention or move gradient preference rows to a separate trait.
