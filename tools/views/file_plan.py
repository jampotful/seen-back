"""Plans the filing of the owner's UNPROCESSED folder by script, so no model has to read the papers to file them.
Usage: python3 -I tools/views/file_plan.py LISTING.tsv PLAN.jsonl [--snippets SNIPPETS.tsv] [--repo .]
LISTING.tsv: one file a line, "key<TAB>size<TAB>file name" (key: anything that names the file to the executor, such as
its Drive id; keep the plan out of the repository when it holds Drive ids). SNIPPETS.tsv (optional): "key<TAB>text" with
the first few hundred characters of a file, from Drive's own content snippet, for files the names cannot place.
Each file gets one action in PLAN.jsonl:
- file: it matches a paper on docs/views/wanted-merged.csv (by a DOI or ISBN in its name, a link fragment, its title,
  or its snippet). "name" is "Surname Year Short title.pdf" (with " (partial)" when the owner marked the paper
  partial) and "folder" the paper's folder (a top-level paper goes to a topic folder named after the views that asked
  for it: Mammals, Reptiles and amphibians, Fish, Plants and fungi, Sea life; the executor creates any that are
  missing); "page_id" is the paper's id on the Papers Wanted page.
- extra: no match, but its title or snippet names a listed animal or a trait word together with an animal; filed under
  "Extras (not on the list)" with a cleaned name, and read by the intake like any paper.
- skip: no match and nothing to do with the views (a journal issue downloaded whole, an editorial, an obituary);
  moved to "Not on the list" and never read.
- duplicate: the same file as another one in the listing (same size and the same name once "(1)" is removed, or the
  same size and the same matched paper); moved to "Duplicates".
- unknown: the name says nothing; fetch its snippet and run again with --snippets.
Prints counts and the papers the owner marked saved that no file in this listing matches."""
import csv, json, os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from papers_page import row as page_row
from traitwords import traits_in

def norm(t): return re.sub(r'[^a-z0-9]+', ' ', (t or '').lower()).strip()
def squash(t): return re.sub(r'[^a-z0-9]', '', (t or '').lower())
STOP = set('the of and in a an on to for with by from at as its their into using under over between during is are be'.split())
JUNK = re.compile(r'^(editorial[- ]board|book[- ]review|obituary|erratum|corrigendum|contents|index)\b', re.I)
ANIMAL = re.compile(r'\b(cats?|dogs?|frogs?|toads?|fish|fishes|goldfish|carp|birds?|owls?|hawks?|pigeons?|chicks?|ducks?|bees?|wasps?|'
                    r'ants?|flies|fly|butterfl\w*|moths?|beetles?|spiders?|squirrels?|deer|horses?|cattle|sheep|goats?|rabbits?|'
                    r'turtles?|lizards?|snakes?|alligators?|crocodil\w*|geckos?|mice|mouse|rats?|bats?|seals?|sea lions?|sharks?|'
                    r'insects?|mammals?|reptiles?|amphibians?|primates?|monkeys?|macaques?|slime|fungi|mushrooms?|plants?|algae)\b', re.I)

TOPIC = [('Mammals', 'deer dog cat bigcat fox horse squirrel rabbit raccoon mammal-groups mammals-met'),
         ('Reptiles and amphibians', 'reptile alligator frog herps herps-met turtle lizard snake'),
         ('Fish', 'fish-shark fish'), ('Plants and fungi', 'plant-fungus-slime plant'), ('Sea life', 'sea-invertebrates')]
def topic(views):
    vs = {v.strip() for v in (views or '').split(',')}
    for name, keys in TOPIC:
        if vs & set(keys.split()): return name
    return ''

def words(t): return [w for w in norm(t).split() if len(w) > 3 and w not in STOP]

def name_title(fname):
    """The title a file name carries, if any: ScienceDirect ("Title-words_1973_Vision-Research.pdf"), Wiley
    ("Journal - 2012 - Author - Title.pdf") or a plain descriptive name."""
    stem = re.sub(r'\s*\(\d+\)\s*$', '', re.sub(r'\.pdf$', '', fname, flags=re.I))
    m = re.match(r'^(.*?)_(\d{4})_', stem)
    if m: return m.group(1).replace('--', ': ').replace('-', ' '), m.group(2)
    if ' - ' in stem:  # Wiley and similar: "Journal - 2012 - Author - Title" or "Title - Author - 1971 - Journal - Site"
        segs = [x.strip() for x in stem.split(' - ')]
        yr = next((x for x in segs if re.fullmatch(r'(1[89]|20)\d\d', x)), '')
        rest = [x for x in segs if x != yr and len(x.split()) > 1 and not re.search(r'online library|nature link|cambridge core|sciencedirect', x, re.I)]
        if rest: return max(rest, key=len), yr
    if ' _ ' in stem: return stem.split(' _ ')[0], ''  # a web page printed to PDF: "Title _ Journal _ Site"
    y = re.search(r'\b(1[89]\d\d|20[0-4]\d)\b', stem)
    return stem.replace('_', ' '), (y.group(1) if y else '')

