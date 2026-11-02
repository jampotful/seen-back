# audit-436: desk-d325, evidence lines 1 to 5

Audited 1 November 2026 from the desk-d325 files present untracked in the worktree (docs/views/evidence/desk-d325.jsonl, 9 lines, and docs/tracks/progress/desk-d325.md; neither committed here, neither edited). Scope: 1-based lines 1 to 5 only; lines 6 to 9 belong to another auditor. HEAD equals origin/main (f7fda7950). `python3 -I tools/senses/check.py --require-evidence-kind docs/views/evidence/desk-d325.jsonl`: "9 records, 0 problems". Quote lengths (`len(q.split())`): 17, 27, 14, 36, 40, all within 40 (line 5 exactly at the limit).

Sources opened (WebFetch; every URL from a WebSearch result): journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0135590 (two passes), journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0062938 (two passes), www.frontiersin.org/journals/ecology-and-evolution/articles/10.3389/fevo.2022.948324/pdf (two passes; the /text URL redirected to public-pages-files-2025.frontiersin.org, which returned the abstract only), www.nature.com/articles/srep06241 (three passes; body only, no header or rights box returned), www.mammaldiversity.org/taxon/1004563. Crossref single-DOI lookup api.crossref.org/works/10.1038/srep06241. Not opened: PMC, DOAJ, catalogue mirrors (utm.my, uitm.edu.my, uv.mx, bib-bvb.de, utb.cz), Springer, an elogim proxy result (skipped), ResearchGate, academia.edu. No curl, Sci-Hub or LibGen. WebFetch returns pieces of about 125 characters; every quote below was reassembled from consecutive pieces the tool reported as joined without gap. 9 WebSearches.

## Repeats

`grep -rl` over the whole docs/ tree (excluding desk-d325 files) for "Barbastella barbastellus", "Coelops frithii", "Hipposideros armiger", "Scalopus aquaticus", pone.0135590, pone.0062938, 948324, srep06241, Leitch, Seibert. Hits: Barbastella, H. armiger and Scalopus in gaps/try-species.json (not evidence); H. armiger in desk-d212.md only as an unread Doppler-shift lead (Schoeppler et al., different paper); Scalopus on main only as an Animal Diversity Web eye_type record (mammal-groups:167) and its sheet line. Leitch appears only in alligator and shark records (other papers). The Leitch, Sarko, Catania optic-nerve counts are on main as audit/mammal-groups:194 (retract): taxon "Sorex cinereus; Sorex palustris; ...", trait acuity_cpd, masked/water shrew optic-nerve fibres. Line 5 files the eastern mole's cochlear nerve count from a different sentence and structure; it does not repeat 194. No repeats among lines 1 to 5.

## Names and higher taxa

Barbastella barbastellus, Coelops frithii (MDD page opened: valid, Hipposideridae, Chiroptera; formosanus/inflata are synonyms, no split), Hipposideros armiger, Scalopus aquaticus: accepted names, no synonym. Barbastella page body prints only "European Vespertilionids"; "(Chiroptera: Vespertilionidae)" appears only in a reference title, so blank family/order is defensible. Coelops: "Family Hipposideridae" printed in the Introduction and filed; Chiroptera only in reference titles, order blank fine. H. armiger: the PDF Introduction prints "(Chiroptera: Hipposideridae)" but line 4 leaves both blank and its note says "Family and order not read"; moot because the line is held out. Scalopus: the Sci Rep body prints "Talpidae" (as sister family) and "monophyletic order Eulipotyphla"; the note's "Family and order not printed in the sections read" is inaccurate. Not counted (blank is not wrong data); optional fix below.

## Per line

### Lines 1 and 2, Barbastella barbastellus, peak frequency and source level

Bibliographic: printed byline Anna-Maria Seibert, Jens C. Koblitz, Annette Denzinger, Hans-Ulrich Schnitzler; citation "PLoS ONE 10(9): e0135590", 2015, DOI 10.1371/journal.pone.0135590; title verbatim. Licence: "This is an open access article distributed under the terms of the Creative Commons Attribution License". Accepted.

