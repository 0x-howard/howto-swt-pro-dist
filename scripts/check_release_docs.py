#!/usr/bin/env python3
"""Validate Pro public release docs, encrypted artifact, manifest, and tag."""

import argparse
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
CURRENT = MANIFEST["latest"]
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
README = (ROOT / "README.md").read_text(encoding="utf-8")
CHANGELOG = (ROOT / "docs" / "CHANGELOG.md").read_text(encoding="utf-8")


def fail(reason: str) -> None:
    raise SystemExit(f"RELEASE_DOCS_CHECK_FAILED: {reason}")


parser = argparse.ArgumentParser()
parser.add_argument("--tag")
args = parser.parse_args()

if VERSION != CURRENT:
    fail(f"VERSION {VERSION} does not match manifest latest {CURRENT}")
release = MANIFEST.get("releases", {}).get(CURRENT)
if not release or release.get("version") != CURRENT:
    fail(f"manifest release metadata missing for {CURRENT}")
bundle = ROOT / "releases" / CURRENT / f"howto-swt-pro-{CURRENT}.bundle"
if not bundle.is_file():
    fail(f"encrypted bundle missing: {bundle.relative_to(ROOT)}")
if hashlib.sha256(bundle.read_bytes()).hexdigest() != release.get("ciphertext_sha256"):
    fail("encrypted bundle SHA-256 does not match manifest")
if bundle.stat().st_size != release.get("size"):
    fail("encrypted bundle size does not match manifest")
expected_url = f"https://raw.githubusercontent.com/0x-howard/howto-swt-pro-dist/main/releases/{CURRENT}/howto-swt-pro-{CURRENT}.bundle"
if release.get("asset_url") != expected_url:
    fail("encrypted bundle asset_url is not the canonical public URL")
if args.tag and args.tag != f"v{CURRENT}":
    fail(f"tag {args.tag} does not match v{CURRENT}")
if not re.search(rf"^## v{re.escape(CURRENT)}(?:\s|$)", CHANGELOG, re.MULTILINE):
    fail(f"v{CURRENT} missing from docs/CHANGELOG.md")
match = re.search(
    r"<!-- CHANGELOG_LATEST_START -->(.*?)<!-- CHANGELOG_LATEST_END -->",
    README,
    re.DOTALL,
)
if not match:
    fail("README recent-update markers missing")
versions = re.findall(r"\|\s*v(\d+(?:\.\d+)+)\s*\|", match.group(1))
if not versions or CURRENT not in versions:
    fail(f"README recent updates do not include v{CURRENT}")
if len(versions) > 5 or len(versions) != len(set(versions)):
    fail("README recent updates must contain 1-5 unique versions")
print(f"RELEASE_DOCS_CHECK_OK: v{CURRENT}; {len(versions)} recent versions")
