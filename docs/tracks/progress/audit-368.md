# audit-368: desk-d276, evidence line 1

Audited 1 November 2026 from the desk-d276 files present untracked in the worktree (docs/tracks/progress/desk-d276.md and docs/views/evidence/desk-d276.jsonl, 1 line; neither committed here, neither edited). Worktree HEAD and origin/main 45821c8c (d275 merged after audit 367). `python3 -I tools/senses/check.py | grep 'd276\.'`: "docs/views/evidence/desk-d276.jsonl: 1 records, 0 problems". Quote length (`len(q.split())`): 13. Non-ASCII in the quote: "µ" only, as printed. Format model audit 358; desk-audit.md evidence clause (40-word limit; a lead is not reinstated on length alone); /tmp/desk/rules.md (31 October 2026).

Sources opened (WebFetch): journals.biologists.com/bio/article/6/4/496/1866/In-air-hearing-of-the-great-cormorant (four passes: byline, citation, licence, Abstract; Methods and Results on animal, frequencies, threshold, noise; the masking passage and Discussion; the citation and licence lines again); api.crossref.org/works?filter=doi:10.1242/bio.023879 (answered; two list queries by title returned nothing); www.fws.gov/taxonomic-tree/29892; ebird.org/species/grecor5. bio.biologists.org/content/6/4/496 failed at its site (client_error); pubmed.ncbi.nlm.nih.gov/28288967 returned a reCAPTCHA interstitial, not worked around. PMC, the DOAJ/library-catalogue mirrors, zendy.io, ResearchGate and Semantic Scholar results were not opened. No curl, library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 125 characters; points marked "(tool summary)" were not returned verbatim. 6 WebSearches (2 extended).

## Bibliographic and licence

- Page citation, verbatim: "Alyssa Maxwell, Kirstin Anderson Hansen, Sara Torres Ortiz, Ole Næsbye Larsen, Ursula Siebert, Magnus Wahlberg;" | "In-air hearing of the great cormorant (Phalacrocorax carbo). Biol Open 15 April 2017; 6 (4): 496–502." | "doi: https://doi.org/10.1242/bio.023879". Received 29 Dec 2016, accepted 09 Mar 2017, version of record 13 March 2017 (tool summary). Author order, full title, 6(4): 496-502 and printed year 2017 all as recorded. DOI verified.
- Crossref (filter=doi): authors in the same order (given/family: Alyssa Maxwell; Kirstin Anderson / Hansen; Sara / Torres Ortiz; Ole / Næsbye Larsen; Ursula Siebert; Magnus Wahlberg); title identical (Phalacrocorax carbo in italics markup); Biology Open; no volume, issue or page, article number bio.023879; issued and published-online 2017-01-01; one licence entry, http://creativecommons.org/licenses/by/3.0, content-version am, delay 1598 days; no relation, no update-to.
- Uncounted: the record's initials render "Torres Ortiz" as "Ortiz ST" and "Næsbye Larsen" as "Larsen ON". Crossref files the compound forms as family names, but it also files "Hansen" alone with "Kirstin Anderson" as given names, so its own split is not consistent, and the page prints full names with no family/given split. The record's form is a standard initials rendering and the order is right; I do not count it. If the owner wants Crossref's families, the strings are "Torres Ortiz S" and "Næsbye Larsen O".

