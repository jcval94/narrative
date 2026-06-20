from tools.validate_case_structure import find_dashboard_violations, validate_markdown


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
