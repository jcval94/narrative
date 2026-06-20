# Codex Create Full Case

Crea un caso completo usando todas las fases de `CODEX_WORKFLOW.md`.

Empieza obligatoriamente con `00_curriculum_mapper`. Declara nivel analítico, técnica principal y técnica mínima suficiente antes de escribir historia, datos o HTML.

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

Antes de terminar, valida estructura y confirma que no hay dashboard.

También confirma que no hay filtros, pestañas, KPI cards, exploradores, self-service ni navegación compleja. Termina con `14_quality_gatekeeper`.
