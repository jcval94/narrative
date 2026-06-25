# El loop que mando el mismo aviso a todos

<!-- story
concept: condicionales, loops y logica de automatizacion
characters: Nico, Irene, Joel, la coordinadora
situation: Programacion en Python se enseña mediante una decision practica que necesita codigo o datos bien definidos
bad_logic: automatizar una repeticion basta aunque no separe casos distintos
escalation: el loop procesa todo igual y manda avisos incorrectos
data_turn: una persona compara el atajo contra una version verificable
chart: casos procesados con y sin condicion
decision: agregar condiciones antes de repetir acciones
punchline: El loop trabajo muchisimo; el problema es que nunca pregunto a quien.
rule: un loop repite, pero la condicion decide cuando debe cambiar el camino
synthetic_data: true
-->

## La automatizacion obediente

> **Nico:** "El script ya recorre todos los registros."

> **Irene:** "Tambien les manda el mismo aviso a todos."

> **Joel:** "Eso era la automatizacion."

> **Nico:** "Eso era repeticion, no criterio."

> **Joel:** "Antes lo haciamos a mano."

> **la coordinadora:** "A mano al menos alguien distinguia pendientes de cerrados."

La clase no se atoro por falta de ganas. Se atoro porque una idea razonable se
habia quedado a medio camino entre conversacion y procedimiento. En la mesa ya
habia prisa, capturas abiertas y alguien diciendo que lo importante era avanzar.
Por eso el error parecia pequeno: no rompia la historia completa, solo la parte
donde la maquina tenia que entender exactamente que hacer.

## Repetir no es decidir

> **Joel:** "Hacemos dos scripts, uno para cada caso."

> **Irene:** "Mejor una condicion dentro del loop."

> **Joel:** "Pero dos scripts se sienten mas productivos."

> **la coordinadora:** "Y duplican el lugar donde equivocarnos."

> **Joel:** "El correo generico es educado."

> **Nico:** "Educado y falso sigue siendo falso."

> **Irene:** "Entonces el atajo si hizo trabajo, solo que no el trabajo correcto."

> **la coordinadora:** "Quiero ver donde se separa la intuicion del resultado."

La solucion comoda tenia una virtud: se podia explicar en una frase. El problema
era que tambien escondia entradas, reglas y excepciones. Cuando el grupo la
siguio dos pasos mas, aparecio lo de siempre: una salida que parecia formal, una
persona intentando defenderla y otra buscando el dato exacto donde la historia
dejaba de sostenerse.

## La pregunta antes de la vuelta

> **Nico:** "Compare registros procesados antes y despues del if."

> **la coordinadora:** "Cuantos avisos dejaron de salir mal."

> **Nico:** "La condicion separo quien necesitaba accion y quien no."

> **Irene:** "Eso cambia lo que tenemos que enseñar."

> **Nico:** "Si. Primero la regla humana, luego la forma tecnica."

<svg data-chart="central" viewBox="0 0 720 320" role="img" aria-label="casos procesados con y sin condicion">
  <rect width="720" height="320" fill="#fff"/>
  <text x="36" y="32" font-size="18" font-weight="bold">casos procesados con y sin condicion</text>
  <line x1="58" y1="260" x2="662" y2="260" stroke="#777" stroke-width="2"/>
  <rect x="70" y="188" width="174" height="72" fill="#286d9b"/>
  <text x="157" y="178" font-size="18" text-anchor="middle">39</text>
  <text x="157" y="286" font-size="13" text-anchor="middle">sin if</text>
  <rect x="272" y="147" width="174" height="113" fill="#d58b2f"/>
  <text x="359" y="137" font-size="18" text-anchor="middle">61</text>
  <text x="359" y="286" font-size="13" text-anchor="middle">dos scripts</text>
  <rect x="474" y="85" width="174" height="175" fill="#4c8b63"/>
  <text x="561" y="75" font-size="18" text-anchor="middle">94</text>
  <text x="561" y="286" font-size="13" text-anchor="middle">loop con if</text>
  <text x="36" y="306" font-size="13" fill="#9f3625">La condicion evita repetir el error.</text>
</svg>

<!-- learning:pause -->
> **Irene:** "Que papel tiene un if dentro de un loop de automatizacion."

**Lo que muestra:** La evidencia muestra que repetir sin logica amplifica errores. El loop permite recorrer muchos registros; el condicional decide que accion corresponde en cada caso. Automatizar bien no es hacer mas, es hacer lo correcto muchas veces.

## Menos correos, mas logica

> **la coordinadora:** "El loop solo enviara aviso si el estado lo requiere."

> **Joel:** "Hay que escribir la regla completa."

> **Nico:** "Y dejar de molestar a quien ya termino."

> **Joel:** "Y si alguien quiere saltarse ese paso."

> **Nico:** "Que primero explique que evidencia esta dispuesto a perder."

> **Irene:** "El loop trabajo muchisimo; el problema es que nunca pregunto a quien."

**Regla:** un loop repite, pero la condicion decide cuando debe cambiar el camino.
