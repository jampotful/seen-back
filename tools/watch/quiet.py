"""Reports quiet research activity without authorizing allowance resets or session restarts.

Run by .github/workflows/quiet-alert.yml every 15 minutes. It uses the GitHub API (GITHUB_TOKEN) and none of the Claude
allowance, because a Claude session that has hit its limit cannot send anything itself.

docs/tracks/watch.json arms it. An explicit pause or the daily window suppresses all alert writes, including tests
and recovery notices. pause_review_at is informational and never resumes monitoring or research. The legacy
optional "through" cutoff remains supported. When no eligible (non-codex/) branch has
received a commit for quiet_minutes, it opens one issue labelled "quiet" that mentions the owner (GitHub notifies
them according to their notification settings) and, when the repository secret NTFY_TOPIC is set, sends a phone push
through ntfy.sh. One quiet spell gets one issue. While the issue stays open and the repository stays quiet, the alert
repeats every remind_minutes, at most "reminders" times. When commits resume, the issue closes with a note and a second
push says so. Closing the issue by hand silences that spell. Over the 30 hours of steady work before this was written,
the longest gap between commits was 46 minutes.

By hand: Actions > quiet-alert > Run workflow, with "test" ticked, sends one test alert and closes it at once. A new value
of "test" in watch.json does the same at the next scheduled run, once."""
import datetime, json, os, re, urllib.error, urllib.request
from zoneinfo import ZoneInfo

API = 'https://api.github.com'
REPO = os.environ['GITHUB_REPOSITORY']
OWNER, NAME = REPO.split('/')
TOKEN = os.environ['GITHUB_TOKEN']
TOPIC = os.environ.get('NTFY_TOPIC', '').strip()
TEST = os.environ.get('TEST', '').lower() == 'true'
LABEL = 'quiet'
HERE = os.path.dirname(os.path.abspath(__file__))


def gh(method, path, body=None):
    url = API + path if path.startswith('/') else path
    req = urllib.request.Request(url, method=method, data=None if body is None else json.dumps(body).encode(),
                                 headers={'Authorization': 'Bearer ' + TOKEN, 'Accept': 'application/vnd.github+json',
                                          'X-GitHub-Api-Version': '2022-11-28', 'User-Agent': 'quiet-alert'})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            text = r.read()
            return json.loads(text) if text else None
    except urllib.error.HTTPError as e:
        if e.code == 422 and path.endswith('/labels'):
            return None  # the label already exists
        raise


def when(s):
    return datetime.datetime.fromisoformat(s.replace('Z', '+00:00'))


def newest_commit():
    """(time, branch) of the newest branch tip, over every branch."""
    q = ('query($owner:String!,$name:String!,$after:String){repository(owner:$owner,name:$name){'
         'refs(refPrefix:"refs/heads/",first:100,after:$after){pageInfo{hasNextPage endCursor}'
         'nodes{name target{... on Commit{committedDate}}}}}}')
    best, after = (None, None), None
    while True:
        refs = gh('POST', '/graphql', {'query': q, 'variables': {'owner': OWNER, 'name': NAME, 'after': after}})
        refs = refs['data']['repository']['refs']
        for n in refs['nodes']:
            if n['name'].startswith('codex/'):
                continue  # an outside worker's pull request says nothing about the Claude allowance
            c = (n.get('target') or {}).get('committedDate')
            if c and (best[0] is None or when(c) > best[0]):
                best = (when(c), n['name'])
        if not refs['pageInfo']['hasNextPage']:
            return best
        after = refs['pageInfo']['endCursor']


def push(title, message, priority, tags, click=None):
    if not TOPIC:
        return
    headers = {'Title': title, 'Priority': priority, 'Tags': tags}
    if click:
        headers['Click'] = click
    try:
        urllib.request.urlopen(urllib.request.Request('https://ntfy.sh/' + TOPIC, data=message.encode(),
                                                      headers=headers, method='POST'), timeout=20).read()
    except Exception as e:  # never print the topic: it is the only key to the owner's phone channel
        print('ntfy push failed:', type(e).__name__)



class AlertSuppressed(Exception):
    """The notification window closed while an evaluation was in progress."""


