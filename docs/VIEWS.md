# Views still to build

Compiled 11 October 2026. The app draws a camera view for sixteen groups of living things. Everything else falls in a seventeenth group called `other`, which has no view yet. This file lists what is in `other`, for the world and for the one region built so far, so that the next views can be chosen by how often people meet each creature.

## Where this list went next (12 October 2026)

`docs/COVERAGE.md` merges the 43 proposed views below into nineteen groups for the base app, which hold all but 0.10% of the records now in `other`, and says what they cost, where their photos come from and how each claim will be measured. The sheets of sensing notes for the first of them (spider, fish, bat, tick and fungus, each checked by a second agent) are in `docs/views/sheets/`. Three of those sheets split a proposed view in two: jumping spiders from other spiders, sharks and rays from other fish, and flying foxes from other bats. The fungus sheet sets slime moulds apart from fungi, and the tick sheet leaves mites out of the tick's view.

## How it was counted

- The world figures are counts of iNaturalist research-grade observations in GBIF (dataset `50c9509d-22c7-4a22-a47d-8c48425ef4a7`), read on 11 October 2026 as facets by order and by family: 169,720,759 records in all. No single observation was fetched. Results are in `runs/fetch/10` and `runs/fetch/11` on the `ci` branch.
- Each order was passed through the app's own rule (`tools/species/eyes.py`). Orders that the rule sends to `other` were then sorted into proposed views by `tools/species/views_todo.py`. The proposed views are a first sorting by Claude and no source stands behind the grouping itself; a view may need splitting once its sheet of notes is written.
- Carnivores and hoofed mammals were split by family, because cats, dogs and grazing animals have views and their relatives do not.
- GBIF gives lizards, snakes, turtles and crocodilians no order, so they are missing from the table of orders; their 4,749,946 records are counted here as having a view.
- Observation counts say what people photograph and upload. They overstate what is easy to photograph and understate what is small, fast, nocturnal or under water.

## The world

Of 169,720,759 records, 150,789,960 (88.8%) fall in a group that has a view and 18,689,811 (11.0%) fall in `other`. The rest could not be placed.

