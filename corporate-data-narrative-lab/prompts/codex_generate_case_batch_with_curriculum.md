# Codex Generate Case Batch With Curriculum

Genera una tanda de casos que cubra niveles distintos del currículo:

```text
Niveles: [lista]
Tema general: [opcional]
Cantidad: [n]
```

Cada caso debe usar una técnica distinta o una forma distinta de pensar con datos. Evita convertir todo en clasificación supervisada.

Para cada caso:

- empieza con `00_curriculum_mapper`;
- declara nivel analítico y técnica mínima suficiente;
- usa HTML simple con una visualización central;
- evita dashboards, filtros, pestañas, KPI cards y self-service;
- incluye humor tragicómico controlado;
- valida con `14_quality_gatekeeper`.
