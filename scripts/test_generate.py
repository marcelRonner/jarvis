#!/usr/bin/env python3
"""Tests for the generated OKF log: versions and filed assessments, grouped by day, newest first."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from generate import okf_log

CHANGE_LOG = """# Change Log

## v1.2 – Second (2026-09-13)

Released the second version.

## v1.1 – First (2026-09-12)

Released the [first](../x.md) version.
"""

ASSESSMENT = """---
title: "OKF v0.2 Conformance Assessment – {day}"
type: assessment
description: "Conformant; {note}."
---
"""


class OkfLog(unittest.TestCase):
    def build(self, assessments: dict[str, str]) -> str:
        directory = tempfile.TemporaryDirectory()
        self.addCleanup(directory.cleanup)
        root = Path(directory.name)
        (root / "changeLog.md").write_text(CHANGE_LOG, encoding="utf-8")
        (root / "sources").mkdir()
        for name, text in assessments.items():
            (root / "sources" / name).write_text(text, encoding="utf-8")
        return okf_log(root / "changeLog.md", root / "sources")

    def test_an_assessment_is_listed_under_its_day_before_the_release(self) -> None:
        log = self.build({"okf_assessment_2026_09_13.md": ASSESSMENT.format(day="2026-09-13", note="first run")})
        day = log.split("## 2026-09-13\n", 1)[1].split("\n## ", 1)[0]
        entries = [line for line in day.splitlines() if line.startswith("- ")]
        self.assertEqual(entries[0], "- **Assessment:** [OKF v0.2 Conformance Assessment – 2026-09-13]"
                                     "(sources/okf_assessment_2026_09_13.md) — Conformant; first run.")
        self.assertTrue(entries[1].startswith("- **Release:** [v1.2 – Second]"))

    def test_an_assessment_on_a_day_without_a_release_gets_its_own_heading(self) -> None:
        log = self.build({"okf_assessment_2026_09_14.md": ASSESSMENT.format(day="2026-09-14", note="later")})
        headings = [line for line in log.splitlines() if line.startswith("## ")]
        self.assertEqual(headings, ["## 2026-09-14", "## 2026-09-13", "## 2026-09-12"])

    def test_a_second_run_on_the_same_day_is_listed_first(self) -> None:
        log = self.build({"okf_assessment_2026_09_13.md": ASSESSMENT.format(day="2026-09-13", note="morning"),
                          "okf_assessment_2026_09_13_2.md": ASSESSMENT.format(day="2026-09-13", note="afternoon")})
        self.assertLess(log.index("afternoon"), log.index("morning"))

    def test_release_summary_links_keep_only_their_text(self) -> None:
        self.assertIn("Released the first version.", self.build({}))

    def test_a_misnamed_assessment_is_refused(self) -> None:
        with self.assertRaises(SystemExit):
            self.build({"okf_assessment_13-09-2026.md": ASSESSMENT.format(day="2026-09-13", note="x")})


if __name__ == "__main__":
    unittest.main()
