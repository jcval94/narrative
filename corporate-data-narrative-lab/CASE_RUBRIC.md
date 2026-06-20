# Case Rubric

Este repositorio no crea dashboards. Crea narrativas con evidencia visual.

La técnica mínima suficiente manda. No uses modelos si una tasa resuelve el caso. No uses una tasa si el comportamiento se adapta y requiere monitoreo.

Califica cada dimensión de 1 a 5.

| Dimensión | 1 | 3 | 5 |
| --- | --- | --- | --- |
| Tesis | No hay verdad incómoda clara | Hay tesis, pero genérica | La tesis es clara, transferible y guía todo el caso |
| Nivel analítico | Técnica arbitraria | Técnica razonable pero poco justificada | Técnica mínima suficiente, explícita y defendible |
| Técnica mínima suficiente | Se usa complejidad decorativa o insuficiente | Hay ajuste parcial entre técnica y problema | La técnica revela exactamente lo necesario |
| Conflicto | Áreas caricaturizadas o ausentes | Tensión plausible pero superficial | Incentivos de cada área son realistas y comprensibles |
| Patrón analítico | La señal no sostiene la conclusión | La señal sugiere algo, pero falta precisión | La señal visual hace inevitable la pregunta correcta |
| Visualización | Parece dashboard o está sobrecargada | Es simple, pero necesita mejor foco | Es mínima, clara y funciona como evidencia |
| Narrativa | Lineal, genérica o académica | Tiene historia pero poco giro | Tiene tensión, revelación, decisión imperfecta y giro |
| Solución robusta | Lista genérica de buenas prácticas | Correcta pero incompleta | Resuelve el problema manteniendo interpretación de negocio |
| Solución débil | Demasiado absurda | Plausible pero poco peligrosa | Cómoda, defendible y peligrosamente insuficiente |
| Piloto | No mide nada | Mide algo, pero sin reversa clara | Tiene población, métrica, control, éxito, reversa y monitoreo |
| Humor | Excesivo, ofensivo o ausente | Algunas frases útiles | Dosificado, seco y subordinado al análisis |
| Aprendizaje | Obvio o no transferible | Transferible pero poco accionable | El alumno puede aplicar el criterio en otro problema |
| Simplicidad HTML | Dashboard, filtros o UI compleja | HTML simple con ruido visual | Página vertical, autocontenida y centrada en una evidencia |

## Criterios De Reprobación Automática

Un caso debe fallar si:

- construye un dashboard;
- crea filtros, pestañas, drilldowns, navegación compleja o self-service;
- tiene más de dos visualizaciones sin justificación;
- no tiene tesis;
- no declara nivel analítico;
- no declara técnica mínima suficiente;
- no tiene conflicto;
- no tiene giro;
- no tiene piloto;
- usa humor excesivo;
- la gráfica no soporta la historia;
- usa una técnica innecesariamente compleja;
- usa una técnica demasiado simple para un fenómeno adaptativo;
- no enseña una habilidad transferible;
- usa datos personales reales.
