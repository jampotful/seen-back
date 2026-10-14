"""Scores a search-recall test (docs/tracks/prompts/recall-test.md) against the measurements already logged.
Usage: python3 -I tools/views/recall_score.py docs/tracks/tests/recall-high.jsonl [more files]
A cell is a hit when the test found a source whose DOI is among the logged sources of a measurement of that trait in that
genus (grade m, read in full). A cell whose finds have other DOIs is marked "check": the desk opens the source and counts
it a hit when it measures that trait in a species of that genus. A cell with nothing found is a miss. THOROUGH.md asks for
at least 9 hits in 10."""
import glob, json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def logged():
    out = {}
    for p in glob.glob(os.path.join(ROOT, 'docs/views/evidence/*.jsonl')):
        for l in open(p, encoding='utf-8'):
            try: r = json.loads(l)
            except ValueError: continue
            s = r.get('source') or {}
            if r.get('grade') == 'm' and r.get('opened') and not r.get('partial') and s.get('doi') and r.get('taxon'):
                out.setdefault((r['taxon'].split()[0], r.get('trait')), set()).add(s['doi'].lower().strip())
    return out

def main():
    known = logged()
    for path in sys.argv[1:]:
        hits = checks = 0; lines = []
        for l in open(path, encoding='utf-8'):
            try: c = json.loads(l)
            except ValueError: continue
            dois = {(f.get('doi') or '').lower().strip() for f in c.get('found') or [] if f.get('doi')}
            want = known.get((c.get('genus'), c.get('trait')), set())
            if dois & want: state = 'hit'; hits += 1
            elif c.get('found'): state = 'check'; checks += 1
            else: state = 'miss'
            lines.append(f"  {state:5}  {c.get('genus')} {c.get('trait')}  found {sorted(dois) or '-'}  logged {sorted(want) or '-'}")
        print(f'{os.path.basename(path)}: {hits} hits, {checks} to check by hand, of {len(lines)}')
        print('\n'.join(lines))

if __name__ == '__main__':
    main()
