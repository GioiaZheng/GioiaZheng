"""Validate the public profile README."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote


REQUIRED_HEADINGS = (
    "About Me",
    "Selected Work",
    "Current Research",
)

REQUIRED_PHRASES = (
    "Gioia Zheng",
    "Applied Computer Science and Artificial Intelligence",
    "Sapienza University of Rome",
    "failure analysis",
)

REQUIRED_LINKS = (
    "https://gioiazheng.github.io",
    "https://www.linkedin.com/in/gioia-zheng-9233a0303",
    "mailto:gioia.zheng.stud@gmail.com",
    "cv/Gioia_Zheng_cv.pdf",
)

MOJIBAKE_MARKERS = ("Ã", "Â", "â€", "â€“", "â€™")
MARKDOWN_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
HTML_HREF_RE = re.compile(r"<a\s+[^>]*href=[\"']([^\"']+)[\"']", re.IGNORECASE)
HEADING_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)


def _is_external_link(target: str) -> bool:
    return bool(re.match(r"^[a-z][a-z0-9+.-]*:", target, re.IGNORECASE))


def extract_links(content: str) -> list[str]:
    links = [match.group(1).strip() for match in MARKDOWN_LINK_RE.finditer(content)]
    links.extend(match.group(1).strip() for match in HTML_HREF_RE.finditer(content))
    return links


def validate_profile(root: Path) -> list[str]:
    readme = root / "README.md"
    errors: list[str] = []

    if not readme.is_file():
        return ["README.md is missing."]

    content = readme.read_text(encoding="utf-8")
    headings = set(HEADING_RE.findall(content))

    for heading in REQUIRED_HEADINGS:
        if heading not in headings:
            errors.append(f"README.md is missing the '{heading}' section.")

    for phrase in REQUIRED_PHRASES:
        if phrase not in content:
            errors.append(f"README.md is missing required profile text: {phrase}.")

    for line_number, line in enumerate(content.splitlines(), start=1):
        if any(marker in line for marker in MOJIBAKE_MARKERS):
            errors.append(f"README.md:{line_number} contains suspicious encoding artifacts.")

    links = extract_links(content)
    for required_link in REQUIRED_LINKS:
        if required_link not in links:
            errors.append(f"README.md is missing required link: {required_link}.")

    root_resolved = root.resolve()
    for link in links:
        if not link or link.startswith("#") or _is_external_link(link):
            continue

        link_path = unquote(link.split("#", 1)[0])
        if not link_path:
            continue

        target = (readme.parent / link_path).resolve()
        try:
            target.relative_to(root_resolved)
        except ValueError:
            errors.append(f"README.md links outside the repository: {link}.")
            continue

        if not target.exists():
            errors.append(f"README.md has a broken local link: {link}.")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()

    errors = validate_profile(args.root)
    if errors:
        print("Profile check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Profile check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
