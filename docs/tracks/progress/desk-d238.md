# desk-d238

Records filed (6, `docs/views/evidence/desk-d238.jsonl`, check.py 0 problems):
1. Agalychnis callidryas, sense_light_nonvisual, hatching toward light (PeerJ 6: e6018, 10.7717/peerj.6018). Light not measured; side alternated, not randomised.
2. Xenopus laevis, behaviour_vision, individual tadpole green/light/dark preferences stable over days (Animals 16(17): 2717, 10.3390/ani16172717). Lab-bred; stimulus colours are Lab values on a monitor; no group-level statistic read.
3-4. Apis mellifera, sense_hearing, Johnston's organ: 20 nm flagellar tip displacement minimum response; 265-350 Hz mechanical sensitivity (PLoS ONE 2(2): e234, 10.1371/journal.pone.0000234). Measured stimulus; hive-comb bees plus foragers.
5-6. Gryllus bimaculatus, sense_hearing, phonotactic steering at 1-6 degrees and 12.9 dB binaural tympanic difference at 30 degrees (PLoS ONE 5(12): e15141, 10.1371/journal.pone.0015141). Lab colony, 75 dB SPL calibrated for the behaviour test.

Quotes 3-6 and 1-2 were returned by a summarising page tool; records 3, 4 and 5 are sentences returned in two abutting pieces in one response (said in pieces in `note`). Licence sentences for the two PLOS papers were read as summaries, not verbatim; Crossref CC BY 4.0 (unspecified version) on all.

Held leads and why:
- Lucilia cuprina / Chrysomya rufifacies green v yellow (Insects 17(3): 283, 10.3390/insects17030283): two Results sentences read intact in pieces (Ch. rufifacies preferred green, t = -15.23, p = 0.004; L. cuprina no difference, t = 1.61, p = 0.25) but the Methods are internally unclear (one valve closed yet two flasks lit; paired t-test on 3 replicates per configuration; calculated reflectance). Held for the owner.
- Honeybee 414 v 424 nm (pone.0048577): result sentence is 42 words and cannot be cut without dropping the CI.
- Salmo salar infrasound (pone.0063696): the key sentence's end was not confirmed by the tool; stimulus level not reported.
- Piranha operant colour test (Animals 14(22): 3187): two fish, no learning shown; not a measurement.
- Medaka SWS2 mutants (fgene.2020.00801): lab mutant lines, lambda max cited from earlier work.
- Gammarus spp. light (peerj.279): pooled genus.
- White shark electric deterrent (pone.0062730): Carcharodon electric already held out.
- Euschistus heros air-gap signalling (pone.0056503): result sentences over 125 characters returned truncated; no counts in text.
- Not reached (PLOS rate limit): bushcricket travelling waves pone.0031008, bumblebee colour learning pone.0071551, Aedes fruitless pbio.3004041.
- Already on main or in earlier units (found by DOI grep): Arctocephalus forsteri audiograms, Nyctereutes ABR, Sea turtle colour preference (ani15050628), many fish hearing papers (d160, d184, d216).

Owner questions:
1. Agalychnis record: confirm sense_light_nonvisual versus behaviour_vision for an embryo's light cue. Family Phyllomedusidae follows main's Thomas 2022 rows; other main rows say Hylidae.
2. DOI greps must include the MDPI journal codes (ani, insects, biology); `animals16...` style greps miss them.
3. Tool note: WebFetch on PLOS rate-limits after about 6 article fetches in a session and sometimes returns a different article's text for a printable-PDF URL.

## Desk disposition after audit 332

Audit 332 checked all 6 lines: 6 of 6 needed correction (omitted design, controls, statistics, calculated-versus-measured displacement); none unfixable. Replacement text applied. Agalychnis moved to behaviour_vision (ruling: eyed animals' phototaxis is filed there). Lab-bred Xenopus laevis, managed Apis mellifera and the Cambridge Gryllus bimaculatus colony accepted at species rank. 6 merged, 0 held out.
