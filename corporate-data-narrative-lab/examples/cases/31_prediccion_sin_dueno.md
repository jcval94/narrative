# La prediccion que llego sin dueno

<!-- story
concept: propiedad operativa del producto de datos
characters: Monica, Esteban, Silvia, el sponsor
situation: un modelo entrega alertas diarias pero ningun equipo acepta operar la decision
bad_logic: si el dato llega a tiempo, alguien naturalmente lo usara
escalation: las alertas se reenvian entre areas hasta vencer
data_turn: Monica mide alertas recibidas, tomadas y cerradas por dueno
chart: uso real por area
decision: asignar dueno, horario, SLA y cierre de cada alerta
punchline: La prediccion era puntual; lo que llego tarde fue el organigrama.
rule: un producto de datos necesita dueno operativo antes de automatizar alertas
synthetic_data: true
-->

## La alerta impecable

> **Monica:** "Las alertas salen diario a primera hora."

> **Esteban:** "Y se contestan diario con esto no es mio."

> **Silvia:** "Tecnicamente llegan a tiempo."

> **Monica:** "Llegar no es aterrizar."

> **Silvia:** "El correo incluye a todas las areas relevantes."

> **el sponsor:** "Todas relevantes significa nadie responsable."

La sala todavia olia a cafe recalentado y a cierre de trimestre. Nadie habia
planeado discutir fundamentos; querian una solucion que cupiera en el correo de
seguimiento. El problema era que la frase corta habia salido barata al escribirla
y cara al operarla. Cada persona habia completado los huecos con su propia
costumbre, y la herramienta habia completado los huecos con lo unico que tenia:
instrucciones incompletas.

## El correo viajo mas que el caso

> **Silvia:** "Agregamos mas copias para que alguien reaccione."

> **Esteban:** "Mas copias no crean dueno."

> **Silvia:** "Pero aumentan la probabilidad de culpa."

> **el sponsor:** "Ayer una alerta dio cinco vueltas y caduco."

> **Silvia:** "Al menos todos estaban informados."

> **Monica:** "Informados de que nadie la tomo."

> **Esteban:** "Entonces el atajo si tuvo costo, solo que en otro escritorio."

> **el sponsor:** "Quiero saber exactamente donde se esta pagando."

La mala idea no nacio como capricho. Nacio como atajo razonable para quitar
presion, cerrar pendientes y poder decir en la siguiente junta que algo ya se
habia movido. Por eso sobrevivio mas de lo que merecia. Cada defensa resolvia
un pedazo visible y empujaba el costo a otro lugar: soporte, clientes,
revision, presupuesto o la persona que tendria que explicar el resultado con la
cara tranquila.

## Recibir no es hacerse cargo

> **Monica:** "Segui cada alerta hasta su cierre."

> **el sponsor:** "Cuantas pasan de recibidas a atendidas."

> **Monica:** "Las que tienen dueno sobreviven; las demas circulan."

> **Esteban:** "Eso explica por que la salida parecia correcta al principio."

> **Monica:** "Correcta para una pregunta que no era la importante."

<svg data-chart="central" viewBox="0 0 720 320" role="img" aria-label="uso real por area">
  <rect width="720" height="320" fill="#fff"/>
  <text x="36" y="32" font-size="18" font-weight="bold">uso real por area</text>
  <line x1="58" y1="260" x2="662" y2="260" stroke="#777" stroke-width="2"/>
  <rect x="70" y="85" width="124" height="175" fill="#286d9b"/>
  <text x="132" y="75" font-size="18" text-anchor="middle">100</text>
  <text x="132" y="286" font-size="13" text-anchor="middle">recibidas</text>
  <rect x="222" y="180" width="124" height="80" fill="#d58b2f"/>
  <text x="284" y="170" font-size="18" text-anchor="middle">46</text>
  <text x="284" y="286" font-size="13" text-anchor="middle">tomadas</text>
  <rect x="374" y="210" width="124" height="50" fill="#4c8b63"/>
  <text x="436" y="200" font-size="18" text-anchor="middle">29</text>
  <text x="436" y="286" font-size="13" text-anchor="middle">cerradas</text>
  <rect x="526" y="131" width="124" height="129" fill="#c64e36"/>
  <text x="588" y="121" font-size="18" text-anchor="middle">74</text>
  <text x="588" y="286" font-size="13" text-anchor="middle">con dueno</text>
  <text x="36" y="306" font-size="13" fill="#9f3625">El dueno operativo cambia el uso real.</text>
</svg>

<!-- learning:pause -->
> **Esteban:** "Que elemento operativo falta cuando una prediccion correcta no cambia nada."

**Lo que muestra:** La grafica separa entrega, toma de responsabilidad y cierre. Una alerta puede ser tecnicamente correcta y aun asi inutil si no tiene dueno, horario, criterio de accion y seguimiento. El producto de datos incluye operacion.

## El dueno aparece antes de la alarma

> **el sponsor:** "Cada alerta tendra dueno y tiempo de respuesta."

> **el sponsor:** "Tambien quiero responsable, criterio y evidencia de revision."

> **Silvia:** "Menos personas recibiran el correo."

> **Monica:** "Y por fin alguien lo contestara con accion."

> **Silvia:** "Y si alguien pide excepcion."

> **Monica:** "Que la pida con costo visible y fecha."

> **el sponsor:** "Y si no hay evidencia, no hay lanzamiento."

> **Esteban:** "Eso va a incomodar a la prisa."

> **Monica:** "La prisa ya nos estaba cobrando intereses."

> **Esteban:** "La prediccion era puntual; lo que llego tarde fue el organigrama."

**Regla:** un producto de datos necesita dueno operativo antes de automatizar alertas.
