"""Reads the OpenAlex harvests (.github/workflows/harvest.yml) from the ci branch, for the desk and its agents.
Usage:
  python3 -I tools/views/harvest_get.py Genus [Genus ...]     print what the build machines found for these genera
  python3 -I tools/views/harvest_get.py --next 40 [--skip FILE] the next genera, heaviest first, that a harvest holds
      and that still lack a full-protocol search record (FILE lists genera already handed out, one a line)
  python3 -I tools/views/harvest_get.py --run                  the harvest runs found and their summaries
Every run on the ci branch is read and merged by genus, the newest run winning; a shard stopped by its time limit
still counts. For each genus it prints the protocol's searches already sent (scientific name, English name, trait
groups), the citation step (works citing the nearest measured relative's source that name the genus) and the family
review search, each work with title, year, venue, DOI, open-access status, link and licence, and its abstract's start."""
import json, os, re, subprocess, sys, zlib

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def git(*a, binary=False):
    r = subprocess.run(['git', '-C', ROOT, *a], capture_output=True)
    return r.stdout if binary else r.stdout.decode('utf-8', 'replace')


def load():
    git('fetch', '-q', '--depth', '1', 'origin', '+refs/heads/ci:refs/remotes/origin/ci')
    names = [n for n in git('ls-tree', '-r', '--name-only', 'origin/ci', 'runs/harvest').split() if n.endswith('harvest.jsonl.gz')]
    if not names: sys.exit('No harvest on the ci branch yet. Push a branch run/harvest/<name> to start one.')
    num = lambda n: tuple(int(x) for x in re.findall(r'runs/harvest/(\d+)-(\d+)/', n)[0])
    genera, families, summaries, runs = {}, {}, [], set()
    for n in sorted(names, key=num):
        runs.add(num(n)[0]); base = n.rsplit('/', 1)[0]
        summaries.append(base + ': ' + (git('show', f'origin/ci:{base}/summary.txt').strip() or 'no summary (stopped early)'))
        raw = zlib.decompressobj(16 + zlib.MAX_WBITS).decompress(git('show', 'origin/ci:' + n, binary=True))
        for l in raw.decode('utf-8', 'replace').splitlines():
            try: d = json.loads(l)
            except ValueError: continue  # the last line of a shard that was cut off
            d['run'] = num(n)[0]
            if d.get('type') == 'genus_extra' and d.get('genus') in genera:  # steps added later by a SUPPLEMENT run (ci/harvest/harvest.py)
                g = genera[d['genus']]
                if d.get('family') and not g.get('family'): g['family'] = d['family']; g['family_source'] = d.get('family_source', '')
                if d.get('queries'): g.setdefault('extra', []).append(d)
                continue
            if d.get('type') == 'genus': genera[d['genus']] = d
            elif d.get('type') == 'family':
                # a later run's failed review ("gave up") never hides an earlier run's completed one
                old = families.get(d['family'])
                if not (old and not (old.get('query') or {}).get('error') and (d.get('query') or {}).get('error')): families[d['family']] = d
    qp = os.path.join(ROOT, 'docs/views/gaps/queue.jsonl')  # the queue's open traits now, which can differ from the harvest's
    if os.path.exists(qp):
        now = {}
        for l in open(qp, encoding='utf-8'):
            try: c = json.loads(l)
            except ValueError: continue
            now.setdefault(c.get('genus'), set()).add(c.get('trait'))
        for g, d in genera.items():
            if g in now:
                d['harvest_traits'] = list(d.get('traits', [])); d['traits'] = sorted(now[g])
    for g in genera.values():  # a query a later run completed drops the same query's earlier failure
        ok = {q.get('q') for x in g.get('extra', []) for q in x.get('queries', []) if not q.get('error')}
        for x in g.get('extra', []):
            x['queries'] = [q for q in x.get('queries', []) if not (q.get('error') and q.get('q') in ok)]
    return ','.join(map(str, sorted(runs))), genera, families, summaries


def show(d, families):
    w = d['works']
    def item(wid, k):
        x = w.get(wid, {})
        oa = f"{x.get('oa_status') or 'closed'} {x.get('oa_url') or ''} {x.get('license') or ''}".strip()
        return f"  [{k}] {x.get('title')} ({x.get('year')}) {x.get('venue')} | doi {x.get('doi') or '-'} | {oa}\n      {(x.get('abstract') or '')[:350]}"
    src = f" [family from {d['family_source']}]" if d.get('family_source') else ''
    later = sorted(set(d['traits']) - set(d.get('harvest_traits', d['traits'])))
    late = f" (opened since the harvest, so no trait query of the harvest names them: {', '.join(later)})" if later else ''
    out = [f"## {d['genus']} ({d['family']}, {d['order']}){src} open traits: {', '.join(d['traits'])}{late}; views {', '.join(d['views'])}; harvest run {d['run']}"]
    k = 0
    for q in d['queries']:
        out.append(f"query \"{q['q']}\": {q.get('n')} hits" + (f" (error {q['error']})" if q.get('error') else ''))
        for wid in q.get('ids', []): k += 1; out.append(item(wid, k))
    for c in d['chase']:
        out.append(f"citation step: works citing {c['cited_doi']} that name {d['genus']}: {c.get('n')}" + (f" (error {c['error']})" if c.get('error') else ''))
        for wid in c.get('ids', []): k += 1; out.append(item(wid, k))
    for ex in d.get('extra', []):
        for q in ex['queries']:
            out.append(f"query \"{q['q']}\" (supplement run {ex['run']}): {q.get('n')} hits" + (f" (error {q['error']})" if q.get('error') else ''))
            for wid in q.get('ids', []):
                k += 1; x = ex['works'].get(wid, {})
                out.append(f"  [{k}] {x.get('title')} ({x.get('year')}) {x.get('venue')} | doi {x.get('doi') or '-'} | {x.get('oa_status') or 'closed'} {x.get('oa_url') or ''} {x.get('license') or ''}\n      {(x.get('abstract') or '')[:350]}")
    f = families.get(d['family'])
    if f:
        out.append(f"family review \"{f['query']['q']}\": {f['query'].get('n')} hits")
        for wid in f['query'].get('ids', []):
            x = f['works'].get(wid, {})
            out.append(f"  - {x.get('title')} ({x.get('year')}) | doi {x.get('doi') or '-'} | {x.get('oa_status') or 'closed'} {x.get('oa_url') or ''}")
    return '\n'.join(out)


def main():
    a = sys.argv[1:]
    runs, genera, families, summaries = load()
    if '--run' in a:
        print(f'harvest runs {runs}: {len(genera)} genera, {len(families)} family reviews'); print('\n'.join(summaries)); return
    if '--next' in a:
        k = int(a[a.index('--next') + 1]); skip = set()
        if '--skip' in a:
            p = a[a.index('--skip') + 1]
            if os.path.exists(p): skip = {l.strip() for l in open(p) if l.strip() and not l.startswith('#')}
        sys.path.insert(0, os.path.join(ROOT, 'ci', 'harvest')); os.chdir(ROOT)
        import harvest
        need = [t['genus'] for t in harvest.targets()]
        print('\n'.join([g for g in need if g in genera and g not in skip][:k])); return
    for g in a:
        print(show(genera[g], families) if g in genera else f'## {g}: in no harvest run yet ({runs})')
        print()


if __name__ == '__main__':
    main()
