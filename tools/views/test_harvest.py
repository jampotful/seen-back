#!/usr/bin/env python3
"""Harvest selection and PLANTTRAITS use local fixtures; no network or paid API."""
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools/views'))
spec = importlib.util.spec_from_file_location('harvest', ROOT / 'ci/harvest/harvest.py')
harvest = importlib.util.module_from_spec(spec)
spec.loader.exec_module(harvest)


def write(root, rel, rows):
    path = Path(root) / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(''.join(json.dumps(r) + '\n' for r in rows))


class HarvestTests(unittest.TestCase):
    def fixture(self, root):
        write(root, 'docs/views/gaps/rows.json', [{'classes': {'order': []}}])
        write(root, 'docs/views/gaps/queue.jsonl', [
            dict(view='plant', taxon=g + ' alba', genus=g, family='Rosaceae', order='Rosales',
                 trait='diel', score=score) for g, score in [('Thin', 20), ('Screened', 10), ('Partial', 5)]])
        thin = dict(taxon='Thin', level='genus', trait='diel', queries=['one', 'two'], chased='10.example/paper', where=['WebSearch'])
        screened = dict(thin, taxon='Screened', where=['OpenAlex, harvest run 2'])
        partial = dict(thin, taxon='Partial', where=['OpenAlex, harvest run 2'], queries=['one'])
        write(root, 'docs/views/searched/sweep.jsonl', [thin, screened, partial])

    def test_only_successful_nonempty_genus_receipts_count(self):
        import subprocess
        rows = [dict(type='genus', genus='Ready', queries=[{'q': 'Ready vision', 'ids': []}]),
                dict(type='genus', genus='Failed', queries=[{'q': 'Failed vision', 'error': 'gave up'}]),
                dict(type='genus', genus='Empty', queries=[]),
                dict(type='genus_extra', genus='Extra', queries=[{'q': 'Extra vision'}]),
                dict(type='family', family='Rosaceae', query={'q': 'Rosaceae review'})]
        raw = ''.join(json.dumps(r) + '\n' for r in rows).encode() + b'{"type":'
        def run(args, **kwargs):
            self.assertNotIn('fetch', args)
            return subprocess.CompletedProcess(args, 0, 'runs/harvest/1-0/harvest.jsonl' if 'ls-tree' in args else raw)
        with patch('subprocess.run', side_effect=run):
            self.assertEqual(harvest.harvested_before(fetch=False), {'Ready'})

    def test_thin_searches_do_not_exhaust_harvest_targets(self):
        with tempfile.TemporaryDirectory() as root, patch.object(harvest, 'ROOT', root), \
             patch.object(harvest, 'harvested_before', return_value={'Thin', 'Screened'}):
            self.fixture(root)
            self.assertEqual([t['genus'] for t in harvest.targets()], ['Thin', 'Partial'])
            with patch.object(harvest, 'harvested_before', return_value=set()):
                self.assertEqual([t['genus'] for t in harvest.targets()], ['Thin', 'Screened', 'Partial'])

    def test_planttraits_sends_only_missing_queries_for_harvested_genera(self):
        with tempfile.TemporaryDirectory() as root, patch.object(harvest, 'ROOT', root):
            self.fixture(root)
            sent = []
            def search(q, works):
                sent.append(q)
                return {'q': q, 'n': 0, 'ids': []}
            with patch.object(harvest, 'harvested_before', return_value={'Thin'}), \
                 patch.object(harvest, 'extras_done', return_value={('Thin', 'Thin flower opening time')}), \
                 patch.object(harvest, 'search', side_effect=search), patch.object(harvest.time, 'sleep'):
                out = str(Path(root) / 'out')
                harvest.plant_traits_main(out, 0, 1)
            self.assertEqual(sent, ['Thin nyctinasty', 'Thin anthesis', 'Thin pollination biology'])
            got = [json.loads(line) for line in (Path(out) / 'harvest.jsonl').read_text().splitlines()]
            self.assertEqual([(r['type'], r['genus']) for r in got], [('genus_extra', 'Thin')])


if __name__ == '__main__':
    unittest.main()
