from tools.validate_html_story import validate_html


def test_valid_html_story_passes() -> None:
    html = """
    <html><body>
      <h2>Nivel analítico</h2>
      <h2>Técnica</h2>
      <h2>Evidencia visual</h2>
      <svg></svg>
      <h2>Qué parece</h2>
      <h2>Qué revela</h2>
      <h2>Giro</h2>
      <h2>Acción robusta</h2>
      <h2>Acción débil</h2>
      <h2>Piloto</h2>
      <h2>Comentario tragicómico</h2>
      <h2>Preguntas</h2>
    </body></html>
    """

    assert validate_html(html) == []


def test_html_with_filter_fails() -> None:
    html = "<html><body><select><option>Filtro</option></select></body></html>"

    errors = validate_html(html)

    assert any("Forbidden" in error for error in errors)
