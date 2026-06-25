# La maquina que obedecio demasiado literal

<!-- story
concept: instrucciones precisas para comunicarse con una maquina
characters: Nora, Hugo, Celia, la gerente
situation: un equipo pide a un sistema ordenar solicitudes con una frase ambigua
bad_logic: si una persona entiende la intencion, la maquina tambien la entiende
escalation: el sistema acomoda casos por texto literal y manda reclamos graves al final
data_turn: Nora compara instrucciones vagas contra instrucciones con criterio y salida esperada
chart: tabla de instrucciones y resultados
decision: escribir instrucciones con objetivo, datos de entrada, criterio y ejemplo de salida
punchline: La maquina si escucho; el problema es que nadie le dijo lo que querian.
rule: una maquina no adivina contexto; recibe instrucciones, datos y criterios
synthetic_data: true
-->

## El correo muy claro

> **Nora:** "Ya le pedi que atienda lo urgente primero."

> **Hugo:** "Urgente como palabra o urgente como riesgo real."

> **Celia:** "Como palabra. Es lo mismo, no."

> **Nora:** "Para nosotros si. Para el sistema no necesariamente."

> **Celia:** "Pero el mensaje decia clarito que priorizara urgencias."

> **la gerente:** "Y ahora tenemos casos graves esperando turno."

La sala todavia olia a cafe recalentado y a cierre de trimestre. Nadie habia
planeado discutir fundamentos; querian una solucion que cupiera en el correo de
seguimiento. El problema era que la frase corta habia salido barata al escribirla
y cara al operarla. Cada persona habia completado los huecos con su propia
costumbre, y la herramienta habia completado los huecos con lo unico que tenia:
instrucciones incompletas.

## La frase que todos entendian

> **Celia:** "Podemos poner urgentisimo para que entienda mejor."

> **Hugo:** "Eso solo grita mas fuerte la misma instruccion."

> **Celia:** "Entonces agregamos tres signos de admiracion."

> **la gerente:** "Ayer paso primero un folio que decia urgente en mayusculas."

> **Celia:** "Tambien era sobre globos de la oficina."

> **Nora:** "Y se quedo atras una cancelacion con dinero retenido."

> **Hugo:** "Entonces el atajo si tuvo costo, solo que en otro escritorio."

> **la gerente:** "Quiero saber exactamente donde se esta pagando."

La mala idea no nacio como capricho. Nacio como atajo razonable para quitar
presion, cerrar pendientes y poder decir en la siguiente junta que algo ya se
habia movido. Por eso sobrevivio mas de lo que merecia. Cada defensa resolvia
un pedazo visible y empujaba el costo a otro lugar: soporte, clientes,
revision, presupuesto o la persona que tendria que explicar el resultado con la
cara tranquila.

## Lo que la maquina si leyo

> **Nora:** "Separé lo que pedimos de lo que necesitabamos decidir."

> **la gerente:** "Ensename la diferencia sin poesia."

> **Nora:** "La version vaga ordena por palabra; la clara ordena por impacto."

> **Hugo:** "Eso explica por que la salida parecia correcta al principio."

> **Nora:** "Correcta para una pregunta que no era la importante."

<svg data-chart="central" viewBox="0 0 720 320" role="img" aria-label="tabla de instrucciones y resultados">
  <rect width="720" height="320" fill="#fff"/>
  <text x="36" y="32" font-size="18" font-weight="bold">tabla de instrucciones y resultados</text>
  <line x1="58" y1="260" x2="662" y2="260" stroke="#777" stroke-width="2"/>
  <rect x="70" y="190" width="174" height="70" fill="#286d9b"/>
  <text x="157" y="180" font-size="18" text-anchor="middle">38</text>
  <text x="157" y="286" font-size="13" text-anchor="middle">frase vaga</text>
  <rect x="272" y="100" width="174" height="160" fill="#d58b2f"/>
  <text x="359" y="90" font-size="18" text-anchor="middle">86</text>
  <text x="359" y="286" font-size="13" text-anchor="middle">con criterio</text>
  <rect x="474" y="85" width="174" height="175" fill="#4c8b63"/>
  <text x="561" y="75" font-size="18" text-anchor="middle">94</text>
  <text x="561" y="286" font-size="13" text-anchor="middle">con ejemplo</text>
  <text x="36" y="306" font-size="13" fill="#9f3625">La salida mejora cuando la instruccion dice como decidir.</text>
</svg>

<!-- learning:pause -->
> **Hugo:** "Si dos personas entienden la frase de formas distintas, que necesita la maquina para no inventar el criterio."

**Lo que muestra:** La evidencia separa texto, criterio y salida. La instruccion vaga produce una prioridad comoda pero equivocada; la instruccion completa define objetivo, datos disponibles y como debe verse la respuesta. Eso es especificar una tarea computable.

## Hablarle menos bonito y mas claro

> **la gerente:** "Desde hoy cada pedido lleva entrada, criterio y ejemplo."

> **la gerente:** "Tambien quiero responsable, criterio y evidencia de revision."

> **Celia:** "Va a tardar mas que escribir porfa arreglalo."

> **Nora:** "Y menos que explicar por que arreglo otra cosa."

> **Celia:** "Y si alguien pide excepcion."

> **Nora:** "Que la pida con costo visible y fecha."

> **la gerente:** "Y si no hay evidencia, no hay lanzamiento."

> **Hugo:** "Eso va a incomodar a la prisa."

> **Nora:** "La prisa ya nos estaba cobrando intereses."

> **Hugo:** "La maquina si escucho; el problema es que nadie le dijo lo que querian."

**Regla:** una maquina no adivina contexto; recibe instrucciones, datos y criterios.
