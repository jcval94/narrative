# Data Visual Evidence Guide

## Evidencia, No Dashboard

Una visualización en este proyecto no sirve para explorar todo. Sirve para sostener una afirmación narrativa. Debe hacer visible una señal incómoda con el menor número posible de elementos.

Si necesitas filtros, pestañas, múltiples KPIs o varias vistas sincronizadas, probablemente dejaste de crear evidencia y empezaste a crear un dashboard.

Este repositorio no crea dashboards. Crea narrativas con evidencia visual.

La técnica mínima suficiente manda. No uses modelos si una tasa resuelve el caso. No uses una tasa si el comportamiento se adapta y requiere monitoreo.

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
