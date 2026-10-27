# Codex dispatch: requests, receipts, and reconciliation

Status: three separate Codex tasks accepted and receipted; an hourly reconciliation dispatcher is configured. End-to-end result/review verification remains pending.
Investigated 26 October 2026, approximately 22:40 EDT (27 October 02:40 UTC).
Repository baseline: `71825ae52ef1b8ea24d4bef7ea4459b3aff94f03`.

## Initial investigation (before authenticated reconciliation)

- Issues [28](https://github.com/jampotful/seen-back/issues/28), [29](https://github.com/jampotful/seen-back/issues/29), and [30](https://github.com/jampotful/seen-back/issues/30) contain a mention in their original bodies. At inspection they had no comments or task links; the requested engineering and data branches were absent and no corresponding pull requests were visible.
- All 27 workflow files on main were inspected. None handles `issues` or `issue_comment` events or invokes Codex. GitHub's workflow-run API returned zero runs for each of those two event types. The quiet-alert workflow observes repository activity; it does not launch Codex.
- The GitHub connection can read the repository and reports push/admin permission. The accessible app installation selects all repositories and subscribes to issue events, among others. Event subscription and repository access do not establish that an issue mention is an execution trigger, that Codex has a usable environment, or that the account has available usage.
- OpenAI's [GitHub integration documentation](https://learn.chatgpt.com/docs/third-party/github) documents review requests in pull-request comments and other tasks using a pull request as context. It does not document an ordinary issue-body mention as this workflow's launch mechanism.
- The desk's previous wording explicitly said an issue mention might start a round "if that works". No acceptance receipt connected any of these three requests to a Codex task. This is a confirmed dispatch/observability gap, not proof of a stopped or nonexistent agent.
- Issue [26](https://github.com/jampotful/seen-back/issues/26) was created at 04:07:40 UTC and PR [27](https://github.com/jampotful/seen-back/pull/27) at 04:21:44 UTC. The PR has no task link identifying its launch mechanism. Although GitHub records `merged=false`, the desk's [closing comment](https://github.com/jampotful/seen-back/pull/27#issuecomment-6408499738) says it incorporated the findings through the branch. That is consistent with the desk's existing review procedure.
- No Regards scheduled task was returned by the connected ChatGPT automation lookup. This is not a list of Codex Cloud chats.
- The available browser reached a sign-in screen rather than an authenticated Codex task list. An attempt to run the documented read-only `codex cloud list --json --limit 20` on the connected Mac timed out at the remote-tool boundary. Neither result says that any research task failed.

## Recovery ledger — do not launch from silence

| Issue | Assignment | Existing prompt | Output | Execution state |
|---|---|---|---|---|
| #28 | Plant screening, requested as 20 batches / 701 genera | `docs/tracks/prompts/codex-round.md` | One round PR, batch progress and evidence checks | Accepted: [existing task](https://chatgpt.com/local/01a17b61-4607-7408-a742-6cf27748a0d6); follow operational ledger, do not resubmit |
| #29 | Six engineering corrections | `docs/tracks/prompts/codex-eng-1.md` | `codex/eng-1`, one PR, tests and per-view count deltas | Accepted: [existing task](https://chatgpt.com/local/01a17b5f-39c8-7350-b5b6-c4fefaa9b0c8); follow operational ledger, do not resubmit |
| #30 | Synonyms, homonyms, wanted-reference proposals | `docs/tracks/prompts/codex-data-1.md` | `codex/data-1`, one PR, row counts and checks | Accepted: [existing task](https://chatgpt.com/local/01a17b5f-fede-72d7-9d94-ae0affff10f4); follow operational ledger, do not resubmit |

The count in #28 is the request's snapshot, not a fresh computed queue count. On an authorized retry, refresh main and compute the current queue, respecting holds and pending branches. Do not substitute a new broad research sweep.

## Supported launch and status interface

OpenAI documents [Codex Cloud CLI submission and listing](https://learn.chatgpt.com/docs/cli/reference). Use an authenticated, authorized host with its existing ChatGPT account. Do not put login credentials into GitHub or add an API billing fallback.

1. Identify the actual Regards cloud environment in the authenticated Codex interface. Confirm its repository, branch, network/tool access and model settings. Do not infer an environment ID from a repository ID.
2. List its tasks using `codex cloud list --env <verified-environment-id> --json --limit 20`, following every returned `--cursor` needed to cover the relevant requests. Inspect task details, including differently titled or manually launched tasks, before deciding that an issue is unstarted. Listing is experimental; validate the installed CLI's help and returned schema.
3. Adopt a matching existing task by recording its real task URL/ID, environment, assignment and observed status in the issue. If it is running, monitor that task. If completed, inspect its result before submitting anything new. An empty or failed lookup is not evidence of absence.
4. Only after establishing that the assignment is unstarted, submit ONE task with `codex cloud exec --env <verified-environment-id> --attempts 1 <prompt>`. The prompt must identify `jampotful/seen-back#<issue>`, refresh main, follow the corresponding unchanged task prompt, retain the required branch/output scope, and preserve desk review. The requested plant round's model/effort is GPT-6.1 Sol / High.
5. Save the returned task URL/ID immediately and post a receipt in the issue. A nonzero exit, timeout or lost response requires reconciliation before a retry: the service may have accepted a request whose reply was lost.
6. Verify a real running, failed, blocked or completed status from Codex; do not label an issue "running" merely because a command was sent.

Suggested receipt fields (actual values only):

```text
Assignment: jampotful/seen-back#29
Task: <returned URL and ID>
Environment: <verified ID>
Submitted at: <UTC timestamp>
Observed status: <status and observation time>
Output branch: codex/eng-1
Review: research desk; no automatic merge
```

## Requirements for unattended operation

The following remains the acceptance checklist. The hourly dispatcher described below has been configured; a complete result/review cycle is still required before declaring full recovery.

- One configured dispatcher owns launch decisions; use a durable atomic claim keyed by repository and issue. Keep independent claims and tasks for #28, #29 and #30.
- Accept only authorized desk/owner assignments with recognized prompt paths. Never turn arbitrary public issue text into unrestricted instructions.
- Keep durable states: requested, reconciling, submitting, accepted, running, blocked/failed, result-ready, reviewed. An unknown submission outcome stays held until reconciled; a heartbeat timeout alone must not launch a duplicate.
- Write a task receipt before reporting acceptance. Monitor task status even when unrelated repository commits continue. Alert on missing receipts or blocked executions, not only a quiet repository.
- Recover tasks that finished without opening a PR; inspect and publish the existing result before retrying research. Check branch/PR identity and current queue coverage at each handoff.
- Preserve each assignment's tests, file restrictions and PR requirements. Do not combine engineering/data proposals with the plant round.
- The research desk audits outputs, applies accepted work through the branch, and closes the PR with its disposition. Do not automatically merge, close assignments merely on submission, regenerate published gap files as part of #29, or release OA holds without the desk's existing gate.
- Reuse the account's existing allowance. Authentication, usage limits and network failures become visible blocked states. Do not silently switch to a paid API or purchase capacity.
- Prove one end-to-end launch/receipt/result/review cycle and a repeated-delivery duplicate-suppression test before calling the workflow restored.

## Authenticated reconciliation and activation — 27 October 2026 UTC

The account's authenticated Codex history (sorted by last update), archive, task contents, issue receipts and repository branches/PRs were reconciled. No task matching the three October 26 requests was found. Search alone was not treated as conclusive: the UI warns that some cloud messages can be absent from search. The latest pre-existing Codex task was the completed audit below; the preceding research round was dated October 17 and ended blocked. The archive had no matching task.

The [audit chat](https://chatgpt.com/local/01a17653-7dbd-7465-982d-7b9aa62f00d2) contains a direct owner instruction to audit the repo and its final response links PR #27. This identifies that contribution's actual chat; the issue-to-PR timestamp comparison alone did not establish an issue trigger.

The existing private `seen-back` environment names `jampotful/seen-back`, installs `requests` and `pypdf`, and already permits public internet access. No network permissions or credential settings were widened. Opening the environment's Edit control created an inspection draft; no environment changes were published.

Each request was submitted once in its own cloud chat using GPT-6.1 Sol / High. All three showed Working and received GitHub issue comments with their real task URLs:
- [#28 receipt](https://github.com/jampotful/seen-back/issues/28#issuecomment-6432940952)
- [#29 receipt](https://github.com/jampotful/seen-back/issues/29#issuecomment-6432913248)
- [#30 receipt](https://github.com/jampotful/seen-back/issues/30#issuecomment-6432928724)

Acceptance is not completion. The plant coordinator subsequently checked out exact main `96225855ff44ad1bdb15cc365314b3b4e06cb284`, created `codex/round-2026-10-27-issue-28`, computed **20 batches / 644 genera**, and launched six batch workers. Engineering subsequently completed with [PR #35](https://github.com/jampotful/seen-back/pull/35), ready for desk review and unmerged: all six requested fixes, six passing view-test scripts, and nine unchanged baseline senses-check failures. Its six changed files stay within the authorized tools/test scope. Data initially ended with a [proxy-access blocker](https://github.com/jampotful/seen-back/issues/30#issuecomment-6432950889), without edits; recovery continued in the same chat, not a duplicate task. The plant coordinator then reported successful fetches through supported network-enabled command execution. That evidence was sent to the data chat. Its [correction/resumption receipt](https://github.com/jampotful/seen-back/issues/30#issuecomment-6433052434) confirms Git fetch success and GBIF HTTP 200 through the supported network-enabled execution mode, without altering the enforcement proxy or TLS. The task resumed on `codex/data-1`; all 211 B1 wanted records were accounted for and registry verification continued. The earlier platform-outage diagnosis is superseded.

## Operational dispatcher

The ChatGPT automation **Regards Codex dispatcher** is an hourly condition check, using the existing GitHub connection and Codex account. This is scheduled polling, not a GitHub issue webhook: the available automation integration exposes pull-request events and explicitly excludes non-PR issue events.

The durable ledger is [docs/tracks/codex-dispatch-state.json on codex/dispatch-state](https://github.com/jampotful/seen-back/blob/codex/dispatch-state/docs/tracks/codex-dispatch-state.json). This is an operational branch, **not a PR to merge into main**. It records accepted task URLs, dispatch keys, observations, blockers and recovery attempts. Treat it and the issue receipts as the task-ownership record.

The saved automation:
1. Reconciles linked tasks and repository results. Quiet GitHub activity does not trigger a retry.
2. Accepts only open requests authored by `jampotful` explicitly addressing Codex and naming one of the three recognized prompt paths. It checks overlapping tasks and queue coverage before any new submission.
3. Acquires a durable claim before sending a new task: a commit parented to the current state-branch head, then a non-forced update with `expected_sha`. Conflicts require rereading and reconciliation. A submitting/unknown claim never expires into permission to submit again.
4. Immediately records the persisted task URL and actual observed status in the ledger and issue. Lost submission responses remain held.
5. Recovers stopped work in its **existing chat** only, with bounded attempts per blocker signature; it never sends continuation prompts to a task still Working. New diagnostic evidence is distinguished from a blind retry.
6. Preserves all assignment boundaries, original checks, OA holds and desk review/application. It never merges, closes issues on acceptance, buys capacity, or silently switches to API billing.

The initial three ledger entries were reread as owned assignments: repeat delivery means adopt/monitor, with no additional submission. A stale-head write probe returned an error and the branch head remained unchanged; the connector surfaced a generic GraphQL error, so this is **not** a cleanly diagnosed concurrency test. The first reconciliation pass inspected all three linked tasks, their comments, matching branches and PRs. It adopted #28/#30 as running and #29 as result-ready, with zero new submissions or continuation prompts. Duplicate delivery of all three was suppressed. The complete result/desk-review cycle still remains to be observed.

## Remaining verification

Follow the three existing tasks through execution, validation and ready-for-review PRs, then the desk's disposition. The first reconciliation used authenticated task access and suppressed duplicate delivery; continue checking that later passes retain access. If access, usage or execution fails, retain task ownership and expose a concrete blocker; do not turn silence or an expired session into a new task. The original dispatch/visibility gap is repaired with actual submissions and receipts; complete autonomous operation is not yet proven.
