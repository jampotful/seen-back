# audit-280: desk-d196 (1 evidence record, no search records, no wanted lines)

Audited 31 October 2026 from the desk-d196 files present untracked in the worktree (docs/tracks/progress/desk-d196.md and 1 evidence line in docs/views/evidence/desk-d196.jsonl; neither committed here, neither edited). HEAD e963ff5f equals origin/main (git ls-remote). `tools/senses/check.py` on the evidence file: 1 record, 0 problems. Quote length (`len(q.split())`): 17, within 40. No searched or wanted file, so the one record was judged whole. Rules applied: oa-audit.md "Scientific context and counting (29 October 2026)", oa-read.md (grade and `partial`), BRIEF quote rules and trait table, the publisher-copy licence rule and the name rule, in the form of audits 270 to 279. Duplicates checked with git grep on HEAD across the whole tree (docs/views/evidence, docs/views/audit including corrected/ and ALL.jsonl, docs/views/searched, docs/views/wanted, views/, docs/views/gaps) for Tropilaelaps, mercedesae, Kadowaki and the DOI suffix fphys.2019.00556, and for Laelapidae and Varroa under docs/views and views. 2 WebSearch and 9 WebFetch calls used.

Sources opened: api.crossref.org/works/10.3389/FPHYS.2019.00556 (two passes, uppercase answered; a curl of the same host was refused by the proxy and not retried); the record URL www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2019.00556/pdf (two passes); agric.wa.gov.au/organisms/128321; woah.org Terrestrial Manual chapter 3.02.05 (Tropilaelaps) PDF; researchportalplus.anu.edu.au record of Anderson and Morgan 2007; two tb.plazi.org treatment links (both returned only a redirect notice). All returned by my WebSearches. No library proxy, ResearchGate, academia.edu, Sci-Hub or LibGen page was opened. WebFetch returns model summaries, so quotes were checked as MATCH/MISMATCH; points marked "(tool summary)" were not returned verbatim. No paper text is committed beyond single sentences and fragments quoted for verification.

## Bibliographic and licence

- Lei et al. 2019, fresh Crossref: Jing Lei (first), Qiushi Liu, Tatsuhiko Kadowaki, in the recorded order; title "Honey Bee Parasitic Mite Contains the Sensilla-Rich Sensory Organ on the Foreleg Tarsus" + "Expressing Ionotropic Receptors With Conserved Functions", as recorded; Frontiers in Physiology 10, no issue, article 556; issued and published 2019-05-09; CC BY 4.0 (vor, from 2019-05-09); relation has-preprint 10.1101/505529; no update-to. As recorded. PDF: "Copyright © 2019 Lei, Liu and Kadowaki." and "This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY)." Met.
- Uncounted: the note could name the bioRxiv preprint relation (10.1101/505529) so a later reader does not file the preprint as a second paper.

Bibliographic faults 0; licence faults 0.

## Name

- Tropilaelaps mercedesae: not in gbif-names.tsv or taxonomy-extra.tsv; the unit's authority was a Wikipedia genus list and the WA DPIRD page. Found here: the original description, Anderson and Morgan 2007, Experimental and Applied Acarology 43(1): 1-24, 10.1007/s10493-007-9103-0 (ANU research portal record): "Tropilaelaps mercedesae n. sp., which until now has been mistaken for T. clareae," (fragment); the WOAH Terrestrial Manual chapter 3.2.5 (most recent update adopted 2018): "There are at least four species in the genus Tropilaelaps." (clareae, mercedesae, koenigerum, thaii), genus in "family Laelapidae (Anderson & Roberts, 2013)", T. mercedesae "was formerly mistaken for T. clareae", no synonyms listed; WA DPIRD: "Anderson and Morgan, 2007", Laelapidae, Arachnida. No GBIF or Catalogue of Life page was reached (one targeted search returned none). The name is the current name of a species described in 2007 and treated as distinct by the WOAH standard; I judge it accepted. Not counted. Uncounted: replace the Wikipedia authority in `note` (owner question 2).

