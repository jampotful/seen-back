# audit-439: desk-d327, evidence lines 1 to 5 (of 10)

Audited 1 November 2026 from the desk-d327 files present untracked in the worktree (docs/views/evidence/desk-d327.jsonl, docs/tracks/progress/desk-d327.md; neither committed here, neither edited). HEAD 6dd1541c1 (origin/main, desk d326 merged). This audit covers 1-based file lines 1 to 5 only; lines 6 to 10 go to another auditor. `tools/senses/check.py` on the file: 10 records, 0 problems. Quote lengths (`len(q.split())`), lines 1 to 5: 18, 26, 16, 15, 15, all within 40. Rules applied: /tmp/desk/rules.md (31 Oct 2026) throughout, with audit 295 for the JEB licence precedent and audits 402, 404 and 408 for higher-taxon fields. 9 WebSearch calls and 17 WebFetch calls. No library proxy, ResearchGate, academia.edu, Sci-Hub, LibGen, PMC or author-repository copy was opened (the arago.elte.hu, real.mtak.hu, core.ac.uk, zendy and typeset results for line 1 were left alone). WebFetch returns tool summaries in pieces of about 125 characters, so quotes were checked as MATCH/MISMATCH against verbatim pieces. Points marked "(tool summary)" were not returned verbatim.

## Licence (all five lines): met, with an owner question

What audit 295 accepted, read in full: five Company of Biologists pages (cob.silverchair.com, the host behind journals.biologists.com) that served Methods and Results in full without a login, printed only a publisher copyright line, and showed "No licence line, 'free' label or 'open access' label". Audit 295 ruled, following audits 290 and 293, that "free-to-read status is shown only by the page serving the full text without a login" and that this meets the rule, `access` "open". It also recorded that Crossref had a vor user-licence entry for some DOIs, an am-only entry for one, and none for others, and it treated the licence rule as met on all of them regardless.

