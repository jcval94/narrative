# 05 Simple Visual Builder

## Cuándo usarla

Úsala cuando la señal visual y los datos sintéticos ya están definidos.

## Qué hace

Construye una visualización HTML mínima que funciona como evidencia dentro de una historia.

## Qué no hace

No crea dashboards, filtros, cards, drilldowns, tabs, tablas exploratorias, comparadores complejos, layouts de BI ni widgets de self-service.

## Conexión con las demás skills

Recibe señal desde `03_data_signal_designer` y datos desde `04_synthetic_evidence_generator`; entrega la evidencia a `06_narrative_case_writer`, `13_html_story_renderer` y `14_quality_gatekeeper`.

## Cuándo detenerse y pedir revisión

Detente si la visualización necesita interacción para entenderse, si la gráfica no revela una segunda capa, o si se vuelve más importante que la narrativa.

## Entradas necesarias

- Visual evidence spec.
- Datos o valores agregados.
- Lectura superficial y lectura correcta.

## Salida esperada

- HTML autocontenido o bloque gráfico.
- Máximo una visualización central.
- Excepcionalmente dos si la historia lo exige.
- Título, ejes, leyenda mínima y una o dos anotaciones.
- Texto breve debajo con qué notar.

## Procedimiento

1. Elige Chart.js, SVG o Canvas.
2. Crea una página o bloque visual sobrio.
3. Usa color solo para distinguir evidencia.
4. Añade anotaciones mínimas.
5. Verifica que no haya filtros, tabs, KPI cards ni navegación.

## Errores a evitar

- Crear dashboard.
- Añadir controles exploratorios.
- Mostrar tablas de datos.
- Usar muchas series sin necesidad.
- Hacer que el diseño sea más importante que la señal.

## Criterios de aceptación

- La visualización se entiende sin interacción.
- La gráfica sostiene la tesis.
- El HTML es autocontenido.
- La composición es sobria y legible.
