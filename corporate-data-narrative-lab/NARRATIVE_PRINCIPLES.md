# Narrative Principles

Este repositorio no crea dashboards. Crea narrativas con evidencia visual.

La técnica mínima suficiente manda. No uses modelos si una tasa resuelve el caso. No uses una tasa si el comportamiento se adapta y requiere monitoreo.

## Intriga Antes Que Contexto

Un caso no debe abrir con "contexto breve". Debe abrir con una escena, contradicción, anomalía o pregunta incómoda que haga querer mirar la evidencia.

Buenos inicios:

- "A las 9:03, el tablero se puso verde. Nadie sabía por qué."
- "El comité celebró una mejora que Operativa todavía no había sentido."
- "La métrica bajó justo el día en que nadie cambió el proceso."

El título tampoco debe revelar por completo el truco analítico. Debe prometer una tensión, no entregar la moraleja.

El primer pantallazo debe provocar curiosidad extrema: alguien mira una señal y sospecha que la historia oficial no alcanza.

## Caso Como Investigación

Cada caso debe funcionar como una investigación mínima. No es un informe donde el autor explica todo desde arriba; es una secuencia donde el alumno descubre qué mirar y por qué una conclusión cómoda puede ser peligrosa.

La estructura episódica recomendada es:

1. Escena inicial.
2. Sospecha.
3. Evidencia visual.
4. Hipótesis.
5. Giro analítico.
6. Consecuencia de negocio.
7. Decisión cómoda pero peligrosa.
8. Acción robusta.
9. Cierre tragicómico.
10. Regla transferible.

## Estudiante Como Investigador

El alumno no debe quedar como lector pasivo. El caso debe hacerle preguntas activas:

- ¿Qué pasó?
- ¿Qué mirarías primero?
- ¿Qué conclusión sería peligrosa?
- ¿Qué dato falta?
- ¿Qué hipótesis explica mejor la gráfica?
- ¿Qué decisión cómoda te tentaría y por qué sería insuficiente?

El narrador puede guiar, pero no debe resolver todo antes de que el alumno tenga que interpretar una pista.

## Tensión Antes De Técnica

Un caso funciona cuando hay una decisión real en juego. Antes de elegir una gráfica, define:

- qué quiere Negocio;
- qué ve Data;
- qué necesita Operativa;
- qué limita Tecnología;
- qué teme Riesgos, Auditoría o Legal;
- qué decisión cómoda parece razonable;
- qué solución robusta exige más coordinación.

La tensión no debe caricaturizar a nadie. Un área puede proponer una mala decisión por presión, capacidad limitada, urgencia, incentivos, restricciones de plataforma o falta de ownership.

## Segunda Capa

Cada caso debe tener una lectura superficial y una lectura correcta.

Ejemplo:

- Superficial: el KPI mejoró.
- Correcta: cambió el denominador y ahora mide una población más fácil.

La segunda capa es el corazón didáctico. Si el caso solo confirma lo obvio, todavía no es un caso.

En el Narrative Learning Experience Standard, esta segunda capa se escribe como tensión entre:

- `official_story`: la explicación cómoda que suena razonable;
- `hidden_story`: lo que la evidencia visual obliga a considerar.

## La Gráfica Como Evidencia

La gráfica debe responder una pregunta narrativa:

> ¿Qué tendría que ver el alumno en una sola imagen para sospechar que la historia oficial no alcanza?

La gráfica no tiene que permitir exploración. Tiene que hacer visible una señal:

- un pico raro;
- una cola sospechosa;
- una caída después de una redefinición;
- una similitud entre categorías que deberían comportarse distinto;
- una diferencia de cohortes;
- una ventana temporal que censura el fenómeno.

La gráfica debe estar subordinada al arco narrativo. Si la visualización se vuelve el producto principal, el caso perdió identidad.

Trata la visualización como escena del crimen:

- debe contener una pista visual;
- debe contrastar lo que parece con lo que realmente pasa;
- debe incluir una guía de lectura o anotación breve;
- debe mostrar por qué una conclusión fácil no alcanza;
- debe llegar en el momento narrativo donde el alumno necesita evidencia.

## Lenguaje Humano Antes Que Jerga

Todo término técnico debe pasar por traducción humana. Primero explica la idea en palabras de negocio; después nombra el término si hace falta.

Ejemplos:

- SLA -> casos resueltos a tiempo.
- Denominador -> el grupo de casos que sí cuenta.
- Uplift -> mejora adicional atribuible a la acción.
- Drift -> cuando el comportamiento de los datos cambia con el tiempo.
- Cohorte -> grupo comparable de casos o clientes.
- Umbral -> línea de corte para decidir.
- Ventana temporal -> periodo observado.
- Incrementalidad -> mejora que no habría ocurrido sin la intervención.

Regla: primero lenguaje humano, después término técnico.

## Cierre Didáctico

El cierre debe convertir el caso en criterio transferible:

- cómo leer una métrica;
- cómo cuestionar una definición;
- cómo distinguir síntoma de causa;
- cómo diseñar un piloto;
- cómo proponer una acción robusta sin sobreactuar;
- cómo comunicar riesgo sin sonar alarmista.

Cada cierre debe incluir:

- una consecuencia cómica o tragicómica;
- una regla práctica;
- una pregunta de transferencia.

Ejemplo de regla: "Antes de creerle a un KPI, pregúntale si sigue midiendo lo mismo."

## Evitar Casos Genéricos

Un caso genérico suele tener estas señales:

- no hay dueño del problema;
- la mala decisión es absurda en vez de plausible;
- la gráfica podría pertenecer a cualquier empresa;
- no hay giro;
- el aprendizaje es una frase obvia;
- la solución robusta es una lista de buenas prácticas sin conexión con la evidencia.

Un buen caso deja al alumno pensando: "esto sí podría pasar en una empresa el martes a las 11:30".