| # | Proposed view | Records | Share of all | Orders | Largest orders |
|---:|---|---:|---:|---:|---|
| 1 | fungus and lichen | 4,768,141 | 2.81% | 186 | Agaricales, Polyporales, Lecanorales, Boletales |
| 2 | spider | 2,927,814 | 1.73% | 1 | Araneae |
| 3 | fish | 2,763,409 | 1.63% | 63 | Perciformes, Cypriniformes, Tetraodontiformes, Scorpaeniformes |
| 4 | snail and slug | 2,013,896 | 1.19% | 20 | Stylommatophora, Nudibranchia, Neogastropoda, Littorinimorpha |
| 5 | crab, crayfish, shrimp and lobster | 743,220 | 0.44% | 1 | Decapoda |
| 6 | salamander, newt and caecilian | 632,992 | 0.37% | 2 | Caudata, Gymnophiona |
| 7 | clam, mussel and scallop | 506,098 | 0.30% | 19 | Venerida, Unionida, Cardiida, Mytilida |
| 8 | woodlouse and small crustacean | 466,981 | 0.28% | 31 | Isopoda, Sessilia, Pedunculata, Amphipoda |
| 9 | raccoon, bear, otter, weasel and other carnivore | 444,045 | 0.26% | 1 | Carnivora |
| 10 | jellyfish, coral and anemone | 411,623 | 0.24% | 20 | Actiniaria, Scleractinia, Semaeostomeae, Anthoathecata |
| 11 | starfish, urchin and sea cucumber | 401,633 | 0.24% | 34 | Forcipulatida, Valvatida, Camarodonta, Holothuriida |
| 12 | opossum, kangaroo and other marsupial | 257,274 | 0.15% | 6 | Diprotodontia, Didelphimorphia, Peramelemorphia, Dasyuromorphia |
| 13 | millipede and centipede | 253,381 | 0.15% | 21 | Polydesmida, Scolopendromorpha, Spirobolida, Julida |
| 14 | monkey and ape | 192,888 | 0.11% | 1 | Primates |
| 15 | seaweed and alga | 168,308 | 0.10% | 71 | Fucales, Laminariales, Dictyotales, Scytosiphonales |
| 16 | tick and mite | 166,591 | 0.10% | 6 | Trombidiformes, Ixodida, Mesostigmata, Sarcoptiformes |
| 17 | seal and sea lion | 153,016 | 0.09% | 1 | Carnivora: Phocidae, Otariidae, Odobenidae |
| 18 | harvestman and other arachnid | 135,765 | 0.08% | 8 | Opiliones, Amblypygi, Uropygi, Pseudoscorpiones |
| 19 | slime mould | 113,223 | 0.07% | 7 | Physarales, Ceratiomyxales, Cribrariales, Trichiales |
| 20 | whale and dolphin | 112,349 | 0.07% | 1 | Cetacea |
| 21 | mole, shrew and hedgehog | 102,447 | 0.06% | 5 | Soricomorpha, Erinaceomorpha, Scandentia, Afrosoricida |
| 22 | scorpion | 99,357 | 0.06% | 1 | Scorpiones |
| 23 | bat | 93,809 | 0.06% | 1 | Chiroptera |
| 24 | pig, hippo, rhino, tapir and other hoofed mammal | 93,205 | 0.05% | 2 | Artiodactyla, Perissodactyla |
| 25 | springtail | 91,432 | 0.05% | 6 | Entomobryomorpha, Symphypleona, Poduromorpha, Diplura |
| 26 | sponge | 72,180 | 0.04% | 28 | Haplosclerida, Poecilosclerida, Verongiida, Dictyoceratida |
| 27 | chiton and other mollusc | 71,469 | 0.04% | 7 | Chitonida, Lepidopleurida, Callochitonida, Dentaliida |
| 28 | octopus, squid and cuttlefish | 60,462 | 0.04% | 9 | Octopoda, Sepiida, Myopsida, Spirulida |
| 29 | armadillo, sloth, anteater and pangolin | 59,430 | 0.04% | 4 | Cingulata, Pilosa, Pholidota, Tubulidentata |
| 30 | microbe, alga or virus | 54,040 | 0.03% | 201 | Cyanobacteriales, Rhizobiales, Peronosporales, Acholeplasmatales |
| 31 | earthworm, leech and bristle worm | 50,227 | 0.03% | 9 | Sabellida, Phyllodocida, Arhynchobdellida, Amphinomida |
| 32 | sea squirt and lancelet | 48,280 | 0.03% | 5 | Stolidobranchia, Aplousobranchia, Phlebobranchia, Pyrosomatida |
| 33 | flatworm, roundworm and other worm | 36,763 | 0.02% | 38 | Tricladida, Rhabditida, Monostilifera, Heteronemertea |
| 34 | elephant | 28,818 | 0.02% | 1 | Proboscidea |
| 35 | platypus and echidna | 23,545 | 0.01% | 1 | Monotremata |
| 36 | horseshoe crab and sea spider | 21,844 | 0.01% | 2 | Xiphosurida, Pantopoda |
| 37 | moss animal and lamp shell | 20,705 | 0.01% | 11 | Cheilostomatida, Plumatellida, Ctenostomatida, Terebratulida |
| 38 | other mammal | 11,201 | 0.01% | 2 | Hyracoidea, Dermoptera |
| 39 | manatee and dugong | 8,750 | 0.01% | 1 | Sirenia |
| 40 | comb jelly | 7,185 | 0.00% | 6 | Cydippida, Lobata, Beroida, Platyctenida |
| 41 | water bear, rotifer and velvet worm | 2,010 | 0.00% | 9 | Ploima, Bdelloidea, Flosculariaceae, Collothecacea |
| 42 | other animal | 4 | 0.00% | 2 | Symbiida, Echinorhagata |
| 43 | other arthropod | 1 | 0.00% | 1 | Mystacocaridida |

Every order with its count and its proposed view is in `docs/views/world-orders.csv` (1136 rows).

## Groups that have a view, and how much each one covers

| Group | Records |
|---|---:|
| plant | 64,187,111 |
| insect | 36,613,620 |
| bird | 30,918,576 |
| bee | 4,555,326 |
| hawk | 2,619,200 |
| frog | 2,055,810 |
| wader | 1,885,092 |
| squirrel | 1,405,835 |
| deer | 1,002,329 |
| rabbit | 335,387 |
| dog | 296,559 |
| cat | 165,169 |
| reptile and alligator | 4,749,946 |

