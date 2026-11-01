# audit-420: desk-d314, all 7 evidence lines

Audited 1 November 2026 from the desk-d314 files present untracked in the worktree (docs/tracks/progress/desk-d314.md and docs/views/evidence/desk-d314.jsonl, 7 lines; neither committed here, neither edited). HEAD equals origin/main (46aeaadd7). `python3 -I tools/senses/check.py | grep d314`: "docs/views/evidence/desk-d314.jsonl: 7 records, 0 problems". Quote lengths (`len(q.split())`): 39, 7, 21, 16, 19, 7, 10, all within 40.

Sources opened (WebFetch, every URL from a WebSearch result): zookeys.pensoft.net/article_preview.php?id=2388 (two passes), and the Pensoft article XML zookeys.pensoft.net/article/<id>/download/xml/ for 15118 (two passes), 52751 (two passes), 9619, 62391, 111420, 140329; wsc.nmbe.ch/species/7683; novataxa.blogspot.com/2023/11/heniklynchus.html, cavefishes.org.uk/species-record.php?id=349 and one calacademy catalogue record (wrong species, not used) for the Henicorhynchus name. Crossref single-DOI lookups (api.crossref.org/v1/works/) read for 163.2265, 965.52751 (on retry), 640.9619, 1031.62391 and 1230.140329 (on retry); 713.15118 failed with client_error twice and 1184.111420 was rate-limited twice, so for those two the publisher citation in the article XML was used, as stated. PMC, GBIF, WoRMS, Plazi, BHL, DOAJ, library catalogues (ebusca.uv.mx, katalog.lib.cas.cz, libmast.utm.my), x-mol, omicsdi, reviewer.ly and the VLIZ PDF were not opened; no curl, proxy, ResearchGate, academia.edu, Sci-Hub or LibGen. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 14 WebSearches.

## Bibliographic and licence

- Line 1 (Miller, Rahmadi 2012). Page metadata byline "Jeremy Miller, Cahyo Rahmadi"; Crossref same order; title identical; "ZooKeys 163: 1–11"; issued 2012-01-09. Licence printed: "This is an open access article distributed under the terms of the Creative Commons" / "Attribution License 3.0 (CC-BY), ..."; Crossref CC BY 3.0 vor. Accepted.
- Line 2 (Kamimura, Ferreira 2017). XML byline Yoshitaka Kamimura, Rodrigo L. Ferreira; title "Earwigs from Brazilian caves, with notes on the taxonomic and nomenclatural problems of the Dermaptera (Insecta)" identical; ZooKeys 713: 25–52, 2017; "Creative Commons Attribution License (CC BY 4.0)" printed. Crossref not readable (client_error twice); not worked around.
- Line 3 (Nguyen, Ho, Hoang, Wu, Zhang 2020). XML and Crossref identical in order; title identical including the curly single quotation marks around the genus; 965: 85–101; issued 2020-09-03; CC BY 4.0 printed and Crossref vor. Accepted.
- Line 4 (Sun, Li 2016). The article XML byline is Yue Sun, then Xinzheng Li (corresponding); Plazi's citation title also gives "Sun, Yue & Li, Xinzheng, 2016". Crossref lists the authors in reverse (Xinzheng Li, Yue Sun). The record follows the printed byline, which is the rule; right. Title identical; 640: 37–43; issued 2016-12-13; CC BY 4.0 printed and Crossref vor.
- Line 5 (Lörz, Horton 2021). XML and Crossref identical; title identical; 1031: 19–39; issued 2021-04-14; CC BY 4.0 printed and Crossref vor.
- Line 6 (Wang, Sha, Ren 2023). XML byline Yanrong Wang, Zhongli Sha, Xianqiu Ren; 1184: 261–271, 2023; CC BY 4.0 printed. Crossref rate-limited twice; not worked around.
- Line 7 (Zhou, Zhang, Shen, Mao, Zhang, Zhang 2025). XML and Crossref identical (Yadong Zhou, Ruiyan Zhang, Chengcheng Shen, Qin Mao, Mouyingke Zhang, Dongsheng Zhang); title start identical in Crossref (rest summarised by the tool) and identical in the XML; 1230: 25–36; issued 2025-03-05; CC BY 4.0 printed and Crossref vor.

ZooKeys prints no issue numbers; none filed. Bibliographic faults 0; licence faults 0; source.access "open" right throughout. Optional (not counted): the notes on lines 1, 3, 4, 5 and 7 say "Crossref was not checked (lookup failed)"; Crossref was read here and agrees (line 4 with reversed author order, see above).

