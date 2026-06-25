# La calculadora de diamantes que prometio castillos

<!-- story
concept: mini reto narrativo con calculadora de recursos en Minecraft
characters: Axel, Nora, Tavo, la moderadora
situation: Programacion en Python se enseña mediante una decision practica que necesita codigo o datos bien definidos
bad_logic: multiplicar recursos por construcciones basta aunque falten recetas y limites
escalation: la calculadora promete materiales imposibles y el equipo planea una base que no puede construir
data_turn: una persona compara el atajo contra una version verificable
chart: recursos estimados contra recursos necesarios
decision: crear una funcion que calcule recursos por receta y avise faltantes
punchline: La calculadora no construyo el castillo; solo nos cobro la fantasia en bloques.
rule: un reto de programacion debe transformar reglas del juego en calculos verificables
synthetic_data: true
-->

## La base imposible

> **Axel:** "La calculadora dice que nos alcanza para el castillo."

> **Nora:** "Tambien dice que una antorcha cuesta diamantes."

> **Tavo:** "Eso fue por simplificar recursos."

> **Axel:** "Simplificar no significa inventar recetas."

> **Tavo:** "El reto era practicar codigo, no arquitectura."

> **la moderadora:** "Justo por eso necesitamos reglas claras."

La clase no se atoro por falta de ganas. Se atoro porque una idea razonable se
habia quedado a medio camino entre conversacion y procedimiento. En la mesa ya
habia prisa, capturas abiertas y alguien diciendo que lo importante era avanzar.
Por eso el error parecia pequeno: no rompia la historia completa, solo la parte
donde la maquina tenia que entender exactamente que hacer.

## El inventario tenia limites

> **Tavo:** "Multiplicamos bloques por pisos y ya."

> **Nora:** "Faltan recetas, cofres y herramientas."

> **Tavo:** "Podemos asumir inventario infinito."

> **la moderadora:** "Entonces no es Minecraft, es presupuesto publico."

> **Tavo:** "La fantasia se ve motivadora."

> **Axel:** "La frustracion tambien ensena, pero prefiero evitarla."

> **Nora:** "Entonces el atajo si hizo trabajo, solo que no el trabajo correcto."

> **la moderadora:** "Quiero ver donde se separa la intuicion del resultado."

La solucion comoda tenia una virtud: se podia explicar en una frase. El problema
era que tambien escondia entradas, reglas y excepciones. Cuando el grupo la
siguio dos pasos mas, aparecio lo de siempre: una salida que parecia formal, una
persona intentando defenderla y otra buscando el dato exacto donde la historia
dejaba de sostenerse.

## Receta antes que promesa

> **Axel:** "Compare estimacion simple contra calculo por receta."

> **la moderadora:** "Donde aparecen los faltantes."

> **Axel:** "Cuando cada construccion consume ingredientes reales."

> **Nora:** "Eso cambia lo que tenemos que enseñar."

> **Axel:** "Si. Primero la regla humana, luego la forma tecnica."

<svg data-chart="central" viewBox="0 0 720 320" role="img" aria-label="recursos estimados contra recursos necesarios">
  <rect width="720" height="320" fill="#fff"/>
  <text x="36" y="32" font-size="18" font-weight="bold">recursos estimados contra recursos necesarios</text>
  <line x1="58" y1="260" x2="662" y2="260" stroke="#777" stroke-width="2"/>
  <rect x="70" y="101" width="174" height="159" fill="#286d9b"/>
  <text x="157" y="91" font-size="18" text-anchor="middle">84</text>
  <text x="157" y="286" font-size="13" text-anchor="middle">estimado</text>
  <rect x="272" y="171" width="174" height="89" fill="#d58b2f"/>
  <text x="359" y="161" font-size="18" text-anchor="middle">47</text>
  <text x="359" y="286" font-size="13" text-anchor="middle">real</text>
  <rect x="474" y="85" width="174" height="175" fill="#4c8b63"/>
  <text x="561" y="75" font-size="18" text-anchor="middle">92</text>
  <text x="561" y="286" font-size="13" text-anchor="middle">con faltantes</text>
  <text x="36" y="306" font-size="13" fill="#9f3625">La receta evita promesas imposibles.</text>
</svg>

<!-- learning:pause -->
> **Nora:** "Que entradas y salidas necesita una calculadora de recursos para ser util."

**Lo que muestra:** La grafica muestra que el reto no es solo sumar bloques. La calculadora necesita inventario, recetas, cantidad deseada y faltantes. Programar el juego obliga a convertir reglas narrativas en funciones verificables.

## Construir con numeros honestos

> **la moderadora:** "El mini reto usara recetas y avisos de faltantes."

> **Tavo:** "El castillo sera mas pequeno."

> **Axel:** "Pero se podra construir sin magia contable."

> **Tavo:** "Y si alguien quiere saltarse ese paso."

> **Axel:** "Que primero explique que evidencia esta dispuesto a perder."

> **Nora:** "La calculadora no construyo el castillo; solo nos cobro la fantasia en bloques."

**Regla:** un reto de programacion debe transformar reglas del juego en calculos verificables.
