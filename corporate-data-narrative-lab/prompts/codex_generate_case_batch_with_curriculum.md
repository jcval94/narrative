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
- diseña `opening_hook`, rol del alumno, misterio central, historia oficial, historia oculta, pista visual, pregunta activa, traducción de jerga, giro, decisión débil, decisión robusta, cierre tragicómico y regla transferible;
- abre con intriga, no con contexto breve;
- usa HTML simple con una visualización central;
- evita dashboards, filtros, pestañas, KPI cards de monitoreo y self-service;
- incluye humor tragicómico integrado a la historia;
- cierra con regla transferible y pregunta de transferencia;
- valida con `14_quality_gatekeeper`.
