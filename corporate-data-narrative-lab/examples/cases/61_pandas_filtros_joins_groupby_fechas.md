# El groupby que perdio los lunes

<!-- story
concept: pandas esencial con filtros, joins, groupby y fechas
characters: Olga, Ivan, Ceci, el mentor
situation: Lectura y Limpieza se enseña mediante una decision practica que necesita codigo o datos bien definidos
bad_logic: si pandas devuelve una tabla, la transformacion quedo bien
escalation: un filtro de fechas mal convertido excluye dias y el resumen cambia
data_turn: una persona compara el atajo contra una version verificable
chart: filas antes y despues de filtros de fecha
decision: convertir tipos, filtrar explicitamente, unir con llaves y agrupar despues de validar
punchline: Pandas no odio los lunes; nosotros los dejamos como texto.
rule: en pandas, valida tipos y filas antes de confiar en filtros, joins o groupby
synthetic_data: true
-->

## La tabla bonita

> **Olga:** "El groupby ya resume ventas por dia."

> **Ivan:** "Pero faltan varios lunes."

> **Ceci:** "Tal vez esos dias no hubo ventas."

> **Olga:** "O la fecha no era fecha."

> **Ceci:** "Pandas no se quejo."

> **el mentor:** "Pandas no siempre se queja por ti."

La clase no se atoro por falta de ganas. Se atoro porque una idea razonable se
habia quedado a medio camino entre conversacion y procedimiento. En la mesa ya
habia prisa, capturas abiertas y alguien diciendo que lo importante era avanzar.
Por eso el error parecia pequeno: no rompia la historia completa, solo la parte
donde la maquina tenia que entender exactamente que hacer.

## La fecha era texto disfrazado

> **Ceci:** "Rellenamos los lunes con cero."

> **Ivan:** "Primero averigüemos si los borramos."

> **Ceci:** "El cero se ve ordenado."

> **el mentor:** "Ordenado y falso es peor."

> **Ceci:** "La grafica quedaba suave."

> **Olga:** "Demasiado suave para una semana real."

> **Ivan:** "Entonces el atajo si hizo trabajo, solo que no el trabajo correcto."

> **el mentor:** "Quiero ver donde se separa la intuicion del resultado."

La solucion comoda tenia una virtud: se podia explicar en una frase. El problema
era que tambien escondia entradas, reglas y excepciones. Cuando el grupo la
siguio dos pasos mas, aparecio lo de siempre: una salida que parecia formal, una
persona intentando defenderla y otra buscando el dato exacto donde la historia
dejaba de sostenerse.

## Filtrar despues de convertir

> **Olga:** "Revise tipos, filtros y filas antes del groupby."

> **el mentor:** "Donde se fueron los lunes."

> **Olga:** "Se perdieron al filtrar texto como si fuera fecha."

> **Ivan:** "Eso cambia lo que tenemos que enseñar."

> **Olga:** "Si. Primero la regla humana, luego la forma tecnica."

<svg data-chart="central" viewBox="0 0 720 320" role="img" aria-label="filas antes y despues de filtros de fecha">
  <rect width="720" height="320" fill="#fff"/>
  <text x="36" y="32" font-size="18" font-weight="bold">filas antes y despues de filtros de fecha</text>
  <line x1="58" y1="260" x2="662" y2="260" stroke="#777" stroke-width="2"/>
  <rect x="70" y="160" width="174" height="100" fill="#286d9b"/>
  <text x="157" y="150" font-size="18" text-anchor="middle">52</text>
  <text x="157" y="286" font-size="13" text-anchor="middle">sin validar</text>
  <rect x="272" y="101" width="174" height="159" fill="#d58b2f"/>
  <text x="359" y="91" font-size="18" text-anchor="middle">83</text>
  <text x="359" y="286" font-size="13" text-anchor="middle">fechas ok</text>
  <rect x="474" y="85" width="174" height="175" fill="#4c8b63"/>
  <text x="561" y="75" font-size="18" text-anchor="middle">91</text>
  <text x="561" y="286" font-size="13" text-anchor="middle">join validado</text>
  <text x="36" y="306" font-size="13" fill="#9f3625">Los tipos correctos protegen el resumen.</text>
</svg>

<!-- learning:pause -->
> **Ivan:** "Que validaciones conviene hacer antes de usar filtros, joins y groupby en pandas."

**Lo que muestra:** La evidencia muestra que pandas permite transformar rapido, pero exige revisar tipos, nulos, llaves y conteos. Convertir fechas antes de filtrar evita excluir datos validos. El groupby solo resume lo que sobrevivio.

## Agrupar con piso firme

> **el mentor:** "El flujo validara tipos y conteos antes de resumir."

> **Ceci:** "Habra mas pasos antes de la grafica."

> **Olga:** "Y menos dias desaparecidos."

> **Ceci:** "Y si alguien quiere saltarse ese paso."

> **Olga:** "Que primero explique que evidencia esta dispuesto a perder."

> **Ivan:** "Pandas no odio los lunes; nosotros los dejamos como texto."

**Regla:** en pandas, valida tipos y filas antes de confiar en filtros, joins o groupby.