Name faults 0.

## Duplicates

- Tropilaelaps, mercedesae and the DOI are absent from main; "Kadowaki" hits only a persimmon wanted line (Sun et al. 2010, another person and paper). No Laelapidae or Varroa record under docs/views or views. Not a repeat, no contradiction.

Duplicates 0.

## Per-paper findings

### Lei et al. 2019 (line 1)

Quote MATCH (Discussion, subsection "T. mercedesae Sensory Organ Enriched With mRNAs for Sensory Proteins and Proteins Necessary for Ciliary Biogenesis/Transport"), whole sentence, 17 words; the degree sign is printed "◦C" in the PDF text, as the note says. The sentence before: "As the exclusive parasite of honey bee larva and pupa, T. mercedesae must adapt to the colony environment" "where the temperature and humidity are different and relatively constant compared to the outside environment."; the sentence after begins "This may have resulted in evolving the novel IRs, Tm15230 and Tm15243,". The sentence carries no citation.

Results (subsection "Conserved Sensory Functions Between D. melanogaster and T. mercedesae IR25a and IR93a"): "As shown in Figure 5A, the mites accumulated at the area of 32–40◦C in a gradient of 15–40◦C but randomly" "positioned on the testing arena without temperature gradient." (MATCH in two pieces; 28 words as check.py counts, so within the 40-word limit). Figure 5 legend: "Temperature and humidity preferences of T. mercedesae."; "(A) The fraction of mites in the area of 32–40◦C (n = 18) and the same area but without thermal gradient (n = 21) is shown."; "(P-value < 0.001, two-tailed Welch's t-test)". The fractions themselves are given only in the figure (tool summary). Methods, Thermotaxis Test: "Thermotaxis of T. mercedesae was tested as above except with 15–40◦C gradient or without temperature gradient."; "The testing arena was photographed every 10 min for 1h and we counted the number of mites located at the area" ">32◦C followed by calculating the preference index as above."; the fly set-up it refers to is an aluminium block with a cold water chamber and a hot probe at the ends, covered "with moist paper to maintain a uniform relative humidity (RH) along the gradient", a glass plate with three lanes 5 mm above, and "All experiments were performed in a room where the temperature was kept constant at 25◦C." Mite sampling: adult females from capped brood cells of colonies from a local beekeeper (tool summary); "The collected mites were directly used for all experiments and kept together with honey bee pupae in 33◦C" "incubator when necessary." Not stated: mites per trial or lane, whether n counts mites or trials, time off the host, and any host material in the arena (none is described). The D. melanogaster 25 °C figure is not measured in the paper: the fly thermotaxis assay scored flies below 24 °C on a 10 to 40 °C gradient, and 25 °C appears only as room temperature and in this Discussion sentence (tool summary).

Trait fit: a thermal gradient choice by whole animals is a behavioural preference, and sense_thermal ("other senses, string with figures") takes it; it is not reported as a detection threshold, and the record does not call it one. Grade m right (one named species, measured in the paper). Access open, `partial` absent, right (full PDF read).

