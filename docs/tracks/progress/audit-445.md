# audit-445: desk-d331, evidence lines 1 and 2

Audited 1 November 2026 from the desk-d331 files present untracked in the worktree (docs/views/evidence/desk-d331.jsonl, 2 lines; docs/tracks/progress/desk-d331.md); neither committed here, neither edited. HEAD c4665c016 (desk d330 merge). `tools/senses/check.py --require-evidence-kind` on the file: 2 records, 0 problems. Quote lengths 34 and 28 words.

Sources opened (WebFetch): api.crossref.org/works?filter=doi: for both DOIs; journals.plos.org article page for e0123453 (two passes, after one Crossref rate limit); www.frontiersin.org .../fmars.2020.00078/text (returned only the abstract) and .../xml/nlm (three passes); nzor.org.nz name page and sealifebase.ca species summary for Teuthowenia pellucida; fishbase.net.br species summary for Photoblepharon steinitzi. No PMC, mirror, repository copy, proxy, ResearchGate or academia.edu page opened. WebFetch returns pieces of about 125 characters; sentences below marked whole were returned whole or as adjoining pieces with the tool confirming the ending. 4 WebSearch, 9 WebFetch.

Duplicates: grep of the whole docs/ tree for "Teuthowenia", "0123453", "Photoblepharon", "fmars.2020.00078", "Hellinger". Teuthowenia appears only in a harvest-53 screened note (a thesis, W1598604998, no row); Photoblepharon and the Frontiers DOI only in audit-307's grep list. Main's Hellinger rows are Anomalops katoptron (Hellinger et al. 2017, pone.0170489; Mark et al. 2018, pone.0198765), a different species and papers. Duplicates 0.

## Line 1, Teuthowenia pellucida, eye_diameter_mm [0.5, 33]

Bibliographic: Crossref gives Aaron B. Evans, Monica L. Acosta, Kathrin S. Bolstad in that order; title verbatim as recorded; PLOS ONE 10(5) e0123453, issued 2015-05-13; licence CC BY 4.0, vor; no update-to or relation. The page citation line prints "Evans AB, Acosta ML, Bolstad KS (2015) Retinal Development and Ommin Pigment in the Cranchiid Squid" / "Teuthowenia pellucida (Cephalopoda: Oegopsida). PLoS ONE 10(5): e0123453." and the licence sentence "This is an open access article distributed under the terms of the Creative Commons Attribution License,". Authors, year, title, journal, DOI, access "open" and licence all met.

Quote: Results, "Relative eye size throughout ontogeny", pieces "Ontogenetic changes in eye-to-body-size ratio were investigated by measuring the eye diameter" + "along the dorsal—ventral midline (0.5–33 mm) and mantle length (ML 1.5–165 mm) for specimens with intact eyes" and, on a second pass, the ending "(Fig 1A)." confirmed. MATCH, whole sentence, value in it.

Value format: check.py accepts a two-number list, and main already holds list values for eye_diameter_mm ranges (audit 383 counted three such and accepted [0, 1.6]). The key eye_diameter_mm is an existing main key passed through the "new trait" note. The value is the range of the measured specimens, not a species-wide or adult value, and the conditions say so. Accepted. Context verified verbatim: "A total of 87 specimens of T. pellucida captured at known depths (ranging in size from 1.5 to 210 mm dorsal mantle length—ML)"; "Thirty of the specimens were adults, with 23 reproductively mature or mated."; "Of these specimens, 61 possessed intact enough eyes to permit measurement,"; "light conditions during capture (i.e., day/night) were not" available; R2 = 0.929, n = 33 below ML 50 mm, n = 28 above; Discussion "about 1:5". Specimens loaned from NIWA and NMNZ Te Papa (verbatim). No sentence on shrinkage.

**Error (fixable): preservation overstated.** The method says eye diameters were measured "on formalin-fixed, ethanol-stored museum specimens" and the conditions say the specimens were "fixed in buffered formalin and stored in ethanol". The page states this only for the histology subset: "Whole eyes were removed from seven preserved specimens of Teuthowenia pellucida," / "which had been fixed in 5% buffered formalin and stored in 70–80% ethanol until processed." For the 61 measured specimens the paper gives no fixative. The conditions' "Range over the whole size series" also overstates: the range covers the 61 specimens with intact eyes (ML to 165 mm) of an 87-specimen series running to 210 mm ML.

Name: NZOR prints "Teuthowenia pellucida (Chun, 1910)" as its "Preferred Name" (Cranchiidae, Cephalopoda; no synonym listed); SeaLifeBase prints "Teuthowenia pellucida" "(Chun, 1910)" with "Cephalopoda | Oegopsida | Cranchiidae | Taoniinae" and a narrow circumglobal band near 40° S. The record's authority (Chun, 1910) is right; the brief's "(Ball, 1840?)" is not supported by any page read. Teuthowenia megalops is a separate species (neither page lists it as a synonym), and the New Zealand specimens are filed under the name both checklists treat as preferred. Names 0 faults; the note's "acceptance rests on the OBIS listing" can be upgraded (replacement below). The record carries no class/order/family fields; the title prints Cephalopoda: Oegopsida and the paper names it a cranchiid, so adding them would be optional.

