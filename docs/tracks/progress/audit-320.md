# audit-320: desk-d228, evidence lines 6 to 9

Audited 31 October 2026 from the desk-d228 files present untracked in the worktree (docs/tracks/progress/desk-d228.md and docs/views/evidence/desk-d228.jsonl, 9 lines; neither committed here, neither edited). HEAD and origin/main f250eade (desk-d227). Audit 319 judges lines 1 to 5. `python3 -I tools/senses/check.py | grep d228`: "docs/views/evidence/desk-d228.jsonl: 9 records, 0 problems". Quote lengths (`len(q.split())`) for lines 6, 7 and 9: 16, 26 and 24, all within 40. Evidence records only, so the brief's search-record parts do not apply; audits 316 to 318 are the format model.

Sources opened (WebFetch): journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0191576 (two passes; one earlier attempt rate-limited); journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0185353 (two passes); www.mdpi.com/2075-4450/16/2/170 (three passes); api.crossref.org/v1/works for 10.1371/journal.pone.0191576 (second attempt; first rate-limited), 10.1371/journal.pone.0185353 and 10.3390/insects16020170; obis.org/taxon/140656 for the oyster name; en.wikipedia.org/wiki/Aquatica_ficta for the firefly name. www.biolib.cz/en/taxon/id1534580 returned a traffic check page and was not retried. No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns verbatim pieces of at most about 100 to 125 characters; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification. 2 WebSearches and 13 WebFetch calls used.

## Line 8, Tomicus yunnanensis: HOLD OUT, repeats main (desk-d227)

Not audited beyond the duplicate check, as the launch prompt directs. `git grep` on origin/main: docs/views/evidence/desk-d227.jsonl:4 holds Tomicus yunnanensis, behaviour_vision, DOI 10.3390/biology14081032 (also audit-317.md lines 5, 48 and 75). Same species, trait and DOI. HOLD OUT: repeats main (desk-d227). Excluded from the error count.

## Bibliographic and licence

- Line 6, Owens et al. 2018. Page byline: "Avalon Celeste Stevahn Owens, Victor Benno Meyer-Rochow, En-Cheng Yang", matching the record and Crossref order. Title verbatim on Crossref: "Short- and mid-wavelength artificial light influences the flash signals of Aquatica ficta fireflies (Coleoptera: Lampyridae)". Page citation "PLoS ONE 13(2): e0191576."; Crossref PLOS ONE 13(2) e0191576, issued 2018-02-07. Page licence: "This is an open access article distributed under the terms of the Creative Commons Attribution License"; Crossref CC BY 4.0 vor, relation empty, no update-to. Met. (Uncounted: the note says the page tool did not return the byline; it does.)
- Line 7, Charifi et al. 2017. Page byline "Mohcine Charifi, Mohamedou Sow, Pierre Ciret, Soumaya Benomar, Jean-Charles Massabuau", as recorded and in Crossref order. Title verbatim "The sense of hearing in the Pacific oyster, Magallana gigas". "PLoS ONE 12(10): e0185353."; Crossref issued 2017-10-25. Page prints the Creative Commons Attribution License sentence; Crossref CC BY 4.0 vor, relation empty, no update-to. Met.
- Line 9, Paryavi et al. 2025. Page byline "Mohsen Paryavi, Keith Weiser, Michael Melzer, Damon Crook, Chandrika Ramadugu, and Daniel M. Jenkins", as recorded and in Crossref order. Title verbatim on Crossref. Page line "Insects 2025, 16(2), 170"; Crossref Insects 16(2) 170, issued 2025-02-06. Page prints MDPI's "open access Creative Common CC BY license" sentence; Crossref CC BY 4.0 vor, delay 0, relation empty, no update-to. Accepted under the vor rule. Met.

Bibliographic faults 0; licence faults 0.

## Names

