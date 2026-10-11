"""Proposed views for taxa that eyes.py sends to `other`. A first sorting, used to write docs/VIEWS.md.

Usage: view(kingdom, phylum, class_, order, family="") -> the name of a proposed view. The first rule that matches wins.
"""
FISH_CLASSES={'Actinopterygii','Elasmobranchii','Chondrichthyes','Holocephali','Sarcopterygii','Petromyzonti','Myxini','Cephalaspidomorphi','Coelacanthi','Dipneusti','Cladistii','Chondrostei','Holostei','Teleostei'}
def view(k,p,c,o,f=''):
    if k=='Fungi': return 'fungus and lichen'
    if k in ('Bacteria','Archaea','Viruses','incertae sedis','Chromista','Protozoa'):
        if p=='Mycetozoa' or c in ('Myxomycetes','Protosteliomycetes','Dictyostelia'): return 'slime mould'
        if p in ('Ochrophyta','Rhodophyta') or c in ('Phaeophyceae',): return 'seaweed and alga'
        return 'microbe, alga or virus'
    if k=='Plantae': return 'plant (has a view)'
    if k!='Animalia': return 'unplaced'
    if p=='Arthropoda':
        if o=='Araneae': return 'spider'
        if o in ('Ixodida','Trombidiformes','Mesostigmata','Sarcoptiformes','Oribatida','Holothyrida','Opilioacarida'): return 'tick and mite'
        if o=='Scorpiones': return 'scorpion'
        if c=='Arachnida': return 'harvestman and other arachnid'
        if c in ('Diplopoda','Chilopoda','Symphyla','Pauropoda'): return 'millipede and centipede'
        if c in ('Collembola','Entognatha','Diplura','Protura'): return 'springtail'
        if o=='Decapoda': return 'crab, crayfish, shrimp and lobster'
        if c in ('Malacostraca','Branchiopoda','Maxillopoda','Copepoda','Ostracoda','Hexanauplia','Thecostraca','Ichthyostraca','Remipedia','Cephalocarida'): return 'woodlouse and small crustacean'
        if c in ('Merostomata','Pycnogonida','Xiphosura'): return 'horseshoe crab and sea spider'
        if c=='Insecta': return 'insect (has a view)'
        return 'other arthropod'
    if p=='Mollusca':
        if c=='Cephalopoda': return 'octopus, squid and cuttlefish'
        if c=='Gastropoda': return 'snail and slug'
        if c=='Bivalvia': return 'clam, mussel and scallop'
        return 'chiton and other mollusc'
    if p=='Chordata':
        if c=='Mammalia':
            if o=='Chiroptera': return 'bat'
            if o in ('Cetacea','Cetartiodactyla') and f in ('Delphinidae','Balaenopteridae','Phocoenidae','Physeteridae','Balaenidae','Monodontidae','Ziphiidae','Eschrichtiidae','Kogiidae','Iniidae','Platanistidae','Pontoporiidae'): return 'whale and dolphin'
            if o=='Cetacea': return 'whale and dolphin'
            if o=='Sirenia': return 'manatee and dugong'
            if o=='Primates': return 'monkey and ape'
            if o=='Carnivora':
                if f in ('Phocidae','Otariidae','Odobenidae'): return 'seal and sea lion'
                return 'raccoon, bear, otter, weasel and other carnivore'
            if o in ('Didelphimorphia','Diprotodontia','Dasyuromorphia','Peramelemorphia','Paucituberculata','Microbiotheria','Notoryctemorphia'): return 'opossum, kangaroo and other marsupial'
            if o in ('Soricomorpha','Eulipotyphla','Erinaceomorpha','Afrosoricida','Macroscelidea','Scandentia'): return 'mole, shrew and hedgehog'
            if o in ('Artiodactyla','Perissodactyla','Cetartiodactyla'): return 'pig, hippo, rhino, tapir and other hoofed mammal'
            if o=='Proboscidea': return 'elephant'
            if o in ('Cingulata','Pilosa','Pholidota','Tubulidentata'): return 'armadillo, sloth, anteater and pangolin'
            if o=='Monotremata': return 'platypus and echidna'
            return 'other mammal'
        if c=='Amphibia': return 'salamander, newt and caecilian'
        if c in FISH_CLASSES or (c=='' and o.endswith('formes')): return 'fish'
        if c in ('Ascidiacea','Thaliacea','Appendicularia','Leptocardii'): return 'sea squirt and lancelet'
        return 'other chordate'
    if p=='Annelida': return 'earthworm, leech and bristle worm'
    if p in ('Platyhelminthes','Nemertea','Nematoda','Nematomorpha','Acanthocephala','Sipuncula','Priapulida','Chaetognatha','Hemichordata','Xenacoelomorpha','Gnathostomulida','Gastrotricha'): return 'flatworm, roundworm and other worm'
    if p=='Cnidaria': return 'jellyfish, coral and anemone'
    if p=='Echinodermata': return 'starfish, urchin and sea cucumber'
    if p=='Porifera': return 'sponge'
    if p in ('Bryozoa','Brachiopoda','Entoprocta','Phoronida'): return 'moss animal and lamp shell'
    if p=='Ctenophora': return 'comb jelly'
    if p in ('Tardigrada','Rotifera','Onychophora'): return 'water bear, rotifer and velvet worm'
    return 'other animal'