## Names and higher taxa

- Amauropelma matakecil: World Spider Catalog "Amauropelma matakecil Miller & Rahmadi, 2012", Ctenidae, female only, original description the only taxonomic entry. Accepted. Page prints Araneae and Ctenidae, no class (tool summary: "it does not state the class (Arachnida) anywhere"). Class blank right.
- Cylindrogaster cavernicola: headings Order Dermaptera, Family Diplatyidae (taxon block says Pygidicranidae, as the note discloses); Insecta only in title and citation. Class Insecta from the title is acceptable, disclosed, as audit-408 accepted order from a title. Dermaptera Species File not checked (budget); no later combination seen in results.
- 'Henicorhynchus' thaitui: taxon block Cypriniformes, Cyprinidae; no class line ("Teleostei is labelled as a subclass only in the article title and subject groups", tool summary). Class blank right. Eschmeyer's Catalog record not reached; cavefishes.org.uk lists "Henicorhynchus thaitui" with no synonyms and says the generic placement is doubted but no new genus is named; the novataxa post gives no new combination. Binomial accepted as filed.
- Linopherus beibuwanensis: taxon block Animalia, Amphinomida, Amphinomidae; Polychaeta only in subject categories and reference titles. Class blank right.
- Amathillopsis inkenae: taxon block Amphipoda, Amathillopsidae; "Malacostraca" does not appear. Class blank right.
- Orchomenella compressa: taxon block Amphipoda, Tryphosidae; no class. Class blank right.
- Eunice siphoninsidiator: taxon block Eunicida, Eunicidae; Polychaeta only in keywords. Class blank right.
- WoRMS is refused under the desk rules; the four marine names were not contradicted by any search result (all are original descriptions of 2016 to 2025). Not counted.

eye_type fits all seven (presence/absence, development and colour of eyes).

## Repeats

`git grep -i -E` on origin/main (46aeaadd7) over the whole docs/ tree for the seven genera/epithets and the seven DOIs. No evidence, audit/corrected, audit/ALL, sheets or searched hits. Only progress-note mentions: desk-d293.md, desk-d297.md and desk-d310.md each set Cylindrogaster cavernicola aside ("no state or count"); that is a screening judgement, not a filed value, so line 2 is not a repeat (see line 2). "cavernicola" otherwise hits other species (Hendea myersi cavernicola, Litoria cavernicola). Unmerged origin/research/desk-d* branches: no hits (see Verdict section).

## Per line

### Line 1, Amauropelma matakecil, eyes vestigial

Description, run-in "Eyes." text, read in three abutting pieces on two passes: "Eyes. Vestigial, eye rows recurved forming 2.4.2 pattern, ALE>AME=PME>PLE, AME on small common tubercle," / "ALE and PME form slightly procurved row, PME closer together than PME-ALE, PME slightly more widely spaced than AME," / "eye group = 0.40 of carapace width (Figs 2, 3)." **Quote MATCH**: whole telegraphic sentence after the run-in label, 39 words, the trailing "(Figs 2, 3)." replaced by "…", which is a legitimate trailing figure-reference cut; no qualifier dropped. Value says no more than the quote. Holotype "1 #f", Gua Anjani, 7.73156°S 110.11567°E, 672 m, 23 March 2009 (MZB.Aran.500, S. Harjanto): right. Paratypes: Gua Seplawan 23 April 2010 (MZB.Aran.501) and Gua Nguwik 9 May 2008 (RMNH.ARA.12434), each "1 #f": right. Male: "Repeated attempts to target males have so far failed."; right. Diagnosis ("except Amauropelma leo ... by having small eyes (Fig. 2; large in other species except Amauropelma undara, which is a blind troglobite)"), Remarks ("reduced eyes"; "exhibiting neither eye reduction nor reduced pigmentation" of another species) and Discussion ("in contrast to our new species which has vestigial eyes.") all carried.

Fault: **type status of the juveniles.** The conditions read "paratypes 2 females (...) and 3 juveniles from Gua Anjani", which makes the juveniles paratypes. The page lists them under "Additional material examined:" ("2 juveniles", RMNH.ARA.12436; "1 juvenile", MZB.Aran.502; tool summary for the heading), not as paratypes. One record error, fixable.

**Line 1 FIXABLE.**

