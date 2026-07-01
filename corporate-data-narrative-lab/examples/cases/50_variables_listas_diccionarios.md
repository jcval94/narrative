# La lista que no sabia de quien era cada dato

<!-- story
concept: variables, listas, diccionarios y estructuras esenciales
characters: Rita, Samuel, Caro, el mentor
situation: Programacion en Python se enseña mediante una decision practica que necesita codigo o datos bien definidos
bad_logic: guardar datos en cualquier orden basta mientras el numero se vea bien
escalation: los nombres, cantidades y costos se mezclan y nadie puede explicar el resultado
data_turn: una persona compara el atajo contra una version verificable
chart: estructura de datos contra errores de lectura
decision: usar variables para valores, listas para colecciones y diccionarios para datos con nombre
punchline: La lista no estaba desordenada; estaba pidiendo identificacion oficial.
rule: elige la estructura segun como necesitas guardar y recuperar el dato
synthetic_data: true
-->

## Todo en una fila

> **Rita:** "Guarde nombres, costos y cantidades en una sola lista."

> **Samuel:** "Entonces el orden se volvio tu base de datos."

> **Caro:** "Mientras no movamos nada, funciona."

> **Rita:** "Eso no es estructura, es supersticion."

> **Caro:** "El total sale correcto en mi ejemplo."

> **el mentor:** "Hasta que agregas otro producto y se recorre todo."

La clase no se atoro por falta de ganas. Se atoro porque una idea razonable se
habia quedado a medio camino entre conversacion y procedimiento. En la mesa ya
habia prisa, capturas abiertas y alguien diciendo que lo importante era avanzar.
Por eso el error parecia pequeno: no rompia la historia completa, solo la parte
donde la maquina tenia que entender exactamente que hacer.

## El dato sin apellido

> **Caro:** "Ponemos comentarios entre valores."

> **Samuel:** "Los comentarios no viajan con el dato."

> **Caro:** "Entonces hacemos una lista bonita con separadores."

> **el mentor:** "Bonita no significa consultable."

> **Caro:** "Al menos se ve compacta."

> **Rita:** "Compacta para romperse en silencio."

> **Samuel:** "Entonces el atajo si hizo trabajo, solo que no el trabajo correcto."

> **el mentor:** "Quiero ver donde se separa la intuicion del resultado."

La solucion comoda tenia una virtud: se podia explicar en una frase. El problema
era que tambien escondia entradas, reglas y excepciones. Cuando el grupo la
siguio dos pasos mas, aparecio lo de siempre: una salida que parecia formal, una
persona intentando defenderla y otra buscando el dato exacto donde la historia
dejaba de sostenerse.

## Cada cosa en su contenedor

> **Rita:** "Probe la misma informacion en variables, listas y diccionarios."

> **el mentor:** "Cual estructura reduce errores."

> **Rita:** "El diccionario ayuda cuando cada valor necesita nombre."

> **Samuel:** "Eso cambia lo que tenemos que enseñar."

> **Rita:** "Si. Primero la regla humana, luego la forma tecnica."

<svg data-chart="central" viewBox="0 0 720 320" role="img" aria-label="estructura de datos contra errores de lectura">
  <rect width="720" height="320" fill="#fff"/>
  <text x="36" y="32" font-size="18" font-weight="bold">estructura de datos contra errores de lectura</text>
  <line x1="58" y1="260" x2="662" y2="260" stroke="#777" stroke-width="2"/>
  <rect x="70" y="178" width="174" height="82" fill="#286d9b"/>
  <text x="157" y="168" font-size="18" text-anchor="middle">44</text>
  <text x="157" y="286" font-size="13" text-anchor="middle">lista suelta</text>
  <rect x="272" y="144" width="174" height="116" fill="#d58b2f"/>
  <text x="359" y="134" font-size="18" text-anchor="middle">62</text>
  <text x="359" y="286" font-size="13" text-anchor="middle">variables</text>
  <rect x="474" y="85" width="174" height="175" fill="#4c8b63"/>
  <text x="561" y="75" font-size="18" text-anchor="middle">93</text>
  <text x="561" y="286" font-size="13" text-anchor="middle">diccionario</text>
  <text x="36" y="306" font-size="13" fill="#9f3625">Nombrar campos reduce errores de lectura.</text>
</svg>

<!-- learning:pause -->
> **Samuel:** "Cuando conviene usar una variable, una lista o un diccionario."

**Lo que muestra:** La grafica compara contenedores. Una variable guarda un valor, una lista agrupa elementos similares y un diccionario liga nombres con valores. La estructura correcta baja errores porque el codigo recupera significado, no solo posicion.

## El codigo empieza a contestar

> **el mentor:** "Productos iran como diccionarios dentro de una lista."

> **Caro:** "Escribirlo toma mas lineas."

> **Rita:** "Leerlo toma menos adivinanza."

> **Caro:** "Y si alguien quiere saltarse ese paso."

> **Rita:** "Que primero explique que evidencia esta dispuesto a perder."

> **Samuel:** "La lista no estaba desordenada; estaba pidiendo identificacion oficial."

**Regla:** elige la estructura segun como necesitas guardar y recuperar el dato.
