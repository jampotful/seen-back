# desk-d67 progress (single-species title searches, plant sense_light_nonvisual and diel)

Started 29 October 2026. Branch research/desk-d67. WebSearch used: about 97 of 100. Every record is abstract-only (partial true); each accepted name was read on a POWO page opened in this session, and each cited id is the id of the accepted name itself.

## Task A (wanted lines, docs/views/wanted/desk-d67.jsonl)
Three of four d66 lines completed.
- Jatropha curcas (PeerJ 4: e1819, 2016): six authors read on the DOAJ record; the PeerJ page itself printed only "Rincon-Rabanales et al.".
- Stevia rebaudiana (Int J Biol 3(4): 83-91, 2011): authors Abdullateef RA, Osman M, year, journal and issue from the IIUM repository record; the DOI came from the doi.org result of a search, and the abstract is unread.
- Eucalyptus ten species: the CSIRO page prints 2019 (vol. 66(8), 657-666), so year corrected from 2018.
- Aloe arborescens (Plant Biosystems, DOI 10.1080/11263504.2013.782901) left out: the publisher page fetch prints the title only, and no other opened page gave authors or journal. A neighbouring reference list on the same page shows Plant Biosyst 146/148 papers by Lantieri, Salmeri and others, but nothing ties them to this DOI, so nothing was guessed.

## Filed (3 records, docs/views/evidence/desk-d67.jsonl)
Thuja plicata (Coates and Burton 1999, greatest response to increased light under deep shade), Gaultheria shallon (Messier 1992, leaf area up and leaf thickness down with shading), Lonicera maackii (Lieurance and Cipollini 2013, resource limitation more influential than damage on juvenile growth).

## Species tried
Glechoma hederacea, Impatiens capensis, I. glandulifera, Chamaenerion angustifolium, Ficaria verna, Lonicera japonica, Rosa multiflora, Echium vulgare, Senecio vulgaris, Urtica dioica, Bellis perennis, Alliaria petiolata, Cytisus scoparius, Oxalis pes-caprae, Phytolacca americana, Ricinus communis, Calystegia sepium, Silene spp., Datura wrightii, Linaria vulgaris, Chelidonium majus, Lamium amplexicaule, Lysimachia arvensis, Plantago major, Pseudotsuga menziesii, Thuja plicata, Corylus avellana, Rubus idaeus, Acer saccharum, Tsuga canadensis, Gaultheria shallon, Pinus sylvestris, Vaccinium vitis-idaea, Oenothera speciosa, Dactylorhiza majalis, Populus tremuloides, Lonicera maackii, Quercus rubra, Sorbus aucuparia, Rhus typhina, Mahonia aquifolium.

## Read, not filed
- Already on main: Pinus sylvestris anthocyanin and shade (Razzak 2017, pce.12921), Dactylorhiza majalis light germination (tb06734), Jacobaea maritima (Senecio cineraria) in vitro light (desk-d56), Alliaria petiolata GA3 (Yasin and Andreasen 2015).
- No quote of 125 characters or fewer that reports a result with direction: Oxalis pes-caprae shading (Verdaguer 2010, the shade sentence runs about 240), Alliaria scarification plus GA3 (Sosnoskie and Cardina 2017; journal and DOI not printed on the page), Senecio vulgaris (Lutman 2008), Impatiens capensis (Perglova 2009, no DOI on the page), Echium vulgare (van Breemen 1984, no DOI), Lamium amplexicaule (Baskin 1981), Mahonia aquifolium (Pipinis 2015), Vaccinium vitis-idaea and Arctous alpina shading (pooled, sentences 126 and over), Tsuga canadensis (Mohammed and Parker 1999: the 58% survival clause is part of a 126-character sentence).
- Pseudotsuga menziesii (MacDonald and Owens 1993: "Crown height was greater under abrupt short day than under gradual short day.") readable and whole, but no page printed the journal name next to the DOI, so unfiled.
- Subspecies or hybrid or cultivar: Chelidonium majus subsp. asiaticum (Ji 2022), Eustoma grandiflorum (cultivar), Anagallis arvensis subsp. foemina (Lipp and Ballard 1963; the one-sentence abstract is 214 characters).
- Blocked or unreadable: PMC pages (reCAPTCHA), Thieme (interstitial), scinapse (reCAPTCHA), AMiner, bioone ecoscience and Torrey (meta tags only), a Czech catalogue record behind an Anubis wall.
- Skipped as background: Schulz 2023 on Lonicera maackii in deep shade (its short sentences begin "appears" or restate the aim).

## Advice on yield
Forestry and botany journals from the 1990s on (Canadian Journal of Forest Research, Canadian Journal of Botany) gave all three records: search "<tree or forest-floor shrub> shade light growth" and open an agris.fao.org, zhenzhi or sciencegate record, which print the abstract with year, volume and pages. The commonest losses were result sentences over 125 characters, pages that print no journal or DOI, and species already on main (grep the evidence files for the taxon and DOI before opening a lead). Wildflower queries ("<species> germination light") mostly returned seed-supplier pages and theses. WebFetch paraphrases long sentences and counts characters loosely; ask it for a named sentence "from its first word to the full stop" and re-read it on a second page before filing. Open cells remain for Pinus ponderosa, Quercus alba, Populus deltoides, Sambucus nigra and the dune and fern species, where no search reached a readable abstract.

## Desk disposition after audit 157

Audit 157 judged 1 of 3 evidence records an error (line 1, Thuja plicata: ambient field light, a gradient study, not a set-light trial). The desk dropped that record and merged the other two (Gaultheria shallon, Lonicera maackii). The audit's note on the Lonicera value (it pools light with nitrogen) was a noted fault and did not count toward the error rate. All three wanted lines were merged, with year 2018 restored on the Eucalyptus line (volume 66 is the 2018 volume; online 14 February 2019).