Line 1 quote, Results: "The peak frequency of type 1 calls measured 33.6 kHz, and for type 2 calls 40.1 kHz." MATCH, whole sentence. Line 2 quote: "Type 1 calls had an absolute SL of 80.9 dB SPL rms re 1 m and type 2 calls had a SL of 82.0 dB SPL rms." MATCH, whole sentence. Values say no more than the quotes. The neighbouring ASL sentence (79.9 / 82.4 dB apparent SL) is a different quantity; not omitted contrary data. Conditions verified: three roost sites near Bourges, central France; 29 June to 20 July 2009 and 3 to 5 June 2010; square array 24 sequences, 337 calls; individuals not verified, possible pseudoreplication across nights. Note on orifices: the Abstract concludes "type 1 signals are emitted through the mouth while type 2 signals and approach signals are emitted through the nose", reasoning from measured beam direction (type 1 downward, type 2 upward, about 70 degrees apart) plus the perpendicular mouth/nostril geometry; the array did not show the orifice. The note's "presumed" framing is fair; it omits that beam direction was measured (optional fix). Values are sequence-mean based; the record does not claim otherwise. Author initials written "Seibert AM ... Schnitzler HU" where the page prints "Seibert A-M ... Schnitzler H-U"; main uses both styles, not counted (optional).

**Line 1 OK. Line 2 OK.**

### Line 3, Coelops frithii, duty cycle 7.7%

Bibliographic: byline Ying-Yi Ho, Yin-Ping Fang, Cheng-Han Chou, Hsi-Chi Cheng, Hsueh-Wen Chang; "PLoS ONE 8(5): e62938", 2013; DOI 10.1371/journal.pone.0062938; title verbatim. Licence: "This is an open-access article distributed under the terms of the Creative Commons Attribution License". Accepted.

Quote, Abstract: "This species emitted echolocation calls at duty cycles averaging 7.7±2.8% (n = 87 sequences)." MATCH, whole sentence. Conditions verified: free-flying bats at a roost in an abandoned underground shelter, Beinan, Taitung, January to April 2011; 87 sequences, 425 calls; no individual count; 3 males and 3 females hand-netted and released about 2 m from the microphone for the sex comparison; no dimorphism.

Fault: **value says more than the quote.** Value "duty cycle averaging 7.7 +/- 2.8% (low duty cycle) in a species ostensibly high duty cycle". The "low duty cycle" label and "ostensibly high duty cycle" come from other Abstract sentences ("the hipposiderid Coelops frithii, ostensibly an HDC bat, consistently uses an LDC echolocation strategy ..."), not from the quoted sentence. One error, fixable by trimming the value. Also (not counted): the 7.7% pools sequences from four situations (approach, no approach, roost entrance, stationary; Results "consistently emitted calls at a high repetition rate (94.6±20.2 Hz) and LDC (7.7±2.8%)"), and duty cycle rose during target approach without reported values; conditions could say so (optional).

**Line 3 FIXABLE.**

### Line 4, Hipposideros armiger, population-mean peak frequency 66.80-72.51 kHz

Bibliographic: byline Aiqing Lin, Jiang Feng and Jagmeet S. Kanwal; Frontiers in Ecology and Evolution 10: 948324, 2022; DOI 10.3389/fevo.2022.948324; title verbatim (with subtitle "Acoustic Overflow Across Population Boundaries"). PDF prints "This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY)." Accepted.

Quote, Methods, "Statistical Analysis of Geographic Variation": "Mean peak frequencies of echolocation pulses with a maximum variation of about 6 kHz (66.80–72.51 kHz), showed significant differences across populations, clustering into three distinct groups: Eastern and Western China, Hainan (HN), and Southern Yunnan (SY)." Text MATCH, whole sentence, two pieces joined without gap.

Fault: **the value is not a measurement made in this paper.** The sentence before it reads "Earlier, echolocation pulse parameters were characterized for local populations."; the sentence after reads "This geographic distinction across populations was shown to result from the action of both indirect ecological selection and cultural drift (Lin et al., 2015a)."; the Abstract groups localities "based on previously established region-specific differences in the peak frequency of echolocation pulses". The paper has no Results figure or table of echolocation peak frequency per population (Figure 2, Table 1, Figures 3B and 6 concern social calls); per the tool, the Methods tie the echolocation data to Lin et al. (2015a). The record therefore files a restatement of earlier work at grade m, and its method field ("echolocation pulses recorded from wild-caught bats in a temporary laboratory near each roost") attributes that recording to this study. Secondary values are not filed (rules: review-sourced values not filed). One error, **unfixable** from this source; the primary source is the paper cited as Lin et al. 2015a (not opened here; its DOI was not reached through a permitted page, an elogim proxy result was skipped). Lead only.

**Line 4 UNFIXABLE (hold out).**

### Line 5, Scalopus aquaticus, cochlear nerve 10,127 myelinated axons

Bibliographic: the nature.com fetch returned the article body only (no header, citation box or rights section). Crossref (single-DOI): Duncan B. Leitch, Diana K. Sarko, Kenneth C. Catania; "Brain Mass and Cranial Nerve Size in Shrews and Moles"; Scientific Reports 4, issue 1, article 6241; published online and issued 2014-09-01; no print date. Record's authors, title, "Scientific Reports 4: 6241", 2014 and DOI agree. Byline order verified through Crossref and search-result title only, not on the printed header (caveat, not counted). Licence: no licence sentence in the text returned; Crossref licence array has https://creativecommons.org/licenses/by/4.0 content-version vor (and tdm), start 2014-09-01. Accepted under the "publisher page with no licence sentence + Crossref CC vor" rule.

