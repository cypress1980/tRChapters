# Chapter 8 — Mobile Automation

Native iOS and Android suites. One directory per testRigor suite, because each
targets a different device profile and each test case's UUID belongs to exactly
one suite.

| Directory | Suite ID | Device |
|---|---|---|
| `android-base/` | [`GmDZSeAYdYSDLkSRc`](https://app.testrigor.com/test-suites/GmDZSeAYdYSDLkSRc/test-cases) | Android 30, Ultra |
| `android-example-01/` | [`E6xmsGLoubPG6god8`](https://app.testrigor.com/test-suites/E6xmsGLoubPG6god8/test-cases) | Android 36, Pixel 9 |
| `android-example-02/` | [`MkwytBxehMhocoqap`](https://app.testrigor.com/test-suites/MkwytBxehMhocoqap/test-cases) | Android 35, Pixel 3a |
| `ios-example-03/` | [`cwHukcm4M9fp6Hkpd`](https://app.testrigor.com/test-suites/cwHukcm4M9fp6Hkpd/test-cases) | iOS 17.5, iPhone 15 Pro |
| `ios-example-04/` | [`krQLaLXFXKTYS3o4N`](https://app.testrigor.com/test-suites/krQLaLXFXKTYS3o4N/test-cases) | iOS 27, iPhone 17 Pro Max |
| `ios-example-05/` | [`MS56ps8p2r4HN2wFR`](https://app.testrigor.com/test-suites/MS56ps8p2r4HN2wFR/test-cases) | iOS 17, iPhone XR |

## What each suite covers

- **android-base** — post-install smoke test. Asserts the absence of crash strings
  ("unfortunately", "has stopped", "error") before asserting the product list.
- **android-example-01** — full SauceDemo purchase. Reaches the cart via the
  accessibility id `test-Cart` rather than a visual descriptor.
- **android-example-02** — testRigor sample app: Echo Box, Login Screen, and a
  `restart app` followed by the List Demo dialog.
- **ios-example-03** — the OCR login. `click "More" using OCR only` is what finally
  worked after the long list of commented-out attempts in the same file.
- **ios-example-04** — incomplete, see root README.
- **ios-example-05** — SauceDemo purchase driven almost entirely by `using ai`.

## The iOS password field

iOS secure text fields resisted every ordinary descriptor. What failed, recorded in
`ios-example-03/test-cases/login-add-to-cart-place-order.yaml`: coordinate taps,
`accessibility id "test-Password"`, `secure text field`, `2nd text field`, matching
the bullet glyphs (`••••••••`), per-character `type`, and natural-language
`sign in with username ... and password ...`.

What worked: OCR for navigation, then `enter "..." into input "Password"`.
