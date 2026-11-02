# desk-d389 progress

Angle: open-access Leptonetidae taxonomy papers (Yao / Liu K-K group, Fujian and Jiangxi) that print the sentence 'Eye sizes and interdistances' per species and sex. 57 records from two Pensoft papers (log docs/views/evidence/desk-d389.jsonl). check.py: 0 problems for this log (other files in the repo carry older problems, untouched).

## Filed
- ZooKeys 1247: 187-205 (10.3897/zookeys.1247.154546, Crossref-verified, licence CC BY 4.0 vor; Wang Z-J et al., 2025): Leptonetela zhaoruii (male holotype, female paratype), Pararana jiufushanensis (male holotype, female paratype), Pararana songyuani (male holotype), Pararana gaofani (female, redescription, not a type). 18 records (ALE, PME, PLE per sex).
- ZooKeys 1189: 287-325 (10.3897/zookeys.1189.111041, Crossref-verified, licence CC BY 4.0 vor; Liu B-L et al., 2024): Leptonetela dawu, L. yuanhaoi, Longileptoneta huboliao, L. jiaxiani, L. renzhouensis, L. tianmenensis (male holotype and female paratype each) and Pararana mingxuani (male holotype). 39 records.
- Trait sensory_anatomy throughout: the sentences print 'Eye sizes', and the Material and methods text returned by the fetch tool defines no eye dimension. The sentences print no AME value.

## Weak spots
- Fetch tool returns pieces of about 125 characters; eye sentences over that length were rejoined from two pieces, and surrounding sentences and type lines are tool-returned pieces. Licence sentences are the tool's rendering of the page (possibly paraphrase); Crossref vor confirmed for both DOIs.
- WSC opened from search results for L. zhaoruii, P. jiufushanensis, P. songyuani, P. gaofani, P. mingxuani (all accepted). WSC pages for the six other ZooKeys 1189 species were not reached: validity UNCHECKED (stated in each record).
- Females: where the Paratype line lists several females (L. dawu, L. yuanhaoi, L. renzhouensis, L. tianmenensis, P. jiufushanensis), the text does not say which was measured; stated in each record. P. gaofani female comes from 'material examined' (Lep-22), with no type line.
- Exact subheading text ('Male (holotype)' etc.) was read only through fetch-tool summaries for some species.

## Not filed and why
- Pararana mingxuani female: the line is 'ALE 0.06, PME 0.04, PLE 0.05; ...' with no 'Eye sizes' label (and a clypeus clause inside it).
- Males-only species of ZooKeys 1189 (Leptonetela zuojiashanensis, Longileptoneta guadunensis, L. letuensis) left to stay near 60 lines; they are available in the same paper.
- Otacilia khezu (BDJ 12 e126716): eyes absent; only a Methods sentence 'Eye sizes are measured as the maximum diameter...' (lead for Otacilia papers with eyes).
- Search for Ochyroceratidae/Telemidae Zoosystematics and Evolution papers returned only Plazi/Zenodo/old copies.

## Desk disposition after audits 591-598 (2 November 2026)
All 57 lines (ZooKeys 1247: 187-205 Leptonetela zhaoruii, Pararana jiufushanensis/songyuani/gaofani; ZooKeys 1189: 287-325 Leptonetela dawu/yuanhaoi, Longileptoneta huboliao/jiaxiani/renzhouensis/tianmenensis, Pararana mingxuani) were audited by fresh Opus agents (audits 591 to 598). Counted errors: 28 lines. Most serious: all 13 PLE records from ZooKeys 1189 were filed with value 0.0 where the quotes print 0.05 to 0.09 (check.py does not catch it); the three P. mingxuani female records were wrongly marked label-less (the label is printed). Other faults: wrong following sentences, paraphrased licences, unidentified measured specimens, partial where paths. Every line was replaced with the auditor's corrected text; the merge script also asserted that each value appears as a number in its quote. Nothing dropped. Trait stays sensory_anatomy (whole Methods of both papers read, no eye diameter defined; millimetres printed). WSC validity unchecked for several species; Crossref vor unchecked. Owner question: check.py could test that a record's value appears in its quote.
