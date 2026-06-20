# Data Visual Evidence Guide

## Evidencia, No Dashboard

Una visualización en este proyecto no sirve para explorar todo. Sirve para sostener una afirmación narrativa. Debe hacer visible una señal incómoda con el menor número posible de elementos.

Si necesitas filtros, pestañas, múltiples KPIs o varias vistas sincronizadas, probablemente dejaste de crear evidencia y empezaste a crear un dashboard.

Este repositorio no crea dashboards. Crea narrativas con evidencia visual.

La técnica mínima suficiente manda. No uses modelos si una tasa resuelve el caso. No uses una tasa si el comportamiento se adapta y requiere monitoreo.

La pregunta central siempre es:

> ¿Qué tendría que ver el alumno en una sola imagen para sospechar que la historia oficial no alcanza?

## Elegir La Gráfica Mínima

Usa la gráfica más simple que revele el patrón:

- barra simple para proporciones o conteos;
- línea antes/después para cambios temporales;
- histograma para distribuciones, colas y picos raros;
- boxplot simple para extremos ocultos por promedios;
- matriz pequeña para errores de clasificación;
- scatter simple para relación entre monto, tiempo o severidad;
- grafo SVG solo cuando las relaciones sean la historia.

## Anotaciones

Cada visualización debe tener:

- título claro;
- ejes legibles;
- leyenda mínima si hay más de una serie;
- 1 o 2 anotaciones que orienten la lectura;
- texto breve debajo: "qué debería notar el alumno".

No expliques toda la historia dentro de la gráfica. La gráfica apunta; la narrativa interpreta.

## Función Narrativa De La Gráfica

Antes de renderizar, declara qué papel juega la gráfica en la historia:

- `visual_clue`: la pista que debe activar sospecha;
- `official_story`: la lectura superficial;
- `hidden_story`: la lectura correcta;
- `student_question`: la pregunta que el alumno debe responder mirando la imagen;
- `guided_reading`: los pasos mínimos para leer la señal;
- `decision_risk`: qué decisión peligrosa saldría de mirar mal la gráfica.

Una gráfica buena no solo se entiende. Cambia la decisión.

## Elementos Visuales Permitidos

Más visual no significa dashboard. Está permitido usar elementos que ayuden a interpretar una sola evidencia:

- anotaciones sobre la gráfica;
- callouts con pistas;
- mini cálculos que expliquen una comparación;
- bloques "lo que parece / lo que realmente pasa";
- glosarios visuales para definiciones técnicas;
- líneas de corte, umbrales o ventanas marcadas;
- pequeñas escenas narrativas alrededor de la evidencia;
- preguntas interactivas mínimas sin exploración libre;
- tarjetas narrativas que expliquen pista, hipótesis, riesgo o regla.

Una tarjeta narrativa está permitida si forma parte de la historia o del aprendizaje. Está prohibida si funciona como KPI card de monitoreo, ranking ejecutivo, panel de desempeño o resumen de BI.

## Evitar Sobrevisualización

Evita:

- paneles de métricas;
- navegación;
- filtros;
- drilldowns;
- herramientas self-service;
- widgets complejos;
- tablas exploratorias;
- mapas si la geografía no es la historia;
- colores decorativos sin significado;
- más de dos visualizaciones sin justificación explícita.

También evita:

- tarjetas con números grandes que imitan monitoreo ejecutivo;
- bloques visuales que compiten con la pista central;
- múltiples "vistas" del mismo fenómeno sin una pregunta narrativa nueva;
- interacciones que permitan explorar sin guía;
- decorar la página para que parezca producto.

## HTML Simple

Los HTML de ejemplo deben ser:

- autocontenidos;
- verticales;
- sobrios;
- sin dependencias locales;
- con CSS interno;
- con JS interno solo si hace falta;
- legibles en navegador sin build step.

Chart.js desde CDN es aceptable para ejemplos educativos. SVG inline también es aceptable cuando la gráfica es pequeña.
