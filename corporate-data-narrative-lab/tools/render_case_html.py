from __future__ import annotations

import argparse
import html
import re
from pathlib import Path


CSS = """
:root {
  --ink: #1d2433;
  --muted: #5e697a;
  --line: #d7dde7;
  --paper: #ffffff;
  --bg: #f6f7f9;
  --accent: #3568a8;
  --warn: #a84f35;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
  color: var(--ink);
  background: var(--bg);
  line-height: 1.58;
}
main {
  width: min(920px, calc(100% - 32px));
  margin: 0 auto;
  padding: 42px 0 60px;
}
header {
  margin-bottom: 34px;
}
h1 {
  margin: 0 0 10px;
  font-size: clamp(2rem, 5vw, 3.25rem);
  line-height: 1.05;
}
h2 {
  margin: 0 0 10px;
  font-size: 1.25rem;
}
section {
  margin: 0 0 24px;
}
p, li {
  color: var(--ink);
}
.section {
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 18px 20px;
}
.muted {
  color: var(--muted);
}
.evidence {
  border-left: 4px solid var(--accent);
}
.clue {
  border-left: 4px solid #2f7d68;
}
.decision {
  border-left: 4px solid #7a5a1f;
}
.tragicomic {
  border-left: 4px solid var(--warn);
}
.rule {
  border-left: 4px solid #4a6f2c;
}
"""


DISPLAY_HEADINGS = {
    "opening_hook": "Apertura",
    "protagonist_or_student_role": "Tu rol en la investigación",
    "central_mystery": "El misterio",
    "official_story": "Lo que parece",
    "hidden_story": "Lo que realmente pasa",
    "visual_clue": "Pista visual",
    "student_question": "Pregunta activa",
    "jargon_translation": "Traducción de jerga",
    "analytical_twist": "Giro analítico",
    "weak_decision": "Decisión cómoda",
    "robust_decision": "Acción robusta",
    "tragicomic_ending": "Cierre tragicómico",
    "transferable_rule": "Regla transferible",
}


def split_sections(markdown: str) -> tuple[str, list[tuple[str, list[str]]]]:
    title = "Caso"
    sections: list[tuple[str, list[str]]] = []
    current_heading: str | None = None
    current_lines: list[str] = []

    for raw_line in markdown.splitlines():
        title_match = re.match(r"^#\s+(.+?)\s*$", raw_line)
        section_match = re.match(r"^##\s+(.+?)\s*$", raw_line)

        if title_match:
            title = title_match.group(1)
            continue

        if section_match:
            if current_heading is not None:
                sections.append((current_heading, current_lines))
            current_heading = section_match.group(1)
            current_lines = []
            continue

        if current_heading is not None:
            current_lines.append(raw_line)

    if current_heading is not None:
        sections.append((current_heading, current_lines))

    return title, sections


def render_inline(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"`(.+?)`", r"<code>\1</code>", escaped)
    return escaped


def render_lines(lines: list[str]) -> str:
    blocks: list[str] = []
    paragraph: list[str] = []
    list_items: list[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            blocks.append(f"<p>{render_inline(' '.join(paragraph))}</p>")
            paragraph = []

    def flush_list() -> None:
        nonlocal list_items
        if list_items:
            rendered = "".join(f"<li>{render_inline(item)}</li>" for item in list_items)
            blocks.append(f"<ul>{rendered}</ul>")
            list_items = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            flush_paragraph()
            flush_list()
            continue
        if stripped.startswith("- "):
            flush_paragraph()
            list_items.append(stripped[2:])
        else:
            flush_list()
            paragraph.append(stripped)

    flush_paragraph()
    flush_list()
    return "\n".join(blocks)


def plain_section_text(lines: list[str]) -> str:
    return " ".join(line.strip().lstrip("- ") for line in lines if line.strip())


def render_case(markdown: str) -> str:
    title, sections = split_sections(markdown)
    rendered_sections: list[str] = []
    subtitle = "Narrativa corporativa centrada en datos. Una historia, una evidencia, cero dashboards."

    for heading, lines in sections:
        css_class = "section"
        normalized = heading.lower()
        if normalized == "opening_hook":
            subtitle = plain_section_text(lines) or subtitle
            continue
        if "evidencia" in normalized:
            css_class += " evidence"
        if normalized in {"visual_clue", "student_question", "jargon_translation", "analytical_twist"}:
            css_class += " clue"
        if normalized in {"weak_decision", "robust_decision"}:
            css_class += " decision"
        if "tragicómico" in normalized or "tragicomico" in normalized:
            css_class += " tragicomic"
        if normalized in {"tragicomic_ending"}:
            css_class += " tragicomic"
        if normalized in {"transferable_rule", "pregunta de transferencia"}:
            css_class += " rule"
        display_heading = DISPLAY_HEADINGS.get(normalized, heading)
        rendered_sections.append(
            f'<section class="{css_class}">\n'
            f"  <h2>{html.escape(display_heading)}</h2>\n"
            f"  {render_lines(lines)}\n"
            "</section>"
        )

    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <style>{CSS}</style>
</head>
<body>
  <main>
    <header>
      <h1>{html.escape(title)}</h1>
      <p class="muted">{html.escape(subtitle)}</p>
    </header>
    {''.join(rendered_sections)}
  </main>
</body>
</html>
"""


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a case markdown file to simple HTML.")
    parser.add_argument("case_path", type=Path)
    parser.add_argument("output_path", type=Path)
    args = parser.parse_args()

    markdown = args.case_path.read_text(encoding="utf-8")
    html_output = render_case(markdown)
    args.output_path.parent.mkdir(parents=True, exist_ok=True)
    args.output_path.write_text(html_output, encoding="utf-8")
    print(f"Wrote {args.output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
