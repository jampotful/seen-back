# desk-d323: non-arthropod invertebrate eye and photoreceptor structure (brachiopod larva, oweniid annelids, two squids), 7 records

Branch research/desk-d323 from origin/main. About 40 WebSearches plus fetches; every fetched article URL came from a WebSearch first, except one slip noted below. `python3 -I tools/senses/check.py | grep 'd323\.'`: 7 records, 0 problems. Crossref read for 10.1186/2041-9139-2-6 (no licence field; page prints a Creative Commons Attribution License), 10.3389/fphys.2017.00105 (no licence field; Frontiers PDF prints CC BY) and 10.1186/s40851-022-00188-0 (CC BY 4.0 vor). No new trait key.

Filed (docs/views/evidence/desk-d323.jsonl):
1-2. Terebratalia transversa (brachiopod larva), sensory_anatomy: two putative photoreceptor cells per eye; enlarged ciliary membranes. EvoDevo 2:6 (2011). Family/order not printed. Fixation not on the page; larval age at TEM not stated.
3-4. Bathyteuthis abyssicola (600 um) and Liocranchia reinhardti (150 um), rhabdom_um as receptor length, Table 3 rows, Frontiers in Physiology 8 (2017). Same paper as the Xipholeptos notoides lines in desk-d153 (different species). Weak: table gives no column-level statement of measured vs representative length; B. abyssicola specimens partly aged-preserved.
5-6. Owenia fusiformis and Galathowenia oculata, eye_type flat pigment spot, one shared sentence (Zoological Letters 8, 2022); filed once per species.
7. Galathowenia oculata, sensory_anatomy: two types of pigmented supportive cells (same paper).

Weak spots: the Terebratalia and Purschke quotes came through the fetch tool in pieces or via a summarising layer, so the contiguous wording should be re-checked by the auditor against the page. The Terebratalia cell-count sentence is over 125 characters.

Dropped:
- On main: Copula sivickisi, Tripedalia cystophora and Chiropsella (sea-invertebrates audit), Conomurex luhuanus (jeb.243927, sheets/snail), Acanthaster planci (Petie 2016; also the accepted name for the Great Barrier Reef animals is unsettled), Idiosepius notoides (desk-d153), Lymnaea stagnalis.
- Mined: eye-state sentences of nemerteans, flatworms, polychaetes (desk-d294, d300, d301, d304, d318); Nipponnemertes incainca and Eucestoplana ittanmomen sentences already dropped there.
- Page text only paraphrased by the tool or licence absent: eLife xenopsin paper (Tricellaria inopinata, Malacoceros fuliginosus; abstract sentences over 125 characters, no verbatim text), Teuthowenia pellucida (PLoS ONE 10(5) e0123453; only PMC, a mirror and a repository copy reachable), Leptochiton asellus larval eyespots (EvoDevo; BMC page refused with PROVENANCE_REQUIRED, not retried), Garm et al. Tripedalia opsin paper (no licence on page), Spiochaetopterus costarum and Phyllochaetopterus socialis eye depth (sentences returned only as paraphrase).
- Reviews (Staurozoa eyes, Ciona brain sensory organs): not used.

Process slip: one WebFetch went to a university-proxy host (springerlink.bibliotecabuap.elogim.com) that appeared in search results; it redirected to a login, nothing was read from it, and the host was not used again. No paper was reached through it.
