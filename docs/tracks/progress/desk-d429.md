# desk-d429 progress

Angle: eye-size records, wider net, twenty-fourth round. 10 records from two open papers in journals not used before (log docs/views/evidence/desk-d429.jsonl). check.py: 0 problems, also with --require-evidence-kind. About 36 WebSearches used.

## Filed
- Acta Zoologica Mexicana (nueva serie) 42: 1-7 (10.21829/azm.2026.4212850; Chame-Vazquez D, Gomez-Moreno KG, Jimenez M-L, 2026; Filistatidae): Filistatinella bacanora, male holotype CARCIB-Ar-Ho-0073 and female paratype CARCIB-Ar-Pa-0411, AME/PME/ALE/PLE each, 8 records, eye_diameter_mm because the sentence prints 'Eye diameters and interdistances'.
- Arthropod Systematics & Phylogeny 84: 95-121 (10.3897/asp.84.e174748; Meng G, Carvalho LS, Podsiadlowski L, Huber BA, 2026; Pholcidae): Caipira mineira, male holotype CHNUFPI 9069, PME 45 and AME 20 micrometres (printed units kept, not converted), 2 records, sensory_anatomy (label 'diameter PME', no Methods definition).

## Weak spots
- Filistatinella licence: the PDF is labelled CC BY-NC-SA, not CC BY. Auditor to rule whether NC-SA is acceptable (CC BY-NC is accepted, NC-ND held out).
- F. bacanora: WSC species page not reached (WSC reference 19193 opened, species not named): validity UNCHECKED. Position of the eye sentence between 'Clypeus length' and 'Sternum length' comes from the fetch tool's before/after split. The page prints no Class or Order heading.
- Caipira baiana not filed: the XML section returned only Material examined and Diagnosis; an earlier preview fetch had returned eye sentences for it that the XML did not contain.
- Crossref not read for either paper (UNCHECKED).

## Not filed and why
- Hahnia jiangkou (BDJ 11 e113400), Hahnia dabashan and Sinahahnia chengkou (ZooKeys 1254), ZooKeys 1229 Atypus: already on main.
- Cybaeus eremospelyngus (Species Diversity 30(1)) and Cybaeus pycnothrix, C. tateyamensis (Soil Organisms 97(3)): no eye measurements printed. Cladothela (Acta Arachnologica 74(1)): abstract page only.
- Allpamayu suyuwixsa (Zoosystema 48(9)): publisher page shows abstract only, no licence. Dolomedes afi (Acta Biologica Sibirica 12) and Opisthoncus mileshendyi: the journal site was under maintenance; the Opisthoncus page is an unpublished draft with no eye values. Heterothele maxima (Arachnology 20(4)) and Porrhothele peninsularis: only repository copies appeared in search results. Aphantochilus rainbow (Arachnology 20(4)): no text reached.
- Pensoft pages went into maintenance late in the unit; ZooKeys article ids 106315 and 73345 were not identified.

## Leads
- Zoological Systematics 51(1): 1-73 Mi, Wang & Feng (Araneidae, Qomolangma, 21 new species, WSC reference 19201): no publisher page reached.
- Kaderka Urupelma (Revista Peruana de Biologia 33(3)), Logunov Lyssomaninae (Proc. Zool. Inst. RAS 330(2)), Lin Chilobrachys and Lu Bowie (Acta Arachnologica Sinica 35(1)): no search result reached text.

## Desk disposition after audits 801-802 (2 November 2026)
2 of 10 records merged (Caipira mineira, lines 9-10; audit 802 fixed the heading path, licence cut mark and paratype list; sensory_anatomy; unit µm as printed). Dropped: lines 1-8 (Filistatinella bacanora, Acta Zoológica Mexicana 42: 1-7). Audit 801 found (a) a counted trait error (the Methods never define how eyes were measured, so eye_diameter_mm was wrong and the lines belong under sensory_anatomy), (b) the PDF prints only a header tag "CC BY-NC-SA" with no licence sentence, and (c) the WSC species page was never reached. Under the standing licence rule (an open licence statement on the exact copy read) and the rule that a WSC species page must be opened for every species, the desk holds the lines out; the auditor's corrected replacement lines are in /tmp/m311/audit-801.md and pass check.py if the owner rules a header tag sufficient and the WSC page is read. OWNER QUESTION: is a bare header licence tag (no sentence) enough, and is CC BY-NC-SA acceptable beside CC BY-NC? Counted errors: 8 trait errors on the dropped lines; 0 on the merged lines.
