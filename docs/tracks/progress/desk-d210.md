# desk-d210 progress

Scope: animal sensory-trait records from open-licence papers; coverage map built from docs/views (evidence, audit/ALL, audit/corrected) before searching.

## Coverage map (main at d208)
- Plecoptera, Psocodea, Siphonaptera, Syngnathiformes, Gobiiformes: no rows on main.
- Erinaceidae: only Erinaceus europaeus ocular_media and orbit_convergence; no hearing.
- Uranotaenia: none. Chelonia mydas sense_hearing from Piniak 2016 (e0159711) is already on main, so the held lead is closed.
- Thin keys (taxa on main): airflow 29, electric 40, infrared 28, vibration 66, touch 60, magnetic 41.

## Records filed (3) in docs/views/evidence/desk-d210.jsonl
1. Erinaceus europaeus, sense_hearing, Rasmussen et al. 2026 Biol Lett 22(3) 20250535 (Oxford ORA copy prints CC BY 4.0).
2. Uranotaenia lowii, sense_hearing (female antennal nerve), Pantoja-Sanchez et al. 2023 J Exp Biol 226(24) jeb245359 (NSF copy, CC BY).
3. Periophthalmus barbarus, sense_touch (corneal blink latency), Aiello et al. 2023 PNAS 120(18) e2220404120 (NSF copy, CC BY).

## Searches (WebSearch, about 27)
stonefly drumming; flea host cues; seahorse/pipefish senses; goby senses; hedgehog senses; Piniak 2016; Uranotaenia lowii; booklouse; electroreception; infrared; Syngnathidae behaviour; airflow mechanoreception; peerj pipefish; mdpi stonefly; plos flea; frontiers goby; seismic vibration; magnetic compass; whisker/bill tip; ultrasonic ABR; head louse; seahorse feeding; sturgeon/coelacanth electro; hedgehog/shrew touch; round goby; mudskipper.

## Held out
- Huo et al. 2022 Insects 13(12) 1102 (stonefly mating mistakes): field anecdotes, no counts, licence shown as CC BY 4.0 on page but CC BY 3.0 in metadata; the one drumming sentence is a negative note on one male.
- Berquist et al. 2015 Sci Rep 5:8962 (Latimeria rostral organ): model from one preserved specimen's MRI, no recordings; key sentence "This identified..." opens on a pronoun and results sentences returned only as clauses.
- Han et al. 2024 Front Amphib Reptile Sci (reptile sound-localisation circuits): neuron counts only.
- Gemmell et al. 2013 Nat Commun 4:2840 (seahorse head hydrodynamics): no licence visible on the page read.
- Seahorse/pipefish spectral sensitivities (Visual Neuroscience 2007), round goby hearing papers (Univ. Windsor), Pediculus odour paper (CONICET page returned no content), Rasmussen preprint (Atelerix, Research Square): not open-licence or not readable here.
- Piniak 2016: already on main.

## Owner questions
- Uranotaenia lowii and Periophthalmus barbarus are not in gbif-names.tsv; please confirm or add.
- Periophthalmus barbarus filed under sense_touch (corneal tap reflex latency); move if a better key exists.
- Plecoptera, Psocodea, Siphonaptera remain empty; searches returned only closed or old papers.

## Desk disposition after audit 294

Audit 294: 1 of 3 records in error (33.3%, 2 faults), fixable. Pooled audits 172 to 294: 286 of 653 (43.8%). All three merged with the auditor's replacement text. Uranotaenia lowii: the quote was restored to the whole sentence including "(Fig. 4D)" (38 words), and the conditions now say tones were spaced 0.2 kHz apart, so 450 Hz is the highest test tone reaching the criterion, the next tested being 650 Hz, with best frequency 250 Hz at 68.9 ± 0.7 dB SPL; the url now points to the NSF PAR full-text copy. Erinaceus europaeus and Periophthalmus barbarus took the uncounted additions: the hedgehog row now carries the 16 to 60 kHz criterion range, the 20 to 25 dB behavioural-versus-ABR remark and the six juveniles; the mudskipper row says that ± is not defined as SD or SE, that no sham control was run and that stimulus force was not reported.

Owner questions: add Uranotaenia lowii and Periophthalmus barbarus to gbif-names.tsv (BIODAR and Eschmeyer accept both); confirm sense_touch for a corneal-reflex latency or create a reflex-latency key; for ABR audiograms whose tested range is wider than the criterion range, which belongs in value (the hedgehog row files the tested 4 to 85 kHz, with 16 to 60 kHz at the 60 dB criterion in conditions).