Grade m right (one named species, measured). Line 1: 1 error, fixable.

## Line 2, Photoblepharon steinitzi, behaviour_vision (behavioural_response)

Bibliographic: Crossref gives Jens Hellinger, Peter Jägers, Katharina Spoida, Linda C. Weiss, Melanie D. Mark, Stefan Herlitze in that order; title verbatim as recorded; Frontiers in Marine Science 7, article 78, no issue, issued 2020-02-19; CC BY 4.0, vor; no update-to or relation. The XML page prints "This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY)." Met.

Quote: Results 3.1, pieces "In the presence of the light organ dummy (glow stick) P. steinitzi spend significantly more time" + "30.22% ± 1.8 SEM in the center of the cave", and the last 60 characters returned exactly as "time 30.22% ± 1.8 SEM in the center of the cave (Figure 2D)." MATCH, whole sentence. The preceding sentence gives 98.32% ± 0.77 SEM in the periphery for undisturbed fish; the following gives the fish dummy as "89.47% ± 1.39.2 SEM in the periphery" (the typo is on the page). LED: "95.28% ± 0.14 SEM in the periphery".

Trait and kind: behaviour_vision with behavioural_response stands. This is an experimental manipulation of a light stimulus in the field, not a correlate, and the three luminous dummies (blinking 500 nm LED, constant 519 nm glow stick, lit fish-shaped dummy) drew different time budgets and attack types, which a fish can tell apart at night only by sight. It is a different species and paper from main's Anomalops katoptron behaviour_vision rows (Mark et al. 2018; Hellinger et al. 2017), so no repeat.

**Error (fixable): value exceeds the quote, and a design confound is omitted.**
- The value's second clause ("preliminary small green, blue and red constant lights all drew approaching reactions") comes from a Methods sentence, not the quote. It must be cut from the value. The Methods sentence itself is verified whole: "Preliminary observations with constant glowing small green, blue and red light sources showed approaching reactions of P. steinitzi to all three lights." It can stay in conditions as context.
- "519 nm" is not in the quote (it is in the method), so it comes out of the value.
- The conditions claim the finding "shows the fish reacts to a light source of this wavelength". The paper describes no unlit or non-luminous dummy, and the significant comparison in Figure 2D is across blank, fish dummy, blinking LED and glow stick. Extra time in the centre therefore cannot be assigned to the light rather than to an object placed there. "Every stimulus was recorded in fixed sample time intervals for 5 min in sequential sessions": stimulus order and randomisation are not stated, and the conditions omit this.

Methods details the record marked as "tool summary", now verified verbatim: N = 11 fish dummy, 6 blinking LED, 8 glow stick; site "fringing reef in the Gulf of Aqaba (Red Sea)", "the coast of Dahab"; centre "approximately 1 m", periphery "approximately 2 m"; "The dummies were positioned prior to the experiments in the center region of reef caves."; sex by size "approximately 4–7 cm for potential males and 7–10 cm for potential females"; glow stick 4.5 mm × 37 mm, 519 nm, lit surface taped to 10 mm; LED 500 nm, 1 Hz; fish dummy 100 mm with 10 mm light organs; one-way ANOVA with Holm-Sidak; darting most for the LED "16.15 ± 1.57 reactions"; ramming/biting for the glow stick "14.69 ± 3.66 attacks per trial", fish dummy "0.296 ± 0.16", LED "in one case"; "Therefore, we assume no wavelength dependent effects in behavior by using a 500 nm LED and a 519 nm glow stick." Nothing needs removing; the labels change to verbatim.

Name: FishBase prints "Photoblepharon steinitzi Abe & Haneda, 1973", "Teleostei (teleosts) > Trachichthyiformes (Roughies) > Anomalopidae (Lanterneye fishes)" with no synonym shown. The paper prints "flashlight fish (Anomalopidae)" and no order for the fish ("Beryciformes" appears only in reference titles). Family right. Uncounted: main's three Anomalops katoptron rows carry order Beryciformes (GBIF, audit 307), so this row's Trachichthyiformes (FishBase) differs from main's family-mates (see optional fix).

Grade m right. Line 2: 1 error, fixable.

## Summary

Errors 2 of 2 records (100%), both fixable; none unfixable, none held out. By kind: value exceeding quote 1 (line 2); omitted design confound / overstated method 2 (lines 1, 2); bibliographic 0; licence 0; names 0; duplicates 0; trait keys 0; quotes 0. Verdict: merge both lines after the replacements below. Tested: the replacements below, applied to a scratch copy, give 2 records and 0 problems under check.py --require-evidence-kind, each old string occurring exactly once in its line.

## Replacement

Strings are as decoded text; in the raw JSON line they appear identically (the file stores UTF-8 unescaped and contains no escaped quotes in these spans).

### Line 1