What I found on the copies the unit read (journals.biologists.com URLs in the records' `url` fields, each opened):

| line | DOI | page access label | page licence/copyright | full text served without login | Crossref licence |
|---|---|---|---|---|---|
| 1 | 10.1242/jeb.139295 | none | "© 2016. Published by The Company of Biologists Ltd"; no licence line | Methods served (page cut off by the tool in the Fig. 5 caption); "no 'Access' or purchase prompt ... no login wall" (tool summary) | user-licence-1-1, vor, start 2017-02-15, delay 411 |
| 2 | 10.1242/jeb.158501 | none | "© 2017. Published by The Company of Biologists Ltd" plus link biologists.com/user-licence-1-1/ | Methods and Results served (first Results sentence returned) | user-licence-1-1/, vor, start 2018-03-15, delay 181 |
| 3 | 10.1242/jeb.048165 | none | "© 2010."; no licence statement | Methods and Results served | no licence field |
| 4, 5 | 10.1242/jeb.042937 | none | "© 2010."; no licence statement | Methods and Results served; Discussion partly (tool cut off in Fig. 6 caption) | no licence field |

The licence page that the 2016 and 2017 pages link to (biologists.com/user-licence-1-1/, opened) says non-subscribers get "Free access to non-subscribers to read 6 months after publication", for "research, teaching, private study. Not commercial use"; it is not a Creative Commons licence. All five papers are years past that six-month window, and every page served Methods and Results with no paywall or purchase prompt. These are the publisher's own free full-text pages, which rules.md lists as accepted. That matches audit 295 and is the same evidence. Licence met on lines 1 to 5; `access` "open" is right. None of the pages shows an "Open Access" or "Free" label, so free status rests on (a) full text served without a login and (b) the publisher's six-month free-access term. It does not rest on any label.

Consistency on main: desk-d173 held Egri et al. 2016 (this line 1 paper) on the ground "Licence not CC BY in Crossref; Biologists user licence", and desk-d276 held a Podarcis muralis JEB page (JEB 228(8) jeb249422, a 2025 paper that may have been inside the six-month window when read) because it "prints only the Biologists user-licence link, no CC sentence". Audit 295 and rules.md's "publisher's own free full text" accept such pages. I follow rules.md and audit 295.

Owner question 1: should "publisher's own free full text" cover a non-CC, non-commercial publisher licence whose free reading starts only after an embargo (Company of Biologists user licence 1.1), on the evidence that full text is served without a login and no access label is shown? If not, lines 1 to 5 (and lines 6 to 10, all JEB) would be held out, and desk-d173's hold of Egri 2016 was the right call. If yes, desk-d276's Podarcis page should be rechecked against the six-month window instead of being held for having no CC sentence.

Uncounted licence wording: on lines 3, 4 and 5 the note says the page shows "a link to the Company of Biologists user licence" and repeats "page shows only the copyright line". The 2010 pages returned only "© 2010." and no licence link. Replacement below.

## Names

- Podura aquatica: Linnaeus 1758 (plazi treatments in search results; Wikipedia page in search results). Not in docs/views/gaps/gbif-names.tsv. No sign of synonymy. Accepted.
- Camponotus blandus: gbif-names.tsv "Camponotus blandus EXACT ACCEPTED Camponotus blandus Camponotus 5033859"; printed on the page as "Camponotus blandus (Smith 1858)". Accepted.
- Sepioloidea lineolata: Wikipedia taxobox "Sepioloidea lineolata (Quoy & Gaimard, 1832)", family Sepiadariidae, order Sepiolida, synonym Sepiola lineolata. Accepted.
- **Sepia plangon (line 5): synonym.** gbif-names.tsv line 4430 is "Sepia plangon EXACT SYNONYM Ascarosepion plangon Ascarosepion 2290784". The repo's own docs/views/gaps/try-species.json lists "Ascarosepion plangon" (Mourning Cuttlefish).
- **Sepia mestus (line 4): synonym.** Not in gbif-names.tsv. The Wikipedia taxobox gives "Ascarosepion mestus (Gray, 1849)" with synonym "Sepia mestus Gray 1849", and says "Ascarosepion was revived as a genus in 2023" with Sepia mestus as its type species, citing Lupše et al. 2023. marineinfo.org gives the revision as Lupše N, Reid A, Taite M, Kubodera T, Allcock AL 2023, "Cuttlefishes (Cephalopoda, Sepiidae): the bare bones - an hypothesis of relationships", Marine Biology 170(8): 93, 10.1007/s00227-023-04195-3, re-instating Ascarosepion Rochebrune, 1884. try-species.json lists "Ascarosepion mestus" (Reaper Cuttlefish).

rules.md counts a synonym as an error. Both lines can be fixed by refiling under Ascarosepion with the printed name in the note, as this unit already does for Scarabaeus satyrus (printed Escarabaeus). The Sepia plangon row on main (sea-invertebrates:67, Temple et al. 2021 citing Temple et al. 2012) is filed under the old genus as well; that is outside this audit, but I flag it.

Higher taxa: for lines 1, 4 and 5 the unit filled family and order "from general taxonomy". The progress file discloses this, but the records do not. I did not see Poduridae, Poduromorpha, Sepiidae or Sepiida printed on the pages; line 1's title prints "Collembola" (the class). Main practice (audit 408: a disclosed, uncontroversial fill matching main is acceptable; audit 404: blank class is right when not printed; audit 402: blank when printed is a fault) makes this uncounted. The records should still say so in the note (replacement below). Main already files Sepia under Sepiidae, Sepiida, and Camponotus blandus under Formicidae, Hymenoptera. Line 3 leaves family and order blank and fills class Cephalopoda; that is acceptable.

## Repeats

`git grep -I` on HEAD over docs/, views/ and src/ for "Podura", "139295", "Camponotus blandus", "158501", "Sepioloidea", "048165", "Sepia mestus", "Sepia plangon", "042937", "Egri", "Yilmaz", "Talbot", and case-insensitive for the four DOIs in full. Hits:
- Podura: only search records (sweep-103 `chased`, sweep-55) and desk-d173's held-out list; no evidence row.
- Camponotus blandus: four review-sourced rows (insect:219 to 221, methods:854/855/1044; van der Kooi et al. 2021) with lambda_max 360 and 470 to 560 nm and colour_vision "likely dichromatic". The insect:221 note says the review's "Table 2 cites Yilmaz et al. 2017". That row is a different trait and a different finding (dichromacy from feeding/learning tests, compiled by a review). Line 2 is the innate UV preference, so it is not a repeat. Uncounted: line 2's note should name the main row.
- Sepia plangon: sea-invertebrates:67 (Temple et al. 2021, polarization threshold 1.05 deg from Temple et al. 2012, regraded g). It is a different paper and a different value, so not a repeat. Talbot and Marshall 2011 (Phil Trans B, retinal topography, three coleoids pooled) sits at sea-invertebrates:121/122, a different paper.
- Sepioloidea, Sepia mestus and the four DOIs: no hits.

Repeats 0.

## Per line

### Line 1: Podura aquatica, Egri et al. 2016 (10.1242/jeb.139295)

Page (record URL): title as printed, "Polarization sensitivity in Collembola: an experimental study of polarotaxis in the water-surface-inhabiting springtail Podura aquatica". Heading and citation_title metadata both have no comma before Podura (asked character by character). Crossref has a comma; the record follows the page, which is right. Authors in printed order "Ádám Egri", "Alexandra Farkas", "György Kriska", "Gábor Horváth", matching. DOI matches. Printed citation "J Exp Biol (2016) 219 (16): 2567–2576." Crossref carries no volume, issue or pages (article number jeb.139295; issued 2016).

Quote: MATCH, whole abstract sentence, read whole in one piece, 18 words, contains the value. The value says no more than the quote. Methods (verbatim pieces): "a total of 25,407 P. aquatica specimens were tested in 5 experiments covering 164 trials"; "An additional 300 springtails were also tested individually in experiment 6"; "Around 100-250 P. aquatica specimens were placed in the releaser"; "adults (males and females) were collected from the surface of ponds and creeks"; "in the vicinity of Budapest, between March and June 2015". `method` and `conditions` match. Abstract pieces "Horizontally and vertically polarized light were the most and least attractive, respectively" and "even if the polarized stimulus was 10 times dimmer" match the note's paraphrase. d* is not defined in the text returned. The note says so and marks the record partial; that is cautious but harmless.

Fault (bibliographic, fixable): `journal` gives "219(16): jeb139295". The page prints pages 2567–2576 and does not print the article number, and rules.md requires the citation as printed. Uncounted: the note's comma remark and "printed page range was not seen" are now settled (replacement below); add the family/order disclosure.

Verdict: fixable, 1 fault.

### Line 2: Camponotus blandus, Yilmaz et al. 2017 (10.1242/jeb.158501)

Page: title verbatim; authors "Ayse Yilmaz, Adrian G. Dyer, Wolfgang Rössler, Johannes Spaethe" in printed order; "J Exp Biol 15 September 2017; 220 (18): 3315–3326"; DOI matches. Crossref agrees (220, 18, 3315-3326, issued 2017-09-15).

Quote: MATCH, returned in two contiguous pieces, "Our results show that C. blandus foragers exhibit a strong innate preference for ultraviolet (UV, 365 nm)" "over blue (450 nm) and green (528 nm) wavelengths." It is a whole sentence of 26 words, and the value says no more. Fig. 3 caption: N=50 for equal-photon pairs, N=30 for I/10 pairs (tool summary). Methods: "stimuli pairs emitted equal numbers of photons", measured with a radiometrically calibrated spectrometer and neutral density filters; "only the first decision of each forager was recorded", with ants removed "to prevent retesting" (tool summary of the rest). Origin, verbatim: "All tested workers originated from a Camponotus blandus (Smith 1858) colony", "which was kept in a climate chamber ... at the University of Würzburg, Germany". The page has no queen, field or collection statement, and `conditions` says exactly that. The null is in the note and verified verbatim: "blue versus green: χ2=0.320, P=0.572"; "blue (I) versus green (I/10): χ2=0.133, P=0.715"; "blue (I/10) versus green (I): χ2=3.333, P=0.068". The tenfold persistence of the UV preference is also verified: "UV (I/10) versus blue (I): χ2=22.533, P<0.001"; "UV (I) versus green (I/10): χ2=10.800, P=0.001". The colour-preference section does not describe side randomisation (tool summary), whereas the learning tests were pseudorandomised. Uncounted; worth adding.

Verdict: OK. Uncounted: name the main review row (insect:221, colour_vision "likely dichromatic" via van der Kooi et al. 2021 citing this paper) in the note; add "side randomisation not described for the preference tests".

### Line 3: Sepioloidea lineolata, Talbot and Marshall 2010 (10.1242/jeb.048165)

Page: title as printed, "Polarization sensitivity and retinal topography of the striped pyjama squid (Sepioloidea lineolata – Quoy/Gaimard 1832)", matching the record and Crossref. Authors "Christopher M. Talbot; Justin Marshall"; "J Exp Biol (2010) 213 (19): 3371–3377"; DOI matches.

Quote: MATCH, whole abstract sentence, 16 words. Methods: "Two Sepioloidea lineolata were caught using sein nets in seagrass beds and mudflats at Dunwich", April 2008, North Stradbroke Island (tool summary for place and date); "were kept in tanks at Moreton Bay Research Station with a flow-through filtration system". Control 1, verbatim: "This was a black-and-white, vertically striped drum with stripes one inch (2.54 cm) in thickness". It is an intensity-contrast positive control. Results: "Each animal responded to the Test Drum (Fig. 7A) and Control 1 (Fig. 7C) with consistent and strong OKRs." Fig. 7 caption: "Neither specimen of S. lineolata responded to Control 2 – a plain linear polarizing filter." Design: the protocol was "repeated once for each specimen, for each of the three stimuli". No statistical test or P value is reported (tool summary). The page reports no measurement or matching of intensity between the polarizing stripes; it says only that external light was used "to enhance the apparent contrast between the stripes in the drums". Abstract piece: "This species displayed strong, consistent optokinetic nystagmic eye movements in response to a drum" (sentence continues).

Faults (fixable):
1. The value says more than the quote. It adds "two wild-caught animals" and "strong eye-movement responses to a rotating drum striped in alternating polarization e-vectors". The quoted sentence states only the first behavioural demonstration of a polarized optokinetic response. "Strong" comes from a different abstract sentence that was not quoted, and n and origin belong in `conditions` (where they already are).
2. Scientific context: the design limits are omitted. Each stimulus was run once per animal, no statistic is reported, and stripe intensity was neither measured nor matched. These go beyond "Only two animals". The note also says Control 1 "was not read"; it is a black-and-white stripe drum, so the Control 1 responses are a positive control and not contrary evidence.

Verdict: fixable, 2 faults.

### Line 4: Sepia mestus, Talbot and Marshall 2010 (10.1242/jeb.042937)

Page: title in two pieces, "Polarization sensitivity in two species of cuttlefish – Sepia plangon (Gray 1849) and Sepia mestus (Gray 1849)" and "demonstrated with polarized optomotor stimuli". The joining " – " between the pieces was not returned as a character; it is consistent with the record, and Crossref's own return was paraphrased at that point. Authors "Christopher M. Talbot; Justin Marshall"; "J Exp Biol (2010) 213 (19): 3364–3370"; DOI matches; Crossref agrees.

Quote: MATCH, whole Results sentence, 15 words. Before: "Further to this, no whole-body optomotor nystagmic responses were observed either." After: "Examples of an OMR performed by one representative of each species are shown in Fig. 7." Animals: "obtained from both a commercial supplier and private capture using sein nets in Moreton Bay, Queensland, Australia", March 2007 to July 2008 (tool summary), three of each species, mantle lengths 8 to 15 cm (tool summary). Control 1: "This was a black-and-white, vertically striped drum." "Two of the three S. mestus and two of the three S. plangon performed strong OMRs to Control 1." "The OMRs observed for the Test drum were not found to be statistically significantly different to those obtained in response to Control 1 [Welch two-sample t-test, P=0.944, CI=95%]". The page does not say whether the test pools the species, nor what response measure it uses. "No animal responded to Control 2." Each animal was tested once per stimulus "to avoid habituation" (tool summary). The page reports no measurement or matching of stripe intensity and names no photometer or radiometer (tool summary). External lights were used "to maximise the apparent contrast between the stripes".

Faults (fixable):
1. Name: Sepia mestus is a synonym of Ascarosepion mestus (above).
2. Scientific context: the design limits are omitted (one test per animal per stimulus; no stripe-intensity measurement). The note also leaves the non-significant comparison's partner as "not read" and calls the Control 1 responses "contrary figures". The comparison is Test versus Control 1 (Welch t-test, P=0.944), and Control 1 is a black-and-white stripe positive control.

Value: "3 of 3 animals" is "All S. mestus" combined with the printed n of three per species. The stimulus description is a gloss carried by `method`. Uncounted.

Verdict: fixable, 2 faults.

### Line 5: Sepia plangon, same paper

The page evidence is the same as for line 4. The quote MATCHes and is 15 words; "2 of 3" is "two of the three S. plangon".

Faults (fixable):
1. Name: Sepia plangon is a synonym of Ascarosepion plangon (gbif-names.tsv).
2. Scientific context: the same design omission and Control 1 / Welch t-test wording as line 4.

Uncounted: the note's "also on main from a different paper" should say that row is review-sourced (Temple et al. 2021 citing Temple et al. 2012) and filed under the old genus.

Verdict: fixable, 2 faults.

## Verdicts

| line | taxon | verdict | faults | fields |
|---|---|---|---|---|
| 1 | Podura aquatica | fixable | 1 bibliographic (pages as printed) | source.journal, note |
| 2 | Camponotus blandus | OK | 0 | (uncounted: note) |
| 3 | Sepioloidea lineolata | fixable | 1 value exceeds quote; 1 scientific context (design) | value, method, conditions, note |
| 4 | Sepia mestus -> Ascarosepion mestus | fixable | 1 name (synonym); 1 scientific context | taxon, method, note |
| 5 | Sepia plangon -> Ascarosepion plangon | fixable | 1 name (synonym); 1 scientific context | taxon, method, note |

Faults: 7 in 5 records; 4 of 5 records in error (80%), all fixable; 0 unfixable. By kind: bibliographic 1, quote/value 1, scientific context 3, name 2, licence 0, repeats 0, quote-form 0.

## Replacement

Each old string occurs exactly once in its line (checked by script). Taxon edits are raw-JSON fragments.

Line 1:
- `source.journal`: "Journal of Experimental Biology 219(16): jeb139295" -> "Journal of Experimental Biology 219(16): 2567-2576"
- `note`: " The page title may carry a comma before Podura aquatica in Crossref." -> " Crossref prints a comma before Podura aquatica; the page heading and citation_title metadata have none, so the page wording is used."
- `note`: "; the printed page range was not seen, so the article number is given." -> "; the page prints J Exp Biol (2016) 219 (16): 2567-2576. The user licence gives non-subscribers free access to read 6 months after publication, and the page serves the Methods without a login. Family Poduridae and order Poduromorpha were not seen printed on the page; they are filled from standard classification."

Line 3:
- `value`: "polarized optokinetic response demonstrated in two wild-caught animals, which gave strong eye-movement responses to a rotating drum striped in alternating polarization e-vectors" -> "first behavioural demonstration of a polarized optokinetic response in any cephalopod"
- `method`: "Control 1 and Control 2 drums also run" -> "Control 1 (black-and-white vertically striped drum) and Control 2 (plain linear polarizing filter) also run; each stimulus run once per animal; no statistical test reported; no measurement or matching of intensity between the polarizing stripes reported"
- `conditions`: "April 2008" -> "April 2008; kept in flow-through tanks at Moreton Bay Research Station before testing"
- `note`: "Only two animals." -> "Only two animals, each tested once per stimulus; the paper reports no statistical test and no measurement of intensity differences between the polarizing stripes."
- `note`: "(what Control 1 consists of was not read)" -> "(Control 1 is a black-and-white vertically striped drum, an intensity-contrast positive control)"
- `note`: "page prints only the copyright line (and a link to the Company of Biologists user licence); Crossref has no licence entry for this DOI; page shows only the copyright line." -> "page prints only \"© 2010.\", with no licence line and no access label, and serves Methods and Results without a login; the Company of Biologists user licence 1.1 gives non-subscribers free access to read 6 months after publication; Crossref has no licence entry for this DOI."

Line 4 (raw JSON for taxon):
- `"taxon": "Sepia mestus"` -> `"taxon": "Ascarosepion mestus"`
- `method`: "and a further control (Control 1)" -> "and a black-and-white vertically striped drum (Control 1); each animal tested once per stimulus (to avoid habituation); no measurement or matching of stripe intensity reported"
- `note`: "Contrary figures in the same paper" -> "Positive-control figures in the same paper"
- `note`: "and optomotor responses to the Test drum were not statistically significantly different (comparison partner not read, fetch returned a fragment)" -> "and the Test-drum OMRs were not statistically significantly different from those to Control 1 (Welch two-sample t-test, P=0.944; whether species were pooled and which response measure was used are not stated)"
- `note`: "page prints only the copyright line (and a link to the Company of Biologists user licence); Crossref has no licence entry for this DOI; page shows only the copyright line." -> "page prints only \"© 2010.\", with no licence line and no access label, and serves Methods and Results without a login; the Company of Biologists user licence 1.1 gives non-subscribers free access to read 6 months after publication; Crossref has no licence entry for this DOI. Filed under the accepted name Ascarosepion mestus (Gray, 1849); printed as Sepia mestus (Gray 1849); Ascarosepion re-instated by Lupše et al. 2023, Marine Biology 170: 93, 10.1007/s00227-023-04195-3. Family Sepiidae and order Sepiida filled from standard classification (not printed on the page)."

Line 5 (raw JSON for taxon):
- `"taxon": "Sepia plangon"` -> `"taxon": "Ascarosepion plangon"`
- `method`, `note` "Contrary figures...", `note` "and optomotor responses...": same old -> new as line 4.
- `note`: "page prints only the copyright line (and a link to the Company of Biologists user licence); Crossref has no licence entry for this DOI; page shows only the copyright line." -> as line 4, but with the name sentence reading "Filed under the accepted name Ascarosepion plangon (gbif-names.tsv: Sepia plangon EXACT SYNONYM Ascarosepion plangon); printed as Sepia plangon (Gray 1849)." followed by the same family/order sentence.
- `note`: "Sepia plangon polarization is also on main from a different paper." -> "A Sepia plangon polarization threshold is on main from a different paper (sea-invertebrates:67, Temple et al. 2021 reporting Temple et al. 2012, grade g, filed under the old genus)."

## Optional fixes (uncounted)

- Line 2 `note`: append "Main carries a review-sourced colour_vision row for this species (insect:221, 'likely dichromatic', van der Kooi et al. 2021 Table 2 citing this paper's learning tests); this record is the innate-preference result. Side randomisation is not described for the preference tests."
- Line 2 `note`, licence: "Licence: publisher's own free full text on journals.biologists.com; page prints only the copyright line (and a link to the Company of Biologists user licence);" -> "Licence: publisher's own free full text on journals.biologists.com, served without a login and with no access label; page prints only the copyright line and a link to the Company of Biologists user licence (free to non-subscribers 6 months after publication);"
- Line 1: `partial` true is cautious; the page serves the Methods, and only the Results were cut off by the tool. Leave it.
- Line 3: family Sepiadariidae (Wikipedia taxobox; order there given as Sepiolida) may be filled with a disclosure, or left blank.

## Owner questions

1. Licence: see the licence section above. The question is whether Company of Biologists pages under user licence 1.1 (not CC, non-commercial, free to read after six months, no access label) count as "publisher's own free full text". Applied as yes here, following rules.md and audit 295. This contradicts desk-d173's hold of this same line 1 paper and the ground given for desk-d276's Podarcis hold.
2. Names: Sepia plangon is on main under the old genus (sea-invertebrates:67). Should it be refiled under Ascarosepion, consistent with gbif-names.tsv and try-species.json?
