# 05 Simple Visual Builder

## Cuándo usarla

Úsala cuando la señal visual y los datos sintéticos ya están definidos.

## Qué hace

Construye una visualización HTML mínima que funciona como evidencia dentro de una historia y como pista de investigación para el alumno.

## Qué no hace

No crea dashboards, filtros, KPI cards de monitoreo, drilldowns, tabs, tablas exploratorias, comparadores complejos, layouts de BI ni widgets de self-service. Sí puede usar tarjetas narrativas si explican pista, contraste, mini cálculo, glosario visual o regla.

## Conexión con las demás skills

Recibe señal desde `03_data_signal_designer` y datos desde `04_synthetic_evidence_generator`; entrega la evidencia a `06_narrative_case_writer`, `13_html_story_renderer` y `14_quality_gatekeeper`.

## Cuándo detenerse y pedir revisión

Detente si la visualización necesita interacción para entenderse, si la gráfica no revela una segunda capa, o si se vuelve más importante que la narrativa.

## Entradas necesarias

- Visual evidence spec.
- Datos o valores agregados.
- Lectura superficial y lectura correcta.
- `visual_clue`.
- `student_question`.
- `official_story` y `hidden_story`.

## Salida esperada

- HTML autocontenido o bloque gráfico.
- Máximo una visualización central.
- Excepcionalmente dos si la historia lo exige.
- Título, ejes, leyenda mínima y una o dos anotaciones.
- Texto breve debajo con qué notar.
- Lectura guiada de 2 a 4 pasos.
- Comparación "lo que parece / lo que realmente pasa" si ayuda a interpretar.

## Procedimiento

1. Elige Chart.js, SVG o Canvas.
2. Crea una página o bloque visual sobrio.
3. Usa color solo para distinguir evidencia.
4. Añade anotaciones, callouts o mini cálculos solo si guían la lectura.
5. Escribe qué debe sospechar el alumno al mirar la imagen.
6. Verifica que no haya filtros, tabs, KPI cards de monitoreo ni navegación.

## Errores a evitar

- Crear dashboard.
- Añadir controles exploratorios.
- Mostrar tablas de datos.
- Usar muchas series sin necesidad.
- Hacer que el diseño sea más importante que la señal.
- Usar tarjetas con números grandes como panel ejecutivo.
- Requerir interacción para descubrir la pista.

## Criterios de aceptación

- La visualización se entiende sin interacción.
- La gráfica sostiene la tesis.
- La pista visual está explícita.
- La pregunta activa se puede responder mirando la evidencia.
- El HTML es autocontenido.
- La composición es sobria y legible.
