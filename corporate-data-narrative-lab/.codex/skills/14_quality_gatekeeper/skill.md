# 14 Quality Gatekeeper

## Cuándo usarla

Úsala al final de cada caso y antes de publicarlo.

## Qué hace

Es la última barrera editorial, analítica, educativa y arquitectónica.

## Qué no hace

No negocia dashboards, no aprueba casos incompletos por intención, no deja pasar visualizaciones que no sostienen la historia y no aprueba reportes expositivos disfrazados de narrativa.

## Conexión con las demás skills

Recibe todas las salidas del flujo `00` a `13` y decide si el caso puede publicarse.

## Cuándo detenerse y pedir revisión

Devuelve `NEEDS_REVISION` si el caso es corregible. Devuelve `FAIL` si viola reglas absolutas o no enseña una habilidad transferible.

## Entradas necesarias

- Caso markdown.
- HTML.
- Visual spec.
- Data spec.
- Resultado de validación.
- Campos del `Narrative Learning Experience Standard`.

## Salida esperada

```text
PASS / NEEDS_REVISION / FAIL
```

Con hallazgos accionables.

## Revisión obligatoria

- Tesis clara.
- Intriga inicial.
- Protagonista, narrador o rol del alumno.
- Misterio central.
- Nivel analítico.
- Técnica mínima suficiente.
- Conflicto realista.
- Evidencia visual mínima.
- Evidencia visual como escena del crimen.
- Pregunta activa del alumno.
- Traducción de jerga.
- Narrativa entendible y memorable.
- Giro plausible.
- Solución robusta.
- Solución débil.
- Piloto medible.
- Humor integrado y dosificado.
- Cierre tragicómico.
- Regla transferible.
- HTML simple.
- Cero dashboard innecesario.
- Tarjetas narrativas permitidas solo si no parecen KPI cards.

## Fallo automático

Devuelve `FAIL` si detectas:

- dashboard;
- KPI cards de monitoreo;
- filtros, tabs, drilldowns, navegación compleja o self-service;
- más de dos visualizaciones sin justificación;
- apertura con contexto expositivo en vez de intriga;
- alumno como lector pasivo;
- falta de tesis;
- falta de misterio central;
- falta de pista visual;
- falta de pregunta activa;
- jerga técnica sin traducción;
- falta de nivel analítico;
- falta de técnica mínima suficiente;
- falta de conflicto;
- falta de giro;
- falta de piloto;
- humor excesivo;
- humor que ridiculiza personas, áreas reales o grupos vulnerables;
- gráfica que no soporta la historia;
- sobreingeniería técnica;
- subingeniería técnica;
- caso que no enseña una habilidad transferible;
- cierre sin consecuencia tragicómica, regla transferible o pregunta de transferencia;
- datos personales reales.

## Criterios de aceptación

- El veredicto es claro.
- Los hallazgos son específicos.
- Las correcciones apuntan a publicar el caso.
