"""Lists the work for the next Codex round, computed from what main already holds, so nobody keeps track by hand.
Usage: python3 -I tools/views/codex_queue.py [--json]
Items:
- oa-k: papers of docs/tracks/batches/oa-k.json with no line yet in docs/views/sources/oa-k.jsonl or oa-none-k.jsonl
  (matched by DOI, else by normalised title). Prompt docs/tracks/prompts/oa-pass.md.
- external-k: genera of docs/tracks/batches/external-k.json with no record yet in docs/views/searched/external-k.jsonl
  or docs/views/evidence/external-k.jsonl, listed only when docs/tracks/codex-gates.json has "sweeps": true.
  Prompt docs/tracks/prompts/external-sweep.md.
Entries are positions in the batch file's list, counting from 1. Work from an open pull request is not on main yet, so
a round should start only when no outside pull request is open (docs/tracks/prompts/codex-round.md)."""
import glob, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
def P(*a): return os.path.join(ROOT, *a)
def norm(t): return re.sub(r'[^a-z0-9]+', ' ', (t or '').lower()).strip()

def lines(path):
    if not os.path.exists(path): return []
    out = []
    for l in open(path, encoding='utf-8'):
        try: out.append(json.loads(l))
        except ValueError: pass
    return out

def oa_items():
    items = []
    for path in sorted(glob.glob(P('docs/tracks/batches/oa-*.json')), key=lambda p: int(re.findall(r'\d+', os.path.basename(p))[0])):
        k = re.findall(r'oa-(\d+)\.json$', path)[0]
        papers = json.load(open(path, encoding='utf-8'))['papers']
        seen_doi, seen_title = set(), set()
        for name in (f'oa-{k}.jsonl', f'oa-none-{k}.jsonl'):
            for j in lines(P('docs/views/sources', name)):
                if (j.get('doi') or '').strip(): seen_doi.add(j['doi'].lower().strip())
                if j.get('title'): seen_title.add(norm(j['title']))
        left = [n for n, p in enumerate(papers, 1)
                if not ((p.get('doi') or '').lower().strip() in seen_doi or norm(p.get('title')) in seen_title)]
        if left:
            items.append({'item': f'oa-{k}', 'prompt': 'docs/tracks/prompts/oa-pass.md', 'batch': f'docs/tracks/batches/oa-{k}.json',
                          'entries': left, 'count': len(left), 'of': len(papers)})
    return items

def sweep_items():
    gates = P('docs/tracks/codex-gates.json')
    if not (os.path.exists(gates) and json.load(open(gates)).get('sweeps')): return []
    items = []
    for path in sorted(glob.glob(P('docs/tracks/batches/external-*.json')), key=lambda p: int(re.findall(r'\d+', os.path.basename(p))[0])):
        k = re.findall(r'external-(\d+)\.json$', path)[0]
        d = json.load(open(path, encoding='utf-8'))
        genera = [g['genus'] if isinstance(g, dict) else g for g in (d['genera'] if isinstance(d, dict) else d)]
        done = {(j.get('taxon') or '').split()[0] for j in lines(P('docs/views/searched', f'external-{k}.jsonl')) + lines(P('docs/views/evidence', f'external-{k}.jsonl'))}
        left = [g for g in genera if g not in done]
        if left:
            items.append({'item': f'external-{k}', 'prompt': 'docs/tracks/prompts/external-sweep.md', 'batch': f'docs/tracks/batches/external-{k}.json',
                          'genera': left, 'count': len(left), 'of': len(genera)})
    return items

def held():
    """Items docs/tracks/codex-gates.json holds back until a time, e.g. while an earlier chat may still be working on them."""
    import datetime
    gates = P('docs/tracks/codex-gates.json')
    if not os.path.exists(gates): return set()
    now = datetime.datetime.now(datetime.timezone.utc)
    out = set()
    for item, until in (json.load(open(gates)).get('hold') or {}).items():
        try:
            if datetime.datetime.fromisoformat(until) > now: out.add(item)
        except ValueError:
            out.add(item)
    return out

def main():
    hold = held()
    items = [it for it in oa_items() + sweep_items() if it['item'] not in hold]
    if '--json' in sys.argv[1:]:
        print(json.dumps(items, ensure_ascii=False, indent=1)); return
    if not items:
        print('Nothing to do: every outside batch is finished on main.'); return
    for it in items:
        what = 'entries ' + ','.join(map(str, it['entries'])) if 'entries' in it else 'genera ' + ', '.join(it['genera'])
        print(f"{it['item']}: {it['count']} of {it['of']} left. Follow {it['prompt']} for {it['batch']}, doing only {what}.")

if __name__ == '__main__':
    main()
