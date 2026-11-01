# desk-d306: eye states of larvae, spiders, a fossil and a deep-sea fish in open-access papers, 12 records

Branch research/desk-d306 from origin/main. About 52 WebSearches; WebFetch only on URLs returned by searches (Pensoft download/xml and article_preview, EJT download, Nature, Frontiers, MDPI, the Pensoft J_FILES layout page); Crossref single-DOI lookups through WebFetch for every DOI filed (the api.crossref.org/v1 form failed once for 10.3897/zookeys.734.15061; the /works/ form answered). `python3 -I tools/senses/check.py`: desk-d306.jsonl 12 records, 0 problems.

Repeat check: every species and DOI grepped over the whole origin/main docs/ tree and over the evidence files of all origin/research/desk-* branches (dumped once to a scratch file) before filing. The DOIs of the Pinelema paper (ZooKeys 734) and the Frontiers spookfish paper already carry other species; the species filed here are new.

Angle result: the larval angle (stemmata, eyespots, zoea, ammocoete, tadpole, flatfish eye migration), the stalk-eyed and telescopic-eye angle (Diopsidae, telescope octopus, Macropinna, Scopelarchidae, Gigantura) and bird/bat eye-size papers gave no open page with a whole species-level sentence (news items, closed Zootaxa/Mapress, PMC and Springer). The yield came from spider descriptions (Caponiidae, Telemidae), one Mecoptera larva, one Dermestidae larva, a Jurassic fossil eye, a deep-sea fish and a fish-larva development paper.

Filed (docs/views/evidence/desk-d306.jsonl):
1-3. Caponina alejandroi, C. bochalema, C. huila (Caponiidae), eye_type: six eyes, AME largest and dark, ALE and PLE pale and translucent; EJT 813. Desk d288 had left these as a retrieval gap; each sentence arrives as two consecutive tool pieces.
4. Tarsonops irataylori (Caponiidae), eyes_count 2; ZooKeys 289; holotype male from a Belize cave.
5. Panorpodes kuandianensis (Panorpodidae, Mecoptera), first-instar larva without compound eyes, ocelli or stemmata; ZooKeys 398.
6. Ctesias serra (Dermestidae), last-instar larva, "Six stemmata present on the head (four + two other below)"; ZooKeys 758.
7. Dollocaris ingens (fossil thylacocephalan, Middle Jurassic), ommatidia_count more than 18,000 per eye; Nature Communications 7. New trait.
8. Bathylychnops exilis (Opisthoproctidae), bipartite eye: spherical main globe plus rostrolateral diverticulum with its own lens; Frontiers in Ecology and Evolution 10. 44-word sentence cut with marked ellipses.
9-10. Pinelema spirulata and P. xiezi (Telemidae), six eyes; ZooKeys 734.
11-12. Pholis fangi (Pholidae, family not read from page), eye diameter 0.29 mm (flexion larva) and 1.41 mm (juvenile); Fishes 9(6):213. New trait key eye_diameter_mm (already used on main).

Weak spots for the auditor:
- Ctesias serra: the sentence says six stemmata "on the head" and does not say per side or in all; the value repeats that wording. The comparison table (Table 2) was not readable for the Ctesias row.
- Dollocaris ingens: an estimate, a lower bound derived from facet density; the Discussion calls it "a rough estimate". The page text read gave only "Vannier, J., Schoenemann, B., Gillot, T. et al."; the five authors come from Crossref. Class, order and family left blank. Specimen number not stated in the text read.
- Bathylychnops exilis: the cut in a 44-word sentence (middle clause and trailing figure reference); the page text read printed no licence sentence, Crossref gives CC BY 4.0 vor.
- Caponina and Panorpodes sentences were stitched from two consecutive tool pieces (joins at a comma and space). Panorpodes: page byline Jiang, Yue, Hua; Crossref lists Hua first; the page byline is followed.
- Pholis fangi: eye diameters are single values in running text with no n; the flexion value appears to be one specimen (inference from a figure). Preflexion (0.22, then 0.24 mm) not filed because the stage gives two values. Family and order not read.
- Pinelema: DOI already on main for five other species of the paper.
- Higher taxa: order from titles where no heading was read; class blank for all spiders and beetle.

Dropped candidates:
- Done elsewhere: Gegeneophis carnosus (VZ 72, on desk-d280); Iandumoema smeagol (several units); Pinelema damtaoensis, laensis, nuocnutensis, pacchanensis, zhenzhuang; Leptonetela arvanitidisi and paragamiani on main; Leptonetela penevi (same sentence as arvanitidisi, d283 chose not to file it); Dolichopteryx longipes in the Frontiers paper (the sentence reports an earlier study, and d185 holds the species); Opisthoproctus, Winteria, Rhynchohyalus (d185).
- Fragment or genus-level sentence: Typhlonesticus gocmeni ("Eyeless (Figs 18, 19)." one word); Trilacuna jinyun and T. jiuchi (EJT 748, verbless semicolon chains); Kachinia putao and K. mahmolae (ZooKeys 794, genus-level eye sentence); Aamunops hoof and A. yiselae (EJT 930, eye sentence at genus level only); Zachaeus seyyari (ZooKeys 514, eye tubercle shape only, not an eye state); Yufengus atrophaneuroides (d283 dropped; caption entry); Graptus triguttatus and Peritelus sphaeroides (immature stages of four weevils, Gosik et al.; "Two weakly visible stemmata close to des5." and "Stemmata poorly visible, located close to des5." are descriptive clauses with no stated state beyond visibility; not filed).
- Access or licence: Trechus gamae larva (Bulletin of Insectology, no licence statement); Omegops honggulelengensis and O. xiangi (J Paleontology, no open licence on the page, no lens counts in the text read); Dibamus deimontis (Zootaxa); Taprobanica Indotyphlops (robots_disallowed); journal.fi Entomologica Fennica (bot-check page); ZooKeys 13320 and 118644 (permission request not answered, not retried); Plazi, PMC, Springer, bioone and ResearchGate results not opened.
- Nothing found: stalk-eyed flies (Diopsidae; only core.ac.uk, zenodo and scilit copies), telescope octopus and Macropinna (news pages only), ammocoete eyes (Frontiers pages, intermittent; PMC), flatfish eye migration (Nature Commun Biol and PMC, no named-stage sentence read), zoea eyes, Diptera larval eyespots (figure pages only), harvestmen with eyes (Zoosystema on bioone, Zootaxa).

Questions: Does a six-stemmata sentence that says "on the head" count as a total in the Ctesias record, or should it be held out as a possible per-side count? Is a lower-bound estimate such as "more than 18,000 ommatidia" acceptable as ommatidia_count with value_relation ">"?

## Desk disposition after audits 401 and 402
Audit 401 (lines 1-6): 5 fixable errors; audit 402 (lines 7-12): 4 fixable errors. Whole unit audited; all replacements applied; all 12 records merged.
