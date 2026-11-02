# audit-442 (desk-d329, lines 1 to 6)

Auditor: fresh Opus, 1 November 2026. Scope: 1-based lines 1 to 6 of `docs/views/evidence/desk-d329.jsonl` (lines 7 to 11 go to another auditor). Base: main at 14a624e77. 10 WebSearch calls, 15 WebFetch calls. Every page read through the 125-character summary tool; sentences reassembled from consecutive pieces as noted. No PMC, proxy, ResearchGate or academia.edu copy opened. `check.py --require-evidence-kind` on the unit: 0 problems; the corrected lines below also pass (0 problems on a scratch copy).

## Trait key

BRIEF defines `behaviour_vision` as "a behaviour that shows what is seen (distance prey is detected or attacked, colour choice)" and ECOLOGICAL-OUTCOMES.md repeats it; a measured response to light alone is not enough. Main's Puffinus puffinus light-on record (desk-d225:1) is a controlled field experiment (torch with filters, light-on against light-off, colour and intensity differing), which audit 314 accepted as a flight response to light of different colours. The unit's own justification ("diel is plant-only by ruling") misreads the ruling: the ruling limits plant `diel` to flower timing, and animal `diel` rows exist on main (oa-1 Hypolimnas bolina, oa-8 Apis dorsata); `diel` is a category key, though, so it does not fit these lines either.

- Lines 1, 2 and 6 are field correlates of a calculated moon covariate (GPS step length; acoustic pass counts). No stimulus is controlled and nothing shows what is seen. The records' own notes concede it (line 1: "the finding does not show that ocelots see moonlight"). The same unit filed the equivalent skylark moon covariate (line 9) under `ecological_intervention_outcome` with "intervention: none imposed; natural variation". Fault: refile the same way.
- Line 5 (glow-worm females glowing longer under existing streetlights) is a mating-outcome endpoint under existing lighting, observational; its note says it "does not show what the animals see". Fault: refile as ecological outcome.
- Line 3 (flashlight fish with and without working light organs, prey capture under infrared) fits: it is prey detection using the fish's own light, the BRIEF example class.
- Line 4 (owl monkey activity during lunar eclipses) is accepted under `behaviour_vision`, which is close: the eclipse is a natural light-off against light-on comparison within the same night, analogous to the accepted Puffinus light-on design. The value says no more than "activity inhibited", and it does not assert a visual threshold. A reviewer could prefer `sense_light_nonvisual` (masking may not be image-forming vision); I do not count it.

Trait key faults: 4 (lines 1, 2, 5, 6).

## Per line

### Line 1, Leopardus pardalis: fixable

- Page journals.plos.org (id 10.1371%2Fjournal.pone.0286393; the unencoded URL returned an unrelated beluga paper, so it is unreliable). Title verbatim, authors in order "Maksim Sergeyev, Jason V. Lombardi, Michael E. Tewes, Tyler A. Campbell", PLoS ONE 18(11): e0286393, published 30 November 2023, DOI matches. Crossref (single DOI): same authors and order, vol 18 issue 11 e0286393, issued 2023-11-30, licence CC BY 4.0 vor. The page prints "This is an open access article distributed under the terms of the Creative Commons Attribution License, ...". Licence OK.
- Quote verified in two pieces: "Ocelots moved greater distances during new moons compared to full moons (F value = 5.36, p = 0.021; mean step length" / " between 30 min locations = 122.83 m during full moons and 131.57 during new moons; [Fig 3])." The record cuts "; [Fig 3])." and marks it with an ellipsis. 37 words. Value matches the quote.
- 8 ocelots (3 males, 5 females), adults; Lotek Minitrack GPS or Litetrack Iridium-GPS collars, 30 to 60 minute fixes; 4,567 and 4,101 locations; illumination from R 'lunar' (`lunar.illumination`), not measured; "11.26 m shorter step length" per unit illumination: all confirmed. Felidae or Carnivora are not printed; the blanks are correct.
- Fault (omitted qualifier): the conditions say ocelot habitat selection was "similar across phases" but omit the exception printed in the same paragraph: "Ocelots selected larger patches of dense cover during new moons (OR = 1.14, 95% CI = [0.99, 1.31]; α = 0.07) but used larger patches in proportion to availability during full moons". They also omit the night-length covariate (10.32 m longer steps per extra hour of night).
- "The model's handling of repeated fixes was not read": the page says step length used "mixed effect linear regression models" (lmer) without stating an individual random effect; the full/new comparison is an ANOVA. Fixed in the replacement.
- Trait key fault (above). Authors not in Surname Initials form (fault, see Bibliographic).
- Name: accepted (repo gbif-names.tsv; Plazi treatment "Leopardus pardalis (Linnaeus, 1758)" in search results; the MDD page did not surface). Main: species has only Banks et al. 2015 pupil rows (oa-2:2325-2326); DOI and title absent from docs/. No repeat.

