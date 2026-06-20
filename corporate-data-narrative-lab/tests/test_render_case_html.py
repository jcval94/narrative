from tools.render_case_html import render_case


def test_render_case_outputs_html() -> None:
    markdown = """
# Caso: KPI sospechoso

## Tesis del caso
El KPI mejoró por definición.

## Evidencia visual
- Línea antes/después.
"""

    output = render_case(markdown)

    assert "<!doctype html>" in output
    assert "Caso: KPI sospechoso" in output
    assert "Tesis del caso" in output
    assert "Línea antes/después" in output

