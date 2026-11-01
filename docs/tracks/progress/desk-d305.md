# desk-d305: eye states of scorpions, harvestmen, pseudoscorpions, whip spiders, eels and chaetognaths in CC BY papers, 16 records

Branch research/desk-d305 from origin/main. About 55 WebSearches, WebFetch only on URLs returned by searches (Pensoft download/xml and article_preview, MDPI, EJT download); Crossref single-DOI lookups through WebFetch for every DOI filed. `python3 -I tools/senses/check.py | grep 'd305.jsonl'`: 16 records, 0 problems. Trait eye_type throughout; no new trait key.

Repeat check: every species and DOI grepped over the whole main docs/ tree and over the evidence files of the 1,831 records on origin/research/desk-* branches (dumped once to a scratch file) before filing; no hits except the Zorotypus paper noted under Dropped.

Angle result: the named groups (Acari, Zoraptera, Embioptera, Diplura, Archaeognatha, Zygentoma, Protura, Gastrotricha, Kinorhyncha, Loricifera, Priapulida, Entoprocta, larval photoreceptors, flatworm parasites, hagfish, lampreys, olm) gave no open page with a whole eye sentence. The yield came from Scorpiones, Opiliones, Pseudoscorpiones, Amblypygi, Chaetognatha and two eel papers.

Filed (docs/views/evidence/desk-d305.jsonl):
1. Euscorpius studentium (Euscorpiidae), median ocelli absent, two pairs of small lateral ocelli; Diversity 16(12):737; redescription from one adult male and one adult female (holotype is a subadult male).
2. Euscorpiops lii (Scorpiopidae), median eyes anterior, three pairs of lateral ocelli; ZooKeys 968; holotype male description (d292 had dropped it as two clauses; the two tool pieces are consecutive).
3-4. Spaeleoleptes spaeleus (reduced cornea, no visible retina; male holotype) and S. gimli (two reduced eyes with cornea and retina), EJT 921; d292 had found no usable sentence.
5. Spelaeochthonius tuoliangensis (Pseudotyrannochthoniidae), small eye spots; Discussion sentence; ZooKeys 1204; female-only types, blind congeners contrasted.
6. Uropterygius hades (Muraenidae), eyes small and anteriorly placed; ZooKeys 1220(15-34).
7-8. Ophichthus kbalanensis (eye relatively small, 2.4 in snout length) and O. multidentis (eye moderate, 1.7-2.6 in snout length); ZooKeys 1220(63-78).
9-12. Chaetognaths of Korean waters (ZooKeys 1106): Pterosagitta draco, Flaccisagitta enflata, Krohnitta subtilis, Parasagitta elegans; eye shape and pigment pattern; redescriptions of known species.
13. Sarax timorensis (Charinidae), two pairs of lateral eyes; Abstract sentence of 38 words (ZooKeys 820); d285 had dropped the paper for semicolon-run Description text.
14. Charinus israelensis (Charinidae), eyes small, median eyes almost absent; EJT 234; female-only types.
15-16. Charinus taboa, median eyes reduced / lateral eyes not very developed and unpigmented; ZooKeys 600; two records (median, lateral), one per sentence.

Weak spots for the auditor:
- Chaetognath, Charinus, Sarax and Euscorpiops sentences are verbless or semicolon-joined and were rebuilt from 2 to 4 consecutive tool pieces; word counts done by check.py. Chaetognath records give eye shape and pigment pattern, which is a thin reading of eye_type. The Parasagitta elegans sentence prints no "with" ("Square eyes + shaped eye pigments"), kept as printed.
- Spaeleoleptes: page byline "Gallão", Crossref "Galão"; page followed. Charinus taboa: page "Ponce de Leão Giupponi", Crossref "Ponce de León Giupponi"; page followed. EJT 234 and EJT 921 print the volume as the number; Crossref gives 234 as issue; the licence on EJT 234 is CC BY 3.0 (page) with Crossref content-version "unspecified".
- Euscorpius studentium: the page prints only a rights link (CC BY 3.0) while Crossref says CC BY 4.0 vor.
- Orders left blank where no heading prints one; no class headings in any of these treatments.
- Uropterygius hades and Ophichthus are not a requested angle (eels), taken because the plain Diagnosis/Description sentences were whole.

Dropped:
- Done by another unit: Ochyrocera ritxoco and O. ritxoo (ZooKeys, on main/branches), Zorotypus komatsui (d285). Zorotypus vinsoni (same DOI 10.3897/zookeys.1178.108276, "Compound eyes and three black ocelli present.", alate female) not filed because the DOI is already on d285.
- Fragments only, no whole sentence: Tyrannochthonius pandus and Lagynochthonius laoxueyanensis ("without any traces of eyes;" inside a semicolon chain), Allochthonius hispidus and Spelaeochthonius huanglaoensis (ZooKeys 1204, "no traces of eyes" clauses), Chthonius kirghisicus (Subterranean Biology 38, "one pair of eyes;" clause), Kumarembia hurleyi (fossil Embioptera, "ocelli absent" clause), Brazilozoros kukalovae (Zoosystema; no licence statement on the page; clause text), Charinus israelensis Diagnosis (semicolon chain over 40 words), Sarax timorensis Description (over 40 words).
- No eye sentence on the page: Acanthodasys paurocactus (Gastrotricha), Echinoderes xiphophorus (EJT 773), Truncozetes and Nippobodidae oribatids, Eukoenenia serrana (XML cut before the description), Spinanycta alabamensis (Introduction and Discussion clauses only), Asian cave diplurans and Juxtlacampa (EJT, no "eye" in the text), cave japygids EJT 1043 (no eye sentence), Eptatretus wandoensis (ZooKeys 926, caption only), Parasite 2020 Dactylogyridae page (navigation only).
- Not a state: Ophichthus key couplet lines; Euscorpius lateral-ocelli count only in a table.
- Access: pages that returned "permission request not answered" (zookeys 123624 xml, 9337 xml, subtbiol 150357 xml, EJT 3217 download) were not retried; Charinus santandereanus (Subterranean Biology 52) therefore unfiled. Plazi, Zenodo, bioone, ResearchGate not used. Sites returning a different paper for an article_preview id (zookeys 123624 and 9337 returned the eel and pseudoscorpion papers) were treated as unreliable and the matching paper was checked by Crossref.
- Mites (Acari), ticks, palpigrades, schizomids, ricinuleids, Zygentoma, Protura, Archaeognatha, Embioptera (extant), hagfish, lamprey, olm, miracidia and larval photoreceptor papers: searches returned no open CC BY page with a whole eye sentence (closed Zootaxa/Mapress, Plazi, biostor, springer, rupress, PMC).

Questions: Do verbless descriptive sentences ("Round eyes with star-shaped eye pigments (Fig. 14B).") count as whole sentences? d303 line 8 and d304 line 18 set the precedent; the chaetognath records depend on the answer.

## Desk disposition after audits 399 and 400
Audit 399 (lines 1-8): 7 fixable errors; audit 400 (lines 9-16): 4 fixable errors. Whole unit audited; all replacements applied; all 16 records merged.
