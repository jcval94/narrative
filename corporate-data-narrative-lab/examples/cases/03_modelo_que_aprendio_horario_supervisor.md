# Caso: La IA que llegaba después del incidente

<!-- suspense_spine
format: postmortem de modelo
cold_open: Un modelo presume 97% y una ingeniera pregunta por qué la variable estrella aparece después de la revisión.
setting: Reunión de aprobación de IA operativa.
moment: Jueves 19:26, la demo ejecutiva es a primera hora.
protagonist: Abril de Data reconstruye el reloj de las variables.
opposing_forces: Innovación necesita una demo brillante; Operación necesita una alerta disponible antes del incidente.
recurring_object: El reloj de disponibilidad de datos.
motif: reloj
pressure: La solución debe llamarse IA en la presentación de las 08:00.
comfortable_explanation: La precisión confirma que el modelo encontró señales operativas profundas.
first_anomaly: La variable más importante se carga tras la revisión manual.
false_lead: El supervisor podría registrar una señal temprana durante el proceso.
visual_evidence: Línea de tiempo coloca evaluación_supervisor después del incidente y antes del corte de entrenamiento.
reader_question: Qué variable no existía cuando debía tomarse la decisión.
analytical_twist: El modelo aprendió la conclusión humana ya emitida.
consequence: La validación parece perfecta y la producción queda sin su mejor predictor.
weak_decision: Desplegar y sustituir la variable faltante por cero.
robust_decision: Rehacer el corte temporal y entrenar solo con datos disponibles al decidir.
tragicomic_payoff: El reloj recibe crédito como el único componente que predijo correctamente cuándo sabía el modelo.
transferable_rule: Un modelo no debe saber el futuro, aunque en validación se vea brillante.
final_image: La variable estrella queda detrás de una línea roja llamada momento de decisión.
analytic_level: 18
minimum_sufficient_technique: Auditoría temporal de variables y reentrenamiento sin datos posteriores.
pilot: Validación retrospectiva con cortes reales y despliegue sombra de cuatro semanas.
risks: No automatizar sanciones, documentar disponibilidad y revisar degradación por turno.
synthetic_data: true
worker_context: Data recibió un extracto ya consolidado y una noche para convertirlo en demo.
corporate_pressure: Innovación había vendido una precisión superior a 95% antes de revisar el origen de columnas.
reasonable_shortcut: Entrenar con la tabla final redujo integración y permitió demostrar viabilidad.
absurd_validation: El 97% fue bautizado como inteligencia enterprise y el equipo recibió otra demo.
systemic_critique: La organización compró una respuesta antes de preguntar en qué momento existía la información.
time_jump: Cuatro meses después, el modelo seguía en piloto porque producción no podía fabricar el futuro.
institutional_defense: La variable no podía retirarse porque aparecía como principal hallazgo de consultoría.
human_cost: Operación recibió alertas tardías y Data heredó la defensa de una promesa ajena.
blame_target: governance
satirical_payoff: El reloj, ausente del alcance inicial, terminó siendo el revisor más importante del modelo.
-->

<!-- suspense:cold-open -->
## POSTMORTEM IA-97

> "Noventa y siete por ciento. ¿Le ponemos predictivo o cognitivo?", preguntó Innovación.

> "Primero pongámosle hora", respondió Abril. "¿Cuándo aparece `evaluación_supervisor`?"

<!-- satire:pressure -->
Eran las 19:26. La demo era a las ocho y la promesa de superar 95% ya vivía en una diapositiva ejecutiva. Data había recibido una tabla final, limpia y sin historia de cuándo nacía cada columna.

<!-- satire:shortcut -->
Entrenar sobre esa tabla era razonable para explorar viabilidad. Evitaba cuatro integraciones y permitía comprobar si había señal. El problema fue que la exploración recibió logo, nombre enterprise y fecha de despliegue antes de recibir un reloj.

<!-- satire:validation -->
El 97% fue declarado victoria de IA. Abril obtuvo visibilidad y la oportunidad de preparar otra demo para el lunes.

