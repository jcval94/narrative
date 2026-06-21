# Caso: La cola que no cabía en el promedio

<!-- suspense_spine
format: junta de guardia con recibos
cold_open: El promedio mejora y una llamada lleva seis horas esperando.
setting: Guardia nocturna del centro de atención.
moment: Lunes 21:18, después del cierre del comité.
protagonist: Celia de Calidad revisa el recibo de espera 0098.
opposing_forces: Comité necesita un número simple; Guardia necesita explicar la cola crítica.
recurring_object: El recibo 0098 que sigue imprimiendo minutos.
motif: cola
pressure: La meta mensual se aprobó usando tiempo promedio.
comfortable_explanation: La nueva priorización acelera a la mayoría y mejora servicio.
first_anomaly: Media baja de 18 a 14 minutos mientras el percentil 95 sube de 52 a 121.
false_lead: Unos pocos casos extremos podrían ser incidentes inevitables.
visual_evidence: Distribución concentra casos rápidos y alarga una cola roja a la derecha.
reader_question: Qué métrica defiende a clientes más afectados.
analytical_twist: El promedio mejora porque muchos casos simples son rápidos mientras la cola crítica empeora.
consequence: Los casos complejos envejecen detrás de una meta verde.
weak_decision: Mantener promedio y revisar extremos manualmente.
robust_decision: Publicar mediana y percentiles con alerta de antigüedad crítica.
tragicomic_payoff: El recibo 0098 termina más largo que la diapositiva que decía mejora.
transferable_rule: Cuando el daño vive en la cola, el promedio llega tarde.
final_image: Un recibo atraviesa la mesa del comité y llega al turno nocturno.
analytic_level: 3
minimum_sufficient_technique: Media, mediana y percentiles p90/p95 sobre distribución.
pilot: Cuatro semanas con guardas de cola y comparación de resolución y reapertura.
risks: No sacrificar la mayoría ni usar percentiles sin tamaño de muestra.
synthetic_data: true
worker_context: Guardia operaba con menos personal y recibía los casos que el turno diurno no cerraba.
corporate_pressure: El comité pidió una sola cifra verde para el cierre mensual.
reasonable_shortcut: El promedio resumió miles de atenciones en un número comparable.
absurd_validation: La mejora promedio se premió reduciendo una posición nocturna.
systemic_critique: La organización convirtió eficiencia de casos fáciles en permiso para adelgazar la guardia difícil.
time_jump: Dos meses después, la cola extrema se duplicó y el promedio siguió verde.
institutional_defense: No se podía añadir otra métrica porque la plantilla ejecutiva tenía una cifra por proceso.
human_cost: Clientes críticos y el turno nocturno absorbieron la variabilidad excluida.
blame_target: governance
satirical_payoff: El recibo más largo obtuvo finalmente el espacio que no cabía en la plantilla.
-->

<!-- suspense:cold-open -->
## Guardia 21:18 — recibo 0098

> "Catorce minutos promedio. Buen cierre", escribió el comité antes de desconectarse.

> "El 0098 lleva seis horas", respondió Celia. "Promedia muy bien con los que tardaron dos."

<!-- satire:pressure -->
La plantilla ejecutiva permitía una cifra por proceso. Guardia tenía menos personal, más casos heredados y una meta aprobada antes de que empezara su turno.

<!-- satire:shortcut -->
Usar el promedio era razonable: resumía miles de atenciones y permitía comparar meses. Nadie prometió que describiría a cada cliente; sí terminaron usándolo para decidir capacidad.

<!-- satire:validation -->
El promedio bajó. La eficiencia fue reconocida retirando una posición nocturna y distribuyendo su carga entre quienes habían demostrado compromiso.

<!-- suspense:false-lead -->
## Unos pocos recibos largos

La mayoría sí estaba mejor. La nueva ruta resolvía consultas simples en minutos y reducía esperas comunes. Los extremos podían ser incidentes raros, dependencias externas o casos que ninguna dotación razonable resolvería rápido. Celia no quería frenar una mejora amplia por una excepción ruidosa.

> "No diseñemos toda la operación alrededor del peor día", pidió Planeación.

<!-- satire:time-jump -->
Dos meses después, el promedio seguía en verde. La **cola** superior había duplicado su longitud y Guardia coleccionaba recibos que ya incluían cambio de fecha.

<!-- suspense:humor -->
El recibo 0098 solicitó orientación horizontal para caber en la junta.

<!-- suspense:evidence -->
## La distribución sobre la mesa

Data llevó una curva de tiempos. Había más atenciones entre 2 y 8 minutos, pero una cola roja se extendía mucho más allá de 120. La tabla lateral mostraba media 14, mediana 7, p90 38 y p95 121. El promedio había mejorado; el cinco por ciento peor, no.

<!-- suspense:reader-question -->
<!-- learning:question correct="C" -->
> Si tuvieras que defender a los clientes más afectados, ¿qué mostrarías?
> A. Solo la media de 14 minutos.
> B. Solo el caso 0098 como anécdota.
> C. Mediana, p90, p95 y volumen de casos en la cola.
<!-- learning:answer -->
**C.** Describe experiencia típica y extremos sin convertir un caso en toda la población. A y B eran tentadoras por síntesis o dramatismo, pero una oculta la cola y la otra no dimensiona. **Regla:** acompaña el centro con percentiles cuando el riesgo vive en extremos.
<!-- learning:end -->

<!-- suspense:reveal -->
## Mejora para casi todos

La priorización aceleró muchos casos simples y dejó a los complejos esperando más. La media combinó ambas poblaciones y permitió que una gran cantidad de minutos pequeños tapara una cola crítica creciente.

<!-- suspense:technique -->
Primero se ordenaron los tiempos y se preguntó cuánto espera la mitad, nueve de cada diez y diecinueve de cada veinte. Después llegaron los nombres: **mediana, percentil 90 y percentil 95**. Junto con la media, bastaban para ver el intercambio.

<!-- suspense:decision -->
## La guardia que faltaba en la lámina

Revisar extremos manualmente conservaba la plantilla y reaccionaba tarde. La salida robusta publicaba media, mediana, p90, p95 y antigüedad crítica, y probaba cuatro semanas de cobertura específica sin degradar la mayoría.

<!-- satire:institutional-defense -->
Planeación recordó que la lámina aceptaba una sola cifra. Celia propuso usar el largo del recibo como unidad tipográfica.

<!-- learning:question correct="B" -->
> ¿Qué decisión responde a la forma de la distribución?
> A. Optimizar únicamente la media.
> B. Establecer guardas para p95 y antigüedad, manteniendo seguimiento del centro.
> C. Atender siempre el caso más viejo sin considerar severidad.
<!-- learning:answer -->
**B.** Protege la cola sin abandonar la experiencia mayoritaria. A y C eran tentadoras porque simplifican objetivo o priorización, pero una oculta daño y la otra puede desplazar urgencias. **Regla:** diseña límites para la cola y metas para el centro.
<!-- learning:end -->

<!-- suspense:payoff -->
## El recibo entra al comité

El 0098 se resolvió y su recibo atravesó la mesa completa. La siguiente plantilla aceptó cuatro cifras. La **cola** por fin cupo, aunque el archivo ejecutivo pidió una diapositiva adicional y abrió un comité para reducir diapositivas.

**Regla que queda:** cuando el daño vive en la cola, el promedio llega tarde.
