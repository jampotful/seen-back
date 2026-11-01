# desk-d251

Records filed (docs/views/evidence/desk-d251.jsonl, check.py 0 problems): 6
- Dikerogammarus villosus, sense_chemical: wild-collected killer shrimp strongly attracted to zebra-mussel-scented water, not to fish (tilapia) scent; abstract sentence whole (peerj.8075; two-choice fluviarium; fish-scent nulls and zebra-mussel P values from Results pieces; sample sizes in Methods and captions disagree, noted; Crossref CC BY 4.0 unspecified + page CC Attribution License). Family/order from OBIS.
- Argiope bruennichi, sense_chemical: webs of old females attracted males more than webs of younger females (peerj.1877; abstract sentence whole; females lab-reared from wild juveniles, male origin not stated; paired female-vs-web null and N = 27 statistic in conditions). Family from World Spider Catalog.
- Carcharhinus melanopterus, sense_electric: bait taken in 33% of Scuba7-on trials vs 100% off (s41598-020-60062-x; free-ranging, provisioned sharks; block-randomised on/off; field strength modelled, not measured). Crossref CC BY vor; page prints no licence sentence. Family/order from OBIS.
- Rattus norvegicus, sense_chemical: free-living farm colony did not avoid predator-odour boxes (s41598-018-27054-4; null; abstract sentence of 30 words in two abutting pieces; unmarked rats, sample composition unknown). Crossref CC BY vor.
- Anoplotrupes stercorosus, sense_chemical, two records: wild beetles attracted in field pitfall traps to a DMTS + 3-octanone + benzaldehyde blend, and antennae responded to 24 volatiles in GC-EAD (insects11080476; both abstract sentences whole; counts, Kruskal-Wallis and the blend-3 weak catch in conditions). Crossref CC BY 4.0 vor, page CC BY 3.0.

Held / not filed
- Frog alarm-call null (ani12243537, three anurans in the field): abstract "no response" sentences are pooled or over 125 characters, and Table 2 lists a few escapes that the text denies. Held.
- Sinosuthora/Paradoxornis webbianus and Acrocephalus orientalis nestling alarm-call suppression (ani12162156): wild nestlings tested indoors; only the Discussion sentence is short; parrotbill name form (webbianus/webbiana, Sinosuthora vs Paradoxornis) unresolved and no family source fetched.
- Gasterosteus aculeatus Y-maze bloodworm odour (peerj.3121): wild-caught, lab-held 6 to 12 months; undisturbed-flow Results sentence needs three pieces, abstract sentences over 125 characters.
- Squirrel bird-chatter playback (pone.0221279): every abstract sentence over 125 characters.
- Cancer pagurus EMF (jmse9070776): lowest strength is the only null (threshold risk), Results/Discussion contradict on 250 uT l-Lactate.
- Pipistrellus pipistrellus jamming avoidance (srep30978): observational, abstract null sentence short but weak for a sense trait.
- Spodoptera frugiperda skyglow (insects16121252): lab-reared from wild larvae, abstract sentences over 125 characters.
- Littorina/Littoraria irrorata (peerj.5744): held by d222 (no whole sentence carries the result).
- Reef-fish larvae odour (pone.0072808): family-level pooling. Rat 50 kHz (pone.0211601): laboratory Wistar rats, captive-bred voles.
- Bat deterrent peerj.21231: page failed to open. Nature page s41598-017-09738-5 (shearwater anosmia), srep17061 (gulls): licence not stated on page, abstract sentences long; not pursued.
- Already on main or held earlier: peerj.12567, pone.0051364, pone.0253770, pone.0232136, peerj.2828, peerj.14745, s41598-024-66679-6, s41598-017-11459-8, s41598-020-60383-x, srep33805, pone.0202679, pone.0012698, pone.0239920, peerj.8149.

Owner questions
- Argiope bruennichi: females were collected as juveniles and reared in the lab before field tests; acceptable as wild-origin, or hold?
- Carcharhinus melanopterus: sharks are habituated to daily provisioning; acceptable as free-ranging?
- Rattus norvegicus: colony of unmarked rats, sample size unknown; null kept with that disclosed.

Inverted search note
About 35 searches and fetches. Best yield: field trials of wild populations with null or contrasted treatments (Nature/Sci Rep, MDPI Insects, PeerJ). Many hits were already on main or held (check slugs with git grep before fetching); most abstracts have all sentences over 125 characters, so the usable quote is often a short abstract result sentence or none.

## Desk disposition after audit 346

Audit 346 checked all 6 lines: 5 of 6 in error (line 6, Anoplotrupes stercorosus GC-EAD, matched). Main corrections: line 5 trap site is the Schwäbische Alb, not Darmstadt (Darmstadt is the GC-EAD beetles); line 2's note wrongly said main has no Argiope bruennichi sense_chemical row (spider.jsonl:199 is a different paper, Talukder et al. 2025, so not a repeat); lines 1 to 4 had omitted nulls, controls and design (blank versus blank side-bias check, one web per young and middle-aged class, modelled not measured field strengths with unidentified sharks, single wild rat colony). Replacement text applied; 6 merged, 0 held out. Owner questions answered by the audit: lab-reared virgin Argiope females from wild juveniles, provisioned sharks and an unmarked wild rat colony are acceptable with disclosure; the Scuba7 deterrent fits sense_electric (modelled V/m).