- Aquatica ficta (Olivier, 1909), Lampyridae (Luciolinae), Coleoptera, synonym Luciola ficta: Wikipedia only (BioLib returned a traffic check). The paper's title prints Lampyridae and Coleoptera. Met, on a secondary source.
- Magallana gigas: OBIS (WoRMS backbone) page for AphiaID 140656 shows Crassostrea gigas (Thunberg, 1793) as a "superseded combination" with "Accepted name: Magallana gigas", class Bivalvia, order Ostreida, family Ostreidae. So the record's name is the accepted one and Ostreidae and Ostreida are confirmed; the paper itself names neither family nor order (tool summary). The note's "from general knowledge" should be replaced (below; uncounted).
- Oryctes rhinoceros: the Abstract prints "coconut rhinoceros beetle (CRB; Oryctes rhinoceros Linnaeus)". Scarabaeidae, Coleoptera as on main's gaps for the genus (O. nasicornis cells). Met. The note says the name is given "in the Methods"; it is also in the Abstract (uncounted).

Names faults 0.

## Duplicates

git grep on origin/main (f250eade) across the whole docs tree (evidence, audit/corrected, audit/ALL, searched, sheets, gaps, batches, codex-findings, progress notes) for "Aquatica", "ficta", "pone.0191576", "0191576", "Owens", "Magallana", "Crassostrea", "gigas", "Ostreid", "pone.0185353", "0185353", "Charifi", "Pacific oyster", "Oryctes", "Oryctes rhinoceros", "rhinoceros beetle", "insects16020170", "16020170", "Paryavi", "firefl", "Lampyridae". Hits: "ficta" only in searched/sweep-53.jsonl:34 (Lampyris genus search); Magallana gigas only in gaps/try-species.json:1496; Crassostrea only C. virginica (desk-d179 evidence and audits 262, 264); "0185353" only in desk-d224.md:13 as a held lead never opened; Oryctes only O. nasicornis gaps cells and genus search records. None of lines 6, 7 or 9 repeats main. Duplicate faults 0.

## Per-record findings

### Line 6, Aquatica ficta, brighter and slower flashes at 533 nm and below

Abstract, verbatim in two pieces: "When exposed to wavelengths at or below 533 nm, males emitted brighter signals" "with decreased frequency." MATCH, 16 words, whole sentence. Methods confirmed verbatim: "Three male A. ficta fireflies were collected three times from Yongjian Eco Park" on "May 4, May 7, and May 11, 2016."; "Eight sets of data were collected from eight A. ficta males"; "one male died before it could be tested."; "two recordings (May 5 and May 13) were disregarded due to measurement inconsistencies"; "exposed to each of the eight pucks in a randomized order determined by a random sequence generator."; "the order of exposure (i.e. dim or bright first) was secondarily randomized within wavelengths."; "After a 5 min adaptation period"; flux "0.107 ± 0.02 μmol m-2 s-1" and "1.075 ± 0.212 μmol m-2 s-1"; GLMM with "both specimen and exposure order" as random effects. Results: dim-light intensity "444 nm: p = 0.0021; 463 nm: p = 0.01; 488 nm: p = 0.017; 515 nm: p = 0.021; 533 nm: p = 0.066"; bright intensity "p = 0.23 ... 533 nm: p = 0.051"; "three of six males ceased signaling entirely"; long wavelengths "p ≥ 0.3 in all instances". Only males tested. The record's handling of the 533 nm intensity p = 0.066 is right.

**Error (flash-frequency statistics misstated; restraint-induced signal type omitted; value adds "alarm").** (a) The record gives frequency as "p = 0.0042 to 0.049 at dim light, p = 0.0019 to 0.032 at bright". The page prints dim "444 nm: p = 0.0042, 463 nm: p = 0.049, 488 nm: p = p < 0.0001," "515 nm: p = 0.0098; 533 nm: p = 0.046" and bright "444 nm: p = 0.0019; 463 nm: p < 0.0001, 488 nm: p < 0.0001, 515 nm: p = 0.0018, 533 nm: p = 0.032". The strongest results (p < 0.0001 at 488 nm dim and at 463 and 488 nm bright) fall outside the stated ranges, so the ranges are wrong. (b) The signals were restraint-induced alarm flashes: "The act of restraint induced a series of fast" (alarm flashes, Signal morphology section; rest of sentence tool summary), against courtship flashes seen in the field at collection. The record says "alarm flashes" but not that restraint produced them, which bounds what the light effect says about free-flying signalling. (c) The value says "alarm flashes"; the quote says "signals". The word is in another Abstract sentence ("recorded their alarm flash signals"), not in the quote, so the value says more than the quote. Also added below: the previous-exposure statistics ("1×: p < 0.0001, χ2 = 15.205; 10×: p = 0.0012, χ2 = 14.668") and the collection count (nine collected, three per date; uncounted wording). Fixable.

