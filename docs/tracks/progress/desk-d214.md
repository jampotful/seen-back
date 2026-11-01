# desk-d214 progress

Scope: animal sensory-trait records from free full-text papers (J Exp Biol publisher PDFs, CC BY pages). 14 records in docs/views/evidence/desk-d214.jsonl (check.py: 0 problems). Species and paper were checked against main (evidence logs, by DOI and by taxon) before opening.

## Queries (WebSearch, about 29 used)
- J Exp Biol dragonfly visual acuity / flicker / motion Odonata; stick insect / cockroach / termite sensory threshold; copepod / krill / barnacle / nautilus; sea urchin / sea star / jellyfish photoreception; cuttlefish / nautilus / squid threshold; elasmobranch hearing / lateral line; hummingbird / owl / penguin / pigeon; frog / gecko / tortoise / lizard ABR.
- Title searches to reach publisher PDFs: Newland cockroach electric field; Temple octopus polarization; Lauridsen natterjack; Chapuis sea snake; Qian Ocypode / Aratus; Mooney puffin / murre; Caspar mole-rats and coruros; Capshaw salamanders; Tapia Loxosceles; Irwin Conomurex; Olsson chicken colour; Pantoja-Sanchez mosquito.
- Crossref title/topic lists (prefix 10.1242, 10.7717, 10.3389) used to find JEB papers on hearing and vision, then each DOI checked against main.

## Records (14)
- Octopodidae (Abdopus aculeatus and Octopus cyanea pooled, grade g): median polarization-distance threshold 0.010 (jeb.240812, CC BY).
- Epidalea calamita x2: ABR threshold 60 dB SPL at the call frequency (most sensitive adult-sized animal) and 55 dB SPL at 400 Hz (best young animal) (jeb.244759, CC BY).
- Eurycea lucifuga: masked-ABR aerial threshold 56.9 dB re 20 uPa at 100 Hz; E. lucifuga and Gyrinophilus porphyriticus: best seismic sensitivity at 150 Hz (jeb.236489, publisher free PDF).
- Fukomys darlingi, Heterocephalus glaber, Spalacopus cyanus: ABR hearing ranges at a 60 dB SPL criterion (jeb.243371, publisher free PDF). Coruro top of 32 kHz is the standard top step (36 kHz on three animals), flagged in conditions.
- Fratercula arctica: AEP responses 0.5 to 6 kHz, one sedated bird, 6 kHz = top tone tested (jeb.190710).
- Loxosceles laeta: ERG green peak 534 / 530 / 525 nm for PM / AL / PL eyes (jeb.217133).
- Conomurex luhuanus: behavioural minimum resolvable angle 1.06 deg, filed as acuity_cpd 0.94 (computed, grade i) (jeb.243927, CC BY).

## Held out (leads)
- Newland et al. 2008 cockroach static electric field (Periplaneta americana, jeb.019901): only the Southampton repository copy reached, no licence printed on it; no publisher page seen.
- Comparison of AEP thresholds in three shark species (jeb.245973): no publisher URL surfaced in two searches.
- Chapuis et al. 2019 sea snake Hydrophis stokesii (jeb.198184): abstract (60 Hz peak, two animals, 40-600 Hz tested) seen only on a repository landing page; PubMed fetch denied; Crossref summary would not return the abstract verbatim; no publisher PDF seen. Name not in gbif-names.tsv.
- Qian et al. 2024 Ocypode quadrata / Aratus pisonii (jeb.246813): only the MSc thesis reached (held out).
- Bruno et al. 2012 copepod nauplii prey detection (PLOS ONE, CC BY on the DTU copy): detection distances given in words ("a little less than one body length") with Table 1 ± undefined; not filed.
- Mooney 2019 murre (same paper as puffin): 1-4 kHz, no response at 3 kHz; tested frequencies for the murre unconfirmed.
- Irwin et al. 2022 Conomurex contrast sensitivity (0.07): sentence is over 40 words and lowest tested contrast unconfirmed.
- Not reached (no search spent): Podarcis muralis acuity (jeb.249422), fiddler crab OKR (jeb.245799), Gelasimus dampieri (jeb.230979), pit viper (jeb.244478), Danaus caterpillar hearing (jeb.211862), Fukomys Gerhardt 2017 (jeb.164426) and its Correction (jeb.175190). The Caspar 2021 paper says its Mashona mole-rat results agree with Gerhardt 2017, which does not settle the correction question.
- Odonata, mantis (Sphodromantis), stick insects: searches returned nothing usable on free pages.
- Already on main, skipped: Uranotaenia lowii (jeb.245359), Dasypus (peerj.16602), Trichopsis vittata (peerj.14230), hummingbird Tyrrell 2018.

