# desk-d579 progress

evidence_intake: evidence-kind-v2; intake_base: e29b201ab944aaafc74aa2a4f5e720a9a9530cd2 (origin/main when checked).

Angle: sensory_anatomy widened beyond frog tympanum. Structures filed: loreal pit and nostril (pit viper), reptile tympanum (gecko), caecilian tentacular canal, orbital aperture and nostril (skull, micro-CT). No new trait or structure key family was invented: sensory_anatomy structure values on main are free text and these follow the d574 wording style (the loreal pit, tentacular canal and orbital aperture are new structure strings under the existing trait; no new trait). About 36 WebSearches. 6 records (docs/views/evidence/desk-d579.jsonl), all anatomical_presence. check.py: 0 problems (plain and --require-evidence-kind); check_submission.py: 6 new, 0 problems.

## Filed (Pensoft, CC BY 4.0 sentence read on the publisher page; authority page opened from my own search)
- Protobothrops flavirostris (Herpetozoa 38: 43-60, 10.3897/herpetozoa.38.e146004; Reptile Database page opened): loreal pit present, large, triangular, closer to eye than to nostril (whole 17-word sentence); nostril vertical, elliptical, completely enclosed in nasal scale (whole sentence, joined from two reader pieces).
- Goniurosaurus wuzhengjuni (ZSE 102(2): 611-620, 10.3897/zse.102.177343; Reptile Database page opened): tympanum deeply recessed, bordered anteriorly by two spinose scales (whole sentence). The species carries one pupil_shape row on main (desk-d573), a different trait.
- Ichthyophis griseivermis (Vertebrate Zoology 75: 405-440, 10.3897/vz.75.e149399; ASW page opened): holotype micro-CT skull atlas; tentacular canal open laterally, fused with the orbital aperture, entirely in the maxillopalatine (whole sentence); orbital apertures oval, slightly dorsoventrally compressed, anterolateral, about the size of the nostrils (one marked cut after the orientation clause); nostrils relatively large, rounded, terminal and anterior orientation (whole sentence).

## Searches that reached the full text
Exact title (plus journal, plus "article preview" for ZSE) returned the article_preview.php link: Protobothrops ('A new endemic karst-associated species of lance-headed pit viper (Squamata, Viperidae, Protobothrops) from Laos Herpetozoa'), Goniurosaurus ('A New Species of Goniurosaurus (Sauria, Gekkota, Eublepharidae) from Guangxi, China Zoosystematics and Evolution article preview'). The Ichthyophis page came from the keyword search 'new species Ichthyophis OR Chikila OR Uraeotyphlus OR Siphonops OR Caecilia sp. nov. 2025 2026 tentacle eyes visible through skin novataxa'. Titles were found from novataxa.blogspot.com month pages reached by search. Authority pages: 'Protobothrops flavirostris Grassby-Lewis 2025 Reptile Database Vang Vieng lance-headed pit viper', 'Goniurosaurus wuzhengjuni Reptile Database species', 'Ichthyophis griseivermis Amphibian Species of the World Poyarkov 2025'.

## Weak spots
- Everything was read through the WebFetch page reader in pieces of about 125 characters; sentences were joined from pieces and not checked against raw page text. The Ichthyophis page reader covered 100000 of 122970 characters (a read from offset 100000 returned table rows only), so the species description, diagnosis and variation sections of that paper were not seen and no tentacular-aperture description sentence is cited.
- The Ichthyophis sentences come from an osteology (CT) section of the holotype, not external anatomy; stated in each record.
- Crossref not used. The ASW page for the caecilian prints no family; family from the URL path and the paper's title.

## Not filed and why
- Goniurosaurus wuzhengjuni naris sentence ("Each external naris is encircled by seven nasal scales ..."): two reader renderings disagreed (a dash-joined list versus a short sentence), so the wording is unverified. Its eyelid fringe count (ciliaria 52/47) is in Table 1 and the Diagnosis item list only.
- Eublepharis jhuma (Herpetozoa 39: 161-176): ear-opening, supraciliary and nostril clauses sit inside one sentence of well over 40 words that starts at 'Eyes large'; the eye/pupil part is on main (desk-d353).
- Gekko wuzhengjuni (ZSE 102(2): 719-729): nares, pupil and ear opening are clauses of one long list sentence; the species is on main for pupil (desk-d573).
- Ovophis zhaoermii (ZooKeys 1230), Trimeresurus nujiang (ZSE 101(4)): the loreal pit and nostril clauses sit in long semicolon sentences; Trimeresurus loong XML cut before the description.
- Trachischium lalremsangai (Herpetozoa 39: 203-215): nostril sentence "Nasals divided; nostril vertical, situated at the suture between anterior and posterior nasals, giving a bilobed appearance." was whole and short, but no Reptile Database page for the species appeared in my search results (only T. hmuifang), so held out; lead for a unit that reaches that page.
- Cyrtodactylus teraiensis (ZooKeys 1275): the reader returned the paper only to the Methods; ED is on main (desk-d488, d490). Vertebrate Zoology / Plazi treatment pages for Scincella balluca and S. alia: journal not established.
- Murina medogensis, M. milinensis, Myotis kalkoae, Soriculus dexingensis: already on main (desk-d345, d347).
