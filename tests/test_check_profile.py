from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.check_profile import extract_links, validate_profile


VALID_README = """<h1 align="center">Gioia Zheng</h1>

<p align="center">
M.Sc. Computer Science · TU Darmstadt<br>
B.Sc. Applied Computer Science and Artificial Intelligence · Sapienza University of Rome · Expected Dec 2026
</p>

<p align="center">
<a href="https://gioiazheng.github.io">Website</a> -
<a href="https://www.linkedin.com/in/gioiazheng/">LinkedIn</a> -
<a href="mailto:gioia.zheng.stud@gmail.com">Email</a> -
<a href="https://gioiazheng.github.io/cv/Gioia_Zheng_Research_CV.pdf">Research CV</a>
</p>

## About Me
I work on RAG/LLM Evaluation, failure analysis, and exact evaluation of reinforcement-learning agents.

## Selected Work

## Selected Open-Source Contributions

## Current Research
"""


class ProfileCheckTests(unittest.TestCase):
    def test_extracts_markdown_and_html_links(self) -> None:
        content = '<a href="cv/resume.pdf">Resume</a> and [repo](docs/readme.md)'

        self.assertEqual(extract_links(content), ["docs/readme.md", "cv/resume.pdf"])

    def test_valid_profile_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            (root / "README.md").write_text(VALID_README, encoding="utf-8")

            self.assertEqual(validate_profile(root), [])

    def test_reports_missing_research_cv_link(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            readme = VALID_README.replace(
                "https://gioiazheng.github.io/cv/Gioia_Zheng_Research_CV.pdf",
                "https://example.com/resume.pdf",
            )
            (root / "README.md").write_text(readme, encoding="utf-8")

            errors = validate_profile(root)

            self.assertIn(
                "README.md is missing required link: "
                "https://gioiazheng.github.io/cv/Gioia_Zheng_Research_CV.pdf.",
                errors,
            )

    def test_reports_missing_required_profile_text(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            readme = VALID_README.replace("failure analysis", "research systems")
            (root / "README.md").write_text(readme, encoding="utf-8")

            errors = validate_profile(root)

            self.assertIn(
                "README.md is missing required profile text: failure analysis.",
                errors,
            )

    def test_reports_missing_required_contact_link(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            readme = VALID_README.replace(
                "https://www.linkedin.com/in/gioiazheng/",
                "https://www.linkedin.com/in/example",
            )
            (root / "README.md").write_text(readme, encoding="utf-8")

            errors = validate_profile(root)

            self.assertIn(
                "README.md is missing required link: "
                "https://www.linkedin.com/in/gioiazheng/.",
                errors,
            )

    def test_reports_forbidden_profile_text(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            readme = VALID_README.replace(
                "M.Sc. Computer Science · TU Darmstadt",
                "Incoming M.Sc. Computer Science · TU Darmstadt",
            )
            (root / "README.md").write_text(readme, encoding="utf-8")

            errors = validate_profile(root)

            self.assertIn(
                "README.md contains forbidden profile text: Incoming M.Sc..",
                errors,
            )


if __name__ == "__main__":
    unittest.main()
