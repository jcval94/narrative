from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from pathlib import Path


LEGACY_REQUIRED_SECTIONS = [
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

NARRATIVE_LEARNING_REQUIRED_SECTIONS = [
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


FORBIDDEN_DASHBOARD_TERMS = [
    "filtro",
    "filtros",
    "pestaña",
    "pestañas",
    "kpi card",
    "kpi cards",
    "drilldown",
    "drilldowns",
    "self-service",
    "explorador",
    "exploradores",
    "navegación compleja",
    "dashboard interactivo",
    "tabla exploratoria",
    "tablas exploratorias",
    "scorecard",
    "panel ejecutivo",
]

FORBIDDEN_CREATION_PATTERNS = [
    r"\b(crea|crear|construye|construir|agrega|agregar|incluye|incluir|usa|usar|permite|permitir)\b.{0,45}\b(dashboard|filtros?|pestañas?|tabs?|kpi cards?|drilldowns?|self-service|exploradores?|tabla exploratoria|tablas exploratorias)\b",
    r"\b(dashboard|filtros?|pestañas?|tabs?|kpi cards?|drilldowns?|self-service|exploradores?|tabla exploratoria|tablas exploratorias)\b.{0,45}\b(interactivo|exploratorio|self-service|descargable)\b",
]

NEGATION_MARKERS = ("no ", "sin ", "cero ", "evita ", "evitar ", "prohibir ", "prohíbe ")

NARRATIVE_LEARNING_MARKERS = {
    normalize
    for normalize in [
        "opening_hook",
        "protagonist_or_student_role",
        "central_mystery",
        "official_story",
        "hidden_story",
        "visual_clue",
        "student_question",
        "jargon_translation",
        "analytical_twist",
        "weak_decision",
        "robust_decision",
        "tragicomic_ending",
        "transferable_rule",
    ]
}

WEAK_OPENING_PATTERNS = [
    r"^(contexto|resumen ejecutivo)\b",
    r"^(este caso|en este caso|el objetivo de este caso)\b",
    r"^breve contexto\b",
]

ACTIVE_QUESTION_MARKERS = [
    "?",
    "que mirarias",
    "que mirarías",
    "que mirar",
    "conclusion peligrosa",
    "conclusión peligrosa",
    "dato falta",
    "hipotesis",
    "hipótesis",
    "que paso",
    "qué pasó",
]

JARGON_TRANSLATIONS = {
    "sla": ["casos resueltos a tiempo", "tiempo comprometido"],
    "denominador": ["grupo de casos", "grupo que si cuenta", "grupo que sí cuenta"],
    "uplift": ["mejora adicional", "atribuible a la accion", "atribuible a la acción"],
    "drift": ["comportamiento de los datos cambia", "datos cambia con el tiempo"],
    "cohorte": ["grupo comparable", "grupo de clientes", "grupo de casos"],
    "umbral": ["linea de corte", "línea de corte"],
    "ventana temporal": ["periodo observado", "período observado"],
    "incrementalidad": ["no habria ocurrido", "no habría ocurrido", "sin la intervencion", "sin la intervención"],
}


def normalize_heading(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().lower())


def fold_text(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value.lower())
    ascii_text = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    return re.sub(r"\s+", " ", ascii_text).strip()


def extract_headings(markdown: str) -> set[str]:
    headings: set[str] = set()
    for line in markdown.splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if match:
            headings.add(normalize_heading(match.group(1)))
    return headings


def extract_section_map(markdown: str) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current_heading: str | None = None

    for line in markdown.splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if match:
            current_heading = normalize_heading(match.group(1))
            sections.setdefault(current_heading, [])
            continue
        if current_heading is not None:
            sections[current_heading].append(line)

    return {heading: "\n".join(lines).strip() for heading, lines in sections.items()}


def first_body_text(markdown: str) -> str:
    for line in markdown.splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            return stripped
    return ""


def uses_narrative_learning_standard(headings: set[str]) -> bool:
    return bool(headings.intersection(NARRATIVE_LEARNING_MARKERS))


def has_negation_before(line: str, term: str) -> bool:
    index = line.find(term)
    if index < 0:
        return False
    prefix = line[max(0, index - 35) : index]
    return any(marker in prefix for marker in NEGATION_MARKERS)


def find_dashboard_violations(markdown: str) -> list[str]:
    violations: list[str] = []
    for line in markdown.lower().splitlines():
        for pattern in FORBIDDEN_CREATION_PATTERNS:
            if re.search(pattern, line) and not any(marker in line for marker in NEGATION_MARKERS):
                violations.append(f"Potential dashboard creation pattern: {line.strip()}")
                break
        for term in FORBIDDEN_DASHBOARD_TERMS:
            if term in line and not has_negation_before(line, term):
                if "dashboard no mentía" in line or "dashboard no mentia" in line:
                    continue
                if line.strip().startswith("- no ") or line.strip().startswith("- sin "):
                    continue
                violations.append(f"Potential dashboard term without guardrail: {term}")
    return violations


def find_untranslated_jargon(markdown: str) -> list[str]:
    folded = fold_text(markdown)
    untranslated: list[str] = []
    for term, translations in JARGON_TRANSLATIONS.items():
        folded_term = fold_text(term)
        if folded_term in folded and not any(fold_text(translation) in folded for translation in translations):
            untranslated.append(term)
    return untranslated


def validate_narrative_learning_standard(markdown: str) -> list[str]:
    errors: list[str] = []
    sections = extract_section_map(markdown)

    opening = sections.get("opening_hook", "") or first_body_text(markdown)
    folded_opening = fold_text(opening[:300])
    if not opening:
        errors.append("Missing opening intrigue.")
    elif any(re.search(pattern, folded_opening) for pattern in WEAK_OPENING_PATTERNS):
        errors.append("Weak opening: start with intrigue, not context or executive summary.")

    student_question = sections.get("student_question", "")
    folded_question = fold_text(student_question)
    if not any(fold_text(marker) in folded_question for marker in ACTIVE_QUESTION_MARKERS):
        errors.append("Missing active student question: ask what to inspect, suspect, test, or reject.")

    visual_clue = sections.get("visual_clue", "")
    folded_visual = fold_text(visual_clue + "\n" + sections.get("evidencia visual", ""))
    if not any(marker in folded_visual for marker in ["pista", "sospech", "contraste", "anotacion", "anotacion", "lo que parece"]):
        errors.append("Missing visual clue or guided visual-reading language.")

    jargon_section = sections.get("jargon_translation", "")
    untranslated = find_untranslated_jargon(markdown)
    if untranslated and len(jargon_section.strip()) < 20:
        errors.append("Missing jargon_translation content for technical terms.")
    for term in untranslated[:4]:
        errors.append(f"Potential untranslated jargon: {term}")

    transferable_rule = sections.get("transferable_rule", "")
    if len(transferable_rule.strip()) < 20:
        errors.append("Missing transferable rule.")

    transfer_question = sections.get("pregunta de transferencia", "")
    if "?" not in transfer_question:
        errors.append("Missing transfer question.")

    ending = sections.get("tragicomic_ending", "")
    if len(ending.strip()) < 20:
        errors.append("Missing tragicomic ending.")

    return errors


def validate_markdown(markdown: str, narrative_learning_standard: bool = False) -> list[str]:
    headings = extract_headings(markdown)
    errors: list[str] = []
    should_use_learning_standard = narrative_learning_standard or uses_narrative_learning_standard(headings)
    required_sections = (
        NARRATIVE_LEARNING_REQUIRED_SECTIONS
        if should_use_learning_standard
        else LEGACY_REQUIRED_SECTIONS
    )

    for section in required_sections:
        if normalize_heading(section) not in headings:
            errors.append(f"Missing section: {section}")

    lowered = markdown.lower()
    visual_count = len(re.findall(r"\b(gráfica|grafica|visualización|visualizacion)\b", lowered))
    if visual_count > 18:
        errors.append(
            "Potential over-visualization: many visual references found. Confirm this is not a dashboard."
        )

    errors.extend(find_dashboard_violations(markdown))

    if "piloto" not in lowered:
        errors.append("Missing pilot language.")

    if "sintético" not in lowered and "sintetico" not in lowered:
        errors.append("Missing explicit synthetic-data language.")

    if "técnica mínima suficiente" not in lowered and "tecnica minima suficiente" not in lowered:
        errors.append("Missing minimum-sufficient-technique language.")

    if "nivel analítico" not in lowered and "nivel analitico" not in lowered:
        errors.append("Missing analytic-level language.")

    if should_use_learning_standard:
        errors.extend(validate_narrative_learning_standard(markdown))

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a narrative case markdown file.")
    parser.add_argument(
        "--narrative-learning-standard",
        action="store_true",
        help="Apply the Narrative Learning Experience Standard for new or regenerated cases.",
    )
    parser.add_argument("case_path", type=Path)
    args = parser.parse_args()

    if not args.case_path.exists():
        print(f"ERROR: file not found: {args.case_path}", file=sys.stderr)
        return 2

    markdown = args.case_path.read_text(encoding="utf-8")
    errors = validate_markdown(
        markdown,
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
