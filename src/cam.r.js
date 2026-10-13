
  // ---------- a name said by the person, matched to a kind of eye
  // Used only where nothing can look at the photo, or to correct a name that came out wrong. In most names of creatures the
  // last word says what the creature is ("fox squirrel", "rat snake", "crane fly", "turkey vulture", "fish crow", "oakworm
  // moth"), so the word of the table that ends last in the name decides. Where two end at the same letter the longer decides
  // ("sea lion" over "lion", "silverfish" over "fish"), then the entry higher in the table. Vultures are among the other birds:
  // the hawk's sharper sight is not established for them. The groups with no view yet are in GROUPS in cam.a.js.
  // Each word is written out whole, with no group of three or more choices inside it: lexWords() below reads the table for the
  // words a slip of the keys is matched against.
  var LEX = [
    ['person', /\b(person|people|humans?|man|woman|men|women|boy|girl|child|children|kids?|bab(y|ies)|me|myself|selfie)\b/],
    // names whose last word belongs to another kind, or names that end in no word of the table
    ['other', /(\bmites?|chiggers?|tardigrades?|water ?bears?|moss ?piglets?|rotifers?|velvet ?worms?|amoebas?|bacteria|microbes?|plankton)\b/],
    ['sealife', /(man[ -]?o'?[ -]?war|sea ?lil(y|ies)|sea ?wasps?|sea ?pens?|shipworms?)\b/],
    ['fungus', /(chicken[ -]?of[ -]?the[ -]?woods|hen[ -]?of[ -]?the[ -]?woods|old[ -]?man[ -]?of[ -]?the[ -]?woods|turkey[ -]?tails?|deer ?moss|reindeer ?moss|dead ?man's ?fingers?|dead ?man's ?foot|jack-?o'?-?lanterns?|destroying ?angels?|shaggy ?manes?|witch's ?butter|slippery ?jacks?|slippery ?jills?|sulphur ?shel(f|ves)|sulfur ?shel(f|ves))\b/],
    ['slime', /(slime ?mou?lds?|\bslimes?|dog ?vomit|wolf's ?milk)\b/],
    ['crab', /(sea ?spiders?|water ?fleas?|pill[ -]?bugs?|sow[ -]?bugs?)\b/],
    ['snail', /(sea ?hares?|sea ?butterfl(y|ies)|sea ?angels?)\b/],
    ['jumper', /(jumping ?spiders?|zebra ?spiders?|peacock ?spiders?)\b/],
    ['scorpion', /(camel ?spiders?|sun ?spiders?|whip ?spiders?)\b/],
    ['spider', /(black ?widows?|brown ?widows?)\b/],
    ['salamander', /(congo ?eels?)\b/],
    ['flyingfox', /(flying[ -]?fox(es)?|fruit ?bats?)\b/],
    ['whale', /(sea ?lions?|sea ?cows?)\b/],
    ['squirrel', /(prairie ?dogs?|guinea ?pigs?)\b/],
    ['primate', /(bush ?bab(y|ies))\b/],
    ['fish', /(sea ?horses?|sea ?robins?|sea ?dragons?)\b/],
    ['reptile', /(slow ?worms?|gila ?monsters?)\b/],
    ['bird', /(nighthawks?|bee-?eaters?|oyster ?catchers?|brown ?creepers?|treecreepers?|wallcreepers?)\b/],
    ['bee', /(velvet ?ants?|cicada ?killers?|cow ?killers?|tarantula ?hawks?|longhorn-?cuckoos?)\b/],
    ['insect', /(silverfish|white ?peacocks?|pondhawks?|monkey ?slugs?|woolly ?bears?|bee-?killers?|inch ?worms?|silk ?worms?|meal ?worms?|glow[ -]?worms?|army ?worms?|cut ?worms?|horn ?worms?|bag ?worms?|web ?worms?|wire ?worms?|canker ?worms?|bud ?worms?|boll ?worms?|ear ?worms?|wood ?worms?|screw ?worms?|root ?worms?|fruit ?worms?|leaf ?worms?)\b/],
    ['plant', /(monkey ?puzzles?|elephant ?ears?|alligator ?flags?|lamb's ?quarters|wood ?anemones?|japanese ?anemones?|madagascar ?periwinkles?|green ?dragons?|wakerobins?|kangaroo ?paws?|crane's-?bills?|spider ?brakes?|rattlesnake ?masters?|greater ?periwinkles?|lesser ?periwinkles?|rosy ?periwinkles?|forget-?me-?nots?|dragon-?tails?|black ?locusts?|honey ?locusts?|devil's ?walking-?sticks?|'s[ -]?foot|'s[ -]?feet|'s[ -]?ears?|'s[ -]?tails?|'s[ -]?tongues?|'s[ -]?claws?|'s[ -]?beards?|'s[ -]?feathers?|'s[ -]?seals?)\b/],
    // the groups with no view yet
    ['worm', /(\bworms?|earthworms?|flatworms?|roundworms?|tapeworms?|hookworms?|lugworms?|ragworms?|bloodworms?|fireworms?|tubeworms?|\bleech(es)?|nematodes?|planarians?|millipedes?|centipedes?|polychaetes?|feather ?dusters?)\b/],
    ['flyingfox', /(megabats?)\b/],
    ['shark', /(sharks?|hammerheads?|\brays?|stingrays?|mantas?|sawfish|guitarfish|dogfish|ratfish|chimaeras?|\bskates?)\b/],
    ['bat', /(\bbats?|microbats?|myotis)\b/],
    ['cephalopod', /(octopus(es)?|octopi|squids?|cuttlefish|nautilus(es)?|argonauts?|cephalopods?)\b/],
    ['sealife', /(starfish|sea ?stars?|brittle ?stars?|feather ?stars?|basket ?stars?|corals?|anemones?|jellyfish|comb ?jell(y|ies)|moon ?jell(y|ies)|box ?jell(y|ies)|sea ?urchins?|urchins?|sea ?cucumbers?|sand ?dollars?|sea ?biscuits?|\bclams?|mussels?|oysters?|scallops?|cockles?|quahogs?|geoducks?|sponges?|sea ?squirts?|tunicates?|\bsalps?|sea ?fans?|hydroids?|\bhydras?|siphonophores?|bryozoans?|lamp ?shells?|brachiopods?|crinoids?)\b/],
    ['crab', /(crabs?|crayfish|crawfish|crawdads?|lobsters?|shrimps?|prawns?|krill|barnacles?|woodlice|woodlouse|roly[ -]?pol(y|ies)|isopods?|amphipods?|copepods?)\b/],
    ['snail', /(snails?|slugs?|whelks?|conch(es)?|conchs|nudibranchs?|limpets?|periwinkles?|chitons?|abalones?|cowr(y|ie)s?|murex(es)?|ramshorns?|tusk ?shells?)\b/],
    ['jumper', /(\bjumpers?|salticids?)\b/],
    ['scorpion', /(scorpions?|harvestm(a|e)n|daddy[ -]?long[ -]?legs|vinegaroons?|amblypygids?|solifugids?|solifugae)\b/],
    ['spider', /(spiders?|tarantulas?|orb[ -]?weavers?|recluses?|huntsm(a|e)n|funnel-?webs?|sheet ?weavers?|sheetweavers?|hacklemesh ?weavers?|funnel ?weavers?|cobweb ?weavers?|micrathenas?)\b/],
    ['tick', /(\bticks?)\b/],
    ['slime', /(myxomycetes?)\b/],
    ['fungus', /(mushrooms?|toadstools?|fung(us|i)|lichens?|\bmou?lds?|mildews?|puffballs?|morels?|chanterelles?|boletes?|polypores?|stinkhorns?|truffles?|earthstars?|earthballs?|agarics?|amanitas?|russulas?|\bbrackets?|parasols?|inkcaps?|ink ?caps?|milkcaps?|milk ?caps?|waxcaps?|waxy ?caps?|webcaps?|fibrecaps?|fibercaps?|\brusts?|rustgills?|sawgills?|mazegills?|brittlegills?|rosegills?|splitgills?|dapperlings?|lepidellas?|deceivers?|shii?takes?|suillus|reishis?|candlesnuffs?|xylarias?|trametes|oysterlings?|\bcrusts?|matsutakes?|grisettes?|brittlestems?|fieldcaps?|elfcups?|pinwheels?|earthtongues?)\b/],
    ['salamander', /(salamanders?|\bnewts?|axolotls?|mudpupp(y|ies)|waterdogs?|amphiumas?|hellbenders?|\bsirens?|\bolms?|caecilians?|\befts?)\b/],
    ['whale', /(whales?|dolphins?|porpoises?|orcas?|\bseals?|walrus(es)?|manatees?|dugongs?|narwhals?|belugas?|humpbacks?|pinnipeds?|cetaceans?)\b/],
    ['primate', /(monkeys?|\bapes?|gorillas?|chimps?|chimpanzees?|orangutans?|bonobos?|gibbons?|baboons?|macaques?|lemurs?|marmosets?|tamarins?|capuchins?|loris(es)?|langurs?|colobus(es)?|mandrills?|tarsiers?|galagos?|howlers?|aye-?ayes?|sifakas?|primates?)\b/],
    ['mammal', /(raccoons?|opossums?|possums?|armadillos?|\bbears?|\botters?|weasels?|\bminks?|ferrets?|stoats?|ermines?|polecats?|\bfishers?|skunks?|badgers?|wolverines?|martens?|\bpigs?|\bhogs?|boars?|warthogs?|peccar(y|ies)|javelinas?|hippos?|hippopotamus(es)?|rhinos?|rhinoceros(es)?|tapirs?|kangaroos?|wallab(y|ies)|koalas?|wombats?|quokkas?|quolls?|bandicoots?|bilb(y|ies)|numbats?|tasmanian ?devils?|sugar ?gliders?|hedgehogs?|\bmoles?|shrews?|tenrecs?|sloths?|anteaters?|pangolins?|aardvarks?|aardwol(f|ves)|elephants?|platypus(es)?|echidnas?|hyrax(es)?|mongooses?|meerkats?|hyenas?|civets?|genets?|binturongs?|fossas?|coatis?|coatimundis?|kinkajous?|\bringtails?|pandas?|mammals?)\b/],
    ['fish', /(fish(es)?|\beels?|minnows?|\bbass|trout|salmon|\bcarps?|bluegills?|perch(es)?|gupp(y|ies)|gob(y|ies)|wrasses?|tunas?|\bcods?|herrings?|sardines?|anchov(y|ies)|\bpikes?|pickerels?|muskies|muskellunges?|walleyes?|\bgars?|mullets?|snappers?|groupers?|snooks?|tarpons?|bowfins?|sturgeons?|\bshads?|menhadens?|sheepshead|lampreys?|piranhas?|barracudas?|marlins?|mackerels?|halibuts?|flounders?|\bkoi|bettas?|tetras?|cichlids?|tilapias?|blenn(y|ies)|sculpins?|sticklebacks?|\bbarbs?|loach(es)?|darters?|shiners?|crappies?|morays?|madtoms?|bullheads?|silversides?|warmouths?|hogchokers?|chubsuckers?|mudskippers?|snakeheads?)\b/],
    // the kinds with views
    ['bee', /(bees?|wasps?|hornets?|yellowjackets?|yellow ?jackets?|daubers?|beewol(f|ves)|ichneumons?|sawfl(y|ies)|horntails?|leaf-?cutters?)\b/],
    ['insect', /(butterfl(y|ies)|\bmoths?|hawkmoths?|silkmoths?|sphinx(es)?|beetles?|scarabs?|chafers?|borers?|sawyers?|engravers?|clerids?|weevils?|curculios?|fl(y|ies)|\bants?|antlions?|crickets?|cicadas?|mantis(es)?|mantids?|bugs?|ladybirds?|assassins?|skippers?|monarchs?|fritillar(y|ies)|swallowtails?|longwings?|birdwings?|hairstreaks?|satyrs?|wood-?nymphs?|leafwings?|clearwings?|daggers?|veneers?|hooktips?|leaftiers?|leaf ?tiers?|buckeyes?|clubtails?|darners?|cruisers?|spreadwings?|forktails?|sprites?|katydids?|coneheads?|locusts?|wetas?|lubbers?|roach(es)?|aphids?|psyllids?|mirids?|phylloxeras?|sharpshooters?|\bscales?|gallmakers?|\bkeds?|thrips|caterpillars?|loopers?|spanworms?|grubs?|maggots?|chrysalis(es)?|mosquito(es)?|gnats?|midges?|fleas?|\blice|\blouse|termites?|walkingsticks?|walking ?sticks?|earwigs?|hoppers?|lacewings?|hellgrammites?|springtails?|leaf ?miners?|leafminers?|insects?)\b/],
    ['frog', /(frogs?|toads?|peepers?|tadpoles?|polliwogs?)\b/],
    ['alligator', /\b(alligators?|gators?|crocodiles?|crocs?|caimans?|gharials?|gavials?)\b/],
    ['reptile', /(lizards?|anoles?|geckos?|skinks?|snakes?|\bracers?|turtles?|tortoises?|terrapins?|sliders?|cooters?|softshells?|loggerheads?|leatherbacks?|hawksbills?|ridleys?|iguanas?|chameleons?|\bdragons?|agamas?|basilisks?|tuataras?|reptiles?|cottonmouths?|moccasins?|copperheads?|rattlers?|hognoses?|pythons?|\bboas?|anacondas?|vipers?|\badders?|cobras?|mambas?|kraits?|taipans?)\b/],
    ['squirrel', /(squirrels?|chipmunks?|\brats?|\bmice|\bmouse|dormouse|dormice|\bvoles?|gophers?|beavers?|porcupines?|capybaras?|hamsters?|gerbils?|chinchillas?|groundhogs?|woodchucks?|marmots?|muskrats?|woodrats?|nutrias?|coypus?|agoutis?|\bpacas?|lemmings?|jerboas?|rodents?)\b/],
    ['bird', /(vultures?|condors?)\b/],
    ['hawk', /(hawks?|eagles?|falcons?|\bkites?|ospreys?|kestrels?|harriers?|buzzards?|caracaras?|merlins?)\b/],
    ['wader', /\b(herons?|egrets?|ibis(es)?|storks?|cranes?|limpkins?|coots?|moorhens?|gallinules?|rails?|crakes?|soras?|jacanas?|shoebills?|pigeons?|doves?|chickens?|roosters?|hens?|turkeys?|pheasants?|quails?|bobwhites?|grouse|partridges?|ptarmigans?|guineafowl|guinea ?fowl|peacocks?|peafowl|peahens?|junglefowl|fowls?|bitterns?|spoonbills?)\b/],
    ['bird', /(birds?|\bducks?|\bgeese|\bgoose|\bswans?|waterfowl|gulls?|\bterns?|pelicans?|cormorants?|anhingas?|cardinals?|warblers?|sparrows?|\bwrens?|\bjays?|\bcrows?|ravens?|\brooks?|jackdaws?|magpies?|robins?|finch(es)?|siskins?|canar(y|ies)|grosbeaks?|juncos?|phoebes?|pewees?|kingbirds?|grackles?|woodpeckers?|flickers?|\bswallows?|\bswifts?|\bowls?|parrots?|parakeets?|macaws?|cockatoos?|cockatiels?|lorikeets?|budgies?|budgerigars?|starlings?|mynas?|mynahs?|bulbuls?|thrush(es)?|thrashers?|vireos?|titmouse|titmice|\btits?|chickadees?|nuthatch(es)?|orioles?|tanagers?|flycatchers?|kingfishers?|kookaburras?|hoopoes?|hornbills?|toucans?|trogons?|quetzals?|motmots?|cuckoos?|roadrunners?|nightjars?|\bloons?|grebes?|penguins?|puffins?|albatross(es)?|petrels?|shearwaters?|gannets?|\bboob(y|ies)|skuas?|flamingos?|flamingoes|sandpipers?|plovers?|killdeers?|avocets?|stilts?|curlews?|godwits?|turnstones?|willets?|yellowlegs|dowitchers?|oystercatchers?|shrikes?|gnatcatchers?|sapsuckers?|towhees?|waxwings?|kinglets?|buntings?|meadowlarks?|\blarks?|wagtails?|pipits?|redstarts?|nightingales?|babblers?|weavers?|honeyeaters?|mallards?|\bteals?|wigeons?|mergansers?|\bscaups?|eiders?|ostrich(es)?|\bemus?|cassowar(y|ies)|kiwis?|\brheas?|bustards?)\b/],
    ['cat', /\b(cats?|kittens?|kitty|kitties|bobcats?|wildcats?|lynx|panthers?|cougars?|pumas?|lions?|tigers?|leopards?|cheetahs?|ocelots?|jaguars?|servals?|caracals?|margays?)\b/],
    ['dog', /\b(dogs?|pupp(y|ies)|fox(es)?|coyotes?|wol(f|ves)|jackals?|dingos?|dingoes|fennecs?|dholes?)\b/],
    ['deer', /\b(deer|reindeer|caribou|fawns?|bucks?|does?|stags?|horses?|pon(y|ies)|cows?|cattle|bulls?|ox|oxen|cal(f|ves)|goats?|sheep|lambs?|elk|moose|bison|buffalo(es)?|yaks?|donkeys?|mules?|zebras?|giraffes?|okapis?|camels?|llamas?|alpacas?|guanacos?|vicunas?|antelopes?|gazelles?|impalas?|kudus?|elands?|oryx(es)?|springboks?|gemsboks?|gnus?|wildebeests?|hartebeests?|duikers?|waterbucks?|dik-?diks?|muntjacs?|chamois|pronghorns?|bighorns?|ibex(es)?)\b/],
    ['rabbit', /\b(rabbits?|bunn(y|ies)|hares?|cottontails?|pikas?)\b/],
    ['plant', /(plants?|trees?|flowers?|\bmoss(es)?|ferns?|grass(es)?|\bvines?|shrubs?|bush(es)?|weeds?|palms?|palmettos?|\boaks?|\bpines?|magnolias?|sweetgums?|maples?|cypress|cedars?|holl(y|ies)|azaleas?|camellias?|berr(y|ies)|worts?|lil(y|ies)|roses?|orchids?|cactus|cacti|succulents?|\biv(y|ies)|creepers?|sumacs?|indigo|catbrier|greenbrier|catnip|cattails?|grapes?|apples?|plums?|\bpeas?|peanuts?|beans?|fruits?|chestnuts?|ardisia|beggarticks|bidens|lea(f|ves)|\bherbs?|basil|fennels?|tomato(es)?|\bmints?|\bsages?|balms?|blossoms?|seedlings?|saplings?|dais(y|ies)|clover|trefoils?|sorrels?|catchfl(y|ies)|sphagnum|bamboo|lantana|hibiscus|honeysuckles?|bromeliads?|tillandsia|dandelions?|thistles?|nettles?|tulips?|daffodils?|popp(y|ies)|lotus(es)?|agaves?|aloes?|yuccas?|eucalyptus|acacias?|baobabs?|birch(es)?|willows?|\belms?|beech(es)?|spruces?|\bfirs?|sequoias?|junipers?|mangroves?|lavender|\breeds?|sedges?|rushes|horsetails?|foxtails?|tickseeds?|frogfruits?|vincas?|\bfigs?|bananas?|wood|seaweeds?|kelp|alga(e)?)\b/]
  ];

  // global copies of the table's patterns, for finding every match in a name
  var LEXG = null;
  function kindOfName(text) {
    var t = String(text || '').toLowerCase().replace(/[‘’ʼ]/g, '\'').replace(/[^a-z' -]+/g, ' '), best = '', end = -1, len = 0, m, e;   // a phone's curly apostrophe is a plain one
    if (!LEXG) LEXG = LEX.map(function (L) { return new RegExp(L[1].source, 'g'); });
    for (var i = 0; i < LEX.length; i++) {
      LEXG[i].lastIndex = 0;
      while ((m = LEXG[i].exec(t))) {
        e = m.index + m[0].length;
        if (e > end || (e === end && m[0].length > len)) { best = LEX[i][0]; end = e; len = m[0].length; }
        if (!m[0].length) LEXG[i].lastIndex++;
      }
    }
    return best;                                   // '' where no word in it is a kind this page knows
  }

  // The words of the table, one plain form each, for catching a slip of the keys ("herron"). Made once from the patterns above.
  var LEXW = null;
  function lexWords() {
    if (LEXW) return LEXW; LEXW = [];
    LEX.forEach(function (L) {
      if (L[0] === 'person') return;
      L[1].source.replace(/\\b/g, '').replace(/^\(/, '').replace(/\)$/, '').replace(/\((\w+)\|\w+\)\??/g, '$1').replace(/\(\w+\)\?/g, '').replace(/(\w)\?/g, function (a, ch) { return ch === 's' ? '' : ch; })
        .split('|').forEach(function (w) { if (/^[a-z]{3,}$/.test(w)) LEXW.push([w, L[0]]); });
    });
    return LEXW;
  }
  function nearWords(text) {                       // kinds whose word is a slip of the keys from a word that was typed
    var out = [], seen = {};
    plain(text).split(' ').forEach(function (t) {
      if (t.length < 3) return; var lim = t.length <= 5 ? 1 : 2;
      lexWords().forEach(function (w) { if (!seen[w[0]] && Math.abs(w[0].length - t.length) <= lim && slips(t, w[0], lim) <= lim) { seen[w[0]] = 1; out.push({ en: w[0], sci: '', kind: w[1] }); } });
    });
    return out.slice(0, 3);
  }

  // ---------- the record: everyone met so far, and the eyes that came with them
  // Kept in this browser, and beside it in the viewer's own private part of the artifact's store, where one is offered.
  var KINDS = ['cat', 'dog', 'squirrel', 'deer', 'rabbit', 'hawk', 'wader', 'bird', 'alligator', 'reptile', 'frog', 'bee', 'insect', 'plant'];
  var REC_KEY = 'seenback.record.v1', remote = null, diagDoc = null, diagLog = [], diagP = Promise.resolve();
  // A short trace of how recognition went, kept in the viewer's own private part of the store, so a fault on a phone can be read afterwards.
  function diag(what, code) {
    diagLog.push({ at: Date.now(), what: what, code: code || '', build: BUILD, framed: framed, sample: !!sample, images: !!canImages, src: S.src, camRefused: !!S.camRefused,
      ua: String(navigator.userAgent || '').slice(0, 180), w: window.innerWidth, h: window.innerHeight });
    diagLog = diagLog.slice(-12);
    if (!diagDoc) return;
    var ref = diagDoc, log = diagLog.slice();
    diagP = diagP.then(function () { return ref.set({ log: log }); }).catch(function () {});
  }
  var framed = (function () { try { return window.self !== window.top; } catch (e) { return true; } })();
  // who gave the name: Claude, this page's small model, the full database on a server, the full database on this device, or the person
  function byOf(by) { return by === 'Claude' || by === 'page' || by === 'service' || by === 'device-large' ? by : 'you'; }
  function cleanMeeting(v, id) {
    if (!v || typeof v !== 'object') return null;
    var key = String(v.key || ''), mid = String(id || v.id || '');
    if (!EYES[key] || key === 'person' || !/^[A-Za-z0-9_-]{4,40}$/.test(mid)) return null;
    var thumb = typeof v.thumb === 'string' && v.thumb.length < 24000 && /^data:image\/jpeg;base64,[A-Za-z0-9+\/=]+$/.test(v.thumb) ? v.thumb : '';
    if (typeof v.common === 'string' && !v.sci && (v.common.toLowerCase() === handName(key).toLowerCase() || /^(a person|something alive)$/i.test(v.common))) v.common = v.common.toLowerCase();   // a group's name kept from an older build loses its capital
    if (typeof v.common === 'string' && v.sci) v.common = nameCase(v.common);   // a species' name kept from an older build is set in lower case, proper names apart
    return { id: mid, key: key, common: clip(v.common, 60) || handName(key), sci: clip(v.sci, 80), by: byOf(v.by), at: +v.at || 0, thumb: thumb, up: v.up ? 1 : 0, loc: v.loc ? 1 : 0 };
  }
  function loadLocal() {
    try { var a = JSON.parse(localStorage.getItem(REC_KEY) || '[]'); return Array.isArray(a) ? a.map(function (v) { return cleanMeeting(v); }).filter(Boolean) : []; }
    catch (e) { return []; }
  }
  var record = loadLocal();
  function saveLocal() {
    try { localStorage.setItem(REC_KEY, JSON.stringify(record.slice(0, 300).map(function (m) { return { id: m.id, key: m.key, common: m.common, sci: m.sci, by: m.by, at: m.at, thumb: m.thumb, up: m.up, loc: m.loc }; }))); } catch (e) {}
  }
  function pushUp(m) {                             // one write at a time for each meeting
    if (!remote) return;
    var col = remote;
    m._p = (m._p || Promise.resolve()).then(function () {
      return col.doc(m.id).set({ key: m.key, common: m.common, sci: m.sci, by: m.by, at: m.at, thumb: m.thumb, loc: m.loc ? 1 : 0 });
    }).then(function () { m.up = 1; saveLocal(); }, function () {});
  }
  function thumbOf(c) {
    var t = makeCanvas(96, 96), x = t.getContext('2d'), k = Math.max(96 / c.width, 96 / c.height);
    x.imageSmoothingQuality = 'high'; x.drawImage(c, (96 - c.width * k) / 2, (96 - c.height * k) / 2, c.width * k, c.height * k);
    try { return t.toDataURL('image/jpeg', .72); } catch (e) { return ''; }
  }
  function noteMeeting(key, named) {               // a photo has its name: keep the meeting, or correct the one already kept for this photo
    S.nov = '';
    if (key === 'person') return;
    var same = function (r) { return r.id !== S.meetingId; }, nm = named.common.toLowerCase();
    S.nov = KINDS.indexOf(key) >= 0 && !record.some(function (r) { return same(r) && r.key === key; }) ? 'kind'
      : !record.some(function (r) { return same(r) && r.common.toLowerCase() === nm; }) ? 'name' : 'again';
    var m = S.meetingId ? record.filter(function (r) { return r.id === S.meetingId; })[0] : null;
    if (!m) {
      m = { id: 'm' + Date.now().toString(36) + Math.floor(Math.random() * 1e9).toString(36), at: Date.now(), thumb: S.animalPhoto ? thumbOf(S.animalPhoto) : '', up: 0 };
      record.unshift(m); S.meetingId = m.id;
    }
    m.key = key; m.common = named.common; m.sci = named.scientific || ''; m.by = byOf(named.by);
    m.loc = named.local ? 1 : 0;                   // the species was chosen from the list of one place
    // the full database's place (placeOf in cam.rec.js) learns from a creature it named with confidence; a name corrected later is taken back
    if (typeof large !== 'undefined' && large.met) large.met(m.id, m.by === 'device-large' ? m.sci : '');
    saveLocal(); pushUp(m); paintRecordBits();
  }
  function forgetMeeting(id) {
    record = record.filter(function (m) { return m.id !== id; });
    if (S.meetingId === id) S.meetingId = null;
    saveLocal(); if (remote) remote.doc(id).delete().catch(function () {});
    paintRecordBits(); renderRecord();
  }
  function initRemote() {
    Promise.all([window.claude.use('db'), window.claude.use('user')]).then(function (r) {
      var db = r[0], user = r[1]; if (!db || !user) return;
      return user.id().then(function (uid) {
        if (!uid) return;
        var col = db.doc('data/users/' + uid + '/record').collection('met');
        return col.orderBy('at', 'desc').limit(300).get().then(function (qs) {
          var there = {}, here = {};
          qs.docs.forEach(function (d) { there[d.id] = d; });
          // what was sent up before and is gone from the store was forgotten on another device
          record = record.filter(function (m) { return !(m.up && !there[m.id]); });
          record.forEach(function (m) { here[m.id] = 1; if (there[m.id]) m.up = 1; });
          qs.docs.forEach(function (d) { if (here[d.id]) return; var m = cleanMeeting(d.data(), d.id); if (m) { m.up = 1; record.push(m); } });
          record.sort(function (a, b) { return b.at - a.at; });
          remote = col; diagDoc = db.doc('data/users/' + uid + '/diag'); saveLocal(); paintRecordBits(); if (!$('record').hidden) renderRecord();
          record.filter(function (m) { return !m.up; }).slice(0, 40).forEach(pushUp);
        });
      });
    }).catch(function () {});
  }

  // ---------- the Gainesville list
  var G60_BY = (function () {
    var o = {}; G60.forEach(function (r, i) { o[r[1].toLowerCase()] = i + 1; o[r[2].toLowerCase()] = i + 1; });
    Object.keys(G60_ALIAS).forEach(function (k) { o[k] = G60_ALIAS[k]; }); return o;
  })();
  function g60Of(m) {
    var sci = (m.sci || '').toLowerCase().split(/\s+/).slice(0, 2).join(' ');
    return G60_BY[sci] || G60_BY[(m.common || '').toLowerCase().trim()] || 0;
  }

  // ---------- the record, drawn
  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text !== undefined) e.textContent = text; return e; }
  function svgEl(tag, attrs) { var e = document.createElementNS('http://www.w3.org/2000/svg', tag); for (var k in attrs) e.setAttribute(k, attrs[k]); return e; }
  function eyeGlyph(key, on) {                     // an iris, and once met, the pupil that kind of eye has
    var s = svgEl('svg', { viewBox: '0 0 24 24', 'aria-hidden': 'true' }), p = EYES[key].pupil;
    s.appendChild(svgEl('circle', { cx: 12, cy: 12, r: 9.6, 'class': 'iris' }));
    if (!on) return s;
    if (p === 'v') s.appendChild(svgEl('ellipse', { cx: 12, cy: 12, rx: 1.7, ry: 7.2, 'class': 'pupil' }));
    else if (p === 'h') s.appendChild(svgEl('rect', { x: 5.2, y: 9.7, width: 13.6, height: 4.6, rx: 2.2, 'class': 'pupil' }));
    else if (p === 'o') s.appendChild(svgEl('circle', { cx: 12, cy: 12, r: 3.7, 'class': 'pupil' }));
    else if (key === 'bee' || key === 'insect') s.appendChild(svgEl('path', { d: 'M12 6.6l4.7 2.7v5.4L12 17.4l-4.7-2.7V9.3z', 'class': 'pupil' }));
    else s.appendChild(svgEl('circle', { cx: 12, cy: 12, r: 1.3, 'class': 'pupil' }));
    return s;
  }
  // The rule of the finding game: eyes are lent for a week from a meeting, and then go back. The record of the meeting stays for good.
  // To see as a heron again after the week, a heron has to be met again. A meeting whose time lies ahead of this clock counts as just made.
  var LEND_MS = 7 * 864e5;
  function lentLeft(m) { return m ? LEND_MS - Math.max(0, Date.now() - m.at) : 0; }
  function lent(m) { return lentLeft(m) > 0; }
  function lentSays(m) {
    var ms = lentLeft(m), d;
    if (ms <= 0) return 'This creature’s view has disappeared';
    d = Math.ceil(ms / 864e5);
    return ms <= 36e5 ? 'This is the last hour with this creature’s view' : ms <= 864e5 ? 'This is the last day with this creature’s view' : d >= 7 ? 'This creature’s view is yours for a week' : 'This creature’s view is yours for ' + d + ' more days';
  }
  function lentLine(m) {                           // the same, in a few words, for the moment of meeting and of looking again
    var ms = lentLeft(m), d = Math.ceil(ms / 864e5);
    return ms <= 0 ? '' : d >= 7 ? 'You can now see the world through this creature\u2019s eyes for a week.' : ms <= 864e5 ? 'The last day' : d + ' days left';
  }
  function ringOf(m, cls) {                        // a ring that empties over the week
    var f = Math.max(0, Math.min(1, lentLeft(m) / LEND_MS)), r = 6, c = 2 * Math.PI * r, s = svgEl('svg', { viewBox: '0 0 16 16', 'aria-hidden': 'true' });
    s.appendChild(svgEl('circle', { cx: 8, cy: 8, r: r, 'class': 'rest' }));
    s.appendChild(svgEl('circle', { cx: 8, cy: 8, r: r, 'class': 'left', 'stroke-dasharray': (c * f).toFixed(2) + ' ' + c.toFixed(2), transform: 'rotate(-90 8 8)' }));
    return s;
  }
  function latestOf(key) { for (var i = 0; i < record.length; i++) if (record[i].key === key) return record[i]; return null; }
  function paintRecordBits() {
    var t = 'Encounters' + (record.length ? ': ' + record.length : ''), n = record.length ? String(record.length) : '';
    $('introRecN').textContent = n; $('recAskAnimalN').textContent = n; $('introRec').setAttribute('aria-label', t); $('recAskAnimal').setAttribute('aria-label', t);
  }
  function renderRecord() {
    var met = {}, once = {}, n = record.length, k = 0, have = {};
    record.forEach(function (m) { if (KINDS.indexOf(m.key) >= 0) { once[m.key] = 1; if (lent(m)) met[m.key] = 1; } var g = g60Of(m); if (g) have[g] = 1; });
    KINDS.forEach(function (key) { if (met[key]) k++; });
    $('recordSub').textContent = '';
    var strip = $('eyeStrip'); strip.textContent = '';
    KINDS.forEach(function (key) {
      var b = el('button', 'eye'); b.type = 'button'; b.disabled = !met[key];
      b.setAttribute('aria-label', met[key] ? 'Look as ' + EYES[key].who : once[key] ? 'A creature you’ve already viewed the world as' : 'A creature you haven’t met yet');
      var g = eyeGlyph(key, !!once[key]), lm = latestOf(key), f, c = 2 * Math.PI * 11;   // a kind met once keeps its pupil, dimmed when This creature’s view has disappeared
      if (met[key]) { f = Math.max(.02, lentLeft(lm) / LEND_MS); g.appendChild(svgEl('circle', { cx: 12, cy: 12, r: 11, 'class': 'loan', 'stroke-dasharray': (c * f).toFixed(2) + ' ' + c.toFixed(2), transform: 'rotate(-90 12 12)' })); }
      b.appendChild(g);                                    // the outer ring is the week, emptying
      if (met[key]) b.addEventListener('click', function () { lookAgain(latestOf(key)); });
      strip.appendChild(b);
    });
    var ul = $('metList'); ul.textContent = '';
    record.slice(0, 150).forEach(function (m) {
      var li = el('li'), th, tx = el('div'), look = el('button', 'ico sm'), x = el('button', 'x', '×');
      if (m.thumb) { th = el('img', 'th'); th.alt = ''; th.src = m.thumb; } else th = el('span', 'th');
      tx.appendChild(el('span', 'nm', m.common));
      // what the eye reads is the name, the scientific name and the date; who named it and how long the eyes remain are said to a screen reader in words,
      // and shown as a ring with the days left
      var sm = el('span', 'sm', [m.sci, labelDate(new Date(m.at))].filter(Boolean).join(' · ')), days = el('span', 'days'), dl = Math.ceil(lentLeft(m) / 864e5);
      sm.appendChild(el('span', 'vh', ' · ' + [m.by === 'Claude' ? 'recognized by Claude' : m.by === 'page' ? 'named by this app' : m.by === 'service' ? 'named by the full database on a server' : m.by === 'device-large' ? 'named on this device by the full database' : '', lentSays(m)].filter(Boolean).join(' · ')));
      tx.appendChild(sm); days.appendChild(ringOf(m)); days.appendChild(document.createTextNode(dl + 'd')); days.setAttribute('aria-hidden', 'true');
      if (!lent(m)) li.className = 'gone';
      look.type = 'button'; look.setAttribute('aria-label', 'Look as ' + m.common);
      var sv = svgEl('svg', { viewBox: '0 0 24 24' }); sv.appendChild(svgEl('path', { d: 'M2.5 12s3.5-6.5 9.5-6.5S21.5 12 21.5 12s-3.5 6.5-9.5 6.5S2.5 12 2.5 12z' })); sv.appendChild(svgEl('circle', { cx: 12, cy: 12, r: 2.8 })); look.appendChild(sv);
      look.addEventListener('click', function () { lookAgain(m); });
      x.type = 'button'; x.setAttribute('aria-label', 'Forget the encounter with ' + m.common);
      x.addEventListener('click', function () {
        var yes = el('button', 'mini', 'Forget'), no = el('button', 'mini', 'Keep');
        yes.type = no.type = 'button'; li.textContent = ''; li.className = 'ask';
        li.appendChild(el('span', 'q', 'Forget the encounter with ' + m.common + '?')); li.appendChild(yes); li.appendChild(no);
        yes.addEventListener('click', function () { forgetMeeting(m.id); });
        no.addEventListener('click', renderRecord);
      });
      li.appendChild(th); li.appendChild(tx); if (lent(m) && !noViewOrPerson(m.key)) { li.appendChild(days); li.appendChild(look); } li.appendChild(x); ul.appendChild(li);   // no way to look where the eyes have gone back, or where there were never any
    });
    $('g60Sum').textContent = 'Gainesville’s sixty: ' + Object.keys(have).length + ' met';
    var ol = $('g60List'); ol.textContent = '';
    G60.forEach(function (r, i) { var li = el('li', have[i + 1] ? 'on' : '', have[i + 1] ? r[2] + ', ' + r[0] + ' records' : r[0] + ' records'); ol.appendChild(li); });
  }
  function openRecord() { renderRecord(); bigDelAsked = false; paintBig(); try { $('buildMark').textContent = aboutText(); } catch (e) {} show('claim', false); show('info', false); show('keep', false); openSheet('record'); $('record').scrollTop = 0; }

  // ---------- looking again through eyes already met
  function photoFromThumb(src) {
    return new Promise(function (res) {
      if (!src) { res(null); return; }
      var im = new Image();
      im.onload = function () { var c = makeCanvas(im.naturalWidth || 96, im.naturalHeight || 96); c.getContext('2d').drawImage(im, 0, 0, c.width, c.height); res(c); };
      im.onerror = function () { res(null); };
      im.src = src;
    });
  }
  function blankStill() { var c = makeCanvas(9, 16), x = c.getContext('2d'); x.fillStyle = '#141414'; x.fillRect(0, 0, 9, 16); return c; }
  function openCamera(facing) {                    // resolves with the camera running; rejects where it is refused, missing, or never answers
    if (!hasCamera || S.camRefused) return Promise.reject(new Error('no camera'));
    return new Promise(function (res, rej) {
      var settled = false;
      function no(e) { if (settled) return; settled = true; stopSource(); S.camRefused = true; rej(e || new Error('refused')); }
      if (inViewer && framed) setTimeout(no, 4000);          // a viewer's frame that neither grants nor refuses is treated as a refusal
      startCamera(facing).then(function () { if (settled) { stopSource(); return; } settled = true; S.camOK = true; res(); }, no);
    });
  }
  function lookAgain(m) {
    if (!m || !EYES[m.key] || noViewOrPerson(m.key) || !lent(m)) return;      // encounters kept by older builds with a human or a creature of no group have no view
    var named = { common: m.common, scientific: m.sci, by: m.by, again: m.at, local: !!m.loc };
    closeSheets(); S.seq++; S.token++; if (nameCtl) nameCtl.abort(); hideName(); msg(''); pocket.offers = []; pocket.kindOffers = []; paintSvc();
    if (rec) { recDrop = true; stopRec(); }
    armBack();
    photoFromThumb(m.thumb).then(function (c) {
      S.animalPhoto = c; S.meetingId = m.id; S.nov = '';
      function live() { thaw(); setEyes(m.key, named); go('animal'); showName(); later(startChange, calm ? 150 : 750); }
      function still() { showStill(c || blankStill(), false); setEyes(m.key, named); setViewPrompt(m.key); go('askView'); }
      if (S.src === 'cam') live();
      else if (S.camOK || !(inViewer && framed)) openCamera('environment').then(live, still);
      else still();
    });
  }
