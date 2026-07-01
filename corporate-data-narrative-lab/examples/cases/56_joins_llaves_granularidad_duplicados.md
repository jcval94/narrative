# El JOIN que duplico las ventas con mucha seguridad

<!-- story
concept: JOINs, llaves, granularidad y duplicados
characters: Hana, Pedro, Lucia, la directora
situation: SQL y Datos se enseña mediante una decision practica que necesita codigo o datos bien definidos
bad_logic: si dos tablas comparten una columna, se pueden unir sin revisar granularidad
escalation: ventas se multiplican porque promociones tiene varias filas por producto
data_turn: una persona compara el atajo contra una version verificable
chart: ventas antes y despues del join
decision: identificar llave, granularidad y duplicados antes de unir
punchline: El JOIN no vendio mas; nada mas conto la misma venta con entusiasmo.
rule: antes de unir tablas, revisa llave unica, granularidad y filas duplicadas
synthetic_data: true
-->

## El total subio solo

> **Hana:** "Despues del JOIN las ventas crecieron precioso."

> **Pedro:** "Sin campana y sin clientes nuevos."

> **Lucia:** "Tal vez el producto mejoro."

> **Hana:** "O la tabla se multiplico."

> **Lucia:** "Uni por product_id, eso era la llave."

> **la directora:** "En promociones product_id aparece varias veces."

La clase no se atoro por falta de ganas. Se atoro porque una idea razonable se
habia quedado a medio camino entre conversacion y procedimiento. En la mesa ya
habia prisa, capturas abiertas y alguien diciendo que lo importante era avanzar.
Por eso el error parecia pequeno: no rompia la historia completa, solo la parte
donde la maquina tenia que entender exactamente que hacer.

## La union tenia eco

> **Lucia:** "Usamos DISTINCT al final."

> **Pedro:** "Eso puede borrar sintomas sin arreglar causa."

> **Lucia:** "Pero DISTINCT suena a limpieza elegante."

> **la directora:** "Elegante no significa correcto."

> **Lucia:** "El total nuevo le gustaba a direccion."

> **Hana:** "A contabilidad le va a gustar menos."

> **Pedro:** "Entonces el atajo si hizo trabajo, solo que no el trabajo correcto."

> **la directora:** "Quiero ver donde se separa la intuicion del resultado."

La solucion comoda tenia una virtud: se podia explicar en una frase. El problema
era que tambien escondia entradas, reglas y excepciones. Cuando el grupo la
siguio dos pasos mas, aparecio lo de siempre: una salida que parecia formal, una
persona intentando defenderla y otra buscando el dato exacto donde la historia
dejaba de sostenerse.

## Una fila contra muchas

> **Hana:** "Revise filas por llave antes de unir."

> **la directora:** "Donde se duplicaron las ventas."

> **Hana:** "Cada venta se repitio por cada promocion del producto."

> **Pedro:** "Eso cambia lo que tenemos que enseñar."

> **Hana:** "Si. Primero la regla humana, luego la forma tecnica."

<svg data-chart="central" viewBox="0 0 720 320" role="img" aria-label="ventas antes y despues del join">
  <rect width="720" height="320" fill="#fff"/>
  <text x="36" y="32" font-size="18" font-weight="bold">ventas antes y despues del join</text>
  <line x1="58" y1="260" x2="662" y2="260" stroke="#777" stroke-width="2"/>
  <rect x="70" y="173" width="174" height="87" fill="#286d9b"/>
  <text x="157" y="163" font-size="18" text-anchor="middle">74</text>
  <text x="157" y="286" font-size="13" text-anchor="middle">antes</text>
  <rect x="272" y="85" width="174" height="175" fill="#d58b2f"/>
  <text x="359" y="75" font-size="18" text-anchor="middle">148</text>
  <text x="359" y="286" font-size="13" text-anchor="middle">join bruto</text>
  <rect x="474" y="171" width="174" height="89" fill="#4c8b63"/>
  <text x="561" y="161" font-size="18" text-anchor="middle">76</text>
  <text x="561" y="286" font-size="13" text-anchor="middle">join correcto</text>
  <text x="36" y="306" font-size="13" fill="#9f3625">La duplicacion venia de granularidad distinta.</text>
</svg>

<!-- learning:pause -->
> **Pedro:** "Que debes revisar antes de hacer un JOIN entre dos tablas."

**Lo que muestra:** La grafica muestra que el JOIN cambio la granularidad. Una tabla estaba a nivel venta y otra a nivel producto promocion. Revisar llaves unicas, cardinalidad y duplicados evita inflar metricas con una union aparentemente valida.

## La llave pide identificacion

> **la directora:** "Agregaremos promociones antes de unirlas a ventas."

> **Lucia:** "La consulta tendra una CTE mas."

> **Hana:** "Y las ventas dejaran de reproducirse."

> **Lucia:** "Y si alguien quiere saltarse ese paso."

> **Hana:** "Que primero explique que evidencia esta dispuesto a perder."

> **Pedro:** "El JOIN no vendio mas; nada mas conto la misma venta con entusiasmo."

**Regla:** antes de unir tablas, revisa llave unica, granularidad y filas duplicadas.