### Line 2, Lynx rufus: fixable

- Same page and licence basis as line 1. Quote "Varying illumination did not affect the step length of bobcats." confirmed verbatim, a whole sentence. 13 bobcats (7 males, 6 females); 7,132 and 7,158 locations; "Step length of bobcats did not differ between new moons and full moons (F value = 2.65, p = 0.104; mean step length between 30 min locations = 120.24 m during full moons and 124.08 during new moons)" confirmed. Habitat-selection contrast (OR 0.73 and 1.12 at full moon, proportional use at new moon) confirmed.
- Faults: trait key; author form. Name accepted (MDD taxon page 1006009 in search results; repo gbif-names.tsv). Main: Lynx rufus only in a pooled S-cone row (cat-dog:138) and batch lists; no repeat.

### Line 3, Anomalops katoptron: fixable

- Page journals.plos.org (id 10.1371%2Fjournal.pone.0170489). Title verbatim; authors in order "Jens Hellinger, Peter Jägers, Marcel Donner, Franziska Sutt, Melanie D. Mark, Budiono Senen, Ralph Tollrian, Stefan Herlitze"; citation line "PLoS ONE 12(2): e0170489"; published 8 February 2017. Crossref: same order, 12(2) e0170489, issued 2017-02-08, CC BY 4.0 vor. The page prints the "Creative Commons Attribution License" sentence. The note's "page prints no separate licence sentence in what was returned" is wrong (note fault, uncounted).
- Quote verified in two pieces: "No change in the blink frequency was observed in non-luminescent A. katoptron after shrimp larvae hatching" / "and only approximately 10% of the shrimp were captured when compared to luminescent A. katoptron." It is a whole sentence of 31 words under the subsection "Blinking behavior while hunting living prey". `where` can name it.
- 5 luminescent and 3 non-luminescent fish; commercial wholesaler in the Netherlands, captured at Cebu; no test statistic reported for the capture comparison although the Methods say capture was analysed by repeated-measures ANOVA; trials under 850 nm infrared. All confirmed.
- Fault (design confound omitted): the non-luminescent fish were not experimentally blocked. Their light organs had degenerated (fewer tubules, lost blood vessels), which the authors attribute "most likely" to food deprivation during transport, and they came from an initial pool of 9 luminescent and 14 non-luminescent fish. Fish condition is therefore confounded with light emission. The record's "(non-functional light organs)" hides this.
- Main: the note says only "an ERG row from another paper". Main in fact holds lambda_max_nm 490, erg_peak_nm 480 and a behaviour_vision row ("attracted by low-intensity blue light but not red light") for this species from Mark et al. 2018 (desk-d221:2-4, 10.1371/journal.pone.0198765). These come from a different paper and endpoint, so they are not a repeat, but the note understates them (uncounted, fixed). Name accepted (audit 307 checked the GBIF species page; desk-d221 on main uses it). Family/order blank: correct, not filled.
- Author form fault.

### Line 4, Aotus azarae: fixable

