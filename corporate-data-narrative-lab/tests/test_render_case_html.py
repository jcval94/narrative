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


def test_render_case_uses_opening_hook_as_subtitle() -> None:
    markdown = """
# Caso: El verde sospechoso

## opening_hook
A las 9:03 el tablero se puso verde.

## protagonist_or_student_role
Eres la analista que revisa el comité.
"""

    output = render_case(markdown)

    assert "A las 9:03 el tablero se puso verde." in output
    assert "opening_hook" not in output
    assert "Tu rol en la investigación" in output
