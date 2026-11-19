# Release Process (Team Falcon)

## Schedule
- Production releases go out every Thursday at 14:00 IST.
- No releases on the last Friday of a quarter (code freeze).
- Hotfixes can ship any weekday before 18:00 IST.

## Branch naming
- Release branches are named `release/YYYY.MM.N`, for example `release/2026.11.2`.
- Hotfix branches are named `hotfix/<ticket-id>`, for example `hotfix/FAL-1423`.

## Approvals
- Every release needs approval from the Release Captain for that week.
- The Release Captain rotates weekly; the current list lives in the #falcon-release Slack channel.
- A release needs 2 approvals on the release PR: the Release Captain and one QA engineer.

## Steps
1. Cut the release branch from `main` on Wednesday by 17:00 IST.
2. Run the full regression suite (`nightly-regression` job); it must be green.
3. Deploy to staging and run smoke tests for at least 2 hours.
4. Get approvals, then deploy to production on Thursday at 14:00 IST.
5. Post release notes in #falcon-release within 1 hour of deploying.

## Rollback
- If error rate rises above 2% within 30 minutes of a release, roll back immediately.
- Rollback command: `falconctl rollback --to previous`.
