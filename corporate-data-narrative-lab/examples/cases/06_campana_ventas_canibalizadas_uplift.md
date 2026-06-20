# Caso: La campaña que vendía a quienes ya iban a comprar

## Tesis del caso

Una campaña puede aumentar ventas brutas y aun así aportar poco valor incremental. La pregunta correcta no es quién compró, sino quién compró por la campaña.

## Nivel analítico del caso

Nivel 20: uplift e incrementalidad. El reto es separar conversión observada de impacto causal aproximado mediante control.

## Técnica principal

Medición de incrementalidad con grupo control y lectura simple de uplift por segmento.

## Técnica mínima suficiente

Comparar tasa de compra en tratamiento contra control para segmentos de alta y media propensión. No hace falta un modelo de uplift completo si el control ya muestra que las ventas iban a ocurrir.

## Por qué no usar una solución más compleja

Un modelo de uplift avanzado puede esperar. La primera decisión es evitar escalar una campaña cuyo lift básico es bajo en el segmento que concentra presupuesto.

## Por qué no usar una solución más simple

Mirar solo ventas brutas confunde impacto con selección. Si se contacta a clientes que ya iban a comprar, la campaña parece exitosa mientras gasta presupuesto en convencer a los convencidos.

## Resumen ejecutivo

Marketing reporta que una campaña de renovación vendió 31% en clientes de alta propensión. Data compara contra un grupo control sintético y encuentra que ese mismo segmento compraba 29% sin contacto. El lift real es bajo. En clientes de propensión media, la venta bruta es menor, pero el incremento es mayor. La campaña estaba optimizando comodidad comercial, no impacto.

## Contexto

La campaña prioriza clientes con mayor probabilidad de compra porque eso mejora resultados visibles. Ventas celebra conversión alta. Finanzas pregunta por retorno. Data revisa control y descubre canibalización: muchas ventas atribuidas habrían ocurrido sin campaña.

## Áreas involucradas

- Marketing quiere mostrar ventas rápidas y defender presupuesto.
- Ventas prefiere leads fáciles de cerrar.
- Data ve que la tasa bruta no mide incrementalidad.
- Finanzas quiere retorno neto de descuentos y contactos.
- Experiencia de Cliente teme saturar a clientes que ya tenían intención de renovar.

## Evidencia visual

La gráfica central compara conversión de tratamiento y control por segmento. En alta propensión, la diferencia es pequeña. En propensión media, la tasa absoluta es menor, pero el lift es más valioso.

## Qué parece a simple vista

Parece que la campaña funciona mejor donde la conversión es más alta. El ranking de ventas brutas favorece al segmento fácil, que siempre llega a la junta con buen peinado.

## Qué está pasando realmente

La campaña se atribuye compras que habrían ocurrido de todos modos. El impacto incremental está en otro segmento, menos espectacular en tasa bruta pero más útil para decidir presupuesto.

## Giro después de 3 meses

Se escala la campaña al segmento de alta propensión porque "convierte mejor". Tres meses después, el costo por venta incremental sube, aumentan quejas por sobrecontacto y las ventas totales apenas cambian. La campaña vendía mucho; el problema es que vendía lo que ya estaba vendido.

## Decisión incorrecta de negocio

Negocio decide mantener el ranking por conversión bruta porque es fácil de explicar y ya fue presentado como caso de éxito. Escalar una campaña sin control porque las ventas brutas subieron tiene una ventaja: la gráfica se ve optimista hasta que llega Finanzas.

## Acción robusta desde Data

- Mantener grupo control por segmento.
- Reportar ventas brutas, ventas incrementales y costo por venta incremental.
- Reasignar presupuesto hacia segmentos persuadibles.
- Limitar frecuencia de contacto en alta propensión.
- Medir saturación, quejas y canibalización.
- Usar modelo de uplift solo cuando el diseño experimental básico esté estable.

## Acción débil sin expertise en datos

Ordenar clientes por propensión y contactar a los de arriba. Es cómodo, eleva conversión visible y confunde al equipo lo suficiente como para llamar estrategia a la selección.

## Piloto propuesto

Duración: 8 semanas. Población: clientes elegibles de alta, media y baja propensión. Grupo control: 15% holdout aleatorio por segmento. Métrica principal: ventas incrementales por 1,000 contactos. Métricas de control: costo por venta incremental, quejas, tasa de baja de comunicaciones y renovación orgánica. Criterio de éxito: lift positivo con costo incremental menor al margen esperado. Criterio de reversa: detener segmento si el lift es menor a 1 punto porcentual o si quejas superan 4%.

## Comentario tragicómico del narrador

La campaña convirtió a clientes que ya estaban convertidos. En términos espirituales es precioso; en términos financieros, menos.

## Aprendizajes

- Conversión bruta no equivale a incrementalidad.
- Un grupo control simple puede cambiar una decisión de presupuesto.
- El mejor segmento por ventas puede no ser el mejor segmento por impacto.
- La técnica avanzada debe esperar hasta que la medición básica sea correcta.

## Preguntas para el alumno

1. ¿Por qué la tasa de compra del tratamiento no basta para evaluar la campaña?
2. ¿Qué segmento debería recibir más presupuesto y por qué?
3. ¿Qué métrica usarías para evitar canibalización?
4. ¿Cuándo tendría sentido pasar de comparación con control a modelo de uplift?

## Respuesta esperada

El alumno debe priorizar incrementalidad sobre ventas brutas. La solución robusta mantiene holdout por segmento, mide costo por venta incremental y reasigna presupuesto hacia clientes persuadibles, sin sobreactuar con un modelo avanzado antes de tener medición confiable.

## Riesgos éticos / privacidad / sesgo

Los datos del caso son sintéticos. En un entorno real, la campaña debe respetar consentimiento, frecuencia de contacto y posibles efectos de saturación. También debe revisarse si la optimización excluye sistemáticamente segmentos menos rentables pero estratégicamente relevantes.

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