def validate_config(cfg):
    """Reject ambiguous policy rather than silently widening notification hours."""
    if not isinstance(cfg, dict) or type(cfg.get('paused')) is not bool:
        raise ValueError('paused must be an explicit boolean')
    if not isinstance(cfg.get('tz'), str) or not cfg['tz']:
        raise ValueError('tz must be explicit')
    tz = ZoneInfo(cfg['tz'])
    for key in ('daily_from', 'daily_until'):
        value = cfg.get(key)
        if not isinstance(value, str) or not (re.fullmatch(r'(?:[01][0-9]|2[0-3]):[0-5][0-9]', value)
                                              or (key == 'daily_until' and value == '24:00')):
            raise ValueError(f'{key} must be HH:MM')
    if cfg['daily_from'] >= cfg['daily_until']:
        raise ValueError('daily hours must be a nonempty same-day window')
    for key, minimum in (('quiet_minutes', 1), ('remind_minutes', 1), ('reminders', 0)):
        if type(cfg.get(key)) is not int or cfg[key] < minimum:
            raise ValueError(f'{key} must be an integer >= {minimum}')
    for key in ('test', 'pause_reason', 'pause_review_at', 'through'):
        if key in cfg and not isinstance(cfg[key], str):
            raise ValueError(f'{key} must be a string')
    if cfg.get('through'):
        if datetime.date.fromisoformat(cfg['through']).isoformat() != cfg['through']:
            raise ValueError('through must be YYYY-MM-DD')
    if cfg.get('pause_review_at') and when(cfg['pause_review_at']).utcoffset() is None:
        raise ValueError('pause_review_at must include a timezone')
    return tz


def all_items(path):
    """Bounded, complete history or a visible failure; never infer absence from truncation."""
    items = []
    separator = '&' if '?' in path else '?'
    for page in range(1, 11):
        batch = gh('GET', f'{path}{separator}per_page=100&page={page}')
        if not isinstance(batch, list):
            raise ValueError('incomplete issue/comment history')
        items.extend(batch)
        if len(batch) < 100:
            return items
    raise ValueError('history limit reached; refusing an alert with incomplete deduplication')


def spell_time(issue):
    """Only a valid alert marker can establish an earlier quiet spell."""
    if 'pull_request' in issue or (issue.get('user') or {}).get('login') != 'github-actions[bot]':
        return None
    match = re.search(r'<!-- since ([^<>\n]+) -->', issue.get('body') or '')
    if match:
        try:
            stamp = when(match[1])
            if stamp.utcoffset() is not None:
                return stamp
        except ValueError:
            pass
    return None


def suppression_reason(cfg, local):
    if cfg.get('paused'):
        reason = cfg.get('pause_reason') or 'owner pause (reason not recorded)'
        review = cfg.get('pause_review_at') or 'not set'
        return f'intentional pause: {reason}; review at {review}; manual re-arm only'
    if cfg.get('through') and local.date().isoformat() > cfg['through']:
        return f'expired through date: {cfg["through"]}'
    if not (cfg.get('daily_from', '00:00') <= local.strftime('%H:%M') < cfg.get('daily_until', '24:00')):
        return f'outside daily hours in {cfg.get("tz", "UTC")}'
    return None


