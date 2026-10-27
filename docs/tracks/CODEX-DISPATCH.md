# Codex dispatch: requests, receipts, and reconciliation

Status: recovery procedure prepared; autonomous dispatcher NOT installed or verified.
Investigated 26 October 2026, approximately 22:40 EDT (27 October 02:40 UTC).
Repository baseline: `71825ae52ef1b8ea24d4bef7ea4459b3aff94f03`.

## What the investigation establishes

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
| #28 | Plant screening, requested as 20 batches / 701 genera | `docs/tracks/prompts/codex-round.md` | One round PR, batch progress and evidence checks | Unknown: reconcile existing Codex chats before retry |
| #29 | Six engineering corrections | `docs/tracks/prompts/codex-eng-1.md` | `codex/eng-1`, one PR, tests and per-view count deltas | Unknown: reconcile existing Codex chats before retry |
| #30 | Synonyms, homonyms, wanted-reference proposals | `docs/tracks/prompts/codex-data-1.md` | `codex/data-1`, one PR, row counts and checks | Unknown: reconcile existing Codex chats before retry |

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

The following is the acceptance checklist for the dispatcher still to be installed, not a claim that it exists.

- One configured dispatcher owns launch decisions; use a durable atomic claim keyed by repository and issue. Keep independent claims and tasks for #28, #29 and #30.
- Accept only authorized desk/owner assignments with recognized prompt paths. Never turn arbitrary public issue text into unrestricted instructions.
- Keep durable states: requested, reconciling, submitting, accepted, running, blocked/failed, result-ready, reviewed. An unknown submission outcome stays held until reconciled; a heartbeat timeout alone must not launch a duplicate.
- Write a task receipt before reporting acceptance. Monitor task status even when unrelated repository commits continue. Alert on missing receipts or blocked executions, not only a quiet repository.
- Recover tasks that finished without opening a PR; inspect and publish the existing result before retrying research. Check branch/PR identity and current queue coverage at each handoff.
- Preserve each assignment's tests, file restrictions and PR requirements. Do not combine engineering/data proposals with the plant round.
- The research desk audits outputs, applies accepted work through the branch, and closes the PR with its disposition. Do not automatically merge, close assignments merely on submission, regenerate published gap files as part of #29, or release OA holds without the desk's existing gate.
- Reuse the account's existing allowance. Authentication, usage limits and network failures become visible blocked states. Do not silently switch to a paid API or purchase capacity.
- Prove one end-to-end launch/receipt/result/review cycle and a repeated-delivery duplicate-suppression test before calling the workflow restored.

## Remaining gate

Authenticated Codex task and environment access is needed to reconcile #28–30 and configure a real dispatcher. No assignment has been retried by this investigation. The current state is **execution unknown**, not **unstarted**. Preserve that distinction until an authoritative status check resolves it.
