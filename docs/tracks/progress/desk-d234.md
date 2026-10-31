# desk-d234

Sonnet 5.5 desk unit. Three records in docs/views/evidence/desk-d234.jsonl (check.py: 0 problems for this file; the intake-4/5 failed files carry older problems). About 28 WebSearches. Candidate DOIs were grepped against the whole docs/ tree and the d230 to d233 evidence files before opening. Taxa and traits searched: fish, frog, reptile, mammal hearing (ABR, audiogram); magnetic compass; electroreception; thermal sensing; touch and vibrissae; colour vision; acuity and ganglion cells; lambda_max and ERG; flicker fusion.

## Records

1 and 2. Pelophylax ridibundus and Rhinella marina, absolute_sensitivity (Astakhova et al. 2021, Int. J. Mol. Sci. 22(24): 13400, 10.3390/ijms222413400): green rods averaged 1.9 (frog) and 1.4 (toad) times the absolute flash sensitivity of red rods. Quote is one 20-word sentence read in two contiguous pieces. Toad difference is stated by the authors as not significant (next sentence, in conditions); frog significance not read. Frogs wild-caught, toads from a breeder, animal numbers and recording temperature not stated. Page CC BY 3.0, Crossref CC BY 4.0 vor. The em dash in the quote is as the tool printed it.
3. Staurois parvus, behaviour_vision (Preininger et al. 2013, PLoS ONE 8(1): e55367, 10.1371/journal.pone.0055367): fewer foot flags to a visual-only artificial foot flag than to acoustic stimuli (GLMM P = 0.007). Quote cut twice at the GLMM parentheses (marked (...)). Non-responders and wild status not stated; white versus grey foot made no difference (Discussion). A relative response, not a threshold. Crossref CC BY 4.0 unspecified plus page statement of the Creative Commons Attribution License.

## Held leads and why

- Monarch magnetic/cold paper (pone.0328737, CC0): already held by d223 (same reasons; Methods say n = 11 cold-exposed, Results n = 10; no randomisation of field order, all monarchs tested 3DS first).
- Carp electrosensitivity (peerj.17962): twitch, loss of orientation and tetany thresholds are in figures only; electrical stimulation of muscle, not electroreception.
- Atelopus franciscus playback (pone.0022080): behavioural, five-point reaction scale, total n not stated, sign tests.
- Collared peccary ganglion cells (pone.0239719): abstract and Results disagree (351.8 vs 2254 GC/mm2) and no cpd value or matching trait key.
- Yellow catfish light colour (animals 14/11/1583): preference, n = 6 per group.
- Pigeon colour discrimination (fevo.2021.639513) and TRPA1 thermal thresholds (fevo.2021.583837): reanalyses or compilations of published data.
- Krieger crab olfactory systems (peerj.1433): anatomy with n = 1 to 3, no trait key fits.
- Lamprey dopamine (ijms27031435): pharmacology.
- Already on main or held earlier: armadillo ABR (peerj.16602, as Dasypus mexicanus), Amalosia (filed by d230), fish hearing PLoS papers (pone.0026479, 0121219, 0037612, 0137290, 0067049, 0108583), eel, turtle, carp, bat and robin magnetic papers, walleye (page failed to load), Principapillatus ERG (reanalysis).

## Owner questions

1. Is absolute_sensitivity the right key for single-cell rod flash sensitivity (ratio of green to red rods), or should it wait for a receptor-level key?
2. Is a relative behavioural response to a visual-only stimulus (record 3) acceptable under behaviour_vision?

## Desk disposition after audit 328

Audit 328 judged all three records in error, all fixable; replacement text applied, 3 records merged, check.py 0 problems. Rod flash sensitivity I0.5 is a calculated photoisomerization density, not a measured light intensity, and the ratio compares rod types at equal photoisomerization density; this is stated in method. The Rhinella marina 1.4-fold ratio is carried as non-significant per the authors. Staurois parvus playback males were free-living in the stream.
