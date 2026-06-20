from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REQUIRED_SECTIONS = [
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
]

FORBIDDEN_CREATION_PATTERNS = [
    r"\b(crea|crear|construye|construir|agrega|agregar|incluye|incluir|usa|usar|permite|permitir)\b.{0,45}\b(dashboard|filtros?|pestañas?|tabs?|kpi cards?|drilldowns?|self-service|exploradores?|tabla exploratoria|tablas exploratorias)\b",
    r"\b(dashboard|filtros?|pestañas?|tabs?|kpi cards?|drilldowns?|self-service|exploradores?|tabla exploratoria|tablas exploratorias)\b.{0,45}\b(interactivo|exploratorio|self-service|descargable)\b",
]

NEGATION_MARKERS = ("no ", "sin ", "cero ", "evita ", "evitar ", "prohibir ", "prohíbe ")


def normalize_heading(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().lower())


def extract_headings(markdown: str) -> set[str]:
    headings: set[str] = set()
    for line in markdown.splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*$", line)
        if match:
            headings.add(normalize_heading(match.group(1)))
    return headings


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


def validate_markdown(markdown: str) -> list[str]:
    headings = extract_headings(markdown)
    errors: list[str] = []

    for section in REQUIRED_SECTIONS:
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

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a narrative case markdown file.")
    parser.add_argument("case_path", type=Path)
    args = parser.parse_args()

    if not args.case_path.exists():
        print(f"ERROR: file not found: {args.case_path}", file=sys.stderr)
        return 2

    markdown = args.case_path.read_text(encoding="utf-8")
    errors = validate_markdown(markdown)

    if errors:
        print("NEEDS_REVISION")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
