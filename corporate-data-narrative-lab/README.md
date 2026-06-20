# Corporate Data Narrative Lab

Repositorio para crear casos educativos de ciencia de datos aplicada a negocio. Cada caso combina una narrativa corporativa, un conflicto plausible entre áreas, datos sintéticos, una visualización HTML mínima y una decisión de negocio imperfecta que permite aprender algo transferible.

**Este proyecto no crea dashboards. Crea narrativas con evidencia visual.**

La visualización no es el producto principal. La visualización es la evidencia que sostiene una historia: una anomalía, una definición rota, un incentivo perverso, una ventana temporal mal elegida o una métrica que mejoró por la razón equivocada.

La técnica mínima suficiente manda. No uses modelos si una tasa resuelve el caso. No uses una tasa si el comportamiento se adapta y requiere monitoreo.

## Qué Es

- Un laboratorio de casos didácticos sobre pensamiento analítico aplicado.
- Una guía para que Codex produzca casos narrativos con datos sintéticos.
- Una colección de ejemplos HTML autocontenidos, sobrios y simples.
- Un sistema de revisión para mantener rigor analítico, humor dosificado y cero dashboards.

## Qué No Es

- No es una aplicación web.
- No es una plataforma de BI.
- No es un generador de dashboards.
- No es una herramienta self-service.
- No es un explorador de datos.
- No es un catálogo de modelos avanzados.
- No es una excusa para usar ML cuando basta una tasa, una mediana o una ventana temporal bien definida.

## Regla De Oro

> Este repositorio no crea dashboards. Crea narrativas corporativas centradas en datos. Cada visualización debe funcionar como evidencia dentro de una historia, no como herramienta exploratoria. Si una visualización necesita filtros, pestañas, múltiples KPIs o múltiples vistas, probablemente estás construyendo el producto equivocado.

## Reglas Absolutas

- Cada HTML es una página sencilla, vertical y autocontenida.
- Cada caso tiene máximo una visualización central, salvo excepción justificada de máximo dos.
- La gráfica nunca sustituye la historia: la prueba.
- La técnica avanzada solo entra cuando la técnica simple destruye la interpretación o no resiste adaptación.
- Un caso que necesita navegación compleja, filtros, drilldowns, KPI cards o self-service debe reescribirse.

## Cómo Usarlo Con Codex

1. Elige un tema de negocio, una gráfica existente o un problema operativo.
2. Pide a Codex que use el flujo de [CODEX_WORKFLOW.md](CODEX_WORKFLOW.md).
3. Codex debe seleccionar el nivel analítico mínimo suficiente usando [DATA_SCIENCE_CURRICULUM.md](DATA_SCIENCE_CURRICULUM.md).
4. Codex debe producir un caso en `examples/cases/`, una especificación de datos, una especificación visual y un HTML simple.
5. Valida la estructura y renderiza el caso.

## Crear Un Caso Nuevo

```powershell
python tools/validate_case_structure.py examples/cases/01_movimientos_pequenos_incentivos.md
python tools/validate_html_story.py examples/html/01_movimientos_pequenos_incentivos.html
python tools/render_case_html.py examples/cases/01_movimientos_pequenos_incentivos.md outputs/01_movimientos_pequenos_incentivos.html
python tools/generate_synthetic_data.py examples/data_specs/01_movimientos_pequenos_incentivos.yml outputs/movimientos.csv
python tools/generate_simple_chart_html.py examples/visual_specs/01_movimientos_pequenos_incentivos.yml outputs/movimientos_chart.html
```

Para crear un caso desde cero con Codex:

```text
Usa este repositorio para crear un caso nuevo sobre [tema].
Empieza con 00_curriculum_mapper y sigue CODEX_WORKFLOW.md.
Elige la técnica mínima suficiente.
No crees dashboard.
Entrega caso markdown, data spec, visual spec y HTML autocontenido.
Valida con 14_quality_gatekeeper.
```

## Estructura

- `DATA_SCIENCE_CURRICULUM.md`: mapa de niveles 0-24 para variar técnicas y complejidad.
- `NARRATIVE_PRINCIPLES.md`: cómo construir tensión, evidencia y cierre didáctico.
- `HUMOR_GUIDE.md`: cómo usar humor tragicómico sin convertir el caso en meme.
- `DATA_VISUAL_EVIDENCE_GUIDE.md`: cómo diseñar una gráfica mínima como evidencia.
- `CASE_RUBRIC.md`: rúbrica 1-5 para revisar casos.
- `.codex/skills/`: skills accionables para guiar a Codex.
- `templates/`: plantillas de caso, datos, visual y HTML.
- `examples/`: tres casos completos y sus HTMLs.
- `tools/`: utilidades mínimas de validación, render y generación sintética.

## Comandos Básicos

```powershell
python -m pytest
python tools/validate_case_structure.py examples/cases/02_cancelaciones_ventana_temporal.md
python tools/validate_html_story.py examples/html/02_cancelaciones_ventana_temporal.html
python tools/render_case_html.py examples/cases/03_kpi_que_mejoro_por_definicion.md outputs/kpi.html
```

## Criterio Rector

La solución correcta no es la más sofisticada. Es la mínima solución robusta que resuelve el problema sin destruir la interpretación de negocio.