### Line 2, Cylindrogaster cavernicola, eyes prominent

Male, Head: "Eyes prominent, slightly shorter than post-ocular length." **Quote MATCH**, whole telegraphic sentence, 7 words. Holotype only ("Holotype ♂, 'Gruta Apertar | da Hora | Jandaíra RN ...'", "'ISLA | 21101', '15.ii.2010 | Ferreira, R.L. leg.'"); "Female. Unknown." Right. Diagnosis and Remarks silent on eyes: right. Three earlier desks set this species aside as "no state or count"; "prominent" eyes do state development (eyes present, not reduced), and a whole Description sentence of this kind has been accepted before, so the record is admissible.

Fault: **habitat context omitted.** The record is filed as a cave earwig ("Gruta ..."; "a paper on earwigs from Brazilian caves"), but the page says the holotype "was collected near the entrance of a cave associated with limestone rocks from the Jandaíra formation" and the Etymology says the name "refers to the cave-dwelling habit of this new species, although it is presently unknown" / "whether it is a troglobite." An eye-state record for a cave species without the near-entrance collection and the open troglobite status misstates the context in which "prominent" is read. One record error, fixable.

**Line 2 FIXABLE.**

### Line 3, 'Henicorhynchus' thaitui, eyes smaller but not vestigial

Troglomorphic characters paragraph: "The eyes are smaller than in congeneric epigean species, but not vestigial or absent" / "as is common in hypogean fish species." **Quote MATCH**, one whole sentence, 21 words; the "where" names the paragraph correctly. Description ("Eye relatively small, positioned laterodorsally in anterior half of head and considerably behind or above rictus," ... "diameter less than maxillary-barbel length."), Diagnosis ("smaller (vs. larger) eyes ..."), "reduced eye size" in the same paragraph, and Table 1 eye diameter in % HL (17.7 | 10.9 | 17.7 | 13.6) all carried. Holotype IEBR 105901, 74.3 mm SL, Khe Lanh Cave, 12 August 2011, A.T. Ho and N.T. Hoang; paratypes 5 + 4 + 4 = 13 with the holotype's data; "At least 50 individuals of various sizes were observed in streams and pools, 14 of which were caught by hand net (Fig. 7)."; no sex anywhere. All right.

**Line 3 MATCH.**

### Line 4, Linopherus beibuwanensis, two pairs of reddish eyes

Description, Prostomium: "Posterior lobe heart-shaped, bilobed along posterior margin, with median antenna and two pairs of reddish eyes." **Quote MATCH**, whole sentence, 16 words. Next sentence ("Anterior pair of eye spots semicircular in shape and large, posterior pair of eye spots rounded and small."), Diagnosis ("with two pairs of eyes, anterior pair semicircular in shape"), Remarks contrast ("the latter has no externally detectable eyes ...") carried. Holotype MBM010010, 91 m, sandy mud, 11 Feb 1959; paratypes MBM200142, 200143, 200144, 200145, 200122 at 66–93 m (MBM200122 has no depth printed), 1959–1962; "One female paratype (MBM200143) with eggs"; "preserved in 75% ethanol solution"; "Color in alcohol pale yellow". Preserved colour as the note says. Right.

**Line 4 MATCH.**

### Line 5, Amathillopsis inkenae, eyes white in life, fading in fixation

Remarks: "Eyes are clearly visible, solid white, in live and fresh condition, but fade after a few days of fixation." **Quote MATCH**, whole sentence, 19 words. Description "eyes present, pigmented, strongly white in fresh specimen"; genus diagnosis "eyes present (round or ovoid) or absent": carried. Holotype "Male, 9.4 mm", 4622 m, 20 July 2020, RV 'Sonne' cruise 267, ROV KIEL 6000, ZMH K-60236; paratype "Male, 14 mm", 4834–4844 m, 06 June 2018, RRS 'James Cook', Otter Trawl Semi-Balloon 14, NHMUK 2021.66; holotype photographed on board, "placed in RNAlater", then "transferred to the -20 °C freezer". All right.

**Line 5 MATCH.**

### Line 6, Orchomenella compressa, no trace of eyes in ethanol material

