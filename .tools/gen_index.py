#!/usr/bin/env python3
"""Regenerate the suite/test-case index in README.md from the YAML files on disk.

Every suite becomes a heading linking to testRigor; every test case under it links
to that case. Names, UUIDs and filenames are read from the committed files, so the
index cannot describe anything that is not actually in the repo.
"""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUITES = json.load(open(os.path.join(ROOT, ".tools", "suites.json")))

SUITE_URL = "https://app.testrigor.com/test-suites/{suite}/test-cases"
CASE_URL  = "https://app.testrigor.com/test-suites/{suite}/test-cases/{case}"

CHAPTER_TITLE = {
    "2": "Chapter 2 — Use Cases",
    "4": "Chapter 4 — Grabbing and Validating Values",
    "5": "Chapter 5 — Control Flow and Data",
    "6": "Chapter 6 — Hard Things",
    "8": "Chapter 8 — Mobile Automation",
    "9": "Chapter 9 — API Automation",
    "—": "Chapter Wise",
}

def chapter_of(dest):
    m = re.match(r"chapter-0?(\d+)", dest)
    return m.group(1) if m else "—"

def md(s):
    """Escape what would otherwise break a table cell or a link label."""
    return s.replace("|", "\\|").replace("[", "\\[").replace("]", "\\]")

def read_cases(dest):
    d = os.path.join(ROOT, dest, "test-cases")
    if not os.path.isdir(d):
        return []
    cases = []
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".yaml"):
            continue
        name, uuid, disabled = None, None, False
        for line in open(os.path.join(d, fn)):
            if line.startswith("# Test case name:"):
                raw = line.split(":", 1)[1].strip()
                try:
                    name = json.loads(raw)
                except json.JSONDecodeError:
                    name = raw.strip('"')
            elif line.startswith("# DISABLED"):
                disabled = True
            elif line.startswith("testCaseUuid:"):
                uuid = line.split(":", 1)[1].strip().strip('"')
        if not uuid:
            raise SystemExit(f"no testCaseUuid in {dest}/test-cases/{fn}")
        cases.append((name or fn[:-5], uuid, fn, disabled))
    return cases

by_chapter = {}
for sid, name, dest in SUITES:
    by_chapter.setdefault(chapter_of(dest), []).append((sid, name, dest))

order = sorted(by_chapter, key=lambda c: (c == "—", c.zfill(2)))
out, n_cases = [], 0
for ch in order:
    suites = sorted(by_chapter[ch], key=lambda r: r[2])
    total = sum(len(read_cases(d)) for _, _, d in suites)
    out.append(f"<details>")
    out.append(f"<summary><b>{CHAPTER_TITLE.get(ch, 'Chapter ' + ch)}</b> — "
               f"{len(suites)} suite{'s' if len(suites) != 1 else ''}, {total} test cases</summary>")
    out.append("")
    for sid, name, dest in suites:
        cases = read_cases(dest)
        n_cases += len(cases)
        out.append(f"#### [{md(name)}]({SUITE_URL.format(suite=sid)})")
        out.append("")
        out.append(f"`{sid}` · [`{dest}/`](./{dest}/test-cases) · "
                   f"{len(cases)} test case{'s' if len(cases) != 1 else ''}")
        out.append("")
        out.append("| Test case | File |")
        out.append("|---|---|")
        for cname, uuid, fn, disabled in cases:
            label = md(cname) + (" _(disabled)_" if disabled else "")
            out.append(f"| [{label}]({CASE_URL.format(suite=sid, case=uuid)}) "
                       f"| [`{fn}`](./{dest}/test-cases/{fn}) |")
        out.append("")
    out.append("</details>")
    out.append("")

block = "\n".join(out).rstrip()
p = os.path.join(ROOT, "README.md")
s = open(p).read()
pat = re.compile(r"(<!-- index:start -->\n).*?(<!-- index:end -->)", re.S)
if not pat.search(s):
    raise SystemExit("index markers not found in README.md")
s = pat.sub(lambda m: m.group(1) + block + "\n" + m.group(2), s)
open(p, "w").write(s)
if block.splitlines()[-1] not in open(p).read():
    raise SystemExit("index did not land in README.md")
print(f"{len(SUITES)} suites, {n_cases} test cases indexed")