- Page journals.plos.org (id 10.1371%2Fjournal.pone.0012572). Title verbatim; authors "Eduardo Fernández-Duque, Horacio de la Iglesia, Hans G. Erkert"; citation "PLoS ONE 5(9): e12572" (2010). Crossref: same, issued 2010-09-03, CC BY 4.0 with content-version "unspecified". The page prints "This is an open-access article distributed under the terms of the Creative Commons Attribution License, ...". That is an accepted pairing.
- Quote verified (Abstract, two pieces, a whole sentence of 29 words). The page spells the species "A. azarai" with no subspecies. MDD taxon 1000744 lists Aotus azarae (von Humboldt, 1812), Aotidae, Primates, as accepted; the repo's gbif-names.tsv lists azarai as a SYNONYM of azarae. Filing under azarae with the spelling disclosed is correct. Aotidae is not printed; "Primates" appears only as a subject label. The blanks are correct.
- n = 10, 6 to 18 months, sex of all ten not stated: confirmed. 36.6 ± 0.9% of activity in dark hours: confirmed.
- Fault (statistic omitted): the eclipse comparison carries a Friedman test, X² = 32.35, df = 8, p printed "0.000", with activity during the full eclipse lower than during the partial eclipse, the penumbra and the periods before and after. The record gives no statistic and says only that animals per eclipse were "not read". The counts are in the Figure 3 panels, which the tool did not return.
- Minor (corrected, uncounted): the luminance came from a remote photocell on a 2-m post pointed at the zenith in an open savannah area. The record says "a luxmeter".
- The note says "genus appears only for a fovea row", which is wrong. Main has Aotus azarae acuity_cpd 8.3 and eye axial length 19.9 (oa-1:4232-4233) and Aotus azarai acuity_cpd rows (oa-1:4050-4051, canon-5:214). Those are different traits and papers, so this is not a repeat. Main's own rows filed under the synonym azarai are outside this audit and should be flagged to the desk.
- Author form fault.

### Line 5, Lampyris noctiluca: fixable

- Page mdpi.com/2075-4450/12/8/734. Authors "Mira Van den Broeck, Raphaël De Cock, Stefan Van Dongen and Erik Matthysen"; "Insects 2021, 12(8), 734"; DOI 10.3390/insects12080734; the page prints "Creative Commons Attribution (CC BY) license". Crossref: same order, 12(8) 734, issued 2021-08-17, CC BY 4.0 vor. Licence OK.
- Quote verified (Abstract, two pieces, a whole sentence of 35 words). Value matches. 24 dark and 27 lit females, 0.008 to 0.020 and 0.017 to 8.53 lux, low-pressure sodium lighting: confirmed. Lampyridae and Coleoptera are printed; leaving them blank is allowed.
- Fault (false inconsistency): the conditions say "the origin counts in the text (28 found in situ) differ from the sample table summary (4 + 15)". The paper has no table, and the counts reconcile. Methods: "Twenty-eight adult females were found in situ, of which 19 were monitored in the location where they were ... and 9 were relocated to a different ambient light condition, mostly moving them from lit conditions to dark (n = 8) ...". The Results count 4 + 15 in situ plus 8 + 1 translocated, which makes 28.
- Fault (effect size omitted): the survival-analysis sentence reads "time to mating increased significantly with ambient light intensity (p > 0.001; estimate = −0.598 + S.E = 0.125)". The record keeps the p typo but drops the estimate and SE. Placement was "arbitrarily" chosen, not randomised (added).
- Trait key fault. Author form fault. Name accepted (repo gbif-names.tsv). Main: sweep-53:9 acceptance_deg and insect:217 colour_vision come from other papers; the DOI is absent. No repeat.

### Line 6, Molossus molossus: fixable

- Page peerj.com/articles/10591 and its PDF (both in search results). Byline "Dylan G.E. Gomes, Giulliana Appel and Jesse R. Barber"; how-to-cite "Gomes DGE, Appel G, Barber JR. 2020. ... PeerJ 8:e10591 DOI 10.7717/peerj.10591". Crossref: same order, vol 8 e10591, issued 2020-12-18, CC BY 4.0 with content-version "unspecified". The page prints "...distributed under the terms of the Creative Commons Attribution License...". Licence OK. The caller's "e10589 or similar" is wrong: e10591 is correct.
- Quote verified in two pieces (Results, a whole sentence of 24 words). The preceding sentence ("There is an 80.9% probability that moonlight had a positive effect on overall bat activity.") is reflected in the conditions. The percentages are undefined in the paper (confirmed); illumination is "calculated using custom windows command line code"; 12,151 and 3,972 passes; 10 to 19 April 2018, nine nights.
- Fault (site misdescribed): the conditions say the Methods name "Saut Pararé" and the Figure 3 caption names "Nouragues", and call the page inconsistent. The Methods print "Saut Pararé Nourages research station", so both name the Nouragues station, and the difference is the spelling Nourages/Nouragues.
- Trait key fault. Author form fault. Name accepted: MDD taxon 1005202 lists Molossus molossus (Pallas, 1766), Molossidae, Chiroptera, with French Guiana in range; its note says the species "previously included M. tropidorhynchus ... and M. verrilli" (Loureiro et al. 2019). That split does not affect French Guiana. The family and order are printed in the paper; leaving them blank is allowed. Main: no Molossus molossus row, DOI absent. No repeat.

