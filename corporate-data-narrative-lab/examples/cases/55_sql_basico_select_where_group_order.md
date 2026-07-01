# La consulta que trajo toda la tienda

<!-- story
concept: SQL basico con SELECT, WHERE, GROUP BY y ORDER BY
characters: Meli, Sergio, Paula, el gerente
situation: SQL y Datos se enseña mediante una decision practica que necesita codigo o datos bien definidos
bad_logic: pedir todos los datos primero y pensar despues es mas rapido
escalation: la consulta devuelve filas innecesarias y una conclusion sin agrupar
data_turn: una persona compara el atajo contra una version verificable
chart: filas consultadas contra respuesta necesaria
decision: seleccionar columnas, filtrar filas, agrupar ventas y ordenar resultados
punchline: La consulta no respondio la pregunta; trajo la tienda completa para que la entrevistaramos.
rule: una consulta basica debe pedir solo las columnas, filas y agrupaciones que responden la pregunta
synthetic_data: true
-->

## Todo por si acaso

> **Meli:** "Hice SELECT estrella para revisar ventas."

> **Sergio:** "Eso trajo columnas que nadie pidio."

> **Paula:** "Mejor tener todo por si acaso."

> **Meli:** "Por si acaso no es una pregunta de negocio."

> **Paula:** "Querian saber productos mas vendidos."

> **el gerente:** "Entonces faltaba filtrar, agrupar y ordenar."

La clase no se atoro por falta de ganas. Se atoro porque una idea razonable se
habia quedado a medio camino entre conversacion y procedimiento. En la mesa ya
habia prisa, capturas abiertas y alguien diciendo que lo importante era avanzar.
Por eso el error parecia pequeno: no rompia la historia completa, solo la parte
donde la maquina tenia que entender exactamente que hacer.

## La tabla no era la respuesta

> **Paula:** "Abrimos la tabla y buscamos a ojo."

> **Sergio:** "Eso convierte SQL en vitrina."

> **Paula:** "Podemos ordenar en Excel despues."

> **el gerente:** "Despues siempre llega con otro despues."

> **Paula:** "La consulta si corrio."

> **Meli:** "Correr no es responder."

> **Sergio:** "Entonces el atajo si hizo trabajo, solo que no el trabajo correcto."

> **el gerente:** "Quiero ver donde se separa la intuicion del resultado."

La solucion comoda tenia una virtud: se podia explicar en una frase. El problema
era que tambien escondia entradas, reglas y excepciones. Cuando el grupo la
siguio dos pasos mas, aparecio lo de siempre: una salida que parecia formal, una
persona intentando defenderla y otra buscando el dato exacto donde la historia
dejaba de sostenerse.

## Cuatro palabras que ordenan la pregunta

> **Meli:** "Compare la consulta completa contra una consulta enfocada."

> **el gerente:** "Cuantas filas necesitabamos leer."

> **Meli:** "Muchas menos cuando la pregunta guia SELECT y WHERE."

> **Sergio:** "Eso cambia lo que tenemos que enseñar."

> **Meli:** "Si. Primero la regla humana, luego la forma tecnica."

<svg data-chart="central" viewBox="0 0 720 320" role="img" aria-label="filas consultadas contra respuesta necesaria">
  <rect width="720" height="320" fill="#fff"/>
  <text x="36" y="32" font-size="18" font-weight="bold">filas consultadas contra respuesta necesaria</text>
  <line x1="58" y1="260" x2="662" y2="260" stroke="#777" stroke-width="2"/>
  <rect x="70" y="226" width="174" height="34" fill="#286d9b"/>
  <text x="157" y="216" font-size="18" text-anchor="middle">18</text>
  <text x="157" y="286" font-size="13" text-anchor="middle">todo</text>
  <rect x="272" y="143" width="174" height="117" fill="#d58b2f"/>
  <text x="359" y="133" font-size="18" text-anchor="middle">61</text>
  <text x="359" y="286" font-size="13" text-anchor="middle">filtrado</text>
  <rect x="474" y="85" width="174" height="175" fill="#4c8b63"/>
  <text x="561" y="75" font-size="18" text-anchor="middle">91</text>
  <text x="561" y="286" font-size="13" text-anchor="middle">agrupado</text>
  <text x="36" y="306" font-size="13" fill="#9f3625">Filtrar y agrupar acerca la consulta a la pregunta.</text>
</svg>

<!-- learning:pause -->
> **Sergio:** "Como se conectan SELECT, WHERE, GROUP BY y ORDER BY en una pregunta simple."

**Lo que muestra:** La evidencia muestra que SQL basico no es traer todo. SELECT elige columnas, WHERE filtra filas, GROUP BY resume y ORDER BY ordena la respuesta. La consulta debe parecerse a la decision que quieres tomar.

## La consulta deja de cargar cajas

> **el gerente:** "La pregunta se escribira antes de la consulta."

> **Paula:** "Ya no tendremos todo por si acaso."

> **Meli:** "Y tendremos algo que si contesta."

> **Paula:** "Y si alguien quiere saltarse ese paso."

> **Meli:** "Que primero explique que evidencia esta dispuesto a perder."

> **Sergio:** "La consulta no respondio la pregunta; trajo la tienda completa para que la entrevistaramos."

**Regla:** una consulta basica debe pedir solo las columnas, filas y agrupaciones que responden la pregunta.