Licence. The copy read is the Company of Biologists' own article page, serving the full text (Methods, Results, Discussion) without a login. It prints, verbatim in three pieces: "This is an Open Access article distributed under the terms of the Creative Commons Attribution License" | "which permits unrestricted use, distribution and reproduction in any medium" | "provided that the original work is properly attributed.", linked to creativecommons.org/licenses/by/3.0 (tool summary of the link); "© 2017" with The Company of Biologists Ltd as holder (tool summary). Rules applied:
1. Publisher's own free full text is accepted outright (rules.md; audits 290, 293, 295 for Biologists pages on journals.biologists.com / cob.silverchair.com).
2. The page carries an open statement on the exact copy read.
3. The Crossref tag is CC BY 3.0, the same licence the page links; it does not conflict. The am content-version means Crossref registered it for the accepted manuscript only, and rules.md holds out records whose licence rests on an am licence. This record does not rest on it: it rests on the page sentence on the publisher's own copy, and the am tag only agrees with it.
4. The earlier "Biologists user licence" holds (desk-d228 and d230 JEB leads; desk-d267 jeb217265, the 2020 amphibious-hearing paper, am user licence; desk-d276's own Podarcis muralis jeb249422 hold, page printing only the user-licence link) concern pages with no CC sentence or copies other than the publisher's. Under audits 290 to 295 even those publisher pages would pass as free full text; none of them bears on a page that prints CC BY.

**Licence: passes.** source.access "open" right. Answer to the d276 owner question: yes for this case. An am-only Crossref licence plus a page-printed CC Attribution sentence on the publisher's own free full text is accepted, provided the am tag is not a different (conflicting) licence. Bibliographic faults 0; licence faults 0.

## Names

- docs/views/gaps/gbif-names.tsv line 3693: "Phalacrocorax carbo	EXACT	ACCEPTED	Phalacrocorax carbo	Phalacrocorax	2481890". Met.
- USFWS taxonomic tree 29892 (tool summary of the hierarchy): Great Cormorant, Phalacrocorax carbo; Aves; Suliformes; Phalacrocoracidae; Phalacrocorax. eBird/Clements page grecor5 (a subspecies-group page, "Phalacrocorax carbo maroccanus"): "Suliformes", "Phalacrocoracidae". IOC not opened (the search returned no IOC page). Family and order agree with main's existing Phalacrocorax carbo rows (corrected/birds.jsonl:151; canon-3:60; canon-5:129). The paper names no subspecies (the 2020 JEB paper uses P. c. sinensis); species rank is right. Met.

Name faults 0.

## Duplicates

git grep on origin/main (45821c8c) across the whole docs/ tree (including docs/views/audit/corrected, audit/ALL.jsonl, sheets, searched/) for cormorant, Phalacrocorax, 023879 and Maxwell A: main holds Phalacrocorax carbo only under acuity_cpd, binocular_deg, lambda_max_nm, behaviour_vision and a family-level oil_droplets row; no sense_hearing row for the species and no row with DOI 10.1242/bio.023879. Hold-outs: desk-d268.md line 7 and desk-d273.md lines 19 and 22 (this lead, not read, flagged for retry); desk-d267.md line 16 (a different paper, jeb217265, held for licence). All 166 remote branches matching origin/research/desk-d2* or origin/research/audit-3*: lines with 023879, jeb217265 or sense_hearing next to the species occur only in the d268/d273 hold notes and the desk-d276 files themselves. No audit-3*.md names the cormorant hearing lead. This is a retry of a never-read lead, not a repeat.

Duplicates 0.

## Trait key and units

sense_hearing in-air bird and mammal rows on main: desk-d166 Neomonachus schauinslandi value "best sensitivity: lowest threshold 40 dB re 20 uPa at 0.8 and 3.2 kHz", units "dB re 20 uPa", eye "ear (in air)"; desk-d164 Spheniscus humboldti eye "ear (in air)"; desk-d218 Neophoca cinerea "in-air thresholds of 13 and 14 dB re 20 uPa". d276 follows the d166 pattern exactly; dB re 20 µPa (air reference) is the convention, and dB SPL rows on main (d145, d194, d215) are the same quantity under the other name. Uncounted: main writes "uPa" in value and units; d276 writes "µPa" as the quote prints it (d160 also uses "µPa"). Either passes check.py; the owner may want one form. The record nowhere suggests underwater hearing: eye "ear (in air)", reference 20 µPa, title "In-air hearing". The page reports no underwater testing (tool summary; the Discussion only calls for "Further studies on the underwater hearing abilities of marine birds", verbatim piece).

Grading m: one named species measured directly. Met.

## Per-record findings

### Line 1, Phalacrocorax carbo, lowest in-air threshold 18 dB re 20 µPa rms at 2 kHz

Abstract, verbatim sentence by sentence (sentences 3 and 7 returned in part): "Many aquatic birds use sounds extensively for in-air communication." / "Regardless of this, we know very little about their hearing abilities." / "The in-air audiogram of a male adult great cormorant (Phalacrocorax carbo) was determined using psychophysical methods" (continues with the method of constants, tool summary) / "Hearing thresholds were derived using pure tones of five different frequencies." / "The lowest threshold was at 2 kHz: 18 dB re 20 µPa rms." / "Thresholds derived using signal detection theory were within 2 dB of the ones derived using classical psychophysics." / "The great cormorant is more sensitive to in-air sounds than previously believed" (continues: comparable to several similar-sized birds, tool summary). **Quote MATCH**, 13 words, whole sentence, its start and end both seen with neighbours on either side; "µPa rms" as printed. The value says no more than the quote; "best sensitivity" is supported by the Discussion piece "The great cormorant showed the best sensitivity to sound in the region of 1 to 2 kHz,". "where" Abstract right.

Method. Behavioural psychophysics (method of constants), not AEP/ABR. Threshold verbatim: "the stimulus level generating a HIT rate of the psychometric function half-way between the FA rate and 100%". The record's method field is right.

Verified, verbatim: "The experimental bird was a male 6-year-old wild-caught great cormorant"; "housed in Kerteminde, Denmark, at the Marine Biological Research Center"; "Each session took place inside a 2.5×1×1 m acoustic chamber connected to the animal's outdoor enclosure."; "Out of the fifty sessions performed, five were not included in the data analysis" (criterion false alarms above 35%, tool summary); Results "for each of the six frequencies" against the Abstract's "five different frequencies" (the paper does not resolve it; only 2, 4 and 6 kHz are named in the text returned, the rest are in Table 1, an image); noise levels "were 27-76 dB below the hearing threshold at each frequency"; "the threshold-to-noise ratio was always larger than the critical ratio," | "except for at 2 kHz where they were comparable (Table 1)."; "At 2 kHz there is a slight risk that the hearing threshold would be masked by ambient noise in some trials." Bird caught as a juvenile at about five months, kept in an outdoor aviary (tool summary). Wild-caught status, sex, single animal and five-versus-six disclosure all right in the record.

Fault (counted): the masking caveat is reported one-sided. The record stops at the authors' "slight risk" sentence and omits the test they ran on it and its null result, which bears directly on the logged 2 kHz value. Verbatim: "This possible issue with the data was investigated further by deriving hearing thresholds for each session" | "(by the same probit analysis used for the cumulative data set) and comparing them with the individual" | "third-octave band noise centred at 2 kHz, measured right before or after each session." | "A linear regression performed on these thresholds (varying with 18 dB between the sessions)" | "as a function of the background noise levels (varying with 10 dB between the sessions)" | "did not have a slope significantly different from 0 (ANOVA, F1,6=1.2, P=0.4)." Discussion: "This may explain why there were no signs of masking at 2 kHz," ... "All in all, we can safely conclude that there is no risk of the background noise" | "having masked any of the hearing thresholds presented in this study." Two things are missing: the null regression with the authors' conclusion, and the 18 dB between-session spread of the per-session 2 kHz thresholds. The second is a design fact about how stable the logged value is.

Uncounted: the value could say "in air" (the eye field and reference already carry it).

**Line 1 error (null masking test and the authors' no-masking conclusion omitted; 18 dB per-session spread at 2 kHz not carried).** Fixable.

## Verdict

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Phalacrocorax carbo, 18 dB re 20 µPa rms at 2 kHz (in air) | error, fixable | conditions | quote MATCH (13), licence passes, bibliography, names, units and wild-caught status right; masking regression null (F1,6 = 1.2, P = 0.4), Discussion's no-masking conclusion and the 18 dB between-session spread omitted |

Errors 1 of 1 audited record (100%), above the 5% bar; none held out. By kind: omitted null result 1; quote 0; bibliographic 0; licence 0; names 0; duplicates 0 against main, all 166 desk-d2* and audit-3* branches and the hold-outs; units/grading 0.

Unchecked: Table 1 (an image; the other frequencies and their thresholds, and which frequency is the sixth); the speaker calibration and sound-level measurement procedure (not in the text returned); the "used sessions 20-31% false alarms" figure; the number of trials per session; the 35% exclusion criterion and the five-months capture age (tool summary only); IOC listing (not surfaced); PubMed's author string (reCAPTCHA).

## Replacement text

The old string occurs exactly once in its field (checked with `str.count` on the desk file).

Line 1, counted:
- `conditions`: "where the authors state there is a slight risk the threshold was masked by ambient noise in some trials;" -> "where the authors state there is a slight risk the threshold was masked by ambient noise in some trials; they tested this by deriving per-session 2 kHz thresholds (which varied by 18 dB between sessions) and regressing them on the third-octave noise at 2 kHz measured right before or after each session (noise varied by 10 dB): the slope did not differ significantly from 0 (ANOVA, F1,6 = 1.2, P = 0.4), and the Discussion concludes there is no risk that background noise masked any of the thresholds;"

Line 1, uncounted:
- `value`: "lowest threshold 18 dB" -> "lowest in-air threshold 18 dB"
- `note`: "Authors given as printed by the fetched citation" -> "Authors in printed order, initials rendered from the page byline (Crossref files the families as Torres Ortiz and Næsbye Larsen); licence accepted by audit 368 (page CC BY 3.0 sentence on the publisher's own free full text; Crossref am tag is the same CC BY 3.0, not conflicting)"
