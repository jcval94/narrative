from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path


FORBIDDEN_HTML_PATTERNS = [
    r"<select\b",
    r"<nav\b",
    r"filter",
    r"filtro",
    r"tablist",
    r"role=[\"']tab",
    r"kpi-card",
    r"kpi card",
    r"metric-card",
    r"scorecard",
    r"dashboard-grid",
    r"filter-panel",
    r"drilldown",
    r"self-service",
    r"data-table",
    r"class=[\"'][^\"']*(dashboard|bi-layout|kpi-card|metric-card|scorecard|filter-panel|tab-panel)",
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

NARRATIVE_LEARNING_REQUIRED_TEXT = [
    "misterio",
    "evidencia visual",
    "pista",
    "lectura guiada",
    "lo que parece",
    "lo que realmente pasa",
    "pregunta activa",
    "traducción",
    "giro",
    "decisión cómoda",
    "acción robusta",
    "piloto",
    "cierre tragicómico",
    "regla transferible",
    "pregunta de transferencia",
]


def visible_text(html: str) -> str:
    text = re.sub(r"<script\b.*?</script>", " ", html, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<style\b.*?</style>", " ", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<[^>]+>", " ", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def fold_text(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value.lower())
    ascii_text = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    return re.sub(r"\s+", " ", ascii_text).strip()


def first_visible_words(html: str, limit: int = 60) -> str:
    words = visible_text(html).split()
    return " ".join(words[:limit])


def validate_html(html: str, narrative_learning_standard: bool = False) -> list[str]:
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

    if narrative_learning_standard:
        text = visible_text(html)
        folded_text = fold_text(text)
        first_words = fold_text(first_visible_words(html))
        if "contexto breve" in first_words or first_words.startswith("contexto"):
            errors.append("Weak opening: HTML starts with context instead of intrigue.")

        for required in NARRATIVE_LEARNING_REQUIRED_TEXT:
            if fold_text(required) not in folded_text:
                errors.append(f"Missing narrative learning HTML element: {required}")

        if "?" not in text and "que mirar" not in folded_text:
            errors.append("Missing active question for the student.")

        paragraph_count = len(re.findall(r"<p\b", lowered))
        word_count = len(text.split())
        has_guided_visual_language = any(
            marker in folded_text
            for marker in ["pista", "lectura guiada", "lo que parece", "lo que realmente pasa"]
        )
        if word_count > 1500 and paragraph_count > 30 and not has_guided_visual_language:
            errors.append("HTML appears too textual for the narrative learning standard.")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a simple narrative HTML story.")
    parser.add_argument(
        "--narrative-learning-standard",
        action="store_true",
        help="Apply the Narrative Learning Experience Standard for new or regenerated case HTML.",
    )
    parser.add_argument("html_path", type=Path)
    args = parser.parse_args()

    if not args.html_path.exists():
        print(f"ERROR: file not found: {args.html_path}", file=sys.stderr)
        return 2

    errors = validate_html(
        args.html_path.read_text(encoding="utf-8"),
        narrative_learning_standard=args.narrative_learning_standard,
    )
    if errors:
        print("NEEDS_REVISION")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
