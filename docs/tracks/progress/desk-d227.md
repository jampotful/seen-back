# desk-d227 progress

Scope: animal sensory records from open-access MDPI and PLOS pages, species checked absent from the whole docs tree (git grep by species and DOI, all folders) before each paper was opened. Crossref confirmed DOI, volume, issue, author order and licence for every DOI filed. Records are in docs/views/evidence/desk-d227.jsonl; check.py reports 0 problems for the unit. The page tool returned whole sentences only as fragments; each quote is the fragments joined, so an auditor should compare against the page text.

## Records (9, from 7 papers)
- Aromia bungii (Insects 10(9): 274), sense_chemical: male and female EAG responses similar to 90 volatiles, 17 differ; full range of mV, 5 antennae per sex, standard and mineral oil control in conditions.
- Phthonoloba viridifasciata (Insects 17(6): 554), sense_chemical: female EAG 0.387 mV (4-ethylbenzaldehyde) to 0.206 mV (decane); concentration and n not stated in the sentence.
- Rhoptroceros cyatheae (Int. J. Mol. Sci. 27(9): 4029), sense_chemical: males stronger than females for most of nine volatiles; nine of 13 EAD-active compounds tested, Abstract/Results mismatch (nine vs 13) stated.
- Tomicus yunnanensis (Biology 14(8): 1032), behaviour_vision: female peaks 360, 380, 700 nm, male 360, 400 nm; stimulus set in lux (not photon-matched), most beetles stayed in the start zone.
- Scyliorhinus canicula (Animals 11(1): 174), sense_hearing: sharks occupied the least noisy aquarium sections in playback; behavioural, speaker limited below 200 Hz, no particle motion.
- Nyctereutes procyonoides (Animals 10(2): 233), sense_hearing: BAEP waves I, II, III, V identified at 90 dB SPL only (no threshold).
- Glossina swynnertoni (PLOS NTD 12(9): e0006831), behaviour_vision: 0.5 m2 oblong targets not significantly lower than 1 m2 square; no blank control.
- Bufotes balearicus (Animals 12(19): 2603), two records: sense_chemical (activity falls to predator-fed odour, visual alone no effect) and behaviour_vision null (position unaffected by caged larva).

## Held leads and why
- Pholidobolus montium (Animals 11(11): 3022): opened, licence fine; the only visual evidence is leg-waving to conspecifics or a mirror (a display ethogram, not a sensory measurement).
- Gryllus assimilis phonotaxis (PeerJ 2: e437, 10.7717/peerj.437): usable open-arena sentence and design, but the founding colony is from Bastrop County, Texas, and Walker et al. 2009 restricted G. assimilis; species identity of the colony is an owner question. No issue number printed.
- Glossina fuscipes fuscipes (PLOS NTD 6(5): e1661): subspecies only; sentence on blue, UV and green reflectance read intact (Author Summary). Other tsetse papers (pntd.0003334, 0001491, 0003360, 0000474, 0007460) not opened.
- Animals 12:3537 (three anuran species, avian alarm calls): null behavioural response to heterospecific calls; says nothing about hearing, and Table 2 records a few escapes that the text denies.
- Rhoptroceros, Phthonoloba and the other d217 EAG leads: filed above. Not opened: Aulacophora foveicollis, Philaenus EAG, Miniopterus fuliginosus ABR (pubs.aip.org), Siganus/Arctocephalus/Betta/armadillo/gourami (already on main).
- Scyliorhinus Abstract sentence on swimming time (48 words) and Aromia results range sentence (47 words) exceed 40 words; shorter sentences used instead.
- Crossref `query=` with OR terms returns noise; topic discovery worked better through WebSearch restricted to mdpi.com, peerj.com and journals.plos.org.

## Owner questions
- Does the Gryllus colony count as G. assimilis (title and text say so)?
- Are subspecies such as Glossina fuscipes fuscipes and Glossina morsitans centralis fileable under the species name?
- Rhoptroceros cyatheae: title prints "Selandriidae: Rhopographus"; family given as Selandriidae.

## Desk disposition after audits 317 and 318

Audit 317 (lines 1-5): all five in error; lines 1-4 fixed, line 5 (Scyliorhinus canicula sense_hearing) held out and dropped because its Results contradict its Abstract and hearing is not separated from near-field detection. Audit 318 (lines 6-9): all four in error, all fixable. Replacement text applied; 8 records merged, check.py 0 problems. Rhoptroceros cyatheae filed under Tenthredinidae (paper's Selandriidae noted). Unchecked by auditors: taxonomic authority for Rhoptroceros cyatheae and Phthonoloba viridifasciata; Bufotes balearicus status (full species on sources read; a subspecies treatment exists; main's frog view lists none); several figures read from tool summaries (Tomicus Figure 6 range and df, Glossina Wilcoxon, raccoon dog session p values). Owner question: which authority settles Bufotes balearicus, and whether the frog view accepts it; Gryllus assimilis, Glossina fuscipes fuscipes, Pholidobolus and anuran alarm-call papers remain held.
