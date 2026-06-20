# 14 Quality Gatekeeper

## Cuándo usarla

Úsala al final de cada caso y antes de publicarlo.

## Qué hace

Es la última barrera editorial, analítica y arquitectónica.

## Qué no hace

No negocia dashboards, no aprueba casos incompletos por intención y no deja pasar visualizaciones que no sostienen la historia.

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

## Salida esperada

```text
PASS / NEEDS_REVISION / FAIL
```

Con hallazgos accionables.

## Revisión obligatoria

- Tesis clara.
- Nivel analítico.
- Técnica mínima suficiente.
- Conflicto realista.
- Evidencia visual mínima.
- Narrativa entendible.
- Giro plausible.
- Solución robusta.
- Solución débil.
- Piloto medible.
- Humor dosificado.
- HTML simple.
- Cero dashboard innecesario.

## Fallo automático

Devuelve `FAIL` si detectas:

- dashboard;
- más de dos visualizaciones sin justificación;
- falta de tesis;
- falta de nivel analítico;
- falta de técnica mínima suficiente;
- falta de conflicto;
- falta de giro;
- falta de piloto;
- humor excesivo;
- gráfica que no soporta la historia;
- sobreingeniería técnica;
- subingeniería técnica;
- caso que no enseña una habilidad transferible;
- datos personales reales.

## Criterios de aceptación

- El veredicto es claro.
- Los hallazgos son específicos.
- Las correcciones apuntan a publicar el caso.
