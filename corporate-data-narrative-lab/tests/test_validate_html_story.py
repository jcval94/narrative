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


def test_narrative_learning_html_passes_with_synthetic_snippet() -> None:
    html = """
    <html><body>
      <header><h1>El verde sospechoso</h1><p>A las 9:03 el tablero se puso verde.</p></header>
      <h2>Tu rol en la investigación</h2>
      <p>Eres la analista que debe revisar el comité.</p>
      <h2>El misterio</h2>
      <p>La métrica mejora, pero la operación no.</p>
      <h2>Nivel analítico</h2>
      <p>Técnica mínima suficiente: tasa antes/después.</p>
      <h2>Técnica</h2>
      <p>Comparación temporal simple.</p>
      <h2>Evidencia visual</h2>
      <svg></svg>
      <p>Pista visual: el contraste entre incluidos y excluidos.</p>
      <p>Lectura guiada: mira primero la línea de corte.</p>
      <h2>Qué parece</h2>
      <p>Lo que parece: todo mejora.</p>
      <h2>Qué revela</h2>
      <p>Lo que realmente pasa: cambió quién cuenta.</p>
      <h2>Pregunta activa</h2>
      <p>¿Qué mirarías primero?</p>
      <h2>Traducción de jerga</h2>
      <p>Casos resueltos a tiempo antes de decir SLA.</p>
      <h2>Giro</h2>
      <p>El giro aparece al separar grupos.</p>
      <h2>Acción robusta</h2>
      <p>Auditar la definición.</p>
      <h2>Acción débil</h2>
      <p>Celebrar sin revisar.</p>
      <h2>Decisión cómoda</h2>
      <p>Cerrar el seguimiento.</p>
      <h2>Piloto</h2>
      <p>Control, éxito y reversa.</p>
      <h2>Comentario tragicómico</h2>
      <p>El comité pidió mantener el verde, pero con letra chica.</p>
      <h2>Cierre tragicómico</h2>
      <p>La celebración sobrevivió; el Excel no.</p>
      <h2>Regla transferible</h2>
      <p>Antes de creerle a un KPI, pregúntale si sigue midiendo lo mismo.</p>
      <h2>Pregunta de transferencia</h2>
      <p>¿Dónde más puede cambiar quién cuenta?</p>
      <h2>Preguntas</h2>
      <p>¿Qué dato falta?</p>
    </body></html>
    """

    assert validate_html(html, narrative_learning_standard=True) == []


def test_html_with_filter_fails() -> None:
    html = "<html><body><select><option>Filtro</option></select></body></html>"

    errors = validate_html(html)

    assert any("Forbidden" in error for error in errors)


def test_narrative_learning_html_rejects_dashboard_class() -> None:
    html = """
    <html><body>
      <section class="dashboard-grid"><svg></svg></section>
    </body></html>
    """

    errors = validate_html(html, narrative_learning_standard=True)

    assert any("Forbidden" in error for error in errors)


def test_narrative_learning_html_requires_active_question() -> None:
    html = """
    <html><body>
      <h2>Nivel analítico</h2><h2>Técnica</h2><h2>Evidencia visual</h2><svg></svg>
      <h2>Qué parece</h2><h2>Qué revela</h2><h2>Giro</h2>
      <h2>Acción robusta</h2><h2>Acción débil</h2><h2>Piloto</h2>
      <h2>Comentario tragicómico</h2><h2>Preguntas</h2>
      <h2>Misterio</h2><p>Pista y lectura guiada. Lo que parece y lo que realmente pasa.</p>
      <h2>Pregunta activa</h2><p>Observa la gráfica con calma.</p>
      <h2>Traducción</h2><p>Lenguaje humano primero.</p>
      <h2>Decisión cómoda</h2><p>Cerrar.</p>
      <h2>Cierre tragicómico</h2><p>Terminó en minuta.</p>
      <h2>Regla transferible</h2><p>Pregunta por la definición.</p>
      <h2>Pregunta de transferencia</h2><p>Aplica en otro contexto.</p>
    </body></html>
    """

    errors = validate_html(html, narrative_learning_standard=True)

    assert any("Missing active question" in error for error in errors)