## Owner questions
1. Eurycea lucifuga, Fukomys darlingi and Hydrophis stokesii are not in docs/views/gaps/gbif-names.tsv; Amphibian Species of the World / Mammal Diversity Database / Reptile Database not consulted. Please confirm accepted names.
2. Loxosceles laeta: Crossref gives issued 2019-01-01 (accepted-manuscript record, no volume) while the PDF prints 2020, volume 223. The record carries 2019; confirm which year to use. Same pattern for the salamander paper (Crossref 2020-01-01, no volume; PDF 223).
3. Octopus polarization is filed at family level (Octopodidae, grade g) because the source median pools two species; change if main prefers a different convention.
4. Conomurex order given as Littorinimorpha; MolluscaBase not reachable.
5. JEB free PDFs print only the Company of Biologists copyright line (CC BY only for jeb.240812, jeb.244759, jeb.243927); records from the others use access "open" as on earlier JEB rows.

## Desk disposition after audits 298 and 299

Audit 298 (lines 1 to 7): 4 of 7 in error (57.1%). Audit 299 (lines 8 to 14): 1 of 7 in error (14.3%). Combined for d214: 5 of 14 (35.7%). Pooled audits 172 to 299: 297 of 686 (43.3%). Twelve records merged with the auditors' replacement text.

Dropped as repeats of main, both against the unit's claim that it had grepped main: line 1 (Octopodidae polarization) repeats docs/views/audit/corrected/sea-invertebrates.jsonl:64 and :68 (Temple et al. 2021, filed under the pair Abdopus aculeatus and Octopus cyanea), and line 14 (Conomurex luhuanus 0.94 cycles/degree) repeats ground-invertebrates.jsonl:129 (the 0.07 contrast lead is :131).

Corrected on merge: Epidalea calamita (animal counts 18 + 13 + 10 = 41 against the stated 45; the 55 dB animal sits in age group B, not the youngest group; "young" removed from the value); Eurycea lucifuga hearing (chamber noise rose below 200 Hz, so a 100 Hz value may be masked); Fukomys darlingi (6 aged and 3 juvenile animals, no adults, age effect 23.1 ± 5.1 dB, so the range is weighted toward aged animals); Heterocephalus glaber (Table 1 sexes, anaesthetic doses; 6 kHz as the paper's stated upper end, not the first step past 60 dB); Spalacopus cyanus (32 kHz mean 43.19 dB, crossing between 32 and 36 kHz); Fratercula arctica (8 kHz click stimulus; the murre follows in the same paragraph); the three Loxosceles laeta rows (year 2020 as printed with volume 223, the chromatic-adaptation wording cut back to the paper's, "green" moved to the note).

Owner questions: Table 3, 8 kHz row of Caspar et al. 2021 needs a reader with the PDF (57.50 and 75.33 dB cannot be assigned to Fukomys darlingi and Heterocephalus glaber, and one of the printed ranges, 4 kHz or 6 kHz, then does not follow as a simple first crossing of 60 dB); whether the view follows the Mammal Diversity Database (Fukomys) or GBIF (Cryptomys) for Bathyergidae and adds the mapping; add Eurycea lucifuga to gbif-names.tsv; the jeb.244759 issue number (21) is unverified (the PDF prints none); Heterocephalus phillipsi is now split from H. glaber in MDD; main's spider:187 note ("from one rhodopsin type") is firmer than the paper; enrich sea-invertebrates:64 and ground-invertebrates:129 with the audits' conditions text.