## Bibliographic

All six lines give authors as full given names. The caller's check and the recent merged units (d326 to d328) use Surname Initials. The printed initials are: Sergeyev M, Lombardi JV, Tewes ME, Campbell TA; Hellinger J, Jägers P, Donner M, Sutt F, Mark MD, Senen B, Tollrian R, Herlitze S; Fernández-Duque E, de la Iglesia H, Erkert HG; Van den Broeck M, De Cock R, Van Dongen S, Matthysen E; Gomes DGE, Appel G, Barber JR. These are counted as one format fault per line. Main is mixed (desk-d225 and desk-d221 use full names), so this fault alone would not decide any line. Order, titles, journal, volume, issue, article number, printed years and DOIs are all correct.

## Counts

6 of 6 lines in error, all fixable (100%). Errors by kind: trait key 4 (lines 1, 2, 5, 6); scientific context 4 (line 1 omitted patch-selection exception, line 3 condition confound, line 4 Friedman statistic, line 5 effect estimate); factual error in conditions 2 (line 5 false table inconsistency, line 6 site); author form 6 (lines 1 to 6); quote form 0; licence 0; names 0; duplicates 0; grading 0; value beyond quote 0. Uncounted note faults: line 3 licence sentence and main rows, line 4 main rows and photocell. Lines that would still be in error without the author-form count: 6 of 6. Error lines: 1, 2, 3, 4, 5, 6. Unfixable: none. Held out: none.

## Replacement

Apply to `docs/views/evidence/desk-d329.jsonl`. Every old string is raw JSON text that occurs exactly once in its line. The trait replacements insert the five fields that `ecological_intervention_outcome` requires. With all replacements applied, `check.py --require-evidence-kind` reports 0 problems on lines 1 to 11.

### Line 1

- old (raw JSON text, occurs once in line 1):

    "trait": "behaviour_vision", "evidence_kind": "behavioural_response",

  new:

    "trait": "ecological_intervention_outcome", "evidence_kind": "ecological_outcome", "measured_endpoint": "step length between consecutive GPS fixes of collared ocelots", "experimental_unit": "GPS step (4,567 full-moon and 4,101 new-moon locations from 8 ocelots)", "intervention": "none imposed; natural lunar phase (full moon) and calculated moon illumination", "comparator": "new-moon nights", "mechanism_limit": "movement distance is not detection, avoidance or a visual threshold; illumination is calculated with the R 'lunar' package, not measured, and no light-sensing mechanism is tested",

- old (raw JSON text, occurs once in line 1):

    "authors": "Maksim Sergeyev, Jason V. Lombardi, Michael E. Tewes, Tyler A. Campbell"

  new:

    "authors": "Sergeyev M, Lombardi JV, Tewes ME, Campbell TA"

- old (raw JSON text, occurs once in line 1):

    the same paper also reports that each unit increase in illumination was associated with 11.26 m shorter steps and that ocelot habitat selection was similar across phases (odds ratios for distance to dense cover 0.58 full, 0.56 new);

  new:

    the same paper also reports that each unit increase in illumination was associated with 11.26 m shorter steps, that each extra hour of night was associated with 10.32 m longer steps, and that ocelot habitat selection was highly similar across phases (odds ratios for distance to dense cover 0.58 full, 0.56 new) except that ocelots selected larger dense-cover patches during new moons (OR = 1.14, 95% CI 0.99 to 1.31; alpha = 0.07) and used them in proportion to availability at full moon;

- old (raw JSON text, occurs once in line 1):

    the model's handling of repeated fixes per animal was not read;

  new:

    the full-versus-new comparison is an ANOVA on steps and the page does not say whether individual was a random effect;

