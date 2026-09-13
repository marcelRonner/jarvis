#!/usr/bin/env python3
"""Acceptance tests for the Open Knowledge Format requirements placed on *consumers*.

OKF v0.2 obliges software that reads a bundle to tolerate what a producer may legitimately do. A
bundle cannot prove that by being inspected — only the consumer can, so these tests run against the
two consumers this repository has:

- the Python reader in scripts/okflib.py, which the checks and `make verify` read the documentation with;
- the Hugo site build, run for real against a small bundle that does each tolerated thing.

    OKF-CPT-05  an unknown `type` is consumed                         (§4.1, consumer MUST)
    OKF-CPT-10  an unknown frontmatter key is not rejected, and kept  (§4.1, consumer MUST / SHOULD)
    OKF-TRU-03  a bare `verified` mapping reads as one event          (§5.2, §11, consumer MUST)
    OKF-LNK-03  a broken link is not malformed input                  (§6.1, §11, consumer MUST)
    OKF-CNF-04  missing optional fields, unknown types and keys, broken links and a missing
                index.md do not cause rejection                       (§11, consumer MUST)

The Hugo test builds without `--panicOnWarning`: failing a build over a broken link is this
repository's *producer* policy (`make build`), and says nothing about whether Hugo can consume one.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from okflib import ROOT, Page

UNKNOWN_TYPE = """---
title: "A concept from the future"
type: Future Concept
custom_extension: retained
---

# A concept from the future

See [knowledge not yet written](missing.md).
"""

TYPE_ONLY = """---
type: Reference
---

Nothing but a type.
"""

HOME = """---
title: "Home"
type: overview
---
"""


class PythonReader(unittest.TestCase):
    def read(self, text: str) -> Page:
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        path = Path(directory.name) / "concept.md"
        path.write_text(text, encoding="utf-8")
        return Page(path)

    def test_unknown_type_is_consumed_and_unknown_key_kept(self) -> None:  # OKF-CPT-05, OKF-CPT-10
        page = self.read(UNKNOWN_TYPE)
        self.assertIsNone(page.error)
        self.assertEqual(page.get("type"), "Future Concept")
        self.assertEqual(page.get("custom_extension"), "retained")

    def test_broken_link_is_read_without_rejection(self) -> None:  # OKF-LNK-03
        page = self.read(UNKNOWN_TYPE)
        self.assertIsNone(page.error)
        self.assertIn("missing.md", [target for _, target in page.links()])

    def test_missing_optional_fields_are_not_an_error(self) -> None:  # OKF-CNF-04
        page = self.read(TYPE_ONLY)
        self.assertIsNone(page.error)
        for key in ("title", "description", "tags", "sources", "generated", "verified"):
            self.assertIsNone(page.get(key))
        self.assertEqual(page.sources(), [])
        self.assertEqual(page.verified_events(), [])

    def test_bare_verified_mapping_is_one_event(self) -> None:  # OKF-TRU-03
        bare = self.read('---\ntype: Reference\nverified: { by: "human:owner", at: 2026-09-12T10:00:00Z }\n---\n')
        listed = self.read('---\ntype: Reference\nverified:\n  - { by: "human:owner", at: 2026-09-12T10:00:00Z }\n---\n')
        self.assertEqual(len(bare.verified_events()), 1)
        self.assertEqual(bare.verified_events(), listed.verified_events())


@unittest.skipUnless(shutil.which("hugo") and (ROOT / "node_modules").is_dir(),
                     "needs hugo and `npm install`")
class HugoSiteBuild(unittest.TestCase):
    """The real site configuration and templates, building a bundle that does every tolerated thing."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.tmp = tempfile.TemporaryDirectory()
        site = Path(cls.tmp.name)
        for name in ("hugo.yaml", "go.mod", "go.sum", "package.json"):
            shutil.copy2(ROOT / name, site / name)
        for name in ("layouts", "assets", "packages"):
            shutil.copytree(ROOT / name, site / name)
        (site / "node_modules").symlink_to(ROOT / "node_modules")
        content = site / "content"
        (content / "future").mkdir(parents=True)          # a folder with no _index.md, and no index.md anywhere
        (content / "_index.md").write_text(HOME, encoding="utf-8")
        (content / "future" / "concept.md").write_text(UNKNOWN_TYPE, encoding="utf-8")
        (content / "typeOnly.md").write_text(TYPE_ONLY, encoding="utf-8")
        env = {**os.environ, "PATH": f"{ROOT / 'node_modules' / '.bin'}{os.pathsep}{os.environ.get('PATH', '')}"}
        cls.result = subprocess.run(["hugo", "--quiet", "--baseURL", "/", "-d", "out"], cwd=site,
                                    env=env, capture_output=True, text=True, timeout=300)
        cls.out = site / "out"

    @classmethod
    def tearDownClass(cls) -> None:
        cls.tmp.cleanup()

    def test_the_bundle_builds(self) -> None:  # OKF-CNF-04
        self.assertEqual(self.result.returncode, 0, self.result.stderr)

    def test_unknown_type_renders_with_the_site_chrome(self) -> None:  # OKF-CPT-05, OKF-CPT-10
        html = (self.out / "future" / "concept" / "index.html").read_text(encoding="utf-8")
        self.assertTrue("A concept from the future" in html, "the concept's title is not on its page")
        self.assertTrue("td-sidebar" in html, "an unknown type fell through to a page without the docs layout")

    def test_broken_link_is_passed_through(self) -> None:  # OKF-LNK-03
        html = (self.out / "future" / "concept" / "index.html").read_text(encoding="utf-8")
        self.assertTrue('href="missing.md"' in html or "href=missing.md" in html, "the broken link was dropped")

    def test_concept_with_only_a_type_renders(self) -> None:  # OKF-CNF-04
        self.assertTrue((self.out / "typeonly" / "index.html").exists())


if __name__ == "__main__":
    unittest.main()