### Line 7, Magallana gigas, minimum acoustic energy 0.02 m s-2 at 122 dB rms, 10 to 80 Hz

Abstract, verbatim in two pieces: "The minimum acoustic energy required to elicit a response was 0.02 m∙s-2 at 122 dBrms re 1 μPa" "for frequencies ranging from 10 to 80 Hz." MATCH, 26 words, whole sentence. Methods confirmed verbatim: "purchased from local oyster farmers in the Bay of Arcachon, France"; "18-month-old Pacific oysters, M. gigas (diploid),"; "(≈ 70–75 mm)"; "acclimatized to the experimental set up" "for at least 10 days"; "Two different groups of 16 oysters were studied in April-May 2015 (group A, n = 16)" "and September 2015 (group B, n = 16)."; "Each track of 180 sec pure tone included a 70 sec fade-in"; response if "its amplitude was at least –10%"; acceleration derived from SPL by curves, not measured per oyster; "No test was taken into account from 700–1000 Hz and 8–10 kHz"; sweep "from 1 to 20 kHz" "148 dBrms re 1 μPa" no reaction; "As a partial valve closure cannot be differentiated from a nociceptive response," "it is very likely that oysters detect sounds at lower acoustic energy."; "Similar responses were never observed when the sound was turn-off."; "with 60–95% of animals responding"; logistic model "significant for frequencies ranging from 10 to 400 Hz" "but not significant for 500 or 600 Hz". Group A's sequence "90, 100, 200, 300, 400, 500, 600, 700 and 800 Hz" against the 700 to 1000 Hz exclusion: the record's flag is right.

Hearing versus sound-exposure behaviour: the measure is a behavioural threshold (valve-opening decrease) to controlled pure tones with acceleration estimated, and the authors frame it as hearing, offering statocysts as "good candidates to detect particle motion" without testing that. sense_hearing fits as main files it for Crassostrea virginica gape (desk-d179); the record already states the nociception caveat and the derived acceleration. Trait key met.

**Error (frequency presentation order and interval omitted; order-independence inconsistency omitted).** Group A heard the tones in the ascending sequence listed above, one test "every 30 min" (tool summary for the join), so frequency is confounded with sequence position and time in the set-up; nothing says the order was randomised. The paper claims "the responses were independent of the order of sound frequency presentation" with "p < 0.05" (tool summary), which does not support independence. The record gives neither the fixed order nor the interval, a control-order design confound under the desk rules. Uncounted: the record's "the threshold is the energy evoking a response in 30% of a group" was not confirmed as printed; the page returned "The acoustic energy levels required to induce a valve reaction in 30 to 100% of individuals" and logistic-regression fitting (see Unchecked). Uncounted: the value says "elicited valve closure" where the quote says "elicit a response"; the defined response is a valve-opening decrease of at least 10%, so the quote's wording is safer. Fixable.

### Line 9, Oryctes rhinoceros, avoided traps with visible LEDs in panels

