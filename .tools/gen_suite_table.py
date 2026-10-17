#!/usr/bin/env python3
"""Regenerate the suite-ID table in README.md from .tools/suites.json + disk.

Keeps the README honest: IDs, directories and test counts all come from the
same manifest the exporter uses. Run after adding or removing a suite.
"""
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SUITES = json.load(open(os.path.join(ROOT, ".tools", "suites.json")))

PLATFORM = {
    "GmDZSeAYdYSDLkSRc": "ANDROID_30_X86_ULTRA",
    "E6xmsGLoubPG6god8": "ANDROID_36_X86_64_PIXEL_9",
    "MkwytBxehMhocoqap": "ANDROID_35_X86_64_PIXEL_3A",
    "cwHukcm4M9fp6Hkpd": "IOS_17_5_X86_64_IPHONE_15_PRO",
    "krQLaLXFXKTYS3o4N": "IOS_27_0_ARM64_IPHONE_17_PRO_MAX",
    "MS56ps8p2r4HN2wFR": "IOS_17_0_ARM64_IPHONE_XR",
}

def chapter_of(dest):
    m = re.match(r"chapter-0?(\d+)", dest)
    return m.group(1) if m else "—"

def count(dest):
    d = os.path.join(ROOT, dest, "test-cases")
    return len([f for f in os.listdir(d) if f.endswith(".yaml")]) if os.path.isdir(d) else 0

rows = sorted(SUITES, key=lambda r: (chapter_of(r[2]) == "—", chapter_of(r[2]).zfill(2), r[2]))

APP = "https://app.testrigor.com/test-suites/{}/test-cases"

out = ["| Ch | Suite name in testRigor | Suite ID | Directory | Tests | Platform |",
       "|---|---|---|---|---|---|"]
for sid, name, dest in rows:
    link = f"[`{sid}`]({APP.format(sid)})"
    out.append(f"| {chapter_of(dest)} | {name} | {link} | `{dest}/` | {count(dest)} "
               f"| {'`'+PLATFORM[sid]+'`' if sid in PLATFORM else 'WebDesktopChrome'} |")
table = "\n".join(out)

p = os.path.join(ROOT, "README.md")
s = open(p).read()
pat = re.compile(r"(<!-- suite-table:start -->\n).*?(<!-- suite-table:end -->)", re.S)
if not pat.search(s):
    raise SystemExit("suite-table markers not found in README.md")
new = pat.sub(lambda m: m.group(1) + table + "\n" + m.group(2), s)
open(p, "w").write(new)
if table.splitlines()[-1] not in open(p).read():
    raise SystemExit("table did not land in README.md")
print(f"{len(rows)} suites, {sum(count(r[2]) for r in rows)} test cases")
