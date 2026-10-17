# Chapter 9 — API Automation

Suite [`4mzAaC3mbavKAWKQk`](https://app.testrigor.com/test-suites/4mzAaC3mbavKAWKQk/test-cases) (`WebDesktopChrome`) — 10 test cases, building from a bare
GET up to mocking a response and feeding it into a UI flow.

| File | Covers |
|---|---|
| `get-api.yaml` | `call api get`, assert http code |
| `get-api-result-and-enter-into-ui.yaml` | JSONPath `$.code` into a textarea |
| `post-api.yaml` | POST with headers + JSON body |
| `put-api.yaml` | PUT, grab `$.json.name` |
| `delete-api.yaml` | DELETE with a multiline `[END]` body, assert response text |
| `qa-automation-post.yaml` | POST a flight record, expect 201 |
| `api-plus-ui.yaml` | three values from randomuser.me (no UI — unfinished) |
| `get-and-used-values-in-ui.yaml` | API values drive a full SauceDemo checkout |
| `get-post-put-and-delete.yaml` | all four verbs chained against one resource |
| `mock-api.yaml` | `mock api call` intercepting a live endpoint |

## Request-body styles

Inline, escaped — most cases:

```
and body "{\"origin\":\"JFK\",\"destination\":\"LHR\"}"
```

Multiline, delimited — `delete-api.yaml`, readable for larger payloads:

```
and body text starting from next line and ending with [END]
{
  "message": "Hello world"
}
[END] and get "$.message" and save it as "deleteResponseMessage"
```

## Endpoints

- `tr-playground-api.onrender.com` — GET and DELETE. Render free tier, so the first
  request after an idle period can time out.
- `httpbin.org` — POST and PUT, after the playground host proved unreliable. The
  originals are preserved as comments in those two files.
- `api.qaautomationlabs.com/v1/flights` — the CRUD sequence.
- `randomuser.me`, `reqres.in` — test data and the mocking example.
