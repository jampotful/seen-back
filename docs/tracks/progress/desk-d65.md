# desk-d65 progress (Poaceae, uncommon Asteraceae, wild Fabaceae, Brassicaceae/Solanaceae/Lamiaceae, forest trees)

Started 29 October 2026. Branch research/desk-d65. WebSearch used: about 60 of 100. The unit stopped on the token budget (about 300k), not on searches. Every record is an abstract reading (partial true); each quote is one whole abstract sentence of at most 125 characters, read through WebFetch asked for verbatim sentences with character counts. Taxon and DOI were grepped over docs/views/evidence on main and on the d63 and d64 branches.

## Groups and species tried
- Poaceae: Themeda triandra, Phragmites australis, Spartina alterniflora and S. patens, Bromus (several), Aristida, Eragrostis tef, Agrostis and Poa, Lolium arundinaceum and Dactylis glomerata, Dendrocalamus latiflorus.
- Asteraceae: Helichrysum, Rhodanthe, Podolepis, Gazania, Osteospermum, Baccharis, Tithonia, Senecio cineraria (Jacobaea maritima), Celmisia, Leontopodium.
- Fabaceae: Acacia and Senegalia, Vachellia, Lupinus, Astragalus, Dalea, Mimosa, Desmanthus, Trifolium riograndense, Senna, Medicago truncatula.
- Brassicaceae, Solanaceae, Lamiaceae: Aethionema, Sisymbrium, Cakile, Solanum (Australian), Atriplex, Nicotiana, Malva.
- Forest trees: Quercus, Fraxinus, Triadica, Melia, Acer, Croton, Schizolobium, Copaifera.

## Filed (6 records, docs/views/evidence/desk-d65.jsonl)
- Aristida recurvata and Aristida riparia (Ramos et al. 2019, American Journal of Botany 106(9): 1190-1201; grade g pooled, smoke promoted germination; both names accepted on WFO, colplanta and POWO pages opened; volume, issue and pages from the FAPESP page).
- Senegalia polyphylla (Araujo Neto et al. 2003; paper's Acacia polyphylla is a WFO synonym; germination decreased in darkness).
- Aethionema arabicum (Merai et al. 2019, J Exp Bot; germination inhibited by red, blue and far-red light; accepted name from the GBIF page, Catalogue of Life).
- Quercus mongolica (Li et al. 2024, Forests 15(3): 538; severe shading inhibited growth; full author list from the MDPI PDF).
- Croton urucurana (Alvarenga et al. 2003, Revista Arvore 27(1): 53-57; root biomass higher in full sun).

## Read, not filed
- Already on main: Jacobaea maritima (Victorio et al. 2010, desk-d56; I filed it by mistake and deleted my line before the first commit), Poa annua and the Agrostis/Poa light paper of Knot 2006 (desk-d1), Onopordum/Stachys/Sarcopoterium smoke paper (desk-d32), Dactylis glomerata light cell (sweep-9).
- Sentence over 125 characters, no direction, or not the trait: Themeda triandra thesis (Baxter 1996, thesis, no DOI), Phragmites (Ekstam et al. 1999; the short sentence reports temperature fluctuation, not light), Baccharis halimifolia (Panetta 1979, seed burial only), Baccharis dracunculifolia (Acta Botanica Brasilica 2002, EVI sentence without light direction, no authors or DOI on the page), Solanum centrale and S. orbiculatum (Commander et al. 2008, no direction), Atriplex (Stevens et al. 2006), Senna macranthera, Melia azedarach (Cavusoglu and Sulusoglu, no DOI or pages), Schizolobium parahyba, Copaifera langsdorffii, Acacia species of central Argentina (Funes and Venier 2006, temperature only), Medicago truncatula volatiles (Arimura et al. 2008), Nicotiana attenuata clock paper (already treated by d64).
- Pooled over many species (not filed): Merritt et al. 2006 on seven Australian Asteraceae (every species needed light, DOI 10.1079/SSR2005232; only Podolepis canescens was confirmed accepted, on the APC page; the other six names could not be checked because fetches are limited to URLs that a search returned), Bell et al. 1999 (over a dozen species).
- No DOI or volume printed: Tithonia diversifolia (Agboola et al. 2006, Rev Biol Trop 54(2): 385-402, "Light greatly enhanced the germination percentage of seeds by about 70%."), Desmanthus depressus and Trifolium riograndense (Suñé and Franke 2006, Rev Bras Sementes 28(3): 29-36; both light sentences read, no DOI on any page opened), Fraxinus excelsior (Tabari et al. 1998, Silva Gandavensis; DOI 10.21825/sg.v63i0.834 seen only in a search URL, volume unconfirmed), Eragrostis tef (Tiryaki and Kaplan 2019, abstract truncated on the page opened).
- Subspecies or hybrid: Acer miaotaiense subsp. yangjuechi (Chen et al. 2025, Forests 16: 296; title over 125 characters and rank is a subspecies); Gazania linearis and G. rigens pooled with hybrids (Adnan et al. 2025).
- Blocked or unanswered permission: bie.ala.org.au pages not returned by a search, openjournals.ugent.be, pmc.ncbi.nlm.nih.gov, biblat; no library proxy, ResearchGate or academia.edu page was opened (ezproxy copies in result lists were left alone).

No wanted lines written.

## Advice on yield
1. WebFetch may open only URLs that a search result or the conversation has shown, so an accepted-name check costs one search per species. Pooled records with six or seven names are not worth it; pick single-species papers.
2. The search tool returns titles and URLs only, so every candidate needs a fetch. Titles that name one species plus a light, shade, smoke or GA3 word gave the records (Aethionema, Quercus mongolica, Senegalia polyphylla); generic genus-list queries mostly returned theses, repositories and pooled papers.
3. Veins that worked: SciELO and DOAJ record pages for Brazilian forestry and botany journals (Revista Arvore, Revista Brasileira de Botanica; short English sentences, DOI on the DOAJ page), MDPI PDFs (full author list and DOI on page 1), Oxford and Cambridge article pages. Veins that did not: Tropical Grasslands pages (abstract cut off), Revista de Biologia Tropical (no DOI), repository pages (no volume).
4. Check docs/views/evidence on main for the taxon and the DOI before fetching, not after; three of the papers tried (Jacobaea maritima, Knot 2006, the Czech Poa paper) were already there.
5. Untried here: Lupinus, Trifolium, Medicago wild, Prosopis, Leucaena, Erythrina, Cakile and Lepidium germination, Hordeum and Avena wild, Zoysia, Cynodon, Stipa/Nassella, Phyllostachys and Bambusa flowering, Acer and Betula seedling shade, Rubiaceae and Oleaceae trees, Artemisia, Vernonia and Leontopodium.

## Desk disposition after audit 155
Audit 155 found 0 errors in 6 records. It noted that in the Aristida paper smoke raised germination only in darkness, which the value of lines 1 and 2 omits, so the desk dropped both pooled records. Line 6 (Croton urucurana) was kept: the quoted sentence is supported by the open full text although the abstract contradicts itself on root biomass. Aristida volume, issue and pages were confirmed on Embrapa, not the publisher page; the dropped records carried them. Senegalia polyphylla is accepted on WFO and not confirmed on POWO. 4 records merged.
