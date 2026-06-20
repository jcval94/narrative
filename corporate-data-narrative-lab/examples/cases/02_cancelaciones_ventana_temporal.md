# Caso: Cancelaciones y ventana temporal

## Tesis del caso

Recortar datos para ajustarlos a una limitación de plataforma no arregla el problema. Solo vuelve invisible la evidencia.

## Nivel analítico del caso

Nivel 5: ventanas temporales. El problema central es maduración del fenómeno y censura por herramienta operativa.

## Técnica principal

Análisis de distribución temporal por motivo de cancelación.

## Técnica mínima suficiente

Línea temporal por mes desde apertura para mostrar que algunos motivos aparecen principalmente después del mes 6.

## Por qué no usar una solución más compleja

No hace falta un modelo de predicción de cancelación para demostrar que una ventana de 3 meses no observa el fenómeno completo.

## Por qué no usar una solución más simple

Contar cancelaciones totales en los últimos 3 meses refuerza la limitación de la herramienta y borra la maduración del problema.

## Resumen ejecutivo

La operativa solo puede consultar tres meses de historia en su herramienta. Data envía 24 meses de cancelaciones con datos sintéticos para análisis educativo. Negocio recibe quejas y pide acotar los envíos. La evidencia muestra que "Economía Personal" y "Mala Venta" aparecen tarde y tienen curvas temporales parecidas.

## Contexto

El equipo operativo revisa pólizas canceladas, pero la herramienta solo muestra tres meses. Data entrega histórico completo porque algunos motivos tardan en manifestarse. La tensión aparece cuando el dato correcto no cabe en la plataforma disponible.

## Áreas involucradas

- Negocio quiere bajar quejas de Operativa y mantener avance.
- Operativa necesita consultar casos sin abrir archivos externos.
- Data ve que el recorte destruye el análisis.
- Tecnología no puede ampliar la herramienta en el trimestre.
- Tipificaciones no tiene ownership claro para revisar motivos ambiguos.

## Evidencia visual

La gráfica central muestra cancelaciones por mes desde apertura. Los motivos "Economía Personal" y "Mala Venta" crecen después del mes 6 y se mueven con formas muy parecidas.

## Qué parece a simple vista

Si la herramienta solo permite tres meses, parece razonable enviar solo casos recientes. Menos fricción, menos quejas y menos archivos dando vueltas.

## Qué está pasando realmente

La limitación de plataforma está redefiniendo qué fenómeno puede ver la organización. Al recortar historia, se elimina la zona donde aparecen los motivos más relevantes.

## Giro después de 3 meses

Negocio acepta un piloto de seis meses, pero solo para pólizas recientes. La carga operativa baja y el reporte se ve más limpio. Tres meses después, la efectividad de detección de mala venta cae porque los casos maduros ya no entran. El problema no desapareció; solo quedó fuera de cuadro.

## Decisión incorrecta de negocio

Se decide acotar a seis meses y posponer la conversación con Tipificaciones porque nadie conoce al dueño exacto. La decisión es cómoda: reduce quejas sin pedir cambio de plataforma. También deja sin resolver la causa.

## Acción robusta desde Data

- Mantener 24 meses para análisis.
- Crear una página HTML táctica y simple para consulta operativa completa.
- No construir un dashboard complejo.
- Revisar si "Economía Personal" y "Mala Venta" requieren multitipificación.
- Medir efectividad antes y después del recorte.
- Documentar limitación de plataforma como riesgo de decisión.

## Acción débil sin expertise en datos

Enviar solo lo que la herramienta puede mostrar. El dashboard no mentía; solo omitía los 21 meses donde estaba el problema. Técnicamente no es mentira, es una presentación ejecutiva.

## Piloto propuesto

Duración: 1 mes. Población: cancelaciones enviadas a Operativa con versión completa de 24 meses y versión acotada a 6 meses. Grupo comparador: motivos revisados en el esquema histórico anterior. Métrica principal: efectividad de casos confirmados de mala venta. Métricas secundarias: tiempo de consulta, quejas operativas, porcentaje de casos sin motivo claro. Reversa: regresar a 24 meses si la efectividad cae más de 10%.

## Comentario tragicómico del narrador

Negocio pidió una solución simple. Data explicó una solución correcta. Se eligió una tercera opción: simple, incompleta y con piloto para que doliera en cámara lenta.

## Aprendizajes

- Una ventana temporal puede censurar el fenómeno real.
- La plataforma no debe definir la verdad analítica.
- Motivos similares pueden indicar problema de tipificación.
- Una solución táctica simple puede ser mejor que recortar datos.

## Preguntas para el alumno

1. ¿Qué se pierde al limitar el análisis a tres meses?
2. ¿Por qué la similitud entre "Economía Personal" y "Mala Venta" importa?
3. ¿Qué medirías para decidir si el piloto de seis meses falla?
4. ¿Qué solución táctica propondrías sin construir un dashboard?

## Respuesta esperada

El alumno debe concluir que el problema central es censura temporal. La acción robusta conserva el histórico, da a Operativa una consulta simple y mide si el recorte reduce efectividad. También debe proponer revisión de tipificaciones sin convertirla en un proyecto interminable.

## Riesgos éticos / privacidad / sesgo

Los datos del caso son sintéticos. En datos reales se debe evitar exponer información sensible de clientes y revisar que el recorte no excluya sistemáticamente productos o segmentos con maduración más lenta.

## Checklist de calidad

- Tesis clara.
- Nivel analítico explícito.
- Técnica mínima suficiente declarada.
- Evidencia temporal simple.
- Giro plausible.
- Mala decisión defendible.
- Acción robusta táctica.
- Piloto medible.
- Riesgos tratados.
- HTML simple, sin filtros, sin pestañas.