- `method`: "on formalin-fixed, ethanol-stored museum specimens" -> "on preserved museum specimens (the paper states fixation in 5% buffered formalin and storage in 70–80% ethanol only for the seven specimens taken for histology)"

- `conditions`: "Range over the whole size series, not an adult value: the sentence gives" -> "Range over the specimens with intact eyes, not an adult value and not a species maximum: the sentence gives"

- `conditions`: "fixed in buffered formalin and stored in ethanol; the text read does not say whether shrinkage was corrected." -> "preservation is stated only for the seven histology specimens (5% buffered formalin, then 70–80% ethanol), and the paper does not mention shrinkage or any correction for it."

- `conditions`: "Per the page summary (tool summary, not verbatim): 87 specimens of 1.5 to 210 mm ML, 30 adults," -> "Verbatim on the page (audit 445): 87 specimens of 1.5 to 210 mm ML, 30 adults (23 reproductively mature or mated),"

- `note`: ", but the page states no accepted/valid status and WoRMS/MolluscaBase could not be opened, so acceptance rests on the OBIS listing and the 2015 paper using it." -> " with no status stated; NZOR prints Teuthowenia pellucida (Chun, 1910) as its Preferred Name (Cranchiidae, no synonym listed) and SeaLifeBase prints the same name and authority (Cephalopoda | Oegopsida | Cranchiidae); WoRMS/MolluscaBase could not be opened (audit 445)."

### Line 2

- `note`: "The second clause of the value comes from a Methods sentence, Behavioral Experiments: 'Preliminary observations with constant glowing small green, blue and red light sources showed approaching reactions of P.' + 'P. steinitzi to all three lights.' (tool pieces repeated 'P.' at the join, so the exact join is uncertain; it is not in the quote field)." -> "The Methods sentence on preliminary green, blue and red lights is not in the value, since it has no quote of its own; audit 445 read it whole: 'Preliminary observations with constant glowing small green, blue and red light sources showed approaching reactions of P. steinitzi to all three lights.'"

- `value`: "with a 519 nm glow-stick light-organ dummy present, spent 30.22 +/- 1.8% (SEM) of time in the cave centre (the dummy zone); preliminary small green, blue and red constant lights all drew approaching reactions" -> "with the light-organ dummy (glow stick) present, spent significantly more time, 30.22 +/- 1.8% (SEM), in the centre of the cave"

- `conditions`: "Territorial aggression is the response measured, so the finding shows the fish reacts to a light source of this wavelength, not that it discriminates colour: the authors assumed no wavelength-specific effect because green, blue and red lights all drew approach." -> "Territorial aggression is the response measured. Figure 2D compares blank (no dummy), fish-dummy, blinking-LED and glow-stick recordings (one-way ANOVA with Holm-Sidak post hoc); the paper describes no unlit or non-luminous dummy, so the extra time in the centre is not assigned to the light rather than to an object placed there, although the differing responses to the three luminous dummies show the fish distinguishes them. Every stimulus was recorded for 5 min in sequential sessions; stimulus order and randomisation are not stated. Colour discrimination was not tested: the authors write 'Therefore, we assume no wavelength dependent effects in behavior by using a 500 nm LED and a 519 nm glow stick.' after preliminary observations that small constant green, blue and red lights all drew approach (Methods; not a quoted value)."

- `conditions`: "(11 with the fish dummy, 6 with the LED; per page summary, tool summary, not verbatim)" -> "(11 with the fish dummy, 6 with the LED; verbatim, audit 445)"

- `conditions`: "Per page summary (not verbatim): undisturbed fish spent 98.32% of time in the periphery" -> "Verbatim on the page (audit 445): undisturbed fish spent 98.32% +/- 0.77 SEM of time in the periphery"

- `note`: "Contrary: the blinking LED dummy produced darting reactions (16.15 +/- 1.57, per page summary) and the glow stick most ramming/biting, so response type varied with dummy." -> "Contrary: darting was most pronounced for the blinking LED (16.15 +/- 1.57 reactions) and ramming/biting for the glow stick (14.69 +/- 3.66 attacks per trial; fish dummy 0.296 +/- 0.16; LED one case), so response type varied with dummy (verbatim, audit 445)."

## Optional fixes (not counted)

- Line 1 `note`: "page prints the Creative Commons Attribution License (tool summary)" -> "page prints \"This is an open access article distributed under the terms of the Creative Commons Attribution License,\" (verbatim, audit 445)".
- Line 1: add "class": "Cephalopoda", "order": "Oegopsida", "family": "Cranchiidae" (title prints Cephalopoda: Oegopsida; SeaLifeBase prints Cranchiidae).
- Line 2 `order`: "Trachichthyiformes" agrees with FishBase but not with main's Anomalopidae rows (Beryciformes). Either drop the field (the paper prints no order for the fish), or keep it and leave the main-wide reconciliation to the owner.
- Line 2 `method`: "(about 1 m across, periphery about 2 m)" -> "(approximately 1 m diameter, periphery approximately 2 m)".