Description, Head: "Eyes: no trace visible in ethanol-preserved materials." **Quote MATCH**, whole telegraphic sentence after the run-in label, 7 words; value keeps the preservation limit. Holotype "MBM 286555, ♀ (6.2 mm), dissected, ... depth 1243 m, 16 April 2014."; paratype "MBM 286555, ♂ (5.6 mm), same collection data as holotype." (same number, as the conditions disclose); additional "MBM 286566, 4♀♂, ... RY0069, ROV-3, depth 1243 m, 16 Apr. 2014." Remarks "in lacking of eyes" and Abstract "the absence of eyes" carried; the Description is not tied to one sex (figures holotype female and paratype male), as the conditions say. Right.

**Line 6 MATCH.**

### Line 7, Eunice siphoninsidiator, eyes dark

Description: "Eyes dark, lateral to ceratophores of lateral antennae (Fig. 2G)." **Quote MATCH**, whole telegraphic sentence, 10 words, figure reference kept. Holotype RSIOPOLY80001, O-Hakucho Guyot, 1135 m, 27 June 2023, 100% ethanol; paratype 1# RSIOPOLY80002 (30 June 2023, 1175 m, ethanol); paratype 2# RSIOPOLY86005 (Albo Guyot, 1057 m, 3 September 2024, 10% formalin); five incomplete additional specimens (Albo Guyot, DD Seamount; 1047–1126 m; August–September 2024); no sexes; no Diagnosis; Abstract, Remarks, Variation and Discussion silent on eyes. Right. The conditions' "The Description draws on the type series" is an inference (the paper does not say which specimens the Description rests on; Measurements cover holotype and both paratypes, and the Figure 2 caption shows the "location of eye in the paratype"); not counted, optional fix below.

**Line 7 MATCH.**

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Amauropelma matakecil, eyes vestigial | FIXABLE | conditions | 3 juveniles written as paratypes; page lists them as additional material |
| 2 | Cylindrogaster cavernicola, eyes prominent | FIXABLE | conditions | near-entrance collection and "presently unknown whether it is a troglobite" omitted |
| 3 | 'Henicorhynchus' thaitui, eyes smaller, not vestigial | MATCH | | whole sentence; Description, Diagnosis, Table 1 carried |
| 4 | Linopherus beibuwanensis, two pairs of reddish eyes | MATCH | | byline order as printed (Crossref reverses it) |
| 5 | Amathillopsis inkenae, white eyes fading in fixation | MATCH | | Remarks sentence; both males right |
| 6 | Orchomenella compressa, no trace of eyes in ethanol | MATCH | | preservation limit kept; shared catalogue number disclosed |
| 7 | Eunice siphoninsidiator, eyes dark | MATCH | | type-series basis is an inference (optional fix) |

Errors: 2 of 7 records (28.6%); 2 fixable (lines 1, 2), 0 held out, 0 unfixable; no line to drop. Repeats on main: none. Unmerged origin/research/desk-d* branches (all except d314): every file each branch changes under docs/views relative to origin/main (397 files) grepped for the seven species and DOIs: no hits. Verdict for desk-d314: **ACCEPT AFTER REPLACEMENT** (lines 3 to 7 as filed; lines 1 and 2 with the replacements below, or dropped if they are not applied).

## Replacement

Each old string is copied from the desk file and occurs once in the line named (checked with `str.count`).

Line 1:
- `conditions`: "paratypes 2 females (MZB.Aran.501, Gua Seplawan, 23 April 2010; RMNH.ARA.12434, Gua Nguwik, 9 May 2008) and 3 juveniles from Gua Anjani." -> "paratypes 2 females (MZB.Aran.501, Gua Seplawan, 23 April 2010; RMNH.ARA.12434, Gua Nguwik, 9 May 2008); 3 juveniles from Gua Anjani (RMNH.ARA.12436, MZB.Aran.502) are listed as additional material examined, not as paratypes."

Line 2:
- `conditions`: "The species is treated in a paper on earwigs from Brazilian caves." -> "The holotype 'was collected near the entrance of a cave associated with limestone rocks from the Jandaíra formation', and the Etymology says the name refers to the cave-dwelling habit 'although it is presently unknown whether it is a troglobite.'"

Optional, not counted:
- Line 7 `conditions`: "The Description draws on the type series, not only the holotype" -> "The paper does not say which specimens the Description rests on (Measurements cover the holotype and both paratypes; the Figure 2 caption shows the 'location of eye in the paratype')"
- Lines 1, 3, 4, 5, 7 `note`: "Crossref was not checked (lookup failed)" -> "Crossref read by the auditor agrees (line 4: Crossref reverses the author order; the printed byline is followed)" (apply per line; the old string occurs once in each).
