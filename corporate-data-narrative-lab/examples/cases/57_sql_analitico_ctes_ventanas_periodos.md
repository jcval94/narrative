# La metrica que olvidaba el mes anterior

<!-- story
concept: SQL analitico con CTEs, ventanas y metricas por periodo
characters: Elena, Uriel, Rosa, el director
situation: SQL y Datos se enseña mediante una decision practica que necesita codigo o datos bien definidos
bad_logic: calcular cada periodo aislado basta para explicar movimiento
escalation: el reporte muestra valores mensuales pero no variacion ni acumulados
data_turn: una persona compara el atajo contra una version verificable
chart: metrica mensual con y sin ventana
decision: usar CTEs para ordenar pasos y ventanas para comparar periodos
punchline: La metrica tenia memoria de pez, pero en formato corporativo.
rule: las ventanas permiten comparar una fila con su historia sin perder detalle
synthetic_data: true
-->

## El mes solito

> **Elena:** "El reporte ya trae ventas por mes."

> **Uriel:** "Pero no dice si subieron contra el mes anterior."

> **Rosa:** "Eso se calcula mirando la tabla."

> **Elena:** "La consulta deberia mirarla por nosotros."

> **Rosa:** "No queria complicarla."

> **el director:** "Ahora la decision depende de restar a mano."

La clase no se atoro por falta de ganas. Se atoro porque una idea razonable se
habia quedado a medio camino entre conversacion y procedimiento. En la mesa ya
habia prisa, capturas abiertas y alguien diciendo que lo importante era avanzar.
Por eso el error parecia pequeno: no rompia la historia completa, solo la parte
donde la maquina tenia que entender exactamente que hacer.

## La historia quedo fuera

> **Rosa:** "Hacemos otra consulta para variacion."

> **Uriel:** "Mejor una ventana en la misma historia."

> **Rosa:** "La consulta se va a sentir muy larga."

> **el director:** "Larga con pasos claros gana a corta con misterio."

> **Rosa:** "Podemos dejar comentarios."

> **Elena:** "Una CTE tambien comenta con estructura."

> **Uriel:** "Entonces el atajo si hizo trabajo, solo que no el trabajo correcto."

> **el director:** "Quiero ver donde se separa la intuicion del resultado."

La solucion comoda tenia una virtud: se podia explicar en una frase. El problema
era que tambien escondia entradas, reglas y excepciones. Cuando el grupo la
siguio dos pasos mas, aparecio lo de siempre: una salida que parecia formal, una
persona intentando defenderla y otra buscando el dato exacto donde la historia
dejaba de sostenerse.

## CTE para respirar

> **Elena:** "Reescribi la consulta en pasos y agregue LAG."

> **el director:** "Que aparece al comparar periodos."

> **Elena:** "Se ve la variacion sin perder el valor mensual."

> **Uriel:** "Eso cambia lo que tenemos que enseñar."

> **Elena:** "Si. Primero la regla humana, luego la forma tecnica."

<svg data-chart="central" viewBox="0 0 720 320" role="img" aria-label="metrica mensual con y sin ventana">
  <rect width="720" height="320" fill="#fff"/>
  <text x="36" y="32" font-size="18" font-weight="bold">metrica mensual con y sin ventana</text>
  <line x1="58" y1="260" x2="662" y2="260" stroke="#777" stroke-width="2"/>
  <rect x="70" y="155" width="174" height="105" fill="#286d9b"/>
  <text x="157" y="145" font-size="18" text-anchor="middle">55</text>
  <text x="157" y="286" font-size="13" text-anchor="middle">mensual</text>
  <rect x="272" y="95" width="174" height="165" fill="#d58b2f"/>
  <text x="359" y="85" font-size="18" text-anchor="middle">86</text>
  <text x="359" y="286" font-size="13" text-anchor="middle">con LAG</text>
  <rect x="474" y="85" width="174" height="175" fill="#4c8b63"/>
  <text x="561" y="75" font-size="18" text-anchor="middle">91</text>
  <text x="561" y="286" font-size="13" text-anchor="middle">acumulado</text>
  <text x="36" y="306" font-size="13" fill="#9f3625">La ventana agrega contexto temporal.</text>
</svg>

<!-- learning:pause -->
> **Uriel:** "Para que sirven CTEs y funciones de ventana en una metrica por periodo."

**Lo que muestra:** La evidencia compara un resumen mensual aislado con una metrica que recuerda periodos anteriores. Las CTEs hacen legibles los pasos; las ventanas calculan comparaciones como LAG, acumulados o rankings sin colapsar filas.

## La ventana mira atras

> **el director:** "El reporte incluira variacion y acumulado por ventana."

> **Rosa:** "La consulta tendra mas estructura."

> **Elena:** "Y menos calculadora al lado."

> **Rosa:** "Y si alguien quiere saltarse ese paso."

> **Elena:** "Que primero explique que evidencia esta dispuesto a perder."

> **Uriel:** "La metrica tenia memoria de pez, pero en formato corporativo."

**Regla:** las ventanas permiten comparar una fila con su historia sin perder detalle.
