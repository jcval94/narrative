from tools.validate_case_structure import find_dashboard_violations, validate_markdown


NARRATIVE_LEARNING_SECTIONS = [
    "opening_hook",
    "protagonist_or_student_role",
    "central_mystery",
    "Tesis del caso",
    "Nivel analítico del caso",
    "Técnica principal",
    "Técnica mínima suficiente",
    "official_story",
    "hidden_story",
    "visual_clue",
    "student_question",
    "jargon_translation",
    "Evidencia visual",
    "Qué parece a simple vista",
    "Qué está pasando realmente",
    "analytical_twist",
    "weak_decision",
    "robust_decision",
    "Piloto propuesto",
    "tragicomic_ending",
    "transferable_rule",
    "Pregunta de transferencia",
    "Respuesta esperada",
    "Riesgos éticos / privacidad / sesgo",
    "Checklist de calidad",
]


def build_narrative_learning_case() -> str:
    content = {
        "opening_hook": "A las 9:03 el tablero se puso verde y Operativa siguió apagando incendios.",
        "protagonist_or_student_role": "Eres la analista que debe decidir si el comité puede celebrar.",
        "central_mystery": "El KPI mejora, pero la cola de casos viejos no se mueve.",
        "Tesis del caso": "Un KPI puede mejorar porque cambió qué casos entran al conteo.",
        "Nivel analítico del caso": "Nivel analítico 2 con comparación temporal simple.",
        "Técnica principal": "Tasa antes/después.",
        "Técnica mínima suficiente": "La técnica mínima suficiente es una tasa con denominador claro.",
        "official_story": "Parece que los casos resueltos a tiempo mejoraron.",
        "hidden_story": "La historia oculta es que cambió el grupo de casos que sí cuenta.",
        "visual_clue": "La pista visual es el contraste entre mejora del KPI y acumulación de casos excluidos.",
        "student_question": "¿Qué mirarías primero y qué conclusión sería peligrosa?",
        "jargon_translation": "Casos resueltos a tiempo (SLA). Grupo de casos que sí cuenta (denominador).",
        "Evidencia visual": "Una gráfica sintética con anotación muestra la pista y el contraste.",
        "Qué parece a simple vista": "Parece una mejora sostenida.",
        "Qué está pasando realmente": "Está cambiando el denominador, no necesariamente el servicio.",
        "analytical_twist": "El giro analítico aparece cuando se separan casos incluidos y excluidos.",
        "weak_decision": "Celebrar el KPI y cerrar el seguimiento sería cómodo pero peligroso.",
        "robust_decision": "Auditar la definición y reportar incluidos y excluidos mantiene interpretabilidad.",
        "Piloto propuesto": "Piloto sintético con control, métrica de éxito y reversa.",
        "tragicomic_ending": "El comité pidió mantener el verde, pero ahora con una nota menos feliz.",
        "transferable_rule": "Antes de creerle a un KPI, pregúntale si sigue midiendo lo mismo.",
        "Pregunta de transferencia": "¿En qué otro proceso una mejora podría venir de cambiar quién cuenta?",
        "Respuesta esperada": "El alumno debe sospechar del denominador y proponer una acción robusta.",
        "Riesgos éticos / privacidad / sesgo": "No se usan datos personales reales.",
        "Checklist de calidad": "Sin dashboard, sin filtros, sin KPI cards de monitoreo.",
    }
    return "# Caso: El verde sospechoso\n\n" + "\n\n".join(
        f"## {section}\n{content[section]}" for section in NARRATIVE_LEARNING_SECTIONS
    )


def test_valid_case_passes_required_sections() -> None:
    sections = [
        "Tesis del caso",
        "Nivel analítico del caso",
        "Técnica principal",
        "Técnica mínima suficiente",
        "Por qué no usar una solución más compleja",
        "Por qué no usar una solución más simple",
        "Resumen ejecutivo",
        "Contexto",
        "Áreas involucradas",
        "Evidencia visual",
        "Qué parece a simple vista",
        "Qué está pasando realmente",
        "Giro después de 3 meses",
        "Decisión incorrecta de negocio",
        "Acción robusta desde Data",
        "Acción débil sin expertise en datos",
        "Piloto propuesto",
        "Comentario tragicómico del narrador",
        "Aprendizajes",
        "Preguntas para el alumno",
        "Respuesta esperada",
        "Riesgos éticos / privacidad / sesgo",
        "Checklist de calidad",
    ]
    markdown = "# Caso: Prueba\n\n" + "\n\n".join(
        f"## {section}\nContenido sintético con piloto medible." for section in sections
    )

    assert validate_markdown(markdown) == []


def test_narrative_learning_standard_passes_with_synthetic_snippet() -> None:
    markdown = build_narrative_learning_case()

    assert validate_markdown(markdown, narrative_learning_standard=True) == []


def test_narrative_learning_standard_rejects_context_opening() -> None:
    markdown = build_narrative_learning_case().replace(
        "A las 9:03 el tablero se puso verde y Operativa siguió apagando incendios.",
        "Contexto breve: este caso explica una métrica de atención.",
    )

    errors = validate_markdown(markdown, narrative_learning_standard=True)

    assert any("Weak opening" in error for error in errors)


def test_narrative_learning_standard_flags_untranslated_jargon() -> None:
    markdown = build_narrative_learning_case().replace(
        "Casos resueltos a tiempo (SLA). Grupo de casos que sí cuenta (denominador).",
        "SLA y uplift.",
    )

    errors = validate_markdown(markdown, narrative_learning_standard=True)

    assert any("Potential untranslated jargon" in error for error in errors)


def test_missing_section_fails() -> None:
    markdown = "# Caso: Incompleto\n\n## Tesis del caso\nContenido sintético."

    errors = validate_markdown(markdown)

    assert any("Missing section" in error for error in errors)


def test_dashboard_creation_pattern_fails() -> None:
    markdown = "## Evidencia visual\nVamos a crear filtros por sucursal y una tabla exploratoria."

    errors = find_dashboard_violations(markdown)

    assert errors


def test_dashboard_guardrail_language_is_allowed() -> None:
    markdown = "## Evidencia visual\nNo crear filtros. El dashboard no mentía; omitía historia."

    errors = find_dashboard_violations(markdown)

    assert errors == []
