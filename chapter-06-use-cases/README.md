# Chapter 6 — Hard Things

One suite per browser or platform feature that normally needs a workaround.

| Directory | Suite ID | Tests | Feature |
|---|---|---|---|
| `example-001/` | `c4zZsFYTRQ39o26wC` | 1 | create a record |
| `example-002/` | `zXxr5GrqfxXLZjjqy` | 1 | edit and update a record |
| `example-003/` | `mc3KrJxYt2LNcXMZE` | 1 | click inside an iframe |
| `example-004/` | `Kr4k5RqfEZemCng2Y` | 1 | nested iframes |
| `example-005/` | `cwvFYEiRixJtWo9dz` | 1 | shadow DOM, open and closed |
| `example-006/` | `Y7ma5xWyBcfD9xj3N` | 1 | popup windows |
| `example-007/` | `jWPqwkWaeW8dn83qa` | 2 | tab switching |
| `example-008/` | `DLpr9ptodoc2HyvWD` | 1 | file upload |
| `example-009/` | `FfW3veHbkuhcf5T3f` | 1 | file download |
| `example-010/` | `dNouyaBj4PW3tbdji` | 1 | email delivery and confirmation |
| `example-011/` | `8wqktf2nQ9cqnkwyE` | 1 | QR code scanning |
| `example-012-2fa/` | `Qkz6BvTWGXAEwsi8a` | 2 | two-factor authentication |
| `example-013-audio-recording/` | `WfzKodW6pQZNgmk7t` | 2 | audio |
| `example-014-audio-recording/` | `QSTemnBXhTYJakPac` | 1 | audio |

## Highlights

**Shadow DOM** (`example-005/`) needs no special syntax at all — open and closed
roots are addressed exactly like any other field.

**Email** (`example-010/`) covers both directions: sending and asserting delivery,
then a signup that generates its own address, confirms it from the received mail,
and checks the greeting with an expression:

```
generate unique email, then enter into "Email" and save as "generatedEmail"
...
check that email to stored value "generatedEmail" was delivered
click "Confirm email"
check that page contains expression "Hello, ${generatedName}"
```

**QR codes** (`example-011/`) documents both routes — scanning from a live page
(commented out) and from a stored image (active):

```
scan qr code value from stored value "QRCode" and save it as "code"
check that the stored value "code" itself contains "wikipedia.org"
```

Chapters 13 and 14 both cover audio and both contain a test named `Audio Testing`;
13 adds an `audio debug` case.
