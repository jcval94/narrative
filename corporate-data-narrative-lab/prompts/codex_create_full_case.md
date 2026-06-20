# Codex Create Full Case

Crea un caso completo usando todas las fases de `CODEX_WORKFLOW.md`.

Empieza obligatoriamente con `00_curriculum_mapper`. Declara nivel analítico, técnica principal y técnica mínima suficiente antes de escribir historia, datos o HTML.

Después diseña el `Narrative Learning Experience Standard` antes de renderizar: `opening_hook`, `protagonist_or_student_role`, `central_mystery`, `official_story`, `hidden_story`, `visual_clue`, `student_question`, `jargon_translation`, `analytical_twist`, `weak_decision`, `robust_decision`, `tragicomic_ending` y `transferable_rule`.

Entrada:

```text
Tema: [tema]
Restricción o área: [opcional]
Nivel sugerido: [opcional]
```

Salida requerida:

- `examples/cases/NN_nombre.md`
- `examples/data_specs/NN_nombre.yml`
- `examples/visual_specs/NN_nombre.yml`
- `examples/html/NN_nombre.html`

El caso debe abrir con intriga, no con contexto breve. Debe sentirse como investigación educativa, no como reporte expositivo.

Antes de terminar, valida estructura y confirma que no hay dashboard.

También confirma que no hay filtros, pestañas, KPI cards de monitoreo, exploradores, self-service ni navegación compleja. Usa las validaciones con `--narrative-learning-standard` cuando el caso use el nuevo estándar. Termina con `14_quality_gatekeeper`.
