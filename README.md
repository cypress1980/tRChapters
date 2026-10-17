# tRChapters

Every chapter test suite from testRigor, exported and kept under version control.
**80 test cases across 39 suites.** Each `.yaml` file is one remote test case,
pinned to it by `testCaseUuid`, so a file can be renamed or moved without losing
the link.

| Chapter | Directory | Suites | Tests | Subject |
|---|---|---|---|---|
| 2 | `chapter-02-use-cases/` | 4 | 21 | first plain-English commands on live retail sites |
| 4 | `chapter-04-use-cases/` | 3 | 5 | grabbing and validating values |
| 5 | `chapter-05-use-cases/` | 10 | 14 | loops, conditionals, generated data |
| 6 | `chapter-06-use-cases/` | 14 | 17 | iframes, shadow DOM, email, QR, 2FA, audio |
| 8 | `chapter-08-mobile-automation/` | 6 | 7 | native iOS and Android |
| 9 | `chapter-09-api-automation/` | 1 | 10 | `call api`, `mock api` |
| — | `chapter-wise/` | 1 | 6 | end-to-end checkout on shop.qaautomationlabs.com |

Each chapter directory has its own README describing what the suites cover.

## Suite IDs — Chapters 8 and 9

| Chapter | Suite | Suite ID | Platform | Tests |
|---|---|---|---|---|
| 8 | tR Android Mobile Automation | `GmDZSeAYdYSDLkSRc` | `ANDROID_30_X86_ULTRA` | 1 |
| 8 | tR Android Mobile Automation Example -01 | `E6xmsGLoubPG6god8` | `ANDROID_36_X86_64_PIXEL_9` | 1 |
| 8 | tR Android Mobile Automation Example -02 | `MkwytBxehMhocoqap` | `ANDROID_35_X86_64_PIXEL_3A` | 1 |
| 8 | tR iOs Mobile Automation Example -03 | `cwHukcm4M9fp6Hkpd` | `IOS_17_5_X86_64_IPHONE_15_PRO` | 2 |
| 8 | tR iOS Mobile Automation Example -04 | `krQLaLXFXKTYS3o4N` | `IOS_27_0_ARM64_IPHONE_17_PRO_MAX` | 1 |
| 8 | tR iOS Mobile Automation Example -05 | `MS56ps8p2r4HN2wFR` | `IOS_17_0_ARM64_IPHONE_XR` | 1 |
| 9 | tR API Automation Example -01 | `4mzAaC3mbavKAWKQk` | `WebDesktopChrome` | 10 |

IDs for Chapters 2, 4, 5, 6 and Chapter Wise are in each chapter's README.

## Layout

One directory per testRigor suite, because a `testCaseUuid` belongs to exactly one
suite — a flat layout would make it easy to push a file against the wrong one.

```
chapter-0N-.../<suite>/test-cases/*.yaml
chapter-09-api-automation/test-cases/*.yaml     # single suite, no sub-directory
```

## Re-exporting

`.tools/export.py` pulls every suite in `.tools/suites.json` and rewrites its
directory. It skips any suite directory that already holds YAML, so an interrupted
run resumes where it stopped; delete a directory to force a refresh.

```bash
TESTRIGOR_API_KEY="<your PAT>" python3 .tools/export.py
```

The script reads the token from the environment and never stores it.

## File format

```yaml
# Suite: <name> (<suite id>)
# Test case name: "<the description shown in the testRigor UI>"
customSteps: |
  <plain-English testRigor steps, verbatim>
labels: [generated-by-ai]          # only where the remote case has labels
testCaseUuid: "<remote test case uuid>"
```

Commented-out steps (`//`) are preserved exactly as they are stored remotely. In
several cases they are the more useful half of the file — see Chapter 8's
`ios-example-03`, which carries ~70 failed attempts at the iOS password field.

## Pushing changes back

```bash
export TESTRIGOR_API_KEY="<your PAT>"    # username menu -> API Tokens
testrigor test-suite run <SUITE_ID> --test-cases-path "chapter-09-api-automation/test-cases/**/*.yaml"
```

Because every file carries a `testCaseUuid`, this **updates those exact remote test
cases and then executes the suite**. It is not a dry run. Push one suite's directory
at a time — the UUIDs in one chapter folder belong to that chapter's suite only.

## Known issues in the exported tests

Recorded, not fixed — these are faithful to what is stored in testRigor.

- `chapter-08-mobile-automation/ios-example-04` — stops part-way through login; never
  reaches the cart, order or logout its name promises.
- `chapter-09-api-automation/api-plus-ui.yaml` — no UI steps at all, despite the name.
- `chapter-02-use-cases/example-001` — the same form-validation case exists three
  times, differing only in the password; `check-that-form-is-working.yaml` is a
  single unfinished line.
- `chapter-05-use-cases/example-007` — four live-mode scratch cases, one still named
  `live-session-1788939641074`.
- Cases still named `debug` or `demo`: iOS examples 03 and 05, Chapter 5 example-007,
  Chapter 6 example-013.
- Chapter 9 moved POST and PUT off `tr-playground-api.onrender.com` to `httpbin.org`;
  GET and DELETE still point at the Render host, which cold-starts on the free tier
  and is the likely source of intermittent failures.

## Credentials

Every credential here belongs to a public demo application — SauceDemo
(`standard_user` / `secret_sauce`), the testRigor sample app (`bob@example.com` /
`10203040`, `alice` / `mypassword`), shop.qaautomationlabs.com (`demo@demo.com` /
`demo`), and throwaway `@testrigor-mail.com` addresses. The card number in
Chapter 2's Best Buy checkout is the standard `4111111111111111` test value.
Nothing in this repo is a real secret.