Abstract sentence 5, verbatim in two pieces: "However, CRB avoided traps with any “visible” wavelength LEDs placed in panels of traps," "while ACP was moderately attracted to blue, yellow, and amber." MATCH, 24 words. The page returned the Abstract as seven sentences, this one whole, with the curly quotation marks around "visible" and the comma before "while" as the record has them; no reassembly from separate sentences. Methods and Results confirmed verbatim: "we tested 16 different treatments"; one array of each colour "into the panels of individual traps" "and the second array of each programmed color on the side of the trap cup of separate traps"; "For the control, we used two unlit panel traps."; rotated weekly "through 16 different trap locations"; "16 weeks"; "pheromone lure (P-O46 Oryctalure, ChemTica SA, Heredia, Costa Rica) changed monthly"; "nominally set to output 84 mA when on" at "100% duty cycle"; "roughly 100 m diameter circle near the West side of the Pearl City Peninsula"; "no ambient street lighting"; lighting p = 1.08 × 10−5, position p = 0.551, week p = 0.0445; UV "more than twice the catch rate observed in unlit traps"; "significant suppression of CRB catches when the trap panels were illuminated with any color other than UV"; "no CRBs were caught at all if the panels were illuminated with amber or red"; "there was a significantly increased catch if the cup was illuminated with amber LED". No total catch printed (Figure 4's n = 11,716 is island-wide geolocated catches, not this trial; tool summary). The value's "any visible-wavelength LEDs" drops the quote's quotation marks only; it says no more.

**Error (unsupported yellow-panel claim; per-treatment test omitted).** (a) The record says "none with yellow panels". The Results name only amber and red as catching nothing; yellow appears for CRB only in the Methods colour list (tool summary of all yellow mentions). The zero for yellow is not in the text and may have been read from Figure 6, which the tool did not render. (b) Omitted: each treatment was judged against the unlit control by "the binomial probabilities of catching at least as many CRBs for the treatment", and no per-treatment p values are printed, so "significant suppression" for blue, green and yellow panels rests on an unreported binomial test. Fixable.

## Trait key and grading

- Line 6, behaviour_vision: fits (flash behaviour under monochromatic light; rulings treat lamp-spectrum comparisons as behaviour).
- Line 7, sense_hearing: fits (behavioural response threshold to waterborne tones; see above).
- Line 9, behaviour_vision: fits (trap choice under coloured LEDs).

Trait key faults 0. Grading `m` right for all three (one named species measured in each paper).

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 6 | Aquatica ficta, brighter and slower flashes at 533 nm and below | error, fixable | value, method, conditions | Quote MATCH (16 words); frequency p ranges omit the p < 0.0001 results; restraint-induced alarm signals not stated; "alarm" in value not in quote |
| 7 | Magallana gigas, 0.02 m s-2 at 122 dB rms, 10 to 80 Hz | error, fixable | method, conditions | Quote MATCH (26 words); fixed ascending frequency order, 30 min interval and the p < 0.05 "independent of order" claim omitted; name and family/order confirmed on OBIS (WoRMS) |
| 8 | Tomicus yunnanensis, phototaxis by sex | HOLD OUT | n/a | Repeats main (desk-d227 line 4, same DOI and trait) |
| 9 | Oryctes rhinoceros, avoided visible-LED panel traps | error, fixable | conditions | Quote MATCH (24 words, whole as printed); "none with yellow panels" not in the text; binomial per-treatment test with no printed p values omitted |

Count (line 8 excluded): 3 of 3 records in error (100%): scientific-context 3 (line 6 also misstated statistics and a value beyond the quote; line 9 also an unsupported factual claim); quote form 0; duplicates 0; bibliographic 0; names 0; licence 0; trait key 0; grading 0. HOLD OUT: line 8 (repeats main).

Pooled with audits 172 to 318: 382 of 790 evidence records (48.4%), taking audit 316's 370 of 778, adding audit 317's 5 of 5 and audit 318's 4 of 4 (379 of 787), and 3 of 3 here. Audit 319's lines 1 to 5 are not included.

## Unchecked

- Line 7: the exact percentage criterion behind the 0.02 m s-2 threshold (the record's "30% of a group"); the page returned "30 to 100% of individuals" with logistic fitting. The 30 min interval and the p < 0.05 order sentence came as tool summaries around verbatim fragments.
- Line 9: Figure 6 per-treatment totals (image; not rendered), so the blue, green and yellow panel catches are unread; the CC BY 3.0 page metadata the note cites was not seen by me (licence rests on the page's CC BY sentence plus Crossref vor).
- Line 6: Aquatica ficta status checked on Wikipedia only.
- Line 8: not audited beyond the duplicate check.

## Replacement text

Line 6:
- `value`: "males exposed to wavelengths at or below 533 nm emitted brighter alarm flashes at a lower flash frequency" -> "males exposed to wavelengths at or below 533 nm emitted brighter signals with decreased frequency".
- `method`: "wild-caught males recorded for their alarm flashes during 1 min exposures" -> "wild-caught males, restrained so that restraint induced alarm flash signals (courtship flashes were what they emitted in the field), recorded during 1 min exposures".
- `conditions`: "flash frequency fell at every wavelength from 444 to 533 nm (p = 0.0042 to 0.049 at dim light, p = 0.0019 to 0.032 at bright)" -> "flash frequency fell at every wavelength from 444 to 533 nm (dim: 444 nm p = 0.0042, 463 nm p = 0.049, 488 nm p < 0.0001, 515 nm p = 0.0098, 533 nm p = 0.046; bright: 444 nm p = 0.0019, 463 and 488 nm p < 0.0001, 515 nm p = 0.0018, 533 nm p = 0.032)".
- `conditions`: "earlier exposures lowered flash frequency but not intensity" -> "the number of previous exposures lowered flash frequency (1x: p < 0.0001, chi2 = 15.205; 10x: p = 0.0012, chi2 = 14.668) but not intensity; only males were tested".
- `conditions` (uncounted wording): "eight males tested, one died before testing" -> "nine males collected (three on each date), one died before testing, eight tested on 5 to 9 and 12 to 14 May 2016".
- `note` (uncounted): "Authors in Crossref order (the page tool did not return the printed author line); title, volume and issue from Crossref." -> "Authors as printed on the page byline and in Crossref order; title, volume and issue confirmed on Crossref."

Line 7:
- `method`: "waterborne pure-tone exposures (3 min, 70 s fade-in)" -> "waterborne pure-tone exposures (180 s, 70 s fade-in), one test every 30 min, group A in the fixed ascending order 90, 100, 200, 300, 400, 500, 600, 700, 800 Hz (no randomisation reported)".
- `conditions`: "no separate sham group, responses did not occur with the sound off;" -> "no separate sham group, responses did not occur with the sound off; because frequencies were presented in ascending order, frequency is confounded with sequence position and time, and the paper's statement that responses were independent of presentation order is printed with p < 0.05, which does not support independence;".
- `conditions`: "the threshold is the energy evoking a response in 30% of a group;" -> "thresholds were estimated by logistic regression of the percentage of each group responding, the paper speaking of 'acoustic energy levels required to induce a valve reaction in 30 to 100% of individuals';" (the 30% criterion for the Abstract figure is unconfirmed; keep the paper's wording until it is).
- `value` (uncounted): "minimum acoustic energy that elicited valve closure was 0.02 m s-2 at 122 dB rms re 1 uPa for frequencies from 10 to 80 Hz" -> "minimum acoustic energy required to elicit a response was 0.02 m s-2 at 122 dB rms re 1 uPa for frequencies from 10 to 80 Hz".
- `note` (uncounted): "I could not open WoRMS or GBIF to confirm acceptance, so the family Ostreidae and order Ostreida are from general knowledge." -> "OBIS (WoRMS backbone, obis.org/taxon/140656) lists Crassostrea gigas (Thunberg, 1793) as a superseded combination with accepted name Magallana gigas, family Ostreidae, order Ostreida, class Bivalvia (audit 320)."

Line 8: HOLD OUT, repeats main (desk-d227). Do not file.

Line 9:
- `conditions`: "no beetles were caught at all with amber or red panels and none with yellow panels, I did not read the blue and green panel catches," -> "no beetles were caught at all with amber or red panels; the text gives no separate catch for yellow, blue or green panels (per-treatment totals only in Figure 6, not read); each treatment was compared with the unlit control by binomial probabilities of catching at least as many beetles, and no per-treatment p values are printed,".
- `note` (uncounted): "Abstract abbreviation CRB is the coconut rhinoceros beetle, Oryctes rhinoceros, named in the Methods." -> "Abstract abbreviation CRB is the coconut rhinoceros beetle, named in the Abstract as 'coconut rhinoceros beetle (CRB; Oryctes rhinoceros Linnaeus)'."

Verdict: 3 of 3 audited records in error (100%), above the 5% bar. Lines 6, 7 and 9 fixable with the replacement text above; line 8 HOLD OUT (repeats main). Pooled 382 of 790 (48.4%) before audit 319.
