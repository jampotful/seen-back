# desk-d209 progress

Task: 5 to 10 new animal sensory-trait records from open-licence papers in under-covered groups. Result: 2 records filed, 6 leads held out. Yield was low because the obvious open papers are already on main (nine of the first twelve papers opened were already filed).

## Coverage map (from docs/views/evidence and audit files, taxa per order)
Thin orders: Trichoptera 1, Collembola 1, Dermaptera 1, Gadiformes 1, Anguilliformes 1, Thysanoptera 2, Ephemeroptera 4, Salmoniformes 2, Siluriformes 6, Blattodea 7, Isopoda 7, Orthoptera 18, Hemiptera 46. No taxa at all: Plecoptera, Psocodea, Siphonaptera, Embioptera, Syngnathiformes (Hippocampus, Syngnathus), Gobiiformes, Gasterosteiformes (Pungitius), Atelerix. Thin traits (taxa): sense_airflow 5, sense_electric 14, sense_infrared 16, sense_vibration 20, sense_touch 29, sense_magnetic 28, sense_hearing 72. No sense_hearing row for any sea turtle.

## Queries (WebSearch, 39 of 40 used)
ABR/AEP catfish eel cod loach; tympanal organ bushcricket katydid mole cricket; caddisfly electroretinogram; stonefly substrate vibration; flea/louse/silverfish spectral; mole cricket Gryllotalpa hearing; PeerJ hearing/ERG cockroach cicada planthopper thrips; Frontiers ABR fish eel catfish goby sculpin; Insects antennal sensilla Hemiptera Orthoptera Blattodea; whitefly/aphid/bed bug/stink bug ERG; hedgehog/tenrec/hyrax/armadillo/mole-rat hearing; flicker/optomotor fish crustacean beetle; site:peerj.com, site:frontiersin.org, site:mdpi.com trait words; seahorse/pipefish; goby; beetle ERG CC BY; reptile AEP CC; lateral line CC; Piniak green turtle; Lavender loggerhead; site:cob.silverchair.com (two); site:biologists.com; cicada/treehopper hearing; Dermaptera/Embioptera/Psocoptera/Phthiraptera/Siphonaptera; sturgeon/paddlefish/bichir; cephalopod hearing; substrate vibration threshold; magnetic compass; airflow trichobothria; electroreception; BMC Zoology/Zoological Letters; RSOS myriapod/mite; Maruska damselfish; Uranotaenia lowii; Vasconcelos toadfish; Gelasimus.

## Records filed (docs/views/evidence/desk-d209.jsonl)
1. Gryllotalpa major, sense_hearing, 25 kHz ultrasound sensitivity band. Howard, Mason, Hill 2008, J Exp Biol 211(22), 10.1242/jeb.023143. Publisher page, Results sentence. Abstract and Results differ on the 2 kHz and 10 kHz dB values, so only the 25 kHz finding is filed.
2. Abudefduf abdominalis, sense_hearing, 95 to 240 Hz high-sensitivity band (AEP, 24 fish, null for sex and season stated in conditions). Maruska, Boyle, Dewan, Tricas 2007, J Exp Biol 210(22), 10.1242/jeb.004390. Publisher page, Results sentence.

## Held-out leads
- Hearing in the juvenile green sea turtle (Chelonia mydas), Piniak et al., PLoS ONE 11(10): e0159711, 10.1371/journal.pone.0159711. No sea turtle sense_hearing on main. journals.plos.org fetch was rate-limited three times; the USF repository copy page prints CC BY 3.0 but its PDF fetch was blocked (permission prompt unanswered). Needs a retry on a quiet day.
- Frog-biting mosquito Uranotaenia lowii, Pantoja-Sanchez et al., J Exp Biol 226: jeb245359, 10.1242/jeb.245359 (NSF PAR copy prints CC BY). Key Results sentences (best antennal-nerve frequency, 250 Hz threshold, phonotaxis) are over 125 characters and the fetch tool would not return them verbatim; the tool returned abstract sentences only in fragments, which I did not use.
- New Zealand ground weta Hemiandrus pallitarsis, tibial organ with up to 90 scolopidia, Sci Rep 7: 2031, 10.1038/s41598-017-02132-1. nature.com fetch blocked. Anatomy-only count, so it also needs a trait decision (lesson 10).
- African pygmy hedgehog Atelerix albiventris audiogram, Heffner et al., J Comp Physiol A 208(5-6): 653-670, 10.1007/s00359-022-01579-6. Springer host refused; open licence not confirmed.
- Lusitanian toadfish Halobatrachus didactylus saccular sensitivity, Vasconcelos et al., J Exp Biology 218, 10.1242/jeb.123059 (DOI from a search-result URL, not yet checked on Crossref). Only a core.ac.uk copy with no licence was reachable; no publisher page found.
- Fiddler crab Gelasimus dampieri spectral sensitivity, Jessop et al., J Exp Biol 223(23): jeb230979, 10.1242/jeb.230979 (from an aggregator; publisher page blocked). Not filed on main under this DOI.
- Hippocampus seahorse theses and Visual Neuroscience papers: thesis (held out), VN not open. Lined seahorse hearing (JASA 2010) not open.
- Already on main (not re-filed): Epinephelus awoara ABR, Euprymna berryi hearing, Tursiops electroreception, Acrocephalus scirpaceus magnet, Cicadatra atra, slipper lobsters, Monochamus vibration, Electrogena.

## Owner questions
1. Gryllotalpa major and Abudefduf abdominalis are not in docs/views/gaps/gbif-names.tsv. Both are, to my knowledge, accepted names, but I could not check; please confirm or add.
2. Do scolopidia counts and tibial organ anatomy belong under sense_vibration ("organs" is in the trait definition) or need an anatomy trait?
3. JEB articles carry no licence line on the publisher page. Is the Company of Biologists free-to-read copy acceptable as access "open" (as in desk-d206)?

## Desk disposition after audit 293

Audit 293: 2 of 2 records in error (100%), both fixable. Pooled audits 172 to 293: 285 of 650 (43.8%). Both merged with the auditor's replacement text. Gryllotalpa major: the value no longer carries the second-peak claim from the next sentence (moved to conditions), and the method states the level steps and averaging. Abudefduf abdominalis: the 95 to 240 Hz band is now described as the authors' "relatively high sensitivity" description of the four lowest of eight stimuli with no threshold criterion, not a hearing range; thresholds were measured to 800 Hz and 95 Hz was the lowest frequency presented.

Licence: the Company of Biologists pages are the publisher's own free full text, served without a login, with no licence line (audit 290 ruling).

Owner questions: add Gryllotalpa major and Abudefduf abdominalis to gbif-names.tsv; confirm that source.access "open" is right for a free, unlicensed publisher copy; the 2 kHz best frequency of Gryllotalpa major could be filed separately (only its dB value is disputed).
