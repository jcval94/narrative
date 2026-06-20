# Caso: Movimientos pequeños e incentivos

## Tesis del caso

Una regla de negocio mal diseñada no solo mide el comportamiento: lo crea. Si una cuenta se considera activada por cualquier movimiento, el incentivo aprende a producir movimientos mínimos.

## Nivel analítico del caso

Nivel 14: interpretabilidad. El caso empieza con una distribución simple, pero la solución robusta requiere convertir señales tempranas en una definición comportamental entendible.

## Técnica principal

Modelo supervisado interpretable para estimar activación legítima durante los primeros 60 días, acompañado de reglas derivadas de señales estables.

## Técnica mínima suficiente

Histograma de movimientos entre -10 y 10 pesos para detectar el patrón inicial, seguido de un modelo interpretable solo si la organización va a rediseñar la definición de activación.

## Por qué no usar una solución más compleja

No hace falta iniciar con un sistema antifraude completo. Primero hay que demostrar que el incentivo está creando un comportamiento anómalo y que una regla fija se puede evadir.

## Por qué no usar una solución más simple

Una alerta por monto menor a 1 peso solo detecta la forma actual del problema. Si alguien transfiere 1.01 pesos o usa otro banco, la alerta queda convertida en instructivo.

## Resumen ejecutivo

La empresa paga incentivos por cuentas nuevas que tuvieron al menos un movimiento. Data revisa datos sintéticos de movimientos pequeños y encuentra una concentración inusual de salidas cercanas a -1 peso desde cuentas de empleados. La lectura superficial es que son montos irrelevantes. La lectura correcta es que la regla de activación es manipulable.

## Contexto

Comercial celebra un aumento de cuentas activadas. Operativa no reporta incidentes relevantes porque los montos son pequeños. Data revisa movimientos entre -10 y 10 pesos porque el incentivo depende de que exista cualquier actividad inicial.

## Áreas involucradas

- Negocio quiere mantener el ritmo de activación y evitar rediseñar incentivos a mitad de trimestre.
- Data ve un patrón que no se explica por comportamiento natural de clientes.
- Operativa no quiere revisar miles de movimientos pequeños sin priorización.
- Riesgos teme sanciones injustas si la señal se usa sin revisión humana.
- Auditoría necesita una definición que pueda explicarse y versionarse.

## Evidencia visual

La gráfica central es un histograma de movimientos pequeños. Las entradas y salidas se parecen en casi todo el rango, excepto por una concentración de salidas entre -2.04 y -0.71 pesos.

## Qué parece a simple vista

Parecen movimientos menores, probablemente ruido de clientes que prueban la cuenta con montos bajos. La pérdida económica directa es casi invisible.

## Qué está pasando realmente

La distribución sugiere que algunos empleados están enviando montos mínimos a cuentas nuevas para activar la regla de incentivo. El problema no es el peso transferido; es la definición de activación.

## Giro después de 3 meses

Se activa una alerta sobre salidas pequeñas desde cuentas de empleados. Tres meses después, esas salidas desaparecen. Ahora aparecen entradas pequeñas a cuentas nuevas desde otros bancos. La conducta no terminó; cambió de carril.

## Decisión incorrecta de negocio

Negocio propone mantener el incentivo y bloquear solo transferencias menores a 1 peso desde cuentas de empleados. Es rápido, auditable y se puede explicar en una diapositiva. También deja intacta la mecánica que generó el problema.

## Acción robusta desde Data

- Redefinir cuenta activada con comportamiento legítimo durante los primeros 60 días.
- Comparar cuentas incentivadas contra cuentas orgánicas.
- Usar señales como hora del primer movimiento, origen del dinero, monto, repetición por empleado, sucursal y relación empleado-cliente.
- Entrenar un modelo supervisado interpretable.
- Traducir coeficientes, reglas de árbol o SHAP values a criterios operativos.
- Monitorear drift y desplazamiento de origen del dinero.
- Separar señal analítica de decisión disciplinaria.

## Acción débil sin expertise en datos

Dejar una alerta si se transfiere algo menor a 1 peso desde una cuenta de empleado. Funciona perfecto siempre que nadie lo piense demasiado, especialmente quien quiere evadirla.

## Piloto propuesto

Duración: 8 semanas. Población: cuentas nuevas de 30 sucursales con alta activación reciente y 10 sucursales holdout. Métrica principal: proporción de cuentas con actividad legítima a 60 días. Métricas secundarias: concentración por empleado, origen del primer fondeo, reclamos de clientes y falsos positivos revisados. Reversa: volver a definición anterior si la activación legítima cae más de 8% sin reducción de patrones sospechosos.

## Comentario tragicómico del narrador

La alerta detectó el fraude. El fraude detectó la alerta. Ganó el que tuvo menos juntas.

## Aprendizajes

- Un incentivo mal definido puede crear el comportamiento que pretende medir.
- Una distribución simple puede revelar una manipulación antes que un modelo.
- Un modelo puede ser útil si termina en una definición operativa interpretable.
- Una regla fija sin monitoreo se vuelve manual de evasión.

## Preguntas para el alumno

1. ¿Por qué el monto pequeño no vuelve irrelevante el problema?
2. ¿Qué señales agregarías para distinguir activación legítima de activación inducida?
3. ¿Por qué la alerta menor a 1 peso falla después de tres meses?
4. ¿Qué métrica usarías para decidir si el piloto debe continuar?

## Respuesta esperada

El alumno debe identificar que la anomalía no prueba culpabilidad individual, pero sí evidencia una definición manipulable. La solución debe rediseñar la activación alrededor de comportamiento legítimo, usar señales múltiples, mantener revisión humana y monitorear adaptación.

## Riesgos éticos / privacidad / sesgo

Los datos del ejemplo son sintéticos. En un caso real, la señal no debe usarse para sancionar automáticamente empleados. Debe abrir revisión de definición, auditoría muestral y derecho de respuesta. También se debe evitar vigilancia laboral excesiva y revisar si ciertas sucursales quedan sobrerrepresentadas por mezcla de clientes.

## Checklist de calidad

- Tesis clara.
- Nivel analítico explícito.
- Técnica mínima suficiente declarada.
- Evidencia simple.
- Giro plausible.
- Mala decisión defendible.
- Acción robusta interpretable.
- Piloto medible.
- Riesgos éticos tratados.
- HTML simple, sin filtros, sin pestañas.