Some of these are broad. `insect` is one view for 28 orders, among them butterflies, beetles, dragonflies and flies. `bee` is the whole order Hymenoptera, so ants and wasps are drawn with a bee's eyes. `bird` covers 38 orders, from owls to ducks to hummingbirds. `squirrel` is every rodent, and `wader` includes pigeons and chickens. Splitting these is a second list of work, separate from the one above.

## Alachua County, Florida

The species list of the one region built so far holds 5,911 species; 983 of them are in `other`. Every one is listed in `docs/views/no-view-us-fl-alachua.csv` with its proposed view.

| Proposed view | Species | Records | Most recorded |
|---|---:|---:|---|
| spider | 161 | 4,660 | Golden Silk Spider, Mabel Orchard Orbweaver, Twin-flagged Jumping Spider |
| fungus and lichen | 599 | 4,483 | Christmas lichen, Ringless Honey Mushroom, Tropical White Polypore |
| snail and slug | 34 | 1,067 | manatee treesnail, Rosy Wolfsnail, Ghost Bulimulus |
| fish | 60 | 1,028 | Eastern Mosquitofish, Bluegill, Florida Bass |
| raccoon, bear, otter, weasel and other carnivore | 4 | 356 | Common Raccoon, North American River Otter, American Black Bear |
| millipede and centipede | 20 | 333 | Greenhouse Millipede, Rusty Millipede, Smokey Oak Millipede |
| bat | 6 | 268 | Mexican Free-tailed Bat, Southeastern Myotis, Tricolored Bat |
| slime mould | 15 | 184 | Common Coral Slime, Dog Vomit Slime Mold, White Carnival Candy Slime Mold |
| woodlouse and small crustacean | 9 | 169 | Common Pill Woodlouse, Florida Fast Woodlouse, Oak Woodlouse |
| tick and mite | 10 | 163 | Lone Star Tick, American Dog Tick, Eastern Black-legged Tick |
| salamander, newt and caecilian | 10 | 148 | Striped Newt, Eastern Newt, Two-toed Amphiuma |
| opossum, kangaroo and other marsupial | 1 | 137 | Virginia Opossum |
| flatworm, roundworm and other worm | 6 | 76 | Wandering Hammerhead Worm, Shovel-headed Garden Worm, Leptonemertes chalicophora |
| harvestman and other arachnid | 5 | 62 | Hadrobunus grandis, Leiobunum bimaculatum, Banded Harvestman |
| pig, hippo, rhino, tapir and other hoofed mammal | 1 | 61 | Eurasian Wild Pig |
| mole, shrew and hedgehog | 3 | 56 | Eastern Mole, Southern Short-tailed Shrew, North American Least Shrew |
| springtail | 12 | 53 | Dicyrtomina ornata, Sminthurus bivittatus, Ptenothrix marmorata |
| scorpion | 1 | 44 | Hentz Striped Scorpion |
| clam, mussel and scallop | 9 | 38 | Asian Clam, Florida Spike, Paper Pondshell |
| crab, crayfish, shrimp and lobster | 8 | 26 | White Tubercled Crayfish, Slough Crayfish, Eastern Grass Shrimp |
| microbe, alga or virus | 4 | 17 | Star Jelly, Hornworm Parasitoid Wasp Bracovirus, Euglena oblonga |
| earthworm, leech and bristle worm | 3 | 5 | Smooth Turtle Leech, Macrobdella ditetra, Placobdella multilineata |
| moss animal and lamp shell | 1 | 4 | Magnificent Bryozoan |
| manatee and dugong | 1 | 2 | West Indian Manatee |

## What the species list itself lacks

- The list is one county. A person anywhere else gets names only from that county's list. Use across the world needs a list for each region, or one world list; the scripts in `tools/species` take a region.
- The list holds wild things recorded on iNaturalist. Dogs, cats, cattle, sheep, horses, chickens, most houseplants and common garden flowers are missing or thin, and they are among the living things people meet most.
- When the app begins to report typed names it has no view for, that tally joins this file as a third table.