<!-- suspense:false-lead -->
## Una señal demasiado buena

Quizá el supervisor registraba observaciones durante el turno y la columna contenía pistas tempranas: orden, carga, desviaciones visibles. Una evaluación humana podía condensar experiencia útil. Quitarla sin investigar también era peligroso; podía desechar la señal que hacía accionable al modelo.

> "El experto conoce la operación. El modelo solo aprendió de él", defendió Consultoría.

<!-- satire:time-jump -->
Cuatro meses después, el piloto seguía esperando integración. Producción entregaba la columna a las 18:00; la alerta debía salir a las 14:00. El calendario lo llamaba retraso técnico. El **reloj** lo llamaba imposibilidad.

<!-- suspense:humor -->
La IA podía anticipar el incidente con cuatro horas de anticipación siempre que alguien se lo hubiera confirmado cuatro horas después.

<!-- suspense:evidence -->
## El minuto que partió el modelo

Data dibujó una línea: 13:40 señales operativas, 14:00 decisión, 14:25 incidente, 17:30 revisión, 18:00 carga de `evaluación_supervisor`. Una línea roja en las 14:00 separaba lo conocible de lo futuro. La variable estrella quedó del lado equivocado.

<!-- suspense:reader-question -->
<!-- learning:question correct="C" -->
> ¿Qué variable no podía existir al momento de decidir?
> A. Carga acumulada hasta las 13:40.
> B. Turno y tipo de operación conocidos al inicio.
> C. Evaluación del supervisor cargada a las 18:00.
<!-- learning:answer -->
**C.** La línea de tiempo la ubica después de decisión, incidente y revisión. A y B eran tentadoras para sospechar correlaciones operativas, pero sí estaban disponibles. **Regla:** cada predictor necesita una hora de nacimiento anterior a la decisión.
<!-- learning:end -->

<!-- suspense:reveal -->
## La conclusión disfrazada de predictor

El modelo no había descubierto riesgo oculto. Había aprendido el dictamen posterior del supervisor. Durante validación veía una respuesta que producción todavía no tenía; por eso parecía extraordinario y por eso no podía funcionar igual en vivo.

<!-- suspense:technique -->
Primero se preguntó qué sabía el sistema a las 14:00. Después se nombró la falla: **fuga de información**, o leakage. La solución mínima era fechar disponibilidad, reconstruir cada fila como se veía al decidir y reentrenar sin variables posteriores.

<!-- suspense:decision -->
## Acción correctiva 3.2

Sustituir la variable faltante por cero conservaba la fecha de demo y destruía el comportamiento aprendido. La salida robusta rehacía el corte temporal, comparaba desempeño sin futuro y ejecutaba cuatro semanas en sombra antes de usar alertas.

<!-- satire:institutional-defense -->
Consultoría recordó que `evaluación_supervisor` era el principal hallazgo del modelo. Abril respondió que también era el principal hallazgo del supervisor, solo que varias horas antes y con sueldo distinto.

<!-- learning:question correct="B" -->
> ¿Qué validación representa mejor la producción?
> A. Dividir al azar la tabla final completa.
> B. Reconstruir cada caso con variables disponibles antes de las 14:00 y separar periodos posteriores.
> C. Mantener la variable y ocultarla en la explicación ejecutiva.
<!-- learning:answer -->
**B.** Simula la información y el orden temporal reales. A y C eran tentadoras porque preservan precisión o fecha de entrega, pero permiten que el futuro contamine el entrenamiento. **Regla:** valida desde el momento de decisión, no desde la comodidad de la tabla final.
<!-- learning:end -->

<!-- suspense:payoff -->
## El único predictor puntual

La nueva versión bajó a 71% y por primera vez pudo correr a las 14:00. En la portada, el **reloj** apareció como control obligatorio. No recibió nombre de IA, presupuesto ni visibilidad; solo evitó que el futuro volviera a entrar por la puerta de servicio.

**Regla que queda:** un modelo no debe saber el futuro, aunque en validación se vea brillante.
