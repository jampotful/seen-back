# desk-d206 (animal sensory-trait screen, replaces the plant screen)

Grep before filing: combined text of docs/views/evidence/*.jsonl, audit/ALL.jsonl and audit/corrected on main. Zero rows by taxon or DOI for: Esox, Hippocampus, Syngnathus, Pomatoschistus, Campylomormyrus, Ephoron, Pygocentrus/Serrasalmidae, Piaractus, Plecoptera, Rotifera, Tardigrada, Peripatus-group except Euperipatoides rowelli (one acuity row from a modelling paper, 10.1371/journal.pcbi.1008808, a different paper and finding). Onychophora, Mormyridae family rows were absent as order or family labels, but the order label is blank on many older rows, so "no rows" is claimed only for the taxa named here.

## Records (5, docs/views/evidence/desk-d206.jsonl)
1. Euperipatoides rowelli, behaviour_vision, spatial resolution 15 to 40 deg (Kirwan et al. 2018, JEB, 10.1242/jeb.175802). Abstract quote; design from the open PDF.
2. Campylomormyrus compressirostris, sense_electric (Nagel et al. 2018, Sci Rep, 10.1038/s41598-018-29132-z).
3. Campylomormyrus tamandua, same paper, the marginal heterospecific preference in condition V is in conditions.
4. Ephoron virgo, behaviour_vision, wavelength-dependent larval repellence, max 400 nm (Mészáros et al. 2024, JEB 227(10), 10.1242/jeb.247142).
5. Serrasalmidae (family, grade g), sense_hearing, five of eight species detect 50 to 3600 Hz (Mélotte et al. 2018, Sci Rep 8(1):1281, 10.1038/s41598-018-19812-1).

## Queries (web:)
Esox lucius vision lateral line open access; seahorse Hippocampus sensory; Tardigrade/Hypsibius eye light magnetic; mormyrid electroreception Frontiers/PLOS; stonefly Plecoptera vibrational/photoreceptor; Onychophora velvet worm sensory; goby Gobiidae vision/hearing/spectral; caddisfly Trichoptera light/vibration; Campylomormyrus EOD; Ctenophora light/mechanosensory; scorpion/harvestman Sci Rep; mayfly/stonefly/caddisfly phototaxis; centipede/millipede Tömösváry; rotifer/bryozoan/sponge larvae phototaxis; tardigrade behavioural response; piranha/tetra hearing; pipefish/seahorse sensory; pike visual/lateral line/olfactory. Fetches of the papers above plus Crossref for four DOIs.

## Held out
- Pomatoschistus pictus and P. marmoratus hearing, best 100 to 300 Hz, AEP, 6 males each (Amorim et al. 2018, JEB, 10.1242/jeb.183681): every sentence stating the result is over the fetch tool's length (32 and 50 words, tool will not return it whole); Crossref lacks volume/issue. Worth a manual quote check.
- Hypsibius exemplaris / Richtersius cf. coronifer behaviour affected at 4 and 3 ppm oxygen (Hagelbäck and Jönsson 2023, Front Physiol 14:1249773, CC BY): key sentence too long to quote whole; stimulus is hypoxia, a borderline fit for sense_chemical.
- Esox lucius close-focus and binocular field (Sroczyński 1972, Acta Ichthyol Piscat 2(1), 10.3750/AIP1972.02.1.06, CC BY): abstract is a machine translation of a Polish summary, no numeric field angle on the page; full text not reachable.
- Syngnathidae pipefish click sounds (PeerJ 3:e1471): sound production, no hearing statement.
- Polydesmida lack a Tömösváry organ (ZooKeys 930, 10.3897/zookeys.930.48438): morphology, no sensory trait key fits.
- Mischonyx cuspidatus leg tapping toward a spider (J Arachnol 42(1)): defensive behaviour, no licence shown.
- Hippocampus spectral sensitivities (Visual Neurosci, Cambridge PDF) refused for length; Serrasalmidae Table 1 and Springer seahorse hearing not retrievable.
- Not reached: Plecoptera, Trichoptera, Ctenophora, Rotifera, Bryozoa, sponge larvae (search results were dlib.si drumming theses, Wisconsin thesis, and paywalled hosts).

## Owner questions
- Campylomormyrus and Euperipatoides rowelli are absent from docs/views/gaps/gbif-names.tsv (Ephoron virgo and Serrasalmidae also not checked as rows there); please confirm accepted names.
- Two records (Kirwan 2018, Mészáros 2024) carry the Company of Biologists user licence, not a CC licence; the copies read were the publisher PDF and a Hungarian repository PDF. Accept as publisher free full text?
- Crossref gives no volume or issue for Kirwan 2018, so the journal field cites the article number only (the page URL shows 221(11)).
- The Euperipatoides row is filed under behaviour_vision because the paper gives degrees; say if a separate trait for angular resolution is wanted.
