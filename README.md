# tRChapters

testRigor test cases for the `tRChapters` suites, exported from testRigor and kept
under version control. Each `.yaml` file is one remote test case, pinned to it by
`testCaseUuid`, so a file can be renamed or moved without losing the link.

## Suites

| Chapter | Suite | Suite ID | Platform | Tests |
|---|---|---|---|---|
| 8 | tR Android Mobile Automation | `GmDZSeAYdYSDLkSRc` | `ANDROID_30_X86_ULTRA` | 1 |
| 8 | tR Android Mobile Automation Example -01 | `E6xmsGLoubPG6god8` | `ANDROID_36_X86_64_PIXEL_9` | 1 |
| 8 | tR Android Mobile Automation Example -02 | `MkwytBxehMhocoqap` | `ANDROID_35_X86_64_PIXEL_3A` | 1 |
| 8 | tR iOs Mobile Automation Example -03 | `cwHukcm4M9fp6Hkpd` | `IOS_17_5_X86_64_IPHONE_15_PRO` | 2 |
| 8 | tR iOS Mobile Automation Example -04 | `krQLaLXFXKTYS3o4N` | `IOS_27_0_ARM64_IPHONE_17_PRO_MAX` | 1 |
| 8 | tR iOS Mobile Automation Example -05 | `MS56ps8p2r4HN2wFR` | `IOS_17_0_ARM64_IPHONE_XR` | 1 |
| 9 | tR API Automation Example -01 | `4mzAaC3mbavKAWKQk` | `WebDesktopChrome` | 10 |

17 test cases total.

## Layout

```
chapter-08-mobile-automation/
  android-base/            android-example-01/   android-example-02/
  ios-example-03/          ios-example-04/       ios-example-05/
    test-cases/*.yaml
chapter-09-api-automation/
  test-cases/*.yaml
```

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

- `chapter-08-mobile-automation/ios-example-04` — stops part-way through login; never
  reaches the cart, order or logout its name promises.
- `chapter-09-api-automation/api-plus-ui.yaml` — no UI steps at all, despite the name.
- Two cases are still named `debug` (iOS examples 03 and 05).
- Chapter 9 moved POST and PUT off `tr-playground-api.onrender.com` to `httpbin.org`;
  GET and DELETE still point at the Render host, which cold-starts on the free tier
  and is the likely source of intermittent failures.

## Credentials

Every credential here belongs to a public demo application — SauceDemo
(`standard_user` / `secret_sauce`), the testRigor sample app (`bob@example.com` /
`10203040`, `alice` / `mypassword`). Nothing in this repo is a real secret.
