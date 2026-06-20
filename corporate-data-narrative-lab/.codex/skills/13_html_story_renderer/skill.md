# 13 HTML Story Renderer

## Cuándo usarla

Úsala cuando el caso markdown ya está aprobado o casi aprobado.

## Qué hace

Renderiza una historia vertical con una evidencia visual central.

## Qué no hace

No construye dashboards, filtros, paneles, pestañas, widgets complejos, navegación innecesaria ni múltiples visualizaciones sin justificación.

## Conexión con las demás skills

Recibe caso desde `06_narrative_case_writer`, evidencia desde `05_simple_visual_builder` y restricciones desde `14_quality_gatekeeper`.

## Cuándo detenerse y pedir revisión

Detente si el HTML empieza a parecer una herramienta de BI, si necesita interacción para entenderse o si omite contexto, interpretación, giro, acciones, piloto, humor discreto o preguntas.

## Entradas necesarias

- Caso markdown.
- Especificación visual.
- Datos agregados o sintéticos.
- Título y subtítulo.

## Salida esperada

Página HTML vertical con:

- Título.
- Subtítulo.
- Nivel analítico.
- Técnica principal.
- Contexto breve.
- Visualización central.
- Qué parece.
- Qué revela.
- Giro.
- Acción robusta.
- Acción débil.
- Decisión de negocio.
- Piloto.
- Comentario tragicómico.
- Preguntas.
- Respuesta esperada.

## Procedimiento

1. Usa HTML autocontenido.
2. Usa CSS interno.
3. Usa JS interno solo si hace falta.
4. Renderiza una visualización central.
5. Mantén diseño sobrio.
6. No agregues navegación ni componentes de dashboard.

## Errores a evitar

- Filtros.
- Tabs.
- KPI cards.
- Navegación compleja.
- Varias gráficas no justificadas.
- Layout ejecutivo.

## Criterios de aceptación

- El HTML se abre localmente.
- La página se lee verticalmente.
- La gráfica está integrada como evidencia.
- No hay dashboard.
