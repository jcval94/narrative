# Las primeras runas y el archivo que hablaba raro

<!-- story
concept: lectura de CSV, Excel, JSON y APIs
characters: Mora, Diego, Vicky, la instructora
situation: Lectura y Limpieza se enseña mediante una decision practica que necesita codigo o datos bien definidos
bad_logic: todos los datos se leen igual si al final parecen tabla
escalation: se mezclan separadores, hojas, objetos anidados y respuestas de API sin validar
data_turn: una persona compara el atajo contra una version verificable
chart: fuentes leidas con validacion de formato
decision: elegir lector por formato y validar filas, columnas y tipos al entrar
punchline: El CSV no estaba poseido; solo venia con separador regional.
rule: leer datos empieza por reconocer formato, estructura y validaciones basicas
synthetic_data: true
-->

## El archivo con runas

> **Mora:** "El CSV se abrio todo en una sola columna."

> **Diego:** "Probablemente usa otro separador."

> **Vicky:** "Pero es archivo de datos."

> **Mora:** "Datos no significa mismo idioma."

> **Vicky:** "Excel si lo abre."

> **la instructora:** "Excel adivina cosas que Python necesita explicitas."

La clase no se atoro por falta de ganas. Se atoro porque una idea razonable se
habia quedado a medio camino entre conversacion y procedimiento. En la mesa ya
habia prisa, capturas abiertas y alguien diciendo que lo importante era avanzar.
Por eso el error parecia pequeno: no rompia la historia completa, solo la parte
donde la maquina tenia que entender exactamente que hacer.

## No todo es tabla al nacer

> **Vicky:** "Copiamos y pegamos a mano."

> **Diego:** "Eso convierte lectura en artesania."

> **Vicky:** "Podemos hacerlo solo esta vez."

> **la instructora:** "Esa frase funda muchos procesos eternos."

> **Vicky:** "JSON y API tambien parecen convertibles."

> **Mora:** "Primero hay que entender como vienen."

> **Diego:** "Entonces el atajo si hizo trabajo, solo que no el trabajo correcto."

> **la instructora:** "Quiero ver donde se separa la intuicion del resultado."

La solucion comoda tenia una virtud: se podia explicar en una frase. El problema
era que tambien escondia entradas, reglas y excepciones. Cuando el grupo la
siguio dos pasos mas, aparecio lo de siempre: una salida que parecia formal, una
persona intentando defenderla y otra buscando el dato exacto donde la historia
dejaba de sostenerse.

## Cada fuente pide su llave

> **Mora:** "Probe lectores por formato y valide la entrada."

> **la instructora:** "Que fuentes entran correctamente."

> **Mora:** "Las que usan el lector y parametros correctos."

> **Diego:** "Eso cambia lo que tenemos que enseñar."

> **Mora:** "Si. Primero la regla humana, luego la forma tecnica."

<svg data-chart="central" viewBox="0 0 720 320" role="img" aria-label="fuentes leidas con validacion de formato">
  <rect width="720" height="320" fill="#fff"/>
  <text x="36" y="32" font-size="18" font-weight="bold">fuentes leidas con validacion de formato</text>
  <line x1="58" y1="260" x2="662" y2="260" stroke="#777" stroke-width="2"/>
  <rect x="70" y="200" width="174" height="60" fill="#286d9b"/>
  <text x="157" y="190" font-size="18" text-anchor="middle">33</text>
  <text x="157" y="286" font-size="13" text-anchor="middle">adivinar</text>
  <rect x="272" y="118" width="174" height="142" fill="#d58b2f"/>
  <text x="359" y="108" font-size="18" text-anchor="middle">78</text>
  <text x="359" y="286" font-size="13" text-anchor="middle">lector correcto</text>
  <rect x="474" y="85" width="174" height="175" fill="#4c8b63"/>
  <text x="561" y="75" font-size="18" text-anchor="middle">96</text>
  <text x="561" y="286" font-size="13" text-anchor="middle">validado</text>
  <text x="36" y="306" font-size="13" fill="#9f3625">La validacion confirma que la fuente entro bien.</text>
</svg>

<!-- learning:pause -->
> **Diego:** "Que debes revisar al leer CSV, Excel, JSON o una API por primera vez."

**Lo que muestra:** La evidencia separa formato y validacion. CSV necesita separador y encoding, Excel hoja y encabezados, JSON estructura anidada y API estado de respuesta. Leer bien evita limpiar errores creados al importar.

## Leer antes de limpiar

> **la instructora:** "Cada fuente tendra funcion de lectura y validacion inicial."

> **Vicky:** "La primera celda sera mas cuidadosa."

> **Mora:** "Y menos mistica."

> **Vicky:** "Y si alguien quiere saltarse ese paso."

> **Mora:** "Que primero explique que evidencia esta dispuesto a perder."

> **Diego:** "Tambien podremos repetirla mañana."

> **Mora:** "Exacto. Leer datos no deberia depender del humor del archivo."

> **la instructora:** "Ni del pulso de quien copia y pega."

> **Diego:** "El CSV no estaba poseido; solo venia con separador regional."

**Regla:** leer datos empieza por reconocer formato, estructura y validaciones basicas.
