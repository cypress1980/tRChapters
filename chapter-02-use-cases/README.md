# Chapter 2 — Use Cases

First contact with testRigor's plain-English commands, worked against live public
sites (Amazon, Best Buy) rather than a controlled demo app.

| Directory | Suite ID | Tests | Focus |
|---|---|---|---|
| `example-001/` | [`jWwko9ksyc6RQT7pZ`](https://app.testrigor.com/test-suites/jWwko9ksyc6RQT7pZ/test-cases) | 10 | product search, add to cart, form validation |
| `example-002/` | [`wfGesuhM5Desq5NGG`](https://app.testrigor.com/test-suites/wfGesuhM5Desq5NGG/test-cases) | 4 | Apple Watch / Kindle search, guest checkout |
| `example-003/` | [`hpDJ8KQZNSpuFjQv7`](https://app.testrigor.com/test-suites/hpDJ8KQZNSpuFjQv7/test-cases) | 2 | new customer registration |
| `example-004/` | [`QukEEJfAJuy8nQraL`](https://app.testrigor.com/test-suites/QukEEJfAJuy8nQraL/test-cases) | 5 | Samsung phone search across two retailers |

## Reading these

Many cases here carry long runs of `scroll down` / `scroll up` / `go back` /
`reload`, and several end without the assertion their name promises. That is a
faithful record of iterating against real retail sites, where layouts shift and
product listings rotate. They are kept as written.

The form-validation case in `example-001/` exists in three near-identical copies
differing only in the password (`SecurePass@123` vs `SecurePass123!`). The same
directory also holds `check-that-form-is-working.yaml`, a single-line case
(`in the field for name write the name`) that never grew past a sketch.

`example-004/` is the clearest pair for teaching: the same goal — add a Samsung
phone to the cart — written for Amazon and then for Best Buy, where the Amazon
version lands in ten steps and the Best Buy version sprawls past forty.
