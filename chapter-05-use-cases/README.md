# Chapter 5 — Control Flow and Data

Loops, conditionals, generated data, and multi-step registration flows.

| Directory | Suite ID | Tests | Focus |
|---|---|---|---|
| `example-001/` | `pvfAWs4hFkNdEKMEe` | 1 | fund transfer between accounts |
| `example-002/` | `gX6ZGxP2KZxhv7xWa` | 1 | grab a price, purchase, verify total |
| `example-003/` | `qHzgqE9JFQQ9R4PXn` | 2 | Best Buy signup |
| `example-004/` | `9HQBypJGP4e3oydMP` | 1 | registration then login |
| `example-005/` | `StJBByQnwDMShWv9N` | 1 | `until` loops |
| `example-006/` | `TMLXZYchBjReHqFQv` | 1 | registration driven by a loop |
| `example-007/` | `HGWCDwqZWaxZQktxh` | 4 | live-mode scratch sessions |
| `example-008/` | `8NWAvPRkndXvKXCzH` | 1 | `if / else / end` |
| `example-009/` | `DxfM2bgfs4KRZD5bK` | 1 | ParaBank registration |
| `example-010/` | `5yjnbXirPTzCuvcNX` | 1 | registration |

## The two constructs worth the chapter

**Loop until a condition** — `example-005/`. Three lines that page through a table
without knowing how many pages there are:

```
scroll down until page contains "Showing"
click "Next" until page contains "Hope Fuentes"
click "Hope Fuentes"
```

**Branch** — `example-008/`, with the `end` terminator testRigor requires:

```
if page contains "Kailash Pathak" then
  hover over "Kailash Pathak"
  click "Kailash Pathak"
  wait 3 sec
else
  enter "Edinburgh" into "Search:"
  wait 3 sec
  click "Cedric Kelly"
end
```

Note the suite behind `example-004/` is named `R Use Case Chapter 5 - Example-004`
in testRigor — a missing `t`, preserved here so the name still matches the server.

`example-007/` holds four throwaway cases from live-mode sessions, including one
still named `live-session-1788939641074`.
