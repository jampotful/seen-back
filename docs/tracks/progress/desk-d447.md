# desk-d447 progress

Angle: eye-size records, forty-second round, wider net (European Journal of Taxonomy papers reached through publisher download URLs that appeared in my own search results). 57 records in docs/views/evidence/desk-d447.jsonl; check.py and check.py --require-evidence-kind report 0 problems for this log (other logs in the tree carry older problems that are not mine). Every value was re-checked by script against its own quote.

## Filed
- EJT 861: 113-131 (10.5852/ejt.2023.861.2071; Gonzalez-Filho, Guadanucci & Brescovit 2023; Barychelidae): Ammonius benoiti male holotype ALE, PME, PLE (AME printed 'absent', not filed); Ammonius pupulus female RMCA 227221 AME, ALE, PME, PLE (female first described here). eye_diameter_mm because the sentence prints 'Eyes diameters and interdistances' (a variant of the literal label; flagged in notes). 7 records.
- EJT 921: 98-115 (10.5852/ejt.2024.921.2419; Bertani, Bichuette, Cordeiro & Gallão 2024; Sicariidae, cave species): Loxosceles boqueirao, L. planetaria, L. bodoquena, male and female each, ALE, PME, PLE. sensory_anatomy because the label is 'Eye sizes' and the Methods define no eye dimension. 18 records.
- EJT 856: 152-169 (10.5852/ejt.2023.856.2035; Rheims 2023; Sparassidae): Cuiambuca aratangi (male holotype, female paratype), C. borborema (female holotype), C. vacabrava (male holotype, female paratype IBSP 43277), AME, ALE, PME, PLE. eye_diameter_mm ('Eye diameters:' printed). The sentence has no per-eye labels; eyes are assigned by position in the Methods order AME, ALE, PME, PLE. 20 records.
- EJT 821: 166-199 (10.5852/ejt.2022.821.1805; Rheims & Alayón 2022; Sparassidae): Neostasina aceitillar (female holotype), N. bani (male holotype), N. maisi (male holotype), AME, ALE, PME, PLE by Methods order. 12 records. Held back only by the 60-line cap: N. demaco, N. juanita, N. toronegro (female holotypes), N. paraiso (male holotype, female paratype), the female paratypes of N. bani and N. maisi (all read in the same PDF, sentences 'Eye diameters: ...'); a later unit can file them from the publisher download URL.

## Weak spots
- All text came as fragments and summaries of the publisher PDFs through the fetch tool (each PDF read two or three times with consistent numbers). Conditions say which sentences were returned as quoted.
- Cuiambuca: the Methods sentence naming the eye order came as a fragment plus the tool's paraphrase; auditors should confirm the order AME, ALE, PME, PLE on the page (same check as Uaica in desk-d378).
- Loxosceles: no WSC species page reached (the WSC Loxosceles list shows 'last updated 2024-02-20'); validity UNCHECKED. Cuiambuca: WSC genus page lists the three species; per-species status not stated. Ammonius: WSC species pages 67840 and 12165 accepted.
- Ammonius pupulus female: the tool did not tie the code RMCA 227221 to a specific line of 'Other material examined'.
- Crossref not read for any DOI; DOIs come from the publisher pages/PDF.

## Not filed and why
- Ero lizae, E. natashae (EJT 921: 76): the descriptions print only ocular-tubercle lengths and widths, no eye sizes.
- Cybaeodamus ampullatus, C. spinosissimus, C. malkini (EJT 1004: 92-119): values reached only on a repository copy (africamuseum.be); the publisher download URL was not permitted. Lead.
- Ecuadorian Microstigmatidae (EJT 1007: 87-132, six new species): publisher download failed with a client error. Lead.
- Sinahahnia chengkou and Uaica species: already on main.
- Plazi treatment pages return only a redirect notice; not usable.

## Desk disposition after audits (2 November 2026)

Audits 877-884 judged all 57 lines (EJT 861 Ammonius, EJT 921 Loxosceles, EJT 856 Cuiambuca, EJT 821 Neostasina). 21 lines merged: Ammonius benoiti and A. pupulus (1-7), Cuiambuca aratangi and C. borborema female (29-35), C. vacabrava female ALE, PME, PLE (43-45), Neostasina maisi male (54-57). 36 lines were named for dropping and dropped, none for a wrong value or quote: Loxosceles boqueirao, L. planetaria, L. bodoquena (lines 8-25, no WSC species page reached by audits 878, 879, 880); Cuiambuca aratangi male PLE (26-28 in audit 880's block, PDF never reached from its own searches), C. borborema female PME and PLE, C. vacabrava male and female AME (36-42, audit 882's searches never surfaced the publisher full text); Neostasina aceitillar (46-49, no WSC species page) and N. bani (50-53, no WSC species page). The auditors' corrected replacement lines for the dropped lines are in /tmp/m311/audit-878.md to audit-884.md for a later refile if a WSC species page and the Methods eye order are reached from a unit's own search results. The Methods of EJT 856 and EJT 821 print the eye order ('eye diameters as AME, ALE, PME, PLE and interdistances as...'), so the positional assignment of the unlabelled eye values is justified for the kept lines. TRAIT: audit 877 moved the Ammonius lines to sensory_anatomy because the Methods print no diameter definition; the desk kept eye_diameter_mm because the quoted sentence prints the label 'Eyes diameters and interdistances' (standing label ruling; the same call as desk-d446). OWNER QUESTION (carried): eye_diameter_mm vs sensory_anatomy for label-only evidence.
