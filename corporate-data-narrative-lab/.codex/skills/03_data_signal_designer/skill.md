# 03 Data Signal Designer

## Cuándo usarla

Úsala cuando ya existe tesis y conflicto, pero antes de generar datos o HTML.

## Qué hace

Diseña el patrón visual mínimo que revela una segunda capa de la historia.

## Qué no hace

No diseña dashboards, no recomienda múltiples vistas por comodidad y no añade variables que no cambian la decisión.

## Conexión con las demás skills

Recibe tesis y conflicto desde `01_case_thesis_builder` y `02_corporate_conflict_builder`; entrega variables mínimas a `04_synthetic_evidence_generator` y restricciones visuales a `05_simple_visual_builder`.

## Cuándo detenerse y pedir revisión

Detente si la señal necesita filtros para verse, si requiere más de dos visualizaciones, o si la gráfica solo decora la historia.

## Entradas necesarias

- Tesis.
- Nivel analítico.
- Técnica mínima suficiente.
- Lectura superficial.
- Lectura correcta.

## Salida esperada

- Patrón visual mínimo.
- Tipo de gráfica.
- Variables necesarias.
- Anotaciones.
- Qué debe notar el alumno.
- Qué no debe incluirse.

Pregunta central: ¿qué tendría que ver el alumno en una sola gráfica para sospechar que hay más historia?

## Procedimiento

1. Escribe la pregunta: "¿qué tendría que ver el alumno para sospechar?"
2. Selecciona una sola forma visual.
3. Define los ejes y series mínimos.
4. Define una o dos anotaciones.
5. Verifica que la señal pueda entenderse sin filtros.

## Errores a evitar

- Proponer dashboards.
- Usar varias gráficas para compensar una tesis débil.
- Agregar variables que no cambian la conclusión.
- Diseñar exploración cuando se necesita evidencia.

## Criterios de aceptación

- La gráfica revela una segunda capa.
- Hay máximo dos anotaciones.
- No requiere interacción.
- La señal conecta directamente con la tesis.