def main():
    cfg = json.load(open(os.path.join(HERE, '..', '..', 'docs', 'tracks', 'watch.json'), encoding='utf-8'))
    tz = validate_config(cfg)
    now = datetime.datetime.now(datetime.timezone.utc)
    clock = lambda t: t.astimezone(tz).strftime('%I:%M %p').lstrip('0').lower()
    reason = suppression_reason(cfg, now.astimezone(tz))
    if reason:
        print(f'alerts suppressed: {reason}')
        return  # no GitHub or ntfy writes, including tests or recovery notices
    def require_armed():
        # Recheck before each mutation: API reads can cross the daily cutoff.
        reason = suppression_reason(cfg, datetime.datetime.now(datetime.timezone.utc).astimezone(tz))
        if reason:
            raise AlertSuppressed(reason)

    def write(method, path, body):
        require_armed()
        return gh(method, path, body)

    def notify(*args):
        if TOPIC:
            require_armed()
            push(*args)

    issues_url = f'/repos/{REPO}/issues'
    write('POST', f'/repos/{REPO}/labels', {'name': LABEL, 'color': 'd93f0b',
                                         'description': 'The research went quiet (tools/watch/quiet.py)'})
    test_id = str(cfg.get('test') or '').strip()  # a new value in watch.json sends one test alert, without the Actions page
    if test_id and not TEST:
        done = all_items(f'{issues_url}?state=all&sort=created&direction=desc')
        TEST_TITLE = f'Test of the quiet alert ({test_id})'
        if not any(i.get('title') == TEST_TITLE for i in done):
            i = write('POST', issues_url, {'title': TEST_TITLE, 'body':
                   f'@{OWNER} This is a test of the alert that tells you when the research goes quiet. '
                   'If it reached you, alerts work. Nothing to do.'})
            notify('Regards: test alert', 'If this reached your phone, the quiet alert works. Nothing to do.',
                 'default', 'white_check_mark', i['html_url'])
            write('PATCH', f'{issues_url}/{i["number"]}', {'state': 'closed', 'state_reason': 'completed'})
            print('test alert sent:', i['html_url'], '| phone push:', 'yes' if TOPIC else 'no NTFY_TOPIC secret')
    if TEST:
        i = write('POST', issues_url, {'title': 'Test of the quiet alert', 'body':
               f'@{OWNER} This is a test of the alert that tells you when the research goes quiet. '
               'If it reached you, alerts work. Nothing to do.'})
        notify('Regards: test alert', 'If this reached your phone, the quiet alert works. Nothing to do.',
             'default', 'white_check_mark', i['html_url'])
        write('PATCH', f'{issues_url}/{i["number"]}', {'state': 'closed', 'state_reason': 'completed'})
        print('test alert sent:', i['html_url'], '| phone push:', 'yes' if TOPIC else 'no NTFY_TOPIC secret')
        return
    last, branch = newest_commit()
    if last is None or last.utcoffset() is None or last > now:
        raise ValueError('unknown activity: no eligible commit or invalid/future commit time')
    quiet = (now - last).total_seconds() / 60
    marker = f'<!-- since {last.isoformat()} -->'
    issues = all_items(f'{issues_url}?labels={LABEL}&state=all&sort=created&direction=desc')
    matches = [i for i in issues if spell_time(i) == last]
    # If duplicates already exist, respect a manual closure rather than notify again.
    spell = next((i for i in matches if i['state'] != 'open'), next(iter(matches), None))
    for i in issues:
        previous = spell_time(i)
        if i['state'] == 'open' and previous is not None and previous < last:
            recovery_marker = f'<!-- recovered since {last.isoformat()} -->'
            history = all_items(i['comments_url'])
            if not any(recovery_marker in (c.get('body') or '') for c in history):
                write('POST', f'{issues_url}/{i["number"]}/comments',
                   {'body': f'Commit activity resumed: the newest is from {clock(last)} on `{branch}`. '
                            f'This does not confirm research-session health. Closing.\n\n{recovery_marker}'})
            write('PATCH', f'{issues_url}/{i["number"]}', {'state': 'closed', 'state_reason': 'completed'})
            notify('Regards: commit activity resumed', f'A commit landed at {clock(last)}. Research-session health is unverified.',
                 'default', 'white_check_mark', i['html_url'])
            print('closed', i['html_url'])
    if quiet < cfg.get('quiet_minutes', 50):
        print(f'busy: newest commit {quiet:.0f} minutes ago on {branch}')
        return
    if spell is None:
        body = (f'@{OWNER} No monitored branch (excluding codex/) has received a commit for {quiet:.0f} minutes. '
                f'The newest is from {clock(last)} on `{branch}`.\n\n'
                'This is a commit-activity signal, not proof of a failed research session. '
                'Check owner pause instructions, desk status and usage before deciding what to do. '
                'Do not reset allowance or restart research without owner approval.\n\n'
                'This issue closes itself when commits resume. Close it yourself to silence this quiet spell.\n\n'
                + marker)
        i = write('POST', issues_url, {'title': f'Research quiet since {clock(last)}', 'body': body, 'labels': [LABEL]})
        notify(f'Regards: quiet for {quiet:.0f} min',
             'Check pause instructions, desk status and usage. No restart without owner approval.',
             'high', 'warning', i['html_url'])
        print('alert opened:', i['html_url'])
        return
    if spell['state'] != 'open':
        print('quiet; this spell was already closed by hand')
        return
    comments = all_items(spell['comments_url'])
    reminders = [c for c in comments if (c.get('body') or '').startswith('Still quiet')]
    latest_alert = max([when(spell['created_at'])] + [when(c['created_at']) for c in reminders])
    since_alert = (now - latest_alert).total_seconds() / 60
    if len(reminders) < cfg.get('reminders', 2) and since_alert >= cfg.get('remind_minutes', 120):
        write('POST', f'{issues_url}/{spell["number"]}/comments',
           {'body': f'Still quiet: {quiet:.0f} minutes since the last commit. @{OWNER}'})
        notify(f'Regards: still quiet, {quiet:.0f} min',
             'Check pause instructions, desk status and usage. No restart without owner approval.',
             'high', 'warning', spell['html_url'])
        print('reminder sent')
    else:
        print(f'quiet for {quiet:.0f} minutes; alert already sent')


if __name__ == '__main__':
    try:
        main()
    except AlertSuppressed as e:
        print(f'alerts suppressed: {e}')
