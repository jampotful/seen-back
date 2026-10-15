"""Refreshes the Papers Wanted page's research side in one command. The research desk runs it at every check-in and
after every merge, so the page keeps filing papers into To get, Try again and Done by itself.
Usage: python3 -I tools/views/papers_refresh.py TICKS_DIR OUT_DIR [--gaps]
Before: with ArtifactData on the page, "get" ticks/all and "list" extra (limit 1000), both with out_dir TICKS_DIR.
Steps: gaps.py --world 1200 when --gaps is given (so docs/views/gaps/cells.jsonl is current); papers_status.py (the owner's marks
-> docs/views/papers-status.jsonl); wanted_csv.py (every wanted list but fixes.jsonl, with --fix and --status);
gain.py (verdicts, ranks and priorities -> docs/views/wanted-merged.csv and OUT_DIR/status.json); papers_extra.py
(papers the page does not hold yet -> OUT_DIR/extra/batch-N.json).
After: ArtifactData "set" status/all with file_path OUT_DIR/status.json (if_version: the version you last read), then
"batch" with each OUT_DIR/extra/batch-N.json, and when OUT_DIR/ticks-patch.json exists (a mark on a duplicate that was
folded into another paper), "update" ticks/all with it. Commit docs/views/papers-status.jsonl and docs/views/wanted-merged.csv.
What the page does with it: a paper the owner saved, or one whose verdict is done or read, goes to Done; a paper marked
partial or can't get goes to Try again, ranked by priority, then by what it would still fill; the rest is To get."""
import glob, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
def run(*a):
    r = subprocess.run([sys.executable, '-I', *a], cwd=ROOT, capture_output=True, text=True)
    sys.stdout.write(r.stdout); sys.stderr.write(r.stderr)
    if r.returncode: sys.exit(f'stopped: {a[0]} failed')
args = sys.argv[1:]; gaps = '--gaps' in args; args = [a for a in args if a != '--gaps']
ticks_dir, out = os.path.abspath(args[0]), os.path.abspath(args[1]); os.makedirs(out, exist_ok=True)
ticks = os.path.join(ticks_dir, 'ticks', 'all.json')
if not os.path.exists(ticks): sys.exit(f'no {ticks}: save ticks/all there first (ArtifactData get, out_dir {ticks_dir})')
if gaps: run('tools/views/gaps.py', '--world', '1200')  # the 1,200-species lists of QUEUE 18; the default 60 shrinks the table
merged = 'docs/views/wanted-merged.csv'
run('tools/views/papers_status.py', ticks, merged, 'docs/views/papers-status.jsonl')
lists = sorted(p for p in glob.glob(os.path.join(ROOT, 'docs/views/wanted/*.jsonl')) if not p.endswith('fixes.jsonl'))
raw = os.path.join(out, 'wanted-raw.csv')
folds = os.path.join(out, 'folds.json')
run('tools/views/wanted_csv.py', raw, *lists, '--fix', 'docs/views/wanted/fixes.jsonl', '--status', 'docs/views/papers-status.jsonl', '--folds', folds)
import json
marks = json.load(open(ticks)); marks = marks.get('data', marks)
patch = {dst: marks[src] for src, dst in json.load(open(folds)).items() if marks.get(src) in (True, 'partial', 'na') and not marks.get(dst)}
pp = os.path.join(out, 'ticks-patch.json')
if os.path.exists(pp): os.remove(pp)
if patch:
    json.dump(patch, open(pp, 'w')); print(len(patch), 'marks on folded duplicates to carry over: ArtifactData update ticks/all with file_path', pp)
run('tools/views/gain.py', raw, merged, '--status', os.path.join(out, 'status.json'))
run('tools/views/papers_extra.py', merged, 'docs/views/papers-base-ids.json', os.path.join(out, 'extra'), os.path.join(ticks_dir, 'extra'))
print(f'next: ArtifactData set status/all from {out}/status.json, then batch each {out}/extra/batch-N.json')
