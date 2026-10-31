# desk-d228: animal sensory evidence, lateral search

Nine records in docs/views/evidence/desk-d228.jsonl (`python3 -I tools/senses/check.py docs/views/evidence/desk-d228.jsonl`: 9 records, 0 problems). Every species and DOI was grepped across the whole docs tree before the paper was opened. Page text came through WebFetch (whole sentences only up to about 125 characters, longer Abstract sentences read as adjoining fragments and checked for punctuation); DOIs, authors, volume and issue verified on api.crossref.org.

## Records
1. Trypodendron lineatum, sense_chemical (Front. Physiol. 14: 1155129, 10.3389/fphys.2023.1155129): 37 of 90 strongly responding OSNs best to lineatin. Beetles came from lineatin-baited traps; Methods say 187 sensilla, Abstract 170. Licence: Crossref CC BY 4.0 vor.
2. Ips acuminatus, sense_chemical (Front. For. Glob. Change 8: 1588866, 10.3389/ffgc.2025.1588866): class IAc6, >80 Hz to alpha-isophorone (n = 6; preceding sentence says n = 7 and females only). Licence: Crossref CC BY 4.0 vor. Title assembled from two halves on the AGRIS record.
3. Neolamprologus pulcher, behaviour_vision (PeerJ 7: e8149, 10.7717/peerj.8149): attack playback produced responses much like a live predator (aggression only; attentiveness differed).
4. Neolamprologus pulcher, sense_chemical: chemical cues had no effect (null; combined visual plus chemical assay).
5. Porichthys notatus, sense_hearing (PLoS ONE 8(12): e82182, 10.1371/journal.pone.0082182): larval behavioural thresholds 140 to 150 dB re 1 uPa below 225 Hz.
6. Aquatica ficta, behaviour_vision (PLOS ONE 13(2): e0191576, 10.1371/journal.pone.0191576): flash changes at 533 nm and below; 533 nm dim-light intensity p = 0.066; no effect at 597 nm and above; six males.
7. Magallana gigas, sense_hearing (PLOS ONE 12(10): e0185353, 10.1371/journal.pone.0185353): valve-closure threshold 0.02 m s-2 at 122 dB rms re 1 uPa, 10 to 80 Hz.
8. Tomicus yunnanensis, behaviour_vision (Biology 14(8): 1032, 10.3390/biology14081032): phototaxis peaks by sex; stimuli matched in lux, not photons.
9. Oryctes rhinoceros, behaviour_vision (Insects 16(2): 170, 10.3390/insects16020170): beetles avoided panel traps with visible LEDs; all traps pheromone-baited; amber in the cup raised catch.

## Held leads and why
- Podarcis muralis acuity (jeb249422), Gelasimus dampieri (jeb230979), Sepia infrasound (jeb166074): no publisher page reachable (search returned only repositories; Biologists licence is not CC BY).
- Miniopterus fuliginosus ABR (10.1121/1.5079904): Crossref CC BY 4.0 vor, but only third-party and repository copies appeared in search; the Crossref abstract is paraphrase only through the tool.
- Mooney murre, pit viper thermography, Athetis, Empoasca, Papilio hospiton, Phthorimaea, Paracentrotus, Troides, Oligota/Parastethorus, Liolaemus, Crematogaster, Haemaphysalis, Carausius, Odontoponera, Acheta, Thamnophis, Maylandia, Cosmopolites, Rana aurora, Principapillatus, Holotrichia, Orchestes, Batocera, Bruchophagus: not retried; held reasons are in desk-d218 to d226 and are unchanged (sentences over the tool limit, no licence line, pooled results).
- Rhodnius prolixus bite targeting by heat (PLoS ONE, 10.1371/journal.pone.0000932): species already has sense_thermal on main.
- Carcharodon carcharias electric deterrent (PLoS ONE 8(5): e62730): effect on interaction distances, field strength not mapped (Discussion "105 V/m" conflicts with measured 105 V); no whole sentence carries a threshold.
- Harp seal vibrissae (PLoS ONE, 10.1371/journal.pone.0054876): excised cadaver vibrissae, biomechanics rather than a sensory measurement.
- Gromphadorhina portentosa (PeerJ 19805): habituation and a null odour-conditioning result; no sensory threshold, not filed.
- Hemigrapsus/NZ crab megalopae sound thresholds (pone.0028572) and Pacific oyster light sensitivity (pone.0140149): journals.plos.org rate-limited every fetch after the first few; open leads, both absent from main by DOI.
- Babina daunchina hearing (pone.0045792): species already on main.
- Crossref list queries: only the PeerJ prefix returned usable lists (fish hearing); the others returned client errors or rate limits.

## Owner questions
- Quotes for records 2, 7, 8 and 9 are Abstract sentences longer than the tool limit, read as adjoining fragments (record 9 confirmed twice with punctuation). Say if reassembled sentences should be re-read by an auditor on a full page.
- MDPI pages show CC BY 3.0 metadata against Crossref CC BY 4.0 (records 8, 9); filed as CC BY.
- Neolamprologus pulcher stock is a five-generation laboratory colony; filed at species rank as main does for laboratory colonies.
- Magallana gigas: family Ostreidae and order Ostreida are from general knowledge (WoRMS and GBIF not reachable).