Full sentence, Results, "Cochlear nerve" (four pieces, joined without gap): "The total number of myelinated axons of the cochlear nerve varied significantly with log brain size (y = 0.300x + 3.990, R2 = 0.906, p = 0.0127) (Fig. 3D) and log body size across (y = 0.240x + 3.553; R2 = 0.963, p = 0.0031) across the examined species, with the greatest number of axons found in the Eastern mole (mean = 10,127, Std dev. = 704) and the fewest in the smoky shrew (mean = 5865, Std dev. = 125) (Table S2)." The record's quote is this sentence with two marked cuts: (1) "(y = 0.300x ... p = 0.0031)" including "(Fig. 3D) and log body size across", (2) "and the fewest in the smoky shrew (mean = 5865, Std dev. = 125) (Table S2)." Every kept word matches. The cut marker is "[...]" rather than "…"; check.py does not test cut markers, rules.md requires only that cuts be marked, and main carries "[...]" in 6 other quotes: accepted. Neither cut removes a qualifier of the eastern-mole count; cut 1 drops a second significant correlate (log body size), which the note mislabels as "regression statistics omitted" (optional note fix; the dropped finding concerns the cross-species relation, not the filed value). The smoky shrew value is restated in conditions. Starts at the sentence start; contains 10,127 and SD 704; value 10127 with units "myelinated axons per cochlear nerve (mean; SD 704)" says no more than the quote. Methods: six eastern moles captured in Davidson County, Tennessee; no sex stated; per-species n for cochlear counts not stated (cochlear axon diameters n = 63). Conditions disclose all of this. Trait: main has no nerve-axon key (only retinal ganglion cell keys); sensory_anatomy with anatomical_measurement, structure "cochlear nerve" and a named measurement fits SENSORY-ANATOMY.md, and the note says no hearing function is established. Not a repeat of mammal-groups:194 (above).

**Line 5 OK.**

## Count

Lines judged: 5. Errors: 2 (line 3 value overstates quote, fixable; line 4 secondary value filed as this paper's measurement, unfixable). Error lines: 3, 4. OK: 1, 2, 5.

## Replacement

Line 3, field `value` (single field):
- old: `duty cycle averaging 7.7 +/- 2.8% (low duty cycle) in a species ostensibly high duty cycle`
- new: `duty cycle averaging 7.7 +/- 2.8% (n = 87 sequences)`

Line 4: drop the line (hold out). No replacement; lead for a future unit: the echolocation population means cited in this paper as Lin et al. 2015a (find and verify its DOI from a permitted page).

## Optional fixes (not counted)

Line 3, field `conditions` (old occurs once in line 3):
- old: `mostly free-flying;`
- new: `mostly free-flying; the 7.7% mean pools the 87 sequences from four situations (approach, no approach, roost entrance, stationary), and duty cycle rose during target approach without reported values;`

Line 3, field `note` (old occurs once in line 3):
- old: `Abstract sentence read on the full-text page.`
- new: `Abstract sentence read on the full-text page. The Abstract calls the species "ostensibly an HDC bat" that "consistently uses an LDC echolocation strategy".`

Line 5, field `note` (old occurs once in line 5):
- old: `(regression statistics omitted; sentence continues with the smoky shrew value)`
- new: `(the first cut removes the two regression statistics, "(Fig. 3D)" and the clause "and log body size across", i.e. the count also varied significantly with log body size; the second removes the smoky shrew value and "(Table S2)")`

Line 5, fields `family` and `order` plus note (multi-field raw JSON; old strings each occur once in line 5):
- old: `"family": "", "order": ""` -> new: `"family": "Talpidae", "order": "Eulipotyphla"`
- old: `Family and order not printed in the sections read.` -> new: `Family Talpidae and order Eulipotyphla as printed in the text.`

Lines 1 and 2, field `source.authors` (old occurs once in each line):
- old: `Seibert AM, Koblitz JC, Denzinger A, Schnitzler HU`
- new: `Seibert A-M, Koblitz JC, Denzinger A, Schnitzler H-U`

Lines 1 and 2, field `note` (old occurs once in each line):
- old: `are assigned by the authors from head anatomy and earlier work; the paper does not record which orifice emitted each call.`
- new: `are assigned by the authors from the measured beam directions (type 1 downward, type 2 upward, about 70 degrees apart) and the roughly perpendicular mouth and nostril openings; the array did not record which orifice emitted each call.`
