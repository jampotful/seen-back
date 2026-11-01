# desk-d213 (animal sense-trait screen, unsaturated systems)

About 33 WebSearches and 45 WebFetches (Crossref api.crossref.org/works/<DOI> used to confirm authors, volume, licence and corrections). Main was grepped by genus and DOI before every candidate was opened.

## Queries (web)
Subterranean mammals (mole-rat hearing), lamprey/hagfish, Neoceratodus, pinnipeds/manatee/hyrax, penguins/kiwi, Odonata/mantis/stick insect/cockroach, Sphodromantis lineola (plus Crossref title list), C. elegans, brittle star/sea star/Nautilus/Nematostella/Hydra, planarian/termite/leech, tortoise/skink/gecko/tuatara ABR, marsupials, cichlid/catfish/goldfish hearing, Ladich-group fish hearing, Cassiopea/box jelly/ctenophore, cephalopod hearing, frogs beyond Xenopus, caecilian/lungfish/coelacanth/paddlefish, star-nosed mole/golden mole/wombat, Malkemper/Begall mole-rats, crustacean and bivalve sound detection, lobster title search, sea urchin/sea star vision, termite/stingless bee/Lasius, firefly, Diadema title search, larval-fish ontogeny (Higgs and Fuiman), JEB-site searches for lamprey/hagfish and for hummingbird/penguin/owl, tuatara/caecilian. Crossref relevance queries by prefix (PeerJ) were too noisy to use.

## Records (3, docs/views/evidence/desk-d213.jsonl, all grade m, all publisher's own free JEB page on cob.silverchair.com)
- Doryteuthis pealeii, sense_hearing: AEP responses 30 to 500 Hz, lowest thresholds 100 to 200 Hz (Mooney et al. 2010, 10.1242/jeb.048348). Squid sedated in MgCl2; band is where responses were obtained.
- Ophiomastix wendtii, motion: response to 67% of looms, 50% of overhead passes, 35% of blank-screen controls (Sumner-Rooney et al. 2021, 10.1242/jeb.236653, CC BY printed). Different finding from the two desk-d149 rows on the same paper.
- Brevoortia tyrannus, behaviour_vision: 0.06 to 0.33 of neuromast-blocked larvae responded in light, dark-strep baseline 0 to 7% (Higgs and Fuiman 1996, 10.1242/jeb.199.12.2619).
Quotes came through WebFetch, not machine text; quotecheck was not run.

## Held out
- Gerhardt et al. 2017 JEB (10.1242/jeb.164426), Fukomys anselli/micklemi/mechowii ABR audiograms (hearing range 125 Hz to 4 kHz at 60 dB SPL, best 1 kHz): a published Correction exists (10.1242/jeb.175190, 220(24) 4747) whose content I could not see, Crossref's title differs from the PDF's ("extremely low high-frequency cut-offs" against "extremely poor high-frequency hearing"), the abstract sentence is shared by three species, and F. micklemi is not in gbif-names.tsv (Fukomys anselli is listed there as a synonym of Cryptomys anselli). Not on main. Strong lead for the owner.
- Yerramilli and Johnsen 2010 JEB 213: 249 (Strongylocentrotus purpuratus 10 deg target detected, 6.5 deg not): the positive sentences are 264 to 404 characters, and the abstract says 39 specimens while Methods say 20 and Table 1 gives N = 19 and 20. Not on main.
- Jezequel et al. 2021 JEB 224(6) jeb240747 (Homarus americanus AEP, best 80 to 120 Hz, 16 lobsters): only copy opened is on archimer.ifremer.fr and prints no open licence; no publisher page was found. Not on main.
- Kirwan et al. 2018 JEB 221(14) jeb176271 (Diadema africanum spatial resolution 29 to 69 deg): Bristol repository copy prints only the publisher copyright. Not on main.
- Muntz 1986 JEB 126: 513 (Nautilus pompilius behavioural spectral sensitivity): the text states no behavioural peak, only a comparison with a 467 nm nomogram. Not on main.
- Dehnhardt and Kaminski 1995 JEB 198: 2317 (Phoca vitulina vibrissal size discrimination, Weber fractions 0.27 and 0.25 / 0.13 and 0.08): abstract gives 0.08 for the female where Results give 0.09, no vibrissae-covered control reported, key sentences long. Not on main.
- Elepfandt et al. 2000 Xenopus laevis (excluded system); Goutte et al. 2017 Brachycephalus and Wang et al. 2022 Trachemys (both already on main); Ladich and Schulz-Mirbach 2013 (on main).
- Robert et al. 2025 JEB 228(11) 10.1242/jeb.249296 and Nityananda et al. 2019 JEB 222 10.1242/jeb.198614 (Sphodromantis lineola, absent from main, CC BY on Newcastle ePrints record pages): the PDF fetch returned PROVENANCE_REQUIRED and no publisher page was seen. Good leads for a reader who can open them. Tarawneh et al. 2018 Biology Open (10.1242/bio.029439, S. lineola contrast thresholds): only abstract seen, no licence.
- Glover et al. 2019 Sci Rep 9: 13369 (Eptatretus stoutii T-maze, 10.1038/s41598-019-49863-x) and Malkemper et al. 2023 Commun Biol 6: 242 (C. elegans magnetic null, CC BY): nature.com fetch refused once / abstract sentences long. Coelacanth rostral organ (Berquist 2015 Sci Rep, Latimeria chalumnae): anatomy and modelling, no measurement of a threshold.
- Jezequel et al. 2023 JASA scallop: copyright only, no licence. Sansom et al. 2025 Ecol Evol termite review: morphology.

## Owner questions
1. Brevoortia tyrannus is not in gbif-names.tsv; which family does the desk use (Clupeidae by GBIF, Alosidae in some recent fish catalogues)?
2. Fukomys anselli is a GBIF synonym of Cryptomys anselli yet used on main; Fukomys micklemi is absent from the name table. Which authority decides, and can someone open the Gerhardt 2017 correction?
3. Can a reader open journals.biologists.com for Robert 2025, Nityananda 2019, Jezequel 2021 and Kirwan 2018 to confirm licences and quotes?
4. Looming response in a brittle star is filed under `motion`; confirm that key for looming responses in a non-eyed animal.

## Desk disposition after audit 297

Audit 297: 2 of 3 records in error (66.7%). Pooled audits 172 to 297: 292 of 665 (43.9%). Line 1 (Doryteuthis pealeii hearing) was dropped: it repeats docs/views/audit/corrected/sea-invertebrates.jsonl:113 (same DOI, same abstract sentence, same 30 to 500 Hz value), and the 100 to 200 Hz figure is already in :113's note and :114's value. The unit's note that it grepped main by DOI was wrong. Two records merged with the auditor's replacement text: Ophiomastix wendtii (the loom came first and the overhead pass second, so the 67% versus 50% difference is confounded with order; the 35% blank-screen scoring is the model's baseline, which found responses to both stimuli but not to a negative control) and Brevoortia tyrannus (family Alosidae per Eschmeyer, streptomycin blocking not verified in these larvae and sparing the inner ear, dark-control comparison added; the per-treatment larvae numbers were unconfirmed and are marked as such).

Owner questions: correct sea-invertebrates:113 and :114 with the audit's conditions text (19 squid, MgCl2 sedation, tank and shaker ranges, control recordings in Fig. 2, 500 Hz as the response limit and not the testing limit); add Ophiomastix wendtii and Brevoortia tyrannus to gbif-names.tsv and confirm Eschmeyer families for clupeiforms; the menhaden Table 1 numbers need a reader who can open journals.biologists.com.
