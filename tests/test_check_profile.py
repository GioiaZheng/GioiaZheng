from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.check_profile import extract_links, validate_profile


VALID_README = """<h1 align="center">Gioia Zheng</h1>

<p align="center">
B.Sc. student in Applied Computer Science and Artificial Intelligence<br>
Sapienza University of Rome, Italy
</p>

<p align="center">
<a href="https://gioiazheng.github.io">Website</a> -
<a href="https://www.linkedin.com/in/gioia-zheng-9233a0303">LinkedIn</a> -
<a href="mailto:gioia.zheng.stud@gmail.com">Email</a> -
<a href="cv/Gioia_Zheng_cv.pdf">Resume</a>
</p>

## About Me
I work on retrieval, evaluation, and failure analysis.

## Selected Work

## Current Research
"""


class ProfileCheckTests(unittest.TestCase):
    def test_extracts_markdown_and_html_links(self) -> None:
        content = '<a href="cv/resume.pdf">Resume</a> and [repo](docs/readme.md)'

        self.assertEqual(extract_links(content), ["docs/readme.md", "cv/resume.pdf"])

    def test_valid_profile_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            (root / "cv").mkdir()
            (root / "cv" / "Gioia_Zheng_cv.pdf").write_bytes(b"%PDF-1.4\n")
            (root / "README.md").write_text(VALID_README, encoding="utf-8")

            self.assertEqual(validate_profile(root), [])

    def test_reports_missing_local_resume_link(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            (root / "README.md").write_text(VALID_README, encoding="utf-8")

            errors = validate_profile(root)

            self.assertIn("README.md has a broken local link: cv/Gioia_Zheng_cv.pdf.", errors)

    def test_reports_missing_required_profile_text(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir:
            root = Path(tmp_dir)
            (root / "cv").mkdir()
            (root / "cv" / "Gioia_Zheng_cv.pdf").write_bytes(b"%PDF-1.4\n")
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
            (root / "cv").mkdir()
            (root / "cv" / "Gioia_Zheng_cv.pdf").write_bytes(b"%PDF-1.4\n")
            readme = VALID_README.replace(
                "https://www.linkedin.com/in/gioia-zheng-9233a0303",
                "https://www.linkedin.com/in/example",
            )
            (root / "README.md").write_text(readme, encoding="utf-8")

            errors = validate_profile(root)

            self.assertIn(
                "README.md is missing required link: "
                "https://www.linkedin.com/in/gioia-zheng-9233a0303.",
                errors,
            )


if __name__ == "__main__":
    unittest.main()
