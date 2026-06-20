from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


FORBIDDEN_HTML_PATTERNS = [
    r"<select\b",
    r"<nav\b",
    r"filter",
    r"filtro",
    r"tablist",
    r"role=[\"']tab",
    r"kpi-card",
    r"drilldown",
    r"self-service",
    r"data-table",
]

REQUIRED_TEXT = [
    "nivel analítico",
    "técnica",
    "evidencia visual",
    "qué parece",
    "qué revela",
    "giro",
    "acción robusta",
    "acción débil",
    "piloto",
    "comentario tragicómico",
    "preguntas",
]


def validate_html(html: str) -> list[str]:
    lowered = html.lower()
    errors: list[str] = []

    for pattern in FORBIDDEN_HTML_PATTERNS:
        if re.search(pattern, lowered):
            errors.append(f"Forbidden dashboard/UI pattern found: {pattern}")

    for text in REQUIRED_TEXT:
        if text not in lowered:
            errors.append(f"Missing narrative HTML section: {text}")

    svg_count = lowered.count("<svg")
    canvas_count = lowered.count("<canvas")
    visual_count = svg_count + canvas_count
    if visual_count == 0:
        errors.append("Missing central visualization: no SVG or canvas found.")
    if visual_count > 2:
        errors.append(f"Too many visualizations: {visual_count}. Maximum is 2 with justification.")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a simple narrative HTML story.")
    parser.add_argument("html_path", type=Path)
    args = parser.parse_args()

    if not args.html_path.exists():
        print(f"ERROR: file not found: {args.html_path}", file=sys.stderr)
        return 2

    errors = validate_html(args.html_path.read_text(encoding="utf-8"))
    if errors:
        print("NEEDS_REVISION")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
