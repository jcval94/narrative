# Caso: El KPI que mejoró por definición

## Tesis del caso

Un KPI puede mejorar porque cambió la definición, no porque mejoró el proceso. Cuando el denominador se vuelve más fácil, la celebración necesita auditoría.

## Nivel analítico del caso

Nivel 23: gobernanza analítica, con base en nivel 2 de ratios y KPIs.

## Técnica principal

Versionado de definición, comparación de denominadores y métrica comparable antes/después.

## Técnica mínima suficiente

Línea temporal del KPI publicado contra KPI comparable con definición anterior.

## Por qué no usar una solución más compleja

No hace falta predecir cumplimiento de SLA. La pregunta es si el indicador mide la misma población antes y después del cambio.

## Por qué no usar una solución más simple

Mirar solo el KPI publicado acepta una mejora aparente sin revisar qué casos salieron del denominador.

## Resumen ejecutivo

El KPI de atención en tiempo sube de forma repentina después de excluir casos complejos de la medición. Negocio propone llevar la mejora a comité. Data reconstruye la serie comparable y muestra que el proceso no cambió de manera sustantiva; cambió la población medida.

## Contexto

El área de atención recibe presión por mejorar cumplimiento de SLA. Para hacer el indicador más "comparable", se excluyen casos que requieren dictamen de otra área. El reporte mensual mejora de inmediato y todos respiran, que es una métrica no oficial pero muy monitoreada.

## Áreas involucradas

- Negocio quiere mostrar avance después de dos trimestres difíciles.
- Atención necesita un KPI que no la castigue por dependencias externas.
- Data ve que la serie dejó de ser comparable.
- Auditoría necesita saber qué definición llegó al comité.
- Tecnología solo replica la regla vigente en el reporte.

## Evidencia visual

La gráfica central compara el KPI publicado con una reconstrucción comparable. El KPI publicado salta después del cambio de definición; la serie comparable apenas se mueve.

## Qué parece a simple vista

Parece que el proceso mejoró. La línea publicada sube, el comité recibe una buena noticia y el documento tiene color verde suficiente para dormir con tranquilidad.

## Qué está pasando realmente

La definición v2 excluye casos complejos. El numerador mejora porque el denominador dejó fuera la parte difícil. La métrica publicada ya no responde la misma pregunta que respondía antes.

## Giro después de 3 meses

Tres meses después, las áreas excluidas acumulan rezago. El KPI de atención sigue verde, pero las quejas por casos complejos suben. El indicador no mintió: solo cambió de tema sin avisar con suficiente letra.

## Decisión incorrecta de negocio

Se decide celebrar la mejora y llevarla a comité como evidencia de estabilización. La nota de cambio queda en un anexo. La definición estaba en el Excel definitivo, versión final, final ahora sí.

## Acción robusta desde Data

- Versionar definiciones de KPI.
- Publicar KPI oficial y KPI comparable durante transición.
- Auditar exclusiones por volumen, motivo y área responsable.
- Mantener ownership de cada regla.
- Crear nota metodológica breve para comité.
- Medir rezago de casos excluidos como métrica de riesgo.

## Acción débil sin expertise en datos

Mantener la nueva definición porque se ve mejor y reduce discusiones. El proceso no mejoró; solo dejó de invitar a los casos difíciles.

## Piloto propuesto

Duración: 3 ciclos mensuales. Población: todos los casos de atención, con marca de incluido/excluido. Grupo comparador: KPI recalculado con definición v1. Métrica principal: diferencia entre KPI publicado y comparable. Métricas secundarias: volumen excluido, antigüedad de casos complejos, quejas y cumplimiento por área dependiente. Reversa: pausar publicación como mejora si la brecha supera 7 puntos o si el rezago excluido crece más de 12%.

## Comentario tragicómico del narrador

El KPI subió en el momento exacto en que dejó de mirar la parte complicada. Hay procesos que no mejoran: encuentran iluminación favorable.

## Aprendizajes

- Un KPI sin definición versionada puede contar una historia falsa.
- Las exclusiones no son detalles técnicos; son decisiones de negocio.
- Una serie comparable protege la interpretación.
- Gobernanza mínima puede evitar celebraciones prematuras.

## Preguntas para el alumno

1. ¿Por qué el salto del KPI no basta para concluir mejora?
2. ¿Qué denominador compararías antes y después?
3. ¿Qué métrica de riesgo vigilarías para los casos excluidos?
4. ¿Cómo presentarías esto a comité sin destruir la confianza en el indicador?

## Respuesta esperada

El alumno debe distinguir KPI publicado de KPI comparable. La solución robusta no exige cancelar la nueva definición, pero sí versionarla, mostrar el impacto de exclusiones, medir rezago y evitar presentar una mejora metodológica como mejora operativa.

## Riesgos éticos / privacidad / sesgo

Los datos del caso son sintéticos. En un entorno real, excluir casos complejos puede invisibilizar clientes con necesidades más difíciles o procesos que requieren apoyo humano. La revisión debe separar medición operativa de calidad real de atención.

## Checklist de calidad

- Tesis clara.
- Nivel analítico explícito.
- Técnica mínima suficiente declarada.
- Evidencia antes/después.
- Giro plausible.
- Mala decisión defendible.
- Acción robusta de gobernanza.
- Piloto medible.
- Riesgos tratados.
- HTML simple, sin filtros, sin pestañas.
