"""Offline contract tests. Every transport is mocked; no tokens or network required."""
import contextlib
import datetime as dt
import importlib.util
import io
import json
import os
import pathlib
import unittest
from unittest.mock import patch, mock_open
from urllib.parse import parse_qs, urlsplit
from zoneinfo import ZoneInfo

MODULE = pathlib.Path(__file__).with_name('quiet.py')
with patch.dict(os.environ, {'GITHUB_REPOSITORY': 'example/review', 'GITHUB_TOKEN': 'offline', 'NTFY_TOPIC': '', 'TEST': ''}, clear=True):
    spec = importlib.util.spec_from_file_location('quiet', MODULE)
    quiet = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(quiet)

NOW = dt.datetime(2026, 11, 9, 15, 0, tzinfo=dt.timezone.utc)
LAST = NOW - dt.timedelta(hours=3)
CFG = {'tz': 'America/New_York', 'daily_from': '08:00', 'daily_until': '23:00',
       'quiet_minutes': 50, 'remind_minutes': 120, 'reminders': 2, 'paused': False, 'test': ''}

class Frozen(dt.datetime):
    @classmethod
    def now(cls, tz=None):
        return NOW.astimezone(tz) if tz else NOW.replace(tzinfo=None)

def issue(state='open', last=LAST, age=180):
    return {'number': 10, 'user': {'login': 'github-actions[bot]'}, 'body': f'<!-- since {last.isoformat()} -->', 'state': state,
            'created_at': (NOW - dt.timedelta(minutes=age)).isoformat(),
            'html_url': 'https://example.invalid/10', 'comments_url': '/comments'}

