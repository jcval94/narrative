# 13 HTML Story Renderer

## Cuándo usarla

Úsala cuando el caso markdown ya está aprobado o casi aprobado.

## Qué hace

Renderiza una investigación narrativa vertical con una evidencia visual central.

## Qué no hace

No construye dashboards, filtros, paneles, pestañas, widgets complejos, navegación innecesaria, KPI cards de monitoreo ni múltiples visualizaciones sin justificación. Puede usar tarjetas narrativas si enseñan pista, contraste, mini cálculo, glosario visual, pregunta o regla.

## Conexión con las demás skills

Recibe caso desde `06_narrative_case_writer`, evidencia desde `05_simple_visual_builder` y restricciones desde `14_quality_gatekeeper`.

## Cuándo detenerse y pedir revisión

Detente si el HTML empieza a parecer una herramienta de BI, si necesita interacción para entenderse o si omite intriga, rol del alumno, misterio, pista visual, pregunta activa, interpretación, giro, acciones, piloto, cierre tragicómico o regla transferible.

## Entradas necesarias

- Caso markdown.
- Especificación visual.
- Datos agregados o sintéticos.
- Título intrigante.
- `opening_hook`.
- `protagonist_or_student_role`.
- `central_mystery`.
- `visual_clue`.
- `student_question`.
- `transferable_rule`.

## Salida esperada

Página HTML vertical con:

- Título.
- Opening hook.
- Rol del alumno.
- Misterio central.
- Nivel analítico.
- Técnica principal.
- Visualización central.
- Pista visual.
- Lectura guiada.
- Qué parece.
- Qué revela.
- Pregunta activa.
- Traducción de jerga.
- Giro.
- Acción robusta.
- Acción débil.
- Decisión de negocio.
- Piloto.
- Cierre tragicómico.
- Regla transferible.
- Pregunta de transferencia.
- Respuesta esperada.

## Procedimiento

1. Usa HTML autocontenido.
2. Usa CSS interno.
3. Usa JS interno solo si hace falta.
4. Renderiza una visualización central.
5. Abre con intriga, no con contexto breve.
6. Usa tarjetas narrativas solo para pista, comparación, mini cálculo, glosario o regla.
7. Mantén diseño sobrio.
8. No agregues navegación ni componentes de dashboard.

## Errores a evitar

- Filtros.
- Tabs.
- KPI cards.
- Navegación compleja.
- Varias gráficas no justificadas.
- Layout ejecutivo.
- Hero decorativo sin evidencia.
- Tarjetas de monitoreo que parezcan BI.
- Texto largo sin guía visual.

## Criterios de aceptación

- El HTML se abre localmente.
- La página se lee verticalmente.
- La gráfica está integrada como evidencia.
- El primer pantallazo genera curiosidad.
- El alumno tiene una pregunta activa.
- El cierre incluye regla transferible.
- No hay dashboard.
