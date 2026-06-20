# Caso: Productividad inflada por duplicados

## Tesis del caso

Un KPI de productividad puede mejorar porque se duplicó la unidad de conteo, no porque el proceso atienda más problemas reales. Antes de premiar volumen, hay que saber qué representa una fila.

## Nivel analítico del caso

Nivel 6: calidad de datos. El problema central está en duplicados, granularidad de captura y definición de caso atendido.

## Técnica principal

Perfilamiento de calidad de datos y deduplicación por unidad de problema.

## Técnica mínima suficiente

Comparar tickets cerrados contra problemas únicos cerrados usando reglas simples de deduplicación por cliente, motivo, ventana de tiempo y referencia operativa.

## Por qué no usar una solución más compleja

No hace falta clasificar tickets con NLP ni crear un modelo de productividad. La señal aparece al comparar conteos brutos con conteos únicos.

## Por qué no usar una solución más simple

Contar solo tickets cerrados conserva el incentivo equivocado. Si la unidad de conteo está rota, cualquier promedio o ranking posterior solo ordena ruido con mucha seguridad.

## Resumen ejecutivo

Operativa reporta una mejora de productividad después de integrar dos sistemas de atención. Data revisa datos sintéticos y observa que los tickets cerrados suben, pero los problemas únicos atendidos casi no cambian. La integración está generando tickets duplicados por el mismo problema y el KPI premia cerrar varias filas para un solo caso real.

## Contexto

El equipo de Atención mide productividad por tickets cerrados al día. Tras integrar el sistema de reclamos con el sistema de seguimiento, cada interacción puede crear más de un ticket. Operativa celebra más cierres; los clientes no sienten más resolución.

## Áreas involucradas

- Operativa quiere mostrar productividad y defender capacidad.
- Negocio quiere reducir backlog sin contratar más personal.
- Data sospecha que cambió la granularidad del dato.
- Tecnología explica que la integración crea registros por evento, no por problema.
- Auditoría pide que el KPI represente trabajo real y no artefactos del sistema.

## Evidencia visual

La gráfica central compara tickets cerrados y problemas únicos cerrados antes y después de la integración. Los tickets suben de forma marcada; los problemas únicos apenas se mueven.

## Qué parece a simple vista

Parece una mejora operativa. Se cerraron más tickets, el ranking subió y varias personas respiraron como si eso fuera un control interno.

## Qué está pasando realmente

La integración cambió la unidad de conteo. Un mismo problema de cliente puede generar ticket de reclamo, ticket de seguimiento y ticket de cierre. El KPI mide actividad del sistema, no resolución de problemas.

## Giro después de 3 meses

Data propone deduplicar por problema único. Tres meses después, algunos equipos empiezan a registrar subcasos separados para conservar productividad. La métrica anterior no solo medía mal; entrenó una forma de verse bien.

## Decisión incorrecta de negocio

Se decide excluir únicamente duplicados exactos porque es fácil de explicar y no afecta demasiado el KPI publicado. La solución robusta requería coordinación entre áreas. Por suerte, alguien propuso un Excel temporal que vivirá para siempre.

## Acción robusta desde Data

- Definir una unidad canónica de problema atendido.
- Crear reglas de deduplicación por cliente, motivo, referencia y ventana temporal.
- Reportar tickets, problemas únicos y tasa de duplicidad juntos durante transición.
- Ajustar incentivos para premiar resolución, no filas cerradas.
- Monitorear si aparecen subcasos artificiales después de cambiar la regla.

## Acción débil sin expertise en datos

Eliminar solo tickets con campos idénticos. Es fácil, rápido y deja vivos los duplicados creados por la integración, que casi nunca son idénticos cuando alguien necesita que no lo sean.

## Piloto propuesto

Duración: 4 semanas. Población: tres células operativas con alto volumen y una célula holdout. Métrica principal: problemas únicos resueltos por analista. Métricas de control: tickets cerrados, tasa de duplicidad, recontacto a 7 días y quejas. Criterio de éxito: mantener resolución única sin aumentar recontacto. Criterio de reversa: pausar cambio si el recontacto sube más de 6% o si la deduplicación genera más de 5% de falsos agrupamientos.

## Comentario tragicómico del narrador

La regla funcionó durante tres semanas, que en tiempo corporativo equivale a una era dorada.

## Aprendizajes

- Una fila no siempre representa una unidad de negocio.
- Los cambios de sistema pueden cambiar la métrica sin cambiar el proceso.
- Deduplicar requiere definición operativa, no solo limpieza técnica.
- Un KPI mal definido puede enseñar a producir registros, no resultados.

## Preguntas para el alumno

1. ¿Cuál debería ser la unidad de conteo del KPI?
2. ¿Por qué eliminar duplicados exactos no resuelve el problema?
3. ¿Qué señales indicarían que los equipos se adaptaron a la nueva regla?
4. ¿Cómo comunicarías el cambio sin acusar a Operativa de manipulación?

## Respuesta esperada

El alumno debe distinguir tickets de problemas únicos y proponer una definición de unidad canónica. La acción robusta debe combinar reglas de deduplicación, monitoreo de adaptación y cambio de incentivos. La comunicación debe reconocer que Operativa respondió a la métrica disponible.

## Riesgos éticos / privacidad / sesgo

Los datos del caso son sintéticos. En un entorno real, la deduplicación no debe borrar problemas legítimos de clientes ni castigar analistas por errores de integración. Debe existir revisión muestral y canal para corregir agrupamientos incorrectos.

## Checklist de calidad

- Tesis clara.
- Nivel analítico declarado.
- Técnica mínima suficiente declarada.
- Evidencia visual simple.
- Conflicto corporativo plausible.
- Mala decisión defendible.
- Piloto medible.
- Riesgos tratados.
- HTML simple, sin filtros, sin pestañas.

