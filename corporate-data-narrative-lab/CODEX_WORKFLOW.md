# Codex Workflow

Este repositorio no crea dashboards. Crea narrativas con evidencia visual.

La técnica mínima suficiente manda. No uses modelos si una tasa resuelve el caso. No uses una tasa si el comportamiento se adapta y requiere monitoreo.

Flujo recomendado para crear o mejorar un caso.

```text
0. curriculum_mapper
1. case_thesis_builder
2. corporate_conflict_builder
3. data_signal_designer
4. synthetic_evidence_generator
5. simple_visual_builder
6. narrative_case_writer
7. tragicomic_editor
8. learning_designer
9. business_decision_simulator
10. pilot_designer
11. ethics_and_risk_reviewer
12. senior_data_reviewer
13. html_story_renderer
14. quality_gatekeeper
```

## Protocolo

1. Define el tema o problema.
2. Selecciona nivel analítico y técnica mínima suficiente.
3. Declara la tesis del caso en una frase.
4. Construye el conflicto entre áreas.
5. Diseña la señal visual mínima.
6. Diseña datos sintéticos que sostengan esa señal.
7. Escribe el caso con estructura narrativa.
8. Agrega humor con dosis controlada.
9. Diseña actividades y respuesta esperada.
10. Simula una mala decisión defendible.
11. Propón piloto medible.
12. Revisa ética, privacidad y sesgo.
13. Revisa rigor analítico.
14. Renderiza HTML simple.
15. Ejecuta control de calidad.

Validaciones mínimas:

```powershell
python tools/validate_case_structure.py examples/cases/NN_caso.md
python tools/validate_html_story.py examples/html/NN_caso.html
python -m pytest
```

## Regla De Parada

Si durante el flujo aparece la necesidad de filtros, pestañas, múltiples KPIs o exploración libre, detente. Reescribe la pregunta narrativa hasta que una sola evidencia visual pueda sostenerla.

También detente si:

- la técnica se eligió por sofisticación y no por necesidad;
- una técnica simple no resiste adaptación del comportamiento;
- la visualización se volvió más importante que la historia;
- el HTML empieza a parecer app, BI o self-service.