- old (raw JSON text, occurs once in line 1):

    Behaviour key used for a light-driven movement response because diel is plant-only by ruling.

  new:

    Filed as an ecological outcome (audit 442): a field correlate of calculated illumination does not show what is seen (BRIEF behaviour_vision), and this unit filed the skylark moon covariate the same way.

### Line 2

- old (raw JSON text, occurs once in line 2):

    "trait": "behaviour_vision", "evidence_kind": "behavioural_response",

  new:

    "trait": "ecological_intervention_outcome", "evidence_kind": "ecological_outcome", "measured_endpoint": "step length between consecutive GPS fixes of collared bobcats", "experimental_unit": "GPS step (7,132 full-moon and 7,158 new-moon locations from 13 bobcats)", "intervention": "none imposed; natural lunar phase and calculated moon illumination", "comparator": "new-moon nights and lower calculated illumination", "mechanism_limit": "a null on movement distance is not sensory absence; illumination is calculated, not measured, and no light-sensing mechanism is tested",

- old (raw JSON text, occurs once in line 2):

    "authors": "Maksim Sergeyev, Jason V. Lombardi, Michael E. Tewes, Tyler A. Campbell"

  new:

    "authors": "Sergeyev M, Lombardi JV, Tewes ME, Campbell TA"

- old (raw JSON text, occurs once in line 2):

    the model's handling of repeated fixes per animal was not read

  new:

    the full-versus-new comparison is an ANOVA on steps and the page does not say whether individual was a random effect

### Line 3

- old (raw JSON text, occurs once in line 3):

    "authors": "Jens Hellinger, Peter Jägers, Marcel Donner, Franziska Sutt, Melanie D. Mark, Budiono Senen, Ralph Tollrian, Stefan Herlitze"

  new:

    "authors": "Hellinger J, Jägers P, Donner M, Sutt F, Mark MD, Senen B, Tollrian R, Herlitze S"

- old (raw JSON text, occurs once in line 3):

    5 luminescent and 3 non-luminescent fish used in the behaviour experiments,

  new:

    5 luminescent and 3 non-luminescent fish used in the behaviour experiments (from an initial 9 luminescent and 14 non-luminescent); the non-luminescent fish were not experimentally blocked: their light organs had degenerated (fewer tubules, lost blood vessels), which the authors attribute most likely to food deprivation during transport, so fish condition is confounded with light emission;

- old (raw JSON text, occurs once in line 3):

    "where": "Results"

  new:

    "where": "Results, 'Blinking behavior while hunting living prey'"

- old (raw JSON text, occurs once in line 3):

    The subsection heading of this sentence was not returned, so 'Results' only.

  new:

    Subsection heading confirmed by audit 442.

- old (raw JSON text, occurs once in line 3):

    page prints no separate licence sentence in what was returned.

  new:

    the page prints 'Creative Commons Attribution License'.

- old (raw JSON text, occurs once in line 3):

    DOI checked absent from main (the species has an ERG row from another paper).

  new:

    DOI checked absent from main; main holds Anomalops katoptron lambda_max_nm, erg_peak_nm and a behaviour_vision row (attracted by low-intensity blue but not red light) from Mark et al. 2018 (10.1371/journal.pone.0198765), a different paper and endpoint.

### Line 4

- old (raw JSON text, occurs once in line 4):

    "authors": "Eduardo Fernández-Duque, Horacio de la Iglesia, Hans G. Erkert"

  new:

    "authors": "Fernández-Duque E, de la Iglesia H, Erkert HG"

- old (raw JSON text, occurs once in line 4):

    luminance came from a luxmeter in an open area next to the study site,

  new:

    luminance came from a remote photocell on a 2-m post pointed at the zenith in an open savannah area next to the study site,

- old (raw JSON text, occurs once in line 4):

    and temperature also masked activity

  new:

    and temperature also masked activity; the eclipse comparison is a Friedman test (X2 = 32.35, df = 8, p printed as 0.000), full eclipse lower than partial eclipse, penumbra and the periods before and after; subjects per eclipse are given only in the Figure 3 panels

