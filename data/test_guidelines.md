# Test Guidelines (Team Falcon)

## Coverage
- Minimum line coverage for every service is 82%.
- New code in a PR must have at least 90% coverage.
- PRs that drop overall coverage by more than 0.5% are blocked by CI.

## Test types
- Unit tests live in `tests/unit/` and must run in under 2 minutes in total.
- Integration tests live in `tests/integration/` and run only on the `main` branch and release branches.
- End-to-end tests run in the `nightly-regression` job at 02:00 IST.

## Naming rules
- Test files: `test_<module>.py`.
- Test functions: `test_<what>_<expected_result>`, for example `test_login_with_bad_password_returns_401`.
- CI job names: `<service>-<test-type>`, for example `payments-unit` or `payments-integration`.

## Flaky tests
- A test that fails and then passes on retry without code changes is marked flaky.
- Flaky tests must be tagged `@pytest.mark.flaky` and get a ticket in the FLAKY Jira project.
- A flaky test must be fixed or deleted within 10 working days.
- If a service has more than 5 open flaky tickets, it cannot be released until they are below 5.

## Test data
- Never use production data in tests.
- Shared fixtures live in `tests/conftest.py`.
