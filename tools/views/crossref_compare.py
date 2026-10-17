"""Compares the evidence logs' source fields with Crossref (ci/crossref, branch run/crossref/<n>) and writes
recheck rows for the two faults the audits find most often: a journal field without a volume, and an author list whose
names differ from Crossref only by accents. Everything else that differs (other author names, year, title) is
listed in the report for an agent or CC to settle.
Usage: python3 -I tools/views/crossref_compare.py CROSSREF.jsonl[.gz] OUT_PREFIX [--n NUMBER]
Writes OUT_PREFIX-report.txt and, with --n, docs/views/recheck/recheck-<NUMBER>.jsonl in the recheck schema
(action "correct", supersedes "<unit>:<line>"); apply it with the usual apply_recheck step."""
import glob, gzip, json, os, re, sys, unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def fold(s):
    return re.sub(r'[^a-z]', '', unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower())


def strip_accents(x):
    return ''.join(c for c in unicodedata.normalize('NFKD', x) if not unicodedata.combining(c))


def initials(given):
    parts = re.split(r'[\s.]+', given.replace('-', ' -').strip())
    out = ''
    for p in parts:
        p = p.lstrip('-')
        if p and p[0].isalpha(): out += p[0].upper()
    return out


def live_ids():
    dead = set()
    for l in open(os.path.join(ROOT, 'docs/views/audit/ALL.jsonl'), encoding='utf-8'):
        try: r = json.loads(l)
        except ValueError: continue
        if r.get('verdict') == 'retract': dead.add(r['id'])
    return dead


def pages(m):
    p = m.get('page') or m.get('article_number') or ''
    return str(p)


def main():
    path, prefix = sys.argv[1], sys.argv[2]
    num = sys.argv[sys.argv.index('--n') + 1] if '--n' in sys.argv else None
    op = gzip.open if path.endswith('.gz') else open
    cr = {}
    for l in op(path, 'rt', encoding='utf-8'):
        try: d = json.loads(l)
        except ValueError: continue
        if 'error' not in d: cr[d['doi']] = d
    dead = live_ids()
    rows, report = [], []
    for f in sorted(glob.glob(os.path.join(ROOT, 'docs/views/evidence/*.jsonl'))):
        unit = os.path.basename(f)[:-6]
        if unit.startswith('recheck-') and not unit.endswith('-fixed'): continue
        for i, l in enumerate(open(f, encoding='utf-8').read().split('\n'), 1):
            if not l.strip(): continue
            try: r = json.loads(l)
            except ValueError: continue
            rid = f'{unit}:{i}'
            if rid in dead: continue
            s = r.get('source') or {}
            m = cr.get(str(s.get('doi', '')).strip().lower())
            if not m: continue
            new = json.loads(json.dumps(s)); why = []
            j = str(s.get('journal', ''))
            if j and not re.search(r'\d', j) and m.get('volume'):
                jn = re.sub(r'\s*\((?:volume|vol\.?)[^)]*unconfirmed\)', '', j).strip()
                add = m['volume'] + (f"({m['issue']})" if m.get('issue') else '') + (f": {pages(m)}" if pages(m) else '')
                new['journal'] = f'{jn} {add}'; why.append(f"journal field had no volume; Crossref gives {add}")
            ca = m.get('authors') or []
            if ca and s.get('authors'):
                logged = [a.strip() for a in re.split(r',\s*', str(s['authors'])) if a.strip()]
                cr_names = [f"{a['family']} {initials(a['given'])}".strip() for a in ca]
                if len(logged) == len(cr_names) and logged != cr_names and all(fold(x.split()[0] if x.split() else x) == fold(y.split()[0] if y.split() else y) for x, y in zip(logged, cr_names)):
                    # same people, differing family-name accents or spellings; take Crossref's family names, keep logged initials
                    fixed = []
                    for x, y in zip(logged, cr_names):
                        xs, ys = x.split(), y.split()
                        fam = xs[0] if (ys[0].isupper() and not xs[0].isupper()) else ys[0]  # Crossref prints some old names in capitals
                        # take the Crossref family name only when removing accents makes the two identical (UPDATE 18b):
                        # a changed apostrophe, hyphen, capital or spacing accent leaves the logged name as it is
                        if strip_accents(fam) != strip_accents(xs[0]) or fam == xs[0]:
                            fam = xs[0]
                        fixed.append(' '.join([fam] + xs[1:]) if len(xs) > 1 else fam)
                    if fixed != logged:
                        new['authors'] = ', '.join(fixed); why.append('family names with their accents as Crossref prints them')
                elif len(logged) != len(cr_names) or [fold(x.split()[0]) for x in logged if x.split()] != [fold(y.split()[0]) for y in cr_names if y.split()]:
                    report.append(f'{rid}\t{s.get("doi")}\tauthors differ\tlogged: {s["authors"]}\tcrossref: {", ".join(cr_names)}')
            if m.get('year') and s.get('year') and int(s['year']) != int(m['year']):
                report.append(f'{rid}\t{s.get("doi")}\tyear logged {s["year"]} crossref {m["year"]}')
            if why and num:
                nr = {k: v for k, v in r.items() if k not in ('rechecked', 'audit')}
                nr['source'] = new
                nr.update({'unit': f'recheck-{num}', 'supersedes': rid, 'action': 'correct',
                           'reason': 'Crossref record (build-machine lookup, run/crossref): ' + '; '.join(why) + '.'})
                rows.append(nr)
            elif why:
                report.append(f'{rid}\t{s.get("doi")}\twould fix: ' + '; '.join(why))
    open(prefix + '-report.txt', 'w', encoding='utf-8').write('\n'.join(report) + '\n')
    if num and rows:
        open(os.path.join(ROOT, f'docs/views/recheck/recheck-{num}.jsonl'), 'w', encoding='utf-8').write(''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in rows))
    print(len(cr), 'Crossref records;', len(rows), 'recheck rows;', len(report), 'lines in the report')


main()
