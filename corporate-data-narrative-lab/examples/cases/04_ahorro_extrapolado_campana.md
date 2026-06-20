# Caso: El ahorro extrapolado que no cabía en la realidad

## Tesis del caso

Una regla de 3 puede ser suficiente para desmontar una mala decisión si el problema real está en la población elegible. El error no estaba en multiplicar; estaba en multiplicar por quien no podía recibir el beneficio.

## Nivel analítico del caso

Nivel 0: aritmética de negocio. El caso se resuelve con proporciones, población elegible y una comparación simple entre impacto presentado e impacto realista.

## Técnica principal

Regla de 3 con población elegible y tasa de adopción realista.

## Técnica mínima suficiente

Separar universo total, clientes elegibles, clientes contactables y adopción esperada. Después, calcular el ahorro solo sobre la población donde la campaña podía operar.

## Por qué no usar una solución más compleja

No hace falta un modelo de propensión ni segmentación avanzada. El error ocurre antes: el denominador usado en la estimación incluye clientes que no eran elegibles, no tenían permiso de contacto o ya usaban el canal digital.

## Por qué no usar una solución más simple

Tomar el ahorro promedio del piloto y multiplicarlo por toda la base ignora elegibilidad, contacto y adopción. La cuenta se ve limpia, pero limpia como presentación, no como realidad.

## Resumen ejecutivo

Negocio presenta una campaña de migración digital con ahorro esperado de 18 millones de pesos al año. Data revisa el cálculo y encuentra que el ahorro del piloto fue multiplicado por toda la base de clientes, aunque solo 28% era elegible y apenas 14% podía ser contactado sin restricciones. La visualización muestra que la mayor parte del ahorro vive en una población que la campaña nunca podía tocar.

## Contexto

El área de Canales Digitales hizo un piloto con clientes que todavía llamaban al centro de atención para operaciones simples. En el piloto, quienes migraron al canal digital redujeron llamadas y generaron un ahorro operativo promedio. La cifra se llevó a comité como si aplicara a todos los clientes activos.

## Áreas involucradas

- Negocio quiere justificar presupuesto para escalar la campaña.
- Data observa que el denominador del cálculo mezcla clientes elegibles y no elegibles.
- Operativa espera reducción de llamadas, pero teme que la meta sea inalcanzable.
- Legal recuerda que parte de la base no puede contactarse por consentimiento.
- Finanzas necesita distinguir ahorro bruto prometido de ahorro capturable.

## Evidencia visual

La gráfica central compara tres montos: ahorro presentado en comité, ahorro si se usa solo población elegible y ahorro capturable considerando contacto y adopción. La caída no requiere modelado; requiere no confundir universo con mercado accionable.

## Qué parece a simple vista

Parece una oportunidad grande y rápida. Si cada cliente migrado ahorra dinero, multiplicar por toda la base suena eficiente, que es como se llama a la esperanza cuando viene en Excel.

## Qué está pasando realmente

El piloto medía un subconjunto muy específico. Al extrapolar a toda la base, la estimación incluyó clientes que no tenían llamadas que reducir, clientes ya digitales y clientes que no podían ser contactados. La multiplicación era correcta. La realidad, lamentablemente, no estaba copiada en Excel.

## Giro después de 3 meses

La campaña se escala con una meta de ahorro basada en el cálculo inflado. Tres meses después, el contacto efectivo es menor al esperado y Operativa sigue viendo volumen de llamadas. El comité pide "optimizar creatividades", aunque el problema estaba en el denominador desde el primer día.

## Decisión incorrecta de negocio

Se decide mantener la meta original porque ya fue presentada en comité y ajustar el mensaje de campaña. Es una decisión cómoda: no obliga a corregir el business case ni a explicar que el ahorro aprobado no era capturable.

## Acción robusta desde Data

- Recalcular el ahorro con embudo explícito: universo, elegibles, contactables, interesados, adoptantes y reducción real de llamadas.
- Separar ahorro bruto, ahorro capturable y ahorro observado.
- Publicar una versión comparable del business case con supuestos.
- Diseñar seguimiento mensual de adopción y reducción de llamadas por cohorte.
- Comunicar a Finanzas un rango de ahorro, no un número único con traje ejecutivo.

## Acción débil sin expertise en datos

Mantener el ahorro de 18 millones y explicar la desviación como problema de ejecución de campaña. Es rápido, conserva la narrativa y convierte una cuenta mal planteada en una meta operativa injusta.

## Piloto propuesto

Duración: 6 semanas. Población: clientes elegibles, contactables y con historial de llamadas reducibles. Grupo comparador: clientes elegibles no contactados durante el periodo. Métrica principal: reducción neta de llamadas por cliente elegible contactado. Métricas de control: tasa de contacto, adopción digital, reclamos y costo de campaña. Criterio de éxito: ahorro neto observado dentro de 15% del rango recalculado. Criterio de reversa: detener escalamiento si la reducción neta queda por debajo de 50% del supuesto mínimo.

## Comentario tragicómico del narrador

Detectaste correctamente el problema, así que naturalmente fuiste recompensado con más trabajo. Eso te pasa por eficiente.

## Aprendizajes

- El denominador correcto puede importar más que una técnica avanzada.
- Un piloto no se extrapola a poblaciones que no comparten condiciones.
- La regla de 3 es poderosa cuando se usa sobre la base correcta.
- La comunicación a negocio debe separar oportunidad total de oportunidad accionable.

## Preguntas para el alumno

1. ¿Qué población debe usarse para estimar el ahorro capturable?
2. ¿Por qué un modelo de propensión sería sobreingeniería en este caso?
3. ¿Qué supuestos deberían aparecer explícitamente en el business case?
4. ¿Cómo explicarías a Finanzas la diferencia entre ahorro presentado y ahorro observable?

## Respuesta esperada

El alumno debe identificar que el problema central es el denominador. La solución robusta usa aritmética simple con población elegible, contactabilidad y adopción esperada. También debe proponer un piloto que mida reducción neta, no solo envíos o clics.

## Riesgos éticos / privacidad / sesgo

Los datos del caso son sintéticos. En un caso real, la campaña debe respetar consentimientos de contacto y no presionar a clientes que requieren canales asistidos por accesibilidad, edad, idioma o vulnerabilidad.

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

