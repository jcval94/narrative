# Case Rubric

Este repositorio no crea dashboards. Crea narrativas con evidencia visual.

La técnica mínima suficiente manda. No uses modelos si una tasa resuelve el caso. No uses una tasa si el comportamiento se adapta y requiere monitoreo.

Califica cada dimensión de 1 a 5.

| Dimensión | 1 | 3 | 5 |
| --- | --- | --- | --- |
| Tesis | No hay verdad incómoda clara | Hay tesis, pero genérica | La tesis es clara, transferible y guía todo el caso |
| Intriga inicial | Abre con contexto expositivo o resumen | Hay una tensión inicial, pero tarda en aparecer | Abre con escena, anomalía, contradicción o pregunta incómoda |
| Historia mínima | Faltan protagonista, conflicto, pista o consecuencia | Hay historia, pero algunos hitos son débiles | Incluye rol/protagonista, conflicto, pista visual, giro, consecuencia, decisión débil, acción robusta y cierre |
| Rol del alumno | Alumno lector pasivo | Algunas preguntas activas | Alumno investiga: mira, sospecha, formula hipótesis y decide |
| Nivel analítico | Técnica arbitraria | Técnica razonable pero poco justificada | Técnica mínima suficiente, explícita y defendible |
| Técnica mínima suficiente | Se usa complejidad decorativa o insuficiente | Hay ajuste parcial entre técnica y problema | La técnica revela exactamente lo necesario |
| Conflicto | Áreas caricaturizadas o ausentes | Tensión plausible pero superficial | Incentivos de cada área son realistas y comprensibles |
| Patrón analítico | La señal no sostiene la conclusión | La señal sugiere algo, pero falta precisión | La señal visual hace inevitable la pregunta correcta |
| Visualización | Parece dashboard o está sobrecargada | Es simple, pero necesita mejor foco | Es mínima, clara y funciona como evidencia |
| Visualidad pedagógica | La gráfica decora o queda aislada | Hay anotación básica | La visualización funciona como escena del crimen: pista, contraste y lectura guiada |
| Visualidad sin dashboard | Usa KPI cards, filtros, tabs o monitoreo | Tiene tarjetas narrativas con riesgo de parecer BI | Usa tarjetas narrativas, callouts o mini cálculos solo para enseñar la historia |
| Narrativa | Lineal, genérica o académica | Tiene historia pero poco giro | Tiene tensión, revelación, decisión imperfecta y giro |
| Claridad para principiantes | Mucha jerga o explicación opaca | Algunos términos se explican | Primero lenguaje humano, después término técnico |
| Reducción de jerga | Términos técnicos sin traducción | Traducciones parciales | Cada término clave se traduce con ejemplo o lenguaje de negocio |
| Solución robusta | Lista genérica de buenas prácticas | Correcta pero incompleta | Resuelve el problema manteniendo interpretación de negocio |
| Solución débil | Demasiado absurda | Plausible pero poco peligrosa | Cómoda, defendible y peligrosamente insuficiente |
| Piloto | No mide nada | Mide algo, pero sin reversa clara | Tiene población, métrica, control, éxito, reversa y monitoreo |
| Humor integrado | Excesivo, ofensivo, ausente o pegado al final | Algunas frases útiles | Seco, respetuoso, dentro de la historia y útil para recordar |
| Final memorable | Cierra con resumen genérico | Cierra con aprendizaje pero poca escena | Termina con consecuencia tragicómica, regla práctica y pregunta de transferencia |
| Regla transferible | No hay regla | Hay una moraleja amplia | La regla es breve, accionable y aplicable a otro caso |
| Aprendizaje | Obvio o no transferible | Transferible pero poco accionable | El alumno puede aplicar el criterio en otro problema |
| Rigor analítico | La narrativa tapa imprecisiones | Análisis razonable con supuestos débiles | Precisión analítica clara sin sobreingeniería |
| Simplicidad HTML | Dashboard, filtros o UI compleja | HTML simple con ruido visual | Página vertical, autocontenida y centrada en una evidencia |

## Criterios De Reprobación Automática

Un caso debe fallar si:

- construye un dashboard;
- crea filtros, pestañas, drilldowns, navegación compleja o self-service;
- usa KPI cards de monitoreo o paneles de BI disfrazados de tarjetas narrativas;
- tiene más de dos visualizaciones sin justificación;
- abre con contexto expositivo y no genera intriga;
- deja al alumno como lector pasivo;
- no tiene tesis;
- no declara nivel analítico;
- no declara técnica mínima suficiente;
- no tiene conflicto;
- no tiene pista visual;
- no tiene giro;
- no tiene piloto;
- no traduce jerga técnica clave;
- usa humor excesivo;
- usa humor para ridiculizar personas, áreas reales o grupos vulnerables;
- la gráfica no soporta la historia;
- usa una técnica innecesariamente compleja;
- usa una técnica demasiado simple para un fenómeno adaptativo;
- no enseña una habilidad transferible;
- no termina con regla transferible;
- usa datos personales reales.
