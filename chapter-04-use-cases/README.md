# Chapter 4 — Grabbing and Validating Values

Reading values off the page, reshaping them, and feeding them back in.

| Directory | Suite ID | Tests |
|---|---|---|
| `example-001/` | `RQdpveizyyDSXfLdx` | 2 |
| `example-002/` | `CfKauFmQ4o3eaFD28` | 2 |
| `example-003/` | `HvptojZKfhoe6q4p8` | 1 |

## What each shows

**`example-001/` — positional grabs.** `grab value from element below "Email:"`
and `... to the right of "Password:"`, then a regex to strip the label off the
captured text:

```
extract value by regex "(?<=Password:\s).*$" from stored value "password" and save as "password"
```

**`example-002/` — semantic grabs.** The same job with `grab value by description
"First accepted username" using AI`, no positional anchor at all. The commented
first attempt (`"Accepted usernames are:"`) grabbed the label rather than the
value, which is why the description was narrowed.

This directory also holds `SCRUM-65 Ecommerce checkout end to end` — the only
test in the repo tied to a ticket (label `SCRUM-65`) and the only one whose steps
are annotated step-by-step against a written test plan.

**`example-003/` — assertion vocabulary.** `check that "Login" is enabled`,
`check that input "Email" has value "..."`, and a free-text AI assertion:
`check that page "contains login credentials for users" using ai`.
