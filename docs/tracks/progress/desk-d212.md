# desk-d212 progress

Task: animal sensory-trait records from open-licence papers, aiming at species and papers absent from main (checked against every evidence and audit file by species and DOI). 3 records filed (target 5; fewer filed rather than padded). About 34 WebSearches used.

## Records filed (docs/views/evidence/desk-d212.jsonl)
1. Hipposideros pratti, sense_echolocation: Doppler shift compensation in the moving-pendulum paradigm, 83.9% (72.3 to 92.6% across four bats). Luo et al. 2022, Front Syst Neurosci 16: 920703, CC BY. A 2025 Corrigendum (equation operator typo, conclusions unchanged) is noted in the record.
2. Chrysochloris asiatica, sense_vibration: ossicular chain resonant frequencies 71 to 200 Hz in euthanised, dissected skulls (laser Doppler vibrometry). Willi, Bronner, Narins 2006, J Exp Biol 209: 302-313, free-to-read publisher PDF with no CC licence printed (access open on the publisher-free-text rule).
3. Lophiobagrus cyclurus, sense_hearing: lowest AEP threshold 81.6 dB re 1 uPa at 1 kHz in the largest size group. Lechner et al. 2011, PLoS ONE 6: e18511, University of Vienna repository PDF printing the CC Attribution statement.

## Queries (WebSearch, word for word in the order run, abbreviated groups)
- Eumetopias/Callorhinus vibrissae hydrodynamic detection threshold; Paramormyrops/Brachyhypopomus/Sternopygus EOD electroreceptor tuning; Pteronotus/Rhinolophus/Noctilio echolocation call frequency
- Electrophorus electroreception; Callorhinus ursinus vision/hearing/vibrissae; Hipposideros/Pteronotus Doppler shift compensation; Varanus sensory
- Dugong/Trichechus senegalensis sensory; Eublepharis/gecko colour vision behaviour; Cassiopea/Aurelia light detection
- Luo Jinhong Hipposideros/Rhinolophus; Rhinolophus resting frequency; Precise Doppler shift compensation Hipposideros armiger; golden mole/elephant shrew/sengi; Noctilio/Pteronotus/Mormoops; Latimeria/Polypterus/Lepisosteus
- JEB auditory brainstem response; JEB seismic vibration sensitivity; amphioxus Branchiostoma; wombat/koala/dunnart; Harpegnathos/Odontomachus/Paraponera ants; Nothobranchius/Kryptolebias/Anableps; Ginglymostoma/Squatina/Hexanchus/Isurus
- catfish/gourami/Channa hearing; Lasius/Pogonomyrmex/Messor polarized light; Ladich hearing PLOS ONE; Ladich Scientific Reports/Frontiers/PeerJ; Danionella/Pimelodus/Platydoras/Synodontis hearing; Pollimyrus/Petrocephalus/Gymnarchus; Ginglymostoma/Torpedo/Narcine; Corrigendum search for the H. pratti paper; Mammal Diversity Database check; Lophiobagrus Catalog of Fishes

Screening of main: genera absent from main's evidence (Electrophorus, Callorhinus, Eumetopias, Pusa, Dugong, Hipposideros, Pteronotus, Noctilio, Aplysia, Cassiopea, Branchiostoma, Latimeria, Polypterus, Varanus, Eublepharis, Neotoma, Elephantulus, Chrysochloris, Nothobranchius, Kryptolebias, Anableps, Ginglymostoma, Squatina, Torpedo, Pollimyrus and others) were searched; most hits were closed or on refused hosts. Main is saturated for the named systems in the launch list (bats, hawkmoths, seals, mantis shrimp, fiddler crabs, Cataglyphis, Scarabaeus, Octopus, zebrafish, crocodilians, snakes).

## Held-out leads
- Hipposideros armiger Doppler shift compensation (Schoeppler, Schnitzler, Denzinger, Sci Rep 8: 4598, DOI 10.1038/s41598-018-22880-y): the only readable copy attempts failed (nature.com page: permission request unanswered; Tuebingen repository: no abstract, no file). Lead only.
- Same group: Luo et al. 2023 J Comp Physiol A 209: 203-214 (Springer, host refused); closed licence.
- Rhinolophus hipposideros resting frequency (Kohyt et al. 2022, Folia Biologica 70: 33-42, CC-BY printed on the repository copy): the mean (about 108.7 kHz females, about 105.4 kHz males, SD about 0.6 to 0.9) is only in Table 1 and the summary tool will not return table rows verbatim, and no Results sentence of 125 characters or fewer states it. Not filed.
- Cape golden mole sibling and Zambian mole-rat review (Burda 2022, Front Ecol Evol 10: 866709): review, no measurement.
- Hearing in African bullhead catfish group: Synodontis schoutedeni ontogeny (Lechner, Wysocki, Ladich, BMC Biol 8: 10): the only fetch route redirected to Springer (refused host). Lead only.
- Four-eyed fish Anableps opsin expression (Salgado et al. 2022, Front Neurosci 16: 995469, CC BY): gene-expression asymmetry, not a measured sensory trait; held.
- Gecko colour/image response (Katlein et al. 2022, J Zool 317: 138-146, three species pooled in the abstract, a null for colour): pooled and null; the licence statement came from a repository record page, not an exact copy. Held.
- Piebald shrew (Diplomesodon pulchellum) self-produced body vibration 160.5 Hz (Volodin et al. 2012, J Exp Biol 215: 2849-2852): production, not sensing; held.
- Harbour seal papers (Krueger et al. 2018 jeb170753; Niesterok et al. 2017 jeb158055): harbour seal is unit d211's species; not filed.
- Capshaw et al. 2020 salamander seismic and bone conduction (J Exp Biol 223: jeb.236489): species not named on the page reached, no full text. Lead only.
- Coelacanth rostral organ (Sci Rep 2015, Springer link, PMC refused): not read.

## Owner questions
1. Hipposideros pratti: confirm against the Mammal Diversity Database (a Wikipedia taxon box shows the genus as Macronycteris while the species and IUCN name are Hipposideros pratti). gbif-names.tsv has no row for any of the three taxa filed.
2. Lophiobagrus cyclurus micro sign: the tool returned 'mPa' for the unit; check the printed article gives dB re 1 uPa.
3. H. pratti 83.9%: the quoted Discussion sentence does not name the pendulum paradigm; the summary tool said it concerns the pendulum only (Abstract gives 84% for it). If a reviewer wants the pendulum in the quote itself, use the Abstract or Results sentence once a full text is available.
4. Chrysochloris asiatica: no CC licence is printed on the publisher PDF (copyright line only); accepted here under the publisher-free-text rule.

## Tool notes
Blocked: nature.com article page (permission request unanswered), Springer redirect from BMC Biology, DOAJ record for one H. pratti-related search. quotecheck.py was not run: no full text was available locally, only summary-tool readings, so every quote rests on the summary tool's verbatim return and on its statement of where each sentence begins and ends.
