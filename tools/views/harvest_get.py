"""Reads the latest OpenAlex harvest (.github/workflows/harvest.yml) from the ci branch, for the desk and its agents.
Usage:
  python3 -I tools/views/harvest_get.py Genus [Genus ...]     print what the build machines found for these genera
  python3 -I tools/views/harvest_get.py --next 40 [--skip FILE] the next genera, heaviest first, that are in the
      harvest and still lack a full-protocol search record (FILE lists genera already handed out, one a line)
  python3 -I tools/views/harvest_get.py --run                  the harvest run in use and its summaries
For each genus it prints the protocol's searches already sent (scientific name, English name, trait groups), the
citation step (works citing the nearest measured relative's source that name the genus) and the family review search,
each work with title, year, venue, DOI, open-access status, link and licence, and the start of its abstract."""
import gzip, json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def git(*a, binary=False):
    r = subprocess.run(['git', '-C', ROOT, *a], capture_output=True)
    return r.stdout if binary else r.stdout.decode('utf-8', 'replace')


def latest():
    git('fetch', '-q', '--depth', '1', 'origin', '+refs/heads/ci:refs/remotes/origin/ci')
    runs = {}
    for line in git('show', 'origin/ci:INDEX.txt').splitlines():
        m = re.search(r'runs/harvest/(\d+)-(\d+)\s+(\w+)', line)
        if m: runs.setdefault(int(m.group(1)), {})[int(m.group(2))] = m.group(3)
    for n in sorted(runs, reverse=True):
        if runs[n] and all(v == 'success' for v in runs[n].values()) and len(runs[n]) >= 3:
            return n, sorted(runs[n])
    return None, []


def load():
    n, shards = latest()
    if n is None: sys.exit('No finished harvest on the ci branch yet. Push a branch run/harvest/<name> to start one.')
    genera, families, summaries = {}, {}, []
    for s in shards:
        base = f'runs/harvest/{n}-{s}/'
        summaries.append(git('show', f'origin/ci:{base}summary.txt').strip())
        raw = git('show', f'origin/ci:{base}harvest.jsonl.gz', binary=True)
        for l in gzip.decompress(raw).decode('utf-8').splitlines():
            d = json.loads(l)
            if d['type'] == 'genus': genera[d['genus']] = d
            else: families[d['family']] = d
    return n, genera, families, summaries


def show(d, families, run):
    w = d['works']
    def item(wid, k):
        x = w.get(wid, {})
        oa = f"{x.get('oa_status') or 'closed'} {x.get('oa_url') or ''} {x.get('license') or ''}".strip()
        ab = (x.get('abstract') or '')[:350]
        return f"  [{k}] {x.get('title')} ({x.get('year')}) {x.get('venue')} | doi {x.get('doi') or '-'} | {oa}\n      {ab}"
    out = [f"## {d['genus']} ({d['family']}, {d['order']}) open traits: {', '.join(d['traits'])}; views {', '.join(d['views'])}; harvest run {run}"]
    k = 0
    for q in d['queries']:
        out.append(f"query \"{q['q']}\": {q.get('n')} hits" + (f" (error {q['error']})" if q.get('error') else ''))
        for wid in q.get('ids', []): k += 1; out.append(item(wid, k))
    for c in d['chase']:
        out.append(f"citation step: works citing {c['cited_doi']} that name {d['genus']}: {c.get('n')}" + (f" (error {c['error']})" if c.get('error') else ''))
        for wid in c.get('ids', []): k += 1; out.append(item(wid, k))
    f = families.get(d['family'])
    if f:
        out.append(f"family review \"{f['query']['q']}\": {f['query'].get('n')} hits")
        for wid in f['query'].get('ids', []):
            x = f['works'].get(wid, {}); out.append(f"  - {x.get('title')} ({x.get('year')}) | doi {x.get('doi') or '-'} | {x.get('oa_status') or 'closed'} {x.get('oa_url') or ''}")
    return '\n'.join(out)


def main():
    a = sys.argv[1:]
    run, genera, families, summaries = load()
    if '--run' in a:
        print(f'harvest run {run}'); print('\n'.join(summaries)); return
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
        print(show(genera[g], families, run) if g in genera else f'## {g}: not in harvest run {run}')
        print()


if __name__ == '__main__':
    main()
