# desk-d421 progress

Angle: eye-size records, wider net, sixteenth round. 24 records from one open Arthropod Systematics & Phylogeny paper (log docs/views/evidence/desk-d421.jsonl). check.py: 0 problems for desk-d421.jsonl (other files carry older problems).

## Filed
- ASP 83: 687-712 (10.3897/asp.83.e171040; Allegue M, Peralta-Seen N, Ferretti N, 2025; Theraphosidae): Euathlus basalticus, E. kupal, E. susanae, male holotype and female paratype each, AME/ALE/PME/PLE, sensory_anatomy (sentence 'Eye sizes and interdistances'; Methods define no eye dimension).

## Weak spots
- Fetch tool cuts sentences at about 125 characters; each eye sentence was fetched in two calls (start, then remainder) and joined. Type lines were returned in pieces.
- Preview page prints no journal, volume or pages; volume 83 and pages 687-712 come from WSC reference 18893; an XML fetch had returned pp. 713-736 (unresolved). DOI from the figure-link prefix on the page. Crossref not read.
- E. susanae male eye sentence prints 'ALE, 0.59' (stray comma); filed as 0.59, flagged in the note.
- WSC: reference 18893 and genus list 3352 opened (all three species listed, no explicit status label); individual species pages not opened.

## Not filed and why
- Heteropoda curvata, flamma, lucerna (EJT 1022): already on main (desk-d378).
- Romopelma chirapa / Homoeomma josti (Evolutionary Systematics 10(2)): XML cut before chirapa's description; josti filed in desk-d411.
- Phlogiellus khampheng (ZooKeys 1247): on the avoid list.
- Pinelema (Raffles Bulletin of Zoology, RBZ-2025-0036): publisher page says All Rights Reserved, PDF not in search results.
- Ctenus igatu (J. Arachnol. 50): BioOne page returned no text. Porrhomma ozrenense (Zootaxa 5642): not open. Sinopoda ZooKeys 1159: already filed. Shuqiangius: only S. chuan new.

## Desk disposition after audits 775-777 (2 November 2026)
Filed 24, merged 24, counted errors 0 under the desk policy (wrong taxon, wrong quote or value, dropped line). All 24 lines carried a wrong citation page range (687-712, copied from WSC reference 18893); audits 775-777 opened the publisher XML from their own search results, which prints Arthropod Systematics & Phylogeny 83: 713-736 with no issue number (Zenodo and Plazi agree), and the corrected journal string is merged. The auditors labelled this an error; the desk counts it as a citation fault and reports it here so it is not hidden. Other faults: heading numbers and full stops missing in the where path, incomplete Methods, summarised Other-material paragraph. sensory_anatomy kept on all lines (the paper prints no eye-measurement definition). Nothing dropped. Lead: none new.
