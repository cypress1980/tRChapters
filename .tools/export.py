#!/usr/bin/env python3
"""Export testRigor suites to YAML files, one per test case.

Usage:  TESTRIGOR_API_KEY=<pat> python3 .tools/export.py
Reads SUITES below, writes <dir>/test-cases/<slug>.yaml for every test case.
"""
import json, os, re, sys, time, urllib.request

URL = "https://api2.testrigor.com/api/v1/mcp"
TOK = os.environ.get("TESTRIGOR_API_KEY", "").strip()
if not TOK:
    sys.exit("set TESTRIGOR_API_KEY")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (suite id, suite name, destination directory relative to repo root)
SUITES = json.load(open(os.path.join(ROOT, ".tools", "suites.json")))

_sid = None
def rpc(method, params, sid=None):
    body = {"jsonrpc": "2.0", "id": 1, "method": method}
    if params is not None:
        body["params"] = params
    req = urllib.request.Request(URL, data=json.dumps(body).encode(),
        headers={"personal-access-token": TOK, "Content-Type": "application/json",
                 "Accept": "application/json, text/event-stream",
                 **({"mcp-session-id": sid} if sid else {})})
    with urllib.request.urlopen(req, timeout=60) as r:
        raw = r.read().decode().strip()
        sid_out = r.headers.get("mcp-session-id")
        if not raw:                       # notifications return 202 with no body
            return sid_out, None
        if raw.startswith("event:"):      # SSE framing
            raw = "".join(l[5:].strip() for l in raw.splitlines() if l.startswith("data:"))
        return sid_out, json.loads(raw)

def connect():
    sid, _ = rpc("initialize", {"protocolVersion": "2025-03-26", "capabilities": {},
                                "clientInfo": {"name": "export", "version": "1"}})
    rpc("notifications/initialized", None, sid)
    return sid

def list_cases(sid, suite_id):
    out = []
    page = 0
    while True:
        _, res = rpc("tools/call", {"name": "list_test_cases",
                     "arguments": {"testSuiteId": suite_id, "page": page}}, sid)
        if res.get("result", {}).get("isError"):
            raise RuntimeError(res["result"]["content"][0]["text"])
        d = json.loads(res["result"]["content"][0]["text"])
        out += d.get("test_cases", [])
        page += 1
        if page >= d.get("total_pages", 1):
            return out

def slug(s, n=70):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return (s[:n].rstrip("-") or "test-case")

def emit(tc, suite_name, suite_id):
    steps = (tc.get("custom_steps") or "").replace("\r\n", "\n").rstrip()
    body = "\n".join(("  " + l).rstrip() for l in steps.split("\n"))
    name = (tc.get("description") or "").replace("\n", " ").strip()
    out = [f"# Suite: {suite_name} ({suite_id})",
           f"# Test case name: {json.dumps(name, ensure_ascii=False)}"]
    if tc.get("disabled"):
        out.append("# DISABLED in testRigor")
    out += ["customSteps: |", body]
    if tc.get("labels"):
        out.append("labels: [" + ", ".join(tc["labels"]) + "]")
    out.append(f'testCaseUuid: "{tc["uuid"]}"')
    return "\n".join(out) + "\n"

def list_cases_retry(suite_id, attempts=5):
    """The server resets long-lived sessions; reconnect and retry rather than die."""
    global sid
    for i in range(attempts):
        try:
            return list_cases(sid, suite_id)
        except Exception as e:
            if i == attempts - 1:
                raise
            wait = 2 * (i + 1)
            print(f"     retry {i+1}/{attempts-1} after {type(e).__name__}; reconnecting in {wait}s")
            time.sleep(wait)
            sid = connect()

sid = connect()
total = 0
for suite_id, suite_name, dest in SUITES:
    d = os.path.join(ROOT, dest, "test-cases")
    if os.path.isdir(d) and any(f.endswith(".yaml") for f in os.listdir(d)):
        n = len([f for f in os.listdir(d) if f.endswith(".yaml")])
        print(f"{n:3d}  {dest}  (already exported, skipped)", flush=True)
        total += n
        continue
    os.makedirs(d, exist_ok=True)
    cases = list_cases_retry(suite_id)
    seen = {}
    for tc in cases:
        base = slug(tc.get("description") or tc["uuid"])
        seen[base] = seen.get(base, 0) + 1
        fn = base if seen[base] == 1 else f"{base}-{seen[base]}"
        open(os.path.join(d, fn + ".yaml"), "w").write(emit(tc, suite_name, suite_id))
    total += len(cases)
    print(f"{len(cases):3d}  {dest}", flush=True)
print(f"\n{total} test cases from {len(SUITES)} suites")