class QuietTests(unittest.TestCase):
    def setUp(self):
        self.transport = patch.object(quiet.urllib.request, 'urlopen', side_effect=AssertionError('Network prohibited'))
        self.network = self.transport.start()
        self.addCleanup(self.transport.stop)
        self.addCleanup(self.network.assert_not_called)

    def run_main(self, cfg=None, issues=None, comments=None, last=LAST, test=False,
                 topic='offline-test-topic', times=None, fail_path=None, expect_error=None):
        writes, reads, pushes = [], [], []
        moments = iter(times or [NOW])
        current = NOW
        class Clock(dt.datetime):
            @classmethod
            def now(cls, tz=None):
                nonlocal current
                current = next(moments, current)
                return current.astimezone(tz) if tz else current.replace(tzinfo=None)
        def gh(method, path, body=None):
            if fail_path and fail_path in path:
                raise RuntimeError('simulated API failure')
            if method == 'GET':
                reads.append(path)
                items = (comments or []) if path.startswith('/comments') else (issues or [])
                page = int(parse_qs(urlsplit(path).query).get('page', ['1'])[0])
                return items[(page-1)*100:page*100]
            writes.append((method, path, body))
            if method == 'POST' and path.endswith('/issues'):
                return issue()
        output = io.StringIO()
        with patch('builtins.open', mock_open(read_data=json.dumps(CFG if cfg is None else cfg))), \
             patch.object(quiet.datetime, 'datetime', Clock), patch.object(quiet, 'TEST', test), \
             patch.object(quiet, 'TOPIC', topic), patch.object(quiet, 'push', side_effect=lambda *args: pushes.append(args)), \
             patch.object(quiet, 'gh', side_effect=gh), patch.object(quiet, 'newest_commit', return_value=(last, 'main')), \
             contextlib.redirect_stdout(output):
            if expect_error:
                with self.assertRaises(expect_error):
                    quiet.main()
            else:
                quiet.main()
        self.reads, self.pushes = reads, pushes
        self.network.assert_not_called()
        return writes, output.getvalue()

    def test_pause_blocks_every_write_including_test_and_recovery(self):
        writes, log = self.run_main({**CFG, 'paused': True, 'pause_reason': 'budget', 'test': 'new'},
                                   issues=[issue(last=LAST-dt.timedelta(hours=1))], test=True)
        self.assertEqual(writes, [])
        self.assertEqual(self.pushes, [])
        self.assertEqual(self.reads, [])
        self.assertIn('intentional pause: budget', log)

    def test_review_time_does_not_auto_rearm(self):
        writes, log = self.run_main({**CFG, 'paused': True, 'pause_review_at': '2000-01-01T00:00:00Z'})
        self.assertEqual(writes, [])
        self.assertEqual(self.pushes, [])
        self.assertEqual(self.reads, [])
        self.assertIn('manual re-arm only', log)

    def test_expired_cutoff_is_distinct(self):
        writes, log = self.run_main({**CFG, 'through': '2026-10-31'})
        self.assertEqual(writes, [])
        self.assertEqual(self.pushes, [])
        self.assertEqual(self.reads, [])
        self.assertIn('expired through date', log)

    def test_quiet_hours_block_test_and_recovery(self):
        writes, log = self.run_main({**CFG, 'daily_from': '11:00', 'test': 'new'},
                                   issues=[issue(last=LAST-dt.timedelta(hours=1))], test=True)
        self.assertEqual(writes, [])
        self.assertEqual(self.pushes, [])
        self.assertEqual(self.reads, [])
        self.assertIn('outside daily hours', log)

    def test_window_boundaries_winter_and_summer(self):
        tz = ZoneInfo('America/New_York')
        for day in ['2026-07-09', '2026-11-09']:
            for clock, armed in [('07:59', False), ('08:00', True), ('22:59', True), ('23:00', False)]:
                local = dt.datetime.fromisoformat(day+'T'+clock).replace(tzinfo=tz)
                self.assertEqual(quiet.suppression_reason(CFG, local) is None, armed)

    def test_no_cutoff_remains_armed_in_future(self):
        local = dt.datetime(2030, 1, 1, 12, tzinfo=ZoneInfo('America/New_York'))
        self.assertIsNone(quiet.suppression_reason(CFG, local))

    def test_one_issue_without_ntfy(self):
        writes, log = self.run_main(topic='')
        self.assertEqual(self.pushes, [])
        created = [x for x in writes if x[1].endswith('/issues')]
        self.assertEqual(len(created), 1)
        self.assertIn('not proof', created[0][2]['body'])
        self.assertIn('alert opened', log)

    def test_busy_has_no_issue(self):
        writes, log = self.run_main(last=NOW-dt.timedelta(minutes=49))
        self.assertEqual(len(writes), 1)  # existing idempotent label setup only
        self.assertIn('busy', log)

    def test_exact_threshold_opens(self):
        writes, _ = self.run_main(last=NOW-dt.timedelta(minutes=50))
        self.assertEqual(len([x for x in writes if x[1].endswith('/issues')]), 1)

    def test_same_spell_does_not_duplicate(self):
        writes, _ = self.run_main(issues=[issue(age=30)])
        self.assertEqual(len(writes), 1)

    def test_manual_close_silences_spell(self):
        writes, log = self.run_main(issues=[issue(state='closed')])
        self.assertEqual(len(writes), 1)
        self.assertIn('closed by hand', log)

    def test_two_hour_reminder(self):
        writes, _ = self.run_main(issues=[issue(age=120)])
        self.assertEqual(len([x for x in writes if x[1].endswith('/comments')]), 1)

    def test_reminder_cooldown(self):
        comments = [{'body': 'Still quiet: 180 minutes', 'created_at': (NOW-dt.timedelta(minutes=119)).isoformat()}]
        writes, _ = self.run_main(issues=[issue()], comments=comments)
        self.assertEqual(len(writes), 1)

    def test_reminder_cap(self):
        comments = [{'body': 'Still quiet: older', 'created_at': (NOW-dt.timedelta(hours=3+i)).isoformat()} for i in [1, 0]]
        writes, _ = self.run_main(issues=[issue()], comments=comments)
        self.assertEqual(len(writes), 1)

    def test_recovery_closes_during_hours(self):
        writes, _ = self.run_main(issues=[issue()], last=NOW-dt.timedelta(minutes=1))
        self.assertEqual(len([x for x in writes if x[0] == 'PATCH']), 1)

    def test_codex_branches_excluded(self):
        refs = {'data': {'repository': {'refs': {'pageInfo': {'hasNextPage': False}, 'nodes': [
            {'name': 'codex/dispatch-state', 'target': {'committedDate': NOW.isoformat()}},
            {'name': 'main', 'target': {'committedDate': LAST.isoformat()}}]}}}}
        with patch.object(quiet, 'gh', return_value=refs):
            self.assertEqual(quiet.newest_commit(), (LAST, 'main'))

    def test_pause_precedes_expiry_and_hours(self):
        writes, log = self.run_main({**CFG, 'paused': True, 'through': '2000-01-01', 'daily_from': '11:00'})
        self.assertEqual(writes, [])
        self.assertIn('intentional pause', log)
        self.assertEqual(self.pushes, [])

    def test_pause_reason_is_optional_and_never_rearms(self):
        writes, log = self.run_main({**CFG, 'paused': True})
        self.assertEqual(writes, [])
        self.assertIn('reason not recorded', log)

    def test_invalid_config_fails_before_all_remote_calls(self):
        bad = [None, [], {k:v for k,v in CFG.items() if k != 'paused'},
               {**CFG, 'paused': 'false'}, {**CFG, 'paused': 0},
               {k:v for k,v in CFG.items() if k != 'tz'}, {**CFG, 'tz': 'Not/A_Zone'},
               {**CFG, 'daily_from': '8:00'}, {**CFG, 'daily_from': '24:00'},
               {**CFG, 'daily_until': '25:00'}, {**CFG, 'daily_until': '08:00'},
               {**CFG, 'daily_from': '23:00', 'daily_until': '08:00'},
               {**CFG, 'quiet_minutes': 0}, {**CFG, 'quiet_minutes': True},
               {**CFG, 'remind_minutes': -1}, {**CFG, 'reminders': -1},
               {**CFG, 'through': '2026-02-30'}, {**CFG, 'through': '20261109'},
               {**CFG, 'pause_review_at': '2026-11-08T22:10:00'},
               {**CFG, 'pause_review_at': 'nonsense'}, {**CFG, 'pause_reason': 1},
               {**CFG, 'test': True}]
        for config in bad:
            with self.subTest(config=config):
                # None is otherwise the helper's shorthand for CFG.
                if config is None:
                    with self.assertRaises(ValueError):
                        quiet.validate_config(None)
                    continue
                writes, _ = self.run_main(cfg=config, expect_error=(ValueError, KeyError))
                self.assertEqual(writes, [])
                self.assertEqual(self.reads, [])
                self.assertEqual(self.pushes, [])

    def test_valid_config_and_midnight_end(self):
        self.assertEqual(str(quiet.validate_config({**CFG, 'daily_until': '24:00'})), 'America/New_York')
        self.assertEqual(str(quiet.validate_config(CFG)), 'America/New_York')

    def test_through_is_inclusive(self):
        tz = ZoneInfo('America/New_York')
        config = {**CFG, 'through': '2026-11-09'}
        self.assertIsNone(quiet.suppression_reason(config, dt.datetime(2026,11,9,12,tzinfo=tz)))
        self.assertIn('expired', quiet.suppression_reason(config, dt.datetime(2026,11,10,12,tzinfo=tz)))

    def test_dst_transition_days_preserve_local_window(self):
        tz = ZoneInfo('America/New_York')
        for day in ['2026-03-08', '2026-11-01']:
            for clock, armed in [('07:59:59', False), ('08:00:00', True), ('22:59:59', True), ('23:00:00', False)]:
                local = dt.datetime.fromisoformat(day+'T'+clock).replace(tzinfo=tz)
                self.assertEqual(quiet.suppression_reason(CFG, local) is None, armed)

    def test_cutoff_before_label_sends_nothing(self):
        before = dt.datetime(2026,11,10,3,59,59,tzinfo=dt.timezone.utc)
        end = before + dt.timedelta(seconds=1)
        writes, _ = self.run_main(times=[before,end], expect_error=quiet.AlertSuppressed)
        self.assertEqual(writes, [])
        self.assertEqual(self.pushes, [])

    def test_cutoff_before_new_issue_does_not_alert(self):
        before = dt.datetime(2026,11,10,3,59,59,tzinfo=dt.timezone.utc)
        writes, _ = self.run_main(times=[before,before,before+dt.timedelta(seconds=1)], expect_error=quiet.AlertSuppressed)
        self.assertEqual(len(writes), 1)
        self.assertEqual(self.pushes, [])

    def test_cutoff_between_issue_and_phone_stops_phone(self):
        before = dt.datetime(2026,11,10,3,59,59,tzinfo=dt.timezone.utc)
        writes, _ = self.run_main(times=[before,before,before,before+dt.timedelta(seconds=1)], expect_error=quiet.AlertSuppressed)
        self.assertEqual(len(writes), 2)
        self.assertEqual(self.pushes, [])

    def test_cutoff_before_reminder_stops_reminder(self):
        before = dt.datetime(2026,11,10,3,59,59,tzinfo=dt.timezone.utc)
        writes, _ = self.run_main(issues=[issue()], times=[before,before,before+dt.timedelta(seconds=1)], expect_error=quiet.AlertSuppressed)
        self.assertEqual(len(writes), 1)
        self.assertEqual(self.pushes, [])

    def test_cutoff_before_recovery_stops_recovery(self):
        before = dt.datetime(2026,11,10,3,59,59,tzinfo=dt.timezone.utc)
        writes, _ = self.run_main(issues=[issue()], last=NOW-dt.timedelta(minutes=1),
                                 times=[before,before,before+dt.timedelta(seconds=1)], expect_error=quiet.AlertSuppressed)
        self.assertEqual(len(writes), 1)
        self.assertEqual(self.pushes, [])

    def test_closed_spell_beyond_first_page_stays_silent(self):
        issues = [{**issue(), 'body': 'unrelated labelled issue', 'number': i} for i in range(100)]
        writes, _ = self.run_main(issues=issues+[issue(state='closed')])
        self.assertEqual(len(writes), 1)
        self.assertEqual(len(self.reads), 2)
        self.assertEqual(self.pushes, [])

    def test_reminder_cap_beyond_first_comment_page(self):
        comments = [{'body': 'Discussion', 'created_at': NOW.isoformat()} for _ in range(100)]
        comments += [{'body': 'Still quiet', 'created_at': LAST.isoformat()} for _ in range(2)]
        writes, _ = self.run_main(issues=[issue()], comments=comments)
        self.assertEqual(len(writes), 1)
        self.assertEqual(self.pushes, [])

    def test_incomplete_issue_history_refuses_alert(self):
        issues = [{**issue(), 'body': 'unrelated'} for _ in range(1000)]
        writes, _ = self.run_main(issues=issues, expect_error=ValueError)
        self.assertEqual(len(writes), 1)
        self.assertEqual(len(self.reads), 10)
        self.assertEqual(self.pushes, [])

    def test_incomplete_comment_history_refuses_reminder(self):
        comments = [{'body': 'Discussion', 'created_at': NOW.isoformat()} for _ in range(1000)]
        writes, _ = self.run_main(issues=[issue()], comments=comments, expect_error=ValueError)
        self.assertEqual(len(writes), 1)
        self.assertEqual(self.pushes, [])

    def test_api_read_failure_does_not_create_issue(self):
        writes, _ = self.run_main(fail_path='?labels=', expect_error=RuntimeError)
        self.assertEqual(len(writes), 1)
        self.assertEqual(self.pushes, [])

    def test_api_write_failure_does_not_send_phone_push(self):
        writes, _ = self.run_main(fail_path='/issues', test=True, expect_error=RuntimeError)
        self.assertEqual(len(writes), 1)
        self.assertEqual(self.pushes, [])

    def test_missing_and_future_activity_fail_visibly(self):
        for stamp in [None, NOW+dt.timedelta(seconds=1), NOW.replace(tzinfo=None)]:
            writes, _ = self.run_main(last=stamp, expect_error=ValueError)
            self.assertEqual(len(writes), 1)
            self.assertEqual(self.pushes, [])

    def test_recovery_ignores_unmarked_malformed_and_newer_issues(self):
        issues = [{**issue(), 'body': body} for body in ['unrelated', '<!-- since bad -->', '<!-- since 2026-11-09T12:00:00 -->']]
        issues += [issue(last=LAST+dt.timedelta(minutes=1)), issue(age=30)]
        writes, _ = self.run_main(issues=issues)
        self.assertEqual(len(writes), 1)
        self.assertEqual(self.pushes, [])

    def test_manual_close_wins_over_existing_duplicate(self):
        writes, _ = self.run_main(issues=[issue(), issue(state='closed')])
        self.assertEqual(len(writes), 1)
        self.assertEqual(self.pushes, [])

    def test_zero_reminders_disables_reminders(self):
        writes, _ = self.run_main(cfg={**CFG, 'reminders': 0}, issues=[issue()])
        self.assertEqual(len(writes), 1)
        self.assertEqual(self.pushes, [])

    def test_cooldown_uses_latest_timestamp_not_comment_order(self):
        comments = [{'body': 'Still quiet', 'created_at': NOW.isoformat()},
                    {'body': 'Still quiet', 'created_at': LAST.isoformat()}]
        writes, _ = self.run_main(cfg={**CFG, 'reminders': 3}, issues=[issue()], comments=comments)
        self.assertEqual(len(writes), 1)

    def test_manual_test_is_gated_but_works_when_armed(self):
        writes, _ = self.run_main(test=True)
        self.assertEqual([x[0] for x in writes], ['POST','POST','PATCH'])
        self.assertEqual(len(self.pushes), 1)

    def test_legacy_config_test_is_not_repeated_beyond_first_page(self):
        issues = [{**issue(state='closed'), 'title': 'Other', 'body': 'Other'} for _ in range(100)]
        issues += [{**issue(state='closed'), 'title': 'Test of the quiet alert (approved-id)'}]
        writes, _ = self.run_main(cfg={**CFG, 'test': 'approved-id'}, issues=issues)
        self.assertEqual(len(writes), 1)
        self.assertEqual(self.pushes, [])

    def test_ntfy_empty_topic_does_not_attempt_transport(self):
        with patch.object(quiet, 'TOPIC', ''):
            quiet.push('Title', 'Message', 'default', 'test')
        self.network.assert_not_called()

    def test_ntfy_failure_is_contained_and_topic_redacted(self):
        output = io.StringIO()
        with patch.object(quiet, 'TOPIC', 'private-test-topic'), contextlib.redirect_stdout(output):
            quiet.push('Title', 'Message', 'default', 'test')
        self.network.assert_called_once()
        self.assertIn('ntfy push failed', output.getvalue())
        self.assertNotIn('private-test-topic', output.getvalue())
        self.network.reset_mock()

    def test_branch_scan_paginates_and_excludes_codex_on_every_page(self):
        def page(nodes, more=False):
            return {'data': {'repository': {'refs': {'pageInfo': {'hasNextPage': more, 'endCursor': 'next'}, 'nodes': nodes}}}}
        pages = [page([{'name':'main','target':{'committedDate':LAST.isoformat()}}], True),
                 page([{'name':'codex/work','target':{'committedDate':NOW.isoformat()}},
                       {'name':'research','target':{'committedDate':(LAST+dt.timedelta(minutes=1)).isoformat()}}])]
        with patch.object(quiet, 'gh', side_effect=pages) as api:
            self.assertEqual(quiet.newest_commit(), (LAST+dt.timedelta(minutes=1), 'research'))
            self.assertEqual(api.call_args_list[1].args[2]['variables']['after'], 'next')

    def test_recovery_retry_does_not_repeat_committed_comment(self):
        latest = NOW-dt.timedelta(minutes=1)
        comments = [{'body': f'<!-- recovered since {latest.isoformat()} -->', 'created_at': NOW.isoformat()}]
        writes, _ = self.run_main(issues=[issue()], comments=comments, last=latest)
        self.assertEqual([x[0] for x in writes], ['POST', 'PATCH'])
        self.assertEqual(len(self.pushes), 1)

    def test_cutoff_between_recovery_comment_and_close_stops_close(self):
        before = dt.datetime(2026,11,10,3,59,59,tzinfo=dt.timezone.utc)
        writes, _ = self.run_main(issues=[issue()], last=NOW-dt.timedelta(minutes=1),
                                 times=[before,before,before,before+dt.timedelta(seconds=1)], expect_error=quiet.AlertSuppressed)
        self.assertEqual([x[0] for x in writes], ['POST','POST'])
        self.assertEqual(self.pushes, [])

    def test_cutoff_during_manual_test_prevents_later_writes(self):
        before = dt.datetime(2026,11,10,3,59,59,tzinfo=dt.timezone.utc)
        writes, _ = self.run_main(test=True, times=[before,before,before,before,before+dt.timedelta(seconds=1)],
                                 expect_error=quiet.AlertSuppressed)
        self.assertEqual([x[0] for x in writes], ['POST','POST'])
        self.assertEqual(len(self.pushes), 1)

    def test_pause_to_rearm_to_alert_reminder_recovery_lifecycle(self):
        # A stateful fake API persists the exact emitted issue/comments between evaluations.
        state = {'issues': [], 'comments': [], 'writes': [], 'pushes': [], 'now': NOW, 'last': LAST}
        class Clock(dt.datetime):
            @classmethod
            def now(cls, tz=None):
                return state['now'].astimezone(tz) if tz else state['now'].replace(tzinfo=None)
        def api(method, path, body=None):
            if method == 'GET':
                return state['comments'] if path.startswith('/comments') else state['issues']
            state['writes'].append((method,path,body))
            if path.endswith('/issues'):
                created = {**issue(), **body, 'created_at': state['now'].isoformat()}
                state['issues'].append(created)
                return created
            if path.endswith('/comments'):
                state['comments'].append({**body, 'created_at': state['now'].isoformat()})
            if method == 'PATCH':
                state['issues'][0].update(body)
        def run(config):
            with patch('builtins.open', mock_open(read_data=json.dumps(config))):
                quiet.main()
        with patch.object(quiet.datetime, 'datetime', Clock), patch.object(quiet, 'TEST', False), \
             patch.object(quiet, 'TOPIC', ''), patch.object(quiet, 'gh', side_effect=api), \
             patch.object(quiet, 'push', side_effect=lambda *args: state['pushes'].append(args)), \
             patch.object(quiet, 'newest_commit', side_effect=lambda: (state['last'], 'main')), \
             contextlib.redirect_stdout(io.StringIO()):
            run({**CFG, 'paused': True, 'pause_review_at': '2000-01-01T00:00:00Z'})
            self.assertEqual(state['writes'], [])
            # The approved re-arm commit itself is activity; no immediate stale alert.
            state['last'] = NOW
            run(CFG)
            self.assertEqual(state['issues'], [])
            state['now'] = NOW+dt.timedelta(minutes=50)
            run(CFG)
            run(CFG)
            self.assertEqual(len(state['issues']), 1)
            self.assertEqual(state['comments'], [])
            for minutes, expected in [(169,0),(170,1),(289,1),(290,2),(410,2)]:
                state['now'] = NOW+dt.timedelta(minutes=minutes)
                run(CFG)
                self.assertEqual(len(state['comments']), expected)
            state['last'] = state['now']
            run(CFG)
            self.assertEqual(state['issues'][0]['state'], 'closed')
            self.assertEqual(len(state['comments']), 3)
            run(CFG)
            self.assertEqual(len(state['comments']), 3)
            self.assertEqual(state['pushes'], [])
        self.network.assert_not_called()

    def test_never_closes_human_issue_or_pull_request(self):
        older = LAST-dt.timedelta(hours=1)
        items = [{**issue(last=older), 'user': {'login': 'owner'}},
                 {**issue(last=older), 'pull_request': {'url':'https://example.invalid/pr'}}, issue(age=30)]
        writes, _ = self.run_main(issues=items)
        self.assertEqual(len(writes), 1)
        self.assertEqual(self.pushes, [])

if __name__ == '__main__':
    unittest.main()