- old (raw JSON text, occurs once in line 4):

    DOI checked absent from main (genus appears only for a fovea row).

  new:

    DOI checked absent from main; main holds Aotus azarae acuity_cpd and eye axial length and Aotus azarai acuity_cpd rows (oa-1, canon-5) from other papers and traits.

### Line 5

- old (raw JSON text, occurs once in line 5):

    "trait": "behaviour_vision", "evidence_kind": "behavioural_response",

  new:

    "trait": "ecological_intervention_outcome", "evidence_kind": "ecological_outcome", "measured_endpoint": "number of consecutive nights a female glowed (taken as time to mating)", "experimental_unit": "individual female (51: 24 dark, 27 lit)", "intervention": "existing low-pressure sodium streetlighting (0.017 to 8.53 lux at the female)", "comparator": "dark areas (0.008 to 0.020 lux)", "mechanism_limit": "glow duration is an inferred mating outcome, not a measure of what males or females see; site, light and female origin are not separated",

- old (raw JSON text, occurs once in line 5):

    "authors": "Mira Van den Broeck, Raphaël De Cock, Stefan Van Dongen, Erik Matthysen"

  new:

    "authors": "Van den Broeck M, De Cock R, Van Dongen S, Matthysen E"

- old (raw JSON text, occurs once in line 5):

    and 8 translocated from lit to dark areas all stopped glowing after one night;

  new:

    28 found in situ (19 monitored where found, 9 relocated: 8 lit to dark, 1 between lit conditions) and 23 reared; all 24 dark-area females (4 in situ, 12 reared, 8 translocated) stopped glowing after one night;

- old (raw JSON text, occurs once in line 5):

    the survival analysis of time to mating gives p printed as '> 0.001' (probably a typo for < 0.001), and the origin counts in the text (28 found in situ) differ from the sample table summary (4 + 15)

  new:

    the survival analysis found time to mating increased with ambient light intensity (estimate -0.598, S.E. 0.125, p printed as '> 0.001', probably a typo for < 0.001); females were 'arbitrarily' chosen and released, not randomised

- old (raw JSON text, occurs once in line 5):

    Behaviour key used because the finding is a light-driven reproductive-signal response; it is not a threshold and does not show what the animals see.

  new:

    Filed as an ecological outcome (audit 442): the endpoint is glow duration under existing streetlighting, which does not show what the animals see (BRIEF behaviour_vision).

### Line 6

- old (raw JSON text, occurs once in line 6):

    "trait": "behaviour_vision", "evidence_kind": "behavioural_response",

  new:

    "trait": "ecological_intervention_outcome", "evidence_kind": "ecological_outcome", "measured_endpoint": "printed probability of a positive moonlight effect on M. molossus acoustic activity (bat passes); the paper does not define it", "experimental_unit": "bat pass recorded at canopy-tower detectors (9 nights x 4 locations)", "intervention": "none imposed; natural variation in calculated moon illumination", "comparator": "lower calculated moon illumination", "mechanism_limit": "acoustic activity is not detection, avoidance or a visual threshold; moon illumination is calculated, the percentages are undefined in the paper, and passes are not individuals",

- old (raw JSON text, occurs once in line 6):

    "authors": "Dylan G.E. Gomes, Giulliana Appel, Jesse R. Barber"

  new:

    "authors": "Gomes DGE, Appel G, Barber JR"

- old (raw JSON text, occurs once in line 6):

    at the Saut Pararé station, Nouragues (the Figure 3 caption names Nouragues, the Methods Saut Pararé; the page is inconsistent),

  new:

    at the Nouragues research station (the Methods print 'Saut Pararé Nourages research station', the Figure 3 caption 'Nouragues Research Station'; a spelling difference),

## Optional fixes

- Line 4: if the desk prefers to keep moon-driven activity out of `behaviour_vision` entirely, `sense_light_nonvisual` (masking) is the alternative; I did not count it.
- Line 4: read the per-eclipse subject counts from the Figure 3 panels if a tool returns them.
- Line 5: family "Lampyridae" and order "Coleoptera" are printed and may be filled; line 6: "Molossidae" (Methods) and "Chiroptera" (keywords) are printed and may be filled.
- Main (outside this unit): oa-1:4050-4051 and canon-5:214 carry Aotus azarai, a synonym of Aotus azarae; flag for the main-file name pass.