Line 1. Counted (scientific context, fixable). The value "prefers temperatures between 32 and 40 °C" reads as a bounded preferred range, but 40 °C is the hot end of the 15 to 40 °C gradient and the Methods scored the mites simply as those "at the area >32◦C". The assay therefore shows that mites gathered at the warmest part of the arena it offered; it cannot show where their preference ends above 32 °C, and nothing above 40 °C was offered. The record carries neither the gradient range nor the >32 °C scoring, nor the design behind the test (off-host adult females from capped brood, kept with pupae at 33 °C before testing, 1 h with photographs every 10 min in a 25 °C room, uniform humidity, preference index, Welch's t-test P < 0.001), so a reader would take 40 °C as an upper preference limit. The Results sentence that reports the measurement is 28 words and quotable; the note's statement that it came back only as over-limit text reflects the abolished 125-character limit (desk-audit.md), and that sentence, which names the gradient, should be the quote. The value's "(the same sentence gives 25 °C for Drosophila melanogaster)" is an unsourced comparison about another species; uncounted, drop it.

## Verdicts

| line | taxon / value | verdict | fields | reason |
|---|---|---|---|---|
| 1 | Tropilaelaps mercedesae, prefers 32 to 40 °C | correct | quote, where, value, method, conditions | Quote MATCH (Discussion); 40 °C is the gradient's hot end and the Methods score >32 °C, so the "range" has no measured upper bound; gradient, scoring and off-host design not carried; a 28-word Results sentence was available |

Evidence errors: 1 of 1 (100%): scientific-context faults 1 (line 1); quote-form 0; name 0; duplicates 0; licence 0; bibliographic 0; abstract-access grading 0. Unfixable records: none.

Pooled with audits 172 to 279: 248 of 590 evidence records (42.0%; audit 279's 247 of 589 plus 1 of 1 here). Audits running at the same time as this one are not included. No search records, so nothing to pool with audits 83 to 90.

## Replacement text

Counted (line 1):
- `quote`: "As shown in Figure 5A, the mites accumulated at the area of 32–40◦C in a gradient of 15–40◦C but randomly positioned on the testing arena without temperature gradient." (copy the characters from the PDF; 28 words)
- `where`: "Results, section 'Conserved Sensory Functions Between D. melanogaster and T. mercedesae IR25a and IR93a'; Figure 5A"
- `value`: "adult females accumulated in the warmest zone offered (32 to 40 °C, the hot end of a 15 to 40 °C gradient) and were randomly placed without a gradient; no upper preference limit tested"
- `method`: "thermal gradient choice assay (aluminium block, cold water chamber and hot probe at the ends, moist paper for uniform humidity, glass-plate lanes; fly set-up of the same paper): 15 to 40 °C gradient or no gradient, photographed every 10 min for 1 h, mites at >32 °C counted for a preference index; two-tailed Welch's t-test"
- `conditions`: "Figure 5A: gradient n = 18, no gradient n = 21 (unit of n not stated; mites per trial not stated); P < 0.001; fractions given only in the figure; adult females from capped brood cells, tested off the host in a 25 °C room after being kept with honey bee pupae at 33 °C when necessary; no host material in the arena is described"
- `note`: keep the licence sentence; add "The Discussion restates the result: 'In fact, the mite prefers temperature between 32 and 40◦C in contrast to D. melanogaster at 25◦C.' (the fly figure is not measured in the paper)."; replace the name sentences with "Name: described by Anderson and Morgan 2007 (Exp Appl Acarol 43(1): 1-24, 10.1007/s10493-007-9103-0); the WOAH Terrestrial Manual chapter 3.2.5 (updated 2018) recognises it as one of four Tropilaelaps species, family Laelapidae; no GBIF or Catalogue of Life page reached. Not in gbif-names.tsv."; add "Crossref relation: has-preprint 10.1101/505529."

## Owner questions

1. When a gradient choice puts animals at the end of the gradient, should `value` give the scored zone with the gradient's ceiling stated (as above), or only "above 32 °C"? The replacement text keeps the paper's 32 to 40 °C zone with the ceiling named.
2. Tropilaelaps mercedesae rests on the original description and the WOAH manual; no GBIF or Catalogue of Life page was reached and the name is absent from gbif-names.tsv. Is that enough for Acari, or should the owner add it to taxonomy-extra.tsv?

Progress note: accurate on the DOI, the licence, the Discussion sentence and the not-filed no-gradient result. Its claim that the Results sentences were too long applies the abolished 125-character limit (the Results sentence is 28 words), and its name authority is weaker than what is reachable (original description, WOAH manual). It does not say that 40 °C is the gradient's top.

Verdict: 1 error in 1 (100%), above the 5% bar; pooled 42.0%. Error line: 1. No unfixable records; line 1 can merge with the counted text.

This report is model output and carries no authority.
