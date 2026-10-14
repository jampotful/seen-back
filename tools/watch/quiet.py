"""Tells the owner when the research goes quiet, so a used-up Claude allowance gets its reset while they are away.

Run by .github/workflows/quiet-alert.yml every 15 minutes. It uses the GitHub API (GITHUB_TOKEN) and none of the Claude
allowance, because a Claude session that has hit its limit cannot send anything itself.

docs/tracks/watch.json arms it. Inside the daily window, on days up to and including "through", when no branch has
received a commit for quiet_minutes, it opens one issue labelled "quiet" that mentions the owner (GitHub notifies
them, by email unless they turned that off) and, when the repository secret NTFY_TOPIC is set, sends a phone push
through ntfy.sh. One quiet spell gets one issue. While the issue stays open and the repository stays quiet, the alert
repeats every remind_minutes, at most "reminders" times. When commits resume, the issue closes with a note and a second
push says so. Closing the issue by hand silences that spell. Over the 30 hours of steady work before this was written,
the longest gap between commits was 46 minutes.

By hand: Actions > quiet-alert > Run workflow, with "test" ticked, sends one test alert and closes it at once. A new value
of "test" in watch.json does the same at the next scheduled run, once."""
import datetime, json, os, urllib.error, urllib.request
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


def armed(cfg, local):
    if cfg.get('paused'):
        return False
    if cfg.get('through') and local.date().isoformat() > cfg['through']:
        return False
    return cfg.get('daily_from', '00:00') <= local.strftime('%H:%M') < cfg.get('daily_until', '24:00')


def main():
    cfg = json.load(open(os.path.join(HERE, '..', '..', 'docs', 'tracks', 'watch.json'), encoding='utf-8'))
    tz = ZoneInfo(cfg.get('tz', 'UTC'))
    now = datetime.datetime.now(datetime.timezone.utc)
    clock = lambda t: t.astimezone(tz).strftime('%I:%M %p').lstrip('0').lower()
    issues_url = f'/repos/{REPO}/issues'
    gh('POST', f'/repos/{REPO}/labels', {'name': LABEL, 'color': 'd93f0b',
                                         'description': 'The research went quiet (tools/watch/quiet.py)'})
    test_id = str(cfg.get('test') or '').strip()  # a new value in watch.json sends one test alert, without the Actions page
    if test_id and not TEST:
        done = gh('GET', f'{issues_url}?state=all&sort=created&direction=desc&per_page=30') or []
        TEST_TITLE = f'Test of the quiet alert ({test_id})'
        if not any(i.get('title') == TEST_TITLE for i in done):
            i = gh('POST', issues_url, {'title': TEST_TITLE, 'body':
                   f'@{OWNER} This is a test of the alert that tells you when the research goes quiet. '
                   'If it reached you, alerts work. Nothing to do.'})
            push('Regards: test alert', 'If this reached your phone, the quiet alert works. Nothing to do.',
                 'default', 'white_check_mark', i['html_url'])
            gh('PATCH', f'{issues_url}/{i["number"]}', {'state': 'closed', 'state_reason': 'completed'})
            print('test alert sent:', i['html_url'], '| phone push:', 'yes' if TOPIC else 'no NTFY_TOPIC secret')
    if TEST:
        i = gh('POST', issues_url, {'title': 'Test of the quiet alert', 'body':
               f'@{OWNER} This is a test of the alert that tells you when the research goes quiet. '
               'If it reached you, alerts work. Nothing to do.'})
        push('Regards: test alert', 'If this reached your phone, the quiet alert works. Nothing to do.',
             'default', 'white_check_mark', i['html_url'])
        gh('PATCH', f'{issues_url}/{i["number"]}', {'state': 'closed', 'state_reason': 'completed'})
        print('test alert sent:', i['html_url'], '| phone push:', 'yes' if TOPIC else 'no NTFY_TOPIC secret')
        return
    last, branch = newest_commit()
    quiet = (now - last).total_seconds() / 60
    marker = f'<!-- since {last.isoformat()} -->'
    issues = gh('GET', f'{issues_url}?labels={LABEL}&state=all&sort=created&direction=desc&per_page=10') or []
    spell = next((i for i in issues if marker in (i.get('body') or '')), None)
    for i in issues:  # an open alert from an earlier spell means commits have resumed since it opened
        if i['state'] == 'open' and i is not spell:
            gh('POST', f'{issues_url}/{i["number"]}/comments',
               {'body': f'Commits resumed: the newest is from {clock(last)} on `{branch}`. Closing.'})
            gh('PATCH', f'{issues_url}/{i["number"]}', {'state': 'closed', 'state_reason': 'completed'})
            push('Regards: running again', f'A commit landed at {clock(last)}. Nothing to do.',
                 'default', 'white_check_mark', i['html_url'])
            print('closed', i['html_url'])
    if quiet < cfg.get('quiet_minutes', 50):
        print(f'busy: newest commit {quiet:.0f} minutes ago on {branch}')
        return
    if not armed(cfg, now.astimezone(tz)):
        print(f'quiet for {quiet:.0f} minutes, outside the alert window')
        return
    if spell is None:
        body = (f'@{OWNER} No branch has received a commit for {quiet:.0f} minutes. '
                f'The newest is from {clock(last)} on `{branch}`.\n\n'
                "The usual cause is a used-up Claude allowance. Open Claude's usage page, and if a meter is full, "
                'press the reset. Then open the research desk thread and send: continue\n\n'
                'If no meter is full, the desk stopped for another reason, and the same message restarts it. '
                'This issue closes itself when commits resume. Close it yourself to silence this quiet spell.\n\n'
                + marker)
        i = gh('POST', issues_url, {'title': f'Research quiet since {clock(last)}', 'body': body, 'labels': [LABEL]})
        push(f'Regards: quiet for {quiet:.0f} min',
             'Check Claude usage. If a meter is full, press reset, then send "continue" to the research desk.',
             'high', 'warning', i['html_url'])
        print('alert opened:', i['html_url'])
        return
    if spell['state'] != 'open':
        print('quiet; this spell was already closed by hand')
        return
    comments = gh('GET', spell['comments_url'] + '?per_page=100') or []
    reminders = [c for c in comments if (c.get('body') or '').startswith('Still quiet')]
    since_alert = (now - when(reminders[-1]['created_at'] if reminders else spell['created_at'])).total_seconds() / 60
    if len(reminders) < cfg.get('reminders', 2) and since_alert >= cfg.get('remind_minutes', 120):
        gh('POST', f'{issues_url}/{spell["number"]}/comments',
           {'body': f'Still quiet: {quiet:.0f} minutes since the last commit. @{OWNER}'})
        push(f'Regards: still quiet, {quiet:.0f} min',
             'Check Claude usage. If a meter is full, press reset, then send "continue" to the research desk.',
             'high', 'warning', spell['html_url'])
        print('reminder sent')
    else:
        print(f'quiet for {quiet:.0f} minutes; alert already sent')


if __name__ == '__main__':
    main()