def surname(authors):
    """First author's surname from "Banks MS, ...", "Anders Ödeen, ..." or "Duarte Toledo R (director: ...)"."""
    first = re.split(r',|;| and | & |\(', (authors or '').strip())[0].strip()
    toks = [t for t in re.split(r'\s+', first) if t]
    if not toks or not toks[0][0].isalpha() or first.lower().startswith(('not ', 'unknown')): return 'Unknown'
    initials = lambda t: re.fullmatch(r'(?:[A-Z]\.?-?){1,3}', t) is not None
    if len(toks) > 1 and initials(toks[-1]): return toks[0]
    if len(toks) > 1 and initials(toks[0]): return toks[-1]
    return toks[-1] if len(toks) > 1 else toks[0]

def short_name(authors, year, title, partial):
    ws = [w for w in re.sub(r'[^\w\s-]', ' ', title or '').split() if w.lower() not in ('a', 'an', 'the')][:6]
    t = ' '.join(ws); t = t[:1].upper() + t[1:]
    return f"{surname(authors)} {year or 'n.d.'} {t}".strip() + (' (partial)' if partial else '') + '.pdf'

def main():
    args = sys.argv[1:]; repo = '.'; snip_path = None
    if '--repo' in args: i = args.index('--repo'); repo = args[i + 1]; del args[i:i + 2]
    if '--snippets' in args: i = args.index('--snippets'); snip_path = args[i + 1]; del args[i:i + 2]
    listing, out = args
    wanted = list(csv.DictReader(open(os.path.join(repo, 'docs/views/wanted-merged.csv'), encoding='utf-8')))
    for r in wanted: r['_id'] = page_row(r)['id']
    marks = {}
    sp = os.path.join(repo, 'docs/views/papers-status.jsonl')
    if os.path.exists(sp):
        for l in open(sp, encoding='utf-8'):
            try: j = json.loads(l); marks[j['id']] = j['status']
            except (ValueError, KeyError): pass
    by_doi = {squash(r['doi']): r for r in wanted if r['doi']}
    suffix = {squash(r['doi'].split('/', 1)[-1]): r for r in wanted if r['doi'] and len(squash(r['doi'].split('/', 1)[-1])) >= 6}
    links = [(squash(r['link']), r) for r in wanted if r['link']]
    isbns = [(re.sub(r'\D', '', r['how to get it'] + ' ' + r['journal or book']), r) for r in wanted]
    snips = {}
    if snip_path:
        for l in open(snip_path, encoding='utf-8'):
            if '\t' in l: k, t = l.rstrip('\n').split('\t', 1); snips[k] = t
    animals = set()
    cp = os.path.join(repo, 'docs/views/gaps/cells.jsonl')
    if os.path.exists(cp):
        for l in open(cp):
            c = json.loads(l); animals.update(x for x in (norm(c['genus']), norm(c.get('en', ''))) if len(x) > 4)

    def by_title(text, year, strict):
        tw = set(words(text)); best, score = None, 0.0
        if len(tw) < 3: return None
        for r in wanted:
            ww = words(r['title'])
            if len(ww) < 3: continue
            inside = sum(1 for w in ww if w in tw) / len(ww)          # the paper's title found in the text
            covered = sum(1 for w in tw if w in set(ww)) / len(tw)   # a truncated file name found in the title
            s = inside if strict else max(inside, covered if len(tw) >= 4 else 0)
            if year and r['year'] and str(r['year']) != str(year): s -= 0.3
            if s > score: best, score = r, s
        return best if score >= 0.8 else None

    def match(key, fname):
        stem = re.sub(r'\s*\(\d+\)\s*$', '', re.sub(r'\.pdf$', '', fname, flags=re.I)); sq = squash(stem)
        if len(sq) >= 6:
            for s, r in suffix.items():
                if sq == s or (len(sq) >= 8 and (sq in s or s in sq)): return r, 'doi in name'
            for l, r in links:
                if len(sq) >= 6 and sq in l: return r, 'link in name'
        raw = stem.lower().strip()
        if len(raw) >= 4:
            for r in wanted:
                hay = (r['link'] + ' ' + r['how to get it']).lower()
                if raw + '.pdf' in hay or hay.endswith('/' + raw): return r, 'name in link'
        digits = re.sub(r'\D', '', stem)
        if len(digits) in (10, 13):
            core = digits[:9] if len(digits) == 10 else digits[3:12]
            for d, r in isbns:
                if core and core in d: return r, 'isbn in name'
        title, year = name_title(fname)
        r = by_title(title, year, strict=False)
        if r: return r, 'title in name'
        spaced = re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', stem).lower()  # "TesisRaulDuarte" -> "tesis raul duarte"
        hits = [r for r in wanted if len(surname(r['authors'])) >= 5 and re.search(r'(?<![a-z])' + re.escape(surname(r['authors']).lower()) + r'(?![a-z])', spaced)
                and (not year or str(r['year']) == str(year))]
        if len(hits) == 1: return hits[0], 'author in name'
        if key in snips:
            t = snips[key]
            for d in re.findall(r'10\.\d{4,9}/[^\s"]+', t):
                if squash(d) in by_doi: return by_doi[squash(d)], 'doi in snippet'
            m = re.search(r'PII:\s*(\S+)', t)
            if m and squash('10.1016/' + m.group(1)) in by_doi: return by_doi[squash('10.1016/' + m.group(1))], 'pii in snippet'
            r = by_title(t[:600], '', strict=True)
            if r: return r, 'title in snippet'
        return None, ''

    files = []
    for l in open(listing, encoding='utf-8'):
        parts = l.rstrip('\n').split('\t')
        if len(parts) >= 3: files.append({'key': parts[0], 'size': parts[1], 'fname': parts[2]})
    plan, seen_name, seen_paper, matched_ids = [], {}, {}, set()
    for f in sorted(files, key=lambda f: (bool(re.search(r'\(\d+\)\.pdf$', f['fname'], re.I)), f['fname'])):
        base = re.sub(r'\s*\(\d+\)(?=\.pdf$)', '', f['fname'], flags=re.I)
        if (f['size'], base) in seen_name:
            plan.append({'key': f['key'], 'action': 'duplicate', 'folder': 'Duplicates', 'of': seen_name[(f['size'], base)], 'was': f['fname']}); continue
        seen_name[(f['size'], base)] = f['fname']
        r, how = match(f['key'], f['fname'])
        if r:
            if (f['size'], r['_id']) in seen_paper:
                plan.append({'key': f['key'], 'action': 'duplicate', 'folder': 'Duplicates', 'of': seen_paper[(f['size'], r['_id'])], 'was': f['fname']}); continue
            seen_paper[(f['size'], r['_id'])] = f['fname']; matched_ids.add(r['_id'])
            folder = r['put in folder'] if r['put in folder'] != 'Regards papers (top level)' else topic(r['views'])
            plan.append({'key': f['key'], 'action': 'file', 'page_id': r['_id'], 'doi': r['doi'], 'how': how, 'was': f['fname'],
                         'name': short_name(r['authors'], r['year'], r['title'], marks.get(r['_id']) == 'partial'), 'folder': folder}); continue
        title, year = name_title(f['fname']); text = (title + ' ' + snips.get(f['key'], '')[:600])
        real = [w for w in words(title) if w.isalpha() and w not in ('main', 'content', 'file', 'viewcontent', 'online', 'download', 'fulltext', 'article')]
        opaque = len(real) < 3 and f['key'] not in snips
        if JUNK.match(title.strip()):
            plan.append({'key': f['key'], 'action': 'skip', 'folder': 'Not on the list', 'was': f['fname'], 'why': 'not a paper'}); continue
        if opaque:
            plan.append({'key': f['key'], 'action': 'unknown', 'was': f['fname']}); continue
        nt = norm(text)
        issue_dump = re.search(r'_(1[89]\d\d|20\d\d)_[A-Za-z-]+\.pdf$', f['fname']) is not None
        if ANIMAL.search(text) or any(' ' + a + ' ' in ' ' + nt + ' ' for a in animals) or (not issue_dump and traits_in(text)):
            plan.append({'key': f['key'], 'action': 'extra', 'folder': 'Extras (not on the list)', 'was': f['fname'],
                         'name': (re.sub(r'\s+', ' ', title).strip()[:90] + (f' ({year})' if year else '') + '.pdf')}); continue
        plan.append({'key': f['key'], 'action': 'skip', 'folder': 'Not on the list', 'was': f['fname'], 'why': 'no listed animal'})
    with open(out, 'w', encoding='utf-8') as fo:
        for p in plan: fo.write(json.dumps(p, ensure_ascii=False) + '\n')
    count = collections.Counter(p['action'] for p in plan)
    print(len(plan), 'files:', ', '.join(f'{k} {v}' for k, v in count.most_common()))
    missing = [r['title'][:70] for r in wanted if marks.get(r['_id']) in ('full', 'partial') and r['_id'] not in matched_ids]
    if missing: print(len(missing), 'papers marked saved with no file in this listing (some may be filed already):', '; '.join(missing[:8]), '...' if len(missing) > 8 else '')

if __name__ == '__main__':
    main()
